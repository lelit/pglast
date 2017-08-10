# -*- coding: utf-8 -*-
# :Project:   pg_query -- Serialization logic
# :Created:   mer 02 ago 2017 15:46:11 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

from contextlib import contextmanager
from io import StringIO
from re import match

from .error import Error
from .node import Node, Scalar
from .keywords import RESERVED_KEYWORDS
from .parser import parse_plpgsql, parse_sql


NODE_PRINTERS = {}
"Registry of specialized printers, keyed by their `tag`."


class PrinterAlreadyPresentError(Error):
    "Exception raised trying to register another function for a tag already present."


def get_printer_for_node_tag(node_tag):
    "Get specific printer implementation for given `node_tag`."

    try:
        return NODE_PRINTERS[node_tag]
    except KeyError:
        raise NotImplementedError("Printer for node %r is not implemented yet"
                                  % node_tag)


def node_printer(node_tag, override=False):
    """Decorator to register a specific printer implementation for given `node_tag`.

    :param str node_tag: the node tag
    :param bool override: when ``True`` the function will be registered even if already present
    """

    def decorator(impl):
        if not override and node_tag in NODE_PRINTERS:
            raise PrinterAlreadyPresentError("A printer is already registered for tag %r"
                                             % node_tag)
        NODE_PRINTERS[node_tag] = impl
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

    def write(self, s, *, _special_chars=set("""_*+/-"'=<>""")):
        """Emit string `s`.

        :param str s: the string to emit
        :return: the number of character written to the stream

        When `s` is not empty and `pending_separator` is ``True`` and the first character of
        `s` is alphanumeric, emit a single whitespace before writing out `s` and then reset
        `pending_separator` to ``False``.
        """

        count = 0
        if s:
            if self.pending_separator:
                if s[0].isalnum() or s[0] in _special_chars:
                    count = super().write(' ')
                self.pending_separator = False
            count += super().write(s)
            self.last_emitted_char = s[-1]

        return count

    def writes(self, s):
        "Shortcut for ``self.write(s); self.separator()``."

        count = self.write(s)
        self.separator()
        return count

    def swrite(self, s):
        "Shortcut for ``self.separator(); self.write(s);``."

        self.separator()
        return self.write(s)

    def swrites(self, s):
        "Shortcut for ``self.separator(); self.write(s); self.separator()``."

        self.separator()
        count = self.write(s)
        self.separator()
        return count


class RawStream(OutputStream):
    """Basic SQL parse tree writer.

    :param separate_statements: a boolean, ``True`` by default, that tells whether multiple
                                statements shall be separated by an empty line

    This augments :class:`OutputStream` and implements the basic machinery needed to serialize
    the *parse tree* produced by :func:`~.parser.parse_sql()` back to a textual representation,
    without any adornment.
    """

    def __init__(self, **options):
        super().__init__()
        if 'separate_statements' not in options:
            options['separate_statements'] = True
        self.options = options
        self.expression_level = 0
        self.current_column = 0
        self.current_indent = 0
        self.indentation_stack = []

    def __call__(self, sql, plpgsql=False):
        """Main entry point: execute :meth:`print` on each statement in `sql`.

        :param sql: either the source SQL in textual form, or a :class:`~.node.Node` instance
        :param bool plpgsql: whether `sql` is really a ``plpgsql`` statement
        :returns: a string with the equivalent SQL obtained by serializing the syntax tree
        """

        if isinstance(sql, str):
            sql = Node(parse_plpgsql(sql) if plpgsql else parse_sql(sql))

        first = True
        for statement in sql:
            if first:
                first = False
            else:
                self.write(';')
                self.newline()
                if self.options['separate_statements']:
                    self.newline()
            self.print(statement)
        return self.getvalue()

    def concat_scalars(self, scalars, sep=' ', are_names=False):
        """Concatenate given `scalars`, using `sep` as the separator.

        :param scalars: a sequence of nodes
        :param str sep: the separator between them
        :param bool are_names: whether the nodes are actually *names*, which possibly require
                               to be enclosed between double-quotes
        :returns: a string
        """

        substream = type(self)(**self.options)
        substream.print_list(scalars, sep, are_names=are_names, standalone_items=False)
        return substream.getvalue()

    def dedent(self):
        "Pop the indentation level from the stack and set `current_indent` to that."

        self.current_indent = self.indentation_stack.pop()

    def indent(self, amount=0, relative=True):
        """Push current indentation level to the stack, then set it adding `amount` to the
        `current_column` if `relative` is ``True`` otherwise to `current_indent`.
        """

        self.indentation_stack.append(self.current_indent)
        base_indent = (self.current_column if relative else self.current_indent)
        self.current_indent = base_indent + amount

    def maybe_double_quote_name(self, scalar):
        """Double-quote the given `scalar` if needed.

        :param scalar: a :class:`~.node.Scalar` string instance
        :return: the string value of the scalar, possibly double quoted

        The `scalar` represent a name of a column/table/alias: when any of its characters
        is not a lower case letter, a digit or underscore, it must be double quoted.
        """

        assert isinstance(scalar, Scalar) and isinstance(scalar.value, str)
        s = scalar.value
        if not match(r'[a-z_][a-z0-9_]*$', s) or s in RESERVED_KEYWORDS:
            return '"%s"' % s
        else:
            return s

    def newline(self):
        "Emit a single whitespace, shall be overridden by the prettifier subclass."

        self.separator()

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

    def _print_items(self, items, sep, newline, are_names=False):
        first = True
        for item in items:
            if first:
                first = False
            else:
                if not are_names:
                    if newline:
                        self.newline()
                self.write(sep)
                if not are_names:
                    self.write(' ')
            self.print(item, is_name=are_names)

    def _print_scalar(self, node, is_name):
        value = self.maybe_double_quote_name(node) if is_name else str(node.value)
        self.write(value)

    def print(self, node, is_name=False):
        """Lookup the specific printer for the given `node` and execute it."""

        if isinstance(node, Scalar):
            self._print_scalar(node, is_name)
        else:
            printer = get_printer_for_node_tag(node.node_tag)
            if is_name and node.node_tag == 'String':
                printer(node, self, is_name=True)
            else:
                printer(node, self)
            self.separator()

    @contextmanager
    def expression(self):
        self.expression_level += 1
        if self.expression_level > 1:
            self.write('(')
        yield
        if self.expression_level > 1:
            self.write(')')
        self.expression_level -= 1

    def print_list(self, nodes, sep=',', relative_indent=None, standalone_items=None,
                   are_names=False):
        """Execute :meth:`print` on all the `items`, separating them with `sep`.

        :param nodes: a sequence of :class:`~.node.Node` instances
        :param str sep: the separator between them
        :param bool relative_indent: if given, the relative amount of indentation to apply
                                     before the first item, by default computed automatically
                                     from the length of the separator `sep`
        :param bool standalone_items: whether a newline will be emitted before each item
        :param bool are_names: whether the nodes are actually *names*, which possibly require
                               to be enclosed between double-quotes
        """

        if relative_indent is None:
            relative_indent = -(len(sep) + 1)

        if standalone_items is None:
            standalone_items = not all(isinstance(n, Node) and n.node_tag == 'A_Const'
                                       for n in nodes)

        with self.push_indent(relative_indent):
            self._print_items(nodes, sep, standalone_items, are_names=are_names)


class IndentedStream(RawStream):
    """Indented SQL parse tree writer.

    :param align_expression_operands: whether to vertically align the operands of an expression
    :param \*\*options: other options accepted by :class:`Serializer`

    This augments :class:`RawStream` to emit a prettified representation of a *parse tree*.
    """

    def __init__(self, **options):
        if 'align_expression_operands' not in options:
            options['align_expression_operands'] = True
        super().__init__(**options)

    def newline(self):
        "Emit a newline."

        self.write('\n')

    def print_list(self, nodes, sep=',', relative_indent=None, standalone_items=None,
                   are_names=False):
        """Execute :meth:`print` on all the `items`, separating them with `sep`.

        :param nodes: a sequence of :class:`~.node.Node` instances
        :param str sep: the separator between them
        :param bool relative_indent: if given, the relative amount of indentation to apply
                                     before the first item, by default computed automatically
                                     from the length of the separator `sep`
        :param bool standalone_items: whether a newline will be emitted before each item
        :param bool are_names: whether the nodes are actually *names*, which possibly require
                               to be enclosed between double-quotes
        """

        if standalone_items is None:
            standalone_items = not all(isinstance(n, Node) and n.node_tag == 'A_Const'
                                       for n in nodes)

        if len(nodes) > 1 and len(sep) > 1 and relative_indent is None and standalone_items:
            self.write(' '*(len(sep) + 1)) # separator added automatically

        super().print_list(nodes, sep, relative_indent, standalone_items, are_names)

    def write(self, s):
        """Write string `s` to the stream, adjusting the `current_column` accordingly.

        :param str s: the string to emit
        :return: the number of character written to the stream

        If `s` is a newline character (``\\n``) set `current_column` to 0. Otherwise when
        `current_column` is 0 and `current_indent` is not emit a number of whitespaces *before*
        emitting `s`, to indent it as expected.
        """

        if s and s != '\n' and self.current_column == 0 and self.current_indent > 0:
            self.current_column = super().write(' ' * self.current_indent)

        count = super().write(s)
        if s == '\n':
            self.current_column = 0
        else:
            self.current_column += count

        return count
