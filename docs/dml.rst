.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2020 Lele Gaifax
..

======================================================
 :mod:`pglast.printers.dml` --- DML printer functions
======================================================

.. module:: pglast.printers.dml
   :synopsis: DML printer functions

.. index:: A_ArrayExpr

.. function:: a_array_expr(node, output)

   Pretty print a `node` of type `A_ArrayExpr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L412>`__ to the `output` stream.

.. index:: A_Const

.. function:: a_const(node, output)

   Pretty print a `node` of type `A_Const <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L285>`__ to the `output` stream.

.. index:: A_Expr

.. function:: a_expr(node, output)

   Pretty print a `node` of type `A_Expr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L272>`__ to the `output` stream.

.. index:: A_Indices

.. function:: a_indices(node, output)

   Pretty print a `node` of type `A_Indices <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L379>`__ to the `output` stream.

.. index:: A_Indirection

.. function:: a_indirection(node, output)

   Pretty print a `node` of type `A_Indirection <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L402>`__ to the `output` stream.

.. index::
   pair: A_Indirection;A_Star

.. function:: a_indirection_a_star(node, output)

   Pretty print a `node` of type `A_Star <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L368>`__, when it is inside a `A_Indirection <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L402>`__, to the `output` stream.

.. index::
   pair: A_Indirection;ColumnRef

.. function:: a_indirection_column_ref(node, output)

   Pretty print a `node` of type `ColumnRef <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L232>`__, when it is inside a `A_Indirection <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L402>`__, to the `output` stream.

.. index::
   pair: A_Indirection;FuncCall

.. function:: a_indirection_func_call(node, output)

   Pretty print a `node` of type `FuncCall <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L347>`__, when it is inside a `A_Indirection <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L402>`__, to the `output` stream.

.. index::
   pair: A_Indirection;String

.. function:: a_indirection_field(node, output)

   Pretty print a `node` of type `String <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/value.h#L42>`__, when it is inside a `A_Indirection <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L402>`__, to the `output` stream.

.. index:: A_Star

.. function:: a_star(node, output)

   Pretty print a `node` of type `A_Star <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L368>`__ to the `output` stream.

.. index:: Alias

.. function:: alias(node, output)

   Pretty print a `node` of type `Alias <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L39>`__ to the `output` stream.

.. index:: BitString

.. function:: bitstring(node, output)

   Pretty print a `node` of type `BitString <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: BoolExpr

.. function:: bool_expr(node, output)

   Pretty print a `node` of type `BoolExpr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L565>`__ to the `output` stream.

.. index:: BooleanTest

.. function:: boolean_test(node, output)

   Pretty print a `node` of type `BooleanTest <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L1225>`__ to the `output` stream.

.. index:: CaseExpr

.. function:: case_expr(node, output)

   Pretty print a `node` of type `CaseExpr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L913>`__ to the `output` stream.

.. index:: CaseWhen

.. function:: case_when(node, output)

   Pretty print a `node` of type `CaseWhen <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L927>`__ to the `output` stream.

.. index:: CoalesceExpr

.. function:: coalesce_expr(node, output)

   Pretty print a `node` of type `CoalesceExpr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L1067>`__ to the `output` stream.

.. index:: CollateClause

.. function:: collate_clause(node, output)

   Pretty print a `node` of type `CollateClause <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L306>`__ to the `output` stream.

.. index:: ColumnRef

.. function:: column_ref(node, output)

   Pretty print a `node` of type `ColumnRef <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L232>`__ to the `output` stream.

.. index:: CommonTableExpr

.. function:: common_table_expr(node, output)

   Pretty print a `node` of type `CommonTableExpr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1424>`__ to the `output` stream.

.. index:: ConstraintsSetStmt

.. function:: constraints_set_stmt(node, output)

   Pretty print a `node` of type `ConstraintsSetStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3290>`__ to the `output` stream.

.. index:: DeleteStmt

.. function:: delete_stmt(node, output)

   Pretty print a `node` of type `DeleteStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1518>`__ to the `output` stream.

.. index:: Float

.. function:: float(node, output)

   Pretty print a `node` of type `Float <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: FuncCall

.. function:: func_call(node, output)

   Pretty print a `node` of type `FuncCall <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L347>`__ to the `output` stream.

.. index:: GroupingSet

.. function:: grouping_set(node, output)

   Pretty print a `node` of type `GroupingSet <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1300>`__ to the `output` stream.

.. index:: IndexElem

.. function:: index_elem(node, output)

   Pretty print a `node` of type `IndexElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L696>`__ to the `output` stream.

.. index:: InferClause

.. function:: infer_clause(node, output)

   Pretty print a `node` of type `InferClause <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1386>`__ to the `output` stream.

.. index:: Integer

.. function:: integer(node, output)

   Pretty print a `node` of type `Integer <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: InsertStmt

.. function:: insert_stmt(node, output)

   Pretty print a `node` of type `InsertStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1502>`__ to the `output` stream.

.. index:: JoinExpr

.. function:: join_expr(node, output)

   Pretty print a `node` of type `JoinExpr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L1471>`__ to the `output` stream.

.. index:: LockingClause

.. function:: locking_clause(node, output)

   Pretty print a `node` of type `LockingClause <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L745>`__ to the `output` stream.

.. index:: MinMaxExpr

.. function:: min_max_expr(node, output)

   Pretty print a `node` of type `MinMaxExpr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L1085>`__ to the `output` stream.

.. index:: MultiAssignRef

.. function:: multi_assign_ref(node, output)

   Pretty print a `node` of type `MultiAssignRef <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L455>`__ to the `output` stream.

.. index:: NamedArgExpr

.. function:: named_arg_expr(node, output)

   Pretty print a `node` of type `NamedArgExpr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L481>`__ to the `output` stream.

.. index:: Null

.. function:: null(node, output)

   Pretty print a `node` of type `Null <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: NullTest

.. function:: null_test(node, output)

   Pretty print a `node` of type `NullTest <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L1202>`__ to the `output` stream.

.. index:: ParamRef

.. function:: param_ref(node, output)

   Pretty print a `node` of type `ParamRef <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L242>`__ to the `output` stream.

.. index:: OnConflictClause

.. function:: on_conflict_clause(node, output)

   Pretty print a `node` of type `OnConflictClause <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1401>`__ to the `output` stream.

.. index:: RangeFunction

.. function:: range_function(node, output)

   Pretty print a `node` of type `RangeFunction <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L560>`__ to the `output` stream.

.. index:: RangeSubselect

.. function:: range_subselect(node, output)

   Pretty print a `node` of type `RangeSubselect <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L538>`__ to the `output` stream.

.. index:: RangeVar

.. function:: range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L63>`__ to the `output` stream.

.. index:: RawStmt

.. function:: raw_stmt(node, output)

   Pretty print a `node` of type `RawStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1482>`__ to the `output` stream.

.. index:: ResTarget

.. function:: res_target(node, output)

   Pretty print a `node` of type `ResTarget <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L437>`__ to the `output` stream.

.. index:: RowExpr

.. function:: row_expr(node, output)

   Pretty print a `node` of type `RowExpr <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L1005>`__ to the `output` stream.

.. index:: SelectStmt

.. function:: select_stmt(node, output)

   Pretty print a `node` of type `SelectStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1564>`__ to the `output` stream.

.. index:: SetToDefault

.. function:: set_to_default(node, output)

   Pretty print a `node` of type `SetToDefault <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L1278>`__ to the `output` stream.

.. index:: SortBy

.. function:: sort_by(node, output)

   Pretty print a `node` of type `SortBy <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L466>`__ to the `output` stream.

.. index:: SQLValueFunction

.. function:: sql_value_function(node, output)

   Pretty print a `node` of type `SQLValueFunction <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L1126>`__ to the `output` stream.

.. index:: String

.. function:: string(node, output)

   Pretty print a `node` of type `String <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: SubLink

.. function:: sub_link(node, output)

   Pretty print a `node` of type `SubLink <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/primnodes.h#L637>`__ to the `output` stream.

.. index:: TransactionStmt

.. function:: transaction_stmt(node, output)

   Pretty print a `node` of type `TransactionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3008>`__ to the `output` stream.

.. index::
   pair: TransactionStmt;DefElem

.. function:: transaction_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L726>`__, when it is inside a `TransactionStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L3008>`__, to the `output` stream.

.. index:: TruncateStmt

.. function:: truncate_stmt(node, output)

   Pretty print a `node` of type `TruncateStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2642>`__ to the `output` stream.

.. index:: TypeCast

.. function:: type_cast(node, output)

   Pretty print a `node` of type `TypeCast <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L295>`__ to the `output` stream.

.. index:: TypeName

.. function:: type_name(node, output)

   Pretty print a `node` of type `TypeName <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L206>`__ to the `output` stream.

.. index:: UpdateStmt

.. function:: update_stmt(node, output)

   Pretty print a `node` of type `UpdateStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1532>`__ to the `output` stream.

.. index::
   pair: OnConflictClause;ResTarget

.. index::
   pair: UpdateStmt;ResTarget

.. function:: update_stmt_res_target(node, output)

   Pretty print a `node` of type `ResTarget <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L437>`__, when it is inside a `OnConflictClause <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1401>`__ or a `UpdateStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1532>`__, to the `output` stream.

.. index:: VariableSetStmt

.. function:: variable_set_stmt(node, output)

   Pretty print a `node` of type `VariableSetStmt <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L2016>`__ to the `output` stream.

.. index:: WindowDef

.. function:: window_def(node, output)

   Pretty print a `node` of type `WindowDef <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L484>`__ to the `output` stream.

.. index:: WithClause

.. function:: with_clause(node, output)

   Pretty print a `node` of type `WithClause <https://github.com/rdunklau/libpg_query/blob/90bc162/tmp/postgres/src/include/nodes/parsenodes.h#L1372>`__ to the `output` stream.
