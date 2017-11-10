# -*- coding: utf-8 -*-
# :Project:   pg_query -- Pythonic wrapper around libpg_query
# :Created:   mer 02 ago 2017 15:11:02 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

from . import enums
from .error import Error
from .node import Missing, Node
from .parser import get_postgresql_version, parse_plpgsql, parse_sql


def prettify(statement, safety_belt=True, **options):
    """Render given `statement` into a prettified format.

    :param statement: either a string containing the statement(s) or a :class:`~.node.Node`
                      instance
    :param bool safety_belt: whether to perform a safe check against bugs in pg_query's
                             serialization
    :param \*\*options: any keyword option accepted by :class:`~.printer.IndentedStream`
                        constructor
    :returns: a string with the equivalent prettified statement

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
            warnings.warn("Detected a bug in pg_query serialization, please report: %s\n%s"
                          % (e, prettified), RuntimeWarning)
            return statement

        _remove_location(orig_pt)
        _remove_location(pretty_pt)

        if pretty_pt != orig_pt:  # pragma: no cover
            warnings.warn("Detected a non-cosmetic difference between original and"
                          " prettified statements, please report", RuntimeWarning)
            return statement

    return prettified


def _remove_location(parse_tree):
    "Drop the node location, pointless for comparison between raw and pretty printed nodes."

    if isinstance(parse_tree, list):
        for v in parse_tree:
            if v:
                _remove_location(v)
    else:
        parse_tree.pop('location', None)
        for v in parse_tree.values():
            if v and isinstance(v, (dict, list)):
                _remove_location(v)


__all__ = ('Error', 'Missing', 'Node', 'enums', 'get_postgresql_version',
           'parse_plpgsql', 'parse_sql', 'prettify')
