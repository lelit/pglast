.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

========================================================
 :mod:`pg_query.printers.ddl` --- DDL printer functions
========================================================

.. module:: pg_query.printers.ddl

.. index:: ColumnDef

.. function:: column_def(node, output)

   Pretty print a `node` of type `ColumnDef <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L636>`__ to the `output` stream.

.. index:: Constraint

.. function:: constraint(node, output)

   Pretty print a `node` of type `Constraint <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2075>`__ to the `output` stream.

.. index:: CreateDomainStmt

.. function:: create_domain_stmt(node, output)

   Pretty print a `node` of type `CreateDomainStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2502>`__ to the `output` stream.

.. index:: CreateSchemaStmt

.. function:: create_schema_stmt(node, output)

   Pretty print a `node` of type `CreateSchemaStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1668>`__ to the `output` stream.

.. index:: CreateSeqStmt

.. function:: create_seq_stmt(node, output)

   Pretty print a `node` of type `CreateSeqStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2464>`__ to the `output` stream.

.. index:: DefElem

.. function:: create_seq_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L715>`__, when it is inside a `CreateSeqStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2464>`__, to the `output` stream.

.. index:: CreateStmt

.. function:: create_stmt(node, output)

   Pretty print a `node` of type `CreateStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1997>`__ to the `output` stream.

.. index:: CreatedbStmt

.. function:: createdb_stmt(node, output)

   Pretty print a `node` of type `CreatedbStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L3020>`__ to the `output` stream.

.. index:: DefElem

.. function:: def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L715>`__ to the `output` stream.

.. index:: IndexStmt

.. function:: index_stmt(node, output)

   Pretty print a `node` of type `IndexStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L2693>`__ to the `output` stream.

.. index:: PartitionBoundSpec

.. function:: partition_bound_spec(node, output)

   Pretty print a `node` of type `PartitionBoundSpec <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L795>`__ to the `output` stream.

.. index:: PartitionElem

.. function:: partition_elem(node, output)

   Pretty print a `node` of type `PartitionElem <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L762>`__ to the `output` stream.

.. index:: PartitionRangeDatum

.. function:: partition_range_datum(node, output)

   Pretty print a `node` of type `PartitionRangeDatum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L823>`__ to the `output` stream.

.. index:: PartitionSpec

.. function:: partition_spec(node, output)

   Pretty print a `node` of type `PartitionSpec <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L777>`__ to the `output` stream.

.. index:: RoleSpec

.. function:: role_spec(node, output)

   Pretty print a `node` of type `RoleSpec <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L324>`__ to the `output` stream.
