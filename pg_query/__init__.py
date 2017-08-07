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
from .parser import parse_plpgsql, parse_sql


def prettify(statement, **options):
    """Render given `statement` into a prettified format.

    :param statement: either a string containing the statement(s) or a :class:`~.node.Node`
                      instance
    :param \*\*options: any keyword option accepted by :class:`~.printer.IndentedStream`
                        constructor
    :returns: a string with the equivalent prettified statement
    """

    # Intentional lazy imports, so the modules are loaded on demand

    from .printer import IndentedStream
    from .printers import sql

    return IndentedStream(**options)(statement)


__all__ = ('Error', 'Missing', 'Node', 'enums', 'parse_plpgsql', 'parse_sql', 'prettify')
