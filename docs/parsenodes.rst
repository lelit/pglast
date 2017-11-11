.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

================================================================================
 :mod:`pg_query.enums.parsenodes` --- Constants extracted from `parsenodes.h`__
================================================================================

__ https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h

.. module:: pg_query.enums.parsenodes


.. class:: pg_query.enums.parsenodes.A_Expr_Kind

   Corresponds to the `A_Expr_Kind enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L251>`__.

   .. data:: AEXPR_OP

   .. data:: AEXPR_OP_ANY

   .. data:: AEXPR_OP_ALL

   .. data:: AEXPR_DISTINCT

   .. data:: AEXPR_NOT_DISTINCT

   .. data:: AEXPR_NULLIF

   .. data:: AEXPR_OF

   .. data:: AEXPR_IN

   .. data:: AEXPR_LIKE

   .. data:: AEXPR_ILIKE

   .. data:: AEXPR_SIMILAR

   .. data:: AEXPR_BETWEEN

   .. data:: AEXPR_NOT_BETWEEN

   .. data:: AEXPR_BETWEEN_SYM

   .. data:: AEXPR_NOT_BETWEEN_SYM

   .. data:: AEXPR_PAREN


.. class:: pg_query.enums.parsenodes.AlterSubscriptionType

   Corresponds to the `AlterSubscriptionType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L3405>`__.

   .. data:: ALTER_SUBSCRIPTION_OPTIONS

   .. data:: ALTER_SUBSCRIPTION_CONNECTION

   .. data:: ALTER_SUBSCRIPTION_PUBLICATION

   .. data:: ALTER_SUBSCRIPTION_REFRESH

   .. data:: ALTER_SUBSCRIPTION_ENABLED


.. class:: pg_query.enums.parsenodes.AlterTSConfigType

   Corresponds to the `AlterTSConfigType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L3346>`__.

   .. data:: ALTER_TSCONFIG_ADD_MAPPING

   .. data:: ALTER_TSCONFIG_ALTER_MAPPING_FOR_TOKEN

   .. data:: ALTER_TSCONFIG_REPLACE_DICT

   .. data:: ALTER_TSCONFIG_REPLACE_DICT_FOR_TOKEN

   .. data:: ALTER_TSCONFIG_DROP_MAPPING


.. class:: pg_query.enums.parsenodes.AlterTableType

   Corresponds to the `AlterTableType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1696>`__.

   .. data:: AT_AddColumn

   .. data:: AT_AddColumnRecurse

   .. data:: AT_AddColumnToView

   .. data:: AT_ColumnDefault

   .. data:: AT_DropNotNull

   .. data:: AT_SetNotNull

   .. data:: AT_SetStatistics

   .. data:: AT_SetOptions

   .. data:: AT_ResetOptions

   .. data:: AT_SetStorage

   .. data:: AT_DropColumn

   .. data:: AT_DropColumnRecurse

   .. data:: AT_AddIndex

   .. data:: AT_ReAddIndex

   .. data:: AT_AddConstraint

   .. data:: AT_AddConstraintRecurse

   .. data:: AT_ReAddConstraint

   .. data:: AT_AlterConstraint

   .. data:: AT_ValidateConstraint

   .. data:: AT_ValidateConstraintRecurse

   .. data:: AT_ProcessedConstraint

   .. data:: AT_AddIndexConstraint

   .. data:: AT_DropConstraint

   .. data:: AT_DropConstraintRecurse

   .. data:: AT_ReAddComment

   .. data:: AT_AlterColumnType

   .. data:: AT_AlterColumnGenericOptions

   .. data:: AT_ChangeOwner

   .. data:: AT_ClusterOn

   .. data:: AT_DropCluster

   .. data:: AT_SetLogged

   .. data:: AT_SetUnLogged

   .. data:: AT_AddOids

   .. data:: AT_AddOidsRecurse

   .. data:: AT_DropOids

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

   .. data:: AT_AddIdentity

   .. data:: AT_SetIdentity

   .. data:: AT_DropIdentity


.. class:: pg_query.enums.parsenodes.ConstrType

   Corresponds to the `ConstrType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2045>`__.

   .. data:: CONSTR_NULL

   .. data:: CONSTR_NOTNULL

   .. data:: CONSTR_DEFAULT

   .. data:: CONSTR_IDENTITY

   .. data:: CONSTR_CHECK

   .. data:: CONSTR_PRIMARY

   .. data:: CONSTR_UNIQUE

   .. data:: CONSTR_EXCLUSION

   .. data:: CONSTR_FOREIGN

   .. data:: CONSTR_ATTR_DEFERRABLE

   .. data:: CONSTR_ATTR_NOT_DEFERRABLE

   .. data:: CONSTR_ATTR_DEFERRED

   .. data:: CONSTR_ATTR_IMMEDIATE


.. class:: pg_query.enums.parsenodes.DefElemAction

   Corresponds to the `DefElemAction enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L707>`__.

   .. data:: DEFELEM_UNSPEC

   .. data:: DEFELEM_SET

   .. data:: DEFELEM_ADD

   .. data:: DEFELEM_DROP


.. class:: pg_query.enums.parsenodes.DiscardMode

   Corresponds to the `DiscardMode enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L3170>`__.

   .. data:: DISCARD_ALL

   .. data:: DISCARD_PLANS

   .. data:: DISCARD_SEQUENCES

   .. data:: DISCARD_TEMP


.. class:: pg_query.enums.parsenodes.DropBehavior

   Corresponds to the `DropBehavior enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1677>`__.

   .. data:: DROP_RESTRICT

   .. data:: DROP_CASCADE


.. class:: pg_query.enums.parsenodes.FetchDirection

   Corresponds to the `FetchDirection enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2661>`__.

   .. data:: FETCH_FORWARD

   .. data:: FETCH_BACKWARD

   .. data:: FETCH_ABSOLUTE

   .. data:: FETCH_RELATIVE


.. class:: pg_query.enums.parsenodes.FunctionParameterMode

   Corresponds to the `FunctionParameterMode enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2746>`__.

   .. data:: FUNC_PARAM_IN

   .. data:: FUNC_PARAM_OUT

   .. data:: FUNC_PARAM_INOUT

   .. data:: FUNC_PARAM_VARIADIC

   .. data:: FUNC_PARAM_TABLE


.. class:: pg_query.enums.parsenodes.GrantObjectType

   Corresponds to the `GrantObjectType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1836>`__.

   .. data:: ACL_OBJECT_COLUMN

   .. data:: ACL_OBJECT_RELATION

   .. data:: ACL_OBJECT_SEQUENCE

   .. data:: ACL_OBJECT_DATABASE

   .. data:: ACL_OBJECT_DOMAIN

   .. data:: ACL_OBJECT_FDW

   .. data:: ACL_OBJECT_FOREIGN_SERVER

   .. data:: ACL_OBJECT_FUNCTION

   .. data:: ACL_OBJECT_LANGUAGE

   .. data:: ACL_OBJECT_LARGEOBJECT

   .. data:: ACL_OBJECT_NAMESPACE

   .. data:: ACL_OBJECT_TABLESPACE

   .. data:: ACL_OBJECT_TYPE


.. class:: pg_query.enums.parsenodes.GrantTargetType

   Corresponds to the `GrantTargetType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1829>`__.

   .. data:: ACL_TARGET_OBJECT

   .. data:: ACL_TARGET_ALL_IN_SCHEMA

   .. data:: ACL_TARGET_DEFAULTS


.. class:: pg_query.enums.parsenodes.ImportForeignSchemaType

   Corresponds to the `ImportForeignSchemaType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2284>`__.

   .. data:: FDW_IMPORT_SCHEMA_ALL

   .. data:: FDW_IMPORT_SCHEMA_LIMIT_TO

   .. data:: FDW_IMPORT_SCHEMA_EXCEPT


.. class:: pg_query.enums.parsenodes.ObjectType

   Corresponds to the `ObjectType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1608>`__.

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

   .. data:: OBJECT_POLICY

   .. data:: OBJECT_PUBLICATION

   .. data:: OBJECT_PUBLICATION_REL

   .. data:: OBJECT_ROLE

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


.. class:: pg_query.enums.parsenodes.OverridingKind

   Corresponds to the `OverridingKind enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L30>`__.

   .. data:: OVERRIDING_NOT_SET

   .. data:: OVERRIDING_USER_VALUE

   .. data:: OVERRIDING_SYSTEM_VALUE


.. class:: pg_query.enums.parsenodes.PartitionRangeDatumKind

   Corresponds to the `PartitionRangeDatumKind enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L816>`__.

   .. data:: PARTITION_RANGE_DATUM_MINVALUE

   .. data:: PARTITION_RANGE_DATUM_VALUE

   .. data:: PARTITION_RANGE_DATUM_MAXVALUE


.. class:: pg_query.enums.parsenodes.QuerySource

   Corresponds to the `QuerySource enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L38>`__.

   .. data:: QSRC_ORIGINAL

   .. data:: QSRC_PARSER

   .. data:: QSRC_INSTEAD_RULE

   .. data:: QSRC_QUAL_INSTEAD_RULE

   .. data:: QSRC_NON_INSTEAD_RULE


.. class:: pg_query.enums.parsenodes.RTEKind

   Corresponds to the `RTEKind enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L928>`__.

   .. data:: RTE_RELATION

   .. data:: RTE_SUBQUERY

   .. data:: RTE_JOIN

   .. data:: RTE_FUNCTION

   .. data:: RTE_TABLEFUNC

   .. data:: RTE_VALUES

   .. data:: RTE_CTE

   .. data:: RTE_NAMEDTUPLESTORE


.. class:: pg_query.enums.parsenodes.ReindexObjectType

   Corresponds to the `ReindexObjectType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L3215>`__.

   .. data:: REINDEX_OBJECT_INDEX

   .. data:: REINDEX_OBJECT_TABLE

   .. data:: REINDEX_OBJECT_SCHEMA

   .. data:: REINDEX_OBJECT_SYSTEM

   .. data:: REINDEX_OBJECT_DATABASE


.. class:: pg_query.enums.parsenodes.RoleSpecType

   Corresponds to the `RoleSpecType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L316>`__.

   .. data:: ROLESPEC_CSTRING

   .. data:: ROLESPEC_CURRENT_USER

   .. data:: ROLESPEC_SESSION_USER

   .. data:: ROLESPEC_PUBLIC


.. class:: pg_query.enums.parsenodes.RoleStmtType

   Corresponds to the `RoleStmtType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2421>`__.

   .. data:: ROLESTMT_ROLE

   .. data:: ROLESTMT_USER

   .. data:: ROLESTMT_GROUP


.. class:: pg_query.enums.parsenodes.SetOperation

   Corresponds to the `SetOperation enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1495>`__.

   .. data:: SETOP_NONE

   .. data:: SETOP_UNION

   .. data:: SETOP_INTERSECT

   .. data:: SETOP_EXCEPT


.. class:: pg_query.enums.parsenodes.SortByDir

   Corresponds to the `SortByDir enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L48>`__.

   .. data:: SORTBY_DEFAULT

   .. data:: SORTBY_ASC

   .. data:: SORTBY_DESC

   .. data:: SORTBY_USING


.. class:: pg_query.enums.parsenodes.SortByNulls

   Corresponds to the `SortByNulls enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L56>`__.

   .. data:: SORTBY_NULLS_DEFAULT

   .. data:: SORTBY_NULLS_FIRST

   .. data:: SORTBY_NULLS_LAST


.. class:: pg_query.enums.parsenodes.TableLikeOption

   Corresponds to the `TableLikeOption enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L667>`__.

   .. data:: CREATE_TABLE_LIKE_DEFAULTS

   .. data:: CREATE_TABLE_LIKE_CONSTRAINTS

   .. data:: CREATE_TABLE_LIKE_IDENTITY

   .. data:: CREATE_TABLE_LIKE_INDEXES

   .. data:: CREATE_TABLE_LIKE_STORAGE

   .. data:: CREATE_TABLE_LIKE_COMMENTS

   .. data:: CREATE_TABLE_LIKE_ALL


.. class:: pg_query.enums.parsenodes.TransactionStmtKind

   Corresponds to the `TransactionStmtKind enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2914>`__.

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


.. class:: pg_query.enums.parsenodes.VacuumOption

   Corresponds to the `VacuumOption enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L3086>`__.

   .. data:: VACOPT_VACUUM

   .. data:: VACOPT_ANALYZE

   .. data:: VACOPT_VERBOSE

   .. data:: VACOPT_FREEZE

   .. data:: VACOPT_FULL

   .. data:: VACOPT_NOWAIT

   .. data:: VACOPT_SKIPTOAST

   .. data:: VACOPT_DISABLE_PAGE_SKIPPING


.. class:: pg_query.enums.parsenodes.ViewCheckOption

   Corresponds to the `ViewCheckOption enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2988>`__.

   .. data:: NO_CHECK_OPTION

   .. data:: LOCAL_CHECK_OPTION

   .. data:: CASCADED_CHECK_OPTION


.. class:: pg_query.enums.parsenodes.WCOKind

   Corresponds to the `WCOKind enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1110>`__.

   .. data:: WCO_VIEW_CHECK

   .. data:: WCO_RLS_INSERT_CHECK

   .. data:: WCO_RLS_UPDATE_CHECK

   .. data:: WCO_RLS_CONFLICT_CHECK


.. data:: ACL_INSERT

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L72>`__.

.. data:: ACL_SELECT

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L73>`__.

.. data:: ACL_UPDATE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L74>`__.

.. data:: ACL_DELETE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L75>`__.

.. data:: ACL_TRUNCATE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L76>`__.

.. data:: ACL_REFERENCES

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L77>`__.

.. data:: ACL_TRIGGER

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L78>`__.

.. data:: ACL_EXECUTE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L79>`__.

.. data:: ACL_USAGE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L80>`__.

.. data:: ACL_CREATE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L82>`__.

.. data:: ACL_CREATE_TEMP

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L83>`__.

.. data:: ACL_CONNECT

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L84>`__.

.. data:: FRAMEOPTION_NONDEFAULT

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L504>`__.

.. data:: FRAMEOPTION_RANGE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L505>`__.

.. data:: FRAMEOPTION_ROWS

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L506>`__.

.. data:: FRAMEOPTION_BETWEEN

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L507>`__.

.. data:: FRAMEOPTION_START_UNBOUNDED_PRECEDING

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L508>`__.

.. data:: FRAMEOPTION_END_UNBOUNDED_PRECEDING

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L509>`__.

.. data:: FRAMEOPTION_START_UNBOUNDED_FOLLOWING

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L510>`__.

.. data:: FRAMEOPTION_END_UNBOUNDED_FOLLOWING

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L511>`__.

.. data:: FRAMEOPTION_START_CURRENT_ROW

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L512>`__.

.. data:: FRAMEOPTION_END_CURRENT_ROW

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L513>`__.

.. data:: FRAMEOPTION_START_VALUE_PRECEDING

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L514>`__.

.. data:: FRAMEOPTION_END_VALUE_PRECEDING

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L515>`__.

.. data:: FRAMEOPTION_START_VALUE_FOLLOWING

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L516>`__.

.. data:: FRAMEOPTION_END_VALUE_FOLLOWING

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L517>`__.

.. data:: PARTITION_STRATEGY_LIST

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L786>`__.

.. data:: PARTITION_STRATEGY_RANGE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L787>`__.

.. data:: FKCONSTR_ACTION_NOACTION

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2064>`__.

.. data:: FKCONSTR_ACTION_RESTRICT

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2065>`__.

.. data:: FKCONSTR_ACTION_CASCADE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2066>`__.

.. data:: FKCONSTR_ACTION_SETNULL

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2067>`__.

.. data:: FKCONSTR_ACTION_SETDEFAULT

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2068>`__.

.. data:: FKCONSTR_MATCH_FULL

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2071>`__.

.. data:: FKCONSTR_MATCH_PARTIAL

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2072>`__.

.. data:: FKCONSTR_MATCH_SIMPLE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2073>`__.

.. data:: CURSOR_OPT_BINARY

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2627>`__.

.. data:: CURSOR_OPT_SCROLL

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2628>`__.

.. data:: CURSOR_OPT_NO_SCROLL

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2629>`__.

.. data:: CURSOR_OPT_INSENSITIVE

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2630>`__.

.. data:: CURSOR_OPT_HOLD

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2631>`__.

.. data:: CURSOR_OPT_FAST_PLAN

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2633>`__.

.. data:: CURSOR_OPT_GENERIC_PLAN

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2634>`__.

.. data:: CURSOR_OPT_CUSTOM_PLAN

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2635>`__.

.. data:: CURSOR_OPT_PARALLEL_OK

   See `here for details <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2636>`__.
