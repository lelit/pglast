# -*- coding: utf-8 -*-
# :Project:   pg_query -- Printer function for SQL DDL nodes
# :Created:   gio 09 nov 2017 10:50:30 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

from .. import enums
from ..node import Missing, List
from ..printer import node_printer


@node_printer('ColumnDef')
def column_def(node, output):
    output.print_node(node.colname, is_name=True)
    output.write(' ')
    if node.typeName:
        output.print_node(node.typeName, is_name=True)
    else:
        if node.constraints:
            output.write('WITH OPTIONS ')
    if node.collClause:
        output.print_node(node.collClause)
    if node.is_not_null:
        # FIXME: find a way to get here
        output.swrite('NOT NULL')
    if node.constraints:
        output.print_list(node.constraints, '', standalone_items=False)


@node_printer('Constraint')
def constraint(node, output):
    if node.conname:
        output.swrite('CONSTRAINT ')
        output.print_node(node.conname, is_name=True)
    ct = enums.ConstrType
    if node.contype == ct.CONSTR_NULL:
        output.swrite('NULL')
    elif node.contype == ct.CONSTR_DEFAULT:
        output.swrite('DEFAULT ')
        # """
        # we may have the expression in either "raw" form [...]  or "cooked" form [...]
        # should never have both in the same node!
        # """
        output.print_node(node.raw_expr or node.cooked_expr)
    elif node.contype == ct.CONSTR_NOTNULL:
        output.swrite('NOT NULL')
    elif node.contype == ct.CONSTR_CHECK:
        output.swrite('CHECK (')
        output.print_node(node.raw_expr or node.cooked_expr)
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
            output.print_node(node.access_method)
            output.write(' ')
        output.write('(')
        first = True
        for elem, clauses in node.exclusions:
            if first:
                first = False
            else:
                output.write(', ')
            output.print_node(elem)
            output.swrite('WITH ')
            output.write(clauses.string_value)
        output.write(')')
    elif node.contype == ct.CONSTR_FOREIGN:
        if node.fk_attrs:
            output.swrite('FOREIGN KEY ')
            output.write(' (')
            output.print_list(node.fk_attrs, are_names=True)
            output.write(')')
        output.swrite('REFERENCES ')
        output.print_node(node.pktable, is_name=True)
        output.write(' (')
        output.print_list(node.pk_attrs, are_names=True)
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
    with output.push_indent():
        first = True
        if node.options:
            output.write(' WITH (')
            output.print_list(node.options)
            output.write(')')
            first = False
        if node.indexspace:
            if first:
                first = False
            else:
                output.newline()
            output.write(' USING INDEX TABLESPACE ')
            output.print_node(node.indexspace, is_name=True)


@node_printer('CreateAmStmt')
def create_am_stmt(node, output):
    output.write('CREATE ACCESS METHOD ')
    output.print_node(node.amname, is_name=True)
    if node.amtype == 'i':
        output.write(' TYPE INDEX HANDLER ')
        output.print_list(node.handler_name, '.', are_names=True)
    else:  # pragma: nocover
        raise NotImplementedError


@node_printer('CreateDomainStmt')
def create_domain_stmt(node, output):
    output.write('CREATE DOMAIN ')
    output.print_list(node.domainname, '.', are_names=True)
    output.write(' AS ')
    output.print_node(node.typeName)
    if node.collClause:
        output.print_node(node.collClause)
    if node.constraints:
        output.print_list(node.constraints, '', standalone_items=False)


@node_printer('CreateSchemaStmt')
def create_schema_stmt(node, output):
    output.write('CREATE SCHEMA ')
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    if node.schemaname:
        output.print_node(node.schemaname, is_name=True)
    if node.authrole:
        output.swrite('AUTHORIZATION ')
        output.print_node(node.authrole)
    if node.schemaElts:
        output.newline()
        output.write('  ')
        with output.push_indent():
            output.print_list(node.schemaElts, '', standalone_items=True)


@node_printer('CreateSeqStmt')
def create_seq_stmt(node, output):
    output.write('CREATE ')
    if node.sequence.relpersistence == enums.RELPERSISTENCE_TEMP:
        output.writes('TEMPORARY')
    output.writes('SEQUENCE')
    if node.if_not_exists:
        output.writes('IF NOT EXISTS')
    if node.sequence.schemaname is not Missing:
        output.print_node(node.sequence.schemaname, is_name=True)
        output.write('.')
    output.print_node(node.sequence.relname, is_name=True)
    if node.options:
        output.newline()
        output.write('  ')
        with output.push_indent():
            output.print_list(node.options, '')


@node_printer('CreateSeqStmt', 'DefElem')
def create_seq_stmt_def_elem(node, output):
    option = node.defname.value
    if option == 'cycle':
        if node.arg.ival.value == 0:
            output.write('NO ')
        output.write('CYCLE')
    elif option == 'increment':
        output.write('INCREMENT BY ')
        output.print_node(node.arg)
    elif option == 'owned_by':
        output.write('OWNED BY ')
        output.print_list(node.arg, '.', are_names=True)
    elif option == 'start':
        output.write('START WITH ')
        output.print_node(node.arg)
    else:
        if node.arg is Missing:
            output.write('NO ')
        output.write(option.upper())
        if node.arg is not Missing:
            output.write(' ')
            output.print_node(node.arg)
    if node.defaction != enums.DefElemAction.DEFELEM_UNSPEC:  # pragma: nocover
        raise NotImplementedError


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
    output.print_node(node.relation)
    if node.ofTypename:
        output.write(' OF ')
        output.print_node(node.ofTypename, is_name=True)
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
    with output.push_indent():
        first = True
        if node.inhRelations and not node.partbound:
            output.write(' INHERITS (')
            output.print_list(node.inhRelations)
            output.write(')')
            first = False
        if node.partbound:
            if first:
                first = False
            else:  # pragma: nocover
                output.newline()
            output.write(' FOR VALUES ')
            output.print_node(node.partbound)
        if node.partspec:
            if first:
                first = False
            else:  # pragma: nocover
                output.newline()
            output.write(' PARTITION BY ')
            output.print_node(node.partspec)
        if node.options:
            if first:
                first = False
            else:
                output.newline()
            if len(node.options) == 1 and node.options[0].defname == 'oids':
                output.write(' WITH')
                if node.options[0].arg.ival.value == 0:
                    output.write
                    output.write('OUT')
                output.write(' OIDS')
            else:
                output.write(' WITH (')
                output.print_list(node.options)
                output.write(')')
        if node.oncommit != enums.OnCommitAction.ONCOMMIT_NOOP:
            if first:
                first = False
            else:
                output.newline()
            output.write(' ON COMMIT ')
            if node.oncommit == enums.OnCommitAction.ONCOMMIT_PRESERVE_ROWS:
                output.write('PRESERVE ROWS')
            elif node.oncommit == enums.OnCommitAction.ONCOMMIT_DELETE_ROWS:
                output.write('DELETE ROWS')
            elif node.oncommit == enums.OnCommitAction.ONCOMMIT_DROP:
                output.write('DROP')
        if node.tablespacename:
            if first:
                first = False
            else:
                output.newline()
            output.write(' TABLESPACE ')
            output.print_node(node.tablespacename, is_name=True)


@node_printer('CreateTableAsStmt')
def create_table_as_stmt(node, output):
    output.writes('CREATE')
    into = node.into
    rel = into.rel
    if rel.relpersistence == enums.RELPERSISTENCE_TEMP:
        output.writes('TEMPORARY')
    elif rel.relpersistence == enums.RELPERSISTENCE_UNLOGGED:
        output.writes('UNLOGGED')
    output.writes('TABLE')
    if node.if_not_exists:
        output.writes('IF NOT EXISTS')
    output.print_node(rel)
    if into.colNames:
        output.write(' (')
        output.print_list(into.colNames, are_names=True)
        output.write(')')
    output.newline()
    if into.options:
        if len(into.options) == 1 and into.options[0].defname == 'oids':
            output.write('  WITH')
            if into.options[0].arg.ival.value == 0:
                output.write
                output.write('OUT')
            output.write(' OIDS')
        else:
            output.write('  WITH (')
            output.print_list(into.options)
            output.write(')')
        output.newline()
    if into.onCommit != enums.OnCommitAction.ONCOMMIT_NOOP:
        output.write('  ON COMMIT ')
        if into.onCommit == enums.OnCommitAction.ONCOMMIT_PRESERVE_ROWS:
            output.write('PRESERVE ROWS')
        elif into.onCommit == enums.OnCommitAction.ONCOMMIT_DELETE_ROWS:
            output.write('DELETE ROWS')
        elif into.onCommit == enums.OnCommitAction.ONCOMMIT_DROP:
            output.write('DROP')
        output.newline()
    if into.tableSpaceName:
        output.write('  TABLESPACE ')
        output.print_node(into.tableSpaceName, is_name=True)
        output.newline()
    output.write('  AS ')
    if ((node.query.targetList is not Missing
         and node.query.whereClause is Missing
         and len(node.query.targetList[0].val.fields) == 1
         and node.query.targetList[0].val.fields[0].node_tag == 'A_Star')):
        output.write('TABLE ')
        output.print_list(node.query.fromClause)
    else:
        with output.push_indent():
            output.print_node(node.query)
    if node.into.skipData:
        output.newline()
        output.write('  WITH NO DATA')


@node_printer('CreatedbStmt')
def createdb_stmt(node, output):
    output.write('CREATE DATABASE ')
    output.print_node(node.dbname, is_name=True)
    if node.options:
        output.newline()
        output.write('  WITH ')
        output.print_list(node.options, '')


@node_printer('DefElem')
def def_elem(node, output):
    output.print_node(node.defname)
    output.write(' = ')
    output.print_node(node.arg)
    if node.defaction != enums.DefElemAction.DEFELEM_UNSPEC:  # pragma: nocover
        raise NotImplementedError


@node_printer('DropdbStmt')
def drop_db_stmt(node, output):
    output.write('DROP DATABASE')
    if node.missing_ok:
        output.write(' IF EXISTS')
    output.write(' ')
    output.print_node(node.dbname, is_name=True)


@node_printer('DropOwnedStmt')
def drop_owned_stmt(node, output):
    output.write('DROP OWNED BY ')
    output.print_list(node.roles, are_names=True)
    if node.behavior == enums.DropBehavior.DROP_CASCADE:
        output.write(' CASCADE')
    elif node.behavior == enums.DropBehavior.DROP_RESTRICT:
        output.write(' RESTRICT')


@node_printer('DropRoleStmt')
def drop_role_stmt(node, output):
    output.write('DROP ROLE')
    if node.missing_ok:
        output.write(' IF EXISTS')
    output.write(' ')
    output.print_list(node.roles, are_names=True)


@node_printer('DropStmt')
def drop_stmt(node, output):
    otypes = enums.ObjectType
    output.write('DROP ')
    output.writes({
        otypes.OBJECT_ACCESS_METHOD: 'ACCESS METHOD',
        otypes.OBJECT_AGGREGATE: 'AGGREGATE',
        otypes.OBJECT_AMOP: 'AMOP',
        otypes.OBJECT_AMPROC: 'AMPROC',
        otypes.OBJECT_ATTRIBUTE: 'ATTRIBUTE',
        otypes.OBJECT_CAST: 'CAST',
        otypes.OBJECT_COLUMN: 'COLUMN',
        otypes.OBJECT_COLLATION: 'COLLATION',
        otypes.OBJECT_CONVERSION: 'CONVERSION',
        otypes.OBJECT_DATABASE: 'DATABASE',
        otypes.OBJECT_DEFAULT: 'DEFAULT',
        otypes.OBJECT_DEFACL: 'DEFACL',
        otypes.OBJECT_DOMAIN: 'DOMAIN',
        otypes.OBJECT_DOMCONSTRAINT: 'DOMCONSTRAINT',
        otypes.OBJECT_EVENT_TRIGGER: 'EVENT TRIGGER',
        otypes.OBJECT_EXTENSION: 'EXTENSION',
        otypes.OBJECT_FDW: 'FOREIGN DATA WRAPPER',
        otypes.OBJECT_FOREIGN_SERVER: 'SERVER',
        otypes.OBJECT_FOREIGN_TABLE: 'FOREIGN TABLE',
        otypes.OBJECT_FUNCTION: 'FUNCTION',
        otypes.OBJECT_INDEX: 'INDEX',
        otypes.OBJECT_LANGUAGE: 'LANGUAGE',
        otypes.OBJECT_LARGEOBJECT: 'LARGEOBJECT',
        otypes.OBJECT_MATVIEW: 'MATERIALIZED VIEW',
        otypes.OBJECT_OPCLASS: 'OPERATOR CLASS',
        otypes.OBJECT_OPERATOR: 'OPERATOR',
        otypes.OBJECT_OPFAMILY: 'OPERATOR FAMILY',
        otypes.OBJECT_POLICY: 'POLICY',
        otypes.OBJECT_PUBLICATION: 'PUBLICATION',
        otypes.OBJECT_PUBLICATION_REL: 'PUBLICATION_REL',
        otypes.OBJECT_ROLE: 'ROLE',
        otypes.OBJECT_RULE: 'RULE',
        otypes.OBJECT_SCHEMA: 'SCHEMA',
        otypes.OBJECT_SEQUENCE: 'SEQUENCE',
        otypes.OBJECT_SUBSCRIPTION: 'SUBSCRIPTION',
        otypes.OBJECT_STATISTIC_EXT: 'STATISTICS',
        otypes.OBJECT_TABCONSTRAINT: 'TABCONSTRAINT',
        otypes.OBJECT_TABLE: 'TABLE',
        otypes.OBJECT_TABLESPACE: 'TABLESPACE',
        otypes.OBJECT_TRANSFORM: 'TRANSFORM',
        otypes.OBJECT_TRIGGER: 'TRIGGER',
        otypes.OBJECT_TSCONFIGURATION: 'TEXT SEARCH CONFIGURATION',
        otypes.OBJECT_TSDICTIONARY: 'TEXT SEARCH DICTIONARY',
        otypes.OBJECT_TSPARSER: 'TEXT SEARCH PARSER',
        otypes.OBJECT_TSTEMPLATE: 'TEXT SEARCH TEMPLATE',
        otypes.OBJECT_TYPE: 'TYPE',
        otypes.OBJECT_USER_MAPPING: 'USER_MAPPING',
        otypes.OBJECT_VIEW: 'VIEW',
    }[node.removeType.value])
    if node.removeType == otypes.OBJECT_INDEX:
        if node.concurrent:
            output.write(' CONCURRENTLY')
    if node.missing_ok:
        output.write(' IF EXISTS')
    output.write(' ')
    if node.objects:
        if node.removeType in (otypes.OBJECT_OPCLASS, otypes.OBJECT_OPFAMILY):
            nodes = list(node.objects[0])
            using = nodes.pop(0)
            output.print_list(nodes, '.', standalone_items=False, are_names=True)
            output.write(' USING ')
            output.print_node(using, is_name=True)
        elif node.removeType == otypes.OBJECT_TRANSFORM:
            nodes = list(node.objects[0])
            output.write('FOR ')
            output.print_node(nodes.pop(0), is_name=True)
            output.write(' LANGUAGE ')
            output.print_list(nodes, '.', standalone_items=False, are_names=True)
        elif node.removeType in (otypes.OBJECT_POLICY,
                                 otypes.OBJECT_RULE,
                                 otypes.OBJECT_TRIGGER):
            nodes = list(node.objects[0])
            on = nodes.pop(0)
            output.print_list(nodes, '.', standalone_items=False, are_names=True)
            output.write(' ON ')
            output.print_node(on, is_name=True)
        elif isinstance(node.objects[0], List):
            if node.objects[0][0].node_tag != 'String':
                output.print_lists(node.objects, ' AS ', standalone_items=False,
                                   are_names=True)
            else:
                output.print_lists(node.objects, sep='.', sublist_open='', sublist_close='',
                                   standalone_items=False, are_names=True)
        else:
            output.print_list(node.objects, ',', standalone_items=False, are_names=True)
    if node.behavior == enums.DropBehavior.DROP_CASCADE:
        output.write(' CASCADE')
    elif node.behavior == enums.DropBehavior.DROP_RESTRICT:
        output.write(' RESTRICT')


@node_printer('DropSubscriptionStmt')
def drop_subscription_stmt(node, output):
    output.write('DROP SUBSCRIPTION')
    if node.missing_ok:
        output.write(' IF EXISTS')
    output.write(' ')
    output.print_node(node.subname, is_name=True)
    if node.behavior == enums.DropBehavior.DROP_CASCADE:
        output.write(' CASCADE')
    elif node.behavior == enums.DropBehavior.DROP_RESTRICT:
        output.write(' RESTRICT')


@node_printer('DropTableSpaceStmt')
def drop_table_space_stmt(node, output):
    output.write('DROP TABLESPACE')
    if node.missing_ok:
        output.write(' IF EXISTS')
    output.write(' ')
    output.print_node(node.tablespacename, is_name=True)


@node_printer('DropUserMappingStmt')
def drop_user_mapping_stmt(node, output):
    output.write('DROP USER MAPPING')
    if node.missing_ok:
        output.write(' IF EXISTS')
    output.write(' FOR ')
    output.print_node(node.user)
    output.write(' SERVER ')
    output.print_node(node.servername, is_name=True)


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
        output.print_node(node.idxname, is_name=True)
    output.newline()
    with output.push_indent(2):
        output.write('ON ')
        output.print_node(node.relation)
        if node.accessMethod != 'btree':
            output.write('USING ')
            output.print_node(node.accessMethod, is_name=True)
        output.write(' (')
        output.print_list(node.indexParams)
        output.write(')')
        if node.options:
            output.newline()
            output.write('WITH (')
            output.print_list(node.options)
            output.write(')')
        if node.tableSpace:
            output.newline()
            output.write('TABLESPACE ')
            output.print_node(node.tableSpace, is_name=True)
        if node.whereClause:
            output.newline()
            output.write('WHERE ')
            output.print_node(node.whereClause)


@node_printer('ObjectWithArgs')
def object_with_args(node, output):
    if node.parent_node.removeType == enums.ObjectType.OBJECT_OPERATOR:
        output.write(node.objname.string_value)
        if not node.args_unspecified:
            output.write(' ')
    else:
        output.print_list(node.objname, '.', standalone_items=False, are_names=True)
    if not node.args_unspecified:
        output.write('(')
        output.print_list(node.objargs, ',', standalone_items=False)
        output.write(')')


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
        output.print_node(node.name, is_name=True)
    elif node.expr:
        output.print_node(node.expr)
    if node.collation or node.opclass:  # pragma: nocover
        raise NotImplementedError


@node_printer('PartitionRangeDatum')
def partition_range_datum(node, output):
    if node.kind == enums.PartitionRangeDatumKind.PARTITION_RANGE_DATUM_MINVALUE:
        output.write('MINVALUE')
    elif node.kind == enums.PartitionRangeDatumKind.PARTITION_RANGE_DATUM_MAXVALUE:
        output.write('MAXVALUE')
    else:
        output.print_node(node.value)


@node_printer('PartitionSpec')
def partition_spec(node, output):
    output.print_node(node.strategy)
    output.write(' (')
    output.print_list(node.partParams)
    output.write(')')


@node_printer('RoleSpec')
def role_spec(node, output):
    if node.roletype == enums.RoleSpecType.ROLESPEC_CURRENT_USER:
        output.write('CURRENT_USER')
    elif node.roletype == enums.RoleSpecType.ROLESPEC_SESSION_USER:
        output.write('SESSION_USER')
    elif node.roletype == enums.RoleSpecType.ROLESPEC_PUBLIC:
        output.write('PUBLIC')
    else:
        output.print_node(node.rolename, is_name=True)
