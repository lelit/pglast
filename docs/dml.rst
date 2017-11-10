.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

========================================================
 :mod:`pg_query.printers.dml` --- DML printer functions
========================================================

.. module:: pg_query.printers.dml

.. index:: A_ArrayExpr

.. function:: a_array_expr(node, output)

   Pretty print a `node` of type `A_ArrayExpr <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L411>`__ to the `output` stream.

.. index:: A_Const

.. function:: a_const(node, output)

   Pretty print a `node` of type `A_Const <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L284>`__ to the `output` stream.

.. index:: A_Expr

.. function:: a_expr(node, output)

   Pretty print a `node` of type `A_Expr <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L271>`__ to the `output` stream.

.. index:: A_Indices

.. function:: a_indices(node, output)

   Pretty print a `node` of type `A_Indices <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L378>`__ to the `output` stream.

.. index:: A_Indirection

.. function:: a_indirection(node, output)

   Pretty print a `node` of type `A_Indirection <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L401>`__ to the `output` stream.

.. index:: A_Star

.. function:: a_star(node, output)

   Pretty print a `node` of type `A_Star <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L367>`__ to the `output` stream.

.. index:: Alias

.. function:: alias(node, output)

   Pretty print a `node` of type `Alias <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L39>`__ to the `output` stream.

.. index:: BoolExpr

.. function:: bool_expr(node, output)

   Pretty print a `node` of type `BoolExpr <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L559>`__ to the `output` stream.

.. index:: CaseExpr

.. function:: case_expr(node, output)

   Pretty print a `node` of type `CaseExpr <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L903>`__ to the `output` stream.

.. index:: CaseWhen

.. function:: case_when(node, output)

   Pretty print a `node` of type `CaseWhen <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L917>`__ to the `output` stream.

.. index:: CoalesceExpr

.. function:: coalesce_expr(node, output)

   Pretty print a `node` of type `CoalesceExpr <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1042>`__ to the `output` stream.

.. index:: CollateClause

.. function:: collate_clause(node, output)

   Pretty print a `node` of type `CollateClause <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L305>`__ to the `output` stream.

.. index:: ColumnRef

.. function:: column_ref(node, output)

   Pretty print a `node` of type `ColumnRef <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L231>`__ to the `output` stream.

.. index:: CommonTableExpr

.. function:: common_table_expr(node, output)

   Pretty print a `node` of type `CommonTableExpr <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1364>`__ to the `output` stream.

.. index:: DeleteStmt

.. function:: delete_stmt(node, output)

   Pretty print a `node` of type `DeleteStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1457>`__ to the `output` stream.

.. index:: Float

.. function:: float(node, output)

   Pretty print a `node` of type `Float <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: FuncCall

.. function:: func_call(node, output)

   Pretty print a `node` of type `FuncCall <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L346>`__ to the `output` stream.

.. index:: IndexElem

.. function:: index_elem(node, output)

   Pretty print a `node` of type `IndexElem <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L685>`__ to the `output` stream.

.. index:: InferClause

.. function:: infer_clause(node, output)

   Pretty print a `node` of type `InferClause <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1333>`__ to the `output` stream.

.. index:: Integer

.. function:: integer(node, output)

   Pretty print a `node` of type `Integer <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: InsertStmt

.. function:: insert_stmt(node, output)

   Pretty print a `node` of type `InsertStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1441>`__ to the `output` stream.

.. index:: JoinExpr

.. function:: join_expr(node, output)

   Pretty print a `node` of type `JoinExpr <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1446>`__ to the `output` stream.

.. index:: LockingClause

.. function:: locking_clause(node, output)

   Pretty print a `node` of type `LockingClause <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L734>`__ to the `output` stream.

.. index:: MinMaxExpr

.. function:: min_max_expr(node, output)

   Pretty print a `node` of type `MinMaxExpr <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1060>`__ to the `output` stream.

.. index:: MultiAssignRef

.. function:: multi_assign_ref(node, output)

   Pretty print a `node` of type `MultiAssignRef <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L454>`__ to the `output` stream.

.. index:: NullTest

.. function:: null_test(node, output)

   Pretty print a `node` of type `NullTest <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1177>`__ to the `output` stream.

.. index:: ParamRef

.. function:: param_ref(node, output)

   Pretty print a `node` of type `ParamRef <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L241>`__ to the `output` stream.

.. index:: OnConflictClause

.. function:: on_conflict_clause(node, output)

   Pretty print a `node` of type `OnConflictClause <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1348>`__ to the `output` stream.

.. index:: RangeFunction

.. function:: range_function(node, output)

   Pretty print a `node` of type `RangeFunction <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L553>`__ to the `output` stream.

.. index:: RangeSubselect

.. function:: range_subselect(node, output)

   Pretty print a `node` of type `RangeSubselect <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L531>`__ to the `output` stream.

.. index:: RangeVar

.. function:: range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L63>`__ to the `output` stream.

.. index:: RawStmt

.. function:: raw_stmt(node, output)

   Pretty print a `node` of type `RawStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1421>`__ to the `output` stream.

.. index:: ResTarget

.. function:: res_target(node, output)

   Pretty print a `node` of type `ResTarget <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L436>`__ to the `output` stream.

.. index:: RowExpr

.. function:: row_expr(node, output)

   Pretty print a `node` of type `RowExpr <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L983>`__ to the `output` stream.

.. index:: SelectStmt

.. function:: select_stmt(node, output)

   Pretty print a `node` of type `SelectStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1503>`__ to the `output` stream.

.. index:: SetToDefault

.. function:: set_to_default(node, output)

   Pretty print a `node` of type `SetToDefault <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1253>`__ to the `output` stream.

.. index:: SortBy

.. function:: sort_by(node, output)

   Pretty print a `node` of type `SortBy <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L465>`__ to the `output` stream.

.. index:: SQLValueFunction

.. function:: sql_value_function(node, output)

   Pretty print a `node` of type `SQLValueFunction <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1101>`__ to the `output` stream.

.. index:: String

.. function:: string(node, output)

   Pretty print a `node` of type `String <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: SubLink

.. function:: sub_link(node, output)

   Pretty print a `node` of type `SubLink <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L631>`__ to the `output` stream.

.. index:: TypeCast

.. function:: type_cast(node, output)

   Pretty print a `node` of type `TypeCast <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L294>`__ to the `output` stream.

.. index:: TypeName

.. function:: type_name(node, output)

   Pretty print a `node` of type `TypeName <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L205>`__ to the `output` stream.

.. index:: UpdateStmt

.. function:: update_stmt(node, output)

   Pretty print a `node` of type `UpdateStmt <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1471>`__ to the `output` stream.

.. index:: WindowDef

.. function:: window_def(node, output)

   Pretty print a `node` of type `WindowDef <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L483>`__ to the `output` stream.

.. index:: WithClause

.. function:: with_clause(node, output)

   Pretty print a `node` of type `WithClause <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/parsenodes.h#L1319>`__ to the `output` stream.
