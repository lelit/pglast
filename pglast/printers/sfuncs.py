# -*- coding: utf-8 -*-
# :Project:   pglast -- Special functions
# :Created:   mer 22 nov 2017 08:34:34 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018 Lele Gaifax
#

from ..printer import special_function


@special_function('pg_catalog.date_part')
def date_part(node, output):
    """
    Emit function ``pg_catalog.date_part(field, timestamp)`` as
    ``EXTRACT(field FROM timestamp)``.
    """
    output.write('EXTRACT(')
    output.write(node.args[0].val.str.value.upper())
    output.write(' FROM ')
    output.print_node(node.args[1])
    output.write(')')


@special_function('pg_catalog.overlaps')
def overlaps(node, output):
    "Emit function ``pg_catalog.overlaps(a, b, c, d)`` as ``(a, b) OVERLAPS (c, d)``."
    output.write('(')
    output.print_list((node.args[0], node.args[1]), standalone_items=False)
    output.write(') OVERLAPS (')
    output.print_list((node.args[2], node.args[3]), standalone_items=False)
    output.write(')')


@special_function('pg_catalog.timezone')
def timezone(node, output):
    """
    Emit function ``pg_catalog.timezone(tz, timestamp)`` as ``timestamp AT TIME ZONE tz``.
    """
    output.print_node(node.args[1])
    output.write(' AT TIME ZONE ')
    output.print_node(node.args[0])
