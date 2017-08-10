# -*- coding: utf-8 -*-
# :Project:   pg_query -- DO NOT EDIT: automatically extracted from parsenodes.h @ 10-latest-0-g1ec5c22
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

import enum


class A_Expr_Kind(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L251>`__."

    AEXPR_OP = 0
    AEXPR_OP_ANY = enum.auto()
    AEXPR_OP_ALL = enum.auto()
    AEXPR_DISTINCT = enum.auto()
    AEXPR_NOT_DISTINCT = enum.auto()
    AEXPR_NULLIF = enum.auto()
    AEXPR_OF = enum.auto()
    AEXPR_IN = enum.auto()
    AEXPR_LIKE = enum.auto()
    AEXPR_ILIKE = enum.auto()
    AEXPR_SIMILAR = enum.auto()
    AEXPR_BETWEEN = enum.auto()
    AEXPR_NOT_BETWEEN = enum.auto()
    AEXPR_BETWEEN_SYM = enum.auto()
    AEXPR_NOT_BETWEEN_SYM = enum.auto()
    AEXPR_PAREN = enum.auto()

class AlterSubscriptionType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L3392>`__."

    ALTER_SUBSCRIPTION_OPTIONS = 0
    ALTER_SUBSCRIPTION_CONNECTION = enum.auto()
    ALTER_SUBSCRIPTION_PUBLICATION = enum.auto()
    ALTER_SUBSCRIPTION_REFRESH = enum.auto()
    ALTER_SUBSCRIPTION_ENABLED = enum.auto()

class AlterTSConfigType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L3333>`__."

    ALTER_TSCONFIG_ADD_MAPPING = 0
    ALTER_TSCONFIG_ALTER_MAPPING_FOR_TOKEN = enum.auto()
    ALTER_TSCONFIG_REPLACE_DICT = enum.auto()
    ALTER_TSCONFIG_REPLACE_DICT_FOR_TOKEN = enum.auto()
    ALTER_TSCONFIG_DROP_MAPPING = enum.auto()

class AlterTableType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L1683>`__."

    AT_AddColumn = 0
    AT_AddColumnRecurse = enum.auto()
    AT_AddColumnToView = enum.auto()
    AT_ColumnDefault = enum.auto()
    AT_DropNotNull = enum.auto()
    AT_SetNotNull = enum.auto()
    AT_SetStatistics = enum.auto()
    AT_SetOptions = enum.auto()
    AT_ResetOptions = enum.auto()
    AT_SetStorage = enum.auto()
    AT_DropColumn = enum.auto()
    AT_DropColumnRecurse = enum.auto()
    AT_AddIndex = enum.auto()
    AT_ReAddIndex = enum.auto()
    AT_AddConstraint = enum.auto()
    AT_AddConstraintRecurse = enum.auto()
    AT_ReAddConstraint = enum.auto()
    AT_AlterConstraint = enum.auto()
    AT_ValidateConstraint = enum.auto()
    AT_ValidateConstraintRecurse = enum.auto()
    AT_ProcessedConstraint = enum.auto()
    AT_AddIndexConstraint = enum.auto()
    AT_DropConstraint = enum.auto()
    AT_DropConstraintRecurse = enum.auto()
    AT_ReAddComment = enum.auto()
    AT_AlterColumnType = enum.auto()
    AT_AlterColumnGenericOptions = enum.auto()
    AT_ChangeOwner = enum.auto()
    AT_ClusterOn = enum.auto()
    AT_DropCluster = enum.auto()
    AT_SetLogged = enum.auto()
    AT_SetUnLogged = enum.auto()
    AT_AddOids = enum.auto()
    AT_AddOidsRecurse = enum.auto()
    AT_DropOids = enum.auto()
    AT_SetTableSpace = enum.auto()
    AT_SetRelOptions = enum.auto()
    AT_ResetRelOptions = enum.auto()
    AT_ReplaceRelOptions = enum.auto()
    AT_EnableTrig = enum.auto()
    AT_EnableAlwaysTrig = enum.auto()
    AT_EnableReplicaTrig = enum.auto()
    AT_DisableTrig = enum.auto()
    AT_EnableTrigAll = enum.auto()
    AT_DisableTrigAll = enum.auto()
    AT_EnableTrigUser = enum.auto()
    AT_DisableTrigUser = enum.auto()
    AT_EnableRule = enum.auto()
    AT_EnableAlwaysRule = enum.auto()
    AT_EnableReplicaRule = enum.auto()
    AT_DisableRule = enum.auto()
    AT_AddInherit = enum.auto()
    AT_DropInherit = enum.auto()
    AT_AddOf = enum.auto()
    AT_DropOf = enum.auto()
    AT_ReplicaIdentity = enum.auto()
    AT_EnableRowSecurity = enum.auto()
    AT_DisableRowSecurity = enum.auto()
    AT_ForceRowSecurity = enum.auto()
    AT_NoForceRowSecurity = enum.auto()
    AT_GenericOptions = enum.auto()
    AT_AttachPartition = enum.auto()
    AT_DetachPartition = enum.auto()
    AT_AddIdentity = enum.auto()
    AT_SetIdentity = enum.auto()
    AT_DropIdentity = enum.auto()

class ConstrType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2032>`__."

    CONSTR_NULL = 0
    CONSTR_NOTNULL = enum.auto()
    CONSTR_DEFAULT = enum.auto()
    CONSTR_IDENTITY = enum.auto()
    CONSTR_CHECK = enum.auto()
    CONSTR_PRIMARY = enum.auto()
    CONSTR_UNIQUE = enum.auto()
    CONSTR_EXCLUSION = enum.auto()
    CONSTR_FOREIGN = enum.auto()
    CONSTR_ATTR_DEFERRABLE = enum.auto()
    CONSTR_ATTR_NOT_DEFERRABLE = enum.auto()
    CONSTR_ATTR_DEFERRED = enum.auto()
    CONSTR_ATTR_IMMEDIATE = enum.auto()

class DefElemAction(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L707>`__."

    DEFELEM_UNSPEC = 0
    DEFELEM_SET = enum.auto()
    DEFELEM_ADD = enum.auto()
    DEFELEM_DROP = enum.auto()

class DiscardMode(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L3157>`__."

    DISCARD_ALL = 0
    DISCARD_PLANS = enum.auto()
    DISCARD_SEQUENCES = enum.auto()
    DISCARD_TEMP = enum.auto()

class DropBehavior(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L1664>`__."

    DROP_RESTRICT = 0
    DROP_CASCADE = enum.auto()

class FetchDirection(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2648>`__."

    FETCH_FORWARD = 0
    FETCH_BACKWARD = enum.auto()
    FETCH_ABSOLUTE = enum.auto()
    FETCH_RELATIVE = enum.auto()

class FunctionParameterMode(str, enum.Enum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2733>`__."

    FUNC_PARAM_IN = 'i'
    FUNC_PARAM_OUT = 'o'
    FUNC_PARAM_INOUT = 'b'
    FUNC_PARAM_VARIADIC = 'v'
    FUNC_PARAM_TABLE = 't'

class GrantObjectType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L1823>`__."

    ACL_OBJECT_COLUMN = 0
    ACL_OBJECT_RELATION = enum.auto()
    ACL_OBJECT_SEQUENCE = enum.auto()
    ACL_OBJECT_DATABASE = enum.auto()
    ACL_OBJECT_DOMAIN = enum.auto()
    ACL_OBJECT_FDW = enum.auto()
    ACL_OBJECT_FOREIGN_SERVER = enum.auto()
    ACL_OBJECT_FUNCTION = enum.auto()
    ACL_OBJECT_LANGUAGE = enum.auto()
    ACL_OBJECT_LARGEOBJECT = enum.auto()
    ACL_OBJECT_NAMESPACE = enum.auto()
    ACL_OBJECT_TABLESPACE = enum.auto()
    ACL_OBJECT_TYPE = enum.auto()

class GrantTargetType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L1816>`__."

    ACL_TARGET_OBJECT = 0
    ACL_TARGET_ALL_IN_SCHEMA = enum.auto()
    ACL_TARGET_DEFAULTS = enum.auto()

class ImportForeignSchemaType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2271>`__."

    FDW_IMPORT_SCHEMA_ALL = 0
    FDW_IMPORT_SCHEMA_LIMIT_TO = enum.auto()
    FDW_IMPORT_SCHEMA_EXCEPT = enum.auto()

class ObjectType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L1595>`__."

    OBJECT_ACCESS_METHOD = 0
    OBJECT_AGGREGATE = enum.auto()
    OBJECT_AMOP = enum.auto()
    OBJECT_AMPROC = enum.auto()
    OBJECT_ATTRIBUTE = enum.auto()
    OBJECT_CAST = enum.auto()
    OBJECT_COLUMN = enum.auto()
    OBJECT_COLLATION = enum.auto()
    OBJECT_CONVERSION = enum.auto()
    OBJECT_DATABASE = enum.auto()
    OBJECT_DEFAULT = enum.auto()
    OBJECT_DEFACL = enum.auto()
    OBJECT_DOMAIN = enum.auto()
    OBJECT_DOMCONSTRAINT = enum.auto()
    OBJECT_EVENT_TRIGGER = enum.auto()
    OBJECT_EXTENSION = enum.auto()
    OBJECT_FDW = enum.auto()
    OBJECT_FOREIGN_SERVER = enum.auto()
    OBJECT_FOREIGN_TABLE = enum.auto()
    OBJECT_FUNCTION = enum.auto()
    OBJECT_INDEX = enum.auto()
    OBJECT_LANGUAGE = enum.auto()
    OBJECT_LARGEOBJECT = enum.auto()
    OBJECT_MATVIEW = enum.auto()
    OBJECT_OPCLASS = enum.auto()
    OBJECT_OPERATOR = enum.auto()
    OBJECT_OPFAMILY = enum.auto()
    OBJECT_POLICY = enum.auto()
    OBJECT_PUBLICATION = enum.auto()
    OBJECT_PUBLICATION_REL = enum.auto()
    OBJECT_ROLE = enum.auto()
    OBJECT_RULE = enum.auto()
    OBJECT_SCHEMA = enum.auto()
    OBJECT_SEQUENCE = enum.auto()
    OBJECT_SUBSCRIPTION = enum.auto()
    OBJECT_STATISTIC_EXT = enum.auto()
    OBJECT_TABCONSTRAINT = enum.auto()
    OBJECT_TABLE = enum.auto()
    OBJECT_TABLESPACE = enum.auto()
    OBJECT_TRANSFORM = enum.auto()
    OBJECT_TRIGGER = enum.auto()
    OBJECT_TSCONFIGURATION = enum.auto()
    OBJECT_TSDICTIONARY = enum.auto()
    OBJECT_TSPARSER = enum.auto()
    OBJECT_TSTEMPLATE = enum.auto()
    OBJECT_TYPE = enum.auto()
    OBJECT_USER_MAPPING = enum.auto()
    OBJECT_VIEW = enum.auto()

class OverridingKind(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L30>`__."

    OVERRIDING_NOT_SET = 0
    OVERRIDING_USER_VALUE = enum.auto()
    OVERRIDING_SYSTEM_VALUE = enum.auto()

class QuerySource(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L38>`__."

    QSRC_ORIGINAL = 0
    QSRC_PARSER = enum.auto()
    QSRC_INSTEAD_RULE = enum.auto()
    QSRC_QUAL_INSTEAD_RULE = enum.auto()
    QSRC_NON_INSTEAD_RULE = enum.auto()

class RTEKind(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L920>`__."

    RTE_RELATION = 0
    RTE_SUBQUERY = enum.auto()
    RTE_JOIN = enum.auto()
    RTE_FUNCTION = enum.auto()
    RTE_TABLEFUNC = enum.auto()
    RTE_VALUES = enum.auto()
    RTE_CTE = enum.auto()
    RTE_NAMEDTUPLESTORE = enum.auto()

class ReindexObjectType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L3202>`__."

    REINDEX_OBJECT_INDEX = 0
    REINDEX_OBJECT_TABLE = enum.auto()
    REINDEX_OBJECT_SCHEMA = enum.auto()
    REINDEX_OBJECT_SYSTEM = enum.auto()
    REINDEX_OBJECT_DATABASE = enum.auto()

class RoleSpecType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L316>`__."

    ROLESPEC_CSTRING = 0
    ROLESPEC_CURRENT_USER = enum.auto()
    ROLESPEC_SESSION_USER = enum.auto()
    ROLESPEC_PUBLIC = enum.auto()

class RoleStmtType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2408>`__."

    ROLESTMT_ROLE = 0
    ROLESTMT_USER = enum.auto()
    ROLESTMT_GROUP = enum.auto()

class SetOperation(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L1482>`__."

    SETOP_NONE = 0
    SETOP_UNION = enum.auto()
    SETOP_INTERSECT = enum.auto()
    SETOP_EXCEPT = enum.auto()

class SortByDir(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L48>`__."

    SORTBY_DEFAULT = 0
    SORTBY_ASC = enum.auto()
    SORTBY_DESC = enum.auto()
    SORTBY_USING = enum.auto()

class SortByNulls(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L56>`__."

    SORTBY_NULLS_DEFAULT = 0
    SORTBY_NULLS_FIRST = enum.auto()
    SORTBY_NULLS_LAST = enum.auto()

class TableLikeOption(enum.IntFlag):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L667>`__."

    CREATE_TABLE_LIKE_DEFAULTS = 1 << 0
    CREATE_TABLE_LIKE_CONSTRAINTS = 1 << 1
    CREATE_TABLE_LIKE_IDENTITY = 1 << 2
    CREATE_TABLE_LIKE_INDEXES = 1 << 3
    CREATE_TABLE_LIKE_STORAGE = 1 << 4
    CREATE_TABLE_LIKE_COMMENTS = 1 << 5
    CREATE_TABLE_LIKE_ALL = 0x7FFFFFFF

class TransactionStmtKind(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2901>`__."

    TRANS_STMT_BEGIN = 0
    TRANS_STMT_START = enum.auto()
    TRANS_STMT_COMMIT = enum.auto()
    TRANS_STMT_ROLLBACK = enum.auto()
    TRANS_STMT_SAVEPOINT = enum.auto()
    TRANS_STMT_RELEASE = enum.auto()
    TRANS_STMT_ROLLBACK_TO = enum.auto()
    TRANS_STMT_PREPARE = enum.auto()
    TRANS_STMT_COMMIT_PREPARED = enum.auto()
    TRANS_STMT_ROLLBACK_PREPARED = enum.auto()

class VacuumOption(enum.IntFlag):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L3073>`__."

    VACOPT_VACUUM = 1 << 0
    VACOPT_ANALYZE = 1 << 1
    VACOPT_VERBOSE = 1 << 2
    VACOPT_FREEZE = 1 << 3
    VACOPT_FULL = 1 << 4
    VACOPT_NOWAIT = 1 << 5
    VACOPT_SKIPTOAST = 1 << 6
    VACOPT_DISABLE_PAGE_SKIPPING = 1 << 7

class ViewCheckOption(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2975>`__."

    NO_CHECK_OPTION = 0
    LOCAL_CHECK_OPTION = enum.auto()
    CASCADED_CHECK_OPTION = enum.auto()

class WCOKind(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L1097>`__."

    WCO_VIEW_CHECK = 0
    WCO_RLS_INSERT_CHECK = enum.auto()
    WCO_RLS_UPDATE_CHECK = enum.auto()
    WCO_RLS_CONFLICT_CHECK = enum.auto()


# #define-ed constants

ACL_INSERT = 1<<0
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L72>`__."

ACL_SELECT = 1<<1
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L73>`__."

ACL_UPDATE = 1<<2
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L74>`__."

ACL_DELETE = 1<<3
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L75>`__."

ACL_TRUNCATE = 1<<4
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L76>`__."

ACL_REFERENCES = 1<<5
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L77>`__."

ACL_TRIGGER = 1<<6
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L78>`__."

ACL_EXECUTE = 1<<7
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L79>`__."

ACL_USAGE = 1<<8
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L80>`__."

ACL_CREATE = 1<<9
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L82>`__."

ACL_CREATE_TEMP = 1<<10
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L83>`__."

ACL_CONNECT = 1<<11
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L84>`__."

FRAMEOPTION_NONDEFAULT = 0x00001
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L504>`__."

FRAMEOPTION_RANGE = 0x00002
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L505>`__."

FRAMEOPTION_ROWS = 0x00004
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L506>`__."

FRAMEOPTION_BETWEEN = 0x00008
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L507>`__."

FRAMEOPTION_START_UNBOUNDED_PRECEDING = 0x00010
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L508>`__."

FRAMEOPTION_END_UNBOUNDED_PRECEDING = 0x00020
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L509>`__."

FRAMEOPTION_START_UNBOUNDED_FOLLOWING = 0x00040
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L510>`__."

FRAMEOPTION_END_UNBOUNDED_FOLLOWING = 0x00080
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L511>`__."

FRAMEOPTION_START_CURRENT_ROW = 0x00100
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L512>`__."

FRAMEOPTION_END_CURRENT_ROW = 0x00200
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L513>`__."

FRAMEOPTION_START_VALUE_PRECEDING = 0x00400
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L514>`__."

FRAMEOPTION_END_VALUE_PRECEDING = 0x00800
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L515>`__."

FRAMEOPTION_START_VALUE_FOLLOWING = 0x01000
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L516>`__."

FRAMEOPTION_END_VALUE_FOLLOWING = 0x02000
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L517>`__."

CURSOR_OPT_BINARY = 0x0001
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2614>`__."

CURSOR_OPT_SCROLL = 0x0002
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2615>`__."

CURSOR_OPT_NO_SCROLL = 0x0004
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2616>`__."

CURSOR_OPT_INSENSITIVE = 0x0008
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2617>`__."

CURSOR_OPT_HOLD = 0x0010
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2618>`__."

CURSOR_OPT_FAST_PLAN = 0x0020
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2620>`__."

CURSOR_OPT_GENERIC_PLAN = 0x0040
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2621>`__."

CURSOR_OPT_CUSTOM_PLAN = 0x0080
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2622>`__."

CURSOR_OPT_PARALLEL_OK = 0x0100
"See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/parsenodes.h#L2623>`__."
