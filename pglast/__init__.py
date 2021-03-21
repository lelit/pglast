# -*- coding: utf-8 -*-
# :Project:   pglast -- PostgreSQL Languages AST
# :Created:   mer 02 ago 2017 15:11:02 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021 Lele Gaifax
#

from . import enums
from .error import Error
from .node import Missing, Node
try:
    from .parser import fingerprint, get_postgresql_version, parse_sql, split
except ModuleNotFoundError:
    # bootstrap
    pass


# This is injected automatically at release time
__version__ = 'v2.0.dev3'
"Package's version."

__author__ = 'Lele Gaifax <lele@metapensiero.it>'
"Package's author."


def parse_plpgsql(statement):
    from json import loads
    from .parser import parse_plpgsql_json

    return loads(parse_plpgsql_json(statement))


def prettify(statement, safety_belt=True, **options):
    r"""Render given `statement` into a prettified format.

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

        if pretty_pt != orig_pt:  # pragma: no cover
            print(prettified)
            warnings.warn("Detected a non-cosmetic difference between original and"
                          " prettified statements, please report", RuntimeWarning)
            return statement

    return prettified


__all__ = ('Error', 'Missing', 'Node', 'enums', 'fingerprint', 'get_postgresql_version',
           'parse_plpgsql', 'parse_sql', 'prettify', 'split')
