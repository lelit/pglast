.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2023 Lele Gaifax
..

======================================================
 :mod:`pglast.printers.dml` --- DML printer functions
======================================================

.. module:: pglast.printers.dml
   :synopsis: DML printer functions

.. index:: A_ArrayExpr

.. function:: a_array_expr(node, output)

   Pretty print a `node` of type `A_ArrayExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L444>`__ to the `output` stream.

.. index:: A_Const

.. function:: a_const(node, output)

   Pretty print a `node` of type `A_Const <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L301>`__ to the `output` stream.

.. index:: A_Expr

.. function:: a_expr(node, output)

   Pretty print a `node` of type `A_Expr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L288>`__ to the `output` stream.

.. index:: A_Indices

.. function:: a_indices(node, output)

   Pretty print a `node` of type `A_Indices <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L411>`__ to the `output` stream.

.. index:: A_Indirection

.. function:: a_indirection(node, output)

   Pretty print a `node` of type `A_Indirection <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L434>`__ to the `output` stream.

.. index::
   pair: A_Indirection;A_Star

.. function:: a_indirection_a_star(node, output)

   Pretty print a `node` of type `A_Star <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L400>`__, when it is inside a `A_Indirection <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L434>`__, to the `output` stream.

.. index::
   pair: A_Indirection;ColumnRef

.. function:: a_indirection_column_ref(node, output)

   Pretty print a `node` of type `ColumnRef <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L250>`__, when it is inside a `A_Indirection <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L434>`__, to the `output` stream.

.. index::
   pair: A_Indirection;FuncCall

.. function:: a_indirection_func_call(node, output)

   Pretty print a `node` of type `FuncCall <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L378>`__, when it is inside a `A_Indirection <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L434>`__, to the `output` stream.

.. index::
   pair: A_Indirection;String

.. function:: a_indirection_field(node, output)

   Pretty print a `node` of type `String <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/value.h#L57>`__, when it is inside a `A_Indirection <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L434>`__, to the `output` stream.

.. index:: A_Star

.. function:: a_star(node, output)

   Pretty print a `node` of type `A_Star <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L400>`__ to the `output` stream.

.. index:: Alias

.. function:: alias(node, output)

   Pretty print a `node` of type `Alias <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L39>`__ to the `output` stream.

.. index:: BitString

.. function:: bitstring(node, output)

   Pretty print a `node` of type `BitString <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/value.h#L63>`__ to the `output` stream.

.. index:: Boolean

.. function:: boolean(node, output)

   Pretty print a `node` of type `Boolean <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/value.h#L51>`__ to the `output` stream.

.. index:: BoolExpr

.. function:: bool_expr(node, output)

   Pretty print a `node` of type `BoolExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L622>`__ to the `output` stream.

.. index:: BooleanTest

.. function:: boolean_test(node, output)

   Pretty print a `node` of type `BooleanTest <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L1283>`__ to the `output` stream.

.. index:: CallStmt

.. function:: call_stmt(node, output)

   Pretty print a `node` of type `CallStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3099>`__ to the `output` stream.

.. index:: CaseExpr

.. function:: case_expr(node, output)

   Pretty print a `node` of type `CaseExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L973>`__ to the `output` stream.

.. index:: CaseWhen

.. function:: case_when(node, output)

   Pretty print a `node` of type `CaseWhen <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L987>`__ to the `output` stream.

.. index:: CoalesceExpr

.. function:: coalesce_expr(node, output)

   Pretty print a `node` of type `CoalesceExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L1125>`__ to the `output` stream.

.. index:: CollateClause

.. function:: collate_clause(node, output)

   Pretty print a `node` of type `CollateClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L336>`__ to the `output` stream.

.. index:: ColumnRef

.. function:: column_ref(node, output)

   Pretty print a `node` of type `ColumnRef <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L250>`__ to the `output` stream.

.. index:: CTECycleClause

.. function:: cte_cycle_clause(node, output)

   Pretty print a `node` of type `CTECycleClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1505>`__ to the `output` stream.

.. index::
   pair: CTECycleClause;TypeCast

.. function:: cte_cycle_clause_type_cast(node, output)

   Pretty print a `node` of type `TypeCast <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L325>`__, when it is inside a `CTECycleClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1505>`__, to the `output` stream.

.. index:: CTESearchClause

.. function:: cte_search_clause(node, output)

   Pretty print a `node` of type `CTESearchClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1496>`__ to the `output` stream.

.. index:: CommonTableExpr

.. function:: common_table_expr(node, output)

   Pretty print a `node` of type `CommonTableExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1521>`__ to the `output` stream.

.. index:: ConstraintsSetStmt

.. function:: constraints_set_stmt(node, output)

   Pretty print a `node` of type `ConstraintsSetStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3542>`__ to the `output` stream.

.. index:: CopyStmt

.. function:: copy_stmt(node, output)

   Pretty print a `node` of type `CopyStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L2180>`__ to the `output` stream.

.. index::
   pair: CopyStmt;DefElem

.. function:: copy_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L762>`__, when it is inside a `CopyStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L2180>`__, to the `output` stream.

.. index:: DeclareCursorStmt

.. function:: declare_cursor_stmt(node, output)

   Pretty print a `node` of type `DeclareCursorStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L2894>`__ to the `output` stream.

.. index:: DeleteStmt

.. function:: delete_stmt(node, output)

   Pretty print a `node` of type `DeleteStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1650>`__ to the `output` stream.

.. index:: ExecuteStmt

.. function:: execute_stmt(node, output)

   Pretty print a `node` of type `ExecuteStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3632>`__ to the `output` stream.

.. index:: ExplainStmt

.. function:: explain_stmt(node, output)

   Pretty print a `node` of type `ExplainStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3456>`__ to the `output` stream.

.. index::
   pair: ExplainStmt;DefElem

.. function:: explain_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L762>`__, when it is inside a `ExplainStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3456>`__, to the `output` stream.

.. index:: FetchStmt

.. function:: fetch_stmt(node, output)

   Pretty print a `node` of type `FetchStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L2929>`__ to the `output` stream.

.. index:: Float

.. function:: float(node, output)

   Pretty print a `node` of type `Float <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/value.h#L45>`__ to the `output` stream.

.. index:: FuncCall

.. function:: func_call(node, output)

   Pretty print a `node` of type `FuncCall <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L378>`__ to the `output` stream.

.. index::
   pair: FuncCall;WindowDef

.. function:: func_call_window_def(node, output)

   Pretty print a `node` of type `WindowDef <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L516>`__, when it is inside a `FuncCall <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L378>`__, to the `output` stream.

.. index:: GroupingSet

.. function:: grouping_set(node, output)

   Pretty print a `node` of type `GroupingSet <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1372>`__ to the `output` stream.

.. index:: GroupingFunc

.. function:: grouping_func(node, output)

   Pretty print a `node` of type `GroupingFunc <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L369>`__ to the `output` stream.

.. index:: IndexElem

.. function:: index_elem(node, output)

   Pretty print a `node` of type `IndexElem <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L731>`__ to the `output` stream.

.. index:: InferClause

.. function:: infer_clause(node, output)

   Pretty print a `node` of type `InferClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1459>`__ to the `output` stream.

.. index:: Integer

.. function:: integer(node, output)

   Pretty print a `node` of type `Integer <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/value.h#L28>`__ to the `output` stream.

.. index:: InsertStmt

.. function:: insert_stmt(node, output)

   Pretty print a `node` of type `InsertStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1634>`__ to the `output` stream.

.. index:: IntoClause

.. function:: into_clause(node, output)

   Pretty print a `node` of type `IntoClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L108>`__ to the `output` stream.

.. index:: JoinExpr

.. function:: join_expr(node, output)

   Pretty print a `node` of type `JoinExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L1536>`__ to the `output` stream.

.. index:: LockingClause

.. function:: locking_clause(node, output)

   Pretty print a `node` of type `LockingClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L782>`__ to the `output` stream.

.. index:: ListenStmt

.. function:: listen_stmt(node, output)

   Pretty print a `node` of type `ListenStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3225>`__ to the `output` stream.

.. index:: MergeStmt

.. function:: merge_stmt(node, output)

   Pretty print a `node` of type `MergeStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1679>`__ to the `output` stream.

.. index:: MergeWhenClause

.. function:: merge_when_clause(node, output)

   Pretty print a `node` of type `MergeWhenClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1555>`__ to the `output` stream.

.. index:: MinMaxExpr

.. function:: min_max_expr(node, output)

   Pretty print a `node` of type `MinMaxExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L1143>`__ to the `output` stream.

.. index:: MultiAssignRef

.. function:: multi_assign_ref(node, output)

   Pretty print a `node` of type `MultiAssignRef <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L487>`__ to the `output` stream.

.. index:: NamedArgExpr

.. function:: named_arg_expr(node, output)

   Pretty print a `node` of type `NamedArgExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L521>`__ to the `output` stream.

.. index:: NullTest

.. function:: null_test(node, output)

   Pretty print a `node` of type `NullTest <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L1260>`__ to the `output` stream.

.. index:: ParamRef

.. function:: param_ref(node, output)

   Pretty print a `node` of type `ParamRef <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L260>`__ to the `output` stream.

.. index:: PrepareStmt

.. function:: prepare_stmt(node, output)

   Pretty print a `node` of type `PrepareStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3618>`__ to the `output` stream.

.. index:: OnConflictClause

.. function:: on_conflict_clause(node, output)

   Pretty print a `node` of type `OnConflictClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1474>`__ to the `output` stream.

.. index:: RangeFunction

.. function:: range_function(node, output)

   Pretty print a `node` of type `RangeFunction <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L592>`__ to the `output` stream.

.. index:: RangeSubselect

.. function:: range_subselect(node, output)

   Pretty print a `node` of type `RangeSubselect <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L570>`__ to the `output` stream.

.. index:: RangeTableFunc

.. function:: range_table_func(node, output)

   Pretty print a `node` of type `RangeTableFunc <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L607>`__ to the `output` stream.

.. index::
   pair: RangeTableFunc;ResTarget

.. function:: range_table_func_res_target(node, output)

   Pretty print a `node` of type `ResTarget <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L469>`__, when it is inside a `RangeTableFunc <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L607>`__, to the `output` stream.

.. index:: RangeTableFuncCol

.. function:: range_table_func_col(node, output)

   Pretty print a `node` of type `RangeTableFuncCol <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L625>`__ to the `output` stream.

.. index:: RangeVar

.. function:: range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L63>`__ to the `output` stream.

.. index:: RangeTableSample

.. function:: range_table_sample(node, output)

   Pretty print a `node` of type `RangeTableSample <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L647>`__ to the `output` stream.

.. index:: RawStmt

.. function:: raw_stmt(node, output)

   Pretty print a `node` of type `RawStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1614>`__ to the `output` stream.

.. index:: ResTarget

.. function:: res_target(node, output)

   Pretty print a `node` of type `ResTarget <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L469>`__ to the `output` stream.

.. index:: RowExpr

.. function:: row_expr(node, output)

   Pretty print a `node` of type `RowExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L1063>`__ to the `output` stream.

.. index:: SelectStmt

.. function:: select_stmt(node, output)

   Pretty print a `node` of type `SelectStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1710>`__ to the `output` stream.

.. index:: SetToDefault

.. function:: set_to_default(node, output)

   Pretty print a `node` of type `SetToDefault <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L1336>`__ to the `output` stream.

.. index:: SortBy

.. function:: sort_by(node, output)

   Pretty print a `node` of type `SortBy <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L498>`__ to the `output` stream.

.. index:: SQLValueFunction

.. function:: sql_value_function(node, output)

   Pretty print a `node` of type `SQLValueFunction <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L1184>`__ to the `output` stream.

.. index:: String

.. function:: string(node, output)

   Pretty print a `node` of type `String <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/value.h#L57>`__ to the `output` stream.

.. index:: SubLink

.. function:: sub_link(node, output)

   Pretty print a `node` of type `SubLink <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L694>`__ to the `output` stream.

.. index:: TransactionStmt

.. function:: transaction_stmt(node, output)

   Pretty print a `node` of type `TransactionStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3259>`__ to the `output` stream.

.. index::
   pair: TransactionStmt;DefElem

.. function:: transaction_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L762>`__, when it is inside a `TransactionStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3259>`__, to the `output` stream.

.. index:: TruncateStmt

.. function:: truncate_stmt(node, output)

   Pretty print a `node` of type `TruncateStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L2841>`__ to the `output` stream.

.. index:: TypeCast

.. function:: type_cast(node, output)

   Pretty print a `node` of type `TypeCast <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L325>`__ to the `output` stream.

.. index:: TypeName

.. function:: type_name(node, output)

   Pretty print a `node` of type `TypeName <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L224>`__ to the `output` stream.

.. index::
   pair: VariableSetStmt;TypeCast

.. function:: variable_set_stmt_type_cast(node, output)

   Pretty print a `node` of type `TypeCast <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L325>`__, when it is inside a `VariableSetStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L2212>`__, to the `output` stream.

.. index:: UpdateStmt

.. function:: update_stmt(node, output)

   Pretty print a `node` of type `UpdateStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1664>`__ to the `output` stream.

.. index:: UnlistenStmt

.. function:: unlisten_stmt(node, output)

   Pretty print a `node` of type `UnlistenStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L3235>`__ to the `output` stream.

.. index:: WithClause

.. function:: with_clause(node, output)

   Pretty print a `node` of type `WithClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1445>`__ to the `output` stream.

.. index:: WindowDef

.. function:: window_def(node, output)

   Pretty print a `node` of type `WindowDef <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L516>`__ to the `output` stream.

.. index::
   pair: MergeWhenClause;ResTarget

.. index::
   pair: OnConflictClause;ResTarget

.. index::
   pair: UpdateStmt;ResTarget

.. function:: update_stmt_res_target(node, output)

   Pretty print a `node` of type `ResTarget <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L469>`__, when it is inside a `MergeWhenClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1555>`__ or a `OnConflictClause <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1474>`__ or a `UpdateStmt <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L1664>`__, to the `output` stream.

.. index:: XmlExpr

.. function:: xml_expr(node, output)

   Pretty print a `node` of type `XmlExpr <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/primnodes.h#L1222>`__ to the `output` stream.

.. index:: XmlSerialize

.. function:: xml_serialize(node, output)

   Pretty print a `node` of type `XmlSerialize <https://github.com/pganalyze/libpg_query/blob/1f2d166/src/postgres/include/nodes/parsenodes.h#L793>`__ to the `output` stream.
