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
    if node.typeName:
        output.print(node.typeName, is_name=True)
    else:
        if node.constraints:
            output.write('WITH OPTIONS ')
    if node.collClause:
        output.print(node.collClause)
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
    elif node.contype == ct.CONSTR_UNIQUE:
        output.swrite('UNIQUE')
    elif node.contype == ct.CONSTR_EXCLUSION:
        output.swrite('EXCLUDE USING ')
        if node.access_method:
            output.print(node.access_method)
            output.write(' ')
        output.write('(')
        first = True
        for elem, clauses in node.exclusions:
            if first:
                first = False
            else:
                output.write(', ')
            output.print(elem)
            output.swrite('WITH ')
            output.print_list(clauses)
        output.write(')')
    elif node.contype == ct.CONSTR_FOREIGN:
        if node.fk_attrs:
            output.swrite('FOREIGN KEY ')
            output.write(' (')
            output.print_list(node.fk_attrs)
            output.write(')')
        output.swrite('REFERENCES ')
        output.print(node.pktable)
        output.write(' (')
        output.print_list(node.pk_attrs)
        output.write(')')
        if node.fk_matchtype != enums.FKCONSTR_MATCH_SIMPLE:
            output.write(' MATCH ')
            if node.fk_matchtype == enums.FKCONSTR_MATCH_FULL:
                output.write('FULL')
            elif node.fk_matchtype == enums.FKCONSTR_MATCH_PARTIAL:  # pragma: no cover
                # MATCH PARTIAL not yet implemented
                output.write('PARTIAL')
        if node.fk_del_action != enums.FKCONSTR_ACTION_NOACTION:
            output.write(' ON DELETE ')
            if node.fk_del_action == enums.FKCONSTR_ACTION_RESTRICT:
                output.write('RESTRICT')
            elif node.fk_del_action == enums.FKCONSTR_ACTION_CASCADE:
                output.write('CASCADE')
            elif node.fk_del_action == enums.FKCONSTR_ACTION_SETNULL:
                output.write('SET NULL')
            elif node.fk_del_action == enums.FKCONSTR_ACTION_SETDEFAULT:
                output.write('SET DEFAULT')
        if node.fk_upd_action != enums.FKCONSTR_ACTION_NOACTION:
            output.write(' ON UPDATE ')
            if node.fk_upd_action == enums.FKCONSTR_ACTION_RESTRICT:
                output.write('RESTRICT')
            elif node.fk_upd_action == enums.FKCONSTR_ACTION_CASCADE:
                output.write('CASCADE')
            elif node.fk_upd_action == enums.FKCONSTR_ACTION_SETNULL:
                output.write('SET NULL')
            elif node.fk_upd_action == enums.FKCONSTR_ACTION_SETDEFAULT:
                output.write('SET DEFAULT')

    # Common to UNIQUE & PRIMARY_KEY
    if node.keys:
        output.write(' (')
        output.print_list(node.keys, ', ', are_names=True)
        output.write(')')
    if node.options:
        output.swrite('WITH (')
        output.print_list(node.options)
        output.write(')')
    if node.indexspace:
        output.swrite('USING INDEX TABLESPACE ')
        output.print(node.indexspace, is_name=True)


@node_printer('CreateStmt')
def create_stmt(node, output):
    output.writes('CREATE')
    if node.relation.relpersistence == enums.RELPERSISTENCE_TEMP:
        output.writes('TEMPORARY')
    elif node.relation.relpersistence == enums.RELPERSISTENCE_UNLOGGED:
        output.writes('UNLOGGED')
    output.writes('TABLE')
    if node.if_not_exists:
        output.writes('IF NOT EXISTS')
    output.print(node.relation)
    if node.ofTypename:
        output.write(' OF ')
        output.print(node.ofTypename, is_name=True)
    if node.partbound:
        output.write(' PARTITION OF ')
        output.print_list(node.inhRelations)
    if node.tableElts:
        output.write(' (')
        output.newline()
        output.write('    ')
        with output.push_indent(2):
            output.print_list(node.tableElts)
        output.newline()
        output.write(')')
    if node.inhRelations and not node.partbound:
        output.write(' INHERITS (')
        output.print_list(node.inhRelations)
        output.write(')')
    if node.partbound:
        output.swrite('FOR VALUES ')
        output.print(node.partbound)
    if node.partspec:
        output.write(' PARTITION BY ')
        output.print(node.partspec)
    if node.options:
        output.swrite(' WITH (')
        output.print_list(node.options)
        output.write(')')
    if node.oncommit != enums.OnCommitAction.ONCOMMIT_NOOP:
        output.swrite('ON COMMIT ')
        if node.oncommit == enums.OnCommitAction.ONCOMMIT_PRESERVE_ROWS:
            output.write('PRESERVE ROWS')
        elif node.oncommit == enums.OnCommitAction.ONCOMMIT_DELETE_ROWS:
            output.write('DELETE ROWS')
        elif node.oncommit == enums.OnCommitAction.ONCOMMIT_DROP:
            output.write('DROP')
    if node.tablespacename:
        output.swrite('TABLESPACE ')
        output.print(node.tablespacename, is_name=True)


@node_printer('DefElem')
def def_elem(node, output):
    output.print(node.defname)
    output.write('=')
    output.print(node.arg)
    if node.defaction != enums.DefElemAction.DEFELEM_UNSPEC:
        raise NotImplementedError


@node_printer('IndexStmt')
def index_stmt(node, output):
    output.write('CREATE ')
    if node.unique:
        output.write('UNIQUE ')
    output.write('INDEX ')
    if node.concurrent:
        output.write('CONCURRENTLY ')
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    if node.idxname:
        output.print(node.idxname, is_name=True)
    output.swrite('ON ')
    output.print(node.relation)
    if node.accessMethod != 'btree':
        output.swrite('USING ')
        output.print(node.accessMethod, is_name=True)
    output.write(' (')
    output.print_list(node.indexParams)
    output.write(')')
    if node.options:
        output.swrite('WITH (')
        output.print_list(node.options)
        output.write(')')
    if node.tableSpace:
        output.swrite('TABLESPACE ')
        output.print(node.tableSpace, is_name=True)
    if node.whereClause:
        output.write(' WHERE ')
        output.print(node.whereClause)


@node_printer('PartitionBoundSpec')
def partition_bound_spec(node, output):
    if node.strategy.value == enums.PARTITION_STRATEGY_RANGE:
        output.swrite('FROM (')
        output.print_list(node.lowerdatums)
        output.write(') TO (')
        output.print_list(node.upperdatums)
        output.write(')')
    else:
        output.swrite('IN (')
        output.print_list(node.listdatums)
        output.write(')')


@node_printer('PartitionElem')
def partition_elem(node, output):
    if node.name:
        output.print(node.name, is_name=True)
    elif node.expr:
        output.print(node.expr)
    if node.collation or node.opclass:
        raise NotImplementedError


@node_printer('PartitionRangeDatum')
def partition_range_datum(node, output):
    if node.kind == enums.PartitionRangeDatumKind.PARTITION_RANGE_DATUM_MINVALUE:
        output.write('MINVALUE')
    elif node.kind == enums.PartitionRangeDatumKind.PARTITION_RANGE_DATUM_MAXVALUE:
        output.write('MAXVALUE')
    else:
        output.print(node.value)


@node_printer('PartitionSpec')
def partition_spec(node, output):
    output.print(node.strategy)
    output.write(' (')
    output.print_list(node.partParams)
    output.write(')')
