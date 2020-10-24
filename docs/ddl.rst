.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2020 Lele Gaifax
..

======================================================
 :mod:`pglast.printers.ddl` --- DDL printer functions
======================================================

.. module:: pglast.printers.ddl
   :synopsis: DDL printer functions

.. index:: AccessPriv

.. function:: access_priv(node, output)

   Pretty print a `node` of type `AccessPriv <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1938>`__ to the `output` stream.

.. index:: AlterDatabaseStmt

.. function:: alter_database_stmt(node, output)

   Pretty print a `node` of type `AlterDatabaseStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3113>`__ to the `output` stream.

.. index:: AlterDatabaseSetStmt

.. function:: alter_database_set_stmt(node, output)

   Pretty print a `node` of type `AlterDatabaseSetStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3120>`__ to the `output` stream.

.. index:: AlterEnumStmt

.. function:: alter_enum_stmt(node, output)

   Pretty print a `node` of type `AlterEnumStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3055>`__ to the `output` stream.

.. index:: AlterDefaultPrivilegesStmt

.. function:: alter_default_privileges_stmt(node, output)

   Pretty print a `node` of type `AlterDefaultPrivilegesStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1969>`__ to the `output` stream.

.. index:: AlterFunctionStmt

.. function:: alter_function_stmt(node, output)

   Pretty print a `node` of type `AlterFunctionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2826>`__ to the `output` stream.

.. index:: AlterObjectSchemaStmt

.. function:: alter_object_schema_stmt(node, output)

   Pretty print a `node` of type `AlterObjectSchemaStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2907>`__ to the `output` stream.

.. index:: AlterOwnerStmt

.. function:: alter_owner_stmt(node, output)

   Pretty print a `node` of type `AlterOwnerStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2921>`__ to the `output` stream.

.. index:: AlterRoleStmt

.. function:: alter_role_stmt(node, output)

   Pretty print a `node` of type `AlterRoleStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2491>`__ to the `output` stream.

.. index:: AlterSeqStmt

.. function:: alter_seq_stmt(node, output)

   Pretty print a `node` of type `AlterSeqStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2529>`__ to the `output` stream.

.. index:: AlterTableStmt

.. function:: alter_table_stmt(node, output)

   Pretty print a `node` of type `AlterTableStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1750>`__ to the `output` stream.

.. index:: AlterTableCmd

.. function:: alter_table_cmd(node, output)

   Pretty print a `node` of type `AlterTableCmd <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1837>`__ to the `output` stream.

.. index:: ClusterStmt

.. function:: cluster_stmt(node, output)

   Pretty print a `node` of type `ClusterStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3158>`__ to the `output` stream.

.. index:: ColumnDef

.. function:: column_def(node, output)

   Pretty print a `node` of type `ColumnDef <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L643>`__ to the `output` stream.

.. index:: CommentStmt

.. function:: comment_stmt(node, output)

   Pretty print a `node` of type `CommentStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2654>`__ to the `output` stream.

.. index:: CompositeTypeStmt

.. function:: composite_type_stmt(node, output)

   Pretty print a `node` of type `CompositeTypeStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3022>`__ to the `output` stream.

.. index:: Constraint

.. function:: constraint(node, output)

   Pretty print a `node` of type `Constraint <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2126>`__ to the `output` stream.

.. index:: CreateAmStmt

.. function:: create_am_stmt(node, output)

   Pretty print a `node` of type `CreateAmStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2392>`__ to the `output` stream.

.. index:: CreatedbStmt

.. function:: create_db_stmt(node, output)

   Pretty print a `node` of type `CreatedbStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3102>`__ to the `output` stream.

.. index::
   pair: CreatedbStmt;DefElem

.. function:: create_db_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `CreatedbStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3102>`__, to the `output` stream.

.. index:: CreateCastStmt

.. function:: create_cast_stmt(node, output)

   Pretty print a `node` of type `CreateCastStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3344>`__ to the `output` stream.

.. index:: CreateConversionStmt

.. function:: create_conversion_stmt(node, output)

   Pretty print a `node` of type `CreateConversionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3330>`__ to the `output` stream.

.. index:: CreateDomainStmt

.. function:: create_domain_stmt(node, output)

   Pretty print a `node` of type `CreateDomainStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2558>`__ to the `output` stream.

.. index:: CreateEnumStmt

.. function:: create_enum_stmt(node, output)

   Pretty print a `node` of type `CreateEnumStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3033>`__ to the `output` stream.

.. index:: CreateEventTrigStmt

.. function:: create_event_trig_stmt(node, output)

   Pretty print a `node` of type `CreateEventTrigStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2431>`__ to the `output` stream.

.. index::
   pair: CreateEventTrigStmt;DefElem

.. function:: create_event_trig_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `CreateEventTrigStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2431>`__, to the `output` stream.

.. index:: CreateExtensionStmt

.. function:: create_extension_stmt(node, output)

   Pretty print a `node` of type `CreateExtensionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2222>`__ to the `output` stream.

.. index::
   pair: CreateExtensionStmt;DefElem

.. function:: create_extension_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `CreateExtensionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2222>`__, to the `output` stream.

.. index:: CreateFdwStmt

.. function:: create_fdw_stmt(node, output)

   Pretty print a `node` of type `CreateFdwStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2252>`__ to the `output` stream.

.. index::
   pair: CreateFdwStmt;DefElem

.. function:: create_fdw_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `CreateFdwStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2252>`__, to the `output` stream.

.. index:: CreateForeignTableStmt

.. function:: create_foreign_table_stmt(node, output)

   Pretty print a `node` of type `CreateForeignTableStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2298>`__ to the `output` stream.

.. index::
   pair: CreateForeignTableStmt;DefElem

.. function:: create_foreign_table_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `CreateForeignTableStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2298>`__, to the `output` stream.

.. index:: CreateFunctionStmt

.. function:: create_function_stmt(node, output)

   Pretty print a `node` of type `CreateFunctionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2796>`__ to the `output` stream.

.. index::
   pair: AlterFunctionStmt;DefElem

.. index::
   pair: CreateFunctionStmt;DefElem

.. index::
   pair: DoStmt;DefElem

.. function:: create_function_option(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `AlterFunctionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2826>`__ or a `CreateFunctionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2796>`__ or a `DoStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2840>`__, to the `output` stream.

.. index:: CreateOpClassStmt

.. function:: create_opclass_stmt(node, output)

   Pretty print a `node` of type `CreateOpClassStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2571>`__ to the `output` stream.

.. index:: CreateOpClassItem

.. function:: create_opclass_item(node, output)

   Pretty print a `node` of type `CreateOpClassItem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2586>`__ to the `output` stream.

.. index:: CreatePLangStmt

.. function:: create_plang_stmt(node, output)

   Pretty print a `node` of type `CreatePLangStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2456>`__ to the `output` stream.

.. index:: CreatePolicyStmt

.. function:: create_policy_stmt(node, output)

   Pretty print a `node` of type `CreatePolicyStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2362>`__ to the `output` stream.

.. index:: AlterPolicyStmt

.. function:: create_policy_stmt(node, output)

   Pretty print a `node` of type `AlterPolicyStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2378>`__ to the `output` stream.

.. index:: CreateSchemaStmt

.. function:: create_schema_stmt(node, output)

   Pretty print a `node` of type `CreateSchemaStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1731>`__ to the `output` stream.

.. index:: CreateSeqStmt

.. function:: create_seq_stmt(node, output)

   Pretty print a `node` of type `CreateSeqStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2519>`__ to the `output` stream.

.. index::
   pair: CreateSeqStmt;DefElem

.. function:: create_seq_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `CreateSeqStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2519>`__, to the `output` stream.

.. index::
   pair: AlterSeqStmt;DefElem

.. function:: create_seq_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `AlterSeqStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2529>`__, to the `output` stream.

.. index:: CreateStmt

.. function:: create_stmt(node, output)

   Pretty print a `node` of type `CreateStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2046>`__ to the `output` stream.

.. index:: CreateTableAsStmt

.. function:: create_table_as_stmt(node, output)

   Pretty print a `node` of type `CreateTableAsStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3224>`__ to the `output` stream.

.. index:: CreateTrigStmt

.. function:: create_trig_stmt(node, output)

   Pretty print a `node` of type `CreateTrigStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2404>`__ to the `output` stream.

.. index:: DefineStmt

.. function:: define_stmt(node, output)

   Pretty print a `node` of type `DefineStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2542>`__ to the `output` stream.

.. index:: DefElem

.. function:: def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__ to the `output` stream.

.. index::
   pair: DefineStmt;DefElem

.. function:: define_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `DefineStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2542>`__, to the `output` stream.

.. index:: DiscardStmt

.. function:: discard_stmt(node, output)

   Pretty print a `node` of type `DiscardStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3268>`__ to the `output` stream.

.. index:: DoStmt

.. function:: do_stmt(node, output)

   Pretty print a `node` of type `DoStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2840>`__ to the `output` stream.

.. index:: DropdbStmt

.. function:: drop_db_stmt(node, output)

   Pretty print a `node` of type `DropdbStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3131>`__ to the `output` stream.

.. index:: DropOwnedStmt

.. function:: drop_owned_stmt(node, output)

   Pretty print a `node` of type `DropOwnedStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3408>`__ to the `output` stream.

.. index:: DropRoleStmt

.. function:: drop_role_stmt(node, output)

   Pretty print a `node` of type `DropRoleStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2507>`__ to the `output` stream.

.. index:: DropStmt

.. function:: drop_stmt(node, output)

   Pretty print a `node` of type `DropStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2628>`__ to the `output` stream.

.. index:: DropSubscriptionStmt

.. function:: drop_subscription_stmt(node, output)

   Pretty print a `node` of type `DropSubscriptionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3516>`__ to the `output` stream.

.. index:: DropTableSpaceStmt

.. function:: drop_table_space_stmt(node, output)

   Pretty print a `node` of type `DropTableSpaceStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2192>`__ to the `output` stream.

.. index:: DropUserMappingStmt

.. function:: drop_user_mapping_stmt(node, output)

   Pretty print a `node` of type `DropUserMappingStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2327>`__ to the `output` stream.

.. index:: FunctionParameter

.. function:: function_parameter(node, output)

   Pretty print a `node` of type `FunctionParameter <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2817>`__ to the `output` stream.

.. index:: GrantStmt

.. function:: grant_stmt(node, output)

   Pretty print a `node` of type `GrantStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1901>`__ to the `output` stream.

.. index:: GrantRoleStmt

.. function:: grant_role_stmt(node, output)

   Pretty print a `node` of type `GrantRoleStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1954>`__ to the `output` stream.

.. index:: IndexStmt

.. function:: index_stmt(node, output)

   Pretty print a `node` of type `IndexStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2749>`__ to the `output` stream.

.. index:: LockStmt

.. function:: lock_stmt(node, output)

   Pretty print a `node` of type `LockStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3278>`__ to the `output` stream.

.. index:: NotifyStmt

.. function:: notify_stmt(node, output)

   Pretty print a `node` of type `NotifyStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2963>`__ to the `output` stream.

.. index:: ObjectWithArgs

.. function:: object_with_args(node, output)

   Pretty print a `node` of type `ObjectWithArgs <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1921>`__ to the `output` stream.

.. index:: PartitionBoundSpec

.. function:: partition_bound_spec(node, output)

   Pretty print a `node` of type `PartitionBoundSpec <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L808>`__ to the `output` stream.

.. index:: PartitionElem

.. function:: partition_elem(node, output)

   Pretty print a `node` of type `PartitionElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L773>`__ to the `output` stream.

.. index:: PartitionRangeDatum

.. function:: partition_range_datum(node, output)

   Pretty print a `node` of type `PartitionRangeDatum <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L841>`__ to the `output` stream.

.. index:: PartitionSpec

.. function:: partition_spec(node, output)

   Pretty print a `node` of type `PartitionSpec <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L788>`__ to the `output` stream.

.. index:: RenameStmt

.. function:: rename_stmt(node, output)

   Pretty print a `node` of type `RenameStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2876>`__ to the `output` stream.

.. index:: RoleSpec

.. function:: role_spec(node, output)

   Pretty print a `node` of type `RoleSpec <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L325>`__ to the `output` stream.

.. index:: RuleStmt

.. function:: rule_stmt_printer(node, output)

   Pretty print a `node` of type `RuleStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2947>`__ to the `output` stream.

.. index:: TriggerTransition

.. function:: trigger_transition(node, output)

   Pretty print a `node` of type `TriggerTransition <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1458>`__ to the `output` stream.

.. index:: VacuumStmt

.. function:: vacuum_stmt(node, output)

   Pretty print a `node` of type `VacuumStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3173>`__ to the `output` stream.

.. index:: VacuumRelation

.. function:: vacuum_relation(node, output)

   Pretty print a `node` of type `VacuumRelation <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3188>`__ to the `output` stream.

.. index:: ViewStmt

.. function:: view_stmt(node, output)

   Pretty print a `node` of type `ViewStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3077>`__ to the `output` stream.
