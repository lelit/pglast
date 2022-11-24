.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2022 Lele Gaifax
..

======================================================
 :mod:`pglast.printers.ddl` --- DDL printer functions
======================================================

.. module:: pglast.printers.ddl
   :synopsis: DDL printer functions

.. index:: AccessPriv

.. function:: access_priv(node, output)

   Pretty print a `node` of type `AccessPriv <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2060>`__ to the `output` stream.

.. index:: AlterCollationStmt

.. function:: alter_collation_stmt(node, output)

   Pretty print a `node` of type `AlterCollationStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1967>`__ to the `output` stream.

.. index:: AlterDatabaseStmt

.. function:: alter_database_stmt(node, output)

   Pretty print a `node` of type `AlterDatabaseStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3287>`__ to the `output` stream.

.. index:: AlterDatabaseSetStmt

.. function:: alter_database_set_stmt(node, output)

   Pretty print a `node` of type `AlterDatabaseSetStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3294>`__ to the `output` stream.

.. index:: AlterExtensionStmt

.. function:: alter_extension_stmt(node, output)

   Pretty print a `node` of type `AlterExtensionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2353>`__ to the `output` stream.

.. index::
   pair: AlterExtensionStmt;DefElem

.. function:: alter_extension_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `AlterExtensionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2353>`__, to the `output` stream.

.. index:: AlterExtensionContentsStmt

.. function:: alter_extension_contents_stmt(node, output)

   Pretty print a `node` of type `AlterExtensionContentsStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2360>`__ to the `output` stream.

.. index:: AlterEnumStmt

.. function:: alter_enum_stmt(node, output)

   Pretty print a `node` of type `AlterEnumStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3229>`__ to the `output` stream.

.. index:: AlterDefaultPrivilegesStmt

.. function:: alter_default_privileges_stmt(node, output)

   Pretty print a `node` of type `AlterDefaultPrivilegesStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2091>`__ to the `output` stream.

.. index:: AlterFunctionStmt

.. function:: alter_function_stmt(node, output)

   Pretty print a `node` of type `AlterFunctionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2984>`__ to the `output` stream.

.. index:: AlterObjectSchemaStmt

.. function:: alter_object_schema_stmt(node, output)

   Pretty print a `node` of type `AlterObjectSchemaStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3072>`__ to the `output` stream.

.. index:: AlterOperatorStmt

.. function:: alter_operator_stmt(node, output)

   Pretty print a `node` of type `AlterOperatorStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3099>`__ to the `output` stream.

.. index::
   pair: AlterOperatorStmt;DefElem

.. function:: alter_operator_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `AlterOperatorStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3099>`__, to the `output` stream.

.. index:: AlterOpFamilyStmt

.. function:: alter_op_family_stmt(node, output)

   Pretty print a `node` of type `AlterOpFamilyStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2737>`__ to the `output` stream.

.. index:: AlterOwnerStmt

.. function:: alter_owner_stmt(node, output)

   Pretty print a `node` of type `AlterOwnerStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3086>`__ to the `output` stream.

.. index:: AlterPolicyStmt

.. function:: alter_policy_stmt(node, output)

   Pretty print a `node` of type `AlterPolicyStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2500>`__ to the `output` stream.

.. index:: AlterRoleStmt

.. function:: alter_role_stmt(node, output)

   Pretty print a `node` of type `AlterRoleStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2614>`__ to the `output` stream.

.. index:: AlterSeqStmt

.. function:: alter_seq_stmt(node, output)

   Pretty print a `node` of type `AlterSeqStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2652>`__ to the `output` stream.

.. index:: AlterTableStmt

.. function:: alter_table_stmt(node, output)

   Pretty print a `node` of type `AlterTableStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1856>`__ to the `output` stream.

.. index::
   pair: AlterTableStmt;RangeVar

.. function:: range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L63>`__, when it is inside a `AlterTableStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1856>`__, to the `output` stream.

.. index:: AlterTableCmd

.. function:: alter_table_cmd(node, output)

   Pretty print a `node` of type `AlterTableCmd <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1946>`__ to the `output` stream.

.. index::
   pair: AlterTableCmd;DefElem

.. index::
   pair: CreatePublicationStmt;DefElem

.. index::
   pair: CreateStmt;DefElem

.. index::
   pair: IndexStmt;DefElem

.. index::
   pair: IntoClause;DefElem

.. function:: alter_table_cmd_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `AlterTableCmd <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1946>`__ or a `CreatePublicationStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3628>`__ or a `CreateStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2168>`__ or a `IndexStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2873>`__ or a `IntoClause <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L108>`__, to the `output` stream.

.. index:: AlterTSConfigurationStmt

.. function:: alter_ts_configuration_stmt(node, output)

   Pretty print a `node` of type `AlterTSConfigurationStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3610>`__ to the `output` stream.

.. index:: AlterTSDictionaryStmt

.. function:: alter_ts_dictionary_stmt(node, output)

   Pretty print a `node` of type `AlterTSDictionaryStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3591>`__ to the `output` stream.

.. index:: AlterStatsStmt

.. function:: alter_stats_stmt(node, output)

   Pretty print a `node` of type `AlterStatsStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2939>`__ to the `output` stream.

.. index:: AlterSubscriptionStmt

.. function:: alter_subscription_stmt(node, output)

   Pretty print a `node` of type `AlterSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3671>`__ to the `output` stream.

.. index:: AlterPublicationStmt

.. function:: alter_publication_stmt(node, output)

   Pretty print a `node` of type `AlterPublicationStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3637>`__ to the `output` stream.

.. index:: AlterFdwStmt

.. function:: alter_fdw_stmt(node, output)

   Pretty print a `node` of type `AlterFdwStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2382>`__ to the `output` stream.

.. index::
   pair: AlterFdwStmt;DefElem

.. function:: alter_fdw_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `AlterFdwStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2382>`__, to the `output` stream.

.. index:: AlterForeignServerStmt

.. function:: alter_foreign_server_stmt(node, output)

   Pretty print a `node` of type `AlterForeignServerStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2406>`__ to the `output` stream.

.. index:: AlterUserMappingStmt

.. function:: alter_user_mapping_stmt(node, output)

   Pretty print a `node` of type `AlterUserMappingStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2441>`__ to the `output` stream.

.. index:: AlterRoleSetStmt

.. function:: alter_role_set_stmt(node, output)

   Pretty print a `node` of type `AlterRoleSetStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2622>`__ to the `output` stream.

.. index:: AlterDomainStmt

.. function:: alter_domain_stmt(node, output)

   Pretty print a `node` of type `AlterDomainStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1981>`__ to the `output` stream.

.. index:: AlterEventTrigStmt

.. function:: alter_event_trig_stmt(node, output)

   Pretty print a `node` of type `AlterEventTrigStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2567>`__ to the `output` stream.

.. index:: AlterTypeStmt

.. function:: alter_type_stmt(node, output)

   Pretty print a `node` of type `AlterTypeStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3110>`__ to the `output` stream.

.. index:: CheckPointStmt

.. function:: check_point_stmt(node, output)

   Pretty print a `node` of type `CheckPointStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3419>`__ to the `output` stream.

.. index:: ClusterStmt

.. function:: cluster_stmt(node, output)

   Pretty print a `node` of type `ClusterStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3327>`__ to the `output` stream.

.. index:: ColumnDef

.. function:: column_def(node, output)

   Pretty print a `node` of type `ColumnDef <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L655>`__ to the `output` stream.

.. index:: CommentStmt

.. function:: comment_stmt(node, output)

   Pretty print a `node` of type `CommentStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2777>`__ to the `output` stream.

.. index:: CompositeTypeStmt

.. function:: composite_type_stmt(node, output)

   Pretty print a `node` of type `CompositeTypeStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3196>`__ to the `output` stream.

.. index::
   pair: CompositeTypeStmt;RangeVar

.. function:: composite_type_stmt_range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L63>`__, when it is inside a `CompositeTypeStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3196>`__, to the `output` stream.

.. index:: Constraint

.. function:: constraint(node, output)

   Pretty print a `node` of type `Constraint <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2248>`__ to the `output` stream.

.. index:: CreateAmStmt

.. function:: create_am_stmt(node, output)

   Pretty print a `node` of type `CreateAmStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2514>`__ to the `output` stream.

.. index:: CreatedbStmt

.. function:: create_db_stmt(node, output)

   Pretty print a `node` of type `CreatedbStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3276>`__ to the `output` stream.

.. index::
   pair: CreatedbStmt;DefElem

.. function:: create_db_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `CreatedbStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3276>`__, to the `output` stream.

.. index:: CreateCastStmt

.. function:: create_cast_stmt(node, output)

   Pretty print a `node` of type `CreateCastStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3507>`__ to the `output` stream.

.. index:: CreateConversionStmt

.. function:: create_conversion_stmt(node, output)

   Pretty print a `node` of type `CreateConversionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3493>`__ to the `output` stream.

.. index:: CreateDomainStmt

.. function:: create_domain_stmt(node, output)

   Pretty print a `node` of type `CreateDomainStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2681>`__ to the `output` stream.

.. index:: CreateEnumStmt

.. function:: create_enum_stmt(node, output)

   Pretty print a `node` of type `CreateEnumStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3207>`__ to the `output` stream.

.. index:: CreateEventTrigStmt

.. function:: create_event_trig_stmt(node, output)

   Pretty print a `node` of type `CreateEventTrigStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2554>`__ to the `output` stream.

.. index::
   pair: CreateEventTrigStmt;DefElem

.. function:: create_event_trig_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `CreateEventTrigStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2554>`__, to the `output` stream.

.. index:: CreateExtensionStmt

.. function:: create_extension_stmt(node, output)

   Pretty print a `node` of type `CreateExtensionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2344>`__ to the `output` stream.

.. index::
   pair: CreateExtensionStmt;DefElem

.. function:: create_extension_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `CreateExtensionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2344>`__, to the `output` stream.

.. index:: CreateFdwStmt

.. function:: create_fdw_stmt(node, output)

   Pretty print a `node` of type `CreateFdwStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2374>`__ to the `output` stream.

.. index::
   pair: ColumnDef;DefElem

.. index::
   pair: CreateUserMappingStmt;DefElem

.. index::
   pair: CreateFdwStmt;DefElem

.. function:: create_fdw_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `ColumnDef <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L655>`__ or a `CreateUserMappingStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2432>`__ or a `CreateFdwStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2374>`__, to the `output` stream.

.. index:: CreateForeignServerStmt

.. function:: create_foreign_server_stmt(node, output)

   Pretty print a `node` of type `CreateForeignServerStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2395>`__ to the `output` stream.

.. index:: CreateForeignTableStmt

.. function:: create_foreign_table_stmt(node, output)

   Pretty print a `node` of type `CreateForeignTableStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2420>`__ to the `output` stream.

.. index::
   pair: CreateForeignTableStmt;DefElem

.. index::
   pair: CreateForeignServerStmt;DefElem

.. function:: create_foreign_table_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `CreateForeignTableStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2420>`__ or a `CreateForeignServerStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2395>`__, to the `output` stream.

.. index:: CreateFunctionStmt

.. function:: create_function_stmt(node, output)

   Pretty print a `node` of type `CreateFunctionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2951>`__ to the `output` stream.

.. index::
   pair: AlterFunctionStmt;DefElem

.. index::
   pair: CreateFunctionStmt;DefElem

.. index::
   pair: DoStmt;DefElem

.. function:: create_function_option(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `AlterFunctionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2984>`__ or a `CreateFunctionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2951>`__ or a `DoStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2998>`__, to the `output` stream.

.. index:: CreateOpClassStmt

.. function:: create_opclass_stmt(node, output)

   Pretty print a `node` of type `CreateOpClassStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2694>`__ to the `output` stream.

.. index:: CreateOpClassItem

.. function:: create_opclass_item(node, output)

   Pretty print a `node` of type `CreateOpClassItem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2709>`__ to the `output` stream.

.. index:: CreateOpFamilyStmt

.. function:: create_op_family_stmt(node, output)

   Pretty print a `node` of type `CreateOpFamilyStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2726>`__ to the `output` stream.

.. index:: CreatePLangStmt

.. function:: create_plang_stmt(node, output)

   Pretty print a `node` of type `CreatePLangStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2579>`__ to the `output` stream.

.. index:: CreatePolicyStmt

.. function:: create_policy_stmt(node, output)

   Pretty print a `node` of type `CreatePolicyStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2484>`__ to the `output` stream.

.. index:: CreatePublicationStmt

.. function:: create_publication_stmt(node, output)

   Pretty print a `node` of type `CreatePublicationStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3628>`__ to the `output` stream.

.. index::
   pair: CreatePublicationStmt;RangeVar

.. function:: create_publication_stmt_range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L63>`__, when it is inside a `CreatePublicationStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3628>`__, to the `output` stream.

.. index:: CreateRangeStmt

.. function:: create_range_stmt(node, output)

   Pretty print a `node` of type `CreateRangeStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3218>`__ to the `output` stream.

.. index:: CreateRoleStmt

.. function:: create_role_stmt(node, output)

   Pretty print a `node` of type `CreateRoleStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2606>`__ to the `output` stream.

.. index::
   pair: AlterRoleStmt;DefElem

.. index::
   pair: CreateRoleStmt;DefElem

.. function:: create_or_alter_role_option(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `AlterRoleStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2614>`__ or a `CreateRoleStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2606>`__, to the `output` stream.

.. index:: CreateSchemaStmt

.. function:: create_schema_stmt(node, output)

   Pretty print a `node` of type `CreateSchemaStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1837>`__ to the `output` stream.

.. index:: CreateSeqStmt

.. function:: create_seq_stmt(node, output)

   Pretty print a `node` of type `CreateSeqStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2642>`__ to the `output` stream.

.. index::
   pair: Constraint;DefElem

.. index::
   pair: CreateSeqStmt;DefElem

.. index::
   pair: AlterSeqStmt;DefElem

.. function:: create_seq_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `Constraint <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2248>`__ or a `CreateSeqStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2642>`__ or a `AlterSeqStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2652>`__, to the `output` stream.

.. index:: CreateStatsStmt

.. function:: create_stats_stmt(node, output)

   Pretty print a `node` of type `CreateStatsStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2908>`__ to the `output` stream.

.. index:: CreateStmt

.. function:: create_stmt(node, output)

   Pretty print a `node` of type `CreateStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2168>`__ to the `output` stream.

.. index:: CreateTableAsStmt

.. function:: create_table_as_stmt(node, output)

   Pretty print a `node` of type `CreateTableAsStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3393>`__ to the `output` stream.

.. index:: CreateTableSpaceStmt

.. function:: create_table_space_stmt(node, output)

   Pretty print a `node` of type `CreateTableSpaceStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2305>`__ to the `output` stream.

.. index:: CreateTrigStmt

.. function:: create_trig_stmt(node, output)

   Pretty print a `node` of type `CreateTrigStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2526>`__ to the `output` stream.

.. index::
   pair: AlterSubscriptionStmt;DefElem

.. index::
   pair: CreateSubscriptionStmt;DefElem

.. function:: create_subscription_stmt_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `AlterSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3671>`__ or a `CreateSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3651>`__, to the `output` stream.

.. index:: CreateSubscriptionStmt

.. function:: create_subscription_stmt(node, output)

   Pretty print a `node` of type `CreateSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3651>`__ to the `output` stream.

.. index:: CurrentOfExpr

.. function:: current_of_expr(node, output)

   Pretty print a `node` of type `CurrentOfExpr <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1349>`__ to the `output` stream.

.. index:: CreateTransformStmt

.. function:: create_transform_stmt(node, output)

   Pretty print a `node` of type `CreateTransformStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3521>`__ to the `output` stream.

.. index:: ClosePortalStmt

.. function:: close_portal_stmt(node, output)

   Pretty print a `node` of type `ClosePortalStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2830>`__ to the `output` stream.

.. index:: CreateUserMappingStmt

.. function:: create_user_mapping_stmt(node, output)

   Pretty print a `node` of type `CreateUserMappingStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2432>`__ to the `output` stream.

.. index:: DeallocateStmt

.. function:: deallocate_stmt(node, output)

   Pretty print a `node` of type `DeallocateStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3561>`__ to the `output` stream.

.. index:: DefineStmt

.. function:: define_stmt(node, output)

   Pretty print a `node` of type `DefineStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2665>`__ to the `output` stream.

.. index:: DefElem

.. function:: def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__ to the `output` stream.

.. index::
   pair: DefineStmt;DefElem

.. function:: define_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `DefineStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2665>`__, to the `output` stream.

.. index:: DiscardStmt

.. function:: discard_stmt(node, output)

   Pretty print a `node` of type `DiscardStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3437>`__ to the `output` stream.

.. index:: DoStmt

.. function:: do_stmt(node, output)

   Pretty print a `node` of type `DoStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2998>`__ to the `output` stream.

.. index:: DropdbStmt

.. function:: drop_db_stmt(node, output)

   Pretty print a `node` of type `DropdbStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3305>`__ to the `output` stream.

.. index:: DropOwnedStmt

.. function:: drop_owned_stmt(node, output)

   Pretty print a `node` of type `DropOwnedStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3571>`__ to the `output` stream.

.. index:: DropRoleStmt

.. function:: drop_role_stmt(node, output)

   Pretty print a `node` of type `DropRoleStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2630>`__ to the `output` stream.

.. index:: DropStmt

.. function:: drop_stmt(node, output)

   Pretty print a `node` of type `DropStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2751>`__ to the `output` stream.

.. index:: DropSubscriptionStmt

.. function:: drop_subscription_stmt(node, output)

   Pretty print a `node` of type `DropSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3681>`__ to the `output` stream.

.. index:: DropTableSpaceStmt

.. function:: drop_table_space_stmt(node, output)

   Pretty print a `node` of type `DropTableSpaceStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2314>`__ to the `output` stream.

.. index:: DropUserMappingStmt

.. function:: drop_user_mapping_stmt(node, output)

   Pretty print a `node` of type `DropUserMappingStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2449>`__ to the `output` stream.

.. index:: FunctionParameter

.. function:: function_parameter(node, output)

   Pretty print a `node` of type `FunctionParameter <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2975>`__ to the `output` stream.

.. index:: GrantStmt

.. function:: grant_stmt(node, output)

   Pretty print a `node` of type `GrantStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2011>`__ to the `output` stream.

.. index:: GrantRoleStmt

.. function:: grant_role_stmt(node, output)

   Pretty print a `node` of type `GrantRoleStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2076>`__ to the `output` stream.

.. index:: ImportForeignSchemaStmt

.. function:: import_foreign_schema_stmt(node, output)

   Pretty print a `node` of type `ImportForeignSchemaStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2469>`__ to the `output` stream.

.. index:: IndexStmt

.. function:: index_stmt(node, output)

   Pretty print a `node` of type `IndexStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2873>`__ to the `output` stream.

.. index:: LockStmt

.. function:: lock_stmt(node, output)

   Pretty print a `node` of type `LockStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3447>`__ to the `output` stream.

.. index:: NotifyStmt

.. function:: notify_stmt(node, output)

   Pretty print a `node` of type `NotifyStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3137>`__ to the `output` stream.

.. index:: ObjectWithArgs

.. function:: object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2044>`__ to the `output` stream.

.. index::
   pair: AlterObjectSchemaStmt;ObjectWithArgs

.. function:: alter_object_schema_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2044>`__, when it is inside a `AlterObjectSchemaStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3072>`__, to the `output` stream.

.. index::
   pair: AlterOperatorStmt;ObjectWithArgs

.. function:: alter_operator_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2044>`__, when it is inside a `AlterOperatorStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3099>`__, to the `output` stream.

.. index::
   pair: AlterOwnerStmt;ObjectWithArgs

.. function:: alter_owner_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2044>`__, when it is inside a `AlterOwnerStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3086>`__, to the `output` stream.

.. index::
   pair: CommentStmt;ObjectWithArgs

.. function:: comment_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2044>`__, when it is inside a `CommentStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2777>`__, to the `output` stream.

.. index::
   pair: DropStmt;ObjectWithArgs

.. function:: drop_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2044>`__, when it is inside a `DropStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2751>`__, to the `output` stream.

.. index:: PartitionBoundSpec

.. function:: partition_bound_spec(node, output)

   Pretty print a `node` of type `PartitionBoundSpec <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L824>`__ to the `output` stream.

.. index:: PartitionCmd

.. function:: partition_cmd(node, output)

   Pretty print a `node` of type `PartitionCmd <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L871>`__ to the `output` stream.

.. index:: PartitionElem

.. function:: partition_elem(node, output)

   Pretty print a `node` of type `PartitionElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L789>`__ to the `output` stream.

.. index:: PartitionRangeDatum

.. function:: partition_range_datum(node, output)

   Pretty print a `node` of type `PartitionRangeDatum <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L857>`__ to the `output` stream.

.. index:: PartitionSpec

.. function:: partition_spec(node, output)

   Pretty print a `node` of type `PartitionSpec <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L804>`__ to the `output` stream.

.. index:: ReindexStmt

.. function:: reindex_stmt(node, output)

   Pretty print a `node` of type `ReindexStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3479>`__ to the `output` stream.

.. index::
   pair: ReindexStmt;DefElem

.. function:: reindex_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `ReindexStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3479>`__, to the `output` stream.

.. index:: RenameStmt

.. function:: rename_stmt(node, output)

   Pretty print a `node` of type `RenameStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3040>`__ to the `output` stream.

.. index::
   pair: RenameStmt;RangeVar

.. function:: rename_stmt_range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L63>`__, when it is inside a `RenameStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3040>`__, to the `output` stream.

.. index:: ReplicaIdentityStmt

.. function:: replica_identity_stmt(node, output)

   Pretty print a `node` of type `ReplicaIdentityStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1939>`__ to the `output` stream.

.. index:: RoleSpec

.. function:: role_spec(node, output)

   Pretty print a `node` of type `RoleSpec <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L336>`__ to the `output` stream.

.. index:: RuleStmt

.. function:: rule_stmt_printer(node, output)

   Pretty print a `node` of type `RuleStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3121>`__ to the `output` stream.

.. index:: RefreshMatViewStmt

.. function:: refresh_mat_view_stmt(node, output)

   Pretty print a `node` of type `RefreshMatViewStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3407>`__ to the `output` stream.

.. index:: ReassignOwnedStmt

.. function:: reassign_owned_stmt(node, output)

   Pretty print a `node` of type `ReassignOwnedStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3581>`__ to the `output` stream.

.. index:: ReturnStmt

.. function:: return_stmt(node, output)

   Pretty print a `node` of type `ReturnStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1729>`__ to the `output` stream.

.. index:: SecLabelStmt

.. function:: sec_label_stmt(node, output)

   Pretty print a `node` of type `SecLabelStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2789>`__ to the `output` stream.

.. index:: StatsElem

.. function:: stats_elem(node, output)

   Pretty print a `node` of type `StatsElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2927>`__ to the `output` stream.

.. index:: TableLikeClause

.. function:: table_like_clause(node, output)

   Pretty print a `node` of type `TableLikeClause <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L682>`__ to the `output` stream.

.. index:: TriggerTransition

.. function:: trigger_transition(node, output)

   Pretty print a `node` of type `TriggerTransition <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1533>`__ to the `output` stream.

.. index:: VacuumStmt

.. function:: vacuum_stmt(node, output)

   Pretty print a `node` of type `VacuumStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3342>`__ to the `output` stream.

.. index::
   pair: VacuumStmt;DefElem

.. function:: vacuum_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `VacuumStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3342>`__, to the `output` stream.

.. index:: VacuumRelation

.. function:: vacuum_relation(node, output)

   Pretty print a `node` of type `VacuumRelation <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3357>`__ to the `output` stream.

.. index:: VariableSetStmt

.. function:: variable_set_stmt(node, output)

   Pretty print a `node` of type `VariableSetStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2138>`__ to the `output` stream.

.. index:: VariableShowStmt

.. function:: variable_show_statement(node, output)

   Pretty print a `node` of type `VariableShowStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2151>`__ to the `output` stream.

.. index:: ViewStmt

.. function:: view_stmt(node, output)

   Pretty print a `node` of type `ViewStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3251>`__ to the `output` stream.

.. index::
   pair: ViewStmt;DefElem

.. function:: view_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__, when it is inside a `ViewStmt <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3251>`__, to the `output` stream.
