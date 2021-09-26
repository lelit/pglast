.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2021 Lele Gaifax
..

======================================================
 :mod:`pglast.printers.dml` --- DML printer functions
======================================================

.. module:: pglast.printers.dml
   :synopsis: DML printer functions

.. index:: A_ArrayExpr

.. function:: a_array_expr(node, output)

   Pretty print a `node` of type `A_ArrayExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L413>`__ to the `output` stream.

.. index:: A_Const

.. function:: a_const(node, output)

   Pretty print a `node` of type `A_Const <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L286>`__ to the `output` stream.

.. index:: A_Expr

.. function:: a_expr(node, output)

   Pretty print a `node` of type `A_Expr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L273>`__ to the `output` stream.

.. index:: A_Indices

.. function:: a_indices(node, output)

   Pretty print a `node` of type `A_Indices <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L380>`__ to the `output` stream.

.. index:: A_Indirection

.. function:: a_indirection(node, output)

   Pretty print a `node` of type `A_Indirection <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L403>`__ to the `output` stream.

.. index::
   pair: A_Indirection;A_Star

.. function:: a_indirection_a_star(node, output)

   Pretty print a `node` of type `A_Star <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L369>`__, when it is inside a `A_Indirection <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L403>`__, to the `output` stream.

.. index::
   pair: A_Indirection;ColumnRef

.. function:: a_indirection_column_ref(node, output)

   Pretty print a `node` of type `ColumnRef <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L233>`__, when it is inside a `A_Indirection <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L403>`__, to the `output` stream.

.. index::
   pair: A_Indirection;FuncCall

.. function:: a_indirection_func_call(node, output)

   Pretty print a `node` of type `FuncCall <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L348>`__, when it is inside a `A_Indirection <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L403>`__, to the `output` stream.

.. index::
   pair: A_Indirection;String

.. function:: a_indirection_field(node, output)

   Pretty print a `node` of type `String <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/value.h#L42>`__, when it is inside a `A_Indirection <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L403>`__, to the `output` stream.

.. index:: A_Star

.. function:: a_star(node, output)

   Pretty print a `node` of type `A_Star <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L369>`__ to the `output` stream.

.. index:: Alias

.. function:: alias(node, output)

   Pretty print a `node` of type `Alias <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L39>`__ to the `output` stream.

.. index:: BitString

.. function:: bitstring(node, output)

   Pretty print a `node` of type `BitString <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: BoolExpr

.. function:: bool_expr(node, output)

   Pretty print a `node` of type `BoolExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L579>`__ to the `output` stream.

.. index:: BooleanTest

.. function:: boolean_test(node, output)

   Pretty print a `node` of type `BooleanTest <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L1239>`__ to the `output` stream.

.. index:: CallStmt

.. function:: call_stmt(node, output)

   Pretty print a `node` of type `CallStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L2903>`__ to the `output` stream.

.. index:: CaseExpr

.. function:: case_expr(node, output)

   Pretty print a `node` of type `CaseExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L927>`__ to the `output` stream.

.. index:: CaseWhen

.. function:: case_when(node, output)

   Pretty print a `node` of type `CaseWhen <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L941>`__ to the `output` stream.

.. index:: CoalesceExpr

.. function:: coalesce_expr(node, output)

   Pretty print a `node` of type `CoalesceExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L1081>`__ to the `output` stream.

.. index:: CollateClause

.. function:: collate_clause(node, output)

   Pretty print a `node` of type `CollateClause <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L307>`__ to the `output` stream.

.. index:: ColumnRef

.. function:: column_ref(node, output)

   Pretty print a `node` of type `ColumnRef <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L233>`__ to the `output` stream.

.. index:: CommonTableExpr

.. function:: common_table_expr(node, output)

   Pretty print a `node` of type `CommonTableExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1452>`__ to the `output` stream.

.. index:: ConstraintsSetStmt

.. function:: constraints_set_stmt(node, output)

   Pretty print a `node` of type `ConstraintsSetStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L3345>`__ to the `output` stream.

.. index:: CopyStmt

.. function:: copy_stmt(node, output)

   Pretty print a `node` of type `CopyStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L2013>`__ to the `output` stream.

.. index::
   pair: CopyStmt;DefElem

.. function:: copy_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `CopyStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L2013>`__, to the `output` stream.

.. index:: DeclareCursorStmt

.. function:: declare_cursor_stmt(node, output)

   Pretty print a `node` of type `DeclareCursorStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L2723>`__ to the `output` stream.

.. index:: DeleteStmt

.. function:: delete_stmt(node, output)

   Pretty print a `node` of type `DeleteStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1546>`__ to the `output` stream.

.. index:: ExecuteStmt

.. function:: execute_stmt(node, output)

   Pretty print a `node` of type `ExecuteStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L3441>`__ to the `output` stream.

.. index:: ExplainStmt

.. function:: explain_stmt(node, output)

   Pretty print a `node` of type `ExplainStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L3259>`__ to the `output` stream.

.. index::
   pair: ExplainStmt;DefElem

.. function:: explain_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `ExplainStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L3259>`__, to the `output` stream.

.. index:: FetchStmt

.. function:: fetch_stmt(node, output)

   Pretty print a `node` of type `FetchStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L2758>`__ to the `output` stream.

.. index:: Float

.. function:: float(node, output)

   Pretty print a `node` of type `Float <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: FuncCall

.. function:: func_call(node, output)

   Pretty print a `node` of type `FuncCall <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L348>`__ to the `output` stream.

.. index::
   pair: FuncCall;WindowDef

.. function:: func_call_window_def(node, output)

   Pretty print a `node` of type `WindowDef <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L485>`__, when it is inside a `FuncCall <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L348>`__, to the `output` stream.

.. index:: GroupingSet

.. function:: grouping_set(node, output)

   Pretty print a `node` of type `GroupingSet <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1328>`__ to the `output` stream.

.. index:: GroupingFunc

.. function:: grouping_func(node, output)

   Pretty print a `node` of type `GroupingFunc <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L356>`__ to the `output` stream.

.. index:: IndexElem

.. function:: index_elem(node, output)

   Pretty print a `node` of type `IndexElem <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L698>`__ to the `output` stream.

.. index:: InferClause

.. function:: infer_clause(node, output)

   Pretty print a `node` of type `InferClause <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1414>`__ to the `output` stream.

.. index:: Integer

.. function:: integer(node, output)

   Pretty print a `node` of type `Integer <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: InsertStmt

.. function:: insert_stmt(node, output)

   Pretty print a `node` of type `InsertStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1530>`__ to the `output` stream.

.. index:: IntoClause

.. function:: into_clause(node, output)

   Pretty print a `node` of type `IntoClause <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L108>`__ to the `output` stream.

.. index:: JoinExpr

.. function:: join_expr(node, output)

   Pretty print a `node` of type `JoinExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L1485>`__ to the `output` stream.

.. index:: LockingClause

.. function:: locking_clause(node, output)

   Pretty print a `node` of type `LockingClause <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L748>`__ to the `output` stream.

.. index:: ListenStmt

.. function:: listen_stmt(node, output)

   Pretty print a `node` of type `ListenStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L3028>`__ to the `output` stream.

.. index:: MinMaxExpr

.. function:: min_max_expr(node, output)

   Pretty print a `node` of type `MinMaxExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L1099>`__ to the `output` stream.

.. index:: MultiAssignRef

.. function:: multi_assign_ref(node, output)

   Pretty print a `node` of type `MultiAssignRef <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L456>`__ to the `output` stream.

.. index:: NamedArgExpr

.. function:: named_arg_expr(node, output)

   Pretty print a `node` of type `NamedArgExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L495>`__ to the `output` stream.

.. index:: Null

.. function:: null(node, output)

   Pretty print a `node` of type `Null <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: NullTest

.. function:: null_test(node, output)

   Pretty print a `node` of type `NullTest <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L1216>`__ to the `output` stream.

.. index:: ParamRef

.. function:: param_ref(node, output)

   Pretty print a `node` of type `ParamRef <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L243>`__ to the `output` stream.

.. index:: PrepareStmt

.. function:: prepare_stmt(node, output)

   Pretty print a `node` of type `PrepareStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L3427>`__ to the `output` stream.

.. index:: OnConflictClause

.. function:: on_conflict_clause(node, output)

   Pretty print a `node` of type `OnConflictClause <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1429>`__ to the `output` stream.

.. index:: RangeFunction

.. function:: range_function(node, output)

   Pretty print a `node` of type `RangeFunction <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L561>`__ to the `output` stream.

.. index:: RangeSubselect

.. function:: range_subselect(node, output)

   Pretty print a `node` of type `RangeSubselect <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L539>`__ to the `output` stream.

.. index:: RangeTableFunc

.. function:: range_table_func(node, output)

   Pretty print a `node` of type `RangeTableFunc <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L576>`__ to the `output` stream.

.. index::
   pair: RangeTableFunc;ResTarget

.. function:: range_table_func_res_target(node, output)

   Pretty print a `node` of type `ResTarget <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L438>`__, when it is inside a `RangeTableFunc <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L576>`__, to the `output` stream.

.. index:: RangeTableFuncCol

.. function:: range_table_func_col(node, output)

   Pretty print a `node` of type `RangeTableFuncCol <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L594>`__ to the `output` stream.

.. index:: RangeVar

.. function:: range_var(node, output)

   Pretty print a `node` of type `RangeVar <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L63>`__ to the `output` stream.

.. index:: RangeTableSample

.. function:: range_table_sample(node, output)

   Pretty print a `node` of type `RangeTableSample <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L616>`__ to the `output` stream.

.. index:: RawStmt

.. function:: raw_stmt(node, output)

   Pretty print a `node` of type `RawStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1510>`__ to the `output` stream.

.. index:: ResTarget

.. function:: res_target(node, output)

   Pretty print a `node` of type `ResTarget <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L438>`__ to the `output` stream.

.. index:: RowExpr

.. function:: row_expr(node, output)

   Pretty print a `node` of type `RowExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L1019>`__ to the `output` stream.

.. index:: SelectStmt

.. function:: select_stmt(node, output)

   Pretty print a `node` of type `SelectStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1592>`__ to the `output` stream.

.. index:: SetToDefault

.. function:: set_to_default(node, output)

   Pretty print a `node` of type `SetToDefault <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L1292>`__ to the `output` stream.

.. index:: SortBy

.. function:: sort_by(node, output)

   Pretty print a `node` of type `SortBy <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L467>`__ to the `output` stream.

.. index:: SQLValueFunction

.. function:: sql_value_function(node, output)

   Pretty print a `node` of type `SQLValueFunction <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L1140>`__ to the `output` stream.

.. index:: String

.. function:: string(node, output)

   Pretty print a `node` of type `String <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/value.h#L42>`__ to the `output` stream.

.. index:: SubLink

.. function:: sub_link(node, output)

   Pretty print a `node` of type `SubLink <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L651>`__ to the `output` stream.

.. index:: TransactionStmt

.. function:: transaction_stmt(node, output)

   Pretty print a `node` of type `TransactionStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L3062>`__ to the `output` stream.

.. index::
   pair: TransactionStmt;DefElem

.. function:: transaction_stmt_def_elem(node, output)

   Pretty print a `node` of type `DefElem <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L729>`__, when it is inside a `TransactionStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L3062>`__, to the `output` stream.

.. index:: TruncateStmt

.. function:: truncate_stmt(node, output)

   Pretty print a `node` of type `TruncateStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L2671>`__ to the `output` stream.

.. index:: TypeCast

.. function:: type_cast(node, output)

   Pretty print a `node` of type `TypeCast <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L296>`__ to the `output` stream.

.. index:: TypeName

.. function:: type_name(node, output)

   Pretty print a `node` of type `TypeName <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L207>`__ to the `output` stream.

.. index:: UpdateStmt

.. function:: update_stmt(node, output)

   Pretty print a `node` of type `UpdateStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1560>`__ to the `output` stream.

.. index:: UnlistenStmt

.. function:: unlisten_stmt(node, output)

   Pretty print a `node` of type `UnlistenStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L3038>`__ to the `output` stream.

.. index:: VariableSetStmt

.. function:: variable_set_stmt(node, output)

   Pretty print a `node` of type `VariableSetStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L2045>`__ to the `output` stream.

.. index:: WithClause

.. function:: with_clause(node, output)

   Pretty print a `node` of type `WithClause <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1400>`__ to the `output` stream.

.. index:: WindowDef

.. function:: window_def(node, output)

   Pretty print a `node` of type `WindowDef <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L485>`__ to the `output` stream.

.. index::
   pair: OnConflictClause;ResTarget

.. index::
   pair: UpdateStmt;ResTarget

.. function:: update_stmt_res_target(node, output)

   Pretty print a `node` of type `ResTarget <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L438>`__, when it is inside a `OnConflictClause <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1429>`__ or a `UpdateStmt <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L1560>`__, to the `output` stream.

.. index:: XmlExpr

.. function:: xml_expr(node, output)

   Pretty print a `node` of type `XmlExpr <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/primnodes.h#L1178>`__ to the `output` stream.

.. index:: XmlSerialize

.. function:: xml_serialize(node, output)

   Pretty print a `node` of type `XmlSerialize <https://github.com/pganalyze/libpg_query/blob/802caf2/src/postgres/include/nodes/parsenodes.h#L759>`__ to the `output` stream.
