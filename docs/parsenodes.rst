.. -*- coding: utf-8 -*-
.. :Project:   pglast — DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2025 Lele Gaifax
..

==============================================================================
 :mod:`pglast.enums.parsenodes` --- Constants extracted from `parsenodes.h`__
==============================================================================

__ https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h

.. module:: pglast.enums.parsenodes
   :synopsis: Constants extracted from parsenodes.h


.. class:: pglast.enums.parsenodes.A_Expr_Kind

   Corresponds to the `A_Expr_Kind enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L311>`__.

   .. data:: AEXPR_OP

   .. data:: AEXPR_OP_ANY

   .. data:: AEXPR_OP_ALL

   .. data:: AEXPR_DISTINCT

   .. data:: AEXPR_NOT_DISTINCT

   .. data:: AEXPR_NULLIF

   .. data:: AEXPR_IN

   .. data:: AEXPR_LIKE

   .. data:: AEXPR_ILIKE

   .. data:: AEXPR_SIMILAR

   .. data:: AEXPR_BETWEEN

   .. data:: AEXPR_NOT_BETWEEN

   .. data:: AEXPR_BETWEEN_SYM

   .. data:: AEXPR_NOT_BETWEEN_SYM


.. class:: pglast.enums.parsenodes.AlterPublicationAction

   Corresponds to the `AlterPublicationAction enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L4169>`__.

   .. data:: AP_AddObjects

   .. data:: AP_DropObjects

   .. data:: AP_SetObjects


.. class:: pglast.enums.parsenodes.AlterSubscriptionType

   Corresponds to the `AlterSubscriptionType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L4203>`__.

   .. data:: ALTER_SUBSCRIPTION_OPTIONS

   .. data:: ALTER_SUBSCRIPTION_CONNECTION

   .. data:: ALTER_SUBSCRIPTION_SET_PUBLICATION

   .. data:: ALTER_SUBSCRIPTION_ADD_PUBLICATION

   .. data:: ALTER_SUBSCRIPTION_DROP_PUBLICATION

   .. data:: ALTER_SUBSCRIPTION_REFRESH

   .. data:: ALTER_SUBSCRIPTION_ENABLED

   .. data:: ALTER_SUBSCRIPTION_SKIP


.. class:: pglast.enums.parsenodes.AlterTSConfigType

   Corresponds to the `AlterTSConfigType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L4105>`__.

   .. data:: ALTER_TSCONFIG_ADD_MAPPING

   .. data:: ALTER_TSCONFIG_ALTER_MAPPING_FOR_TOKEN

   .. data:: ALTER_TSCONFIG_REPLACE_DICT

   .. data:: ALTER_TSCONFIG_REPLACE_DICT_FOR_TOKEN

   .. data:: ALTER_TSCONFIG_DROP_MAPPING


.. class:: pglast.enums.parsenodes.AlterTableType

   Corresponds to the `AlterTableType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2348>`__.

   .. data:: AT_AddColumn

   .. data:: AT_AddColumnToView

   .. data:: AT_ColumnDefault

   .. data:: AT_CookedColumnDefault

   .. data:: AT_DropNotNull

   .. data:: AT_SetNotNull

   .. data:: AT_SetExpression

   .. data:: AT_DropExpression

   .. data:: AT_CheckNotNull

   .. data:: AT_SetStatistics

   .. data:: AT_SetOptions

   .. data:: AT_ResetOptions

   .. data:: AT_SetStorage

   .. data:: AT_SetCompression

   .. data:: AT_DropColumn

   .. data:: AT_AddIndex

   .. data:: AT_ReAddIndex

   .. data:: AT_AddConstraint

   .. data:: AT_ReAddConstraint

   .. data:: AT_ReAddDomainConstraint

   .. data:: AT_AlterConstraint

   .. data:: AT_ValidateConstraint

   .. data:: AT_AddIndexConstraint

   .. data:: AT_DropConstraint

   .. data:: AT_ReAddComment

   .. data:: AT_AlterColumnType

   .. data:: AT_AlterColumnGenericOptions

   .. data:: AT_ChangeOwner

   .. data:: AT_ClusterOn

   .. data:: AT_DropCluster

   .. data:: AT_SetLogged

   .. data:: AT_SetUnLogged

   .. data:: AT_DropOids

   .. data:: AT_SetAccessMethod

   .. data:: AT_SetTableSpace

   .. data:: AT_SetRelOptions

   .. data:: AT_ResetRelOptions

   .. data:: AT_ReplaceRelOptions

   .. data:: AT_EnableTrig

   .. data:: AT_EnableAlwaysTrig

   .. data:: AT_EnableReplicaTrig

   .. data:: AT_DisableTrig

   .. data:: AT_EnableTrigAll

   .. data:: AT_DisableTrigAll

   .. data:: AT_EnableTrigUser

   .. data:: AT_DisableTrigUser

   .. data:: AT_EnableRule

   .. data:: AT_EnableAlwaysRule

   .. data:: AT_EnableReplicaRule

   .. data:: AT_DisableRule

   .. data:: AT_AddInherit

   .. data:: AT_DropInherit

   .. data:: AT_AddOf

   .. data:: AT_DropOf

   .. data:: AT_ReplicaIdentity

   .. data:: AT_EnableRowSecurity

   .. data:: AT_DisableRowSecurity

   .. data:: AT_ForceRowSecurity

   .. data:: AT_NoForceRowSecurity

   .. data:: AT_GenericOptions

   .. data:: AT_AttachPartition

   .. data:: AT_DetachPartition

   .. data:: AT_DetachPartitionFinalize

   .. data:: AT_AddIdentity

   .. data:: AT_SetIdentity

   .. data:: AT_DropIdentity

   .. data:: AT_ReAddStatistics


.. class:: pglast.enums.parsenodes.CTEMaterialize

   Corresponds to the `CTEMaterialize enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L1636>`__.

   .. data:: CTEMaterializeDefault

   .. data:: CTEMaterializeAlways

   .. data:: CTEMaterializeNever


.. class:: pglast.enums.parsenodes.ConstrType

   Corresponds to the `ConstrType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2697>`__.

   .. data:: CONSTR_NULL

   .. data:: CONSTR_NOTNULL

   .. data:: CONSTR_DEFAULT

   .. data:: CONSTR_IDENTITY

   .. data:: CONSTR_GENERATED

   .. data:: CONSTR_CHECK

   .. data:: CONSTR_PRIMARY

   .. data:: CONSTR_UNIQUE

   .. data:: CONSTR_EXCLUSION

   .. data:: CONSTR_FOREIGN

   .. data:: CONSTR_ATTR_DEFERRABLE

   .. data:: CONSTR_ATTR_NOT_DEFERRABLE

   .. data:: CONSTR_ATTR_DEFERRED

   .. data:: CONSTR_ATTR_IMMEDIATE


.. class:: pglast.enums.parsenodes.DefElemAction

   Corresponds to the `DefElemAction enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L803>`__.

   .. data:: DEFELEM_UNSPEC

   .. data:: DEFELEM_SET

   .. data:: DEFELEM_ADD

   .. data:: DEFELEM_DROP


.. class:: pglast.enums.parsenodes.DiscardMode

   Corresponds to the `DiscardMode enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3924>`__.

   .. data:: DISCARD_ALL

   .. data:: DISCARD_PLANS

   .. data:: DISCARD_SEQUENCES

   .. data:: DISCARD_TEMP


.. class:: pglast.enums.parsenodes.DropBehavior

   Corresponds to the `DropBehavior enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2329>`__.

   .. data:: DROP_RESTRICT

   .. data:: DROP_CASCADE


.. class:: pglast.enums.parsenodes.FetchDirection

   Corresponds to the `FetchDirection enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3316>`__.

   .. data:: FETCH_FORWARD

   .. data:: FETCH_BACKWARD

   .. data:: FETCH_ABSOLUTE

   .. data:: FETCH_RELATIVE


.. class:: pglast.enums.parsenodes.FunctionParameterMode

   Corresponds to the `FunctionParameterMode enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3439>`__.

   .. data:: FUNC_PARAM_IN

   .. data:: FUNC_PARAM_OUT

   .. data:: FUNC_PARAM_INOUT

   .. data:: FUNC_PARAM_VARIADIC

   .. data:: FUNC_PARAM_TABLE

   .. data:: FUNC_PARAM_DEFAULT


.. class:: pglast.enums.parsenodes.GrantTargetType

   Corresponds to the `GrantTargetType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2484>`__.

   .. data:: ACL_TARGET_OBJECT

   .. data:: ACL_TARGET_ALL_IN_SCHEMA

   .. data:: ACL_TARGET_DEFAULTS


.. class:: pglast.enums.parsenodes.GroupingSetKind

   Corresponds to the `GroupingSetKind enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L1497>`__.

   .. data:: GROUPING_SET_EMPTY

   .. data:: GROUPING_SET_SIMPLE

   .. data:: GROUPING_SET_ROLLUP

   .. data:: GROUPING_SET_CUBE

   .. data:: GROUPING_SET_SETS


.. class:: pglast.enums.parsenodes.ImportForeignSchemaType

   Corresponds to the `ImportForeignSchemaType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2937>`__.

   .. data:: FDW_IMPORT_SCHEMA_ALL

   .. data:: FDW_IMPORT_SCHEMA_LIMIT_TO

   .. data:: FDW_IMPORT_SCHEMA_EXCEPT


.. class:: pglast.enums.parsenodes.JsonQuotes

   Corresponds to the `JsonQuotes enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L1773>`__.

   .. data:: JS_QUOTES_UNSPEC

   .. data:: JS_QUOTES_KEEP

   .. data:: JS_QUOTES_OMIT


.. class:: pglast.enums.parsenodes.JsonTableColumnType

   Corresponds to the `JsonTableColumnType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L1838>`__.

   .. data:: JTC_FOR_ORDINALITY

   .. data:: JTC_REGULAR

   .. data:: JTC_EXISTS

   .. data:: JTC_FORMATTED

   .. data:: JTC_NESTED


.. class:: pglast.enums.parsenodes.ObjectType

   Corresponds to the `ObjectType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2256>`__.

   .. data:: OBJECT_ACCESS_METHOD

   .. data:: OBJECT_AGGREGATE

   .. data:: OBJECT_AMOP

   .. data:: OBJECT_AMPROC

   .. data:: OBJECT_ATTRIBUTE

   .. data:: OBJECT_CAST

   .. data:: OBJECT_COLUMN

   .. data:: OBJECT_COLLATION

   .. data:: OBJECT_CONVERSION

   .. data:: OBJECT_DATABASE

   .. data:: OBJECT_DEFAULT

   .. data:: OBJECT_DEFACL

   .. data:: OBJECT_DOMAIN

   .. data:: OBJECT_DOMCONSTRAINT

   .. data:: OBJECT_EVENT_TRIGGER

   .. data:: OBJECT_EXTENSION

   .. data:: OBJECT_FDW

   .. data:: OBJECT_FOREIGN_SERVER

   .. data:: OBJECT_FOREIGN_TABLE

   .. data:: OBJECT_FUNCTION

   .. data:: OBJECT_INDEX

   .. data:: OBJECT_LANGUAGE

   .. data:: OBJECT_LARGEOBJECT

   .. data:: OBJECT_MATVIEW

   .. data:: OBJECT_OPCLASS

   .. data:: OBJECT_OPERATOR

   .. data:: OBJECT_OPFAMILY

   .. data:: OBJECT_PARAMETER_ACL

   .. data:: OBJECT_POLICY

   .. data:: OBJECT_PROCEDURE

   .. data:: OBJECT_PUBLICATION

   .. data:: OBJECT_PUBLICATION_NAMESPACE

   .. data:: OBJECT_PUBLICATION_REL

   .. data:: OBJECT_ROLE

   .. data:: OBJECT_ROUTINE

   .. data:: OBJECT_RULE

   .. data:: OBJECT_SCHEMA

   .. data:: OBJECT_SEQUENCE

   .. data:: OBJECT_SUBSCRIPTION

   .. data:: OBJECT_STATISTIC_EXT

   .. data:: OBJECT_TABCONSTRAINT

   .. data:: OBJECT_TABLE

   .. data:: OBJECT_TABLESPACE

   .. data:: OBJECT_TRANSFORM

   .. data:: OBJECT_TRIGGER

   .. data:: OBJECT_TSCONFIGURATION

   .. data:: OBJECT_TSDICTIONARY

   .. data:: OBJECT_TSPARSER

   .. data:: OBJECT_TSTEMPLATE

   .. data:: OBJECT_TYPE

   .. data:: OBJECT_USER_MAPPING

   .. data:: OBJECT_VIEW


.. class:: pglast.enums.parsenodes.PartitionRangeDatumKind

   Corresponds to the `PartitionRangeDatumKind enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L922>`__.

   .. data:: PARTITION_RANGE_DATUM_MINVALUE

   .. data:: PARTITION_RANGE_DATUM_VALUE

   .. data:: PARTITION_RANGE_DATUM_MAXVALUE


.. class:: pglast.enums.parsenodes.PartitionStrategy

   Corresponds to the `PartitionStrategy enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L870>`__.

   .. data:: PARTITION_STRATEGY_LIST

   .. data:: PARTITION_STRATEGY_RANGE

   .. data:: PARTITION_STRATEGY_HASH


.. class:: pglast.enums.parsenodes.PublicationObjSpecType

   Corresponds to the `PublicationObjSpecType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L4142>`__.

   .. data:: PUBLICATIONOBJ_TABLE

   .. data:: PUBLICATIONOBJ_TABLES_IN_SCHEMA

   .. data:: PUBLICATIONOBJ_TABLES_IN_CUR_SCHEMA

   .. data:: PUBLICATIONOBJ_CONTINUATION


.. class:: pglast.enums.parsenodes.QuerySource

   Corresponds to the `QuerySource enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L34>`__.

   .. data:: QSRC_ORIGINAL

   .. data:: QSRC_PARSER

   .. data:: QSRC_INSTEAD_RULE

   .. data:: QSRC_QUAL_INSTEAD_RULE

   .. data:: QSRC_NON_INSTEAD_RULE


.. class:: pglast.enums.parsenodes.RTEKind

   Corresponds to the `RTEKind enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L1023>`__.

   .. data:: RTE_RELATION

   .. data:: RTE_SUBQUERY

   .. data:: RTE_JOIN

   .. data:: RTE_FUNCTION

   .. data:: RTE_TABLEFUNC

   .. data:: RTE_VALUES

   .. data:: RTE_CTE

   .. data:: RTE_NAMEDTUPLESTORE

   .. data:: RTE_RESULT


.. class:: pglast.enums.parsenodes.ReindexObjectType

   Corresponds to the `ReindexObjectType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3965>`__.

   .. data:: REINDEX_OBJECT_INDEX

   .. data:: REINDEX_OBJECT_TABLE

   .. data:: REINDEX_OBJECT_SCHEMA

   .. data:: REINDEX_OBJECT_SYSTEM

   .. data:: REINDEX_OBJECT_DATABASE


.. class:: pglast.enums.parsenodes.RoleSpecType

   Corresponds to the `RoleSpecType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L392>`__.

   .. data:: ROLESPEC_CSTRING

   .. data:: ROLESPEC_CURRENT_ROLE

   .. data:: ROLESPEC_CURRENT_USER

   .. data:: ROLESPEC_SESSION_USER

   .. data:: ROLESPEC_PUBLIC


.. class:: pglast.enums.parsenodes.RoleStmtType

   Corresponds to the `RoleStmtType enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3074>`__.

   .. data:: ROLESTMT_ROLE

   .. data:: ROLESTMT_USER

   .. data:: ROLESTMT_GROUP


.. class:: pglast.enums.parsenodes.SetOperation

   Corresponds to the `SetOperation enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2108>`__.

   .. data:: SETOP_NONE

   .. data:: SETOP_UNION

   .. data:: SETOP_INTERSECT

   .. data:: SETOP_EXCEPT


.. class:: pglast.enums.parsenodes.SetQuantifier

   Corresponds to the `SetQuantifier enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L60>`__.

   .. data:: SET_QUANTIFIER_DEFAULT

   .. data:: SET_QUANTIFIER_ALL

   .. data:: SET_QUANTIFIER_DISTINCT


.. class:: pglast.enums.parsenodes.SortByDir

   Corresponds to the `SortByDir enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L44>`__.

   .. data:: SORTBY_DEFAULT

   .. data:: SORTBY_ASC

   .. data:: SORTBY_DESC

   .. data:: SORTBY_USING


.. class:: pglast.enums.parsenodes.SortByNulls

   Corresponds to the `SortByNulls enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L52>`__.

   .. data:: SORTBY_NULLS_DEFAULT

   .. data:: SORTBY_NULLS_FIRST

   .. data:: SORTBY_NULLS_LAST


.. class:: pglast.enums.parsenodes.TableLikeOption

   Corresponds to the `TableLikeOption enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L759>`__.

   .. data:: CREATE_TABLE_LIKE_COMMENTS

   .. data:: CREATE_TABLE_LIKE_COMPRESSION

   .. data:: CREATE_TABLE_LIKE_CONSTRAINTS

   .. data:: CREATE_TABLE_LIKE_DEFAULTS

   .. data:: CREATE_TABLE_LIKE_GENERATED

   .. data:: CREATE_TABLE_LIKE_IDENTITY

   .. data:: CREATE_TABLE_LIKE_INDEXES

   .. data:: CREATE_TABLE_LIKE_STATISTICS

   .. data:: CREATE_TABLE_LIKE_STORAGE

   .. data:: CREATE_TABLE_LIKE_ALL


.. class:: pglast.enums.parsenodes.TransactionStmtKind

   Corresponds to the `TransactionStmtKind enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3653>`__.

   .. data:: TRANS_STMT_BEGIN

   .. data:: TRANS_STMT_START

   .. data:: TRANS_STMT_COMMIT

   .. data:: TRANS_STMT_ROLLBACK

   .. data:: TRANS_STMT_SAVEPOINT

   .. data:: TRANS_STMT_RELEASE

   .. data:: TRANS_STMT_ROLLBACK_TO

   .. data:: TRANS_STMT_PREPARE

   .. data:: TRANS_STMT_COMMIT_PREPARED

   .. data:: TRANS_STMT_ROLLBACK_PREPARED


.. class:: pglast.enums.parsenodes.VariableSetKind

   Corresponds to the `VariableSetKind enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2608>`__.

   .. data:: VAR_SET_VALUE

   .. data:: VAR_SET_DEFAULT

   .. data:: VAR_SET_CURRENT

   .. data:: VAR_SET_MULTI

   .. data:: VAR_RESET

   .. data:: VAR_RESET_ALL


.. class:: pglast.enums.parsenodes.ViewCheckOption

   Corresponds to the `ViewCheckOption enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3733>`__.

   .. data:: NO_CHECK_OPTION

   .. data:: LOCAL_CHECK_OPTION

   .. data:: CASCADED_CHECK_OPTION


.. class:: pglast.enums.parsenodes.WCOKind

   Corresponds to the `WCOKind enum <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L1358>`__.

   .. data:: WCO_VIEW_CHECK

   .. data:: WCO_RLS_INSERT_CHECK

   .. data:: WCO_RLS_UPDATE_CHECK

   .. data:: WCO_RLS_CONFLICT_CHECK

   .. data:: WCO_RLS_MERGE_UPDATE_CHECK

   .. data:: WCO_RLS_MERGE_DELETE_CHECK


.. data:: ACL_INSERT

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L76>`__.

.. data:: ACL_SELECT

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L77>`__.

.. data:: ACL_UPDATE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L78>`__.

.. data:: ACL_DELETE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L79>`__.

.. data:: ACL_TRUNCATE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L80>`__.

.. data:: ACL_REFERENCES

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L81>`__.

.. data:: ACL_TRIGGER

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L82>`__.

.. data:: ACL_EXECUTE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L83>`__.

.. data:: ACL_USAGE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L84>`__.

.. data:: ACL_CREATE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L85>`__.

.. data:: ACL_CREATE_TEMP

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L86>`__.

.. data:: ACL_CONNECT

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L87>`__.

.. data:: ACL_SET

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L88>`__.

.. data:: ACL_ALTER_SYSTEM

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L89>`__.

.. data:: ACL_MAINTAIN

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L90>`__.

.. data:: N_ACL_RIGHTS

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L91>`__.

.. data:: ACL_NO_RIGHTS

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L92>`__.

.. data:: FRAMEOPTION_NONDEFAULT

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L581>`__.

.. data:: FRAMEOPTION_RANGE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L582>`__.

.. data:: FRAMEOPTION_ROWS

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L583>`__.

.. data:: FRAMEOPTION_GROUPS

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L584>`__.

.. data:: FRAMEOPTION_BETWEEN

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L585>`__.

.. data:: FRAMEOPTION_START_UNBOUNDED_PRECEDING

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L586>`__.

.. data:: FRAMEOPTION_END_UNBOUNDED_PRECEDING

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L587>`__.

.. data:: FRAMEOPTION_START_UNBOUNDED_FOLLOWING

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L588>`__.

.. data:: FRAMEOPTION_END_UNBOUNDED_FOLLOWING

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L589>`__.

.. data:: FRAMEOPTION_START_CURRENT_ROW

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L590>`__.

.. data:: FRAMEOPTION_END_CURRENT_ROW

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L591>`__.

.. data:: FRAMEOPTION_START_OFFSET_PRECEDING

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L592>`__.

.. data:: FRAMEOPTION_END_OFFSET_PRECEDING

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L593>`__.

.. data:: FRAMEOPTION_START_OFFSET_FOLLOWING

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L594>`__.

.. data:: FRAMEOPTION_END_OFFSET_FOLLOWING

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L595>`__.

.. data:: FRAMEOPTION_EXCLUDE_CURRENT_ROW

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L596>`__.

.. data:: FRAMEOPTION_EXCLUDE_GROUP

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L597>`__.

.. data:: FRAMEOPTION_EXCLUDE_TIES

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L598>`__.

.. data:: FKCONSTR_ACTION_NOACTION

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2717>`__.

.. data:: FKCONSTR_ACTION_RESTRICT

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2718>`__.

.. data:: FKCONSTR_ACTION_CASCADE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2719>`__.

.. data:: FKCONSTR_ACTION_SETNULL

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2720>`__.

.. data:: FKCONSTR_ACTION_SETDEFAULT

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2721>`__.

.. data:: FKCONSTR_MATCH_FULL

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2724>`__.

.. data:: FKCONSTR_MATCH_PARTIAL

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2725>`__.

.. data:: FKCONSTR_MATCH_SIMPLE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L2726>`__.

.. data:: OPCLASS_ITEM_OPERATOR

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3180>`__.

.. data:: OPCLASS_ITEM_FUNCTION

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3181>`__.

.. data:: OPCLASS_ITEM_STORAGETYPE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3182>`__.

.. data:: CURSOR_OPT_BINARY

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3281>`__.

.. data:: CURSOR_OPT_SCROLL

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3282>`__.

.. data:: CURSOR_OPT_NO_SCROLL

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3283>`__.

.. data:: CURSOR_OPT_INSENSITIVE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3284>`__.

.. data:: CURSOR_OPT_ASENSITIVE

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3285>`__.

.. data:: CURSOR_OPT_HOLD

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3286>`__.

.. data:: CURSOR_OPT_FAST_PLAN

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3288>`__.

.. data:: CURSOR_OPT_GENERIC_PLAN

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3289>`__.

.. data:: CURSOR_OPT_CUSTOM_PLAN

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3290>`__.

.. data:: CURSOR_OPT_PARALLEL_OK

   See `here for details <https://github.com/pganalyze/libpg_query/blob/1c1a32e/src/postgres/include/nodes/parsenodes.h#L3291>`__.
