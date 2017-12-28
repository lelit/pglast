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
    output.print_name(node.colname)
    output.space()
    if node.typeName:
        output.print_name(node.typeName)
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


OBJECT_NAMES = {
    enums.ObjectType.OBJECT_ACCESS_METHOD: 'ACCESS METHOD',
    enums.ObjectType.OBJECT_AGGREGATE: 'AGGREGATE',
    enums.ObjectType.OBJECT_AMOP: 'AMOP',
    enums.ObjectType.OBJECT_AMPROC: 'AMPROC',
    enums.ObjectType.OBJECT_ATTRIBUTE: 'ATTRIBUTE',
    enums.ObjectType.OBJECT_CAST: 'CAST',
    enums.ObjectType.OBJECT_COLUMN: 'COLUMN',
    enums.ObjectType.OBJECT_COLLATION: 'COLLATION',
    enums.ObjectType.OBJECT_CONVERSION: 'CONVERSION',
    enums.ObjectType.OBJECT_DATABASE: 'DATABASE',
    enums.ObjectType.OBJECT_DEFAULT: 'DEFAULT',
    enums.ObjectType.OBJECT_DEFACL: 'DEFACL',
    enums.ObjectType.OBJECT_DOMAIN: 'DOMAIN',
    enums.ObjectType.OBJECT_DOMCONSTRAINT: 'CONSTRAINT',
    enums.ObjectType.OBJECT_EVENT_TRIGGER: 'EVENT TRIGGER',
    enums.ObjectType.OBJECT_EXTENSION: 'EXTENSION',
    enums.ObjectType.OBJECT_FDW: 'FOREIGN DATA WRAPPER',
    enums.ObjectType.OBJECT_FOREIGN_SERVER: 'SERVER',
    enums.ObjectType.OBJECT_FOREIGN_TABLE: 'FOREIGN TABLE',
    enums.ObjectType.OBJECT_FUNCTION: 'FUNCTION',
    enums.ObjectType.OBJECT_INDEX: 'INDEX',
    enums.ObjectType.OBJECT_LANGUAGE: 'LANGUAGE',
    enums.ObjectType.OBJECT_LARGEOBJECT: 'LARGE OBJECT',
    enums.ObjectType.OBJECT_MATVIEW: 'MATERIALIZED VIEW',
    enums.ObjectType.OBJECT_OPCLASS: 'OPERATOR CLASS',
    enums.ObjectType.OBJECT_OPERATOR: 'OPERATOR',
    enums.ObjectType.OBJECT_OPFAMILY: 'OPERATOR FAMILY',
    enums.ObjectType.OBJECT_POLICY: 'POLICY',
    enums.ObjectType.OBJECT_PUBLICATION: 'PUBLICATION',
    enums.ObjectType.OBJECT_PUBLICATION_REL: 'PUBLICATION_REL',
    enums.ObjectType.OBJECT_ROLE: 'ROLE',
    enums.ObjectType.OBJECT_RULE: 'RULE',
    enums.ObjectType.OBJECT_SCHEMA: 'SCHEMA',
    enums.ObjectType.OBJECT_SEQUENCE: 'SEQUENCE',
    enums.ObjectType.OBJECT_SUBSCRIPTION: 'SUBSCRIPTION',
    enums.ObjectType.OBJECT_STATISTIC_EXT: 'STATISTICS',
    enums.ObjectType.OBJECT_TABCONSTRAINT: 'CONSTRAINT',
    enums.ObjectType.OBJECT_TABLE: 'TABLE',
    enums.ObjectType.OBJECT_TABLESPACE: 'TABLESPACE',
    enums.ObjectType.OBJECT_TRANSFORM: 'TRANSFORM',
    enums.ObjectType.OBJECT_TRIGGER: 'TRIGGER',
    enums.ObjectType.OBJECT_TSCONFIGURATION: 'TEXT SEARCH CONFIGURATION',
    enums.ObjectType.OBJECT_TSDICTIONARY: 'TEXT SEARCH DICTIONARY',
    enums.ObjectType.OBJECT_TSPARSER: 'TEXT SEARCH PARSER',
    enums.ObjectType.OBJECT_TSTEMPLATE: 'TEXT SEARCH TEMPLATE',
    enums.ObjectType.OBJECT_TYPE: 'TYPE',
    enums.ObjectType.OBJECT_USER_MAPPING: 'USER_MAPPING',
    enums.ObjectType.OBJECT_VIEW: 'VIEW',
}


@node_printer('CommentStmt')
def comment_stmt(node, output):
    otypes = enums.ObjectType
    output.write('COMMENT ')
    output.write('ON ')
    output.writes(OBJECT_NAMES[node.objtype.value])
    if node.objtype in (otypes.OBJECT_OPCLASS, otypes.OBJECT_OPFAMILY):
        nodes = list(node.object)
        using = nodes.pop(0)
        output.print_name(nodes)
        output.write(' USING ')
        output.print_name(using)
    elif node.objtype in (otypes.OBJECT_TABCONSTRAINT, otypes.OBJECT_POLICY,
                          otypes.OBJECT_RULE, otypes.OBJECT_TRIGGER):
        nodes = list(node.object)
        output.print_name(nodes.pop())
        output.write(' ON ')
        output.print_name(nodes)
    elif node.objtype == otypes.OBJECT_DOMCONSTRAINT:
        nodes = list(node.object)
        output.print_name(nodes.pop())
        output.write(' ON DOMAIN ')
        output.print_name(nodes)
    elif node.objtype == otypes.OBJECT_TRANSFORM:
        nodes = list(node.object)
        output.write('FOR ')
        output.print_name(nodes.pop(0))
        output.write(' LANGUAGE ')
        output.print_name(nodes)
    elif isinstance(node.object, List):
        if node.object[0].node_tag != 'String':
            output.write(' (')
            output.print_list(node.object, ' AS ', standalone_items=False)
            output.write(')')
        else:
            output.print_name(node.object)
    else:
        output.print_name(node.object)
    output.newline()
    output.space(2)
    output.write('IS ')
    with output.push_indent():
        output._write_quoted_string(node.comment.value)


@node_printer('Constraint')
def constraint(node, output):
    if node.conname:
        output.swrite('CONSTRAINT ')
        output.print_name(node.conname)
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
            output.print_name(node.fk_attrs, ',')
            output.write(')')
        output.swrite('REFERENCES ')
        output.print_name(node.pktable)
        output.write(' (')
        output.print_name(node.pk_attrs, ',')
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
        output.print_name(node.keys, ',')
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
            output.print_name(node.indexspace)


@node_printer('CreateAmStmt')
def create_am_stmt(node, output):
    output.write('CREATE ACCESS METHOD ')
    output.print_name(node.amname)
    if node.amtype == 'i':
        output.write(' TYPE INDEX HANDLER ')
        output.print_name(node.handler_name)
    else:  # pragma: nocover
        raise NotImplementedError


@node_printer('CreateCastStmt')
def create_cast_stmt(node, output):
    output.write('CREATE CAST (')
    output.print_node(node.sourcetype)
    output.write(' AS ')
    output.print_node(node.targettype)
    output.write(') ')
    if node.func:
        output.write('WITH FUNCTION ')
        output.print_node(node.func)
    elif node.inout:
        output.write('WITH INOUT')
    else:
        output.write('WITHOUT FUNCTION')
    if node.context == enums.CoercionContext.COERCION_ASSIGNMENT:
        output.write(' AS ASSIGNMENT')
    elif node.context == enums.CoercionContext.COERCION_IMPLICIT:
        output.write(' AS IMPLICIT')


@node_printer('CreateConversionStmt')
def create_conversion_stmt(node, output):
    output.write('CREATE ')
    if node['def']:
        output.write('DEFAULT ')
    output.write('CONVERSION ')
    output.print_name(node.conversion_name)
    output.write(" FOR '%s' TO '%s'" % (node.for_encoding_name.value,
                                        node.to_encoding_name.value))
    output.write(' FROM ')
    output.print_name(node.func_name)


@node_printer('CreateDomainStmt')
def create_domain_stmt(node, output):
    output.write('CREATE DOMAIN ')
    output.print_name(node.domainname)
    output.write(' AS ')
    output.print_node(node.typeName)
    if node.collClause:
        output.print_node(node.collClause)
    if node.constraints:
        output.print_list(node.constraints, '', standalone_items=False)


@node_printer('CreateEventTrigStmt')
def create_event_trig_stmt(node, output):
    output.write('CREATE EVENT TRIGGER ')
    output.print_name(node.trigname)
    output.write(' ON ')
    output.print_name(node.eventname)
    output.newline()
    with output.push_indent(2):
        if node.whenclause:
            output.write('WHEN ')
            output.print_list(node.whenclause, 'AND', relative_indent=-4)
            output.newline()
        output.write('EXECUTE PROCEDURE ')
        output.print_name(node.funcname)
        output.write('()')


@node_printer('CreateEventTrigStmt', 'DefElem')
def create_event_trig_stmt_def_elem(node, output):
    output.print_name(node.defname)
    output.write(' IN (')
    output.print_list(node.arg, standalone_items=False)
    output.write(')')


@node_printer('CreateExtensionStmt')
def create_extension_stmt(node, output):
    output.write('CREATE EXTENSION ')
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    output.print_name(node.extname)
    if node.options:
        output.newline()
        output.space(2)
        output.write('WITH ')
        output.print_list(node.options, '')


@node_printer('CreateExtensionStmt', 'DefElem')
def create_extension_stmt_def_elem(node, output):
    option = node.defname.value
    if option == 'cascade':
        if node.arg.ival == 1:
            output.write('CASCADE')
    elif option == 'old_version':
        output.write('from ')
        output.print_node(node.arg)
    elif option == 'new_version':
        output.write('version ')
        output.print_node(node.arg)
    else:
        output.write(option)
        output.write(' ')
        if option == 'schema':
            output.print_name(node.arg)
        else:
            output.print_node(node.arg)


@node_printer('CreateFdwStmt')
def create_fdw_stmt(node, output):
    output.write('CREATE FOREIGN DATA WRAPPER ')
    output.print_name(node.fdwname)
    if node.func_options:
        output.newline()
        output.space(2)
        with output.push_indent():
            output.print_list(node.func_options, '')
    if node.options:
        output.newline()
        with output.push_indent(2):
            output.write('OPTIONS (')
            output.print_list(node.options)
            output.write(')')


@node_printer('CreateFdwStmt', 'DefElem')
def create_fdw_stmt_def_elem(node, output):
    if node.parent_attribute[0] == 'options':
        output.write(node.defname.value)
        output.write(' ')
        output.print_node(node.arg)
    else:
        output.write(node.defname.value.upper())
        output.write(' ')
        output.print_name(node.arg)


@node_printer('CreateForeignTableStmt')
def create_foreign_table_stmt(node, output):
    output.print_node(node.base)
    if not node.base.tableElts:
        output.newline()
        output.write(' ')
    output.write(' SERVER ')
    output.print_name(node.servername)
    if node.options:
        output.newline()
        with output.push_indent(2):
            output.write('OPTIONS (')
            output.print_list(node.options)
            output.write(')')


@node_printer('CreateForeignTableStmt', 'DefElem')
def create_foreign_table_stmt_def_elem(node, output):
    output.write(node.defname.value)
    output.write(' ')
    output.print_node(node.arg)


@node_printer('CreateSchemaStmt')
def create_schema_stmt(node, output):
    output.write('CREATE SCHEMA ')
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    if node.schemaname:
        output.print_name(node.schemaname)
    if node.authrole:
        output.swrite('AUTHORIZATION ')
        output.print_node(node.authrole)
    if node.schemaElts:
        output.newline()
        output.space(2)
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
        output.print_name(node.sequence.schemaname)
        output.write('.')
    output.print_name(node.sequence.relname)
    if node.options:
        output.newline()
        output.space(2)
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
        output.print_name(node.arg)
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
    if node.parent_node.node_tag == 'CreateForeignTableStmt':
        output.writes('FOREIGN')
    else:
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
        output.print_name(node.ofTypename)
    if node.partbound:
        output.write(' PARTITION OF ')
        output.print_list(node.inhRelations)
    if node.tableElts:
        output.write(' (')
        output.newline()
        output.space(2 if output.comma_at_eoln or len(node.tableElts) == 1 else 4)
        output.print_list(node.tableElts)
        output.newline()
        output.write(')')
    elif node.partbound:
        output.newline()
        output.write(' ')
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
            output.print_name(node.tablespacename)


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
        output.print_name(into.colNames, ',')
        output.write(')')
    output.newline()
    if into.options:
        if len(into.options) == 1 and into.options[0].defname == 'oids':
            output.space(2)
            output.write('WITH')
            if into.options[0].arg.ival.value == 0:
                output.write
                output.write('OUT')
            output.write(' OIDS')
        else:
            output.space(2)
            output.write('WITH (')
            output.print_list(into.options)
            output.write(')')
        output.newline()
    if into.onCommit != enums.OnCommitAction.ONCOMMIT_NOOP:
        output.space(2)
        output.write('ON COMMIT ')
        if into.onCommit == enums.OnCommitAction.ONCOMMIT_PRESERVE_ROWS:
            output.write('PRESERVE ROWS')
        elif into.onCommit == enums.OnCommitAction.ONCOMMIT_DELETE_ROWS:
            output.write('DELETE ROWS')
        elif into.onCommit == enums.OnCommitAction.ONCOMMIT_DROP:
            output.write('DROP')
        output.newline()
    if into.tableSpaceName:
        output.space(2)
        output.write('TABLESPACE ')
        output.print_name(into.tableSpaceName)
        output.newline()
    output.space(2)
    output.write('AS ')
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
        output.space(2)
        output.write('WITH NO DATA')


@node_printer('CreatedbStmt')
def createdb_stmt(node, output):
    output.write('CREATE DATABASE ')
    output.print_name(node.dbname)
    if node.options:
        output.newline()
        output.space(2)
        output.write('WITH ')
        output.print_list(node.options, '')


@node_printer('CreatedbStmt', 'DefElem')
def create_db_stmt_def_elem(node, output):
    option = node.defname.value
    if option == 'connection_limit':
        output.write('connection limit')
    else:
        output.print_node(node.defname)
    if node.arg is not Missing:
        output.write(' = ')
        if isinstance(node.arg, List) or option in ('allow_connections', 'is_template'):
            output.write(node.arg.string_value)
        else:
            output.print_node(node.arg)


@node_printer('DefineStmt')
def define_stmt(node, output):
    output.write('CREATE ')
    output.writes(OBJECT_NAMES[node.kind.value])
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    output.print_list(node.defnames, '.', standalone_items=False, are_names=True,
                      is_symbol=node.kind == enums.ObjectType.OBJECT_OPERATOR)
    output.write(' ')
    if node.args is not Missing:
        output.write('(')
        # args is actually a tuple (list-of-nodes, integer): the integer value, if different
        # from -1, is the number of nodes representing the actual arguments, remaining are
        # ORDER BY
        args, count = node.args
        count = count.ival.value
        if count == -1:
            output.print_list(args, standalone_items=False)
        else:
            output.print_list(args[:count], standalone_items=False)
            output.write(' ORDER BY ')
            output.print_list(args[count:], standalone_items=False)
        output.write(') ')
    if ((node.kind == enums.ObjectType.OBJECT_COLLATION
         and len(node.definition) == 1
         and node.definition[0].defname == 'from')):
        output.write('FROM ')
        output.print_name(node.definition[0].arg)
    else:
        output.write('(')
        output.newline()
        output.space(2 if output.comma_at_eoln or len(node.definition) == 1 else 4)
        output.print_list(node.definition)
        output.newline()
        output.write(')')


@node_printer('DefElem')
def def_elem(node, output):
    output.print_node(node.defname)
    if node.arg is not Missing:
        output.write(' = ')
        if isinstance(node.arg, List):
            output.write(node.arg.string_value)
        else:
            output.print_node(node.arg)
    if node.defaction != enums.DefElemAction.DEFELEM_UNSPEC:  # pragma: nocover
        raise NotImplementedError


@node_printer('DefineStmt', 'DefElem')
def define_stmt_def_elem(node, output):
    output.print_node(node.defname)
    if node.arg is not Missing:
        output.write(' = ')
        if isinstance(node.arg, List):
            is_symbol = node.defname in ('commutator', 'negator')
            if is_symbol and len(node.arg) > 1:
                output.write('OPERATOR(')
                output.print_symbol(node.arg)
                output.write(')')
            else:
                output.print_symbol(node.arg)
        else:
            output.print_node(node.arg)
    if node.defaction != enums.DefElemAction.DEFELEM_UNSPEC:  # pragma: nocover
        raise NotImplementedError


@node_printer('DropdbStmt')
def drop_db_stmt(node, output):
    output.write('DROP DATABASE')
    if node.missing_ok:
        output.write(' IF EXISTS')
    output.write(' ')
    output.print_name(node.dbname)


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
    output.writes(OBJECT_NAMES[node.removeType.value])
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
            output.print_name(nodes)
            output.write(' USING ')
            output.print_name(using)
        elif node.removeType == otypes.OBJECT_TRANSFORM:
            nodes = list(node.objects[0])
            output.write('FOR ')
            output.print_name(nodes.pop(0))
            output.write(' LANGUAGE ')
            output.print_name(nodes)
        elif node.removeType in (otypes.OBJECT_POLICY,
                                 otypes.OBJECT_RULE,
                                 otypes.OBJECT_TRIGGER):
            nodes = list(node.objects[0])
            on = nodes.pop(0)
            output.print_name(nodes)
            output.write(' ON ')
            output.print_name(on)
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
    output.print_name(node.subname)
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
    output.print_name(node.tablespacename)


@node_printer('DropUserMappingStmt')
def drop_user_mapping_stmt(node, output):
    output.write('DROP USER MAPPING')
    if node.missing_ok:
        output.write(' IF EXISTS')
    output.write(' FOR ')
    output.print_node(node.user)
    output.write(' SERVER ')
    output.print_name(node.servername)


@node_printer('FunctionParameter')
def function_parameter(node, output):
    if node.mode is not Missing:
        pm = enums.FunctionParameterMode
        if node.mode == pm.FUNC_PARAM_IN:
            pass  # omit the default, output.write('IN ')
        elif node.mode == pm.FUNC_PARAM_OUT:
            output.write('OUT ')
        elif node.mode == pm.FUNC_PARAM_INOUT:
            output.write('INOUT ')
        elif node.mode == pm.FUNC_PARAM_VARIADIC:
            output.write('VARIADIC ')
        else:
            raise NotImplementedError
    if node.name:
        output.print_name(node.name)
        output.write(' ')
    output.print_node(node.argType)
    if node.defexpr is not Missing:
        output.write(' = ')
        output.print_node(node.defexpr)


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
        output.print_name(node.idxname)
    output.newline()
    with output.push_indent(2):
        output.write('ON ')
        output.print_node(node.relation)
        if node.accessMethod != 'btree':
            output.write('USING ')
            output.print_name(node.accessMethod)
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
            output.print_name(node.tableSpace)
        if node.whereClause:
            output.newline()
            output.write('WHERE ')
            output.print_node(node.whereClause)


@node_printer('ObjectWithArgs')
def object_with_args(node, output):
    # Special treatment for OPERATOR object inside DROP or COMMENT
    if (((node.parent_node.removeType or node.parent_node.objtype)
         == enums.ObjectType.OBJECT_OPERATOR)):
        output.write(node.objname.string_value)
        if not node.args_unspecified:
            output.write(' ')
    else:
        output.print_name(node.objname)
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
        output.print_name(node.name)
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
        output.print_name(node.rolename)
