.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2019 Lele Gaifax
..

====================================================================
 :mod:`pglast.enums.nodes` --- Constants extracted from `nodes.h`__
====================================================================

__ https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h

.. module:: pglast.enums.nodes
   :synopsis: Constants extracted from nodes.h


.. class:: pglast.enums.nodes.AggSplit

   Corresponds to the `AggSplit enum <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L757>`__.

   .. data:: AGGSPLIT_SIMPLE

   .. data:: AGGSPLIT_INITIAL_SERIAL

   .. data:: AGGSPLIT_FINAL_DESERIAL


.. class:: pglast.enums.nodes.AggStrategy

   Corresponds to the `AggStrategy enum <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L735>`__.

   .. data:: AGG_PLAIN

   .. data:: AGG_SORTED

   .. data:: AGG_HASHED

   .. data:: AGG_MIXED


.. class:: pglast.enums.nodes.CmdType

   Corresponds to the `CmdType enum <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L649>`__.

   .. data:: CMD_UNKNOWN

   .. data:: CMD_SELECT

   .. data:: CMD_UPDATE

   .. data:: CMD_INSERT

   .. data:: CMD_DELETE

   .. data:: CMD_UTILITY

   .. data:: CMD_NOTHING


.. class:: pglast.enums.nodes.JoinType

   Corresponds to the `JoinType enum <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L673>`__.

   .. data:: JOIN_INNER

   .. data:: JOIN_LEFT

   .. data:: JOIN_FULL

   .. data:: JOIN_RIGHT

   .. data:: JOIN_SEMI

   .. data:: JOIN_ANTI

   .. data:: JOIN_UNIQUE_OUTER

   .. data:: JOIN_UNIQUE_INNER


.. class:: pglast.enums.nodes.NodeTag

   Corresponds to the `NodeTag enum <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L26>`__.

   .. data:: T_Invalid

   .. data:: T_IndexInfo

   .. data:: T_ExprContext

   .. data:: T_ProjectionInfo

   .. data:: T_JunkFilter

   .. data:: T_ResultRelInfo

   .. data:: T_EState

   .. data:: T_TupleTableSlot

   .. data:: T_Plan

   .. data:: T_Result

   .. data:: T_ProjectSet

   .. data:: T_ModifyTable

   .. data:: T_Append

   .. data:: T_MergeAppend

   .. data:: T_RecursiveUnion

   .. data:: T_BitmapAnd

   .. data:: T_BitmapOr

   .. data:: T_Scan

   .. data:: T_SeqScan

   .. data:: T_SampleScan

   .. data:: T_IndexScan

   .. data:: T_IndexOnlyScan

   .. data:: T_BitmapIndexScan

   .. data:: T_BitmapHeapScan

   .. data:: T_TidScan

   .. data:: T_SubqueryScan

   .. data:: T_FunctionScan

   .. data:: T_ValuesScan

   .. data:: T_TableFuncScan

   .. data:: T_CteScan

   .. data:: T_NamedTuplestoreScan

   .. data:: T_WorkTableScan

   .. data:: T_ForeignScan

   .. data:: T_CustomScan

   .. data:: T_Join

   .. data:: T_NestLoop

   .. data:: T_MergeJoin

   .. data:: T_HashJoin

   .. data:: T_Material

   .. data:: T_Sort

   .. data:: T_Group

   .. data:: T_Agg

   .. data:: T_WindowAgg

   .. data:: T_Unique

   .. data:: T_Gather

   .. data:: T_GatherMerge

   .. data:: T_Hash

   .. data:: T_SetOp

   .. data:: T_LockRows

   .. data:: T_Limit

   .. data:: T_NestLoopParam

   .. data:: T_PlanRowMark

   .. data:: T_PlanInvalItem

   .. data:: T_PlanState

   .. data:: T_ResultState

   .. data:: T_ProjectSetState

   .. data:: T_ModifyTableState

   .. data:: T_AppendState

   .. data:: T_MergeAppendState

   .. data:: T_RecursiveUnionState

   .. data:: T_BitmapAndState

   .. data:: T_BitmapOrState

   .. data:: T_ScanState

   .. data:: T_SeqScanState

   .. data:: T_SampleScanState

   .. data:: T_IndexScanState

   .. data:: T_IndexOnlyScanState

   .. data:: T_BitmapIndexScanState

   .. data:: T_BitmapHeapScanState

   .. data:: T_TidScanState

   .. data:: T_SubqueryScanState

   .. data:: T_FunctionScanState

   .. data:: T_TableFuncScanState

   .. data:: T_ValuesScanState

   .. data:: T_CteScanState

   .. data:: T_NamedTuplestoreScanState

   .. data:: T_WorkTableScanState

   .. data:: T_ForeignScanState

   .. data:: T_CustomScanState

   .. data:: T_JoinState

   .. data:: T_NestLoopState

   .. data:: T_MergeJoinState

   .. data:: T_HashJoinState

   .. data:: T_MaterialState

   .. data:: T_SortState

   .. data:: T_GroupState

   .. data:: T_AggState

   .. data:: T_WindowAggState

   .. data:: T_UniqueState

   .. data:: T_GatherState

   .. data:: T_GatherMergeState

   .. data:: T_HashState

   .. data:: T_SetOpState

   .. data:: T_LockRowsState

   .. data:: T_LimitState

   .. data:: T_Alias

   .. data:: T_RangeVar

   .. data:: T_TableFunc

   .. data:: T_Expr

   .. data:: T_Var

   .. data:: T_Const

   .. data:: T_Param

   .. data:: T_Aggref

   .. data:: T_GroupingFunc

   .. data:: T_WindowFunc

   .. data:: T_ArrayRef

   .. data:: T_FuncExpr

   .. data:: T_NamedArgExpr

   .. data:: T_OpExpr

   .. data:: T_DistinctExpr

   .. data:: T_NullIfExpr

   .. data:: T_ScalarArrayOpExpr

   .. data:: T_BoolExpr

   .. data:: T_SubLink

   .. data:: T_SubPlan

   .. data:: T_AlternativeSubPlan

   .. data:: T_FieldSelect

   .. data:: T_FieldStore

   .. data:: T_RelabelType

   .. data:: T_CoerceViaIO

   .. data:: T_ArrayCoerceExpr

   .. data:: T_ConvertRowtypeExpr

   .. data:: T_CollateExpr

   .. data:: T_CaseExpr

   .. data:: T_CaseWhen

   .. data:: T_CaseTestExpr

   .. data:: T_ArrayExpr

   .. data:: T_RowExpr

   .. data:: T_RowCompareExpr

   .. data:: T_CoalesceExpr

   .. data:: T_MinMaxExpr

   .. data:: T_SQLValueFunction

   .. data:: T_XmlExpr

   .. data:: T_NullTest

   .. data:: T_BooleanTest

   .. data:: T_CoerceToDomain

   .. data:: T_CoerceToDomainValue

   .. data:: T_SetToDefault

   .. data:: T_CurrentOfExpr

   .. data:: T_NextValueExpr

   .. data:: T_InferenceElem

   .. data:: T_TargetEntry

   .. data:: T_RangeTblRef

   .. data:: T_JoinExpr

   .. data:: T_FromExpr

   .. data:: T_OnConflictExpr

   .. data:: T_IntoClause

   .. data:: T_ExprState

   .. data:: T_AggrefExprState

   .. data:: T_WindowFuncExprState

   .. data:: T_SetExprState

   .. data:: T_SubPlanState

   .. data:: T_AlternativeSubPlanState

   .. data:: T_DomainConstraintState

   .. data:: T_PlannerInfo

   .. data:: T_PlannerGlobal

   .. data:: T_RelOptInfo

   .. data:: T_IndexOptInfo

   .. data:: T_ForeignKeyOptInfo

   .. data:: T_ParamPathInfo

   .. data:: T_Path

   .. data:: T_IndexPath

   .. data:: T_BitmapHeapPath

   .. data:: T_BitmapAndPath

   .. data:: T_BitmapOrPath

   .. data:: T_TidPath

   .. data:: T_SubqueryScanPath

   .. data:: T_ForeignPath

   .. data:: T_CustomPath

   .. data:: T_NestPath

   .. data:: T_MergePath

   .. data:: T_HashPath

   .. data:: T_AppendPath

   .. data:: T_MergeAppendPath

   .. data:: T_ResultPath

   .. data:: T_MaterialPath

   .. data:: T_UniquePath

   .. data:: T_GatherPath

   .. data:: T_GatherMergePath

   .. data:: T_ProjectionPath

   .. data:: T_ProjectSetPath

   .. data:: T_SortPath

   .. data:: T_GroupPath

   .. data:: T_UpperUniquePath

   .. data:: T_AggPath

   .. data:: T_GroupingSetsPath

   .. data:: T_MinMaxAggPath

   .. data:: T_WindowAggPath

   .. data:: T_SetOpPath

   .. data:: T_RecursiveUnionPath

   .. data:: T_LockRowsPath

   .. data:: T_ModifyTablePath

   .. data:: T_LimitPath

   .. data:: T_EquivalenceClass

   .. data:: T_EquivalenceMember

   .. data:: T_PathKey

   .. data:: T_PathTarget

   .. data:: T_RestrictInfo

   .. data:: T_PlaceHolderVar

   .. data:: T_SpecialJoinInfo

   .. data:: T_AppendRelInfo

   .. data:: T_PartitionedChildRelInfo

   .. data:: T_PlaceHolderInfo

   .. data:: T_MinMaxAggInfo

   .. data:: T_PlannerParamItem

   .. data:: T_RollupData

   .. data:: T_GroupingSetData

   .. data:: T_StatisticExtInfo

   .. data:: T_MemoryContext

   .. data:: T_AllocSetContext

   .. data:: T_SlabContext

   .. data:: T_Value

   .. data:: T_Integer

   .. data:: T_Float

   .. data:: T_String

   .. data:: T_BitString

   .. data:: T_Null

   .. data:: T_List

   .. data:: T_IntList

   .. data:: T_OidList

   .. data:: T_ExtensibleNode

   .. data:: T_RawStmt

   .. data:: T_Query

   .. data:: T_PlannedStmt

   .. data:: T_InsertStmt

   .. data:: T_DeleteStmt

   .. data:: T_UpdateStmt

   .. data:: T_SelectStmt

   .. data:: T_AlterTableStmt

   .. data:: T_AlterTableCmd

   .. data:: T_AlterDomainStmt

   .. data:: T_SetOperationStmt

   .. data:: T_GrantStmt

   .. data:: T_GrantRoleStmt

   .. data:: T_AlterDefaultPrivilegesStmt

   .. data:: T_ClosePortalStmt

   .. data:: T_ClusterStmt

   .. data:: T_CopyStmt

   .. data:: T_CreateStmt

   .. data:: T_DefineStmt

   .. data:: T_DropStmt

   .. data:: T_TruncateStmt

   .. data:: T_CommentStmt

   .. data:: T_FetchStmt

   .. data:: T_IndexStmt

   .. data:: T_CreateFunctionStmt

   .. data:: T_AlterFunctionStmt

   .. data:: T_DoStmt

   .. data:: T_RenameStmt

   .. data:: T_RuleStmt

   .. data:: T_NotifyStmt

   .. data:: T_ListenStmt

   .. data:: T_UnlistenStmt

   .. data:: T_TransactionStmt

   .. data:: T_ViewStmt

   .. data:: T_LoadStmt

   .. data:: T_CreateDomainStmt

   .. data:: T_CreatedbStmt

   .. data:: T_DropdbStmt

   .. data:: T_VacuumStmt

   .. data:: T_ExplainStmt

   .. data:: T_CreateTableAsStmt

   .. data:: T_CreateSeqStmt

   .. data:: T_AlterSeqStmt

   .. data:: T_VariableSetStmt

   .. data:: T_VariableShowStmt

   .. data:: T_DiscardStmt

   .. data:: T_CreateTrigStmt

   .. data:: T_CreatePLangStmt

   .. data:: T_CreateRoleStmt

   .. data:: T_AlterRoleStmt

   .. data:: T_DropRoleStmt

   .. data:: T_LockStmt

   .. data:: T_ConstraintsSetStmt

   .. data:: T_ReindexStmt

   .. data:: T_CheckPointStmt

   .. data:: T_CreateSchemaStmt

   .. data:: T_AlterDatabaseStmt

   .. data:: T_AlterDatabaseSetStmt

   .. data:: T_AlterRoleSetStmt

   .. data:: T_CreateConversionStmt

   .. data:: T_CreateCastStmt

   .. data:: T_CreateOpClassStmt

   .. data:: T_CreateOpFamilyStmt

   .. data:: T_AlterOpFamilyStmt

   .. data:: T_PrepareStmt

   .. data:: T_ExecuteStmt

   .. data:: T_DeallocateStmt

   .. data:: T_DeclareCursorStmt

   .. data:: T_CreateTableSpaceStmt

   .. data:: T_DropTableSpaceStmt

   .. data:: T_AlterObjectDependsStmt

   .. data:: T_AlterObjectSchemaStmt

   .. data:: T_AlterOwnerStmt

   .. data:: T_AlterOperatorStmt

   .. data:: T_DropOwnedStmt

   .. data:: T_ReassignOwnedStmt

   .. data:: T_CompositeTypeStmt

   .. data:: T_CreateEnumStmt

   .. data:: T_CreateRangeStmt

   .. data:: T_AlterEnumStmt

   .. data:: T_AlterTSDictionaryStmt

   .. data:: T_AlterTSConfigurationStmt

   .. data:: T_CreateFdwStmt

   .. data:: T_AlterFdwStmt

   .. data:: T_CreateForeignServerStmt

   .. data:: T_AlterForeignServerStmt

   .. data:: T_CreateUserMappingStmt

   .. data:: T_AlterUserMappingStmt

   .. data:: T_DropUserMappingStmt

   .. data:: T_AlterTableSpaceOptionsStmt

   .. data:: T_AlterTableMoveAllStmt

   .. data:: T_SecLabelStmt

   .. data:: T_CreateForeignTableStmt

   .. data:: T_ImportForeignSchemaStmt

   .. data:: T_CreateExtensionStmt

   .. data:: T_AlterExtensionStmt

   .. data:: T_AlterExtensionContentsStmt

   .. data:: T_CreateEventTrigStmt

   .. data:: T_AlterEventTrigStmt

   .. data:: T_RefreshMatViewStmt

   .. data:: T_ReplicaIdentityStmt

   .. data:: T_AlterSystemStmt

   .. data:: T_CreatePolicyStmt

   .. data:: T_AlterPolicyStmt

   .. data:: T_CreateTransformStmt

   .. data:: T_CreateAmStmt

   .. data:: T_CreatePublicationStmt

   .. data:: T_AlterPublicationStmt

   .. data:: T_CreateSubscriptionStmt

   .. data:: T_AlterSubscriptionStmt

   .. data:: T_DropSubscriptionStmt

   .. data:: T_CreateStatsStmt

   .. data:: T_AlterCollationStmt

   .. data:: T_A_Expr

   .. data:: T_ColumnRef

   .. data:: T_ParamRef

   .. data:: T_A_Const

   .. data:: T_FuncCall

   .. data:: T_A_Star

   .. data:: T_A_Indices

   .. data:: T_A_Indirection

   .. data:: T_A_ArrayExpr

   .. data:: T_ResTarget

   .. data:: T_MultiAssignRef

   .. data:: T_TypeCast

   .. data:: T_CollateClause

   .. data:: T_SortBy

   .. data:: T_WindowDef

   .. data:: T_RangeSubselect

   .. data:: T_RangeFunction

   .. data:: T_RangeTableSample

   .. data:: T_RangeTableFunc

   .. data:: T_RangeTableFuncCol

   .. data:: T_TypeName

   .. data:: T_ColumnDef

   .. data:: T_IndexElem

   .. data:: T_Constraint

   .. data:: T_DefElem

   .. data:: T_RangeTblEntry

   .. data:: T_RangeTblFunction

   .. data:: T_TableSampleClause

   .. data:: T_WithCheckOption

   .. data:: T_SortGroupClause

   .. data:: T_GroupingSet

   .. data:: T_WindowClause

   .. data:: T_ObjectWithArgs

   .. data:: T_AccessPriv

   .. data:: T_CreateOpClassItem

   .. data:: T_TableLikeClause

   .. data:: T_FunctionParameter

   .. data:: T_LockingClause

   .. data:: T_RowMarkClause

   .. data:: T_XmlSerialize

   .. data:: T_WithClause

   .. data:: T_InferClause

   .. data:: T_OnConflictClause

   .. data:: T_CommonTableExpr

   .. data:: T_RoleSpec

   .. data:: T_TriggerTransition

   .. data:: T_PartitionElem

   .. data:: T_PartitionSpec

   .. data:: T_PartitionBoundSpec

   .. data:: T_PartitionRangeDatum

   .. data:: T_PartitionCmd

   .. data:: T_IdentifySystemCmd

   .. data:: T_BaseBackupCmd

   .. data:: T_CreateReplicationSlotCmd

   .. data:: T_DropReplicationSlotCmd

   .. data:: T_StartReplicationCmd

   .. data:: T_TimeLineHistoryCmd

   .. data:: T_SQLCmd

   .. data:: T_TriggerData

   .. data:: T_EventTriggerData

   .. data:: T_ReturnSetInfo

   .. data:: T_WindowObjectData

   .. data:: T_TIDBitmap

   .. data:: T_InlineCodeBlock

   .. data:: T_FdwRoutine

   .. data:: T_IndexAmRoutine

   .. data:: T_TsmRoutine

   .. data:: T_ForeignKeyCacheInfo


.. class:: pglast.enums.nodes.OnConflictAction

   Corresponds to the `OnConflictAction enum <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L799>`__.

   .. data:: ONCONFLICT_NONE

   .. data:: ONCONFLICT_NOTHING

   .. data:: ONCONFLICT_UPDATE


.. class:: pglast.enums.nodes.SetOpCmd

   Corresponds to the `SetOpCmd enum <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L779>`__.

   .. data:: SETOPCMD_INTERSECT

   .. data:: SETOPCMD_INTERSECT_ALL

   .. data:: SETOPCMD_EXCEPT

   .. data:: SETOPCMD_EXCEPT_ALL


.. class:: pglast.enums.nodes.SetOpStrategy

   Corresponds to the `SetOpStrategy enum <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L787>`__.

   .. data:: SETOP_SORTED

   .. data:: SETOP_HASHED


.. data:: AGGSPLITOP_COMBINE

   See `here for details <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L751>`__.

.. data:: AGGSPLITOP_SKIPFINAL

   See `here for details <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L752>`__.

.. data:: AGGSPLITOP_SERIALIZE

   See `here for details <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L753>`__.

.. data:: AGGSPLITOP_DESERIALIZE

   See `here for details <https://github.com/lfittl/libpg_query/blob/d710cb0/src/postgres/include/nodes/nodes.h#L754>`__.
