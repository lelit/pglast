# -*- coding: utf-8 -*-
# :Project:   pg_query -- Printer function for SQL DDL nodes
# :Created:   gio 09 nov 2017 10:50:30 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

from .. import enums
from ..printer import node_printer


@node_printer('ColumnDef')
def column_def(node, output):
    output.print(node.colname, is_name=True)
    output.write(' ')
    output.print(node.typeName, is_name=True)
    if node.is_not_null:
        # FIXME: find a way to get here
        output.swrite('NOT NULL')
    if node.constraints:
        output.print_list(node.constraints, '', standalone_items=False)


@node_printer('Constraint')
def constraint(node, output):
    if node.conname:
        output.swrite('CONSTRAINT ')
        output.print(node.conname, is_name=True)
    ct = enums.ConstrType
    if node.contype == ct.CONSTR_NULL:
        output.swrite('NULL')
    elif node.contype == ct.CONSTR_DEFAULT:
        output.swrite('DEFAULT ')
        # """
        # we may have the expression in either "raw" form [...]  or "cooked" form [...]
        # should never have both in the same node!
        # """
        output.print(node.raw_expr or node.cooked_expr)
    elif node.contype == ct.CONSTR_NOTNULL:
        output.swrite('NOT NULL')
    elif node.contype == ct.CONSTR_CHECK:
        output.swrite('CHECK (')
        output.print(node.raw_expr or node.cooked_expr)
        output.write(')')
        if node.is_no_inherit:
            output.swrite('NO INHERIT')
    elif node.contype == ct.CONSTR_PRIMARY:
        output.swrite('PRIMARY KEY')
        if node.keys:
            output.write(' (')
            output.print_list(node.keys, ', ', are_names=True)
            output.write(')')
    elif node.contype == ct.CONSTR_UNIQUE:
        output.swrite('UNIQUE')
        if node.keys:
            output.write(' (')
            output.print_list(node.keys, ', ', are_names=True)
            output.write(')')
    elif node.contype == ct.CONSTR_FOREIGN:
        output.swrite('REFERENCES ')
        output.print(node.pktable)
        output.write(' (')
        output.print_list(node.pk_attrs)
        output.write(')')


@node_printer('CreateStmt')
def create_stmt(node, output):
    output.writes('CREATE TABLE')
    if node.if_not_exists:
        output.writes('IF NOT EXISTS')
    output.print(node.relation)
    output.write(' (')
    output.newline()
    output.write('    ')
    with output.push_indent(2):
        output.print_list(node.tableElts)
    output.newline()
    output.write(')')
    if node.inhRelations:
        output.write(' INHERITS (')
        output.print_list(node.inhRelations)
        output.write(')')
