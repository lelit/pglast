# -*- coding: utf-8 -*-
# :Project:   pg_query -- Serialization logic
# :Created:   mer 02 ago 2017 15:46:11 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

from contextlib import contextmanager
from io import StringIO

from .error import Error
from .node import Node, Scalar
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

    def write(self, s):
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
                if s[0].isalnum():
                    count = super().write(' ')
                self.pending_separator = False
            count += super().write(s)
            self.last_emitted_char = s[-1]
        return count


class RawStream(OutputStream):
    """Basic SQL parse tree writer.

    :param separate_statements: a boolean, ``True`` by default, that tells whether multiple
                                statements shall be separated by an empty line

    This implements the basic machinery needed to serialize the *parse tree* produced by
    :func:`~.parser.parse_sql()` back to a textual representation, without any adornment.
    """

    def __init__(self, **options):
        super().__init__()
        if 'separate_statements' not in options:
            options['separate_statements'] = True
        self.options = options
        self.expression_level = 0

    def __call__(self, sql, plpgsql=False):
        """Main entry point: execute :meth:`print` on each statement in `sql`.

        :param sql: either the source SQL in textual form, or a :class:`~.node.Node` instance
        :param plpgsql: whether `sql` is really a ``plpgsql`` statement
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

    def dedent(self):
        "Do nothing, shall be overridden by the prettifier subclass."

    def indent(self, amount=0, relative=True):
        "Do nothing, shall be overridden by the prettifier subclass."

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

        self.indent(amount, relative)
        yield
        self.dedent()

    def _print_items(self, items, sep, newline):
        first = True
        for item in items:
            if first:
                first = False
            else:
                if newline:
                    self.newline()
                else:
                    self.separator()
                self.write(sep)
            self.separator()
            self.print(item)

    def _print_scalar(self, node):
        self.write(str(node.value))

    def print(self, node):
        """Lookup the specific printer for the given `node` and execute it."""

        if isinstance(node, Scalar):
            self._print_scalar(node)
        else:
            printer = get_printer_for_node_tag(node.node_tag)
            printer(node, self)
            self.separator()

    def print_expression(self, nodes, operator):
        """Emit a list of `items` between parens, using `operator` as separator.

        :param nodes: a sequence :class:`~.node.Node` instances, the expression operands
        :param operator: the operator between items
        """

        self.expression_level += 1
        if self.expression_level > 1:
            self.write('(')

        self._print_items(nodes, operator, True)

        self.expression_level -= 1
        if self.expression_level > 0:
            self.write(')')

    def print_list(self, nodes, sep=', ', relative_indent=None, standalone_items=True):
        """Execute :meth:`print` on all the `items`, separating them with `sep`.

        :param nodes: a sequence of :class:`~.node.Node` instances
        :param sep: the separator between them
        :param relative_indent: if given, the relative amount of indentation to apply before
                                the first item, by default computed automatically from the
                                length of the separator `sep`
        :param standalone_items: a boolean that tells whether a newline will be emitted before
                                 each item
        """

        if relative_indent is None:
            relative_indent = -len(sep)
        with self.push_indent(relative_indent):
            self._print_items(nodes, sep, newline=standalone_items)


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
        self.current_column = 0
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
        self.current_indent = base_indent + amount

    def newline(self):
        "Emit a newline."

        self.write('\n')

    def print_expression(self, nodes, operator):
        """Emit a list of `items` between parens, using `operator` as separator.

        :param nodes: a sequence :class:`~.node.Node` instances, the expression operands
        :param operator: the operator between items

        If `align_expression_operands` is ``True`` then the operands will be vertically
        aligned.
        """

        self.expression_level += 1
        if self.expression_level > 1:
            if self.options['align_expression_operands'] and len(nodes) > 1:
                oplen = len(operator)
                self.write('(' + ' '*oplen)
                indent = -oplen
            else:
                self.write('(')
                indent = 0
        else:
            indent = -len(operator)

        with self.push_indent(indent):
            self._print_items(nodes, operator, True)

        self.expression_level -= 1
        if self.expression_level > 0:
            self.write(')')

    def print_list(self, nodes, sep=', ', relative_indent=None, standalone_items=True):
        """Execute :meth:`print` on all the `items`, separating them with `sep`.

        :param nodes: a sequence of :class:`~.node.Node` instances
        :param sep: the separator between them
        :param relative_indent: if given, the relative amount of indentation to apply before
                                the first item, by default computed automatically from the
                                length of the separator `sep`
        :param standalone_items: a boolean that tells whether a newline will be emitted before
                                 each item
        """

        if relative_indent is None:
            relative_indent = -len(sep)

        if len(nodes) > 1:
            self.write(' '*len(sep))

        with self.push_indent(relative_indent):
            self._print_items(nodes, sep, newline=standalone_items)

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
