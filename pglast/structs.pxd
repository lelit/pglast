# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from struct_defs.json @ 14-latest-0-g6ebd8d8
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021-2022 Lele Gaifax
#

#cython: language_level=3

from libc.stdint cimport int16_t, int32_t, uint32_t, uint64_t


cdef extern from "postgres.h":
    ctypedef unsigned char bool

    ctypedef struct Node:
        int type

    ctypedef union ValueUnion:
        int ival
        char *str

    ctypedef struct Value:
        int type
        ValueUnion val

    ctypedef struct Bitmapset:
        int nwords
        unsigned long *words


cdef extern from "nodes/bitmapset.h":
    ctypedef struct Bitmapset:
        pass

    int bms_next_member(const Bitmapset *a, int prevbit)


cdef extern from "nodes/pg_list.h":
    ctypedef struct List:
        int length

    void* list_nth(List* list, int n)


cdef extern from "nodes/value.h":
    ctypedef struct ValUnion:
        int ival
        char *str

    ctypedef struct Value:
        NodeTag type
        ValUnion val

    int intVal(Value* v)
    char* strVal(Value* v)


cdef extern from *:
    ctypedef enum A_Expr_Kind:
        pass

    ctypedef enum AggSplit:
        pass

    ctypedef enum AggStrategy:
        pass

    ctypedef enum AlterSubscriptionType:
        pass

    ctypedef enum AlterTSConfigType:
        pass

    ctypedef enum AlterTableType:
        pass

    ctypedef enum BoolExprType:
        pass

    ctypedef enum BoolTestType:
        pass

    ctypedef enum CTEMaterialize:
        pass

    ctypedef enum CmdType:
        pass

    ctypedef enum CoercionContext:
        pass

    ctypedef enum CoercionForm:
        pass

    ctypedef enum ConstrType:
        pass

    ctypedef enum DefElemAction:
        pass

    ctypedef enum DiscardMode:
        pass

    ctypedef enum DropBehavior:
        pass

    ctypedef enum FetchDirection:
        pass

    ctypedef enum FunctionParameterMode:
        pass

    ctypedef enum GrantTargetType:
        pass

    ctypedef enum GroupingSetKind:
        pass

    ctypedef enum ImportForeignSchemaType:
        pass

    ctypedef enum JoinType:
        pass

    ctypedef enum LimitOption:
        pass

    ctypedef enum LockClauseStrength:
        pass

    ctypedef enum LockTupleMode:
        pass

    ctypedef enum LockWaitPolicy:
        pass

    ctypedef enum MinMaxOp:
        pass

    ctypedef enum NodeTag:
        T_Invalid
        T_IndexInfo
        T_ExprContext
        T_ProjectionInfo
        T_JunkFilter
        T_OnConflictSetState
        T_ResultRelInfo
        T_EState
        T_TupleTableSlot
        T_Plan
        T_Result
        T_ProjectSet
        T_ModifyTable
        T_Append
        T_MergeAppend
        T_RecursiveUnion
        T_BitmapAnd
        T_BitmapOr
        T_Scan
        T_SeqScan
        T_SampleScan
        T_IndexScan
        T_IndexOnlyScan
        T_BitmapIndexScan
        T_BitmapHeapScan
        T_TidScan
        T_TidRangeScan
        T_SubqueryScan
        T_FunctionScan
        T_ValuesScan
        T_TableFuncScan
        T_CteScan
        T_NamedTuplestoreScan
        T_WorkTableScan
        T_ForeignScan
        T_CustomScan
        T_Join
        T_NestLoop
        T_MergeJoin
        T_HashJoin
        T_Material
        T_Memoize
        T_Sort
        T_IncrementalSort
        T_Group
        T_Agg
        T_WindowAgg
        T_Unique
        T_Gather
        T_GatherMerge
        T_Hash
        T_SetOp
        T_LockRows
        T_Limit
        T_NestLoopParam
        T_PlanRowMark
        T_PartitionPruneInfo
        T_PartitionedRelPruneInfo
        T_PartitionPruneStepOp
        T_PartitionPruneStepCombine
        T_PlanInvalItem
        T_PlanState
        T_ResultState
        T_ProjectSetState
        T_ModifyTableState
        T_AppendState
        T_MergeAppendState
        T_RecursiveUnionState
        T_BitmapAndState
        T_BitmapOrState
        T_ScanState
        T_SeqScanState
        T_SampleScanState
        T_IndexScanState
        T_IndexOnlyScanState
        T_BitmapIndexScanState
        T_BitmapHeapScanState
        T_TidScanState
        T_TidRangeScanState
        T_SubqueryScanState
        T_FunctionScanState
        T_TableFuncScanState
        T_ValuesScanState
        T_CteScanState
        T_NamedTuplestoreScanState
        T_WorkTableScanState
        T_ForeignScanState
        T_CustomScanState
        T_JoinState
        T_NestLoopState
        T_MergeJoinState
        T_HashJoinState
        T_MaterialState
        T_MemoizeState
        T_SortState
        T_IncrementalSortState
        T_GroupState
        T_AggState
        T_WindowAggState
        T_UniqueState
        T_GatherState
        T_GatherMergeState
        T_HashState
        T_SetOpState
        T_LockRowsState
        T_LimitState
        T_Alias
        T_RangeVar
        T_TableFunc
        T_Expr
        T_Var
        T_Const
        T_Param
        T_Aggref
        T_GroupingFunc
        T_WindowFunc
        T_SubscriptingRef
        T_FuncExpr
        T_NamedArgExpr
        T_OpExpr
        T_DistinctExpr
        T_NullIfExpr
        T_ScalarArrayOpExpr
        T_BoolExpr
        T_SubLink
        T_SubPlan
        T_AlternativeSubPlan
        T_FieldSelect
        T_FieldStore
        T_RelabelType
        T_CoerceViaIO
        T_ArrayCoerceExpr
        T_ConvertRowtypeExpr
        T_CollateExpr
        T_CaseExpr
        T_CaseWhen
        T_CaseTestExpr
        T_ArrayExpr
        T_RowExpr
        T_RowCompareExpr
        T_CoalesceExpr
        T_MinMaxExpr
        T_SQLValueFunction
        T_XmlExpr
        T_NullTest
        T_BooleanTest
        T_CoerceToDomain
        T_CoerceToDomainValue
        T_SetToDefault
        T_CurrentOfExpr
        T_NextValueExpr
        T_InferenceElem
        T_TargetEntry
        T_RangeTblRef
        T_JoinExpr
        T_FromExpr
        T_OnConflictExpr
        T_IntoClause
        T_ExprState
        T_WindowFuncExprState
        T_SetExprState
        T_SubPlanState
        T_DomainConstraintState
        T_PlannerInfo
        T_PlannerGlobal
        T_RelOptInfo
        T_IndexOptInfo
        T_ForeignKeyOptInfo
        T_ParamPathInfo
        T_Path
        T_IndexPath
        T_BitmapHeapPath
        T_BitmapAndPath
        T_BitmapOrPath
        T_TidPath
        T_TidRangePath
        T_SubqueryScanPath
        T_ForeignPath
        T_CustomPath
        T_NestPath
        T_MergePath
        T_HashPath
        T_AppendPath
        T_MergeAppendPath
        T_GroupResultPath
        T_MaterialPath
        T_MemoizePath
        T_UniquePath
        T_GatherPath
        T_GatherMergePath
        T_ProjectionPath
        T_ProjectSetPath
        T_SortPath
        T_IncrementalSortPath
        T_GroupPath
        T_UpperUniquePath
        T_AggPath
        T_GroupingSetsPath
        T_MinMaxAggPath
        T_WindowAggPath
        T_SetOpPath
        T_RecursiveUnionPath
        T_LockRowsPath
        T_ModifyTablePath
        T_LimitPath
        T_EquivalenceClass
        T_EquivalenceMember
        T_PathKey
        T_PathTarget
        T_RestrictInfo
        T_IndexClause
        T_PlaceHolderVar
        T_SpecialJoinInfo
        T_AppendRelInfo
        T_RowIdentityVarInfo
        T_PlaceHolderInfo
        T_MinMaxAggInfo
        T_PlannerParamItem
        T_RollupData
        T_GroupingSetData
        T_StatisticExtInfo
        T_MemoryContext
        T_AllocSetContext
        T_SlabContext
        T_GenerationContext
        T_Value
        T_Integer
        T_Float
        T_String
        T_BitString
        T_Null
        T_List
        T_IntList
        T_OidList
        T_ExtensibleNode
        T_RawStmt
        T_Query
        T_PlannedStmt
        T_InsertStmt
        T_DeleteStmt
        T_UpdateStmt
        T_SelectStmt
        T_ReturnStmt
        T_PLAssignStmt
        T_AlterTableStmt
        T_AlterTableCmd
        T_AlterDomainStmt
        T_SetOperationStmt
        T_GrantStmt
        T_GrantRoleStmt
        T_AlterDefaultPrivilegesStmt
        T_ClosePortalStmt
        T_ClusterStmt
        T_CopyStmt
        T_CreateStmt
        T_DefineStmt
        T_DropStmt
        T_TruncateStmt
        T_CommentStmt
        T_FetchStmt
        T_IndexStmt
        T_CreateFunctionStmt
        T_AlterFunctionStmt
        T_DoStmt
        T_RenameStmt
        T_RuleStmt
        T_NotifyStmt
        T_ListenStmt
        T_UnlistenStmt
        T_TransactionStmt
        T_ViewStmt
        T_LoadStmt
        T_CreateDomainStmt
        T_CreatedbStmt
        T_DropdbStmt
        T_VacuumStmt
        T_ExplainStmt
        T_CreateTableAsStmt
        T_CreateSeqStmt
        T_AlterSeqStmt
        T_VariableSetStmt
        T_VariableShowStmt
        T_DiscardStmt
        T_CreateTrigStmt
        T_CreatePLangStmt
        T_CreateRoleStmt
        T_AlterRoleStmt
        T_DropRoleStmt
        T_LockStmt
        T_ConstraintsSetStmt
        T_ReindexStmt
        T_CheckPointStmt
        T_CreateSchemaStmt
        T_AlterDatabaseStmt
        T_AlterDatabaseSetStmt
        T_AlterRoleSetStmt
        T_CreateConversionStmt
        T_CreateCastStmt
        T_CreateOpClassStmt
        T_CreateOpFamilyStmt
        T_AlterOpFamilyStmt
        T_PrepareStmt
        T_ExecuteStmt
        T_DeallocateStmt
        T_DeclareCursorStmt
        T_CreateTableSpaceStmt
        T_DropTableSpaceStmt
        T_AlterObjectDependsStmt
        T_AlterObjectSchemaStmt
        T_AlterOwnerStmt
        T_AlterOperatorStmt
        T_AlterTypeStmt
        T_DropOwnedStmt
        T_ReassignOwnedStmt
        T_CompositeTypeStmt
        T_CreateEnumStmt
        T_CreateRangeStmt
        T_AlterEnumStmt
        T_AlterTSDictionaryStmt
        T_AlterTSConfigurationStmt
        T_CreateFdwStmt
        T_AlterFdwStmt
        T_CreateForeignServerStmt
        T_AlterForeignServerStmt
        T_CreateUserMappingStmt
        T_AlterUserMappingStmt
        T_DropUserMappingStmt
        T_AlterTableSpaceOptionsStmt
        T_AlterTableMoveAllStmt
        T_SecLabelStmt
        T_CreateForeignTableStmt
        T_ImportForeignSchemaStmt
        T_CreateExtensionStmt
        T_AlterExtensionStmt
        T_AlterExtensionContentsStmt
        T_CreateEventTrigStmt
        T_AlterEventTrigStmt
        T_RefreshMatViewStmt
        T_ReplicaIdentityStmt
        T_AlterSystemStmt
        T_CreatePolicyStmt
        T_AlterPolicyStmt
        T_CreateTransformStmt
        T_CreateAmStmt
        T_CreatePublicationStmt
        T_AlterPublicationStmt
        T_CreateSubscriptionStmt
        T_AlterSubscriptionStmt
        T_DropSubscriptionStmt
        T_CreateStatsStmt
        T_AlterCollationStmt
        T_CallStmt
        T_AlterStatsStmt
        T_A_Expr
        T_ColumnRef
        T_ParamRef
        T_A_Const
        T_FuncCall
        T_A_Star
        T_A_Indices
        T_A_Indirection
        T_A_ArrayExpr
        T_ResTarget
        T_MultiAssignRef
        T_TypeCast
        T_CollateClause
        T_SortBy
        T_WindowDef
        T_RangeSubselect
        T_RangeFunction
        T_RangeTableSample
        T_RangeTableFunc
        T_RangeTableFuncCol
        T_TypeName
        T_ColumnDef
        T_IndexElem
        T_StatsElem
        T_Constraint
        T_DefElem
        T_RangeTblEntry
        T_RangeTblFunction
        T_TableSampleClause
        T_WithCheckOption
        T_SortGroupClause
        T_GroupingSet
        T_WindowClause
        T_ObjectWithArgs
        T_AccessPriv
        T_CreateOpClassItem
        T_TableLikeClause
        T_FunctionParameter
        T_LockingClause
        T_RowMarkClause
        T_XmlSerialize
        T_WithClause
        T_InferClause
        T_OnConflictClause
        T_CTESearchClause
        T_CTECycleClause
        T_CommonTableExpr
        T_RoleSpec
        T_TriggerTransition
        T_PartitionElem
        T_PartitionSpec
        T_PartitionBoundSpec
        T_PartitionRangeDatum
        T_PartitionCmd
        T_VacuumRelation
        T_IdentifySystemCmd
        T_BaseBackupCmd
        T_CreateReplicationSlotCmd
        T_DropReplicationSlotCmd
        T_StartReplicationCmd
        T_TimeLineHistoryCmd
        T_SQLCmd
        T_TriggerData
        T_EventTriggerData
        T_ReturnSetInfo
        T_WindowObjectData
        T_TIDBitmap
        T_InlineCodeBlock
        T_FdwRoutine
        T_IndexAmRoutine
        T_TableAmRoutine
        T_TsmRoutine
        T_ForeignKeyCacheInfo
        T_CallContext
        T_SupportRequestSimplify
        T_SupportRequestSelectivity
        T_SupportRequestCost
        T_SupportRequestRows
        T_SupportRequestIndexCondition

    ctypedef enum NullTestType:
        pass

    ctypedef enum ObjectType:
        pass

    ctypedef enum OnCommitAction:
        pass

    ctypedef enum OnConflictAction:
        pass

    ctypedef enum OverridingKind:
        pass

    ctypedef enum ParamKind:
        pass

    ctypedef enum PartitionRangeDatumKind:
        pass

    ctypedef enum QuerySource:
        pass

    ctypedef enum RTEKind:
        pass

    ctypedef enum ReindexObjectType:
        pass

    ctypedef enum RoleSpecType:
        pass

    ctypedef enum RoleStmtType:
        pass

    ctypedef enum RowCompareType:
        pass

    ctypedef enum SQLValueFunctionOp:
        pass

    ctypedef enum ScanDirection:
        pass

    ctypedef enum SetOpCmd:
        pass

    ctypedef enum SetOpStrategy:
        pass

    ctypedef enum SetOperation:
        pass

    ctypedef enum SetQuantifier:
        pass

    ctypedef enum SortByDir:
        pass

    ctypedef enum SortByNulls:
        pass

    ctypedef enum SubLinkType:
        pass

    ctypedef enum TableLikeOption:
        pass

    ctypedef enum TransactionStmtKind:
        pass

    ctypedef enum VacOptValue:
        pass

    ctypedef enum VariableSetKind:
        pass

    ctypedef enum ViewCheckOption:
        pass

    ctypedef enum WCOKind:
        pass

    ctypedef enum XmlExprOp:
        pass

    ctypedef enum XmlOptionType:
        pass

    ctypedef enum pg_enc:
        pass

    ctypedef enum vartag_external:
        pass

    ctypedef enum yytokentype:
        pass

    int nodeTag(void* data)


cdef extern from "nodes/parsenodes.h":
    ctypedef struct Query:
        NodeTag type
        CmdType commandType
        QuerySource querySource
        uint64_t queryId
        bool canSetTag
        const Node* utilityStmt
        int resultRelation
        bool hasAggs
        bool hasWindowFuncs
        bool hasTargetSRFs
        bool hasSubLinks
        bool hasDistinctOn
        bool hasRecursive
        bool hasModifyingCTE
        bool hasForUpdate
        bool hasRowSecurity
        bool isReturn
        const List* cteList
        const List* rtable
        const FromExpr* jointree
        const List* targetList
        OverridingKind override
        const OnConflictExpr* onConflict
        const List* returningList
        const List* groupClause
        bool groupDistinct
        const List* groupingSets
        const Node* havingQual
        const List* windowClause
        const List* distinctClause
        const List* sortClause
        const Node* limitOffset
        const Node* limitCount
        LimitOption limitOption
        const List* rowMarks
        const Node* setOperations
        const List* constraintDeps
        const List* withCheckOptions
        int stmt_location
        int stmt_len

    ctypedef struct TypeName:
        NodeTag type
        const List* names
        bool setof
        bool pct_type
        const List* typmods
        int32_t typemod
        const List* arrayBounds
        int location

    ctypedef struct ColumnRef:
        NodeTag type
        const List* fields
        int location

    ctypedef struct ParamRef:
        NodeTag type
        int number
        int location

    ctypedef struct A_Expr:
        NodeTag type
        A_Expr_Kind kind
        const List* name
        const Node* lexpr
        const Node* rexpr
        int location

    ctypedef struct A_Const:
        NodeTag type
        Value val
        int location

    ctypedef struct TypeCast:
        NodeTag type
        const Node* arg
        const TypeName* typeName
        int location

    ctypedef struct CollateClause:
        NodeTag type
        const Node* arg
        const List* collname
        int location

    ctypedef struct RoleSpec:
        NodeTag type
        RoleSpecType roletype
        const char* rolename
        int location

    ctypedef struct FuncCall:
        NodeTag type
        const List* funcname
        const List* args
        const List* agg_order
        const Node* agg_filter
        const WindowDef* over
        bool agg_within_group
        bool agg_star
        bool agg_distinct
        bool func_variadic
        CoercionForm funcformat
        int location

    ctypedef struct A_Star:
        NodeTag type

    ctypedef struct A_Indices:
        NodeTag type
        bool is_slice
        const Node* lidx
        const Node* uidx

    ctypedef struct A_Indirection:
        NodeTag type
        const Node* arg
        const List* indirection

    ctypedef struct A_ArrayExpr:
        NodeTag type
        const List* elements
        int location

    ctypedef struct ResTarget:
        NodeTag type
        const char* name
        const List* indirection
        const Node* val
        int location

    ctypedef struct MultiAssignRef:
        NodeTag type
        const Node* source
        int colno
        int ncolumns

    ctypedef struct SortBy:
        NodeTag type
        const Node* node
        SortByDir sortby_dir
        SortByNulls sortby_nulls
        const List* useOp
        int location

    ctypedef struct WindowDef:
        NodeTag type
        const char* name
        const char* refname
        const List* partitionClause
        const List* orderClause
        int frameOptions
        const Node* startOffset
        const Node* endOffset
        int location

    ctypedef struct RangeSubselect:
        NodeTag type
        bool lateral
        const Node* subquery
        const Alias* alias

    ctypedef struct RangeFunction:
        NodeTag type
        bool lateral
        bool ordinality
        bool is_rowsfrom
        const List* functions
        const Alias* alias
        const List* coldeflist

    ctypedef struct RangeTableFunc:
        NodeTag type
        bool lateral
        const Node* docexpr
        const Node* rowexpr
        const List* namespaces
        const List* columns
        const Alias* alias
        int location

    ctypedef struct RangeTableFuncCol:
        NodeTag type
        const char* colname
        const TypeName* typeName
        bool for_ordinality
        bool is_not_null
        const Node* colexpr
        const Node* coldefexpr
        int location

    ctypedef struct RangeTableSample:
        NodeTag type
        const Node* relation
        const List* method
        const List* args
        const Node* repeatable
        int location

    ctypedef struct ColumnDef:
        NodeTag type
        const char* colname
        const TypeName* typeName
        const char* compression
        int inhcount
        bool is_local
        bool is_not_null
        bool is_from_type
        char storage
        const Node* raw_default
        const Node* cooked_default
        char identity
        const RangeVar* identitySequence
        char generated
        const CollateClause* collClause
        const List* constraints
        const List* fdwoptions
        int location

    ctypedef struct TableLikeClause:
        NodeTag type
        const RangeVar* relation
        int32_t options

    ctypedef struct IndexElem:
        NodeTag type
        const char* name
        const Node* expr
        const char* indexcolname
        const List* collation
        const List* opclass
        const List* opclassopts
        SortByDir ordering
        SortByNulls nulls_ordering

    ctypedef struct DefElem:
        NodeTag type
        const char* defnamespace
        const char* defname
        const Node* arg
        DefElemAction defaction
        int location

    ctypedef struct LockingClause:
        NodeTag type
        const List* lockedRels
        LockClauseStrength strength
        LockWaitPolicy waitPolicy

    ctypedef struct XmlSerialize:
        NodeTag type
        XmlOptionType xmloption
        const Node* expr
        const TypeName* typeName
        int location

    ctypedef struct PartitionElem:
        NodeTag type
        const char* name
        const Node* expr
        const List* collation
        const List* opclass
        int location

    ctypedef struct PartitionSpec:
        NodeTag type
        const char* strategy
        const List* partParams
        int location

    ctypedef struct PartitionBoundSpec:
        NodeTag type
        char strategy
        bool is_default
        int modulus
        int remainder
        const List* listdatums
        const List* lowerdatums
        const List* upperdatums
        int location

    ctypedef struct PartitionRangeDatum:
        NodeTag type
        PartitionRangeDatumKind kind
        const Node* value
        int location

    ctypedef struct PartitionCmd:
        NodeTag type
        const RangeVar* name
        const PartitionBoundSpec* bound
        bool concurrent

    ctypedef struct RangeTblEntry:
        NodeTag type
        RTEKind rtekind
        char relkind
        int rellockmode
        const TableSampleClause* tablesample
        const Query* subquery
        bool security_barrier
        JoinType jointype
        int joinmergedcols
        const List* joinaliasvars
        const List* joinleftcols
        const List* joinrightcols
        const Alias* join_using_alias
        const List* functions
        bool funcordinality
        const TableFunc* tablefunc
        const List* values_lists
        const char* ctename
        unsigned int ctelevelsup
        bool self_reference
        const List* coltypes
        const List* coltypmods
        const List* colcollations
        const char* enrname
        double enrtuples
        const Alias* alias
        const Alias* eref
        bool lateral
        bool inh
        bool inFromCl
        unsigned int requiredPerms
        const Bitmapset* selectedCols
        const Bitmapset* insertedCols
        const Bitmapset* updatedCols
        const Bitmapset* extraUpdatedCols
        const List* securityQuals

    ctypedef struct RangeTblFunction:
        NodeTag type
        const Node* funcexpr
        int funccolcount
        const List* funccolnames
        const List* funccoltypes
        const List* funccoltypmods
        const List* funccolcollations
        const Bitmapset* funcparams

    ctypedef struct TableSampleClause:
        NodeTag type
        const List* args
        const Expr* repeatable

    ctypedef struct WithCheckOption:
        NodeTag type
        WCOKind kind
        const char* relname
        const char* polname
        const Node* qual
        bool cascaded

    ctypedef struct SortGroupClause:
        NodeTag type
        unsigned int tleSortGroupRef
        bool nulls_first
        bool hashable

    ctypedef struct GroupingSet:
        NodeTag type
        GroupingSetKind kind
        const List* content
        int location

    ctypedef struct WindowClause:
        NodeTag type
        const char* name
        const char* refname
        const List* partitionClause
        const List* orderClause
        int frameOptions
        const Node* startOffset
        const Node* endOffset
        bool inRangeAsc
        bool inRangeNullsFirst
        unsigned int winref
        bool copiedOrder

    ctypedef struct RowMarkClause:
        NodeTag type
        unsigned int rti
        LockClauseStrength strength
        LockWaitPolicy waitPolicy
        bool pushedDown

    ctypedef struct WithClause:
        NodeTag type
        const List* ctes
        bool recursive
        int location

    ctypedef struct InferClause:
        NodeTag type
        const List* indexElems
        const Node* whereClause
        const char* conname
        int location

    ctypedef struct OnConflictClause:
        NodeTag type
        OnConflictAction action
        const InferClause* infer
        const List* targetList
        const Node* whereClause
        int location

    ctypedef struct CTESearchClause:
        NodeTag type
        const List* search_col_list
        bool search_breadth_first
        const char* search_seq_column
        int location

    ctypedef struct CTECycleClause:
        NodeTag type
        const List* cycle_col_list
        const char* cycle_mark_column
        const Node* cycle_mark_value
        const Node* cycle_mark_default
        const char* cycle_path_column
        int location
        int cycle_mark_typmod

    ctypedef struct CommonTableExpr:
        NodeTag type
        const char* ctename
        const List* aliascolnames
        CTEMaterialize ctematerialized
        const Node* ctequery
        const CTESearchClause* search_clause
        const CTECycleClause* cycle_clause
        int location
        bool cterecursive
        int cterefcount
        const List* ctecolnames
        const List* ctecoltypes
        const List* ctecoltypmods
        const List* ctecolcollations

    ctypedef struct TriggerTransition:
        NodeTag type
        const char* name
        bool isNew
        bool isTable

    ctypedef struct RawStmt:
        NodeTag type
        const Node* stmt
        int stmt_location
        int stmt_len

    ctypedef struct InsertStmt:
        NodeTag type
        const RangeVar* relation
        const List* cols
        const Node* selectStmt
        const OnConflictClause* onConflictClause
        const List* returningList
        const WithClause* withClause
        OverridingKind override

    ctypedef struct DeleteStmt:
        NodeTag type
        const RangeVar* relation
        const List* usingClause
        const Node* whereClause
        const List* returningList
        const WithClause* withClause

    ctypedef struct UpdateStmt:
        NodeTag type
        const RangeVar* relation
        const List* targetList
        const Node* whereClause
        const List* fromClause
        const List* returningList
        const WithClause* withClause

    ctypedef struct SelectStmt:
        NodeTag type
        const List* distinctClause
        const IntoClause* intoClause
        const List* targetList
        const List* fromClause
        const Node* whereClause
        const List* groupClause
        bool groupDistinct
        const Node* havingClause
        const List* windowClause
        const List* valuesLists
        const List* sortClause
        const Node* limitOffset
        const Node* limitCount
        LimitOption limitOption
        const List* lockingClause
        const WithClause* withClause
        SetOperation op
        bool all
        const SelectStmt* larg
        const SelectStmt* rarg

    ctypedef struct SetOperationStmt:
        NodeTag type
        SetOperation op
        bool all
        const Node* larg
        const Node* rarg
        const List* colTypes
        const List* colTypmods
        const List* colCollations
        const List* groupClauses

    ctypedef struct ReturnStmt:
        NodeTag type
        const Node* returnval

    ctypedef struct PLAssignStmt:
        NodeTag type
        const char* name
        const List* indirection
        int nnames
        const SelectStmt* val
        int location

    ctypedef struct CreateSchemaStmt:
        NodeTag type
        const char* schemaname
        const RoleSpec* authrole
        const List* schemaElts
        bool if_not_exists

    ctypedef struct AlterTableStmt:
        NodeTag type
        const RangeVar* relation
        const List* cmds
        ObjectType objtype
        bool missing_ok

    ctypedef struct ReplicaIdentityStmt:
        NodeTag type
        char identity_type
        const char* name

    ctypedef struct AlterTableCmd:
        NodeTag type
        AlterTableType subtype
        const char* name
        int16_t num
        const RoleSpec* newowner
        const Node* def_ "def"
        DropBehavior behavior
        bool missing_ok
        bool recurse

    ctypedef struct AlterCollationStmt:
        NodeTag type
        const List* collname

    ctypedef struct AlterDomainStmt:
        NodeTag type
        char subtype
        const List* typeName
        const char* name
        const Node* def_ "def"
        DropBehavior behavior
        bool missing_ok

    ctypedef struct GrantStmt:
        NodeTag type
        bool is_grant
        GrantTargetType targtype
        ObjectType objtype
        const List* objects
        const List* privileges
        const List* grantees
        bool grant_option
        const RoleSpec* grantor
        DropBehavior behavior

    ctypedef struct ObjectWithArgs:
        NodeTag type
        const List* objname
        const List* objargs
        const List* objfuncargs
        bool args_unspecified

    ctypedef struct AccessPriv:
        NodeTag type
        const char* priv_name
        const List* cols

    ctypedef struct GrantRoleStmt:
        NodeTag type
        const List* granted_roles
        const List* grantee_roles
        bool is_grant
        bool admin_opt
        const RoleSpec* grantor
        DropBehavior behavior

    ctypedef struct AlterDefaultPrivilegesStmt:
        NodeTag type
        const List* options
        const GrantStmt* action

    ctypedef struct CopyStmt:
        NodeTag type
        const RangeVar* relation
        const Node* query
        const List* attlist
        bool is_from
        bool is_program
        const char* filename
        const List* options
        const Node* whereClause

    ctypedef struct VariableSetStmt:
        NodeTag type
        VariableSetKind kind
        const char* name
        const List* args
        bool is_local

    ctypedef struct VariableShowStmt:
        NodeTag type
        const char* name

    ctypedef struct CreateStmt:
        NodeTag type
        const RangeVar* relation
        const List* tableElts
        const List* inhRelations
        const PartitionBoundSpec* partbound
        const PartitionSpec* partspec
        const TypeName* ofTypename
        const List* constraints
        const List* options
        OnCommitAction oncommit
        const char* tablespacename
        const char* accessMethod
        bool if_not_exists

    ctypedef struct Constraint:
        NodeTag type
        ConstrType contype
        const char* conname
        bool deferrable
        bool initdeferred
        int location
        bool is_no_inherit
        const Node* raw_expr
        const char* cooked_expr
        char generated_when
        const List* keys
        const List* including
        const List* exclusions
        const List* options
        const char* indexname
        const char* indexspace
        bool reset_default_tblspc
        const char* access_method
        const Node* where_clause
        const RangeVar* pktable
        const List* fk_attrs
        const List* pk_attrs
        char fk_matchtype
        char fk_upd_action
        char fk_del_action
        const List* old_conpfeqop
        bool skip_validation
        bool initially_valid

    ctypedef struct CreateTableSpaceStmt:
        NodeTag type
        const char* tablespacename
        const RoleSpec* owner
        const char* location
        const List* options

    ctypedef struct DropTableSpaceStmt:
        NodeTag type
        const char* tablespacename
        bool missing_ok

    ctypedef struct AlterTableSpaceOptionsStmt:
        NodeTag type
        const char* tablespacename
        const List* options
        bool isReset

    ctypedef struct AlterTableMoveAllStmt:
        NodeTag type
        const char* orig_tablespacename
        ObjectType objtype
        const List* roles
        const char* new_tablespacename
        bool nowait

    ctypedef struct CreateExtensionStmt:
        NodeTag type
        const char* extname
        bool if_not_exists
        const List* options

    ctypedef struct AlterExtensionStmt:
        NodeTag type
        const char* extname
        const List* options

    ctypedef struct AlterExtensionContentsStmt:
        NodeTag type
        const char* extname
        int action
        ObjectType objtype
        const Node* object

    ctypedef struct CreateFdwStmt:
        NodeTag type
        const char* fdwname
        const List* func_options
        const List* options

    ctypedef struct AlterFdwStmt:
        NodeTag type
        const char* fdwname
        const List* func_options
        const List* options

    ctypedef struct CreateForeignServerStmt:
        NodeTag type
        const char* servername
        const char* servertype
        const char* version
        const char* fdwname
        bool if_not_exists
        const List* options

    ctypedef struct AlterForeignServerStmt:
        NodeTag type
        const char* servername
        const char* version
        const List* options
        bool has_version

    ctypedef struct CreateForeignTableStmt:
        CreateStmt base
        const char* servername
        const List* options

    ctypedef struct CreateUserMappingStmt:
        NodeTag type
        const RoleSpec* user
        const char* servername
        bool if_not_exists
        const List* options

    ctypedef struct AlterUserMappingStmt:
        NodeTag type
        const RoleSpec* user
        const char* servername
        const List* options

    ctypedef struct DropUserMappingStmt:
        NodeTag type
        const RoleSpec* user
        const char* servername
        bool missing_ok

    ctypedef struct ImportForeignSchemaStmt:
        NodeTag type
        const char* server_name
        const char* remote_schema
        const char* local_schema
        ImportForeignSchemaType list_type
        const List* table_list
        const List* options

    ctypedef struct CreatePolicyStmt:
        NodeTag type
        const char* policy_name
        const RangeVar* table
        const char* cmd_name
        bool permissive
        const List* roles
        const Node* qual
        const Node* with_check

    ctypedef struct AlterPolicyStmt:
        NodeTag type
        const char* policy_name
        const RangeVar* table
        const List* roles
        const Node* qual
        const Node* with_check

    ctypedef struct CreateAmStmt:
        NodeTag type
        const char* amname
        const List* handler_name
        char amtype

    ctypedef struct CreateTrigStmt:
        NodeTag type
        bool replace
        bool isconstraint
        const char* trigname
        const RangeVar* relation
        const List* funcname
        const List* args
        bool row
        int16_t timing
        int16_t events
        const List* columns
        const Node* whenClause
        const List* transitionRels
        bool deferrable
        bool initdeferred
        const RangeVar* constrrel

    ctypedef struct CreateEventTrigStmt:
        NodeTag type
        const char* trigname
        const char* eventname
        const List* whenclause
        const List* funcname

    ctypedef struct AlterEventTrigStmt:
        NodeTag type
        const char* trigname
        char tgenabled

    ctypedef struct CreatePLangStmt:
        NodeTag type
        bool replace
        const char* plname
        const List* plhandler
        const List* plinline
        const List* plvalidator
        bool pltrusted

    ctypedef struct CreateRoleStmt:
        NodeTag type
        RoleStmtType stmt_type
        const char* role
        const List* options

    ctypedef struct AlterRoleStmt:
        NodeTag type
        const RoleSpec* role
        const List* options
        int action

    ctypedef struct AlterRoleSetStmt:
        NodeTag type
        const RoleSpec* role
        const char* database
        const VariableSetStmt* setstmt

    ctypedef struct DropRoleStmt:
        NodeTag type
        const List* roles
        bool missing_ok

    ctypedef struct CreateSeqStmt:
        NodeTag type
        const RangeVar* sequence
        const List* options
        bool for_identity
        bool if_not_exists

    ctypedef struct AlterSeqStmt:
        NodeTag type
        const RangeVar* sequence
        const List* options
        bool for_identity
        bool missing_ok

    ctypedef struct DefineStmt:
        NodeTag type
        ObjectType kind
        bool oldstyle
        const List* defnames
        const List* args
        const List* definition
        bool if_not_exists
        bool replace

    ctypedef struct CreateDomainStmt:
        NodeTag type
        const List* domainname
        const TypeName* typeName
        const CollateClause* collClause
        const List* constraints

    ctypedef struct CreateOpClassStmt:
        NodeTag type
        const List* opclassname
        const List* opfamilyname
        const char* amname
        const TypeName* datatype
        const List* items
        bool isDefault

    ctypedef struct CreateOpClassItem:
        NodeTag type
        int itemtype
        const ObjectWithArgs* name
        int number
        const List* order_family
        const List* class_args
        const TypeName* storedtype

    ctypedef struct CreateOpFamilyStmt:
        NodeTag type
        const List* opfamilyname
        const char* amname

    ctypedef struct AlterOpFamilyStmt:
        NodeTag type
        const List* opfamilyname
        const char* amname
        bool isDrop
        const List* items

    ctypedef struct DropStmt:
        NodeTag type
        const List* objects
        ObjectType removeType
        DropBehavior behavior
        bool missing_ok
        bool concurrent

    ctypedef struct TruncateStmt:
        NodeTag type
        const List* relations
        bool restart_seqs
        DropBehavior behavior

    ctypedef struct CommentStmt:
        NodeTag type
        ObjectType objtype
        const Node* object
        const char* comment

    ctypedef struct SecLabelStmt:
        NodeTag type
        ObjectType objtype
        const Node* object
        const char* provider
        const char* label

    ctypedef struct DeclareCursorStmt:
        NodeTag type
        const char* portalname
        int options
        const Node* query

    ctypedef struct ClosePortalStmt:
        NodeTag type
        const char* portalname

    ctypedef struct FetchStmt:
        NodeTag type
        FetchDirection direction
        long howMany
        const char* portalname
        bool ismove

    ctypedef struct IndexStmt:
        NodeTag type
        const char* idxname
        const RangeVar* relation
        const char* accessMethod
        const char* tableSpace
        const List* indexParams
        const List* indexIncludingParams
        const List* options
        const Node* whereClause
        const List* excludeOpNames
        const char* idxcomment
        unsigned int oldCreateSubid
        unsigned int oldFirstRelfilenodeSubid
        bool unique
        bool primary
        bool isconstraint
        bool deferrable
        bool initdeferred
        bool transformed
        bool concurrent
        bool if_not_exists
        bool reset_default_tblspc

    ctypedef struct CreateStatsStmt:
        NodeTag type
        const List* defnames
        const List* stat_types
        const List* exprs
        const List* relations
        const char* stxcomment
        bool transformed
        bool if_not_exists

    ctypedef struct StatsElem:
        NodeTag type
        const char* name
        const Node* expr

    ctypedef struct AlterStatsStmt:
        NodeTag type
        const List* defnames
        int stxstattarget
        bool missing_ok

    ctypedef struct CreateFunctionStmt:
        NodeTag type
        bool is_procedure
        bool replace
        const List* funcname
        const List* parameters
        const TypeName* returnType
        const List* options
        const Node* sql_body

    ctypedef struct FunctionParameter:
        NodeTag type
        const char* name
        const TypeName* argType
        FunctionParameterMode mode
        const Node* defexpr

    ctypedef struct AlterFunctionStmt:
        NodeTag type
        ObjectType objtype
        const ObjectWithArgs* func
        const List* actions

    ctypedef struct DoStmt:
        NodeTag type
        const List* args

    ctypedef struct InlineCodeBlock:
        NodeTag type
        const char* source_text
        bool langIsTrusted
        bool atomic

    ctypedef struct CallStmt:
        NodeTag type
        const FuncCall* funccall
        const FuncExpr* funcexpr
        const List* outargs

    ctypedef struct CallContext:
        NodeTag type
        bool atomic

    ctypedef struct RenameStmt:
        NodeTag type
        ObjectType renameType
        ObjectType relationType
        const RangeVar* relation
        const Node* object
        const char* subname
        const char* newname
        DropBehavior behavior
        bool missing_ok

    ctypedef struct AlterObjectDependsStmt:
        NodeTag type
        ObjectType objectType
        const RangeVar* relation
        const Node* object
        const Value* extname
        bool remove

    ctypedef struct AlterObjectSchemaStmt:
        NodeTag type
        ObjectType objectType
        const RangeVar* relation
        const Node* object
        const char* newschema
        bool missing_ok

    ctypedef struct AlterOwnerStmt:
        NodeTag type
        ObjectType objectType
        const RangeVar* relation
        const Node* object
        const RoleSpec* newowner

    ctypedef struct AlterOperatorStmt:
        NodeTag type
        const ObjectWithArgs* opername
        const List* options

    ctypedef struct AlterTypeStmt:
        NodeTag type
        const List* typeName
        const List* options

    ctypedef struct RuleStmt:
        NodeTag type
        const RangeVar* relation
        const char* rulename
        const Node* whereClause
        CmdType event
        bool instead
        const List* actions
        bool replace

    ctypedef struct NotifyStmt:
        NodeTag type
        const char* conditionname
        const char* payload

    ctypedef struct ListenStmt:
        NodeTag type
        const char* conditionname

    ctypedef struct UnlistenStmt:
        NodeTag type
        const char* conditionname

    ctypedef struct TransactionStmt:
        NodeTag type
        TransactionStmtKind kind
        const List* options
        const char* savepoint_name
        const char* gid
        bool chain

    ctypedef struct CompositeTypeStmt:
        NodeTag type
        const RangeVar* typevar
        const List* coldeflist

    ctypedef struct CreateEnumStmt:
        NodeTag type
        const List* typeName
        const List* vals

    ctypedef struct CreateRangeStmt:
        NodeTag type
        const List* typeName
        const List* params

    ctypedef struct AlterEnumStmt:
        NodeTag type
        const List* typeName
        const char* oldVal
        const char* newVal
        const char* newValNeighbor
        bool newValIsAfter
        bool skipIfNewValExists

    ctypedef struct ViewStmt:
        NodeTag type
        const RangeVar* view
        const List* aliases
        const Node* query
        bool replace
        const List* options
        ViewCheckOption withCheckOption

    ctypedef struct LoadStmt:
        NodeTag type
        const char* filename

    ctypedef struct CreatedbStmt:
        NodeTag type
        const char* dbname
        const List* options

    ctypedef struct AlterDatabaseStmt:
        NodeTag type
        const char* dbname
        const List* options

    ctypedef struct AlterDatabaseSetStmt:
        NodeTag type
        const char* dbname
        const VariableSetStmt* setstmt

    ctypedef struct DropdbStmt:
        NodeTag type
        const char* dbname
        bool missing_ok
        const List* options

    ctypedef struct AlterSystemStmt:
        NodeTag type
        const VariableSetStmt* setstmt

    ctypedef struct ClusterStmt:
        NodeTag type
        const RangeVar* relation
        const char* indexname
        const List* params

    ctypedef struct VacuumStmt:
        NodeTag type
        const List* options
        const List* rels
        bool is_vacuumcmd

    ctypedef struct VacuumRelation:
        NodeTag type
        const RangeVar* relation
        const List* va_cols

    ctypedef struct ExplainStmt:
        NodeTag type
        const Node* query
        const List* options

    ctypedef struct CreateTableAsStmt:
        NodeTag type
        const Node* query
        const IntoClause* into
        ObjectType objtype
        bool is_select_into
        bool if_not_exists

    ctypedef struct RefreshMatViewStmt:
        NodeTag type
        bool concurrent
        bool skipData
        const RangeVar* relation

    ctypedef struct CheckPointStmt:
        NodeTag type

    ctypedef struct DiscardStmt:
        NodeTag type
        DiscardMode target

    ctypedef struct LockStmt:
        NodeTag type
        const List* relations
        int mode
        bool nowait

    ctypedef struct ConstraintsSetStmt:
        NodeTag type
        const List* constraints
        bool deferred

    ctypedef struct ReindexStmt:
        NodeTag type
        ReindexObjectType kind
        const RangeVar* relation
        const char* name
        const List* params

    ctypedef struct CreateConversionStmt:
        NodeTag type
        const List* conversion_name
        const char* for_encoding_name
        const char* to_encoding_name
        const List* func_name
        bool def_ "def"

    ctypedef struct CreateCastStmt:
        NodeTag type
        const TypeName* sourcetype
        const TypeName* targettype
        const ObjectWithArgs* func
        CoercionContext context
        bool inout

    ctypedef struct CreateTransformStmt:
        NodeTag type
        bool replace
        const TypeName* type_name
        const char* lang
        const ObjectWithArgs* fromsql
        const ObjectWithArgs* tosql

    ctypedef struct PrepareStmt:
        NodeTag type
        const char* name
        const List* argtypes
        const Node* query

    ctypedef struct ExecuteStmt:
        NodeTag type
        const char* name
        const List* params

    ctypedef struct DeallocateStmt:
        NodeTag type
        const char* name

    ctypedef struct DropOwnedStmt:
        NodeTag type
        const List* roles
        DropBehavior behavior

    ctypedef struct ReassignOwnedStmt:
        NodeTag type
        const List* roles
        const RoleSpec* newrole

    ctypedef struct AlterTSDictionaryStmt:
        NodeTag type
        const List* dictname
        const List* options

    ctypedef struct AlterTSConfigurationStmt:
        NodeTag type
        AlterTSConfigType kind
        const List* cfgname
        const List* tokentype
        const List* dicts
        bool override
        bool replace
        bool missing_ok

    ctypedef struct CreatePublicationStmt:
        NodeTag type
        const char* pubname
        const List* options
        const List* tables
        bool for_all_tables

    ctypedef struct AlterPublicationStmt:
        NodeTag type
        const char* pubname
        const List* options
        const List* tables
        bool for_all_tables
        DefElemAction tableAction

    ctypedef struct CreateSubscriptionStmt:
        NodeTag type
        const char* subname
        const char* conninfo
        const List* publication
        const List* options

    ctypedef struct AlterSubscriptionStmt:
        NodeTag type
        AlterSubscriptionType kind
        const char* subname
        const char* conninfo
        const List* publication
        const List* options

    ctypedef struct DropSubscriptionStmt:
        NodeTag type
        const char* subname
        bool missing_ok
        DropBehavior behavior


cdef extern from "nodes/primnodes.h":
    ctypedef struct Alias:
        NodeTag type
        const char* aliasname
        const List* colnames

    ctypedef struct RangeVar:
        NodeTag type
        const char* catalogname
        const char* schemaname
        const char* relname
        bool inh
        char relpersistence
        const Alias* alias
        int location

    ctypedef struct TableFunc:
        NodeTag type
        const List* ns_uris
        const List* ns_names
        const Node* docexpr
        const Node* rowexpr
        const List* colnames
        const List* coltypes
        const List* coltypmods
        const List* colcollations
        const List* colexprs
        const List* coldefexprs
        const Bitmapset* notnulls
        int ordinalitycol
        int location

    ctypedef struct IntoClause:
        NodeTag type
        const RangeVar* rel
        const List* colNames
        const char* accessMethod
        const List* options
        OnCommitAction onCommit
        const char* tableSpaceName
        const Node* viewQuery
        bool skipData

    ctypedef struct Expr:
        NodeTag type

    ctypedef struct Var:
        unsigned int varno
        int varattno
        int32_t vartypmod
        unsigned int varlevelsup
        unsigned int varnosyn
        int varattnosyn
        int location

    ctypedef struct Param:
        ParamKind paramkind
        int paramid
        int32_t paramtypmod
        int location

    ctypedef struct Aggref:
        const List* aggargtypes
        const List* aggdirectargs
        const List* args
        const List* aggorder
        const List* aggdistinct
        const Expr* aggfilter
        bool aggstar
        bool aggvariadic
        char aggkind
        unsigned int agglevelsup
        AggSplit aggsplit
        int aggno
        int aggtransno
        int location

    ctypedef struct GroupingFunc:
        const List* args
        const List* refs
        const List* cols
        unsigned int agglevelsup
        int location

    ctypedef struct WindowFunc:
        const List* args
        const Expr* aggfilter
        unsigned int winref
        bool winstar
        bool winagg
        int location

    ctypedef struct SubscriptingRef:
        int32_t reftypmod
        const List* refupperindexpr
        const List* reflowerindexpr
        const Expr* refexpr
        const Expr* refassgnexpr

    ctypedef struct FuncExpr:
        bool funcretset
        bool funcvariadic
        CoercionForm funcformat
        const List* args
        int location

    ctypedef struct NamedArgExpr:
        const Expr* arg
        const char* name
        int argnumber
        int location

    ctypedef struct OpExpr:
        bool opretset
        const List* args
        int location

    ctypedef struct ScalarArrayOpExpr:
        bool useOr
        const List* args
        int location

    ctypedef struct BoolExpr:
        BoolExprType boolop
        const List* args
        int location

    ctypedef struct SubLink:
        SubLinkType subLinkType
        int subLinkId
        const Node* testexpr
        const List* operName
        const Node* subselect
        int location

    ctypedef struct SubPlan:
        SubLinkType subLinkType
        const Node* testexpr
        const List* paramIds
        int plan_id
        const char* plan_name
        int32_t firstColTypmod
        bool useHashTable
        bool unknownEqFalse
        bool parallel_safe
        const List* setParam
        const List* parParam
        const List* args
        float startup_cost
        float per_call_cost

    ctypedef struct AlternativeSubPlan:
        const List* subplans

    ctypedef struct FieldSelect:
        const Expr* arg
        int fieldnum
        int32_t resulttypmod

    ctypedef struct FieldStore:
        const Expr* arg
        const List* newvals
        const List* fieldnums

    ctypedef struct RelabelType:
        const Expr* arg
        int32_t resulttypmod
        CoercionForm relabelformat
        int location

    ctypedef struct CoerceViaIO:
        const Expr* arg
        CoercionForm coerceformat
        int location

    ctypedef struct ArrayCoerceExpr:
        const Expr* arg
        const Expr* elemexpr
        int32_t resulttypmod
        CoercionForm coerceformat
        int location

    ctypedef struct ConvertRowtypeExpr:
        const Expr* arg
        CoercionForm convertformat
        int location

    ctypedef struct CollateExpr:
        const Expr* arg
        int location

    ctypedef struct CaseExpr:
        const Expr* arg
        const List* args
        const Expr* defresult
        int location

    ctypedef struct CaseWhen:
        const Expr* expr
        const Expr* result
        int location

    ctypedef struct CaseTestExpr:
        int32_t typeMod

    ctypedef struct ArrayExpr:
        const List* elements
        bool multidims
        int location

    ctypedef struct RowExpr:
        const List* args
        CoercionForm row_format
        const List* colnames
        int location

    ctypedef struct RowCompareExpr:
        RowCompareType rctype
        const List* opnos
        const List* opfamilies
        const List* inputcollids
        const List* largs
        const List* rargs

    ctypedef struct CoalesceExpr:
        const List* args
        int location

    ctypedef struct MinMaxExpr:
        MinMaxOp op
        const List* args
        int location

    ctypedef struct SQLValueFunction:
        SQLValueFunctionOp op
        int32_t typmod
        int location

    ctypedef struct XmlExpr:
        XmlExprOp op
        const char* name
        const List* named_args
        const List* arg_names
        const List* args
        XmlOptionType xmloption
        int32_t typmod
        int location

    ctypedef struct NullTest:
        const Expr* arg
        NullTestType nulltesttype
        bool argisrow
        int location

    ctypedef struct BooleanTest:
        const Expr* arg
        BoolTestType booltesttype
        int location

    ctypedef struct CoerceToDomain:
        const Expr* arg
        int32_t resulttypmod
        CoercionForm coercionformat
        int location

    ctypedef struct CoerceToDomainValue:
        int32_t typeMod
        int location

    ctypedef struct SetToDefault:
        int32_t typeMod
        int location

    ctypedef struct CurrentOfExpr:
        unsigned int cvarno
        const char* cursor_name
        int cursor_param

    ctypedef struct InferenceElem:
        const Node* expr

    ctypedef struct TargetEntry:
        const Expr* expr
        int resno
        const char* resname
        unsigned int ressortgroupref
        int resorigcol
        bool resjunk

    ctypedef struct RangeTblRef:
        NodeTag type
        int rtindex

    ctypedef struct JoinExpr:
        NodeTag type
        JoinType jointype
        bool isNatural
        const Node* larg
        const Node* rarg
        const List* usingClause
        const Alias* join_using_alias
        const Node* quals
        const Alias* alias
        int rtindex

    ctypedef struct FromExpr:
        NodeTag type
        const List* fromlist
        const Node* quals

    ctypedef struct OnConflictExpr:
        NodeTag type
        OnConflictAction action
        const List* arbiterElems
        const Node* arbiterWhere
        const List* onConflictSet
        const Node* onConflictWhere
        int exclRelIndex
        const List* exclRelTlist
