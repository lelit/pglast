# -*- coding: utf-8 -*-
# :Project:   pglast -- Printer function for SQL DDL nodes
# :Created:   gio 09 nov 2017 10:50:30 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019 Lele Gaifax
#

from .. import enums
from ..node import Missing, List, Node
from ..printer import node_printer
import re


@node_printer("AccessPriv")
def access_priv(node, output):
    output.print_node(node.priv_name)


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


@node_printer('AlterDatabaseStmt')
def alter_database_stmt(node, output):
    output.write("ALTER DATABASE ")
    output.print_name(node.dbname)
    output.print_list(node.options, ' ')


@node_printer('AlterDatabaseSetStmt')
def alter_database_set_stmt(node, output):
    output.write("ALTER DATABASE ")
    output.print_name(node.dbname)
    output.print_node(node.setstmt)


@node_printer('AlterEnumStmt')
def alter_enum_stmt(node, output):
    output.write("ALTER TYPE ")
    output.print_name(node.typeName)
    if node.newVal:
        output.write("ADD VALUE ")
        if node.skipIfNewValExists:
            output.write("IF NOT EXISTS ")
        output._write_quoted_string(node.newVal.value)
    if node.newValNeighbor:
        if node.newValIsAfter:
            output.write(" AFTER ")
        else:
            output.write(" BEFORE ")
        output._write_quoted_string(node.newValNeighbor.value)


GRANT_OBJECT_TYPES_NAMES = {
    enums.GrantObjectType.ACL_OBJECT_COLUMN: 'COLUMN',
    enums.GrantObjectType.ACL_OBJECT_RELATION: 'TABLE',
    enums.GrantObjectType.ACL_OBJECT_SEQUENCE: 'SEQUENCE',
    enums.GrantObjectType.ACL_OBJECT_DATABASE: 'DATABASE',
    enums.GrantObjectType.ACL_OBJECT_DOMAIN: 'DOMAIN',
    enums.GrantObjectType.ACL_OBJECT_FDW: 'FOREIGN DATA WRAPPER',
    enums.GrantObjectType.ACL_OBJECT_FOREIGN_SERVER: 'SERVER',
    enums.GrantObjectType.ACL_OBJECT_FUNCTION: 'FUNCTION',
    enums.GrantObjectType.ACL_OBJECT_LANGUAGE: 'LANGUAGE',
    enums.GrantObjectType.ACL_OBJECT_LARGEOBJECT: 'LARGEOBJECT',
    enums.GrantObjectType.ACL_OBJECT_NAMESPACE: 'SCHEMA',
    enums.GrantObjectType.ACL_OBJECT_TABLESPACE: 'TABLESPACE',
    enums.GrantObjectType.ACL_OBJECT_TYPE: 'TYPE'
}


@node_printer('AlterDefaultPrivilegesStmt')
def alter_default_privileges_stmt(node, output):
    output.writes('ALTER DEFAULT PRIVILEGES')
    roles = None
    schemas = None
    for opt in node.options:
        optname = opt.defname.value
        if optname == 'roles':
            roles = opt.arg
        elif optname == 'schemas':
            schemas = opt.arg
        else:
            raise NotImplementedError('Option not implemented: %s' % optname)
    if roles is not None:
        output.newline()
        with output.push_indent(2):
            output.write('FOR ROLE ')
            output.print_list(roles, ',')
    if schemas is not None:
        output.newline()
        with output.push_indent(2):
            output.write('IN SCHEMA ')
            output.print_list(schemas, ',', are_names=True)
    action = node.action
    output.newline()
    with output.push_indent(2):
        if action.is_grant:
            output.write('GRANT ')
            preposition = 'TO'
        else:
            output.write('REVOKE ')
            preposition = 'FROM'
        if action.grant_option:
            output.write('GRANT OPTION FOR ')
        if action.privileges:
            output.print_list(action.privileges, ',')
        else:
            output.write('ALL PRIVILEGES')
        output.write(' ON ')
        output.write(GRANT_OBJECT_TYPES_NAMES[action.objtype.value])
        output.write('S ')
        output.writes(preposition)
        output.print_list(action.grantees, ',')
        if action.behavior == enums.DropBehavior.DROP_CASCADE:
            output.newline()
            output.swrite('CASCADE')


@node_printer('AlterFunctionStmt')
def alter_function_stmt(node, output):
    output.write('ALTER FUNCTION ')
    output.print_node(node.func)
    output.print_list(node.actions, ' ')


@node_printer('AlterObjectSchemaStmt')
def alter_object_schema_stmt(node, output):
    objtype = node.objectType.value
    output.write("ALTER ")
    output.writes(OBJECT_NAMES[objtype])
    if objtype in (enums.ObjectType.OBJECT_TABLE,
                   enums.ObjectType.OBJECT_VIEW,
                   enums.ObjectType.OBJECT_FOREIGN_TABLE,
                   enums.ObjectType.OBJECT_MATVIEW):
        name = node.relation
    else:
        name = node.object
    output.print_name(name)
    output.write(" SET SCHEMA ")
    output.print_name(node.newschema)


@node_printer('AlterOwnerStmt')
def alter_owner_stmt(node, output):
    output.write("ALTER ")
    output.writes(OBJECT_NAMES[node.objectType.value])
    output.print_name(node.object)
    output.write('OWNER TO ')
    output.print_node(node.newowner)


@node_printer('AlterRoleStmt')
def alter_role_stmt(node, output):
    mapping = {
        'canlogin': ('LOGIN', True),
        'password': ('PASSWORD', False),
        'inherit': ('INHERIT', True),
        'connectionlimit': ('CONNECTION LIMIT', False),
        'validUntil': ('VALID UNTIL', False),
        'superuser': ('SUPERUSER', True),
        'createrole': ('CREATEROLE', True),
        'isreplication': ('REPLICATION', True),
        'createdb': ('CREATEDB', True),
        'bypassrls': ('BYPASSRLS', True)
    }
    output.write('ALTER ROLE ')
    output.print_node(node.role)
    for opt in node.options:
        optname, isbool = mapping[opt.defname.value]
        if isbool:
            if opt.arg.ival == 1:
                output.write(optname)
            else:
                output.write('NO')
                output.write(optname)
        else:
            output.writes(optname)
            output.print_node(opt.arg)


@node_printer('AlterSeqStmt')
def alter_seq_stmt(node, output):
    output.write("ALTER SEQUENCE ")
    output.print_node(node.sequence)
    if node.options:
        output.print_list(node.options, '')


@node_printer('AlterTableStmt')
def alter_table_stmt(node, output):
    output.write("ALTER ")
    output.writes(OBJECT_NAMES[node.relkind.value])
    if node.missing_ok:
        output.write("IF EXISTS ")
    output.print_node(node.relation)
    output.print_list(node.cmds, ',', standalone_items=True)


@node_printer('AlterTableCmd')
def alter_table_cmd(node, output):
    cmdtype = node.subtype

    if cmdtype == enums.AlterTableType.AT_ChangeOwner:
        output.write("OWNER TO ")
        output.print_name(node.newowner)
        return

    if cmdtype == enums.AlterTableType.AT_SetStatistics:
        output.write("ALTER COLUMN ")
        output.print_name(node.name)
        output.write(" SET STATISTICS ")
        output.print_node(node['def'])
        return

    if cmdtype == enums.AlterTableType.AT_ColumnDefault:
        output.write("ALTER COLUMN ")
        output.print_name(node.name)
        if node['def']:
            output.write(" SET DEFAULT ")
            output.print_node(node['def'])
        else:
            output.write(" DROP DEFAULT ")
        return

    if cmdtype == enums.AlterTableType.AT_AddConstraint:
        output.write("ADD ")
        constraint = node['def']
        output.print_node(constraint)
        # Patch this into pglast.printers.ddl.constraint
        # TODO: understand the meaning of the prev comment
        return

    if cmdtype == enums.AlterTableType.AT_DropConstraint:
        output.write("DROP CONSTRAINT ")
        if node.missing_ok:
            output.write("IF EXISTS ")
        output.print_name(node.name)
        return

    if cmdtype == enums.AlterTableType.AT_ClusterOn:
        output.write("CLUSTER ON ")
        output.print_name(node.name)
        return

    if cmdtype == enums.AlterTableType.AT_EnableRowSecurity:
        output.write(" ENABLE ROW LEVEL SECURITY ")
        return

    if cmdtype == enums.AlterTableType.AT_AddColumn:
        output.write("ADD COLUMN ")
        if node.missing_ok:
            output.write('IF NOT EXISTS ')
        output.print_node(node['def'])
        return

    if cmdtype == enums.AlterTableType.AT_ValidateConstraint:
        output.write("VALIDATE CONSTRAINT ")
        output.print_name(node.name)
        return

    if cmdtype == enums.AlterTableType.AT_DropNotNull:
        output.write("ALTER COLUMN ")
        output.print_name(node.name)
        output.write(" DROP NOT NULL ")
        return

    if cmdtype == enums.AlterTableType.AT_AlterColumnType:
        output.write("ALTER COLUMN ")
        output.print_name(node.name)
        output.write(" TYPE ")
        columndef = node['def']
        output.print_node(columndef)
        if columndef.raw_default:
            output.write('USING ')
            output.print_node(columndef.raw_default)
        return

    if cmdtype == enums.AlterTableType.AT_DropColumn:
        output.write("DROP COLUMN ")
        if node.missing_ok:
            output.write("IF EXISTS ")
        output.print_name(node.name)
        if node.behavior == enums.DropBehavior.DROP_CASCADE:
            output.write("CASCADE ")
        return

    if cmdtype == enums.AlterTableType.AT_SetNotNull:
        output.write("ALTER COLUMN ")
        output.print_name(node.name)
        output.write(" SET NOT NULL")
        return

    if cmdtype == enums.AlterTableType.AT_EnableTrig:
        output.write("ENABLE TRIGGER ")
        output.print_name(node.name)
        return

    if cmdtype == enums.AlterTableType.AT_DisableTrig:
        output.write("DISABLE TRIGGER ")
        output.print_name(node.name)
        return

    raise NotImplementedError("Unsupported alter table cmd: %s" % cmdtype)  # pragma: nocover


@node_printer('ClusterStmt')
def cluster_stmt(node, output):
    output.write('CLUSTER ')
    if node.verbose:
        output.write('VERBOSE ')
    output.print_name(node.relation)
    output.write(' USING ')
    output.print_name(node.indexname)


@node_printer('ColumnDef')
def column_def(node, output):
    if node.colname:
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


@node_printer('CompositeTypeStmt')
def composite_type_stmt(node, output):
    output.write('CREATE TYPE ')
    node.typevar.parse_tree['inh'] = True
    output.print_node(node.typevar)
    output.write(' AS (')
    output.print_list(node.coldeflist, ', ')
    output.write(')')
    node.typevar.parse_tree.pop('inh')


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
    elif node.contype == ct.CONSTR_ATTR_DEFERRABLE:
        output.swrite('DEFERRABLE')
    elif node.contype == ct.CONSTR_ATTR_DEFERRED:
        output.swrite('INITIALLY DEFERRED')
    elif node.contype == ct.CONSTR_FOREIGN:
        if node.fk_attrs:
            output.swrite('FOREIGN KEY ')
            output.write(' (')
            output.print_name(node.fk_attrs, ',')
            output.write(')')
        output.swrite('REFERENCES ')
        output.print_name(node.pktable)
        if node.pk_attrs:
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
        if node.deferrable:
            output.swrite('DEFERRABLE')
            if node.initdeferred:
                output.swrite('INITIALLY DEFERRED')

    if node.indexname:
        output.write(' USING INDEX ')
        output.print_name(node.indexname)
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
        if node.skip_validation:
            output.write(' NOT VALID ')


@node_printer('CreateAmStmt')
def create_am_stmt(node, output):
    output.write('CREATE ACCESS METHOD ')
    output.print_name(node.amname)
    if node.amtype == 'i':
        output.write(' TYPE INDEX HANDLER ')
        output.print_name(node.handler_name)
    else:  # pragma: nocover
        raise NotImplementedError


@node_printer('CreatedbStmt')
def create_db_stmt(node, output):
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


@node_printer('CreateEnumStmt')
def create_enum_stmt(node, output):
    output.write('CREATE TYPE ')
    output.print_name(node.typeName)
    output.write('AS ENUM (')
    output.print_list(node.vals)
    output.write(')')


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


@node_printer('CreateFunctionStmt')
def create_function_stmt(node, output):
    output.write('CREATE ')
    if node.replace:
        output.write('OR REPLACE ')
    output.write('FUNCTION ')
    output.print_name(node.funcname)
    output.write('(')

    # Functions returning a SETOF needs special care, because the resulting record
    # definition is intermixed with real parameters: split them into two separated
    # lists
    real_params = node.parameters
    if node.returnType and node.returnType.setof:
        fpm = enums.FunctionParameterMode
        record_def = []
        real_params = []
        for param in node.parameters:
            if param.mode == fpm.FUNC_PARAM_TABLE:
                record_def.append(Node(
                    {'ColumnDef': {
                        'typeName': {'TypeName': param.argType.parse_tree},
                        'colname': param.name.value}}))
            else:
                real_params.append(param)
    if real_params:
        output.print_list(real_params)
    output.write(')')

    if node.returnType:
        output.newline()
        output.writes('RETURNS')
        if node.returnType.setof and record_def:
            # Do not treat them as argument
            output.write('TABLE (')
            output.print_list(record_def, ',', standalone_items=False)
            output.write(')')
        else:
            output.print_node(node.returnType)

    for option in node.options:
        output.print_node(option)


@node_printer(('AlterFunctionStmt', 'CreateFunctionStmt', 'DoStmt'), 'DefElem')
def create_function_option(node, output):
    option = node.defname.value

    if option == 'as':
        if isinstance(node.arg, List) and len(node.arg) > 1:
            # We are in the weird C case
            output.write('AS ')
            output.print_list(node.arg)
            return

        if node.parent_node.node_tag == 'CreateFunctionStmt':
            output.newline()
            output.write('AS ')

        # Choose a valid dollar-string delimiter

        code = node.arg.string_value
        used_delimiters = set(re.findall(r"\$(\w*)\$", code))
        unique_delimiter = ''
        while unique_delimiter in used_delimiters:
            unique_delimiter += '_'

        # TODO: ideally, when the function is "LANGUAGE SQL", we could reparse
        # the statement and prettify it...

        output.write('$' + unique_delimiter + '$')
        output.write(code)
        output.write('$' + unique_delimiter + '$')
        return

    if option == 'security':
        if node.arg.ival == 1:
            output.swrite('SECURITY DEFINER')
        else:
            output.swrite('SECURITY INVOKER')
        return

    if option == 'strict':
        if node.arg.ival == 1:
            output.swrite('STRICT')
        return

    if option == 'volatility':
        output.separator()
        output.print_symbol(node.arg)
        return

    if option == 'parallel':
        output.swrite('PARALLEL SAFE')
        return

    if option == 'set':
        output.separator()
        output.print_node(node.arg)
        return

    output.writes(node.defname.value.upper())
    output.print_symbol(node.arg)


@node_printer('CreatePolicyStmt')
def create_policy_stmt(node, output):
    output.write('CREATE POLICY ')
    output.print_name(node.policy_name)
    output.write(' ON ')
    output.print_node(node.table)
    if node.permissive:
        output.write('AS PERMISSIVE ')
    else:
        output.write('AS RESTRICTIVE ')
    if node.cmd_name:
        output.write('FOR ')
        output.print_node(node.cmd_name)
    output.write(' TO ')
    output.print_list(node.roles, ',')
    if node.qual:
        output.write(' USING (')
        output.print_node(node.qual)
        output.write(')')
    if node.with_check:
        output.write(' WITH CHECK (')
        output.print_node(node.with_check)
        output.write(')')


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
@node_printer('AlterSeqStmt', 'DefElem')
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
    output.writes(OBJECT_NAMES[node.relkind.value])
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
    with output.push_indent():
        output.print_node(node.query)
    if node.into.skipData:
        output.newline()
        output.space(2)
        output.write('WITH NO DATA')


@node_printer('CreateTrigStmt')
def create_trig_stmt(node, output):
    output.write('CREATE ')
    if node.isconstraint:
        output.write('CONSTRAINT ')
    output.write('TRIGGER ')
    output.print_name(node.trigname)
    output.newline()
    with output.push_indent(2):
        if node.timing:
            if node.timing & enums.TRIGGER_TYPE_BEFORE:
                output.write('BEFORE ')
            elif node.timing & enums.TRIGGER_TYPE_INSTEAD:
                output.write('INSTEAD OF ')
        else:
            output.write('AFTER ')
        event_strings = []
        for ev in ('INSERT', 'DELETE', 'UPDATE'):
            bitmask = getattr(enums, 'TRIGGER_TYPE_%s' % ev)
            if node.events & bitmask:
                event_strings.append(ev)
        output.write(' OR '.join(event_strings))
        if node.columns:
            output.write(' OF ')
            output.print_list(node.columns, ',', are_names=True)

        output.newline()
        output.write('ON ')
        output.print_node(node.relation)

        if node.deferrable:
            output.swrite('DEFERRABLE')
            if node.initdeferred:
                output.swrite('INITIALLY DEFERRED')

        if node.transitionRels:
            output.swrite('REFERENCING ')
            output.print_list(node.transitionRels, ' ')

        output.newline()
        output.write('FOR EACH ')

        if node.row:
            output.write('ROW')
        else:
            output.write('STATEMENT')

        output.newline()
        with output.push_indent(2):
            if node.whenClause:
                output.write('WHEN (')
                with output.expression():
                    output.print_node(node.whenClause)
                output.write(')')
                output.newline()

            output.write('EXECUTE PROCEDURE ')
            output.print_name(node.funcname)
            output.write('(')
            if node.args:
                output.print_list(node.args, ',')
            output.write(')')


@node_printer('DefineStmt')
def define_stmt(node, output):
    output.write('CREATE ')
    output.writes(OBJECT_NAMES[node.kind.value])
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    output.print_list(node.defnames, '.', standalone_items=False, are_names=True,
                      is_symbol=node.kind == enums.ObjectType.OBJECT_OPERATOR)
    if node.args is not Missing:
        output.write(' (')
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
        if node.definition:
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


@node_printer('DiscardStmt')
def discard_stmt(node, output):
    output.write('DISCARD ')
    if node.target == enums.DiscardMode.DISCARD_ALL:
        output.write('ALL')
    elif node.target == enums.DiscardMode.DISCARD_PLANS:
        output.write('PLANS')
    elif node.target == enums.DiscardMode.DISCARD_SEQUENCES:
        output.write('SEQUENCES')
    elif node.target == enums.DiscardMode.DISCARD_TEMP:
        output.write('TEMP')
    else:
        raise NotImplementedError('Invalid target for discard: %s' %
                                  node.target)


@node_printer('DoStmt')
def do_stmt(node, output):
    output.write('DO ')
    output.print_list(node.args, sep=' ', standalone_items=True)


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
            on = nodes[:-1]
            output.print_name(nodes[-1])
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
        else:  # pragma: nocover
            raise NotImplementedError
    if node.name:
        output.print_name(node.name)
        output.write(' ')
    output.print_node(node.argType)
    if node.defexpr is not Missing:
        output.write(' = ')
        output.print_node(node.defexpr)


@node_printer('GrantStmt')
def grant_stmt(node, output):
    if node.is_grant:
        output.write('GRANT ')
        preposition = 'TO'
    else:
        output.write('REVOKE ')
        preposition = 'FROM'
    if node.privileges:
        output.print_list(node.privileges)
    else:
        output.write('ALL PRIVILEGES')
    object_name = GRANT_OBJECT_TYPES_NAMES[node.objtype.value]
    target = node.targtype
    output.newline()
    output.space(2)
    with output.push_indent():
        if target == enums.GrantTargetType.ACL_TARGET_OBJECT:
            output.write('ON ')
            output.writes(object_name)
        elif target == enums.GrantTargetType.ACL_TARGET_ALL_IN_SCHEMA:
            output.write('ON ALL ')
            output.write(object_name)
            output.writes('S IN SCHEMA')
        output.print_list(node.objects, are_names=True)
        output.newline()
        output.write(preposition)
        output.space()
        output.print_list(node.grantees, are_names=True)
        if node.grant_option:
            output.newline()
            output.write('WITH GRANT OPTION')


@node_printer('GrantRoleStmt')
def grant_role_stmt(node, output):
    if node.is_grant:
        output.write('GRANT ')
        preposition = 'TO'
    else:
        output.write('REVOKE ')
        preposition = 'FROM'

    output.print_list(node.granted_roles, ',')
    output.write(' ')
    output.write(preposition)
    output.write(' ')
    output.print_list(node.grantee_roles, ',')
    if node.admin_opt:
        output.write('WITH ADMIN OPTION')


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


LOCK_MODE_NAMES = {
    enums.AccessShareLock: 'ACCESS SHARE',
    enums.RowShareLock: 'ROW SHARE',
    enums.RowExclusiveLock: 'ROW EXCLUSIVE',
    enums.ShareUpdateExclusiveLock: 'SHARE UPDATE EXCLUSIVE',
    enums.ShareLock: 'SHARE',
    enums.ShareRowExclusiveLock: 'SHARE ROW EXCLUSIVE',
    enums.ExclusiveLock: 'EXCLUSIVE',
    enums.AccessExclusiveLock: 'ACCESS EXCLUSIVE'
}


@node_printer('LockStmt')
def lock_stmt(node, output):
    output.write('LOCK ')
    output.print_list(node.relations, ',')
    lock_mode = node.mode.value
    lock_str = LOCK_MODE_NAMES[lock_mode]
    output.write('IN ')
    output.write(lock_str)
    output.write(' MODE')
    if node.nowait:
        output.write(' NOWAIT')


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
        if node.objargs:
            output.print_list(node.objargs, ',', standalone_items=False)
        output.write(')')


@node_printer('PartitionBoundSpec')
def partition_bound_spec(node, output):
    if node.strategy == enums.PARTITION_STRATEGY_RANGE:
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


@node_printer('RenameStmt')
def rename_stmt(node, output):
    objtype = node.renameType.value
    if objtype == enums.ObjectType.OBJECT_COLUMN:
        reltype = node.relationType.value
        output.write('ALTER ')
        output.write(OBJECT_NAMES[reltype])
        output.space()
        output.print_node(node.relation)
        output.write(' RENAME COLUMN ')
        output.print_name(node.subname)
        output.write(' TO ')
        output.print_name(node.newname)
        return
    objtype_name = OBJECT_NAMES[objtype]
    output.write('ALTER ')
    output.write(objtype_name)
    output.space()
    if objtype in (enums.ObjectType.OBJECT_SCHEMA,
                   enums.ObjectType.OBJECT_DATABASE):
        output.write(node.subname.value)
    elif node.relation:
        output.print_node(node.relation)
    else:
        output.print_node(node.object)
    output.write(' RENAME TO ')
    output.print_name(node.newname)


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


@node_printer('TriggerTransition')
def trigger_transition(node, output):
    if node.isNew:
        output.write('NEW TABLE AS ')
    else:
        output.write('OLD TABLE AS ')
    output.print_name(node.name)


@node_printer('VacuumStmt')
def vacuum_stmt(node, output):
    optint = node.options.value
    options = []
    if optint & enums.VacuumOption.VACOPT_VACUUM:
        options.append('VACUUM')
    if optint & enums.VacuumOption.VACOPT_FULL:
        options.append('FULL')
    if optint & enums.VacuumOption.VACOPT_FREEZE:
        options.append('FREEZE')
    if optint & enums.VacuumOption.VACOPT_VERBOSE:
        options.append('VERBOSE')
    if optint & enums.VacuumOption.VACOPT_ANALYZE:
        options.append('ANALYZE')
    if optint & enums.VacuumOption.VACOPT_DISABLE_PAGE_SKIPPING:
        options.append('DISABLE_PAGE_SKIPPING')
    if 'VACUUM' in options:
        output.write('VACUUM ')
        options.remove('VACUUM')
    else:
        output.write('ANALYZE ')
        options.remove('ANALYZE')
    if options:
        # Try so emit a syntax compatible with PG < 11, if possible.
        if 'DISABLE_PAGE_SKIPPING' in options:
            output.write('(')
            output.print_list(Node(options, node), ',')
            output.write(') ')
        else:
            for option in options:
                output.write(option)
                output.space()
    if node.relation:
        output.print_node(node.relation)
        if node.va_cols:
            output.write('(')
            output.print_list(node.va_cols, ',', are_names=True)
            output.write(')')


@node_printer('ViewStmt')
def view_stmt(node, output):
    output.write('CREATE ')
    if node.replace:
        output.write('OR REPLACE ')
    output.write('VIEW ')
    output.print_node(node.view)
    output.newline()
    output.space(2)
    output.write('AS ')
    with output.push_indent():
        output.print_node(node.query)
