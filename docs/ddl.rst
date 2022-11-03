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

   Pretty print a `node` of type `AccessPriv <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1968>`__ to the `output` stream.

.. index:: AlterCollationStmt

.. function:: alter_collation_stmt(node, output)

   Pretty print a `node` of type `AlterCollationStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1887>`__ to the `output` stream.

.. index:: AlterDatabaseStmt

.. function:: alter_database_stmt(node, output)

   Pretty print a `node` of type `AlterDatabaseStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3168>`__ to the `output` stream.

.. index:: AlterDatabaseSetStmt

.. function:: alter_database_set_stmt(node, output)

   Pretty print a `node` of type `AlterDatabaseSetStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3175>`__ to the `output` stream.

.. index:: AlterExtensionStmt

.. function:: alter_extension_stmt(node, output)

   Pretty print a `node` of type `AlterExtensionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2261>`__ to the `output` stream.

.. index::
   pair: AlterExtensionStmt;DefElem

.. function:: alter_extension_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `AlterExtensionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2261>`__, to the `output` stream.

.. index:: AlterExtensionContentsStmt

.. function:: alter_extension_contents_stmt(node, output)

   Pretty print a `node` of type `AlterExtensionContentsStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2268>`__ to the `output` stream.

.. index:: AlterEnumStmt

.. function:: alter_enum_stmt(node, output)

   Pretty print a `node` of type `AlterEnumStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3110>`__ to the `output` stream.

.. index:: AlterDefaultPrivilegesStmt

.. function:: alter_default_privileges_stmt(node, output)

   Pretty print a `node` of type `AlterDefaultPrivilegesStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1999>`__ to the `output` stream.

.. index:: AlterFunctionStmt

.. function:: alter_function_stmt(node, output)

   Pretty print a `node` of type `AlterFunctionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2871>`__ to the `output` stream.

.. index:: AlterObjectSchemaStmt

.. function:: alter_object_schema_stmt(node, output)

   Pretty print a `node` of type `AlterObjectSchemaStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2953>`__ to the `output` stream.

.. index:: AlterOperatorStmt

.. function:: alter_operator_stmt(node, output)

   Pretty print a `node` of type `AlterOperatorStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2980>`__ to the `output` stream.

.. index::
   pair: AlterOperatorStmt;DefElem

.. function:: alter_operator_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `AlterOperatorStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2980>`__, to the `output` stream.

.. index:: AlterOpFamilyStmt

.. function:: alter_op_family_stmt(node, output)

   Pretty print a `node` of type `AlterOpFamilyStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2644>`__ to the `output` stream.

.. index:: AlterOwnerStmt

.. function:: alter_owner_stmt(node, output)

   Pretty print a `node` of type `AlterOwnerStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2967>`__ to the `output` stream.

.. index:: AlterPolicyStmt

.. function:: alter_policy_stmt(node, output)

   Pretty print a `node` of type `AlterPolicyStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2408>`__ to the `output` stream.

.. index:: AlterRoleStmt

.. function:: alter_role_stmt(node, output)

   Pretty print a `node` of type `AlterRoleStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2521>`__ to the `output` stream.

.. index:: AlterSeqStmt

.. function:: alter_seq_stmt(node, output)

   Pretty print a `node` of type `AlterSeqStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2559>`__ to the `output` stream.

.. index:: AlterTableStmt

.. function:: alter_table_stmt(node, output)

   Pretty print a `node` of type `AlterTableStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1779>`__ to the `output` stream.

.. index::
   pair: AlterTableStmt;RangeVar

.. function:: range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/primnodes.h#L63>`__, when it is inside a `AlterTableStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1779>`__, to the `output` stream.

.. index:: AlterTableCmd

.. function:: alter_table_cmd(node, output)

   Pretty print a `node` of type `AlterTableCmd <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1866>`__ to the `output` stream.

.. index::
   pair: AlterTableCmd;DefElem

.. function:: alter_table_cmd_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `AlterTableCmd <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1866>`__, to the `output` stream.

.. index::
   pair: CreatePublicationStmt;DefElem

.. function:: alter_table_cmd_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreatePublicationStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3521>`__, to the `output` stream.

.. index::
   pair: CreateStmt;DefElem

.. function:: alter_table_cmd_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2076>`__, to the `output` stream.

.. index::
   pair: IndexStmt;DefElem

.. function:: alter_table_cmd_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `IndexStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2779>`__, to the `output` stream.

.. index::
   pair: IntoClause;DefElem

.. function:: alter_table_cmd_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `IntoClause <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/primnodes.h#L108>`__, to the `output` stream.

.. index:: AlterTSConfigurationStmt

.. function:: alter_ts_configuration_stmt(node, output)

   Pretty print a `node` of type `AlterTSConfigurationStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3503>`__ to the `output` stream.

.. index:: AlterTSDictionaryStmt

.. function:: alter_ts_dictionary_stmt(node, output)

   Pretty print a `node` of type `AlterTSDictionaryStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3484>`__ to the `output` stream.

.. index:: AlterStatsStmt

.. function:: alter_stats_stmt(node, output)

   Pretty print a `node` of type `AlterStatsStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2829>`__ to the `output` stream.

.. index:: AlterSubscriptionStmt

.. function:: alter_subscription_stmt(node, output)

   Pretty print a `node` of type `AlterSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3562>`__ to the `output` stream.

.. index:: AlterPublicationStmt

.. function:: alter_publication_stmt(node, output)

   Pretty print a `node` of type `AlterPublicationStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3530>`__ to the `output` stream.

.. index:: AlterFdwStmt

.. function:: alter_fdw_stmt(node, output)

   Pretty print a `node` of type `AlterFdwStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2290>`__ to the `output` stream.

.. index::
   pair: AlterFdwStmt;DefElem

.. function:: alter_fdw_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `AlterFdwStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2290>`__, to the `output` stream.

.. index:: AlterForeignServerStmt

.. function:: alter_foreign_server_stmt(node, output)

   Pretty print a `node` of type `AlterForeignServerStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2314>`__ to the `output` stream.

.. index:: AlterUserMappingStmt

.. function:: alter_user_mapping_stmt(node, output)

   Pretty print a `node` of type `AlterUserMappingStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2349>`__ to the `output` stream.

.. index:: AlterRoleSetStmt

.. function:: alter_role_set_stmt(node, output)

   Pretty print a `node` of type `AlterRoleSetStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2529>`__ to the `output` stream.

.. index:: AlterDomainStmt

.. function:: alter_domain_stmt(node, output)

   Pretty print a `node` of type `AlterDomainStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1901>`__ to the `output` stream.

.. index:: AlterEventTrigStmt

.. function:: alter_event_trig_stmt(node, output)

   Pretty print a `node` of type `AlterEventTrigStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2474>`__ to the `output` stream.

.. index:: AlterTypeStmt

.. function:: alter_type_stmt(node, output)

   Pretty print a `node` of type `AlterTypeStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2991>`__ to the `output` stream.

.. index:: CheckPointStmt

.. function:: check_point_stmt(node, output)

   Pretty print a `node` of type `CheckPointStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3306>`__ to the `output` stream.

.. index:: ClusterStmt

.. function:: cluster_stmt(node, output)

   Pretty print a `node` of type `ClusterStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3214>`__ to the `output` stream.

.. index:: ColumnDef

.. function:: column_def(node, output)

   Pretty print a `node` of type `ColumnDef <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L644>`__ to the `output` stream.

.. index:: CommentStmt

.. function:: comment_stmt(node, output)

   Pretty print a `node` of type `CommentStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2684>`__ to the `output` stream.

.. index:: CompositeTypeStmt

.. function:: composite_type_stmt(node, output)

   Pretty print a `node` of type `CompositeTypeStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3077>`__ to the `output` stream.

.. index::
   pair: CompositeTypeStmt;RangeVar

.. function:: composite_type_stmt_range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/primnodes.h#L63>`__, when it is inside a `CompositeTypeStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3077>`__, to the `output` stream.

.. index:: Constraint

.. function:: constraint(node, output)

   Pretty print a `node` of type `Constraint <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2156>`__ to the `output` stream.

.. index:: CreateAmStmt

.. function:: create_am_stmt(node, output)

   Pretty print a `node` of type `CreateAmStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2422>`__ to the `output` stream.

.. index:: CreatedbStmt

.. function:: create_db_stmt(node, output)

   Pretty print a `node` of type `CreatedbStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3157>`__ to the `output` stream.

.. index::
   pair: CreatedbStmt;DefElem

.. function:: create_db_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreatedbStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3157>`__, to the `output` stream.

.. index:: CreateCastStmt

.. function:: create_cast_stmt(node, output)

   Pretty print a `node` of type `CreateCastStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3400>`__ to the `output` stream.

.. index:: CreateConversionStmt

.. function:: create_conversion_stmt(node, output)

   Pretty print a `node` of type `CreateConversionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3386>`__ to the `output` stream.

.. index:: CreateDomainStmt

.. function:: create_domain_stmt(node, output)

   Pretty print a `node` of type `CreateDomainStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2588>`__ to the `output` stream.

.. index:: CreateEnumStmt

.. function:: create_enum_stmt(node, output)

   Pretty print a `node` of type `CreateEnumStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3088>`__ to the `output` stream.

.. index:: CreateEventTrigStmt

.. function:: create_event_trig_stmt(node, output)

   Pretty print a `node` of type `CreateEventTrigStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2461>`__ to the `output` stream.

.. index::
   pair: CreateEventTrigStmt;DefElem

.. function:: create_event_trig_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateEventTrigStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2461>`__, to the `output` stream.

.. index:: CreateExtensionStmt

.. function:: create_extension_stmt(node, output)

   Pretty print a `node` of type `CreateExtensionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2252>`__ to the `output` stream.

.. index::
   pair: CreateExtensionStmt;DefElem

.. function:: create_extension_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateExtensionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2252>`__, to the `output` stream.

.. index:: CreateFdwStmt

.. function:: create_fdw_stmt(node, output)

   Pretty print a `node` of type `CreateFdwStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2282>`__ to the `output` stream.

.. index::
   pair: ColumnDef;DefElem

.. function:: create_fdw_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `ColumnDef <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L644>`__, to the `output` stream.

.. index::
   pair: CreateUserMappingStmt;DefElem

.. function:: create_fdw_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateUserMappingStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2340>`__, to the `output` stream.

.. index::
   pair: CreateFdwStmt;DefElem

.. function:: create_fdw_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateFdwStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2282>`__, to the `output` stream.

.. index:: CreateForeignServerStmt

.. function:: create_foreign_server_stmt(node, output)

   Pretty print a `node` of type `CreateForeignServerStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2303>`__ to the `output` stream.

.. index:: CreateForeignTableStmt

.. function:: create_foreign_table_stmt(node, output)

   Pretty print a `node` of type `CreateForeignTableStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2328>`__ to the `output` stream.

.. index::
   pair: CreateForeignTableStmt;DefElem

.. function:: create_foreign_table_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateForeignTableStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2328>`__, to the `output` stream.

.. index::
   pair: CreateForeignServerStmt;DefElem

.. function:: create_foreign_table_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateForeignServerStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2303>`__, to the `output` stream.

.. index:: CreateFunctionStmt

.. function:: create_function_stmt(node, output)

   Pretty print a `node` of type `CreateFunctionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2841>`__ to the `output` stream.

.. index::
   pair: AlterFunctionStmt;DefElem

.. index::
   pair: CreateFunctionStmt;DefElem

.. index::
   pair: DoStmt;DefElem

.. function:: create_function_option(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `AlterFunctionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2871>`__ or a `CreateFunctionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2841>`__ or a `DoStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2885>`__, to the `output` stream.

.. index:: CreateOpClassStmt

.. function:: create_opclass_stmt(node, output)

   Pretty print a `node` of type `CreateOpClassStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2601>`__ to the `output` stream.

.. index:: CreateOpClassItem

.. function:: create_opclass_item(node, output)

   Pretty print a `node` of type `CreateOpClassItem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2616>`__ to the `output` stream.

.. index:: CreateOpFamilyStmt

.. function:: create_op_family_stmt(node, output)

   Pretty print a `node` of type `CreateOpFamilyStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2633>`__ to the `output` stream.

.. index:: CreatePLangStmt

.. function:: create_plang_stmt(node, output)

   Pretty print a `node` of type `CreatePLangStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2486>`__ to the `output` stream.

.. index:: CreatePolicyStmt

.. function:: create_policy_stmt(node, output)

   Pretty print a `node` of type `CreatePolicyStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2392>`__ to the `output` stream.

.. index:: CreatePublicationStmt

.. function:: create_publication_stmt(node, output)

   Pretty print a `node` of type `CreatePublicationStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3521>`__ to the `output` stream.

.. index::
   pair: CreatePublicationStmt;RangeVar

.. function:: create_publication_stmt_range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/primnodes.h#L63>`__, when it is inside a `CreatePublicationStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3521>`__, to the `output` stream.

.. index:: CreateRangeStmt

.. function:: create_range_stmt(node, output)

   Pretty print a `node` of type `CreateRangeStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3099>`__ to the `output` stream.

.. index:: CreateRoleStmt

.. function:: create_role_stmt(node, output)

   Pretty print a `node` of type `CreateRoleStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2513>`__ to the `output` stream.

.. index::
   pair: AlterRoleStmt;DefElem

.. function:: create_or_alter_role_option(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `AlterRoleStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2521>`__, to the `output` stream.

.. index::
   pair: CreateRoleStmt;DefElem

.. function:: create_or_alter_role_option(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateRoleStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2513>`__, to the `output` stream.

.. index:: CreateSchemaStmt

.. function:: create_schema_stmt(node, output)

   Pretty print a `node` of type `CreateSchemaStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1760>`__ to the `output` stream.

.. index:: CreateSeqStmt

.. function:: create_seq_stmt(node, output)

   Pretty print a `node` of type `CreateSeqStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2549>`__ to the `output` stream.

.. index::
   pair: Constraint;DefElem

.. function:: create_seq_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `Constraint <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2156>`__, to the `output` stream.

.. index::
   pair: CreateSeqStmt;DefElem

.. function:: create_seq_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateSeqStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2549>`__, to the `output` stream.

.. index::
   pair: AlterSeqStmt;DefElem

.. function:: create_seq_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `AlterSeqStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2559>`__, to the `output` stream.

.. index:: CreateStatsStmt

.. function:: create_stats_stmt(node, output)

   Pretty print a `node` of type `CreateStatsStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2814>`__ to the `output` stream.

.. index:: CreateStmt

.. function:: create_stmt(node, output)

   Pretty print a `node` of type `CreateStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2076>`__ to the `output` stream.

.. index:: CreateTableAsStmt

.. function:: create_table_as_stmt(node, output)

   Pretty print a `node` of type `CreateTableAsStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3280>`__ to the `output` stream.

.. index:: CreateTableSpaceStmt

.. function:: create_table_space_stmt(node, output)

   Pretty print a `node` of type `CreateTableSpaceStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2213>`__ to the `output` stream.

.. index:: CreateTrigStmt

.. function:: create_trig_stmt(node, output)

   Pretty print a `node` of type `CreateTrigStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2434>`__ to the `output` stream.

.. index::
   pair: AlterSubscriptionStmt;DefElem

.. function:: create_subscription_stmt_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `AlterSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3562>`__, to the `output` stream.

.. index::
   pair: CreateSubscriptionStmt;DefElem

.. function:: create_subscription_stmt_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CreateSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3544>`__, to the `output` stream.

.. index:: CreateSubscriptionStmt

.. function:: create_subscription_stmt(node, output)

   Pretty print a `node` of type `CreateSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3544>`__ to the `output` stream.

.. index:: CurrentOfExpr

.. function:: current_of_expr(node, output)

   Pretty print a `node` of type `CurrentOfExpr <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/primnodes.h#L1313>`__ to the `output` stream.

.. index:: CreateTransformStmt

.. function:: create_transform_stmt(node, output)

   Pretty print a `node` of type `CreateTransformStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3414>`__ to the `output` stream.

.. index:: ClosePortalStmt

.. function:: close_portal_stmt(node, output)

   Pretty print a `node` of type `ClosePortalStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2736>`__ to the `output` stream.

.. index:: CreateUserMappingStmt

.. function:: create_user_mapping_stmt(node, output)

   Pretty print a `node` of type `CreateUserMappingStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2340>`__ to the `output` stream.

.. index:: DeallocateStmt

.. function:: deallocate_stmt(node, output)

   Pretty print a `node` of type `DeallocateStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3454>`__ to the `output` stream.

.. index:: DefineStmt

.. function:: define_stmt(node, output)

   Pretty print a `node` of type `DefineStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2572>`__ to the `output` stream.

.. index:: DefElem

.. function:: def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__ to the `output` stream.

.. index::
   pair: DefineStmt;DefElem

.. function:: define_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `DefineStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2572>`__, to the `output` stream.

.. index:: DiscardStmt

.. function:: discard_stmt(node, output)

   Pretty print a `node` of type `DiscardStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3324>`__ to the `output` stream.

.. index:: DoStmt

.. function:: do_stmt(node, output)

   Pretty print a `node` of type `DoStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2885>`__ to the `output` stream.

.. index:: DropdbStmt

.. function:: drop_db_stmt(node, output)

   Pretty print a `node` of type `DropdbStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3186>`__ to the `output` stream.

.. index:: DropOwnedStmt

.. function:: drop_owned_stmt(node, output)

   Pretty print a `node` of type `DropOwnedStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3464>`__ to the `output` stream.

.. index:: DropRoleStmt

.. function:: drop_role_stmt(node, output)

   Pretty print a `node` of type `DropRoleStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2537>`__ to the `output` stream.

.. index:: DropStmt

.. function:: drop_stmt(node, output)

   Pretty print a `node` of type `DropStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2658>`__ to the `output` stream.

.. index:: DropSubscriptionStmt

.. function:: drop_subscription_stmt(node, output)

   Pretty print a `node` of type `DropSubscriptionStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3572>`__ to the `output` stream.

.. index:: DropTableSpaceStmt

.. function:: drop_table_space_stmt(node, output)

   Pretty print a `node` of type `DropTableSpaceStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2222>`__ to the `output` stream.

.. index:: DropUserMappingStmt

.. function:: drop_user_mapping_stmt(node, output)

   Pretty print a `node` of type `DropUserMappingStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2357>`__ to the `output` stream.

.. index:: FunctionParameter

.. function:: function_parameter(node, output)

   Pretty print a `node` of type `FunctionParameter <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2862>`__ to the `output` stream.

.. index:: GrantStmt

.. function:: grant_stmt(node, output)

   Pretty print a `node` of type `GrantStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1931>`__ to the `output` stream.

.. index:: GrantRoleStmt

.. function:: grant_role_stmt(node, output)

   Pretty print a `node` of type `GrantRoleStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1984>`__ to the `output` stream.

.. index:: ImportForeignSchemaStmt

.. function:: import_foreign_schema_stmt(node, output)

   Pretty print a `node` of type `ImportForeignSchemaStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2377>`__ to the `output` stream.

.. index:: IndexStmt

.. function:: index_stmt(node, output)

   Pretty print a `node` of type `IndexStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2779>`__ to the `output` stream.

.. index:: LockStmt

.. function:: lock_stmt(node, output)

   Pretty print a `node` of type `LockStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3334>`__ to the `output` stream.

.. index:: NotifyStmt

.. function:: notify_stmt(node, output)

   Pretty print a `node` of type `NotifyStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3018>`__ to the `output` stream.

.. index:: ObjectWithArgs

.. function:: object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1951>`__ to the `output` stream.

.. index::
   pair: AlterObjectSchemaStmt;ObjectWithArgs

.. function:: alter_object_schema_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1951>`__, when it is inside a `AlterObjectSchemaStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2953>`__, to the `output` stream.

.. index::
   pair: AlterOperatorStmt;ObjectWithArgs

.. function:: alter_operator_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1951>`__, when it is inside a `AlterOperatorStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2980>`__, to the `output` stream.

.. index::
   pair: AlterOwnerStmt;ObjectWithArgs

.. function:: alter_owner_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1951>`__, when it is inside a `AlterOwnerStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2967>`__, to the `output` stream.

.. index::
   pair: CommentStmt;ObjectWithArgs

.. function:: comment_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1951>`__, when it is inside a `CommentStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2684>`__, to the `output` stream.

.. index::
   pair: DropStmt;ObjectWithArgs

.. function:: drop_stmt_object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1951>`__, when it is inside a `DropStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2658>`__, to the `output` stream.

.. index:: PartitionBoundSpec

.. function:: partition_bound_spec(node, output)

   Pretty print a `node` of type `PartitionBoundSpec <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L811>`__ to the `output` stream.

.. index:: PartitionCmd

.. function:: partition_cmd(node, output)

   Pretty print a `node` of type `PartitionCmd <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L858>`__ to the `output` stream.

.. index:: PartitionElem

.. function:: partition_elem(node, output)

   Pretty print a `node` of type `PartitionElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L776>`__ to the `output` stream.

.. index:: PartitionRangeDatum

.. function:: partition_range_datum(node, output)

   Pretty print a `node` of type `PartitionRangeDatum <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L844>`__ to the `output` stream.

.. index:: PartitionSpec

.. function:: partition_spec(node, output)

   Pretty print a `node` of type `PartitionSpec <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L791>`__ to the `output` stream.

.. index:: ReindexStmt

.. function:: reindex_stmt(node, output)

   Pretty print a `node` of type `ReindexStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3371>`__ to the `output` stream.

.. index:: RenameStmt

.. function:: rename_stmt(node, output)

   Pretty print a `node` of type `RenameStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2921>`__ to the `output` stream.

.. index::
   pair: RenameStmt;RangeVar

.. function:: rename_stmt_range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/primnodes.h#L63>`__, when it is inside a `RenameStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2921>`__, to the `output` stream.

.. index:: ReplicaIdentityStmt

.. function:: replica_identity_stmt(node, output)

   Pretty print a `node` of type `ReplicaIdentityStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1859>`__ to the `output` stream.

.. index:: RoleSpec

.. function:: role_spec(node, output)

   Pretty print a `node` of type `RoleSpec <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L326>`__ to the `output` stream.

.. index:: RuleStmt

.. function:: rule_stmt_printer(node, output)

   Pretty print a `node` of type `RuleStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3002>`__ to the `output` stream.

.. index:: RefreshMatViewStmt

.. function:: refresh_mat_view_stmt(node, output)

   Pretty print a `node` of type `RefreshMatViewStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3294>`__ to the `output` stream.

.. index:: ReassignOwnedStmt

.. function:: reassign_owned_stmt(node, output)

   Pretty print a `node` of type `ReassignOwnedStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3474>`__ to the `output` stream.

.. index:: SecLabelStmt

.. function:: sec_label_stmt(node, output)

   Pretty print a `node` of type `SecLabelStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2696>`__ to the `output` stream.

.. index:: TableLikeClause

.. function:: table_like_clause(node, output)

   Pretty print a `node` of type `TableLikeClause <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L670>`__ to the `output` stream.

.. index:: TriggerTransition

.. function:: trigger_transition(node, output)

   Pretty print a `node` of type `TriggerTransition <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L1486>`__ to the `output` stream.

.. index:: VacuumStmt

.. function:: vacuum_stmt(node, output)

   Pretty print a `node` of type `VacuumStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3229>`__ to the `output` stream.

.. index::
   pair: VacuumStmt;DefElem

.. function:: vacuum_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `VacuumStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3229>`__, to the `output` stream.

.. index:: VacuumRelation

.. function:: vacuum_relation(node, output)

   Pretty print a `node` of type `VacuumRelation <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3244>`__ to the `output` stream.

.. index:: VariableShowStmt

.. function:: variable_show_statement(node, output)

   Pretty print a `node` of type `VariableShowStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L2059>`__ to the `output` stream.

.. index:: ViewStmt

.. function:: view_stmt(node, output)

   Pretty print a `node` of type `ViewStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3132>`__ to the `output` stream.

.. index::
   pair: ViewStmt;DefElem

.. function:: view_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `ViewStmt <https://github.com/pganalyze/libpg_query/blob/1097b2c/src/postgres/include/nodes/parsenodes.h#L3132>`__, to the `output` stream.
