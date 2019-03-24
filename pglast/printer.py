# -*- coding: utf-8 -*-
# :Project:   pglast -- Serialization logic
# :Created:   mer 02 ago 2017 15:46:11 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019 Lele Gaifax
#

from contextlib import contextmanager
from io import StringIO
from re import match

from .error import Error
from .node import List, Node, Scalar
from .keywords import RESERVED_KEYWORDS
from .parser import parse_plpgsql, parse_sql


NODE_PRINTERS = {}
"Registry of specialized printers, keyed by their `tag`."


SPECIAL_FUNCTIONS = {}
"Registry of specialized function printers, keyed by their qualified name."


class PrinterAlreadyPresentError(Error):
    "Exception raised trying to register another function for a tag already present."


def get_printer_for_node_tag(parent_node_tag, node_tag):
    """Get specific printer implementation for given `node_tag`.

    If there is a more specific printer for it, when it's inside a particular
    `parent_node_tag`, return that instead.
    """

    try:
        return NODE_PRINTERS[(parent_node_tag, node_tag)]
    except KeyError:
        try:
            return NODE_PRINTERS[node_tag]
        except KeyError:
            raise NotImplementedError("Printer for node %r is not implemented yet"
                                      % node_tag)


def node_printer(*node_tags, override=False):
    """Decorator to register a specific printer implementation for given `node_tag`.

    :param \*node_tags: one or two node tags
    :param bool override:
           when ``True`` the function will be registered even if already present in the
           :data:`NODE_PRINTERS` registry

    When `node_tags` contains a single item then the decorated function is the *generic* one,
    and it will be registered in :data:`NODE_PRINTERS` with that key alone. Otherwise it must
    contain two elements: the first may be either a scalar value or a sequence of parent tags,
    and the function will be registered under the key ``(parent_tag, tag)``.
    """

    def decorator(impl):
        if len(node_tags) == 1:
            parent_tags = (None,)
            tag = node_tags[0]
        elif len(node_tags) == 2:
            parent_tags, tag = node_tags
            if not isinstance(parent_tags, (list, tuple)):
                parent_tags = (parent_tags,)
        else:
            raise ValueError("Must specify one or two tags, got %d instead" % len(node_tags))

        for parent_tag in parent_tags:
            t = tag if parent_tag is None else (parent_tag, tag)
            if not override and t in NODE_PRINTERS:
                raise PrinterAlreadyPresentError("A printer is already registered for tag %r"
                                                 % t)
            NODE_PRINTERS[t] = impl
        return impl
    return decorator


def special_function(name, override=False):
    """Decorator to declare a particular PostgreSQL function `name` as *special*, with a
    specific printer.

    :param str name: the qualified name of the PG function
    :param bool override: when ``True`` the function will be registered even if already
                          present in the :data:`SPECIAL_FUNCTIONS` registry
    """

    def decorator(impl):
        if not override and name in SPECIAL_FUNCTIONS:
            raise PrinterAlreadyPresentError("A printer is already registered for function %r"
                                             % name)
        SPECIAL_FUNCTIONS[name] = impl
        return impl
    return decorator


class OutputStream(StringIO):
    "A stream that has a concept of a *pending separator* between consecutive writes."

    def __init__(self):
        super().__init__()
        self.pending_separator = False
        self.last_emitted_char = ' '

    def separator(self):
        """Possibly insert a single whitespace character before next output.

        When the last character written is not a space, set the `pending_separator` flag to
        ``True``: the next call to :meth:`write` will prepend a single whitespace to its
        argument if that begins with an alphanumeric character.
        """

        if not self.last_emitted_char.isspace():
            self.pending_separator = True

    def maybe_write_space(self, nextc=None, _special_chars=set("""_*+/-"'=<>$@""")):
        """Emit a space when needed.

        :param nextc: either None or the next character that will be written
        :return: the number of characters written to the stream

        If the last character written was not a space, and `nextc` is either ``None`` or
        a *special character*, then emit a single whitespace.
        """

        if not self.last_emitted_char.isspace():
            if nextc is None or nextc.isalnum() or nextc in _special_chars:
                return self.write(' ')
        return 0

    def write(self, s):
        """Emit string `s`.

        :param str s: the string to emit
        :return: the number of characters written to the stream

        When `s` is not empty and `pending_separator` is ``True`` and the first character of
        `s` is alphanumeric, emit a single whitespace before writing out `s` and then reset
        `pending_separator` to ``False``.
        """

        count = 0
        if s:
            if self.pending_separator:
                if s != ' ':
                    self.maybe_write_space(s[0])
                self.pending_separator = False
            count = super().write(s)
            self.last_emitted_char = s[-1]

        return count

    def writes(self, s):
        "Shortcut for ``self.write(s); self.separator()``."

        count = self.write(s)
        self.separator()
        return count

    def swrite(self, s):
        "Shortcut for ``self.maybe_write_space(s[0]); self.write(s)``."

        count = self.maybe_write_space(s[0])
        return count + self.write(s)

    def swrites(self, s):
        "Shortcut for ``self.swrite(s); self.separator()``."

        count = self.swrite(s)
        self.separator()
        return count


class RawStream(OutputStream):
    """Basic SQL parse tree writer.

    :param int expression_level:
           start the stream with the given expression level depth, 0 by default
    :param bool separate_statements:
           ``True`` by default, tells whether multiple statements shall be separated by an
           empty line
    :param bool special_functions:
           ``False`` by default, when ``True`` some functions are treated in a special way and
           emitted as equivalent constructs
    :param bool comma_at_eoln:
           ``False`` by default, when ``True`` put the comma right after each item instead of
           at the beginning of the *next* item line

    This augments :class:`OutputStream` and implements the basic machinery needed to serialize
    the *parse tree* produced by :func:`~.parser.parse_sql()` back to a textual representation,
    without any adornment.
    """

    def __init__(self, expression_level=0, separate_statements=True, special_functions=False,
                 comma_at_eoln=False):
        super().__init__()
        self.expression_level = expression_level
        self.separate_statements = separate_statements
        self.special_functions = special_functions
        self.comma_at_eoln = comma_at_eoln
        self.current_column = 0

    def __call__(self, sql, plpgsql=False):
        """Main entry point: execute :meth:`print_node` on each statement in `sql`.

        :param sql: either the source SQL in textual form, or a :class:`~.node.Node` instance
        :param bool plpgsql: whether `sql` is really a ``plpgsql`` statement
        :returns: a string with the equivalent SQL obtained by serializing the syntax tree
        """

        if isinstance(sql, str):
            sql = Node(parse_plpgsql(sql) if plpgsql else parse_sql(sql))
        elif isinstance(sql, Node):
            sql = [sql]
        elif not isinstance(sql, List):
            raise ValueError("Unexpected value for 'sql', must be either a string,"
                             " a Node instance or a List instance, got %r" % type(sql))

        first = True
        for statement in sql:
            if first:
                first = False
            else:
                self.write(';')
                self.newline()
                if self.separate_statements:
                    self.newline()
            self.print_node(statement)
        return self.getvalue()

    def dedent(self):
        "Do nothing, shall be overridden by the prettifier subclass."

    def get_printer_for_function(self, name):
        """Look for a specific printer for function `name` in :data:`SPECIAL_FUNCTIONS`.

        :param str name: the qualified name of the function
        :returns: either ``None`` or a callable

        When the option `special_functions` is ``True``, return the printer function associated
        with `name`, if present. In all other cases return ``None``.
        """

        if self.special_functions:
            return SPECIAL_FUNCTIONS.get(name)

    def indent(self, amount=0, relative=True):
        "Do nothing, shall be overridden by the prettifier subclass."

    def newline(self):
        "Emit a single whitespace, shall be overridden by the prettifier subclass."

        self.separator()

    def space(self, count=1):
        "Emit a single whitespace, shall be overridden by the prettifier subclass."

        self.separator()

    @contextmanager
    def push_indent(self, amount=0, relative=True):
        "Create a no-op context manager, shall be overridden by the prettifier subclass."

        yield

    @contextmanager
    def expression(self):
        "Create a context manager that will wrap subexpressions within parentheses."

        self.expression_level += 1
        if self.expression_level > 1:
            self.write('(')
        yield
        if self.expression_level > 1:
            self.write(')')
        self.expression_level -= 1

    def _concat_nodes(self, nodes, sep=' ', are_names=False):
        """Concatenate given `nodes`, using `sep` as the separator.

        :param scalars: a sequence of nodes
        :param str sep: the separator between them
        :param bool are_names:
               whether the nodes are actually *names*, which possibly require to be enclosed
               between double-quotes
        :returns: a string

        Use a temporary :class:`RawStream` instance to print the list of nodes and return the
        result.
        """

        rawstream = RawStream(expression_level=self.expression_level)
        rawstream.print_list(nodes, sep, are_names=are_names, standalone_items=False)
        return rawstream.getvalue()

    def _write_quoted_string(self, s):
        "Emit the `s` as a single-quoted literal constant."

        self.write("'%s'" % s.replace("'", "''"))

    def _print_scalar(self, node, is_name, is_symbol):
        "Print the scalar `node`, special-casing string literals."

        value = node.value
        if is_symbol:
            self.write(value)
        elif is_name:
            # The `scalar` represent a name of a column/table/alias: when any of its
            # characters is not a lower case letter, a digit or underscore, it must be
            # double quoted
            if not match(r'[a-z_][a-z0-9_]*$', value) or value in RESERVED_KEYWORDS:
                value = '"%s"' % value.replace('"', '""')
            self.write(value)
        elif node.parent_node.node_tag == 'String':
            self._write_quoted_string(value)
        else:
            self.write(str(value))

    def print_name(self, nodes, sep='.'):
        "Helper method, execute :meth:`print_node` or :meth:`print_list` as needed."

        if isinstance(nodes, (List, list)):
            self.print_list(nodes, sep, standalone_items=False, are_names=True)
        else:
            self.print_node(nodes, is_name=True)

    def print_symbol(self, nodes, sep='.'):
        "Helper method, execute :meth:`print_node` or :meth:`print_list` as needed."

        if isinstance(nodes, (List, list)):
            self.print_list(nodes, sep, standalone_items=False, are_names=True, is_symbol=True)
        else:
            self.print_node(nodes, is_name=True, is_symbol=True)

    def print_node(self, node, is_name=False, is_symbol=False):
        """Lookup the specific printer for the given `node` and execute it.

        :param node: an instance of :class:`~.node.Node` or :class:`~.node.Scalar`
        :param bool is_name:
               whether this is a *name* of something, that may need to be double quoted
        :param bool is_symbol:
               whether this is the name of an *operator*, should not be double quoted
        """

        if isinstance(node, Scalar):
            self._print_scalar(node, is_name, is_symbol)
        elif is_name and isinstance(node, (List, list)):
            self.print_list(node, '.', standalone_items=False, are_names=True)
        else:
            parent_node_tag = node.parent_node and node.parent_node.node_tag
            printer = get_printer_for_node_tag(parent_node_tag, node.node_tag)
            if is_name and node.node_tag == 'String':
                printer(node, self, is_name=is_name, is_symbol=is_symbol)
            else:
                printer(node, self)
        self.separator()

    def _print_items(self, items, sep, newline, are_names=False, is_symbol=False):
        last = len(items) - 1
        for idx, item in enumerate(items):
            if idx > 0:
                if sep == ',' and self.comma_at_eoln:
                    self.write(sep)
                    if newline:
                        self.newline()
                    else:
                        self.write(' ')
                else:
                    if not are_names:
                        if newline:
                            self.newline()
                    if sep:
                        self.write(sep)
                        if sep != '.':
                            self.write(' ')
            self.print_node(item, is_name=are_names, is_symbol=is_symbol and idx == last)

    def print_list(self, nodes, sep=',', relative_indent=None, standalone_items=None,
                   are_names=False, is_symbol=False):
        """Execute :meth:`print_node` on all the `nodes`, separating them with `sep`.

        :param nodes: a sequence of :class:`~.node.Node` instances
        :param str sep: the separator between them
        :param bool relative_indent:
               if given, the relative amount of indentation to apply before the first item, by
               default computed automatically from the length of the separator `sep`
        :param bool standalone_items: whether a newline will be emitted before each item
        :param bool are_names:
               whether the nodes are actually *names*, which possibly require to be enclosed
               between double-quotes
        :param bool is_symbol:
               whether the nodes are actually a *symbol* such as an *operator name*, in which
               case the last one must be printed verbatim (e.g. ``"MySchema".===``)
        """

        if relative_indent is None:
            if are_names or is_symbol:
                relative_indent = 0
            else:
                relative_indent = (-(len(sep) + 1)
                                   if sep and (sep != ',' or not self.comma_at_eoln)
                                   else 0)

        if standalone_items is None:
            standalone_items = not all(isinstance(n, Node)
                                       and n.node_tag in ('A_Const', 'ColumnRef',
                                                          'SetToDefault', 'RangeVar')
                                       for n in nodes)

        with self.push_indent(relative_indent):
            self._print_items(nodes, sep, standalone_items, are_names=are_names,
                              is_symbol=is_symbol)

    def print_lists(self, lists, sep=',', relative_indent=None, standalone_items=None,
                    are_names=False, sublist_open='(', sublist_close=')', sublist_sep=',',
                    sublist_relative_indent=None):
        """Execute :meth:`print_list` on all the `lists` items.

        :param lists: a sequence of sequences of :class:`~.node.Node` instances
        :param str sep: passed as is to :meth:`print_list`
        :param bool relative_indent: passed as is to :meth:`print_list`
        :param bool standalone_items: passed as is to :meth:`print_list`
        :param bool are_names: passed as is to :meth:`print_list`
        :param str sublist_open: the string that will be emitted before each sublist
        :param str sublist_close: the string that will be emitted after each sublist
        :param str sublist_sep: the separator between them each sublist
        :param bool sublist_relative_indent:
               if given, the relative amount of indentation to apply before the first sublist,
               by default computed automatically from the length of the separator `sublist_sep`
        """

        if sublist_relative_indent is None:
            sublist_relative_indent = (-(len(sublist_sep) + 1)
                                       if sublist_sep and (sublist_sep != ','
                                                           or not self.comma_at_eoln)
                                       else 0)

        with self.push_indent(sublist_relative_indent):
            self.write(sublist_open)
            first = True
            for lst in lists:
                if first:
                    first = False
                else:
                    if self.comma_at_eoln:
                        self.write(sublist_sep)
                        self.newline()
                        self.write(sublist_open)
                    else:
                        self.newline()
                        self.write(sublist_sep)
                        self.write(' ')
                        self.write(sublist_open)
                self.print_list(lst, sep, relative_indent, standalone_items, are_names)
                self.write(sublist_close)


class IndentedStream(RawStream):
    """Indented SQL parse tree writer.

    :param int compact_lists_margin:
           an integer value that, if given, is used to print lists on a single line, when they
           do not exceed the given margin on the right
    :param int split_string_literals_threshold:
           an integer value that, if given, is used as the threshold beyond that a string
           literal gets splitted in successive chunks of that length
    :param \*\*options: other options accepted by :class:`RawStream`

    This augments :class:`RawStream` to emit a prettified representation of a *parse tree*.
    """

    def __init__(self, compact_lists_margin=None, split_string_literals_threshold=None,
                 **options):
        super().__init__(**options)
        self.compact_lists_margin = compact_lists_margin
        self.split_string_literals_threshold = split_string_literals_threshold
        self.current_indent = 0
        self.indentation_stack = []

    def dedent(self):
        "Pop the indentation level from the stack and set `current_indent` to that."

        self.current_indent = self.indentation_stack.pop()

    def indent(self, amount=0, relative=True):
        """Push current indentation level to the stack, then set it adding `amount` to the
        `current_column` if `relative` is ``True`` otherwise to `current_indent`.
        """

        self.indentation_stack.append(self.current_indent)
        base_indent = (self.current_column if relative else self.current_indent)
        assert base_indent + amount >= 0
        self.current_indent = base_indent + amount

    @contextmanager
    def push_indent(self, amount=0, relative=True):
        """Create a context manager that calls :meth:`indent` and :meth:`dedent` around a block
        of code.

        This is just an helper to simplify code that adjust the indentation level:

        .. code-block:: python

          with output.push_indent(4):
              # code that emits something with the new indentation
        """

        if self.pending_separator and relative:
            amount += 1
        if self.current_column == 0 and relative:
            amount += self.current_indent
        self.indent(amount, relative)
        yield
        self.dedent()

    def newline(self):
        "Emit a newline."

        self.write('\n')

    def space(self, count=1):
        "Emit consecutive spaces."

        self.write(' '*count)

    def print_list(self, nodes, sep=',', relative_indent=None, standalone_items=None,
                   are_names=False, is_symbol=False):
        """Execute :meth:`print_node` on all the `nodes`, separating them with `sep`.

        :param nodes: a sequence of :class:`~.node.Node` instances
        :param str sep: the separator between them
        :param bool relative_indent:
               if given, the relative amount of indentation to apply before the first item, by
               default computed automatically from the length of the separator `sep`
        :param bool standalone_items: whether a newline will be emitted before each item
        :param bool are_names:
               whether the nodes are actually *names*, which possibly require to be enclosed
               between double-quotes
        :param bool is_symbol:
               whether the nodes are actually an *operator name*, in which case the last one
               must be printed verbatim (such as ``"MySchema".===``)
        """

        if standalone_items is None:
            clm = self.compact_lists_margin
            if clm is not None and clm > 0:
                rawlist = self._concat_nodes(nodes, sep, are_names)
                if self.current_column + len(rawlist) < clm:
                    self.write(rawlist)
                    return

            standalone_items = not all(
                (isinstance(n, Node)
                 and n.node_tag in ('A_Const', 'ColumnRef', 'SetToDefault', 'RangeVar'))
                for n in nodes)

        if (((sep != ',' or not self.comma_at_eoln)
             and len(nodes) > 1
             and len(sep) > 1
             and relative_indent is None
             and not are_names
             and not is_symbol
             and standalone_items)):
            self.write(' '*(len(sep) + 1))  # separator added automatically

        super().print_list(nodes, sep, relative_indent, standalone_items, are_names, is_symbol)

    def _write_quoted_string(self, s):
        """Possibly split `s` string in successive chunks.

        When the ``split_string_literals_threshold`` option is greater than 0 and the length of
        `s` exceeds that value, split the string into multiple chunks.
        """

        sslt = self.split_string_literals_threshold
        if sslt is None or sslt <= 0:
            super()._write_quoted_string(s)
        else:
            multiline = '\n' in s
            if multiline:
                self.write('E')
            with self.push_indent():
                while True:
                    chunk = s[:sslt]
                    s = s[sslt:]
                    # Avoid splitting on backslash
                    while chunk.endswith("\\"):
                        chunk += s[0]
                        s = s[1:]
                    chunk = chunk.replace("'", "''")
                    if multiline:
                        chunk = chunk.replace("\\", "\\\\")
                        chunk = chunk.replace("\n", "\\n")
                    self.write("'%s'" % chunk)
                    if s:
                        self.newline()
                    else:
                        break

    def write(self, s):
        """Write string `s` to the stream, adjusting the `current_column` accordingly.

        :param str s: the string to emit
        :return: the number of characters written to the stream

        If `s` is a newline character (``\\n``) set `current_column` to 0. Otherwise when
        `current_column` is 0 and `current_indent` is greater than 0 emit a number of
        whitespaces *before* emitting `s`, to indent it as expected.
        """

        if s and s != '\n' and self.current_column == 0 and self.current_indent > 0:
            self.current_column = super().write(' ' * self.current_indent)

        count = super().write(s)
        if s == '\n':
            self.current_column = 0
        else:
            self.current_column += count

        return count
