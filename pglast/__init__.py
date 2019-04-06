# -*- coding: utf-8 -*-
# :Project:   pglast -- PostgreSQL Languages AST
# :Created:   mer 02 ago 2017 15:11:02 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019 Lele Gaifax
#

from . import enums
from .error import Error
from .node import Missing, Node
from .parser import get_postgresql_version, parse_plpgsql, parse_sql


# This is injected automatically at release time
__version__ = 'v1.4'
"Package's version."

__author__ = 'Lele Gaifax <lele@metapensiero.it>'
"Package's author."


def prettify(statement, safety_belt=True, **options):
    """Render given `statement` into a prettified format.

    :param str statement: the SQL statement(s)
    :param bool safety_belt: whether to perform a safe check against bugs in pglast's
                             serialization
    :param \*\*options: any keyword option accepted by :class:`~.printer.IndentedStream`
                        constructor
    :returns: a string with the equivalent prettified statement(s)

    When `safety_belt` is ``True``, the resulting statement is parsed again and its *AST*
    compared with the original statement: if they don't match, a warning is emitted and the
    original statement is returned. This is a transient protection against possible bugs in the
    serialization machinery that may disappear before 1.0.
    """

    # Intentional lazy imports, so the modules are loaded on demand

    import warnings
    from .printer import IndentedStream
    from . import printers  # noqa

    orig_pt = parse_sql(statement)
    prettified = IndentedStream(**options)(Node(orig_pt))
    if safety_belt:
        try:
            pretty_pt = parse_sql(prettified)
        except Error as e:  # pragma: no cover
            print(prettified)
            warnings.warn("Detected a bug in pglast serialization, please report: %s\n%s"
                          % (e, prettified), RuntimeWarning)
            return statement

        _remove_stmt_len_and_location(orig_pt)
        _remove_stmt_len_and_location(pretty_pt)

        if pretty_pt != orig_pt:  # pragma: no cover
            print(prettified)
            warnings.warn("Detected a non-cosmetic difference between original and"
                          " prettified statements, please report", RuntimeWarning)
            return statement

    return prettified


def split(statements, safety_belt=True, stream_class=None, **options):
    """Split given `statements` and yield one statement at a time.

    :param str statements: the SQL statement(s)
    :param bool safety_belt: whether to perform a safe check against bugs in pglast's
                             serialization
    :param stream_class: the subclass of :class:`~.printer.OutputStream` that shall be
                         used to render each statement, defaults to
                         :class:`~.printer.RawStream`
    :param \*\*options: any keyword option accepted by the `stream_class` constructor
    :returns: a generator that will yield one statement at a time

    When `safety_belt` is ``True``, the resulting statement is parsed again and its *AST*
    compared with the original statement: if they don't match, an :class:`~.error.Error` is
    raised. This is a transient protection against possible bugs in the serialization machinery
    that may disappear before 1.0.
    """

    from . import printers  # noqa

    if stream_class is None:
        from .printer import RawStream
        stream_class = RawStream

    for orig_pt in parse_sql(statements):
        printed = stream_class(**options)(Node(orig_pt))
        if safety_belt:
            printed_pt = parse_sql(printed)[0]

            _remove_stmt_len_and_location(orig_pt)
            _remove_stmt_len_and_location(printed_pt)

            if printed_pt != orig_pt:  # pragma: no cover
                raise Error("Detected a non-cosmetic difference between original and"
                            " printed statement")
        yield printed


def _remove_stmt_len_and_location(parse_tree):
    """Drop ``RawStmt`` `stmt_len`__ and all nodes `location`, pointless for comparison between
    raw and pretty printed nodes.

    __ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/\
       parsenodes.h;h=ecb6cd0249861bf48863a5c35d525d1d73ff89f0;\
       hb=65c6b53991e1c56f6a0700ae26928962ddf2b9fe#l1420
    """

    if isinstance(parse_tree, list):
        for v in parse_tree:
            if v:
                _remove_stmt_len_and_location(v)
    else:
        parse_tree.pop('location', None)
        for k, v in parse_tree.items():
            if k == 'RawStmt':
                v.pop('stmt_len', None)
                v.pop('stmt_location', None)
            if v and isinstance(v, (dict, list)):
                _remove_stmt_len_and_location(v)


__all__ = ('Error', 'Missing', 'Node', 'enums', 'get_postgresql_version',
           'parse_plpgsql', 'parse_sql', 'prettify', 'split')
