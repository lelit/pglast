# -*- coding: utf-8 -*-
# :Project:   pglast -- Printer function for SQL DDL nodes
# :Created:   gio 09 nov 2017 10:50:30 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2020, 2021, 2022 Lele Gaifax
#

import re

from .. import enums
from ..node import Missing, List
from . import IntEnumPrinter, node_printer


@node_printer('AccessPriv')
def access_priv(node, output):
    if node.priv_name is Missing:
        output.write('ALL PRIVILEGES')
    else:
        output.write(node.priv_name.value.upper())
    if node.cols is not Missing:
        output.write(' (')
        output.print_list(node.cols, ',', are_names=True)
        output.write(')')


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
    enums.ObjectType.OBJECT_PROCEDURE: 'PROCEDURE',
    enums.ObjectType.OBJECT_PUBLICATION: 'PUBLICATION',
    enums.ObjectType.OBJECT_PUBLICATION_REL: 'PUBLICATION_REL',
    enums.ObjectType.OBJECT_ROLE: 'ROLE',
    enums.ObjectType.OBJECT_ROUTINE: 'ROUTINE',
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


@node_printer('AlterCollationStmt')
def alter_collation_stmt(node, output):
    output.write('ALTER COLLATION ')
    output.print_name(node.collname)
    output.write(' REFRESH VERSION')


@node_printer('AlterDatabaseStmt')
def alter_database_stmt(node, output):
    output.write('ALTER DATABASE ')
    output.print_name(node.dbname)
    output.print_list(node.options, ' ')


@node_printer('AlterDatabaseSetStmt')
def alter_database_set_stmt(node, output):
    output.write('ALTER DATABASE ')
    output.print_name(node.dbname)
    output.print_node(node.setstmt)


@node_printer('AlterExtensionStmt')
def alter_extension_stmt(node, output):
    output.write('ALTER EXTENSION ')
    output.print_name(node.extname)
    output.print_list(node.options, '')


@node_printer('AlterExtensionStmt', 'DefElem')
def alter_extension_stmt_def_elem(node, output):
    option = node.defname.value
    if option == 'new_version':
        output.write('UPDATE TO ')
        output.print_node(node.arg)
    else:
        raise NotImplementedError('Option not implemented: %s' % option)


@node_printer('AlterExtensionContentsStmt')
def alter_extension_contents_stmt(node, output):
    output.write('ALTER EXTENSION ')
    output.print_name(node.extname)
    if node.action == -1:
        output.write(' DROP ')
    else:
        output.write(' ADD ')
    output.write(OBJECT_NAMES[node.objtype.value])
    output.write(' ')
    output.print_node(node.object)


@node_printer('AlterEnumStmt')
def alter_enum_stmt(node, output):
    output.write('ALTER TYPE ')
    output.print_name(node.typeName)
    if node.newVal:
        if node.oldVal:
            output.write('RENAME VALUE ')
            output.write_quoted_string(node.oldVal.value)
            output.write('TO ')
        else:
            output.write('ADD VALUE ')
            if node.skipIfNewValExists:
                output.write('IF NOT EXISTS ')
        output.write_quoted_string(node.newVal.value)
    if node.newValNeighbor:
        if node.newValIsAfter:
            output.write(' AFTER ')
        else:
            output.write(' BEFORE ')
        output.write_quoted_string(node.newValNeighbor.value)


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
        else:  # pragma: no cover
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
        output.write(OBJECT_NAMES[action.objtype.value])
        output.write('S ')
        output.writes(preposition)
        output.print_list(action.grantees, ',')
        if action.behavior == enums.DropBehavior.DROP_CASCADE:
            output.newline()
            output.write('CASCADE')


@node_printer('AlterFunctionStmt')
def alter_function_stmt(node, output):
    output.write('ALTER ')
    if node.objtype == enums.ObjectType.OBJECT_PROCEDURE:
        output.write('PROCEDURE ')
    else:
        output.write('FUNCTION ')
    output.print_node(node.func)
    output.print_list(node.actions, ' ')


@node_printer('AlterObjectSchemaStmt')
def alter_object_schema_stmt(node, output):
    OT = enums.ObjectType
    objtype = node.objectType
    output.write('ALTER ')
    output.writes(OBJECT_NAMES[objtype])
    if node.missing_ok:
        output.write(' IF EXISTS ')
    if objtype in (OT.OBJECT_TABLE,
                   OT.OBJECT_VIEW,
                   OT.OBJECT_FOREIGN_TABLE,
                   OT.OBJECT_MATVIEW):
        output.print_name(node.relation)
    else:
        if objtype in (OT.OBJECT_OPFAMILY,
                       OT.OBJECT_OPCLASS):
            method, *name = node.object
            output.print_name(name)
            output.write(' USING ')
            output.print_symbol(method)
        else:
            output.print_name(node.object)
    output.write(' SET SCHEMA ')
    output.print_name(node.newschema)


@node_printer('AlterOperatorStmt')
def alter_operator_stmt(node, output):
    output.write('ALTER OPERATOR ')
    output.print_node(node.opername)
    output.write(' SET (')
    output.print_list(node.options)
    output.write(')')


@node_printer('AlterOperatorStmt', 'DefElem')
def alter_operator_stmt_def_elem(node, output):
    if node.defnamespace:
        # FIXME: find a way to get here
        output.print_name(node.defnamespace)
        output.write('.')
    output.print_name(node.defname)
    output.write(' = ')
    if node.arg:
        output.print_symbol(node.arg)
    else:
        output.write('NONE')


@node_printer('AlterOpFamilyStmt')
def alter_op_family_stmt(node, output):
    output.write('ALTER OPERATOR FAMILY ')
    output.print_name(node.opfamilyname)
    output.write(' USING ')
    output.print_name(node.amname)
    output.newline()
    output.space(2)
    output.write('DROP ' if node.isDrop else ' ADD ')
    output.print_list(node.items)


@node_printer('AlterOwnerStmt')
def alter_owner_stmt(node, output):
    output.write('ALTER ')
    output.writes(OBJECT_NAMES[node.objectType.value])
    OT = enums.ObjectType
    if node.objectType in (OT.OBJECT_OPFAMILY,
                           OT.OBJECT_OPCLASS):
        method, name = node.object
        output.print_name(name)
        output.write(' USING ')
        output.print_symbol(method)
    else:
        output.print_name(node.object)
    output.write('OWNER TO ')
    output.print_node(node.newowner)


@node_printer('AlterPolicyStmt')
def alter_policy_stmt(node, output):
    output.write('ALTER POLICY ')
    output.print_name(node.policy_name)
    output.write(' ON ')
    output.print_node(node.table)
    if node.roles:
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


@node_printer('AlterRoleStmt')
def alter_role_stmt(node, output):
    if len(node.options) == 1 and node.options[0].defname == 'rolemembers':
        output.write('ALTER GROUP ')
        output.print_node(node.role)
        if node.action == 1:
            output.write('ADD USER ')
        elif node.action == -1:
            output.write('DROP USER ')
        output.print_list(node.options[0].arg, ',')
    else:
        output.write('ALTER ROLE ')
        output.print_node(node.role)
        output.print_list(node.options, sep=' ')


@node_printer('AlterSeqStmt')
def alter_seq_stmt(node, output):
    output.write('ALTER SEQUENCE ')
    if node.missing_ok:
        output.write('IF EXISTS ')
    output.print_node(node.sequence)
    if node.options:
        output.print_list(node.options, '')


@node_printer('AlterTableStmt')
def alter_table_stmt(node, output):
    output.write('ALTER ')
    output.writes(OBJECT_NAMES[node.relkind.value])
    if node.missing_ok:
        output.write('IF EXISTS ')
    output.print_node(node.relation)
    if len(node.cmds) > 1:
        output.newline()
        output.space(4)
        with output.push_indent():
            output.print_list(node.cmds, ',')
    else:
        output.print_list(node.cmds, ',', standalone_items=True)


def alter_def_elem(node, output):
    if node:
        output.write(' OPTIONS (')
        first = True
        for option in node:
            if first:
                first = False
            else:
                output.write(', ')
            if option.defaction == enums.DefElemAction.DEFELEM_UNSPEC:
                output.print_name(option.defname)
                output.write(' ')
                output.print_node(option.arg)
            elif option.defaction == enums.DefElemAction.DEFELEM_SET:
                output.write('SET ')
                output.print_name(option.defname)
                output.write(' ')
                output.print_node(option.arg)
            elif option.defaction == enums.DefElemAction.DEFELEM_ADD:
                output.write('ADD ')
                output.print_name(option.defname)
                output.write(' ')
                output.print_node(option.arg)
            elif option.defaction == enums.DefElemAction.DEFELEM_DROP:
                output.write('DROP ')
                output.print_name(option.defname)
        output.write(')')


@node_printer('AlterTableStmt', 'RangeVar')
def range_var(node, output):
    if node.parent_node.relkind == enums.ObjectType.OBJECT_TABLE and not node.inh:
        output.write('ONLY ')
    if node.schemaname:
        output.print_name(node.schemaname)
        output.write('.')
    output.print_name(node.relname)
    alias = node.alias
    if alias:
        # FIXME: find a way to get here
        output.write(' AS ')
        output.print_name(alias)


class AlterTableTypePrinter(IntEnumPrinter):
    enum = enums.AlterTableType

    def AT_AddColumn(self, node, output):
        output.write('ADD ')
        if node.parent_node.relkind == enums.ObjectType.OBJECT_TYPE:
            output.write('ATTRIBUTE ')
        else:
            output.write('COLUMN ')
        if node.missing_ok:
            output.write('IF NOT EXISTS ')
        output.print_node(node.def_)

    def AT_AddConstraint(self, node, output):
        output.write('ADD ')
        output.print_node(node.def_)

    def AT_AddInherit(self, node, output):
        output.write('INHERIT ')
        output.print_node(node.def_)

    def AT_AddOf(self, node, output):
        output.write('OF ')
        output.print_node(node.def_)

    def AT_AlterColumnType(self, node, output):
        output.write('ALTER ')
        if node.parent_node.relkind == enums.ObjectType.OBJECT_TYPE:
            output.write('ATTRIBUTE ')
        else:
            output.write('COLUMN ')
        output.print_name(node.name)
        output.write(' TYPE ')
        columndef = node.def_
        output.print_node(columndef)
        if columndef.raw_default:
            output.write('USING ')
            output.print_node(columndef.raw_default)

    def AT_AlterConstraint(self, node, output):
        output.write('ALTER ')
        output.print_node(node.def_)

    def AT_AttachPartition(self, node, output):
        output.write('ATTACH PARTITION ')
        output.print_node(node.def_)

    def AT_ChangeOwner(self, node, output):
        output.write('OWNER TO ')
        output.print_name(node.newowner)

    def AT_ClusterOn(self, node, output):
        output.write('CLUSTER ON ')
        output.print_name(node.name)

    def AT_ColumnDefault(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        if node.def_:
            output.write(' SET DEFAULT ')
            output.print_node(node.def_)
        else:
            output.write(' DROP DEFAULT ')

    def AT_DetachPartition(self, node, output):
        output.write('DETACH PARTITION ')
        output.print_name(node.def_)

    def AT_DisableRowSecurity(self, node, output):
        output.write(' DISABLE ROW LEVEL SECURITY ')

    def AT_DisableTrig(self, node, output):
        output.write('DISABLE TRIGGER ')
        output.print_name(node.name)

    def AT_DropCluster(self, node, output):
        output.write('SET WITHOUT CLUSTER')

    def AT_DropColumn(self, node, output):
        output.write('DROP ')
        if node.parent_node.relkind == enums.ObjectType.OBJECT_TYPE:
            output.write('ATTRIBUTE ')
        else:
            output.write('COLUMN ')
        if node.missing_ok:
            output.write('IF EXISTS ')
        output.print_name(node.name)

    def AT_DropConstraint(self, node, output):
        output.write('DROP CONSTRAINT ')
        if node.missing_ok:
            output.write('IF EXISTS ')
        output.print_name(node.name)

    def AT_DropInherit(self, node, output):
        output.write('NO INHERIT ')
        output.print_node(node.def_)

    def AT_DropNotNull(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        output.write(' DROP NOT NULL ')

    def AT_DropOf(self, node, output):
        output.write('NOT OF')

    def AT_DropOids(self, node, output):
        output.write('SET WITHOUT OIDS')

    def AT_EnableRowSecurity(self, node, output):
        output.write(' ENABLE ROW LEVEL SECURITY ')

    def AT_EnableTrig(self, node, output):
        output.write('ENABLE TRIGGER ')
        output.print_name(node.name)

    def AT_ForceRowSecurity(self, node, output):
        output.write('FORCE ROW LEVEL SECURITY ')

    def AT_ReplicaIdentity(self, node, output):
        output.print_node(node.def_)

    def AT_ResetOptions(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        output.write(' RESET (')
        with output.push_indent():
            output.print_list(node.def_)
        output.write(')')

    def AT_ResetRelOptions(self, node, output):
        output.write('RESET (')
        with output.push_indent():
            output.print_list(node.def_)
        output.write(')')

    def AT_SetNotNull(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        output.write(' SET NOT NULL')

    def AT_SetRelOptions(self, node, output):
        output.write('SET (')
        with output.push_indent():
            output.print_list(node.def_)
        output.write(')')

    def AT_SetStatistics(self, node, output):
        output.write('ALTER COLUMN ')
        if node.name:
            output.print_name(node.name)
        elif node.num:
            output.write(str(node.num.value))
        output.write(' SET STATISTICS ')
        output.print_node(node.def_)

    def AT_SetStorage(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        output.write(' SET STORAGE ')
        output.write(node.def_.val.value)

    def AT_SetUnLogged(self, node, output):
        output.write('SET UNLOGGED')

    def AT_SetLogged(self, node, output):
        output.write('SET LOGGED')

    def AT_SetOptions(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        output.write(' SET (')
        with output.push_indent():
            output.print_list(node.def_)
        output.write(')')

    def AT_ValidateConstraint(self, node, output):
        output.write('VALIDATE CONSTRAINT ')
        output.print_name(node.name)

    def AT_AlterColumnGenericOptions(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        alter_def_elem(node.def_, output)

    def AT_GenericOptions(self, node, output):
        alter_def_elem(node.def_, output)

    def AT_SetTableSpace(self, node, output):
        output.write('SET TABLESPACE ')
        output.print_name(node.name)

    def AT_DropExpression(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        output.write('DROP EXPRESSION')
        if node.missing_ok:
            output.write(' IF EXISTS')

    def AT_AddIdentity(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        if node.num.value > 0:
            # FIXME: find a way to get here
            output.print_node(node.num)
        output.write(' ADD ')
        if node.def_:
            output.print_node(node.def_)

    def AT_DropIdentity(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        if node.num.value > 0:
            # FIXME: find a way to get here
            output.print_node(node.num)
        output.write(' DROP IDENTITY ')
        if node.missing_ok:
            output.write('IF EXISTS ')

    def AT_NoForceRowSecurity(self, node, output):
        output.write('NO FORCE ROW LEVEL SECURITY ')

    def AT_EnableRule(self, node, output):
        output.write('ENABLE RULE ')
        output.print_name(node.name)

    def AT_DisableRule(self, node, output):
        output.write('DISABLE RULE ')
        output.print_name(node.name)

    def AT_EnableReplicaRule(self, node, output):
        output.write('ENABLE REPLICA RULE ')
        output.print_name(node.name)

    def AT_DisableTrigUser(self, node, output):
        output.write('DISABLE TRIGGER USER')

    def AT_EnableReplicaTrig(self, node, output):
        output.write('ENABLE REPLICA TRIGGER ')
        output.print_name(node.name)

    def AT_EnableAlwaysTrig(self, node, output):
        output.write('ENABLE ALWAYS TRIGGER ')
        output.print_name(node.name)

    def AT_DisableTrigAll(self, node, output):
        output.write('DISABLE TRIGGER ALL ')

    def AT_SetIdentity(self, node, output):
        output.write('ALTER COLUMN ')
        output.print_name(node.name)
        if node.num.value > 0:
            # FIXME: find a way to get here
            output.print_node(node.num)
        for elem in node.def_:
            if elem.defname == 'restart':
                output.write('RESTART')
                if elem.arg:
                    output.write(' WITH ')
                    output.print_node(elem.arg)
            else:
                output.write(' SET ')
                if elem.defname == 'cache':
                    output.write('CACHE ')
                    output.print_node(elem.arg)
                elif elem.defname == 'cycle':
                    if elem.arg.val.value == 0:
                        output.write('NO ')
                    output.write('CYCLE')
                elif elem.defname == 'increment':
                    output.write('INCREMENT BY ')
                    output.print_node(elem.arg)
                elif elem.defname == 'maxvalue':
                    if not elem.arg:
                        output.write('NO ')
                    output.write('MAXVALUE')
                    if elem.arg:
                        output.write(' ')
                        output.print_node(elem.arg)
                elif elem.defname == 'minvalue':
                    if not elem.arg:
                        output.write('NO ')
                    output.write('MINVALUE')
                    if elem.arg:
                        output.write(' ')
                        output.print_node(elem.arg)
                elif elem.defname == 'sequence_name':
                    output.write('SEQUENCE NAME ')
                    output.print_name(elem.arg)
                elif elem.defname == 'start':
                    output.write('START WITH ')
                    output.print_node(elem.arg)
                elif elem.defname == 'generated':
                    output.write('GENERATED ')
                    if elem.arg.val == 97:
                        output.write('ALWAYS')
                    elif elem.arg.val == 100:
                        output.write('BY DEFAULT')


alter_table_type_printer = AlterTableTypePrinter()


@node_printer('AlterTableCmd')
def alter_table_cmd(node, output):
    alter_table_type_printer(node.subtype, node, output)
    if node.behavior == enums.DropBehavior.DROP_CASCADE:
        output.swrite('CASCADE')


@node_printer('AlterTableCmd', 'DefElem')
@node_printer('CreatePublicationStmt', 'DefElem')
@node_printer('CreateStmt', 'DefElem')
@node_printer('IndexStmt', 'DefElem')
@node_printer('IntoClause', 'DefElem')
def alter_table_cmd_def_elem(node, output):
    if node.defnamespace:
        output.print_name(node.defnamespace)
        output.write('.')
    output.print_name(node.defname)
    if node.arg:
        output.write(' = ')
        output.print_node(node.arg)


class AlterTSConfigTypePrinter(IntEnumPrinter):
    enum = enums.AlterTSConfigType

    def print_simple_name(self, node, output):
        if isinstance(node, List):
            node = node[0]
        output.write(node.val.value)

    def print_simple_list(self, nodes, output):
        first = True
        for node in nodes:
            if not first:
                output.write(', ')
            else:
                first = False
            self.print_simple_name(node, output)

    def ALTER_TSCONFIG_ADD_MAPPING(self, node, output):
        output.newline()
        output.space(2)
        with output.push_indent():
            output.write('ADD MAPPING FOR ')
            self.print_simple_list(node.tokentype, output)
            output.newline()
        output.write(' WITH ')
        self.print_simple_list(node.dicts, output)

    def ALTER_TSCONFIG_ALTER_MAPPING_FOR_TOKEN(self, node, output):
        output.newline()
        output.space(2)
        with output.push_indent():
            output.write('ALTER MAPPING FOR ')
            self.print_simple_list(node.tokentype, output)
            output.newline()
        output.write('WITH ')
        self.print_simple_list(node.dicts, output)

    def ALTER_TSCONFIG_REPLACE_DICT(self, node, output):
        output.newline()
        output.space(2)
        with output.push_indent():
            output.write('ALTER MAPPING REPLACE ')
            old, new = node.dicts
            self.print_simple_name(old, output)
            output.newline()
        output.write(' WITH ')
        self.print_simple_name(new, output)

    def ALTER_TSCONFIG_REPLACE_DICT_FOR_TOKEN(self, node, output):
        output.newline()
        output.space(2)
        with output.push_indent():
            output.write('ALTER MAPPING FOR ')
            self.print_simple_list(node.tokentype, output)
            output.newline()
            output.write('REPLACE ')
            old, new = node.dicts
            self.print_simple_name(old, output)
            output.newline()
        output.write(' WITH ')
        self.print_simple_name(new, output)

    def ALTER_TSCONFIG_DROP_MAPPING(self, node, output):
        output.newline()
        output.space(2)
        with output.push_indent():
            output.write('DROP MAPPING ')
            if node.missing_ok:
                output.write('IF EXISTS ')
            output.write('FOR ')
            self.print_simple_list(node.tokentype, output)


alter_ts_config_type_printer = AlterTSConfigTypePrinter()


@node_printer('AlterTSConfigurationStmt')
def alter_ts_configuration_stmt(node, output):
    output.write('ALTER TEXT SEARCH CONFIGURATION ')
    output.print_name(node.cfgname)
    output.write(' ')
    alter_ts_config_type_printer(node.kind, node, output)


@node_printer('AlterTSDictionaryStmt')
def alter_ts_dictionary_stmt(node, output):
    output.write('ALTER TEXT SEARCH DICTIONARY ')
    output.print_name(node.dictname)
    output.write(' (')
    if len(node.options) > 1:
        output.newline()
        output.space(2 if output.comma_at_eoln else 4)
    output.print_list(node.options)
    if len(node.options) > 1:
        output.newline()
    output.write(')')


@node_printer('AlterStatsStmt')
def alter_stats_stmt(node, output):
    output.write('ALTER STATISTICS ')
    if node.missing_ok:
        output.write('IF EXISTS ')
    output.print_name(node.defnames)
    output.write(' SET STATISTICS ')
    output.print_node(node.stxstattarget)


@node_printer('AlterSubscriptionStmt')
def alter_subscription_stmt(node, output):
    output.write('ALTER SUBSCRIPTION ')
    output.print_name(node.subname)
    if node.kind == enums.AlterSubscriptionType.ALTER_SUBSCRIPTION_OPTIONS:
        output.write('SET (')
        output.print_name(node.options)
        output.write(')')
    elif node.kind == enums.AlterSubscriptionType.ALTER_SUBSCRIPTION_CONNECTION:
        output.write('CONNECTION ')
        output.print_node(node.conninfo)
    elif node.kind == enums.AlterSubscriptionType.ALTER_SUBSCRIPTION_REFRESH:
        output.write('REFRESH PUBLICATION')
        if node.options:
            output.write(' WITH (')
            output.print_list(node.options)
            output.write(')')
    elif node.kind == enums.AlterSubscriptionType.ALTER_SUBSCRIPTION_PUBLICATION:
        output.write('SET PUBLICATION ')
        output.print_list(node.publication, ',', are_names=True)
        output.write(' WITH (')
        output.print_list(node.options)
        output.write(')')
    elif node.kind == enums.AlterSubscriptionType.ALTER_SUBSCRIPTION_ENABLED:
        if node.options[0].arg.val.value == 0:
            output.write('DISABLE')
        elif node.options[0].arg.val.value == 1:
            output.write('ENABLE')


@node_printer('AlterPublicationStmt')
def alter_publication_stmt(node, output):
    output.write('ALTER PUBLICATION ')
    output.print_name(node.pubname)
    output.write(' ')
    if node.tables:
        if node.tableAction == enums.DefElemAction.DEFELEM_SET:
            output.write('SET TABLE ')
        elif node.tableAction == enums.DefElemAction.DEFELEM_ADD:
            output.write('ADD TABLE ')
        elif node.tableAction == enums.DefElemAction.DEFELEM_DROP:
            output.write('DROP TABLE ')
        output.print_list(node.tables, ',')
    elif node.options:
        output.write('SET (')
        output.print_list(node.options, ',')
        output.write(')')


@node_printer('AlterFdwStmt')
def alter_fdw_stmt(node, output):
    output.write('ALTER FOREIGN DATA WRAPPER ')
    output.print_name(node.fdwname)
    if node.func_options:
        output.print_list(node.func_options, '')
    if node.options:
        alter_def_elem(node.options, output)


@node_printer('AlterFdwStmt', 'DefElem')
def alter_fdw_stmt_def_elem(node, output):
    if node.defname == "handler":
        if node.arg:
            output.writes('HANDLER')
        else:
            output.writes('NO HANDLER')
    elif node.defname == "validator":
        if node.arg:
            output.writes('VALIDATOR')
        else:
            output.writes('NO VALIDATOR')
    if node.arg:
        output.print_name(node.arg)


@node_printer('AlterForeignServerStmt')
def alter_foreign_server_stmt(node, output):
    output.write('ALTER SERVER ')
    output.print_name(node.servername)
    if node.has_version:
        output.write(' VERSION ')
        if node.version:
            output.print_node(node.version)
        else:
            output.write('NULL')
    alter_def_elem(node.options, output)


@node_printer('AlterUserMappingStmt')
def alter_user_mapping_stmt(node, output):
    output.write('ALTER USER MAPPING FOR ')
    role_spec(node.user, output)
    output.writes(' SERVER ')
    output.write(node.servername.value)
    alter_def_elem(node.options, output)


@node_printer('AlterRoleSetStmt')
def alter_role_set_stmt(node, output):
    output.write('ALTER ROLE ')
    if not node.role:
        output.write('ALL')
    else:
        output.print_node(node.role)
    output.write(' ')
    if node.database:
        output.write('IN DATABASE ')
        output.print_name(node.database)
        output.write(' ')
    output.print_node(node.setstmt)


@node_printer('AlterDomainStmt')
def alter_domain_stmt(node, output):
    output.write('ALTER DOMAIN ')
    output.print_name(node.typeName)
    if node.subtype == 'T':
        if node.def_:
            output.write(' SET DEFAULT ')
            output.print_node(node.def_)
        else:
            output.write(' DROP DEFAULT')
    elif node.subtype == 'N':
        output.write(' DROP NOT NULL')
    elif node.subtype == 'O':
        output.write(' SET NOT NULL')
    elif node.subtype == 'C':
        output.write(' ADD ')
        output.print_node(node.def_)
    elif node.subtype == 'X':
        output.write(' DROP CONSTRAINT ')
        if node.missing_ok:
            output.write('IF EXISTS ')
        output.print_name(node.name)
        if node.behavior == enums.DropBehavior.DROP_CASCADE:
            output.write(' CASCADE')
    elif node.subtype == 'V':
        output.write(' VALIDATE CONSTRAINT ')
        output.print_name(node.name)
    else:
        raise NotImplementedError


@node_printer('AlterEventTrigStmt')
def alter_event_trig_stmt(node, output):
    output.write('ALTER EVENT TRIGGER ')
    output.print_name(node.trigname)
    if node.tgenabled == 'O':
        output.write(' ENABLE')
    elif node.tgenabled == 'A':
        output.write(' ENABLE ALWAYS')
    elif node.tgenabled == 'R':
        output.write(' ENABLE REPLICA')
    elif node.tgenabled == 'D':
        output.write(' DISABLE')


@node_printer('AlterTypeStmt')
def alter_type_stmt(node, output):
    output.write('ALTER TYPE ')
    output.print_name(node.typeName)
    output.write(' SET (')
    output.print_list(node.options, ',')
    output.write(')')


@node_printer('CheckPointStmt')
def check_point_stmt(node, output):
    output.write('CHECKPOINT')


@node_printer('ClusterStmt')
def cluster_stmt(node, output):
    output.write('CLUSTER ')
    if (node.options or 0) & enums.ClusterOption.CLUOPT_VERBOSE:
        output.write('VERBOSE ')
    if node.relation:
        output.print_name(node.relation)
    if node.indexname:
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
    if node.fdwoptions:
        output.write(' OPTIONS (')
        output.print_list(node.fdwoptions, ',')
        output.write(')')
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
    elif node.objtype == otypes.OBJECT_AGGREGATE:
        _object_with_args(node.object, output, empty_placeholder='*')
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
    if node.comment:
        with output.push_indent():
            output.write_quoted_string(node.comment.value)
    else:
        output.write('NULL')


@node_printer('CompositeTypeStmt')
def composite_type_stmt(node, output):
    output.write('CREATE TYPE ')
    output.print_node(node.typevar)
    output.write(' AS (')
    if node.coldeflist:
        output.print_list(node.coldeflist, ', ')
    output.write(')')


@node_printer('CompositeTypeStmt', 'RangeVar')
def composite_type_stmt_range_var(node, output):
    # Ignore the inh attribute, that in the normal implementation emits "ONLY" when it is False
    if node.schemaname:
        output.print_name(node.schemaname)
        output.write('.')
    output.print_name(node.relname)
    alias = node.alias
    if alias:
        # FIXME: find a way to get here
        output.write(' AS ')
        output.print_name(alias)


class ConstrTypePrinter(IntEnumPrinter):
    enum = enums.ConstrType

    def CONSTR_ATTR_DEFERRABLE(self, node, output):
        output.swrite('DEFERRABLE')

    def CONSTR_ATTR_DEFERRED(self, node, output):
        output.swrite('INITIALLY DEFERRED')

    def CONSTR_CHECK(self, node, output):
        output.swrite('CHECK (')
        output.print_node(node.raw_expr or node.cooked_expr)
        output.write(')')
        if node.is_no_inherit:
            output.swrite('NO INHERIT')

    def CONSTR_DEFAULT(self, node, output):
        output.swrite('DEFAULT ')
        # """
        # we may have the expression in either "raw" form [...]  or "cooked" form [...]
        # should never have both in the same node!
        # """
        output.print_node(node.raw_expr or node.cooked_expr)

    def CONSTR_EXCLUSION(self, node, output):
        output.swrite('EXCLUDE USING ')
        if node.access_method:
            output.print_symbol(node.access_method)
            output.write(' ')
        output.write('(')
        first = True
        for elem, clauses in node.exclusions:
            if first:
                first = False
            else:
                output.write(', ')
            output.print_node(elem)
            output.swrite('WITH OPERATOR(')
            output.print_symbol(clauses)
            output.write(')')
        output.write(')')
        if node.where_clause:
            output.write(' WHERE (')
            output.print_node(node.where_clause)
            output.write(')')

    def CONSTR_FOREIGN(self, node, output):
        if node.fk_attrs:
            output.swrite('FOREIGN KEY ')
            output.write(' (')
            output.print_name(node.fk_attrs, ',')
            output.write(')')
        if node.pktable:
            output.swrite('REFERENCES ')
            output.print_name(node.pktable)
        if node.pk_attrs:
            output.write(' (')
            output.print_name(node.pk_attrs, ',')
            output.write(')')
        if node.fk_matchtype and node.fk_matchtype != enums.FKCONSTR_MATCH_SIMPLE:
            output.write(' MATCH ')
            if node.fk_matchtype == enums.FKCONSTR_MATCH_FULL:
                output.write('FULL')
            elif node.fk_matchtype == enums.FKCONSTR_MATCH_PARTIAL:  # pragma: no cover
                # MATCH PARTIAL not yet implemented
                output.write('PARTIAL')
        if node.fk_del_action and node.fk_del_action != enums.FKCONSTR_ACTION_NOACTION:
            output.write(' ON DELETE ')
            if node.fk_del_action == enums.FKCONSTR_ACTION_RESTRICT:
                output.write('RESTRICT')
            elif node.fk_del_action == enums.FKCONSTR_ACTION_CASCADE:
                output.write('CASCADE')
            elif node.fk_del_action == enums.FKCONSTR_ACTION_SETNULL:
                output.write('SET NULL')
            elif node.fk_del_action == enums.FKCONSTR_ACTION_SETDEFAULT:
                output.write('SET DEFAULT')
        if node.fk_upd_action and node.fk_upd_action != enums.FKCONSTR_ACTION_NOACTION:
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

    def CONSTR_GENERATED(self, node, output):
        output.swrite('GENERATED ALWAYS AS (')
        output.print_node(node.raw_expr)
        output.write(') STORED')

    def CONSTR_IDENTITY(self, node, output):
        output.swrite('GENERATED ')
        if node.generated_when == enums.ATTRIBUTE_IDENTITY_ALWAYS:
            output.write('ALWAYS ')
        elif node.generated_when == enums.ATTRIBUTE_IDENTITY_BY_DEFAULT:
            output.write('BY DEFAULT ')
        output.write('AS IDENTITY ')
        if node.options:
            output.write('(')
            output.print_list(node.options, '')
            output.write(')')

    def CONSTR_NOTNULL(self, node, output):
        output.swrite('NOT NULL')

    def CONSTR_NULL(self, node, output):
        output.swrite('NULL')

    def CONSTR_PRIMARY(self, node, output):
        output.swrite('PRIMARY KEY')

    def CONSTR_UNIQUE(self, node, output):
        output.swrite('UNIQUE')

    def CONSTR_ATTR_IMMEDIATE(self, node, output):
        output.swrite('INITIALLY IMMEDIATE')


constr_type_printer = ConstrTypePrinter()


@node_printer('Constraint')
def constraint(node, output):
    if node.conname:
        output.swrite('CONSTRAINT ')
        output.print_name(node.conname)

    constr_type_printer(node.contype, node, output)

    if node.indexname:
        output.write(' USING INDEX ')
        output.print_name(node.indexname)
    # Common to UNIQUE & PRIMARY_KEY
    if node.keys:
        output.write(' (')
        output.print_name(node.keys, ',')
        output.write(')')
    if node.including:
        output.write(' INCLUDE (')
        output.print_list(node.including, ',', are_names=True)
        output.write(') ')
    if node.deferrable:
        output.swrite('DEFERRABLE')
    if node.initdeferred:
        output.swrite('INITIALLY DEFERRED')
    with output.push_indent():
        first = True
        if node.options and node.contype == enums.ConstrType.CONSTR_UNIQUE:
            output.write(' WITH (')
            firstOption = True
            for option in node.options:
                if firstOption:
                    firstOption = False
                else:
                    output.write(', ')
                output.print_name(option.defname)
                output.write(' = ')
                output.print_node(option.arg)
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
    # Index access method
    if node.amtype == enums.AMTYPE_INDEX:
        output.write(' TYPE INDEX HANDLER ')
        output.print_name(node.handler_name)
    # Table access method
    elif node.amtype == enums.AMTYPE_TABLE:
        output.write(' TYPE TABLE HANDLER ')
        output.print_name(node.handler_name)
    else:  # pragma: no cover
        raise NotImplementedError('Unhandled amtype: %s' % node.amtype)


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
        output.print_symbol(node.defname)
    if node.arg is not Missing:
        output.write(' = ')
        if isinstance(node.arg, List) or option in ('allow_connections', 'is_template'):
            output.write(node.arg.val.value)
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
    if node.def_:
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
        if node.arg.val.value == 1:
            output.write('CASCADE')
    elif option == 'old_version':
        # FIXME: find a way to get here
        output.write('FROM ')
        output.print_node(node.arg)
    elif option == 'new_version':
        output.write('VERSION ')
        output.print_node(node.arg)
    else:
        output.write(option.upper())
        output.write(' ')
        if option == 'schema':
            output.print_name(node.arg)
        else:
            # FIXME: find a way to get here
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


@node_printer('ColumnDef', 'DefElem')
@node_printer('CreateUserMappingStmt', 'DefElem')
@node_printer('CreateFdwStmt', 'DefElem')
def create_fdw_stmt_def_elem(node, output):
    if node.parent_attribute[0] == 'options' or node.parent_attribute[0] == 'fdwoptions':
        if ' ' in node.defname.value:
            output.write(f'"{node.defname.value}"')
        else:
            output.write(node.defname.value)
        output.write(' ')
        output.print_node(node.arg)
    else:
        output.write(node.defname.value.upper())
        output.write(' ')
        output.print_name(node.arg)


@node_printer('CreateForeignServerStmt')
def create_foreign_server_stmt(node, output):
    output.write('CREATE SERVER ')
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    output.print_name(node.servername)
    if node.servertype:
        output.write(' TYPE ')
        output.print_node(node.servertype)
    if node.version:
        output.write(' VERSION ')
        output.print_node(node.version)
    output.write('FOREIGN DATA WRAPPER ')
    output.print_name(node.fdwname)
    if node.options:
        output.write(' OPTIONS (')
        output.print_list(node.options)
        output.write(')')


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
@node_printer('CreateForeignServerStmt', 'DefElem')
def create_foreign_table_stmt_def_elem(node, output):
    if ' ' in node.defname.value:
        output.write(f'"{node.defname.value}"')
    else:
        output.write(node.defname.value)
    output.write(' ')
    output.print_node(node.arg)


@node_printer('CreateFunctionStmt')
def create_function_stmt(node, output):
    output.write('CREATE ')
    if node.replace:
        output.write('OR REPLACE ')
    if node.is_procedure:
        output.write('PROCEDURE ')
    else:
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
                record_def.append(param)
            else:
                real_params.append(param)
    if real_params:
        output.print_list(real_params)
    output.write(')')

    if node.returnType:
        output.newline()
        output.writes('RETURNS')
        if node.returnType.setof and record_def:
            # Do not treat them as arguments
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

        if isinstance(node.arg, List):
            code = node.arg[0].val.value
        else:
            code = node.arg.val.value
        used_delimiters = set(re.findall(r"\$(\w*)(?=\$)", code))
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
        if node.arg.val.value == 1:
            output.swrite('SECURITY DEFINER')
        else:
            output.swrite('SECURITY INVOKER')
        return

    if option == 'strict':
        if node.arg.val == 0:
            output.swrite('CALLED ON NULL INPUT')
        elif node.arg.val == 1:
            output.swrite('RETURNS NULL ON NULL INPUT')
        return

    if option == 'volatility':
        output.separator()
        output.write(node.arg.val.value.upper())
        return

    if option == 'parallel':
        if node.arg:
            output.swrite('PARALLEL ')
            output.print_name(node.arg)
        else:  # pragma: no cover
            # Backward compatibility, with recent PG the arg is always there
            output.swrite('PARALLEL SAFE')
        return

    if option == 'leakproof':
        if node.arg.val.value == 0:
            output.swrite('NOT')
        output.swrite('LEAKPROOF')
        return

    if option == 'set':
        output.separator()
        output.print_node(node.arg)
        return

    if option == 'window':
        output.write('WINDOW')
        return

    output.writes(node.defname.value.upper())
    output.print_symbol(node.arg)


@node_printer('CreateOpClassStmt')
def create_opclass_stmt(node, output):
    output.write('CREATE OPERATOR CLASS ')
    output.print_name(node.opclassname)
    if node.isDefault:
        output.write('DEFAULT ')
    output.write('FOR TYPE ')
    output.print_name(node.datatype)
    output.write('USING ')
    output.print_name(node.amname)
    output.write('AS ')
    output.print_list(node.items, ',')


@node_printer('CreateOpClassItem')
def create_opclass_item(node, output):
    if node.itemtype == enums.OPCLASS_ITEM_OPERATOR:
        output.write('OPERATOR ')
        output.write('%d ' % node.number._value)
        if node.name:
            _object_with_args(node.name, output, symbol=True, skip_empty_args=True)
        if node.order_family:
            output.write(' FOR ORDER BY ')
            output.print_name(node.order_family)
        if node.class_args:
            output.write(' (')
            output.print_list(node.class_args, standalone_items=False)
            output.write(')')
    elif node.itemtype == enums.OPCLASS_ITEM_FUNCTION:
        output.write('FUNCTION ')
        output.write('%d ' % node.number._value)
        if node.class_args:
            output.write(' (')
            output.print_list(node.class_args, standalone_items=False)
            output.write(')')
        if node.name:
            _object_with_args(node.name, output, skip_empty_args=True)
    elif node.itemtype == enums.OPCLASS_ITEM_STORAGETYPE:
        output.write('STORAGE ')
        output.print_name(node.storedtype)
    else:  # pragma: no cover
        raise NotImplementedError('Unhandled OpClassItem type: %s' % node.itemtype)


@node_printer('CreateOpFamilyStmt')
def create_op_family_stmt(node, output):
    output.write('CREATE OPERATOR FAMILY ')
    output.print_name(node.opfamilyname)
    output.write(' USING ')
    output.print_name(node.amname)


@node_printer('CreatePLangStmt')
def create_plang_stmt(node, output):
    output.write('CREATE ')
    if node.replace:
        output.write('OR REPLACE ')
    if node.pltrusted:
        output.write('TRUSTED ')
    output.write('PROCEDURAL LANGUAGE ')
    output.print_name(node.plname)
    if node.plhandler:
        output.newline()
        with output.push_indent(2):
            output.write('HANDLER ')
            output.print_name(node.plhandler)
            if node.plinline:
                output.newline()
                output.write('INLINE ')
                output.print_name(node.plinline)
            if node.plvalidator:
                output.newline()
                output.write('VALIDATOR ')
                output.print_name(node.plvalidator)


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
        output.print_symbol(node.cmd_name)
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


@node_printer('CreatePublicationStmt')
def create_publication_stmt(node, output):
    output.write('CREATE PUBLICATION ')
    output.print_name(node.pubname)
    output.write(' ')
    if node.tables:
        output.write('FOR TABLE ')
        output.print_list(node.tables, ',')
    elif node.for_all_tables:
        output.write('FOR ALL TABLES ')
    if node.options:
        output.write('WITH (')
        output.print_list(node.options, ',')
        output.write(')')


@node_printer('CreatePublicationStmt', 'RangeVar')
def create_publication_stmt_range_var(node, output):
    if not node.inh:
        output.write('ONLY ')
    if node.schemaname:
        output.print_name(node.schemaname)
        output.write('.')
    output.print_name(node.relname)
    if node.alias:
        # FIXME: find a way to get here
        output.write(' AS ')
        output.print_name(node.alias)


@node_printer('CreateRangeStmt')
def create_range_stmt(node, output):
    output.write('CREATE TYPE ')
    output.print_name(node.typeName)
    output.write(' AS RANGE (')
    output.print_list(node.params)
    output.write(')')


class RoleStmtTypePrinter(IntEnumPrinter):
    enum = enums.RoleStmtType

    def ROLESTMT_ROLE(self, node, output):
        output.write('ROLE')

    def ROLESTMT_USER(self, node, output):
        output.write('USER')

    def ROLESTMT_GROUP(self, node, output):
        output.write('GROUP')


role_stmt_type_printer = RoleStmtTypePrinter()


@node_printer('CreateRoleStmt')
def create_role_stmt(node, output):
    output.write('CREATE ')
    role_stmt_type_printer(node.stmt_type, node, output)
    output.write(' ')
    output.print_name(node.role)
    if node.options:
        output.write(' WITH ')
        output.print_list(node.options, sep=' ')


@node_printer('AlterRoleStmt', 'DefElem')
@node_printer('CreateRoleStmt', 'DefElem')
def create_or_alter_role_option(node, output):
    option = node.defname.value
    argv = node.arg
    if option == 'sysid':
        output.write('SYSID ')
        output.print_node(argv)
    elif option == 'adminmembers':
        output.write('ADMIN ')
        output.print_list(argv)
    elif option == 'rolemembers':
        output.write('ROLE ')
        output.print_list(argv)
    elif option == 'addroleto':
        output.write('IN ROLE ')
        output.print_list(argv)
    elif option == 'superuser':
        output.write('SUPERUSER' if argv.val == 1 else 'NOSUPERUSER')
    elif option == 'createdb':
        output.write('CREATEDB' if argv.val == 1 else 'NOCREATEDB')
    elif option == 'createrole':
        output.write('CREATEROLE' if argv.val == 1 else 'NOCREATEROLE')
    elif option == 'canlogin':
        output.write('LOGIN' if argv.val == 1 else 'NOLOGIN')
    elif option == 'connectionlimit':
        output.write('CONNECTION LIMIT ')
        output.print_node(argv)
    elif option == 'validUntil':
        output.write('VALID UNTIL ')
        output.print_node(argv)
    elif option == 'password':
        output.write('PASSWORD ')
        if argv:
            output.print_node(argv)
        else:
            output.write('NULL')
    elif option == 'inherit':
        output.write('INHERIT' if argv.val == 1 else 'NOINHERIT')
    elif option == 'isreplication':
        output.write('REPLICATION' if argv.val == 1 else 'NOREPLICATION')
    elif option == 'bypassrls':
        output.write('BYPASSRLS' if argv.val == 1 else 'NOBYPASSRLS')
    else:
        raise NotImplementedError('Unhandled option: %s' % option)


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
        output.writes('TEMPORARY ')
    elif node.sequence.relpersistence == enums.RELPERSISTENCE_UNLOGGED:
        output.writes('UNLOGGED ')
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


@node_printer('Constraint', 'DefElem')
@node_printer('CreateSeqStmt', 'DefElem')
@node_printer('AlterSeqStmt', 'DefElem')
def create_seq_stmt_def_elem(node, output):
    option = node.defname.value
    if option == 'cycle':
        if node.arg.val.value == 0:
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
    elif option == 'restart':
        output.write('RESTART')
        if node.arg:
            output.write(' WITH ')
            output.print_node(node.arg)
    else:
        if node.arg is Missing:
            output.write('NO ')
        output.write(option.upper())
        if node.arg is not Missing:
            output.write(' ')
            output.print_node(node.arg)
    if node.defaction != enums.DefElemAction.DEFELEM_UNSPEC:  # pragma: no cover
        raise NotImplementedError('Unhandled defaction: %s' % node.defaction)


@node_printer('CreateStatsStmt')
def create_stats_stmt(node, output):
    output.write('CREATE STATISTICS ')
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    output.print_name(node.defnames)
    if node.stat_types:
        output.write(' (')
        output.print_name(node.stat_types)
        output.write(')')
    output.write(' ON ')
    output.print_list(node.exprs)
    output.write(' FROM ')
    output.print_list(node.relations)


@node_printer('CreateStmt')
def create_stmt(node, output):
    output.writes('CREATE')
    # NB: parent_node may be None iff we are dealing with a single concrete statement, not with
    # the ephemeral RawStmt returned by parse_sql(); in all other cases in this source where
    # we access the parent_node we are actually in a "contextualized printer", that can only be
    # entered when there is a parent node
    if node.parent_node is not None and node.parent_node.node_tag == 'CreateForeignTableStmt':
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
    elif not node.ofTypename:
        output.write(' ()')
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
            else:  # pragma: no cover
                output.newline()
            output.write(' ')
            output.print_node(node.partbound)
        if node.partspec:
            if first:
                first = False
            else:
                output.newline()
            output.write(' PARTITION BY ')
            output.print_node(node.partspec)
        if node.options:
            if first:
                first = False
            else:
                output.newline()
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
    if node.accessMethod:
        output.write(' USING ')
        output.print_name(node.accessMethod)


@node_printer('CreateTableAsStmt')
def create_table_as_stmt(node, output):
    output.writes('CREATE')
    if node.into.rel.relpersistence == enums.RELPERSISTENCE_TEMP:
        output.writes('TEMPORARY')
    elif node.into.rel.relpersistence == enums.RELPERSISTENCE_UNLOGGED:
        output.writes('UNLOGGED')
    output.writes(OBJECT_NAMES[node.relkind.value])
    if node.if_not_exists:
        output.writes('IF NOT EXISTS')
    output.print_node(node.into)
    output.space(2)
    output.write('AS ')
    with output.push_indent():
        output.print_node(node.query)
    if node.into.skipData:
        output.newline()
        output.write('WITH NO DATA')


@node_printer('CreateTableSpaceStmt')
def create_table_space_stmt(node, output):
    output.write('CREATE TABLESPACE ')
    output.print_name(node.tablespacename)
    output.space()
    if node.owner:
        output.write('OWNER ')
        output.print_node(node.owner)
        output.space()
    output.write('LOCATION ')
    output.write_quoted_string(node.location.value)
    if node.options:
        output.write(' WITH (')
        output.print_list(node.options)
        output.write(')')


@node_printer('CreateTrigStmt')
def create_trig_stmt(node, output):
    output.write('CREATE ')
    if node.isconstraint:
        output.write('CONSTRAINT ')
    output.write('TRIGGER ')
    output.print_name(node.trigname)
    output.newline()
    with output.push_indent(2):
        if node.timing.value:
            if node.timing & enums.TRIGGER_TYPE_BEFORE:
                output.write('BEFORE ')
            elif node.timing & enums.TRIGGER_TYPE_INSTEAD:
                output.write('INSTEAD OF ')
        else:
            output.write('AFTER ')
        event_strings = []
        for ev in ('INSERT', 'DELETE', 'UPDATE', 'TRUNCATE'):
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

        if node.constrrel:
            output.swrite('FROM ')
            output.print_name(node.constrrel)

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


@node_printer('AlterSubscriptionStmt', 'DefElem')
@node_printer('CreateSubscriptionStmt', 'DefElem')
def create_subscription_stmt_stmt_def_elem(node, output):
    output.print_name(node.defname)
    if node.arg:
        output.write(' = ')
        if node.arg.node_tag == 'String' and node.arg.val.value in ('true', 'false'):
            output.write(node.arg.val.value)
        else:
            output.print_node(node.arg)


@node_printer('CreateSubscriptionStmt')
def create_subscription_stmt(node, output):
    output.write('CREATE SUBSCRIPTION ')
    output.print_name(node.subname)
    output.write(' CONNECTION ')
    if node.conninfo:
        output.print_node(node.conninfo)
    else:
        output.write("''")
    output.write(' PUBLICATION ')
    output.print_name(node.publication, ',')
    output.write(' ')
    if node.options:
        output.write('WITH (')
        output.print_name(node.options, ',')
        output.write(')')


@node_printer('CurrentOfExpr')
def current_of_expr(node, output):
    output.write('CURRENT OF ')
    output.print_name(node.cursor_name)


@node_printer('CreateTransformStmt')
def create_transform_stmt(node, output):
    output.write('CREATE ')
    if node.replace:
        output.write('OR REPLACE ')
    output.write('TRANSFORM FOR ')
    output.print_name(node.type_name)
    output.write('LANGUAGE ')
    output.print_name(node.lang)
    output.write(' (')
    if node.fromsql:
        output.write('FROM SQL WITH FUNCTION ')
        output.print_node(node.fromsql)
        if node.tosql:
            output.write(', ')
    if node.tosql:
        output.write('TO SQL WITH FUNCTION ')
        output.print_node(node.tosql)
    output.write(')')


@node_printer('ClosePortalStmt')
def close_portal_stmt(node, output):
    output.write('CLOSE ')
    if node.portalname:
        output.print_name(node.portalname)
    else:
        output.write('ALL')


@node_printer('CreateUserMappingStmt')
def create_user_mapping_stmt(node, output):
    output.write('CREATE USER MAPPING ')
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    output.write('FOR ')
    role_spec(node.user, output)
    output.writes(' SERVER')
    output.write(node.servername.value)
    if node.options:
        output.write(' OPTIONS (')
        output.print_list(node.options, ',')
        output.write(')')


@node_printer('DeallocateStmt')
def deallocate_stmt(node, output):
    output.write('DEALLOCATE PREPARE ')
    if node.name:
        output.print_name(node.name)
    else:
        output.write('ALL')


@node_printer('DefineStmt')
def define_stmt(node, output):
    output.write('CREATE ')
    if node.replace:
        output.write('OR REPLACE ')
    output.writes(OBJECT_NAMES[node.kind.value])
    if node.if_not_exists:
        output.write('IF NOT EXISTS ')
    output.print_list(node.defnames, '.', standalone_items=False, are_names=True,
                      is_symbol=node.kind == enums.ObjectType.OBJECT_OPERATOR)
    if node.args is not Missing:
        # args is actually a tuple (list-of-nodes, integer): the integer value, if different
        # from -1, is the number of nodes representing the actual arguments, remaining are
        # ORDER BY
        args, count = node.args
        count = count.val.value
        output.write(' (')
        if count == -1:
            # Special case: if it's an aggregate, and the scalar is equal to
            # None (not is, since it's a Scalar), write a star
            if ((node.kind.value == enums.ObjectType.OBJECT_AGGREGATE
                 and args == None)):
                output.write('*')
                actual_args = []
                orderby_args = []
            else:
                count = len(args)
                actual_args = args
                orderby_args = []
        else:
            if count > 0:
                actual_args = args[:count]
            else:
                actual_args = []
            # For aggregates, if we have a count != -1 BUT we don't have an arg
            # for that, add the last arg as an order by arg.
            if count == len(args):
                orderby_args = actual_args[-1:]
            else:
                orderby_args = args[count:]
        if actual_args:
            output.print_list(actual_args, standalone_items=False)
        if orderby_args:
            output.write(' ORDER BY ')
            output.print_list(orderby_args, standalone_items=False)
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
    output.print_symbol(node.defname)
    if node.arg is not Missing:
        output.write(' = ')
        output.print_node(node.arg)
    if node.defaction != enums.DefElemAction.DEFELEM_UNSPEC:  # pragma: no cover
        raise NotImplementedError('Unhandled defaction: %s' % node.defaction)


@node_printer('DefineStmt', 'DefElem')
def define_stmt_def_elem(node, output):
    output.print_node(node.defname, is_name=True)
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
    if node.defaction != enums.DefElemAction.DEFELEM_UNSPEC:  # pragma: no cover
        raise NotImplementedError('Unhandled defaction: %s' % node.defaction)


class DiscardModePrinter(IntEnumPrinter):
    enum = enums.DiscardMode

    def DISCARD_ALL(self, node, output):
        output.write('ALL')

    def DISCARD_PLANS(self, node, output):
        output.write('PLANS')

    def DISCARD_SEQUENCES(self, node, output):
        output.write('SEQUENCES')

    def DISCARD_TEMP(self, node, output):
        output.write('TEMP')


discard_mode_printer = DiscardModePrinter()


@node_printer('DiscardStmt')
def discard_stmt(node, output):
    output.write('DISCARD ')
    discard_mode_printer(node.target, node, output)


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
    if node.options:
        output.write(' (')
        output.print_list(node.options)
        output.write(')')


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
    # Special case functions since they are not special objects
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
        output.swrite('CASCADE')


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
        elif node.mode == pm.FUNC_PARAM_TABLE:
            pass  # function output column
        else:  # pragma: no cover
            raise NotImplementedError('Unhandled mode: %s' % node.mode)
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
    if not node.is_grant and node.grant_option:
        output.write('GRANT OPTION FOR ')
    if node.privileges:
        output.print_list(node.privileges)
    else:
        output.write('ALL PRIVILEGES')
    # hack for OBJECT_FOREIGN_SERVER
    if node.objtype.value == enums.ObjectType.OBJECT_FOREIGN_SERVER:
        object_name = 'FOREIGN SERVER'
    else:
        object_name = OBJECT_NAMES[node.objtype.value]
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
        if node.is_grant and node.grant_option:
            output.newline()
            output.write('WITH GRANT OPTION')
        if node.behavior == enums.DropBehavior.DROP_CASCADE:
            output.write(' CASCADE')


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


@node_printer('ImportForeignSchemaStmt')
def import_foreign_schema_stmt(node, output):
    output.write('IMPORT FOREIGN SCHEMA ')
    output.print_name(node.remote_schema)
    if node.list_type == enums.ImportForeignSchemaType.FDW_IMPORT_SCHEMA_ALL:
        pass
    elif node.list_type == enums.ImportForeignSchemaType.FDW_IMPORT_SCHEMA_LIMIT_TO:
        output.write(' LIMIT TO (')
        output.print_list(node.table_list)
        output.write(')')
    elif node.list_type == enums.ImportForeignSchemaType.FDW_IMPORT_SCHEMA_EXCEPT:
        output.write(' EXCEPT (')
        output.print_list(node.table_list)
        output.write(')')
    output.writes(' FROM SERVER ')
    output.print_name(node.server_name)
    output.writes(' INTO ')
    output.print_name(node.local_schema)
    alter_def_elem(node.options, output)


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
        if node.indexIncludingParams:
            output.write(' INCLUDE (')
            output.print_list(node.indexIncludingParams)
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


@node_printer('NotifyStmt')
def notify_stmt(node, output):
    output.write('NOTIFY ')
    output.print_name(node.conditionname)
    if node.payload:
        output.write(', ')
        output.write_quoted_string(node.payload.value)


def _object_with_args(node, output, unquote_name=False, symbol=False,
                      skip_empty_args=False, empty_placeholder=''):
    # Special treatment for OPERATOR object inside DROP or COMMENT
    if unquote_name:
        if len(node.objname) > 1:
            for idx, name in enumerate(node.objname):
                if idx > 0:
                    output.write('.')
                output.write(name.val.value)
        else:
            output.write(node.objname.string_value)
        if not node.args_unspecified:
            output.write(' ')
    elif symbol:
        output.print_symbol(node.objname)
    else:
        output.print_name(node.objname)
    if not node.args_unspecified:
        if node.objargs:
            output.write(' (')
            output.print_list(node.objargs, ',', standalone_items=False)
            output.write(')')
        elif not skip_empty_args:
            output.write(' (')
            output.write(empty_placeholder)
            output.write(')')


@node_printer('ObjectWithArgs')
def object_with_args(node, output):
    _object_with_args(node, output)


@node_printer(('AlterObjectSchemaStmt',), 'ObjectWithArgs')
def alter_object_schema_stmt_object_with_args(node, output):
    symbol = node.parent_node.objectType == enums.ObjectType.OBJECT_OPERATOR
    _object_with_args(node, output, symbol=symbol)


@node_printer(('AlterOperatorStmt',), 'ObjectWithArgs')
def alter_operator_stmt_object_with_args(node, output):
    _object_with_args(node, output, unquote_name=True)


@node_printer(('AlterOwnerStmt',), 'ObjectWithArgs')
def alter_owner_stmt_object_with_args(node, output):
    unquote_name = node.parent_node.objectType == enums.ObjectType.OBJECT_OPERATOR
    _object_with_args(node, output, unquote_name=unquote_name)


@node_printer(('CommentStmt',), 'ObjectWithArgs')
def comment_stmt_object_with_args(node, output):
    unquote_name = node.parent_node.objtype == enums.ObjectType.OBJECT_OPERATOR
    _object_with_args(node, output, unquote_name=unquote_name)


@node_printer(('DropStmt',), 'ObjectWithArgs')
def drop_stmt_object_with_args(node, output):
    unquote_name = node.parent_node.removeType == enums.ObjectType.OBJECT_OPERATOR
    if node.parent_node.removeType == enums.ObjectType.OBJECT_AGGREGATE:
        _object_with_args(node, output, empty_placeholder='*', unquote_name=unquote_name)
    else:
        _object_with_args(node, output, unquote_name=unquote_name)


@node_printer('PartitionBoundSpec')
def partition_bound_spec(node, output):
    if node.is_default:
        output.write('DEFAULT')
    else:
        output.write('FOR VALUES ')
        if node.strategy == enums.PARTITION_STRATEGY_RANGE:
            output.swrite('FROM (')
            output.print_list(node.lowerdatums)
            output.write(') TO (')
            output.print_list(node.upperdatums)
            output.write(')')
        elif node.strategy == enums.PARTITION_STRATEGY_LIST:
            output.write('IN (')
            output.print_list(node.listdatums)
            output.write(')')
        elif node.strategy == enums.PARTITION_STRATEGY_HASH:
            output.write('WITH (MODULUS %d, REMAINDER %d)'
                         % (node.modulus.value, node.remainder.value))
        else:
            raise NotImplementedError('Unhandled strategy %r' % node.strategy)


@node_printer('PartitionCmd')
def partition_cmd(node, output):
    output.print_node(node.name, is_name=True)
    if node.bound:
        output.print_node(node.bound)


@node_printer('PartitionElem')
def partition_elem(node, output):
    if node.name:
        output.print_name(node.name)
    elif node.expr:
        output.write('(')
        output.print_node(node.expr)
        output.write(')')
    if node.collation:
        output.write('COLLATE ')
        output.print_list(node.collation, are_names=True)
    if node.opclass:
        output.print_name(node.opclass)


@node_printer('PartitionRangeDatum')
def partition_range_datum(node, output):
    # FIXME: find a way to get here, apparently these have been replaced by ColumRef
    if node.kind == enums.PartitionRangeDatumKind.PARTITION_RANGE_DATUM_MINVALUE:
        output.write('MINVALUE')
    elif node.kind == enums.PartitionRangeDatumKind.PARTITION_RANGE_DATUM_MAXVALUE:
        output.write('MAXVALUE')
    else:
        output.print_node(node.value)


@node_printer('PartitionSpec')
def partition_spec(node, output):
    output.print_symbol(node.strategy)
    output.write(' (')
    output.print_list(node.partParams)
    output.write(')')


class ReindexKindPrinter(IntEnumPrinter):
    enum = enums.ReindexObjectType

    def _print_options(self, node, output):
        if node.concurrent:
            output.write('CONCURRENTLY ')

    def REINDEX_OBJECT_TABLE(self, node, output):
        output.write('TABLE ')
        self._print_options(node, output)
        output.print_node(node.relation)

    def REINDEX_OBJECT_INDEX(self, node, output):
        output.write('INDEX ')
        self._print_options(node, output)
        output.print_node(node.relation)

    def REINDEX_OBJECT_SCHEMA(self, node, output):
        output.write('SCHEMA ')
        self._print_options(node, output)
        output.print_name(node.name)

    def REINDEX_OBJECT_SYSTEM(self, node, output):
        output.write('SYSTEM ')
        self._print_options(node, output)
        output.print_name(node.name)

    def REINDEX_OBJECT_DATABASE(self, node, output):
        output.write('DATABASE ')
        self._print_options(node, output)
        output.print_name(node.name)


reindex_kind_printer = ReindexKindPrinter()


@node_printer('ReindexStmt')
def reindex_stmt(node, output):
    output.write('REINDEX ')
    reindex_kind_printer(node.kind, node, output)


@node_printer('RenameStmt')
def rename_stmt(node, output):
    OT = enums.ObjectType
    objtype = node.renameType
    output.write('ALTER ')
    if objtype == OT.OBJECT_TABCONSTRAINT:
        output.write('TABLE')
    elif objtype == OT.OBJECT_DOMCONSTRAINT:
        output.write('DOMAIN')
    elif objtype == OT.OBJECT_ROLE:
        output.write('ROLE')
    else:
        output.write(OBJECT_NAMES[node.relationType
                                  if objtype in (OT.OBJECT_ATTRIBUTE, OT.OBJECT_COLUMN)
                                  else objtype])
    output.write(' ')
    if node.missing_ok:
        output.write('IF EXISTS ')
    if objtype in (OT.OBJECT_SCHEMA, OT.OBJECT_DATABASE, OT.OBJECT_ROLE):
        output.print_name(node.subname)
    elif (objtype == OT.OBJECT_RULE
          or objtype == OT.OBJECT_POLICY
          or objtype == OT.OBJECT_TRIGGER):
        output.print_name(node.subname)
        output.write(' ON ')
        output.print_node(node.relation)
    elif node.relation:
        output.print_node(node.relation)
    elif objtype in (OT.OBJECT_OPFAMILY, OT.OBJECT_OPCLASS):
        method, name = node.object
        output.print_name(name)
        output.write(' USING ')
        output.print_symbol(method)
    else:
        output.print_name(node.object)
    output.write(' RENAME ')
    if objtype == OT.OBJECT_COLUMN:
        output.write('COLUMN ')
        output.print_name(node.subname)
    elif objtype == OT.OBJECT_TABCONSTRAINT:
        output.write('CONSTRAINT ')
        output.print_name(node.subname)
    elif objtype == OT.OBJECT_ATTRIBUTE:
        output.write('ATTRIBUTE ')
        output.print_name(node.subname)
    elif objtype == OT.OBJECT_DOMCONSTRAINT:
        output.writes('CONSTRAINT')
        output.print_name(node.subname)
    output.swrite('TO ')
    output.print_name(node.newname)
    if node.behavior == enums.DropBehavior.DROP_CASCADE:
        output.write(' CASCADE')


@node_printer('RenameStmt', 'RangeVar')
def rename_stmt_range_var(node, output):
    OT = enums.ObjectType
    if not node.inh and node.parent_node.renameType not in (OT.OBJECT_ATTRIBUTE,
                                                            OT.OBJECT_TYPE):
        output.write('ONLY ')
    if node.schemaname:
        output.print_name(node.schemaname)
        output.write('.')
    output.print_name(node.relname)
    alias = node.alias
    if alias:
        # FIXME: find a way to get here
        output.write(' AS ')
        output.print_name(alias)


@node_printer('ReplicaIdentityStmt')
def replica_identity_stmt(node, output):
    output.write('REPLICA IDENTITY ')
    if node.identity_type == enums.REPLICA_IDENTITY_INDEX:
        output.write('USING INDEX ')
        output.print_name(node.name)
    elif node.identity_type == enums.REPLICA_IDENTITY_DEFAULT:
        output.write('DEFAULT')
    elif node.identity_type == enums.REPLICA_IDENTITY_FULL:
        output.write('FULL')


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


EVENT_NAMES = {
    enums.CmdType.CMD_SELECT: 'SELECT',
    enums.CmdType.CMD_UPDATE: 'UPDATE',
    enums.CmdType.CMD_INSERT: 'INSERT',
    enums.CmdType.CMD_DELETE: 'DELETE',
}


@node_printer('RuleStmt')
def rule_stmt_printer(node, output):
    output.write('CREATE ')
    if node.replace:
        output.write('OR REPLACE ')
    output.write('RULE ')
    output.print_name(node.rulename)
    output.write(' AS')
    output.newline()
    with output.push_indent(2):
        output.write('ON ')
        output.write(EVENT_NAMES[node.event.value])
        output.write(' TO ')
        output.print_name(node.relation)
        if node.whereClause:
            output.newline()
            output.write('WHERE ')
            output.print_node(node.whereClause)
        output.newline()
        output.write('DO ')
        if node.instead:
            output.write('INSTEAD')
        else:
            output.writes('ALSO')
        if node.actions:
            if len(node.actions) > 1:
                output.write(' (')
                output.newline()
                with output.push_indent(2):
                    output.space(2)
                    output.print_list(node.actions, ';', standalone_items=True)
                output.newline()
                output.write(')')
            else:
                output.space()
                with output.push_indent():
                    output.print_list(node.actions)
        else:
            output.write(' NOTHING')


@node_printer('RefreshMatViewStmt')
def refresh_mat_view_stmt(node, output):
    output.write('REFRESH MATERIALIZED VIEW ')
    if node.concurrent:
        output.write('CONCURRENTLY ')
    output.print_node(node.relation)
    if node.skipData:
        output.write('WITH NO DATA')


@node_printer('ReassignOwnedStmt')
def reassign_owned_stmt(node, output):
    output.write('REASSIGN OWNED BY ')
    output.print_list(node.roles, ',', are_names=False)
    output.write(' TO ')
    output.print_node(node.newrole)


@node_printer('SecLabelStmt')
def sec_label_stmt(node, output):
    output.write('SECURITY LABEL ')
    if node.provider:
        output.write('FOR ')
        output.print_name(node.provider)
    output.write(' ON ')
    output.write(OBJECT_NAMES[node.objtype.value])
    output.write(' ')
    output.print_name(node.object)
    output.write(' IS ')
    if node.label:
        output.print_node(node.label)
    else:
        output.write('NULL')


@node_printer('TableLikeClause')
def table_like_clause(node, output):
    output.write('LIKE ')
    output.print_node(node.relation)
    TLO = enums.TableLikeOption
    if node.options == TLO.CREATE_TABLE_LIKE_ALL:
        output.write(' INCLUDING ALL')
    else:
        if node.options & TLO.CREATE_TABLE_LIKE_COMMENTS:
            output.write(' INCLUDING COMMENTS')
        if node.options & TLO.CREATE_TABLE_LIKE_CONSTRAINTS:
            output.write(' INCLUDING CONSTRAINTS')
        if node.options & TLO.CREATE_TABLE_LIKE_DEFAULTS:
            output.write(' INCLUDING DEFAULTS')
        if node.options & TLO.CREATE_TABLE_LIKE_IDENTITY:
            output.write(' INCLUDING IDENTITY')
        if node.options & TLO.CREATE_TABLE_LIKE_GENERATED:
            output.write(' INCLUDING GENERATED')
        if node.options & TLO.CREATE_TABLE_LIKE_INDEXES:
            output.write(' INCLUDING INDEXES')
        if node.options & TLO.CREATE_TABLE_LIKE_STATISTICS:
            output.write(' INCLUDING STATISTICS')
        if node.options & TLO.CREATE_TABLE_LIKE_STORAGE:
            output.write(' INCLUDING STORAGE')


@node_printer('TriggerTransition')
def trigger_transition(node, output):
    if node.isNew:
        output.write('NEW TABLE AS ')
    else:
        output.write('OLD TABLE AS ')
    output.print_name(node.name)


@node_printer('VacuumStmt')
def vacuum_stmt(node, output):
    if node.is_vacuumcmd:
        output.write('VACUUM ')
    else:
        output.write('ANALYZE ')
    if node.options:
        output.write('(')
        output.print_list(node.options, ',')
        output.write(') ')
    if node.rels:
        output.print_list(node.rels, ',')


@node_printer('VacuumStmt', 'DefElem')
def vacuum_stmt_def_elem(node, output):
    output.write(node.defname.value.upper())
    if node.arg:
        output.write(' ')
        output.write(str(node.arg.val.value))


@node_printer('VacuumRelation')
def vacuum_relation(node, output):
    output.print_node(node.relation)
    if node.va_cols:
        output.write('(')
        output.print_list(node.va_cols, ',', are_names=True)
        output.write(')')


@node_printer('VariableShowStmt')
def variable_show_statement(node, output):
    output.write('SHOW ')
    if node.name == 'all':
        output.write('ALL')
    else:
        output.print_symbol(node.name)


class ViewCheckOptionPrinter(IntEnumPrinter):
    enum = enums.ViewCheckOption

    def NO_CHECK_OPTION(self, node, output):
        pass

    def LOCAL_CHECK_OPTION(self, node, output):
        output.write(' WITH LOCAL CHECK OPTION')

    def CASCADED_CHECK_OPTION(self, node, output):
        output.write(' WITH CHECK OPTION')


view_check_option_printer = ViewCheckOptionPrinter()


@node_printer('ViewStmt')
def view_stmt(node, output):
    output.write('CREATE ')
    if node.replace:
        output.write('OR REPLACE ')
    if node.view.relpersistence == enums.RELPERSISTENCE_TEMP:
        output.write('TEMPORARY ')
    elif node.view.relpersistence == enums.RELPERSISTENCE_UNLOGGED:
        output.write('UNLOGGED ')
    output.write('VIEW ')
    output.print_node(node.view)
    if node.aliases:
        output.write(' (')
        output.print_list(node.aliases, are_names=True)
        output.write(')')
    output.newline()
    output.space(2)
    if node.options:
        output.write('WITH (')
        output.print_list(node.options)
        output.write(')')
        output.newline()
        output.space(2)
    output.write('AS ')
    with output.push_indent():
        output.print_node(node.query)
    view_check_option_printer(node.withCheckOption, node, output)


@node_printer('ViewStmt', 'DefElem')
def view_stmt_def_elem(node, output):
    output.print_symbol(node.defname)
    if node.arg:
        output.write(' = ')
        output.print_symbol(node.arg)
    if node.defaction:
        if node.defaction != enums.DefElemAction.DEFELEM_UNSPEC:  # pragma: no cover
            raise NotImplementedError('Unhandled defaction: %s' % node.defaction)
