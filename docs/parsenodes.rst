.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2019 Lele Gaifax
..

==============================================================================
 :mod:`pglast.enums.parsenodes` --- Constants extracted from `parsenodes.h`__
==============================================================================

__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h

.. module:: pglast.enums.parsenodes
   :synopsis: Constants extracted from parsenodes.h


.. class:: pglast.enums.parsenodes.A_Expr_Kind

   Corresponds to the `A_Expr_Kind enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l252>`__.

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


.. class:: pglast.enums.parsenodes.AlterSubscriptionType

   Corresponds to the `AlterSubscriptionType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l3497>`__.

   .. data:: ALTER_SUBSCRIPTION_OPTIONS

   .. data:: ALTER_SUBSCRIPTION_CONNECTION

   .. data:: ALTER_SUBSCRIPTION_PUBLICATION

   .. data:: ALTER_SUBSCRIPTION_REFRESH

   .. data:: ALTER_SUBSCRIPTION_ENABLED


.. class:: pglast.enums.parsenodes.AlterTSConfigType

   Corresponds to the `AlterTSConfigType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l3438>`__.

   .. data:: ALTER_TSCONFIG_ADD_MAPPING

   .. data:: ALTER_TSCONFIG_ALTER_MAPPING_FOR_TOKEN

   .. data:: ALTER_TSCONFIG_REPLACE_DICT

   .. data:: ALTER_TSCONFIG_REPLACE_DICT_FOR_TOKEN

   .. data:: ALTER_TSCONFIG_DROP_MAPPING


.. class:: pglast.enums.parsenodes.AlterTableType

   Corresponds to the `AlterTableType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l1759>`__.

   .. data:: AT_AddColumn

   .. data:: AT_AddColumnRecurse

   .. data:: AT_AddColumnToView

   .. data:: AT_ColumnDefault

   .. data:: AT_DropNotNull

   .. data:: AT_SetNotNull

   .. data:: AT_CheckNotNull

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

   .. data:: AT_ReAddDomainConstraint

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


.. class:: pglast.enums.parsenodes.CTEMaterialize

   Corresponds to the `CTEMaterialize enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l1417>`__.

   .. data:: CTEMaterializeDefault

   .. data:: CTEMaterializeAlways

   .. data:: CTEMaterializeNever


.. class:: pglast.enums.parsenodes.ClusterOption

   Corresponds to the `ClusterOption enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l3152>`__.

   .. data:: CLUOPT_RECHECK

   .. data:: CLUOPT_VERBOSE


.. class:: pglast.enums.parsenodes.ConstrType

   Corresponds to the `ConstrType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2095>`__.

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

   Corresponds to the `DefElemAction enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l718>`__.

   .. data:: DEFELEM_UNSPEC

   .. data:: DEFELEM_SET

   .. data:: DEFELEM_ADD

   .. data:: DEFELEM_DROP


.. class:: pglast.enums.parsenodes.DiscardMode

   Corresponds to the `DiscardMode enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l3260>`__.

   .. data:: DISCARD_ALL

   .. data:: DISCARD_PLANS

   .. data:: DISCARD_SEQUENCES

   .. data:: DISCARD_TEMP


.. class:: pglast.enums.parsenodes.DropBehavior

   Corresponds to the `DropBehavior enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l1740>`__.

   .. data:: DROP_RESTRICT

   .. data:: DROP_CASCADE


.. class:: pglast.enums.parsenodes.FetchDirection

   Corresponds to the `FetchDirection enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2717>`__.

   .. data:: FETCH_FORWARD

   .. data:: FETCH_BACKWARD

   .. data:: FETCH_ABSOLUTE

   .. data:: FETCH_RELATIVE


.. class:: pglast.enums.parsenodes.FunctionParameterMode

   Corresponds to the `FunctionParameterMode enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2807>`__.

   .. data:: FUNC_PARAM_IN

   .. data:: FUNC_PARAM_OUT

   .. data:: FUNC_PARAM_INOUT

   .. data:: FUNC_PARAM_VARIADIC

   .. data:: FUNC_PARAM_TABLE


.. class:: pglast.enums.parsenodes.GrantTargetType

   Corresponds to the `GrantTargetType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l1894>`__.

   .. data:: ACL_TARGET_OBJECT

   .. data:: ACL_TARGET_ALL_IN_SCHEMA

   .. data:: ACL_TARGET_DEFAULTS


.. class:: pglast.enums.parsenodes.GroupingSetKind

   Corresponds to the `GroupingSetKind enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l1291>`__.

   .. data:: GROUPING_SET_EMPTY

   .. data:: GROUPING_SET_SIMPLE

   .. data:: GROUPING_SET_ROLLUP

   .. data:: GROUPING_SET_CUBE

   .. data:: GROUPING_SET_SETS


.. class:: pglast.enums.parsenodes.ImportForeignSchemaType

   Corresponds to the `ImportForeignSchemaType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2340>`__.

   .. data:: FDW_IMPORT_SCHEMA_ALL

   .. data:: FDW_IMPORT_SCHEMA_LIMIT_TO

   .. data:: FDW_IMPORT_SCHEMA_EXCEPT


.. class:: pglast.enums.parsenodes.ObjectType

   Corresponds to the `ObjectType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l1669>`__.

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

   .. data:: OBJECT_PROCEDURE

   .. data:: OBJECT_PUBLICATION

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


.. class:: pglast.enums.parsenodes.OverridingKind

   Corresponds to the `OverridingKind enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l32>`__.

   .. data:: OVERRIDING_NOT_SET

   .. data:: OVERRIDING_USER_VALUE

   .. data:: OVERRIDING_SYSTEM_VALUE


.. class:: pglast.enums.parsenodes.PartitionRangeDatumKind

   Corresponds to the `PartitionRangeDatumKind enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l834>`__.

   .. data:: PARTITION_RANGE_DATUM_MINVALUE

   .. data:: PARTITION_RANGE_DATUM_VALUE

   .. data:: PARTITION_RANGE_DATUM_MAXVALUE


.. class:: pglast.enums.parsenodes.QuerySource

   Corresponds to the `QuerySource enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l40>`__.

   .. data:: QSRC_ORIGINAL

   .. data:: QSRC_PARSER

   .. data:: QSRC_INSTEAD_RULE

   .. data:: QSRC_QUAL_INSTEAD_RULE

   .. data:: QSRC_NON_INSTEAD_RULE


.. class:: pglast.enums.parsenodes.RTEKind

   Corresponds to the `RTEKind enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l955>`__.

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

   Corresponds to the `ReindexObjectType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l3306>`__.

   .. data:: REINDEX_OBJECT_INDEX

   .. data:: REINDEX_OBJECT_TABLE

   .. data:: REINDEX_OBJECT_SCHEMA

   .. data:: REINDEX_OBJECT_SYSTEM

   .. data:: REINDEX_OBJECT_DATABASE


.. class:: pglast.enums.parsenodes.RoleSpecType

   Corresponds to the `RoleSpecType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l317>`__.

   .. data:: ROLESPEC_CSTRING

   .. data:: ROLESPEC_CURRENT_USER

   .. data:: ROLESPEC_SESSION_USER

   .. data:: ROLESPEC_PUBLIC


.. class:: pglast.enums.parsenodes.RoleStmtType

   Corresponds to the `RoleStmtType enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2476>`__.

   .. data:: ROLESTMT_ROLE

   .. data:: ROLESTMT_USER

   .. data:: ROLESTMT_GROUP


.. class:: pglast.enums.parsenodes.SetOperation

   Corresponds to the `SetOperation enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l1556>`__.

   .. data:: SETOP_NONE

   .. data:: SETOP_UNION

   .. data:: SETOP_INTERSECT

   .. data:: SETOP_EXCEPT


.. class:: pglast.enums.parsenodes.SortByDir

   Corresponds to the `SortByDir enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l50>`__.

   .. data:: SORTBY_DEFAULT

   .. data:: SORTBY_ASC

   .. data:: SORTBY_DESC

   .. data:: SORTBY_USING


.. class:: pglast.enums.parsenodes.SortByNulls

   Corresponds to the `SortByNulls enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l58>`__.

   .. data:: SORTBY_NULLS_DEFAULT

   .. data:: SORTBY_NULLS_FIRST

   .. data:: SORTBY_NULLS_LAST


.. class:: pglast.enums.parsenodes.TableLikeOption

   Corresponds to the `TableLikeOption enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l676>`__.

   .. data:: CREATE_TABLE_LIKE_COMMENTS

   .. data:: CREATE_TABLE_LIKE_CONSTRAINTS

   .. data:: CREATE_TABLE_LIKE_DEFAULTS

   .. data:: CREATE_TABLE_LIKE_GENERATED

   .. data:: CREATE_TABLE_LIKE_IDENTITY

   .. data:: CREATE_TABLE_LIKE_INDEXES

   .. data:: CREATE_TABLE_LIKE_STATISTICS

   .. data:: CREATE_TABLE_LIKE_STORAGE

   .. data:: CREATE_TABLE_LIKE_ALL


.. class:: pglast.enums.parsenodes.TransactionStmtKind

   Corresponds to the `TransactionStmtKind enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2994>`__.

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

   Corresponds to the `VariableSetKind enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2006>`__.

   .. data:: VAR_SET_VALUE

   .. data:: VAR_SET_DEFAULT

   .. data:: VAR_SET_CURRENT

   .. data:: VAR_SET_MULTI

   .. data:: VAR_RESET

   .. data:: VAR_RESET_ALL


.. class:: pglast.enums.parsenodes.ViewCheckOption

   Corresponds to the `ViewCheckOption enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l3070>`__.

   .. data:: NO_CHECK_OPTION

   .. data:: LOCAL_CHECK_OPTION

   .. data:: CASCADED_CHECK_OPTION


.. class:: pglast.enums.parsenodes.WCOKind

   Corresponds to the `WCOKind enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l1155>`__.

   .. data:: WCO_VIEW_CHECK

   .. data:: WCO_RLS_INSERT_CHECK

   .. data:: WCO_RLS_UPDATE_CHECK

   .. data:: WCO_RLS_CONFLICT_CHECK


.. data:: ACL_INSERT

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l74>`__.

.. data:: ACL_SELECT

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l75>`__.

.. data:: ACL_UPDATE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l76>`__.

.. data:: ACL_DELETE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l77>`__.

.. data:: ACL_TRUNCATE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l78>`__.

.. data:: ACL_REFERENCES

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l79>`__.

.. data:: ACL_TRIGGER

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l80>`__.

.. data:: ACL_EXECUTE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l81>`__.

.. data:: ACL_USAGE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l82>`__.

.. data:: ACL_CREATE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l84>`__.

.. data:: ACL_CREATE_TEMP

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l85>`__.

.. data:: ACL_CONNECT

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l86>`__.

.. data:: N_ACL_RIGHTS

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l87>`__.

.. data:: ACL_NO_RIGHTS

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l88>`__.

.. data:: FRAMEOPTION_NONDEFAULT

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l504>`__.

.. data:: FRAMEOPTION_RANGE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l505>`__.

.. data:: FRAMEOPTION_ROWS

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l506>`__.

.. data:: FRAMEOPTION_GROUPS

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l507>`__.

.. data:: FRAMEOPTION_BETWEEN

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l508>`__.

.. data:: FRAMEOPTION_START_UNBOUNDED_PRECEDING

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l509>`__.

.. data:: FRAMEOPTION_END_UNBOUNDED_PRECEDING

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l510>`__.

.. data:: FRAMEOPTION_START_UNBOUNDED_FOLLOWING

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l511>`__.

.. data:: FRAMEOPTION_END_UNBOUNDED_FOLLOWING

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l512>`__.

.. data:: FRAMEOPTION_START_CURRENT_ROW

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l513>`__.

.. data:: FRAMEOPTION_END_CURRENT_ROW

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l514>`__.

.. data:: FRAMEOPTION_START_OFFSET_PRECEDING

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l515>`__.

.. data:: FRAMEOPTION_END_OFFSET_PRECEDING

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l516>`__.

.. data:: FRAMEOPTION_START_OFFSET_FOLLOWING

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l517>`__.

.. data:: FRAMEOPTION_END_OFFSET_FOLLOWING

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l518>`__.

.. data:: FRAMEOPTION_EXCLUDE_CURRENT_ROW

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l519>`__.

.. data:: FRAMEOPTION_EXCLUDE_GROUP

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l520>`__.

.. data:: FRAMEOPTION_EXCLUDE_TIES

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l521>`__.

.. data:: PARTITION_STRATEGY_HASH

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l798>`__.

.. data:: PARTITION_STRATEGY_LIST

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l799>`__.

.. data:: PARTITION_STRATEGY_RANGE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l800>`__.

.. data:: FKCONSTR_ACTION_NOACTION

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2115>`__.

.. data:: FKCONSTR_ACTION_RESTRICT

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2116>`__.

.. data:: FKCONSTR_ACTION_CASCADE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2117>`__.

.. data:: FKCONSTR_ACTION_SETNULL

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2118>`__.

.. data:: FKCONSTR_ACTION_SETDEFAULT

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2119>`__.

.. data:: FKCONSTR_MATCH_FULL

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2122>`__.

.. data:: FKCONSTR_MATCH_PARTIAL

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2123>`__.

.. data:: FKCONSTR_MATCH_SIMPLE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2124>`__.

.. data:: OPCLASS_ITEM_OPERATOR

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2582>`__.

.. data:: OPCLASS_ITEM_FUNCTION

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2583>`__.

.. data:: OPCLASS_ITEM_STORAGETYPE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2584>`__.

.. data:: CURSOR_OPT_BINARY

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2683>`__.

.. data:: CURSOR_OPT_SCROLL

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2684>`__.

.. data:: CURSOR_OPT_NO_SCROLL

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2685>`__.

.. data:: CURSOR_OPT_INSENSITIVE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2686>`__.

.. data:: CURSOR_OPT_HOLD

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2687>`__.

.. data:: CURSOR_OPT_FAST_PLAN

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2689>`__.

.. data:: CURSOR_OPT_GENERIC_PLAN

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2690>`__.

.. data:: CURSOR_OPT_CUSTOM_PLAN

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2691>`__.

.. data:: CURSOR_OPT_PARALLEL_OK

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l2692>`__.

.. data:: REINDEXOPT_VERBOSE

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l3303>`__.

.. data:: REINDEXOPT_REPORT_PROGRESS

   See `here for details <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/parsenodes.h#l3304>`__.
