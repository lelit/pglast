# -*- coding: utf-8 -*-
# :Project:   pglast -- Serialization logic
# :Created:   mer 02 ago 2017 15:46:11 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2020, 2021, 2022, 2023 Lele Gaifax
#

from contextlib import contextmanager
from io import StringIO
from re import compile
from sys import stderr

from . import ast, parse_plpgsql, parse_sql
from .keywords import RESERVED_KEYWORDS, TYPE_FUNC_NAME_KEYWORDS
from .printers import get_printer_for_node, get_special_function


is_simple_name = compile(r'[a-z_][a-z0-9_]*$').match
"Determine whether a name is simple enough to not require being double quoted."


def maybe_double_quote_name(name):
    """Possibly enclose `name` within double quotes.

    When `name` is not entirely composed by lower case letters, digits or underscores, or it
    matches one of the PostgreSQL keywords, it must be emitted between double quotes.
    """

    if ((not is_simple_name(name)
         or name in RESERVED_KEYWORDS
         or name in TYPE_FUNC_NAME_KEYWORDS)):
        name = '"%s"' % name.replace('"', '""')
    return name


class OutputStream(StringIO):
    "A stream that has a concept of a *pending separator* between consecutive writes."

    def __init__(self):
        super().__init__()
        self.pending_separator = False
        self.last_emitted_char = ' '

    def show(self, where=stderr):  # pragma: no cover
        "Emit current stream content, by default to `stderr`, to aid debugging."

        where.write(self.getvalue())
        where.write('\n')

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

        If the last character written was neither a space nor an open parentheses, and `nextc`
        is either ``None`` or a *special character*, then emit a single whitespace.
        """

        lec = self.last_emitted_char
        if not lec.isspace() and lec != '(':
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

    :param int separate_statements:
           ``1`` by default, tells how many empty lines should separate statements
    :param bool special_functions:
           ``False`` by default, when ``True`` some functions are treated in a special way and
           emitted as equivalent constructs
    :param bool comma_at_eoln:
           ``False`` by default, when ``True`` put the comma right after each item instead of
           at the beginning of the *next* item line
    :param bool semicolon_after_last_statement:
           ``False`` by default, when ``True`` add a semicolon after the last statement,
           otherwise it is emitted only as a separator between multiple statements
    :param comments: optional sequence of tuples with the comments extracted from the statement
    :param bool remove_pg_catalog_from_functions:
           ``False`` by default, when ``True`` remove the pg_catalog schema from functions

    This augments :class:`OutputStream` and implements the basic machinery needed to serialize
    the *parse tree* produced by :func:`~.parser.parse_sql()` back to a textual representation,
    without any adornment.
    """

    def __init__(self, separate_statements=1, special_functions=False,
                 comma_at_eoln=False, semicolon_after_last_statement=False,
                 comments=None, remove_pg_catalog_from_functions=False):
        super().__init__()
        self.current_column = 0
        self.separate_statements = separate_statements
        self.special_functions = special_functions
        self.comma_at_eoln = comma_at_eoln
        self.semicolon_after_last_statement = semicolon_after_last_statement
        self.comments = comments
        self.remove_pg_catalog_from_functions = remove_pg_catalog_from_functions

    def show(self, where=stderr):  # pragma: no cover
        """Emit also current expression_level and a "pointer" showing current_column."""

        super().show(where)
        if self.current_column:
            where.write('-' * (self.current_column-1))
        where.write('^\n')

    def __call__(self, sql, plpgsql=False):
        """Main entry point: execute :meth:`print_node` on each statement in `sql`.

        :param sql: the SQL statement
        :param bool plpgsql: whether `sql` is really a ``plpgsql`` statement
        :returns: a string with the equivalent SQL obtained by serializing the syntax tree

        The `sql` statement may be either a ``str`` containing the ``SQL`` in textual form, or
        a concrete :class:`.ast.Node` instance or a tuple of them.
        """

        from .visitors import Visitor

        if isinstance(sql, str):
            sql = parse_plpgsql(sql) if plpgsql else parse_sql(sql)
        elif isinstance(sql, ast.Node):
            sql = (sql,)
        elif not (isinstance(sql, tuple) and sql and isinstance(sql[0], ast.Node)):
            raise ValueError("Unexpected value for 'sql', must be either a string,"
                             " an ast.Node or tuple of them, got %r" % type(sql))

        class UpdateAncestors(Visitor):
            def visit(self, ancestors, node):
                node.ancestors = ancestors

        UpdateAncestors()(sql)

        first = True
        for statement in sql:
            if first:
                first = False
            else:
                self.write(';')
                self.newline()
                for _ in range(self.separate_statements):
                    self.newline()
            self.print_node(statement)

        if self.semicolon_after_last_statement:
            self.write(';')

        if self.comments:
            while self.comments:
                self.print_comment(self.comments.pop(0))

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
            return get_special_function(name)

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
    def expression(self, need_parens):
        """Create a context manager usable to conditionally wrap something within parentheses.

        :param bool need_parens: whether to emit opening and closing parentheses

        This method used to be used for *subexpressions*, but now is used to emit almost
        anything that goes within parentheses.
        """

        if need_parens:
            self.write('(')
        yield
        if need_parens:
            self.write(')')

    def _concat_nodes(self, nodes, sep=' ', are_names=False, item_needs_parens=None):

        """Concatenate given `nodes`, using `sep` as the separator.

        :param scalars: a sequence of nodes
        :param str sep: the separator between them
        :param bool are_names:
               whether the nodes are actually *names*, which possibly require to be enclosed
               between double-quotes
        :param item_needs_parens: either ``None`` or a callable
        :returns: a string

        Use a temporary :class:`RawStream` instance to print the list of nodes and return the
        result.
        """

        rawstream = RawStream(
            special_functions=self.special_functions,
            remove_pg_catalog_from_functions=self.remove_pg_catalog_from_functions)
        rawstream.print_list(nodes, sep, are_names=are_names, standalone_items=False,
                             item_needs_parens=item_needs_parens)
        return rawstream.getvalue()

    def write_quoted_string(self, s):
        "Emit the string `s` as a single-quoted literal constant."

        self.write("'%s'" % s.replace("'", "''"))

    def _print_scalar(self, value, is_name, is_symbol):
        "Print the scalar `value`, special-casing string literals."

        is_string = isinstance(value, str)
        if is_symbol and is_string:
            self.write(value)
        elif is_name and is_string:
            self.write(maybe_double_quote_name(value))
        elif is_string:
            self.write_quoted_string(value)
        else:
            self.write(str(value))

    def print_comment(self, comment):
        "Print the given `comment`, unconditionally in the ``C`` syntax, joining all lines."

        is_sql_comment = comment.text.startswith('--')
        if is_sql_comment:
            text = comment.text[2:].strip()
        else:
            text = comment.text[2:-2].strip()
        if text:
            self.swrite('/*')
            lines = text.splitlines()
            if len(lines) > 1:
                with self.push_indent():
                    for line in lines:
                        self.write(line)
                        self.write(' ')
            else:
                self.write(lines[0])
            self.writes('*/')

    def print_name(self, nodes, sep='.'):
        "Helper method, execute :meth:`print_node` or :meth:`print_list` as needed."

        if isinstance(nodes, (list, tuple)):
            self.print_list(nodes, sep, standalone_items=False, are_names=True)
        elif isinstance(nodes, ast.Node):
            self.print_node(nodes, is_name=True)
        else:
            self._print_scalar(nodes, is_name=True, is_symbol=False)
        self.separator()

    def print_symbol(self, nodes, sep='.'):
        "Helper method, execute :meth:`print_node` or :meth:`print_list` as needed."

        if isinstance(nodes, (list, tuple)):
            self.print_list(nodes, sep, standalone_items=False, are_names=True, is_symbol=True)
        elif isinstance(nodes, ast.Node):
            self.print_node(nodes, is_name=True, is_symbol=True)
        else:
            self._print_scalar(str(nodes), is_name=True, is_symbol=True)
        self.separator()

    def print_node(self, node, is_name=False, is_symbol=False):
        """Lookup the specific printer for the given `node` and execute it.

        :param node: an instance of :class:`~.ast.Node`
        :param bool is_name:
               whether this is a *name* of something, that may need to be double quoted
        :param bool is_symbol:
               whether this is the name of an *operator*, should not be double quoted
        """

        if self.comments:
            if hasattr(node, 'location'):
                node_location = getattr(node, 'location')
            elif hasattr(node, 'stmt_location'):
                node_location = getattr(node, 'stmt_location')
            else:
                node_location = None
            if node_location is not None:
                nextc = self.comments[0]
                if nextc.location <= node_location:
                    self.print_comment(self.comments.pop(0))
                    while self.comments and self.comments[0].continue_previous:
                        self.print_comment(self.comments.pop(0))

        if is_name and isinstance(node, (list, tuple)):
            self.print_list(node, '.', standalone_items=False, are_names=True)
        elif isinstance(node, ast.Node):
            printer = get_printer_for_node(node)
            if is_name and isinstance(node, ast.String):
                printer(node, self, is_name=is_name, is_symbol=is_symbol)
            else:
                printer(node, self)
        else:
            self._print_scalar(node, is_name, is_symbol)

        self.separator()

    def _is_pg_catalog_func(self, items):
        return (
            self.remove_pg_catalog_from_functions
            and len(items) > 1
            and isinstance(items, (list, tuple))
            and items[0].ancestors.parent.member == 'funcname'
            and items[0].sval == 'pg_catalog'
            # The list contains all functions that cannot be found without an
            # explicit pg_catalog schema. ie:
            # position(a,b) is invalid but pg_catalog.position(a,b) is fine
            and items[1].sval not in ('position', 'xmlexists')
        )

    def _print_items(self, items, sep, newline, are_names=False, is_symbol=False,
                     item_needs_parens=None):
        first = 1 if self._is_pg_catalog_func(items) else 0
        last = len(items) - 1
        for idx, item in enumerate(items):
            if idx < first:
                continue
            if idx > first:
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
            if item is None:
                self.write('None')
            else:
                if item_needs_parens is None:
                    needs_parens = False
                else:
                    needs_parens = item_needs_parens(item)
                with self.expression(needs_parens):
                    self.print_node(item, is_name=are_names,
                                    is_symbol=is_symbol and idx == last)

    def print_list(self, nodes, sep=',', relative_indent=None, standalone_items=None,
                   are_names=False, is_symbol=False, item_needs_parens=None):
        """Execute :meth:`print_node` on all the `nodes`, separating them with `sep`.

        :param nodes: a sequence of :class:`~.ast.Node` instances
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
        :param item_needs_parens: either ``None`` or a callable
        """

        if relative_indent is None:
            if are_names or is_symbol:
                relative_indent = 0
            else:
                relative_indent = (-(len(sep) + 1)
                                   if sep and (sep != ',' or not self.comma_at_eoln)
                                   else 0)

        if standalone_items is None:
            standalone_items = not all(isinstance(n, (ast.A_Const, ast.ColumnRef,
                                                      ast.SetToDefault, ast.RangeVar))
                                       for n in nodes)

        with self.push_indent(relative_indent):
            self._print_items(nodes, sep, standalone_items, are_names=are_names,
                              is_symbol=is_symbol, item_needs_parens=item_needs_parens)

    def print_lists(self, lists, sep=',', relative_indent=None, standalone_items=None,
                    are_names=False, sublist_open='(', sublist_close=')', sublist_sep=',',
                    sublist_relative_indent=None):
        """Execute :meth:`print_list` on all the `lists` items.

        :param lists: a sequence of sequences of :class:`~.ast.Node` instances
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
    r"""Indented SQL parse tree writer.

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

    def show(self, where=stderr):  # pragma: no cover
        "Emit also current_indent and indentation_stack."

        where.write('current_indent=%d\n' % self.current_indent)
        where.write('indentation_stack=%r\n' % self.indentation_stack)
        super().show(where)

    def dedent(self):
        "Pop the indentation level from the stack and set `current_indent` to that."

        self.current_indent = self.indentation_stack.pop()

    def indent(self, amount=0, relative=True):
        """Push current indentation level to the stack, then set it adding `amount` to the
        `current_column` if `relative` is ``True`` otherwise to `current_indent`.
        """

        self.indentation_stack.append(self.current_indent)
        base_indent = (self.current_column if relative else self.current_indent)
        assert base_indent + amount >= 0, f'base_indent={base_indent} amount={amount}'
        self.current_indent = base_indent + amount

    @contextmanager
    def push_indent(self, amount=0, relative=True):
        """Create a context manager that calls :meth:`indent` and :meth:`dedent` around a block
        of code.

        This is just an helper to simplify code that adjusts the indentation level:

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

    def print_comment(self, comment):
        is_sql_comment = comment.text.startswith('--')
        if is_sql_comment:
            text = comment.text[2:].strip()
        else:
            text = comment.text[2:-2].strip()
        if text:
            ci = self.current_indent
            cc = self.current_column
            if self.tell() != 0 and comment.at_start_of_line and not comment.continue_previous:
                self.newline()
            lines = comment.text.splitlines()
            if len(lines) > 1:
                with self.push_indent():
                    for line in lines:
                        self.write(line)
                        self.newline()
            else:
                self.write(lines[0])
                if is_sql_comment:
                    self.newline()
                else:
                    self.space()
            self.current_column = cc
            self.current_indent = ci

    def print_list(self, nodes, sep=',', relative_indent=None, standalone_items=None,
                   are_names=False, is_symbol=False, item_needs_parens=None):
        """Execute :meth:`print_node` on all the `nodes`, separating them with `sep`.

        :param nodes: a sequence of :class:`~.ast.Node` instances
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
        :param item_needs_parens: either ``None`` or a callable
        """

        if standalone_items is None:
            clm = self.compact_lists_margin
            if clm is not None and clm > 0:
                rawlist = self._concat_nodes(nodes, sep, are_names, item_needs_parens)
                if self.current_column + len(rawlist) < clm:
                    self.write(rawlist)
                    return

            standalone_items = not all(isinstance(n, (ast.A_Const, ast.ColumnRef,
                                                      ast.SetToDefault, ast.RangeVar))
                                       for n in nodes)

        if (((sep != ',' or not self.comma_at_eoln)
             and len(nodes) > 1
             and len(sep) > 1
             and relative_indent is None
             and not are_names
             and not is_symbol
             and standalone_items)):
            self.write(' '*(len(sep) + 1))  # separator added automatically

        super().print_list(nodes, sep, relative_indent, standalone_items, are_names, is_symbol,
                           item_needs_parens)

    def write_quoted_string(self, s):
        """Emit the string `s` possibly splitted in successive chunks.

        When the ``split_string_literals_threshold`` option is greater than 0 and the length of
        `s` exceeds that value, split the string into multiple chunks.
        """

        sslt = self.split_string_literals_threshold
        if sslt is None or sslt <= 0:
            super().write_quoted_string(s)
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
                    else:  # pragma: no cover
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
