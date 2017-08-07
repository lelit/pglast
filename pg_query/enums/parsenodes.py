# -*- coding: utf-8 -*-
# :Project:   pg_query -- DO NOT EDIT: automatically extracted from parsenodes.h @ 10-latest-0-g60de51e
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

import enum


class A_Expr_Kind(enum.IntEnum):
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

class AggSplit(enum.IntEnum):
    AGGSPLIT_SIMPLE = 0
    AGGSPLIT_INITIAL_SERIAL = 0x02 | 0x04
    AGGSPLIT_FINAL_DESERIAL = 0x01 | 0x08

class AggStrategy(enum.IntEnum):
    AGG_PLAIN = 0
    AGG_SORTED = enum.auto()
    AGG_HASHED = enum.auto()
    AGG_MIXED = enum.auto()

class AlterSubscriptionType(enum.IntEnum):
    ALTER_SUBSCRIPTION_OPTIONS = 0
    ALTER_SUBSCRIPTION_CONNECTION = enum.auto()
    ALTER_SUBSCRIPTION_PUBLICATION = enum.auto()
    ALTER_SUBSCRIPTION_REFRESH = enum.auto()
    ALTER_SUBSCRIPTION_ENABLED = enum.auto()

class AlterTSConfigType(enum.IntEnum):
    ALTER_TSCONFIG_ADD_MAPPING = 0
    ALTER_TSCONFIG_ALTER_MAPPING_FOR_TOKEN = enum.auto()
    ALTER_TSCONFIG_REPLACE_DICT = enum.auto()
    ALTER_TSCONFIG_REPLACE_DICT_FOR_TOKEN = enum.auto()
    ALTER_TSCONFIG_DROP_MAPPING = enum.auto()

class AlterTableType(enum.IntEnum):
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

class BoolExprType(enum.IntEnum):
    AND_EXPR = 0
    OR_EXPR = enum.auto()
    NOT_EXPR = enum.auto()

class BoolTestType(enum.IntEnum):
    IS_TRUE = 0
    IS_NOT_TRUE = enum.auto()
    IS_FALSE = enum.auto()
    IS_NOT_FALSE = enum.auto()
    IS_UNKNOWN = enum.auto()
    IS_NOT_UNKNOWN = enum.auto()

class CmdType(enum.IntEnum):
    CMD_UNKNOWN = 0
    CMD_SELECT = enum.auto()
    CMD_UPDATE = enum.auto()
    CMD_INSERT = enum.auto()
    CMD_DELETE = enum.auto()
    CMD_UTILITY = enum.auto()
    CMD_NOTHING = enum.auto()

class CoercionContext(enum.IntEnum):
    COERCION_IMPLICIT = 0
    COERCION_ASSIGNMENT = enum.auto()
    COERCION_EXPLICIT = enum.auto()

class CoercionForm(enum.IntEnum):
    COERCE_EXPLICIT_CALL = 0
    COERCE_EXPLICIT_CAST = enum.auto()
    COERCE_IMPLICIT_CAST = enum.auto()

class ConstrType(enum.IntEnum):
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
    DEFELEM_UNSPEC = 0
    DEFELEM_SET = enum.auto()
    DEFELEM_ADD = enum.auto()
    DEFELEM_DROP = enum.auto()

class DiscardMode(enum.IntEnum):
    DISCARD_ALL = 0
    DISCARD_PLANS = enum.auto()
    DISCARD_SEQUENCES = enum.auto()
    DISCARD_TEMP = enum.auto()

class DropBehavior(enum.IntEnum):
    DROP_RESTRICT = 0
    DROP_CASCADE = enum.auto()

class FetchDirection(enum.IntEnum):
    FETCH_FORWARD = 0
    FETCH_BACKWARD = enum.auto()
    FETCH_ABSOLUTE = enum.auto()
    FETCH_RELATIVE = enum.auto()

class FunctionParameterMode(str, enum.Enum):
    FUNC_PARAM_IN = 'i'
    FUNC_PARAM_OUT = 'o'
    FUNC_PARAM_INOUT = 'b'
    FUNC_PARAM_VARIADIC = 'v'
    FUNC_PARAM_TABLE = 't'

class GrantObjectType(enum.IntEnum):
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
    ACL_TARGET_OBJECT = 0
    ACL_TARGET_ALL_IN_SCHEMA = enum.auto()
    ACL_TARGET_DEFAULTS = enum.auto()

class ImportForeignSchemaType(enum.IntEnum):
    FDW_IMPORT_SCHEMA_ALL = 0
    FDW_IMPORT_SCHEMA_LIMIT_TO = enum.auto()
    FDW_IMPORT_SCHEMA_EXCEPT = enum.auto()

class JoinType(enum.IntEnum):
    JOIN_INNER = 0
    JOIN_LEFT = enum.auto()
    JOIN_FULL = enum.auto()
    JOIN_RIGHT = enum.auto()
    JOIN_SEMI = enum.auto()
    JOIN_ANTI = enum.auto()
    JOIN_UNIQUE_OUTER = enum.auto()
    JOIN_UNIQUE_INNER = enum.auto()

class LockClauseStrength(enum.IntEnum):
    LCS_NONE = 0
    LCS_FORKEYSHARE = enum.auto()
    LCS_FORSHARE = enum.auto()
    LCS_FORNOKEYUPDATE = enum.auto()
    LCS_FORUPDATE = enum.auto()

class LockWaitPolicy(enum.IntEnum):
    LockWaitBlock = 0
    LockWaitSkip = enum.auto()
    LockWaitError = enum.auto()

class MinMaxOp(enum.IntEnum):
    IS_GREATEST = 0
    IS_LEAST = enum.auto()

class NodeTag(enum.IntEnum):
    T_Invalid = 0
    T_IndexInfo = enum.auto()
    T_ExprContext = enum.auto()
    T_ProjectionInfo = enum.auto()
    T_JunkFilter = enum.auto()
    T_ResultRelInfo = enum.auto()
    T_EState = enum.auto()
    T_TupleTableSlot = enum.auto()
    T_Plan = enum.auto()
    T_Result = enum.auto()
    T_ProjectSet = enum.auto()
    T_ModifyTable = enum.auto()
    T_Append = enum.auto()
    T_MergeAppend = enum.auto()
    T_RecursiveUnion = enum.auto()
    T_BitmapAnd = enum.auto()
    T_BitmapOr = enum.auto()
    T_Scan = enum.auto()
    T_SeqScan = enum.auto()
    T_SampleScan = enum.auto()
    T_IndexScan = enum.auto()
    T_IndexOnlyScan = enum.auto()
    T_BitmapIndexScan = enum.auto()
    T_BitmapHeapScan = enum.auto()
    T_TidScan = enum.auto()
    T_SubqueryScan = enum.auto()
    T_FunctionScan = enum.auto()
    T_ValuesScan = enum.auto()
    T_TableFuncScan = enum.auto()
    T_CteScan = enum.auto()
    T_NamedTuplestoreScan = enum.auto()
    T_WorkTableScan = enum.auto()
    T_ForeignScan = enum.auto()
    T_CustomScan = enum.auto()
    T_Join = enum.auto()
    T_NestLoop = enum.auto()
    T_MergeJoin = enum.auto()
    T_HashJoin = enum.auto()
    T_Material = enum.auto()
    T_Sort = enum.auto()
    T_Group = enum.auto()
    T_Agg = enum.auto()
    T_WindowAgg = enum.auto()
    T_Unique = enum.auto()
    T_Gather = enum.auto()
    T_GatherMerge = enum.auto()
    T_Hash = enum.auto()
    T_SetOp = enum.auto()
    T_LockRows = enum.auto()
    T_Limit = enum.auto()
    T_NestLoopParam = enum.auto()
    T_PlanRowMark = enum.auto()
    T_PlanInvalItem = enum.auto()
    T_PlanState = enum.auto()
    T_ResultState = enum.auto()
    T_ProjectSetState = enum.auto()
    T_ModifyTableState = enum.auto()
    T_AppendState = enum.auto()
    T_MergeAppendState = enum.auto()
    T_RecursiveUnionState = enum.auto()
    T_BitmapAndState = enum.auto()
    T_BitmapOrState = enum.auto()
    T_ScanState = enum.auto()
    T_SeqScanState = enum.auto()
    T_SampleScanState = enum.auto()
    T_IndexScanState = enum.auto()
    T_IndexOnlyScanState = enum.auto()
    T_BitmapIndexScanState = enum.auto()
    T_BitmapHeapScanState = enum.auto()
    T_TidScanState = enum.auto()
    T_SubqueryScanState = enum.auto()
    T_FunctionScanState = enum.auto()
    T_TableFuncScanState = enum.auto()
    T_ValuesScanState = enum.auto()
    T_CteScanState = enum.auto()
    T_NamedTuplestoreScanState = enum.auto()
    T_WorkTableScanState = enum.auto()
    T_ForeignScanState = enum.auto()
    T_CustomScanState = enum.auto()
    T_JoinState = enum.auto()
    T_NestLoopState = enum.auto()
    T_MergeJoinState = enum.auto()
    T_HashJoinState = enum.auto()
    T_MaterialState = enum.auto()
    T_SortState = enum.auto()
    T_GroupState = enum.auto()
    T_AggState = enum.auto()
    T_WindowAggState = enum.auto()
    T_UniqueState = enum.auto()
    T_GatherState = enum.auto()
    T_GatherMergeState = enum.auto()
    T_HashState = enum.auto()
    T_SetOpState = enum.auto()
    T_LockRowsState = enum.auto()
    T_LimitState = enum.auto()
    T_Alias = enum.auto()
    T_RangeVar = enum.auto()
    T_TableFunc = enum.auto()
    T_Expr = enum.auto()
    T_Var = enum.auto()
    T_Const = enum.auto()
    T_Param = enum.auto()
    T_Aggref = enum.auto()
    T_GroupingFunc = enum.auto()
    T_WindowFunc = enum.auto()
    T_ArrayRef = enum.auto()
    T_FuncExpr = enum.auto()
    T_NamedArgExpr = enum.auto()
    T_OpExpr = enum.auto()
    T_DistinctExpr = enum.auto()
    T_NullIfExpr = enum.auto()
    T_ScalarArrayOpExpr = enum.auto()
    T_BoolExpr = enum.auto()
    T_SubLink = enum.auto()
    T_SubPlan = enum.auto()
    T_AlternativeSubPlan = enum.auto()
    T_FieldSelect = enum.auto()
    T_FieldStore = enum.auto()
    T_RelabelType = enum.auto()
    T_CoerceViaIO = enum.auto()
    T_ArrayCoerceExpr = enum.auto()
    T_ConvertRowtypeExpr = enum.auto()
    T_CollateExpr = enum.auto()
    T_CaseExpr = enum.auto()
    T_CaseWhen = enum.auto()
    T_CaseTestExpr = enum.auto()
    T_ArrayExpr = enum.auto()
    T_RowExpr = enum.auto()
    T_RowCompareExpr = enum.auto()
    T_CoalesceExpr = enum.auto()
    T_MinMaxExpr = enum.auto()
    T_SQLValueFunction = enum.auto()
    T_XmlExpr = enum.auto()
    T_NullTest = enum.auto()
    T_BooleanTest = enum.auto()
    T_CoerceToDomain = enum.auto()
    T_CoerceToDomainValue = enum.auto()
    T_SetToDefault = enum.auto()
    T_CurrentOfExpr = enum.auto()
    T_InferenceElem = enum.auto()
    T_TargetEntry = enum.auto()
    T_RangeTblRef = enum.auto()
    T_JoinExpr = enum.auto()
    T_FromExpr = enum.auto()
    T_OnConflictExpr = enum.auto()
    T_IntoClause = enum.auto()
    T_NextValueExpr = enum.auto()
    T_ExprState = enum.auto()
    T_AggrefExprState = enum.auto()
    T_WindowFuncExprState = enum.auto()
    T_SetExprState = enum.auto()
    T_SubPlanState = enum.auto()
    T_AlternativeSubPlanState = enum.auto()
    T_DomainConstraintState = enum.auto()
    T_PlannerInfo = enum.auto()
    T_PlannerGlobal = enum.auto()
    T_RelOptInfo = enum.auto()
    T_IndexOptInfo = enum.auto()
    T_ForeignKeyOptInfo = enum.auto()
    T_ParamPathInfo = enum.auto()
    T_Path = enum.auto()
    T_IndexPath = enum.auto()
    T_BitmapHeapPath = enum.auto()
    T_BitmapAndPath = enum.auto()
    T_BitmapOrPath = enum.auto()
    T_TidPath = enum.auto()
    T_SubqueryScanPath = enum.auto()
    T_ForeignPath = enum.auto()
    T_CustomPath = enum.auto()
    T_NestPath = enum.auto()
    T_MergePath = enum.auto()
    T_HashPath = enum.auto()
    T_AppendPath = enum.auto()
    T_MergeAppendPath = enum.auto()
    T_ResultPath = enum.auto()
    T_MaterialPath = enum.auto()
    T_UniquePath = enum.auto()
    T_GatherPath = enum.auto()
    T_GatherMergePath = enum.auto()
    T_ProjectionPath = enum.auto()
    T_ProjectSetPath = enum.auto()
    T_SortPath = enum.auto()
    T_GroupPath = enum.auto()
    T_UpperUniquePath = enum.auto()
    T_AggPath = enum.auto()
    T_GroupingSetsPath = enum.auto()
    T_MinMaxAggPath = enum.auto()
    T_WindowAggPath = enum.auto()
    T_SetOpPath = enum.auto()
    T_RecursiveUnionPath = enum.auto()
    T_LockRowsPath = enum.auto()
    T_ModifyTablePath = enum.auto()
    T_LimitPath = enum.auto()
    T_EquivalenceClass = enum.auto()
    T_EquivalenceMember = enum.auto()
    T_PathKey = enum.auto()
    T_PathTarget = enum.auto()
    T_RestrictInfo = enum.auto()
    T_PlaceHolderVar = enum.auto()
    T_SpecialJoinInfo = enum.auto()
    T_AppendRelInfo = enum.auto()
    T_PartitionedChildRelInfo = enum.auto()
    T_PlaceHolderInfo = enum.auto()
    T_MinMaxAggInfo = enum.auto()
    T_PlannerParamItem = enum.auto()
    T_RollupData = enum.auto()
    T_GroupingSetData = enum.auto()
    T_StatisticExtInfo = enum.auto()
    T_MemoryContext = enum.auto()
    T_AllocSetContext = enum.auto()
    T_SlabContext = enum.auto()
    T_Value = enum.auto()
    T_Integer = enum.auto()
    T_Float = enum.auto()
    T_String = enum.auto()
    T_BitString = enum.auto()
    T_Null = enum.auto()
    T_List = enum.auto()
    T_IntList = enum.auto()
    T_OidList = enum.auto()
    T_ExtensibleNode = enum.auto()
    T_RawStmt = enum.auto()
    T_Query = enum.auto()
    T_PlannedStmt = enum.auto()
    T_InsertStmt = enum.auto()
    T_DeleteStmt = enum.auto()
    T_UpdateStmt = enum.auto()
    T_SelectStmt = enum.auto()
    T_AlterTableStmt = enum.auto()
    T_AlterTableCmd = enum.auto()
    T_AlterDomainStmt = enum.auto()
    T_SetOperationStmt = enum.auto()
    T_GrantStmt = enum.auto()
    T_GrantRoleStmt = enum.auto()
    T_AlterDefaultPrivilegesStmt = enum.auto()
    T_ClosePortalStmt = enum.auto()
    T_ClusterStmt = enum.auto()
    T_CopyStmt = enum.auto()
    T_CreateStmt = enum.auto()
    T_DefineStmt = enum.auto()
    T_DropStmt = enum.auto()
    T_TruncateStmt = enum.auto()
    T_CommentStmt = enum.auto()
    T_FetchStmt = enum.auto()
    T_IndexStmt = enum.auto()
    T_CreateFunctionStmt = enum.auto()
    T_AlterFunctionStmt = enum.auto()
    T_DoStmt = enum.auto()
    T_RenameStmt = enum.auto()
    T_RuleStmt = enum.auto()
    T_NotifyStmt = enum.auto()
    T_ListenStmt = enum.auto()
    T_UnlistenStmt = enum.auto()
    T_TransactionStmt = enum.auto()
    T_ViewStmt = enum.auto()
    T_LoadStmt = enum.auto()
    T_CreateDomainStmt = enum.auto()
    T_CreatedbStmt = enum.auto()
    T_DropdbStmt = enum.auto()
    T_VacuumStmt = enum.auto()
    T_ExplainStmt = enum.auto()
    T_CreateTableAsStmt = enum.auto()
    T_CreateSeqStmt = enum.auto()
    T_AlterSeqStmt = enum.auto()
    T_VariableSetStmt = enum.auto()
    T_VariableShowStmt = enum.auto()
    T_DiscardStmt = enum.auto()
    T_CreateTrigStmt = enum.auto()
    T_CreatePLangStmt = enum.auto()
    T_CreateRoleStmt = enum.auto()
    T_AlterRoleStmt = enum.auto()
    T_DropRoleStmt = enum.auto()
    T_LockStmt = enum.auto()
    T_ConstraintsSetStmt = enum.auto()
    T_ReindexStmt = enum.auto()
    T_CheckPointStmt = enum.auto()
    T_CreateSchemaStmt = enum.auto()
    T_AlterDatabaseStmt = enum.auto()
    T_AlterDatabaseSetStmt = enum.auto()
    T_AlterRoleSetStmt = enum.auto()
    T_CreateConversionStmt = enum.auto()
    T_CreateCastStmt = enum.auto()
    T_CreateOpClassStmt = enum.auto()
    T_CreateOpFamilyStmt = enum.auto()
    T_AlterOpFamilyStmt = enum.auto()
    T_PrepareStmt = enum.auto()
    T_ExecuteStmt = enum.auto()
    T_DeallocateStmt = enum.auto()
    T_DeclareCursorStmt = enum.auto()
    T_CreateTableSpaceStmt = enum.auto()
    T_DropTableSpaceStmt = enum.auto()
    T_AlterObjectDependsStmt = enum.auto()
    T_AlterObjectSchemaStmt = enum.auto()
    T_AlterOwnerStmt = enum.auto()
    T_AlterOperatorStmt = enum.auto()
    T_DropOwnedStmt = enum.auto()
    T_ReassignOwnedStmt = enum.auto()
    T_CompositeTypeStmt = enum.auto()
    T_CreateEnumStmt = enum.auto()
    T_CreateRangeStmt = enum.auto()
    T_AlterEnumStmt = enum.auto()
    T_AlterTSDictionaryStmt = enum.auto()
    T_AlterTSConfigurationStmt = enum.auto()
    T_CreateFdwStmt = enum.auto()
    T_AlterFdwStmt = enum.auto()
    T_CreateForeignServerStmt = enum.auto()
    T_AlterForeignServerStmt = enum.auto()
    T_CreateUserMappingStmt = enum.auto()
    T_AlterUserMappingStmt = enum.auto()
    T_DropUserMappingStmt = enum.auto()
    T_AlterTableSpaceOptionsStmt = enum.auto()
    T_AlterTableMoveAllStmt = enum.auto()
    T_SecLabelStmt = enum.auto()
    T_CreateForeignTableStmt = enum.auto()
    T_ImportForeignSchemaStmt = enum.auto()
    T_CreateExtensionStmt = enum.auto()
    T_AlterExtensionStmt = enum.auto()
    T_AlterExtensionContentsStmt = enum.auto()
    T_CreateEventTrigStmt = enum.auto()
    T_AlterEventTrigStmt = enum.auto()
    T_RefreshMatViewStmt = enum.auto()
    T_ReplicaIdentityStmt = enum.auto()
    T_AlterSystemStmt = enum.auto()
    T_CreatePolicyStmt = enum.auto()
    T_AlterPolicyStmt = enum.auto()
    T_CreateTransformStmt = enum.auto()
    T_CreateAmStmt = enum.auto()
    T_CreatePublicationStmt = enum.auto()
    T_AlterPublicationStmt = enum.auto()
    T_CreateSubscriptionStmt = enum.auto()
    T_AlterSubscriptionStmt = enum.auto()
    T_DropSubscriptionStmt = enum.auto()
    T_CreateStatsStmt = enum.auto()
    T_AlterCollationStmt = enum.auto()
    T_A_Expr = enum.auto()
    T_ColumnRef = enum.auto()
    T_ParamRef = enum.auto()
    T_A_Const = enum.auto()
    T_FuncCall = enum.auto()
    T_A_Star = enum.auto()
    T_A_Indices = enum.auto()
    T_A_Indirection = enum.auto()
    T_A_ArrayExpr = enum.auto()
    T_ResTarget = enum.auto()
    T_MultiAssignRef = enum.auto()
    T_TypeCast = enum.auto()
    T_CollateClause = enum.auto()
    T_SortBy = enum.auto()
    T_WindowDef = enum.auto()
    T_RangeSubselect = enum.auto()
    T_RangeFunction = enum.auto()
    T_RangeTableSample = enum.auto()
    T_RangeTableFunc = enum.auto()
    T_RangeTableFuncCol = enum.auto()
    T_TypeName = enum.auto()
    T_ColumnDef = enum.auto()
    T_IndexElem = enum.auto()
    T_Constraint = enum.auto()
    T_DefElem = enum.auto()
    T_RangeTblEntry = enum.auto()
    T_RangeTblFunction = enum.auto()
    T_TableSampleClause = enum.auto()
    T_WithCheckOption = enum.auto()
    T_SortGroupClause = enum.auto()
    T_GroupingSet = enum.auto()
    T_WindowClause = enum.auto()
    T_ObjectWithArgs = enum.auto()
    T_AccessPriv = enum.auto()
    T_CreateOpClassItem = enum.auto()
    T_TableLikeClause = enum.auto()
    T_FunctionParameter = enum.auto()
    T_LockingClause = enum.auto()
    T_RowMarkClause = enum.auto()
    T_XmlSerialize = enum.auto()
    T_WithClause = enum.auto()
    T_InferClause = enum.auto()
    T_OnConflictClause = enum.auto()
    T_CommonTableExpr = enum.auto()
    T_RoleSpec = enum.auto()
    T_TriggerTransition = enum.auto()
    T_PartitionElem = enum.auto()
    T_PartitionSpec = enum.auto()
    T_PartitionBoundSpec = enum.auto()
    T_PartitionRangeDatum = enum.auto()
    T_PartitionCmd = enum.auto()
    T_IdentifySystemCmd = enum.auto()
    T_BaseBackupCmd = enum.auto()
    T_CreateReplicationSlotCmd = enum.auto()
    T_DropReplicationSlotCmd = enum.auto()
    T_StartReplicationCmd = enum.auto()
    T_TimeLineHistoryCmd = enum.auto()
    T_SQLCmd = enum.auto()
    T_TriggerData = enum.auto()
    T_EventTriggerData = enum.auto()
    T_ReturnSetInfo = enum.auto()
    T_WindowObjectData = enum.auto()
    T_TIDBitmap = enum.auto()
    T_InlineCodeBlock = enum.auto()
    T_FdwRoutine = enum.auto()
    T_IndexAmRoutine = enum.auto()
    T_TsmRoutine = enum.auto()
    T_ForeignKeyCacheInfo = enum.auto()

class NullTestType(enum.IntEnum):
    IS_NULL = 0
    IS_NOT_NULL = enum.auto()

class ObjectType(enum.IntEnum):
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

class OnCommitAction(enum.IntEnum):
    ONCOMMIT_NOOP = 0
    ONCOMMIT_PRESERVE_ROWS = enum.auto()
    ONCOMMIT_DELETE_ROWS = enum.auto()
    ONCOMMIT_DROP = enum.auto()

class OnConflictAction(enum.IntEnum):
    ONCONFLICT_NONE = 0
    ONCONFLICT_NOTHING = enum.auto()
    ONCONFLICT_UPDATE = enum.auto()

class OverridingKind(enum.IntEnum):
    OVERRIDING_NOT_SET = 0
    OVERRIDING_USER_VALUE = enum.auto()
    OVERRIDING_SYSTEM_VALUE = enum.auto()

class ParamKind(enum.IntEnum):
    PARAM_EXTERN = 0
    PARAM_EXEC = enum.auto()
    PARAM_SUBLINK = enum.auto()
    PARAM_MULTIEXPR = enum.auto()

class QuerySource(enum.IntEnum):
    QSRC_ORIGINAL = 0
    QSRC_PARSER = enum.auto()
    QSRC_INSTEAD_RULE = enum.auto()
    QSRC_QUAL_INSTEAD_RULE = enum.auto()
    QSRC_NON_INSTEAD_RULE = enum.auto()

class RTEKind(enum.IntEnum):
    RTE_RELATION = 0
    RTE_SUBQUERY = enum.auto()
    RTE_JOIN = enum.auto()
    RTE_FUNCTION = enum.auto()
    RTE_TABLEFUNC = enum.auto()
    RTE_VALUES = enum.auto()
    RTE_CTE = enum.auto()
    RTE_NAMEDTUPLESTORE = enum.auto()

class ReindexObjectType(enum.IntEnum):
    REINDEX_OBJECT_INDEX = 0
    REINDEX_OBJECT_TABLE = enum.auto()
    REINDEX_OBJECT_SCHEMA = enum.auto()
    REINDEX_OBJECT_SYSTEM = enum.auto()
    REINDEX_OBJECT_DATABASE = enum.auto()

class RoleSpecType(enum.IntEnum):
    ROLESPEC_CSTRING = 0
    ROLESPEC_CURRENT_USER = enum.auto()
    ROLESPEC_SESSION_USER = enum.auto()
    ROLESPEC_PUBLIC = enum.auto()

class RoleStmtType(enum.IntEnum):
    ROLESTMT_ROLE = 0
    ROLESTMT_USER = enum.auto()
    ROLESTMT_GROUP = enum.auto()

class RowCompareType(enum.IntEnum):
    ROWCOMPARE_LT = 1
    ROWCOMPARE_LE = 2
    ROWCOMPARE_EQ = 3
    ROWCOMPARE_GE = 4
    ROWCOMPARE_GT = 5
    ROWCOMPARE_NE = 6

class SQLValueFunctionOp(enum.IntEnum):
    SVFOP_CURRENT_DATE = 0
    SVFOP_CURRENT_TIME = enum.auto()
    SVFOP_CURRENT_TIME_N = enum.auto()
    SVFOP_CURRENT_TIMESTAMP = enum.auto()
    SVFOP_CURRENT_TIMESTAMP_N = enum.auto()
    SVFOP_LOCALTIME = enum.auto()
    SVFOP_LOCALTIME_N = enum.auto()
    SVFOP_LOCALTIMESTAMP = enum.auto()
    SVFOP_LOCALTIMESTAMP_N = enum.auto()
    SVFOP_CURRENT_ROLE = enum.auto()
    SVFOP_CURRENT_USER = enum.auto()
    SVFOP_USER = enum.auto()
    SVFOP_SESSION_USER = enum.auto()
    SVFOP_CURRENT_CATALOG = enum.auto()
    SVFOP_CURRENT_SCHEMA = enum.auto()

class SetOpCmd(enum.IntEnum):
    SETOPCMD_INTERSECT = 0
    SETOPCMD_INTERSECT_ALL = enum.auto()
    SETOPCMD_EXCEPT = enum.auto()
    SETOPCMD_EXCEPT_ALL = enum.auto()

class SetOpStrategy(enum.IntEnum):
    SETOP_SORTED = 0
    SETOP_HASHED = enum.auto()

class SetOperation(enum.IntEnum):
    SETOP_NONE = 0
    SETOP_UNION = enum.auto()
    SETOP_INTERSECT = enum.auto()
    SETOP_EXCEPT = enum.auto()

class SortByDir(enum.IntEnum):
    SORTBY_DEFAULT = 0
    SORTBY_ASC = enum.auto()
    SORTBY_DESC = enum.auto()
    SORTBY_USING = enum.auto()

class SortByNulls(enum.IntEnum):
    SORTBY_NULLS_DEFAULT = 0
    SORTBY_NULLS_FIRST = enum.auto()
    SORTBY_NULLS_LAST = enum.auto()

class SubLinkType(enum.IntEnum):
    EXISTS_SUBLINK = 0
    ALL_SUBLINK = enum.auto()
    ANY_SUBLINK = enum.auto()
    ROWCOMPARE_SUBLINK = enum.auto()
    EXPR_SUBLINK = enum.auto()
    MULTIEXPR_SUBLINK = enum.auto()
    ARRAY_SUBLINK = enum.auto()
    CTE_SUBLINK = enum.auto()

class TableLikeOption(enum.IntFlag):
    CREATE_TABLE_LIKE_DEFAULTS = 1 << 0
    CREATE_TABLE_LIKE_CONSTRAINTS = 1 << 1
    CREATE_TABLE_LIKE_IDENTITY = 1 << 2
    CREATE_TABLE_LIKE_INDEXES = 1 << 3
    CREATE_TABLE_LIKE_STORAGE = 1 << 4
    CREATE_TABLE_LIKE_COMMENTS = 1 << 5
    CREATE_TABLE_LIKE_ALL = 0x7FFFFFFF

class TransactionStmtKind(enum.IntEnum):
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
    VACOPT_VACUUM = 1 << 0
    VACOPT_ANALYZE = 1 << 1
    VACOPT_VERBOSE = 1 << 2
    VACOPT_FREEZE = 1 << 3
    VACOPT_FULL = 1 << 4
    VACOPT_NOWAIT = 1 << 5
    VACOPT_SKIPTOAST = 1 << 6
    VACOPT_DISABLE_PAGE_SKIPPING = 1 << 7

class ViewCheckOption(enum.IntEnum):
    NO_CHECK_OPTION = 0
    LOCAL_CHECK_OPTION = enum.auto()
    CASCADED_CHECK_OPTION = enum.auto()

class WCOKind(enum.IntEnum):
    WCO_VIEW_CHECK = 0
    WCO_RLS_INSERT_CHECK = enum.auto()
    WCO_RLS_UPDATE_CHECK = enum.auto()
    WCO_RLS_CONFLICT_CHECK = enum.auto()

class XmlExprOp(enum.IntEnum):
    IS_XMLCONCAT = 0
    IS_XMLELEMENT = enum.auto()
    IS_XMLFOREST = enum.auto()
    IS_XMLPARSE = enum.auto()
    IS_XMLPI = enum.auto()
    IS_XMLROOT = enum.auto()
    IS_XMLSERIALIZE = enum.auto()
    IS_DOCUMENT = enum.auto()
