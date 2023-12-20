# -*- coding: utf-8 -*-
# :Project:   pglast -- Printer functions for SQL DML nodes
# :Created:   sab 05 ago 2017 16:34:08 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2020, 2021, 2022, 2023 Lele Gaifax
#

from .. import ast, enums
from . import IntEnumPrinter, get_string_value, node_printer


@node_printer(ast.A_ArrayExpr)
def a_array_expr(node, output):
    output.write('ARRAY[')
    if node.elements:
        output.print_list(node.elements)
    output.write(']')


@node_printer(ast.A_Const)
def a_const(node, output):
    if node.isnull:
        output.write('NULL')
    else:
        output.print_node(node.val)


class AExprKindPrinter(IntEnumPrinter):
    enum = enums.A_Expr_Kind

    def AEXPR_BETWEEN(self, node, output):
        output.print_node(node.lexpr)
        output.swrite('BETWEEN ')
        output.print_list(node.rexpr, 'AND', relative_indent=-4)

    def AEXPR_BETWEEN_SYM(self, node, output):
        output.print_node(node.lexpr)
        output.swrite('BETWEEN SYMMETRIC ')
        output.print_list(node.rexpr, 'AND', relative_indent=-4)

    def AEXPR_DISTINCT(self, node, output):
        with output.expression(isinstance(node.lexpr,
                                          (ast.BoolExpr, ast.NullTest, ast.A_Expr))):
            output.print_node(node.lexpr)
        output.swrite('IS DISTINCT FROM ')
        with output.expression(isinstance(node.rexpr,
                                          (ast.BoolExpr, ast.NullTest, ast.A_Expr))):
            output.print_node(node.rexpr)

    def AEXPR_ILIKE(self, node, output):
        output.print_node(node.lexpr)
        if get_string_value(node.name) == '!~~*':
            output.swrites('NOT')
        output.swrite('ILIKE ')
        output.print_node(node.rexpr)

    def AEXPR_IN(self, node, output):
        output.print_node(node.lexpr)
        if get_string_value(node.name) == '<>':
            output.swrites('NOT')
        output.swrite('IN ')
        with output.expression(True):
            output.print_list(node.rexpr)

    def AEXPR_LIKE(self, node, output):
        output.print_node(node.lexpr)
        if get_string_value(node.name) == '!~~':
            output.swrites('NOT')
        output.swrite('LIKE ')
        output.print_node(node.rexpr)

    def AEXPR_NOT_BETWEEN(self, node, output):
        output.print_node(node.lexpr)
        output.swrite('NOT BETWEEN ')
        output.print_list(node.rexpr, 'AND', relative_indent=-4)

    def AEXPR_NOT_BETWEEN_SYM(self, node, output):
        output.print_node(node.lexpr)
        output.swrite('NOT BETWEEN SYMMETRIC ')
        output.print_list(node.rexpr, 'AND', relative_indent=-4)

    def AEXPR_NOT_DISTINCT(self, node, output):
        output.print_node(node.lexpr)
        output.swrite('IS NOT DISTINCT FROM ')
        output.print_node(node.rexpr)

    def AEXPR_NULLIF(self, node, output):
        output.write('NULLIF')
        with output.expression(True):
            output.print_list((node.lexpr, node.rexpr))

    def AEXPR_OP(self, node, output):
        with output.expression(isinstance(abs(node.ancestors), ast.A_Expr)):
            # lexpr is optional because these are valid: -(1+1), +(1+1), ~(1+1)
            if node.lexpr is not None:
                with output.expression(isinstance(node.lexpr,
                                                  (ast.BoolExpr, ast.NullTest, ast.A_Expr))):
                    output.print_node(node.lexpr)
                output.write(' ')
            if isinstance(node.name, tuple) and len(node.name) > 1:
                output.write('OPERATOR')
                with output.expression(True):
                    output.print_symbol(node.name)
            else:
                output.print_symbol(node.name)
            output.write(' ')
            if node.rexpr is not None:
                with output.expression(isinstance(node.rexpr,
                                                  (ast.BoolExpr, ast.NullTest, ast.A_Expr))):
                    output.print_node(node.rexpr)

    def AEXPR_OP_ALL(self, node, output):
        output.print_node(node.lexpr)
        output.write(' ')
        output.write(get_string_value(node.name))
        output.write(' ALL')
        with output.expression(True):
            output.print_node(node.rexpr)

    def AEXPR_OP_ANY(self, node, output):
        output.print_node(node.lexpr)
        output.write(' ')
        output.write(get_string_value(node.name))
        output.write(' ANY')
        with output.expression(True):
            output.print_node(node.rexpr)

    def AEXPR_SIMILAR(self, node, output):
        output.print_node(node.lexpr)
        if get_string_value(node.name) == '!~':
            output.swrites('NOT')
        output.swrite('SIMILAR TO ')
        if ((not isinstance(node.rexpr, ast.FuncCall)
             or node.rexpr.funcname[1].sval != 'similar_to_escape')):
            raise RuntimeError('Expected a FuncCall to "similar_to_escape", got %r',
                               node.rexpr)
        pattern = node.rexpr.args[0]
        output.print_node(pattern)
        if len(node.rexpr.args) > 1:
            output.swrite('ESCAPE ')
            output.print_node(node.rexpr.args[1])


a_expr_kind_printer = AExprKindPrinter()


@node_printer(ast.A_Expr)
def a_expr(node, output):
    a_expr_kind_printer(node.kind, node, output)


@node_printer(ast.A_Indices)
def a_indices(node, output):
    output.write('[')
    if node.is_slice:
        if node.lidx:
            output.print_node(node.lidx)
        output.write(':')
        if node.uidx:
            output.print_node(node.uidx)
    else:
        output.print_node(node.uidx)
    output.write(']')


@node_printer(ast.A_Indirection)
def a_indirection(node, output):
    with output.expression(isinstance(node.arg, (ast.A_ArrayExpr, ast.A_Expr,
                                                 ast.A_Indirection, ast.FuncCall,
                                                 ast.RowExpr, ast.TypeCast))
                           or (isinstance(node.arg, ast.ColumnRef)
                               and not isinstance(node.indirection[0], ast.A_Indices))):
        output.print_node(node.arg)
    output.print_list(node.indirection, '', standalone_items=False)


@node_printer(ast.A_Indirection, ast.A_Star)
def a_indirection_a_star(node, output):
    output.pending_separator = False
    output.write('.')
    a_star(node, output)


@node_printer(ast.A_Indirection, ast.ColumnRef)
def a_indirection_column_ref(node, output):
    with output.expression(True):
        column_ref(node, output)


@node_printer(ast.A_Indirection, ast.FuncCall)
def a_indirection_func_call(node, output):
    with output.expression(True):
        func_call(node, output)


@node_printer(ast.A_Indirection, ast.String)
def a_indirection_field(node, output):
    output.write('.')
    string(node, output, is_name=True)


@node_printer(ast.A_Star)
def a_star(node, output):
    output.write('*')


@node_printer(ast.Alias)
def alias(node, output):
    output.print_name(node.aliasname)
    if node.colnames:
        output.write(' ')
        with output.expression(True):
            output.print_name(node.colnames, sep=',')


@node_printer(ast.BitString)
def bitstring(node, output):
    value = node.bsval
    output.write(f"{value[0]}'{value[1:]}'")


@node_printer(ast.Boolean)
def boolean(node, output):
    output.write('TRUE' if node.boolval else 'FALSE')


def _bool_expr_needs_to_be_wrapped_in_parens(node):
    bet = enums.BoolExprType
    return isinstance(node, ast.BoolExpr) and node.boolop in (bet.AND_EXPR, bet.OR_EXPR)


@node_printer(ast.BoolExpr)
def bool_expr(node, output):
    bet = enums.BoolExprType
    in_res_target = isinstance(node.ancestors[0], ast.ResTarget)
    if node.boolop == bet.AND_EXPR:
        relindent = -4 if not in_res_target else None
        output.print_list(node.args, 'AND', relative_indent=relindent,
                          item_needs_parens=_bool_expr_needs_to_be_wrapped_in_parens)
    elif node.boolop == bet.OR_EXPR:
        relindent = -3 if not in_res_target else None
        output.print_list(node.args, 'OR', relative_indent=relindent,
                          item_needs_parens=_bool_expr_needs_to_be_wrapped_in_parens)
    else:
        output.writes('NOT')
        with output.expression(_bool_expr_needs_to_be_wrapped_in_parens(node.args[0])):
            output.print_node(node.args[0])


class BooleanTestPrinter(IntEnumPrinter):
    enum = enums.BoolTestType

    def IS_FALSE(self, node, output):
        output.write('FALSE')

    def IS_NOT_FALSE(self, node, output):
        output.write('NOT FALSE')

    def IS_NOT_TRUE(self, node, output):
        output.write('NOT TRUE')

    def IS_NOT_UNKNOWN(self, node, output):
        output.write('NOT UNKNOWN')

    def IS_TRUE(self, node, output):
        output.write('TRUE')

    def IS_UNKNOWN(self, node, output):
        output.write('UNKNOWN')


boolean_test_printer = BooleanTestPrinter()


@node_printer(ast.BooleanTest)
def boolean_test(node, output):
    with output.expression(isinstance(node.ancestors[0], ast.A_Expr)):
        with output.expression(isinstance(node.arg, ast.BoolExpr)):
            output.print_node(node.arg)
        output.write(' IS ')
        boolean_test_printer(node.booltesttype, node, output)


@node_printer(ast.CallStmt)
def call_stmt(node, output):
    output.write('CALL ')
    output.print_node(node.funccall)


@node_printer(ast.CaseExpr)
def case_expr(node, output):
    with output.push_indent():
        output.writes('CASE')
        if node.arg:
            output.print_node(node.arg)
        output.newline()
        output.space(2)
        with output.push_indent():
            output.print_list(node.args, '')
            if node.defresult:
                output.newline()
                output.write('ELSE ')
                output.print_node(node.defresult)
        output.newline()
        output.write('END')


@node_printer(ast.CaseWhen)
def case_when(node, output):
    output.write('WHEN ')
    with output.push_indent(-3):
        output.print_node(node.expr)
        output.newline()
        output.write('THEN ')
        output.print_node(node.result)


@node_printer(ast.CoalesceExpr)
def coalesce_expr(node, output):
    output.write('COALESCE')
    with output.expression(True):
        output.print_list(node.args)


@node_printer(ast.CollateClause)
def collate_clause(node, output):
    if node.arg:
        with output.expression(isinstance(node.arg, ast.A_Expr)):
            output.print_node(node.arg)
    output.swrite('COLLATE ')
    output.print_name(node.collname, '.')


@node_printer(ast.ColumnRef)
def column_ref(node, output):
    output.print_name(node.fields)


class CTEMaterializedPrinter(IntEnumPrinter):
    enum = enums.CTEMaterialize

    def CTEMaterializeAlways(self, node, output):
        output.write(' MATERIALIZED')

    def CTEMaterializeDefault(self, node, output):
        pass

    def CTEMaterializeNever(self, node, output):
        output.write(' NOT MATERIALIZED')


cte_materialize_printer = CTEMaterializedPrinter()


@node_printer(ast.CTECycleClause)
def cte_cycle_clause(node, output):
    output.write('CYCLE ')
    output.print_list(node.cycle_col_list, are_names=True)
    output.write(' SET ')
    output.print_name(node.cycle_mark_column)
    if node.cycle_mark_value:
        output.write(' TO ')
        output.print_node(node.cycle_mark_value)
    if node.cycle_mark_default:
        output.write(' DEFAULT ')
        output.print_node(node.cycle_mark_default)
    output.write(' USING ')
    output.print_name(node.cycle_path_column)


@node_printer(ast.CTECycleClause, ast.TypeCast)
def cte_cycle_clause_type_cast(node, output):
    # This is a variant of the standard TypeCast printer, because within a CTECycleClause they
    # must be spelled as "typename 'value'", not as "CAST('value' AS typename)"
    output.print_node(node.typeName)
    output.write(' ')
    output.print_node(node.arg)


@node_printer(ast.CTESearchClause)
def cte_search_clause(node, output):
    output.write('SEARCH ')
    if node.search_breadth_first:
        output.write('BREADTH ')
    else:
        output.write('DEPTH ')
    output.write('FIRST BY ')
    output.print_list(node.search_col_list, are_names=True)
    output.write(' SET ')
    output.print_name(node.search_seq_column)


@node_printer(ast.CommonTableExpr)
def common_table_expr(node, output):
    output.print_name(node.ctename)
    if node.aliascolnames:
        with output.expression(True):
            if len(node.aliascolnames) > 1:
                output.space(2)
            output.print_name(node.aliascolnames, ',')
        output.indent(-1, False)
        output.newline()

    output.swrite('AS')
    cte_materialize_printer(node.ctematerialized, node, output)
    output.write(' ')
    with output.expression(True):
        output.print_node(node.ctequery)
    if node.search_clause:
        output.newline()
        output.newline()
        output.print_node(node.search_clause)
    if node.cycle_clause:
        output.newline()
        output.newline()
        output.print_node(node.cycle_clause)
    if node.aliascolnames:
        output.dedent()
    output.newline()


@node_printer(ast.ConstraintsSetStmt)
def constraints_set_stmt(node, output):
    output.write('SET CONSTRAINTS ')
    if node.constraints:
        output.print_list(node.constraints)
        output.write(' ')
    else:
        output.write('ALL ')
    if node.deferred:
        output.write('DEFERRED')
    else:
        output.write('IMMEDIATE')


@node_printer(ast.CopyStmt)
def copy_stmt(node, output):
    output.write('COPY')
    if node.relation:
        output.write(' ')
        output.print_node(node.relation)
        if node.attlist:
            output.write(' ')
            with output.expression(True):
                output.print_list(node.attlist, are_names=True)
    if node.query:
        output.write(' ')
        with output.expression(True):
            with output.push_indent():
                output.print_node(node.query)
    if node.is_from:
        output.write(' FROM ')
    else:
        output.write(' TO ')
    if node.is_program:
        output.write('PROGRAM ')
    if node.filename:
        output.write_quoted_string(node.filename)
    else:
        if node.is_from:
            output.write('STDIN')
        else:
            output.write('STDOUT')
    if node.options:
        output.newline()
        output.write('WITH ')
        old_syntax = False
        for option in node.options:
            if isinstance(option.arg, ast.Boolean) or option.defname == 'csv':
                old_syntax = True
                break
        if old_syntax:
            options = []
            for option in node.options:
                if ((option.defname == 'csv'
                     or option.defname == 'format' and option.arg.sval == 'csv')):
                    value = 'CSV'
                elif option.defname == 'force_quote':
                    value = 'FORCE QUOTE ' + output._concat_nodes(option.arg, are_names=True)
                elif option.defname in ('delimiter', 'escape', 'quote'):
                    value = f"{option.defname.upper()} AS '{option.arg.sval}'"
                else:
                    value = option.defname.upper()
                options.append(value)
            output.write(' '.join(options))
        else:
            with output.expression(True):
                output.print_list(node.options)
    if node.whereClause:
        output.newline()
        output.write('WHERE ')
        output.print_node(node.whereClause)


@node_printer(ast.CopyStmt, ast.DefElem)
def copy_stmt_def_elem(node, output):
    option = node.defname
    argv = node.arg
    if option == 'format':
        output.write('FORMAT ')
        output.print_symbol(argv)
    elif option == 'freeze':
        output.write('FREEZE')
        if isinstance(argv, ast.String):
            output.swrite(argv.sval.upper())
        elif isinstance(argv, ast.Integer):
            output.swrite(str(argv.ival))
    elif option == 'delimiter':
        output.write('DELIMITER ')
        output.print_node(argv)
    elif option == 'null':
        output.write('NULL ')
        output.print_node(argv)
    elif option == 'header':
        output.write('HEADER')
        if argv is not None:
            output.swrite(argv.sval.upper())
    elif option == 'quote':
        output.write('QUOTE ')
        output.print_node(argv)
    elif option == 'escape':
        output.write('ESCAPE ')
        output.print_node(argv)
    elif option == 'force_quote':
        output.write('FORCE_QUOTE ')
        # If it is a list print it.
        if isinstance(argv, tuple):
            with output.expression(True):
                output.print_list(argv, are_names=True)
        else:
            output.write('*')
    elif option == 'force_null':
        output.write('FORCE_NULL ')
        with output.expression(True):
            output.print_list(argv, are_names=True)
    elif option == 'force_not_null':
        output.write('FORCE_NOT_NULL ')
        with output.expression(True):
            output.print_list(argv, are_names=True)
    elif option == 'encoding':
        output.write('ENCODING ')
        output.print_node(argv)
    elif option == 'convert_selectively':
        output.write(option)
        output.write(' ')
        with output.expression(True):
            output.print_name(argv)
    elif option == 'default':
        output.write(option)
        output.write(' ')
        output.print_node(argv)
    else:
        raise NotImplementedError(option)


@node_printer(ast.DeclareCursorStmt)
def declare_cursor_stmt(node, output):
    output.write('DECLARE ')
    output.print_name(node.portalname)
    output.write(' ')
    if node.options & enums.CURSOR_OPT_BINARY:
        output.writes('BINARY')
    if node.options & enums.CURSOR_OPT_SCROLL:
        output.writes('SCROLL')
    elif node.options & enums.CURSOR_OPT_NO_SCROLL:
        output.writes('NO SCROLL')
    if node.options & enums.CURSOR_OPT_INSENSITIVE:
        output.writes('INSENSITIVE')
    output.writes('CURSOR')
    if node.options & enums.CURSOR_OPT_HOLD:
        output.writes('WITH HOLD')
    output.newline()
    output.space(2)
    output.write('FOR ')
    with output.push_indent():
        output.print_node(node.query)


@node_printer(ast.DeleteStmt)
def delete_stmt(node, output):
    with output.push_indent():
        if node.withClause:
            output.write('WITH ')
            output.print_node(node.withClause)
            output.newline()
            output.space(2)
            output.indent()

        output.write('DELETE FROM ')
        output.print_node(node.relation)
        if node.usingClause:
            output.newline()
            output.write('USING ')
            output.print_list(node.usingClause)
        if node.whereClause:
            output.newline()
            output.write('WHERE ')
            output.print_node(node.whereClause)
        if node.returningList:
            output.newline()
            output.write('RETURNING ')
            output.print_list(node.returningList)

        if node.withClause:
            output.dedent()


@node_printer(ast.ExecuteStmt)
def execute_stmt(node, output):
    output.write('EXECUTE ')
    output.print_name(node.name)
    if node.params:
        with output.expression(True):
            output.print_list(node.params)


@node_printer(ast.ExplainStmt)
def explain_stmt(node, output):
    output.write('EXPLAIN ')
    if node.options:
        with output.expression(True):
            output.print_list(node.options)
        output.newline()
        output.space(2)
    output.print_node(node.query)


@node_printer(ast.ExplainStmt, ast.DefElem)
def explain_stmt_def_elem(node, output):
    output.print_symbol(node.defname)
    if node.arg is not None:
        output.write(' ')
        output.print_symbol(node.arg)


class FetchDirectionPrinter(IntEnumPrinter):
    enum = enums.FetchDirection

    def FETCH_FORWARD(self, node, output):
        if node.howMany == enums.FETCH_ALL:
            output.write('ALL ')
        elif node.howMany != 1:
            output.write(f'FORWARD {node.howMany} ')

    def FETCH_BACKWARD(self, node, output):
        if node.howMany == enums.FETCH_ALL:
            output.write('BACKWARD ALL ')
        elif node.howMany != 1:
            output.write(f'BACKWARD {node.howMany} ')
        else:
            output.write('PRIOR ')

    def FETCH_ABSOLUTE(self, node, output):
        if node.howMany == 1:
            output.write('FIRST ')
        elif node.howMany == -1:
            output.write('LAST ')
        else:
            output.write(f'ABSOLUTE {node.howMany} ')

    def FETCH_RELATIVE(self, node, output):
        output.write(f'RELATIVE {node.howMany} ')


fetch_direction_printer = FetchDirectionPrinter()


@node_printer(ast.FetchStmt)
def fetch_stmt(node, output):
    output.write('MOVE ' if node.ismove else 'FETCH ')
    fetch_direction_printer(node.direction, node, output)
    output.print_name(node.portalname)


@node_printer(ast.Float)
def float(node, output):
    output.write(node.fval)


@node_printer(ast.FuncCall)
def func_call(node, output):
    name = '.'.join(n.sval for n in node.funcname)
    special_printer = output.get_printer_for_function(name)
    if special_printer is not None:
        special_printer(node, output)
        return

    output.print_name(node.funcname)
    with output.expression(True):
        if node.agg_distinct:
            output.writes('DISTINCT')
        if node.args is None:
            if node.agg_star:
                output.write('*')
        else:
            if node.func_variadic:
                if len(node.args) > 1:
                    output.print_list(node.args[:-1])
                    output.write(', ')
                output.write('VARIADIC ')
                output.print_node(node.args[-1])
            else:
                output.print_list(node.args)
        if node.agg_order:
            if not node.agg_within_group:
                output.swrites('ORDER BY')
                output.print_list(node.agg_order)
            else:
                output.writes(') WITHIN GROUP (ORDER BY')
                output.print_list(node.agg_order)
    if node.agg_filter:
        output.swrites('FILTER (WHERE')
        output.print_node(node.agg_filter)
        output.write(')')
    if node.over:
        output.swrite('OVER ')
        output.print_node(node.over)


@node_printer(ast.FuncCall, ast.WindowDef)
def func_call_window_def(node, output):
    if node.name:
        output.print_name(node.name)
    else:
        window_def(node, output)


@node_printer(ast.GroupingSet)
def grouping_set(node, output):
    kind = node.kind
    if kind == enums.GroupingSetKind.GROUPING_SET_CUBE:
        output.write('CUBE ')
    elif kind == enums.GroupingSetKind.GROUPING_SET_ROLLUP:
        output.write('ROLLUP ')
    elif kind == enums.GroupingSetKind.GROUPING_SET_SETS:
        output.write('GROUPING SETS ')
    elif kind == enums.GroupingSetKind.GROUPING_SET_EMPTY:
        output.write('()')
        return
    elif kind == enums.GroupingSetKind.GROUPING_SET_SIMPLE:
        # FIXME: no idea how to reach this branch
        output.write('SIMPLE ')
    else:  # pragma: no cover
        raise NotImplementedError('Unhandled grouping set kind: %s' % kind)
    with output.expression(True):
        output.print_list(node.content, ',')


@node_printer(ast.GroupingFunc)
def grouping_func(node, output):
    output.write(' GROUPING')
    with output.expression(True):
        output.print_list(node.args)


@node_printer(ast.IndexElem)
def index_elem(node, output):
    if node.name is not None:
        output.print_name(node.name)
    else:
        with output.expression(True):
            output.print_node(node.expr)
    if node.collation:
        output.swrite('COLLATE ')
        output.print_name(node.collation, ',')
    if node.opclass:
        output.write(' ')
        output.print_name(node.opclass, '.')
        if node.opclassopts:
            output.write(' ')
            with output.expression(True):
                output.print_list(node.opclassopts)
    if node.ordering != enums.SortByDir.SORTBY_DEFAULT:
        if node.ordering == enums.SortByDir.SORTBY_ASC:
            output.swrite('ASC')
        elif node.ordering == enums.SortByDir.SORTBY_DESC:
            output.swrite('DESC')
        else:  # pragma: no cover
            raise NotImplementedError('Unhandled ordering: %s' % node.ordering)
    if node.nulls_ordering != enums.SortByNulls.SORTBY_NULLS_DEFAULT:
        output.swrite('NULLS ')
        if node.nulls_ordering == enums.SortByNulls.SORTBY_NULLS_LAST:
            output.write('LAST')
        else:
            output.write('FIRST')


@node_printer(ast.InferClause)
def infer_clause(node, output):
    if node.conname:
        output.swrite('ON CONSTRAINT ')
        output.print_name(node.conname)
    if node.indexElems:
        output.separator()
        with output.expression(True):
            output.print_list(node.indexElems)
    if node.whereClause:
        output.swrite('WHERE ')
        output.print_node(node.whereClause)


@node_printer(ast.Integer)
def integer(node, output):
    output.print_node(node.ival)


@node_printer(ast.InsertStmt)
def insert_stmt(node, output):
    with output.push_indent():
        if node.withClause:
            output.write('WITH ')
            output.print_node(node.withClause)
            output.newline()
            output.space(2)
            output.indent()

        output.write('INSERT INTO ')
        output.print_node(node.relation)
        if node.cols:
            output.write(' ')
            with output.expression(True):
                output.print_list(node.cols)
        else:
            output.separator()
        if node.override:
            if node.override == enums.OverridingKind.OVERRIDING_USER_VALUE:
                output.write(' OVERRIDING USER VALUE ')
            elif node.override == enums.OverridingKind.OVERRIDING_SYSTEM_VALUE:
                output.write(' OVERRIDING SYSTEM VALUE ')
        if node.selectStmt:
            output.newline()
            output.print_node(node.selectStmt)
        else:
            output.write('DEFAULT VALUES')
        if node.onConflictClause:
            output.newline()
            output.write('ON CONFLICT ')
            output.print_node(node.onConflictClause)
        if node.returningList:
            output.newline()
            output.write('RETURNING ')
            output.print_name(node.returningList, ',')

        if node.withClause:
            output.dedent()


@node_printer(ast.IntoClause)
def into_clause(node, output):
    output.print_node(node.rel)
    if node.colNames:
        output.write(' ')
        with output.expression(True):
            output.print_name(node.colNames, ',')
    output.newline()
    with output.push_indent(2):
        if node.accessMethod:
            output.write('USING ')
            output.print_name(node.accessMethod)
            output.newline()
        if node.options:
            output.write('WITH ')
            with output.expression(True):
                output.print_list(node.options)
            output.newline()
        if node.onCommit != enums.OnCommitAction.ONCOMMIT_NOOP:
            output.write('ON COMMIT ')
            if node.onCommit == enums.OnCommitAction.ONCOMMIT_PRESERVE_ROWS:
                output.write('PRESERVE ROWS')
            elif node.onCommit == enums.OnCommitAction.ONCOMMIT_DELETE_ROWS:
                output.write('DELETE ROWS')
            elif node.onCommit == enums.OnCommitAction.ONCOMMIT_DROP:
                output.write('DROP')
            output.newline()
        if node.tableSpaceName:
            output.write('TABLESPACE ')
            output.print_name(node.tableSpaceName)
            output.newline()


@node_printer(ast.JoinExpr)
def join_expr(node, output):
    with output.push_indent():
        with output.expression(bool(node.alias)):
            output.print_node(node.larg)
            output.newline()

            if node.isNatural:
                output.write('NATURAL ')

            jt = enums.JoinType
            if node.jointype == jt.JOIN_INNER:
                if not node.usingClause and not node.quals and not node.isNatural:
                    output.write('CROSS')
                else:
                    output.write('INNER')
            elif node.jointype == jt.JOIN_LEFT:
                output.write('LEFT')
            elif node.jointype == jt.JOIN_FULL:
                output.write('FULL')
            elif node.jointype == jt.JOIN_RIGHT:
                output.write('RIGHT')

            output.swrite('JOIN ')

            if isinstance(node.rarg, ast.JoinExpr):
                output.indent(3, relative=False)
                # need this for:
                # tests/test_printers_roundtrip.py::test_pg_regress_corpus[join.sql] -
                # AssertionError: Statement “select * from   int8_tbl x cross join (int4_tbl x cross join lateral (select x.f1) ss)”
                # from libpg_query/test/sql/postgres_regress/join.sql at line 1998
                with output.expression(not bool(node.rarg.alias)):
                    output.print_node(node.rarg)
                output.newline()
            else:
                output.print_node(node.rarg)

            if node.usingClause:
                output.swrite('USING ')
                with output.expression(True):
                    output.print_name(node.usingClause, ',')
                if node.join_using_alias:
                    output.write(' AS ')
                    output.print_node(node.join_using_alias)
            elif node.quals:
                output.swrite('ON ')
                output.print_node(node.quals)

        if node.alias:
            output.writes(' AS ')
            output.print_name(node.alias)

        if isinstance(node.rarg, ast.JoinExpr):
            output.dedent()


@node_printer(ast.JsonAggConstructor)
def json_agg_constructor(node, output):
    if node.agg_order:
        output.write('ORDER BY ')
        output.print_list(node.agg_order)
    parent_node = node.ancestors[0]
    output.swrite('ABSENT' if parent_node.absent_on_null else 'NULL')
    output.write(' ON NULL')
    if getattr(parent_node, 'unique', False):
        output.swrite('WITH UNIQUE KEYS')
    if node.output:
        output.print_node(node.output)


@node_printer(ast.JsonArrayAgg)
def json_array_agg(node, output):
    output.write('json_arrayagg')
    with output.expression(True):
        output.print_node(node.arg)
        output.print_node(node.constructor)
    # Sigh, the following sub-nodes of JsonAggConstructor must be handled here,
    # because they go outside the json_arrayagg() "function"...
    if node.constructor.agg_filter:
        output.write(' FILTER ')
        with output.expression(True):
            output.write('WHERE ')
            output.print_node(node.constructor.agg_filter)
    if node.constructor.over:
        output.write(' OVER ')
        output.print_node(node.constructor.over)


@node_printer(ast.JsonArrayConstructor)
def json_array_constructor(node, output):
    output.write('json_array')
    with output.expression(True):
        if node.exprs:
            output.print_list(node.exprs)
            output.swrite('ABSENT' if node.absent_on_null else 'NULL')
            output.write(' ON NULL')
        if node.output:
            output.print_node(node.output)


@node_printer(ast.JsonArrayQueryConstructor)
def json_array_query_constructor(node, output):
    output.write('json_array')
    with output.expression(True):
        output.print_node(node.query)
        output.print_node(node.format)
        if node.output:
            output.print_node(node.output)


class JsonEncodingPrinter(IntEnumPrinter):
    enum = enums.JsonEncoding

    def JS_ENC_UTF8(self, node, output):
        output.write('UTF8')

    def JS_ENC_UTF16(self, node, output):
        output.write('UTF16')

    def JS_ENC_UTF32(self, node, output):
        output.write('UTF32')


json_encoding_printer = JsonEncodingPrinter()


class JsonFormatTypePrinter(IntEnumPrinter):
    enum = enums.JsonFormatType

    def JS_FORMAT_JSON(self, node, output):
        output.write('JSON')

    def JS_FORMAT_JSONB(self, node, output):
        output.write('JSONB')


json_format_type_printer = JsonFormatTypePrinter()


@node_printer(ast.JsonFormat)
def json_format(node, output):
    if node.format_type != enums.JsonFormatType.JS_FORMAT_DEFAULT:
        output.swrite('FORMAT ')
        json_format_type_printer(node.format_type, node, output)
    if node.encoding != enums.JsonEncoding.JS_ENC_DEFAULT:
        output.swrite('ENCODING ')
        json_encoding_printer(node.encoding, node, output)


@node_printer(ast.JsonIsPredicate)
def json_is_predicate(node, output):
    output.print_node(node.expr)
    output.print_node(node.format)
    output.write(' IS ')
    json_value_type_printer(node.item_type, node, output)
    if node.unique_keys:
        output.write(' WITH UNIQUE KEYS')


@node_printer(ast.JsonKeyValue)
def json_key_value(node, output):
    output.print_node(node.key)
    output.writes(':')
    output.print_node(node.value)


@node_printer(ast.JsonObjectAgg)
def json_object_agg(node, output):
    output.write('json_objectagg')
    with output.expression(True):
        output.print_node(node.arg)
        output.print_node(node.constructor)
    # Sigh, the following sub-nodes of JsonAggConstructor must be handled here,
    # because they go outside the json_objectagg() "function"...
    if node.constructor.agg_filter:
        output.write(' FILTER ')
        with output.expression(True):
            output.write('WHERE ')
            output.print_node(node.constructor.agg_filter)
    if node.constructor.over:
        output.write(' OVER ')
        output.print_node(node.constructor.over)


@node_printer(ast.JsonObjectConstructor)
def json_object_constructor(node, output):
    output.write('json_object')
    with output.expression(True):
        if node.exprs:
            output.print_list(node.exprs)
        if node.absent_on_null:
            output.swrite('ABSENT ON NULL')
        if node.unique:
            output.swrite('WITH UNIQUE KEYS')
        if node.output:
            output.print_node(node.output)


@node_printer(ast.JsonOutput)
def json_output(node, output):
    if node.returning:
        output.swrite('RETURNING ')
        output.print_node(node.typeName)
        output.print_node(node.returning)


@node_printer(ast.JsonReturning)
def json_returning(node, output):
    output.print_node(node.format)


@node_printer(ast.JsonValueExpr)
def json_value_expr(node, output):
    output.print_node(node.raw_expr)
    output.print_node(node.format)


class JsonValueTypePrinter(IntEnumPrinter):
    enum = enums.JsonValueType

    def JS_TYPE_ANY(self, node, output):
        output.write('JSON')

    def JS_TYPE_OBJECT(self, node, output):
        output.write('JSON OBJECT')

    def JS_TYPE_ARRAY(self, node, output):
        output.write('JSON ARRAY')

    def JS_TYPE_SCALAR(self, node, output):
        output.write('JSON SCALAR')


json_value_type_printer = JsonValueTypePrinter()


@node_printer(ast.LockingClause)
def locking_clause(node, output):
    lcs = enums.LockClauseStrength
    if node.strength == lcs.LCS_FORKEYSHARE:
        output.write('KEY SHARE')
    elif node.strength == lcs.LCS_FORSHARE:
        output.write('SHARE')
    elif node.strength == lcs.LCS_FORNOKEYUPDATE:
        output.write('NO KEY UPDATE')
    elif node.strength == lcs.LCS_FORUPDATE:
        output.write('UPDATE')
    if node.lockedRels:
        output.swrites('OF')
        output.print_list(node.lockedRels)
    lwp = enums.LockWaitPolicy
    if node.waitPolicy == lwp.LockWaitSkip:
        output.swrite('SKIP LOCKED')
    elif node.waitPolicy == lwp.LockWaitError:
        output.swrite('NOWAIT')


@node_printer(ast.ListenStmt)
def listen_stmt(node, output):
    output.write('LISTEN ')
    output.print_name(node.conditionname)


@node_printer(ast.MergeStmt)
def merge_stmt(node, output):
    with output.push_indent():
        if node.withClause is not None:
            output.write('WITH ')
            output.print_node(node.withClause)
            output.newline()
            output.space(2)
            output.indent()

        output.write('MERGE INTO ')
        output.print_node(node.relation)
        output.newline()

        output.write('USING ')
        with output.push_indent():
            output.print_node(node.sourceRelation)
            if isinstance(node.sourceRelation, ast.RangeSubselect):
                output.newline()
            output.swrite('ON ')
            output.print_node(node.joinCondition)

        for when in node.mergeWhenClauses:
            output.newline()
            output.write('WHEN ')
            if not when.matched:
                output.write('NOT ')
            output.write('MATCHED ')
            if when.condition is not None:
                output.write('AND ')
                output.print_node(when.condition)
            output.swrite('THEN')
            if when.commandType in (enums.CmdType.CMD_NOTHING, enums.CmdType.CMD_DELETE):
                output.space()
            else:
                output.newline()
            output.print_node(when)

        if node.withClause is not None:
            output.dedent()


@node_printer(ast.MergeWhenClause)
def merge_when_clause(node, output):
    oke = enums.OverridingKind

    if node.commandType == enums.CmdType.CMD_NOTHING:
        output.write('DO NOTHING')
    elif node.commandType == enums.CmdType.CMD_DELETE:
        output.write('DELETE')
    elif node.commandType == enums.CmdType.CMD_INSERT:
        with output.push_indent(2):
            output.write('INSERT ')
            if node.targetList is not None:
                with output.expression(True):
                    output.print_list(node.targetList)
                output.newline()
            if node.override != oke.OVERRIDING_NOT_SET:
                ouv = 'USER' if node.override == oke.OVERRIDING_USER_VALUE else 'SYSTEM'
                output.write(f'OVERRIDING {ouv} VALUE')
                output.newline()
            if node.values is None:
                output.write('DEFAULT VALUES')
            else:
                output.write('VALUES ')
                with output.expression(True):
                    output.print_list(node.values)
    elif node.commandType == enums.CmdType.CMD_UPDATE:
        with output.push_indent(2):
            output.write('UPDATE SET ')
            output.print_list(node.targetList)


@node_printer(ast.MinMaxExpr)
def min_max_expr(node, output):
    if node.op == enums.MinMaxOp.IS_GREATEST:
        output.write('GREATEST')
    else:
        output.write('LEAST')
    with output.expression(True):
        output.print_list(node.args)


@node_printer(ast.MultiAssignRef)
def multi_assign_ref(node, output):
    output.print_node(node.source)


@node_printer(ast.NamedArgExpr)
def named_arg_expr(node, output):
    output.print_name(node.name)
    output.write(' => ')
    output.print_node(node.arg)


@node_printer(ast.NullTest)
def null_test(node, output):
    output.print_node(node.arg)
    output.write(' IS')
    if node.nulltesttype == enums.NullTestType.IS_NOT_NULL:
        output.write(' NOT')
    output.write(' NULL')


@node_printer(ast.ParamRef)
def param_ref(node, output):
    output.write('$%d' % node.number)


@node_printer(ast.PrepareStmt)
def prepare_stmt(node, output):
    output.write('PREPARE ')
    output.print_node(node.name, is_name=True)
    if node.argtypes:
        with output.expression(True):
            output.print_list(node.argtypes)
    output.write(' AS')
    output.newline()
    with output.push_indent(2):
        output.print_node(node.query)


@node_printer(ast.OnConflictClause)
def on_conflict_clause(node, output):
    oca = enums.OnConflictAction
    if node.infer:
        output.print_node(node.infer)
    if node.action == oca.ONCONFLICT_NOTHING:
        output.write('DO NOTHING')
    elif node.action == oca.ONCONFLICT_UPDATE:
        output.newline()
        with output.push_indent(3):
            output.write('DO UPDATE')
            output.newline()
            output.space(2)
            output.write('SET ')
            output.print_list(node.targetList)
            if node.whereClause:
                output.newline()
                output.space(2)
                output.write('WHERE ')
                output.print_node(node.whereClause)


@node_printer(ast.RangeFunction)
def range_function(node, output):
    if node.lateral:
        output.write('LATERAL ')
    if node.is_rowsfrom:
        output.write('ROWS FROM ')
    with output.expression(node.is_rowsfrom):
        first = True
        for fun, cdefs in node.functions:
            if first:
                first = False
            else:
                output.write(', ')
            output.print_node(fun)
            if cdefs:
                # FIXME: find a way to get here
                output.write(' AS ')
                with output.expression(True):
                    output.print_list(cdefs)
    if node.ordinality:
        output.write(' WITH ORDINALITY')
    if node.alias:
        output.write(' AS ')
        output.print_node(node.alias)
    if node.coldeflist:
        if not node.alias:
            output.write(' AS ')
        with output.expression(True):
            output.print_list(node.coldeflist, ',')


@node_printer(ast.RangeSubselect)
def range_subselect(node, output):
    if node.lateral:
        output.write('LATERAL')
    output.maybe_write_space()
    with output.expression(True):
        with output.push_indent():
            output.print_node(node.subquery)
    if node.alias:
        output.write(' AS ')
        output.print_name(node.alias)


@node_printer(ast.RangeTableFunc)
def range_table_func(node, output):
    if node.lateral:
        output.write('LATERAL ')
    output.write('xmltable')
    with output.expression(True):
        with output.push_indent():
            if node.namespaces:
                output.write('xmlnamespaces')
                with output.expression(True):
                    output.print_list(node.namespaces)
                output.writes(',')
                output.newline()
            with output.expression(True):
                output.print_node(node.rowexpr)
            output.newline()
            output.write('PASSING ')
            output.print_node(node.docexpr)
            output.newline()
            output.write('COLUMNS ')
            output.print_list(node.columns)
    if node.alias:
        # FIXME: find a way to get here
        output.write(' AS ')
        output.print_node(node.alias)


@node_printer(ast.RangeTableFunc, ast.ResTarget)
def range_table_func_res_target(node, output):
    if not node.name:
        output.write('DEFAULT ')
    output.print_node(node.val)
    if node.name:
        output.write(' AS ')
        output.print_name(node.name)


@node_printer(ast.RangeTableFuncCol)
def range_table_func_col(node, output):
    output.print_node(node.colname, is_name=True)
    output.write(' ')
    if node.for_ordinality:
        output.write('FOR ORDINALITY')
    else:
        output.print_node(node.typeName)
        if node.colexpr:
            output.swrite('PATH ')
            output.print_node(node.colexpr)
        if node.coldefexpr:
            output.swrite('DEFAULT ')
            output.print_node(node.coldefexpr)
        if node.is_not_null:
            output.swrite('NOT NULL')


@node_printer(ast.RangeVar)
def range_var(node, output):
    if not node.inh:
        output.write('ONLY ')
    if node.catalogname:
        output.print_name(node.catalogname)
        output.write('.')
    if node.schemaname:
        output.print_name(node.schemaname)
        output.write('.')
    output.print_name(node.relname)
    alias = node.alias
    if alias:
        output.write(' AS ')
        output.print_name(alias)


@node_printer(ast.RangeTableSample)
def range_table_sample(node, output):
    output.print_node(node.relation)
    output.write(' TABLESAMPLE ')
    output.print_name(node.method, ' ')
    with output.expression(True):
        output.print_list(node.args, ' ')
    if node.repeatable:
        output.write(' REPEATABLE ')
        with output.expression(True):
            output.print_node(node.repeatable)


@node_printer(ast.RawStmt)
def raw_stmt(node, output):
    output.print_node(node.stmt)


@node_printer(ast.ResTarget)
def res_target(node, output):
    if node.val:
        output.print_node(node.val)
        if node.name:
            output.write(' AS ')
            output.print_name(node.name)
    else:
        output.print_name(node.name)
    if node.indirection:
        print_indirection(node.indirection, output)


@node_printer(ast.RowExpr)
def row_expr(node, output):
    if node.row_format == enums.CoercionForm.COERCE_EXPLICIT_CALL:
        output.write('ROW')
        with output.expression(True):
            if node.args:
                output.print_list(node.args)
    elif node.row_format == enums.CoercionForm.COERCE_IMPLICIT_CAST:
        with output.expression(True):
            output.print_list(node.args)
    else:
        raise NotImplementedError('Coercion type not implemented: %s' %
                                  node.row_format)


def _select_needs_to_be_wrapped_in_parens(node):
    # Accordingly with https://www.postgresql.org/docs/current/sql-select.html, a SELECT
    # statement on either sides of UNION/INTERSECT/EXCEPT must be wrapped in parens if it
    # contains ORDER BY/LIMIT/... or is a nested UNION/INTERSECT/EXCEPT
    return bool(node.sortClause
                or node.limitCount
                or node.limitOffset
                or node.lockingClause
                or node.withClause
                or node.op != enums.SetOperation.SETOP_NONE)


@node_printer(ast.SelectStmt)
def select_stmt(node, output):
    with output.push_indent():
        if node.withClause:
            output.write('WITH ')
            output.print_node(node.withClause)
            output.newline()
            output.space(2)
            output.indent()

        so = enums.SetOperation

        if node.valuesLists:
            # Is this a SELECT ... FROM (VALUES (...))?
            with output.expression(isinstance(node.ancestors[0], ast.RangeSubselect)):
                output.write('VALUES ')
                output.print_lists(node.valuesLists)
        elif node.op != so.SETOP_NONE and (node.larg or node.rarg):
            with output.push_indent():
                if node.larg:
                    with output.expression(_select_needs_to_be_wrapped_in_parens(node.larg)):
                        output.print_node(node.larg)
                output.newline()
                output.newline()
                if node.op == so.SETOP_UNION:
                    output.write('UNION')
                elif node.op == so.SETOP_INTERSECT:
                    output.write('INTERSECT')
                elif node.op == so.SETOP_EXCEPT:
                    output.write('EXCEPT')
                if node.all:
                    output.write(' ALL')
                output.newline()
                output.newline()
                if node.rarg:
                    with output.expression(_select_needs_to_be_wrapped_in_parens(node.rarg)):
                        output.print_node(node.rarg)
        else:
            output.write('SELECT')
            if node.distinctClause:
                output.write(' DISTINCT')
                if node.distinctClause[0]:
                    output.write(' ON ')
                    with output.expression(True):
                        output.print_list(node.distinctClause)
            if node.targetList:
                output.write(' ')
                output.print_list(node.targetList)
            if node.intoClause:
                output.newline()
                output.write('INTO ')
                if node.intoClause.rel.relpersistence == enums.RELPERSISTENCE_UNLOGGED:
                    output.write('UNLOGGED ')
                elif node.intoClause.rel.relpersistence == enums.RELPERSISTENCE_TEMP:
                    output.write('TEMPORARY ')
                output.print_node(node.intoClause)
            if node.fromClause:
                output.newline()
                output.write('FROM ')
                output.print_list(node.fromClause)
            if node.whereClause:
                output.newline()
                output.write('WHERE ')
                output.print_node(node.whereClause)
            if node.groupClause:
                output.newline()
                output.write('GROUP BY ')
                if node.groupDistinct:
                    output.write('DISTINCT ')
                output.print_list(node.groupClause)
            if node.havingClause:
                output.newline()
                output.write('HAVING ')
                output.print_node(node.havingClause)
            if node.windowClause:
                output.newline()
                output.write('WINDOW ')
                output.print_list(node.windowClause)
        if node.sortClause:
            output.newline()
            output.write('ORDER BY ')
            output.print_list(node.sortClause)
        if node.limitCount:
            output.newline()
            if node.limitOption == enums.LimitOption.LIMIT_OPTION_COUNT:
                output.write('LIMIT ')
            elif node.limitOption == enums.LimitOption.LIMIT_OPTION_WITH_TIES:
                output.write('FETCH FIRST ')
            if isinstance(node.limitCount, ast.A_Const) and node.limitCount.isnull:
                output.write('ALL')
            else:
                with output.expression(isinstance(node.limitCount, ast.A_Expr)
                                       and node.limitCount.kind == enums.A_Expr_Kind.AEXPR_OP):
                    output.print_node(node.limitCount)
            if node.limitOption == enums.LimitOption.LIMIT_OPTION_WITH_TIES:
                output.write(' ROWS WITH TIES ')
        if node.limitOffset:
            output.newline()
            output.write('OFFSET ')
            output.print_node(node.limitOffset)
        if node.lockingClause:
            output.newline()
            output.write('FOR ')
            output.print_list(node.lockingClause)

        if node.withClause:
            output.dedent()


@node_printer(ast.SetToDefault)
def set_to_default(node, output):
    output.write('DEFAULT')


@node_printer(ast.SortBy)
def sort_by(node, output):
    output.print_node(node.node)
    sbd = enums.SortByDir
    if node.sortby_dir == sbd.SORTBY_ASC:
        output.swrite('ASC')
    elif node.sortby_dir == sbd.SORTBY_DESC:
        output.swrite('DESC')
    elif node.sortby_dir == sbd.SORTBY_USING:
        output.swrite('USING ')
        output.print_symbol(node.useOp)
    sbn = enums.SortByNulls
    if node.sortby_nulls != sbn.SORTBY_NULLS_DEFAULT:
        output.swrite('NULLS ')
        output.write('FIRST' if node.sortby_nulls == sbn.SORTBY_NULLS_FIRST else 'LAST')


class SQLValueFunctionOpPrinter(IntEnumPrinter):
    enum = enums.SQLValueFunctionOp

    def SVFOP_CURRENT_CATALOG(self, node, output):
        output.write('CURRENT_CATALOG')

    def SVFOP_CURRENT_DATE(self, node, output):
        output.write('CURRENT_DATE')

    def SVFOP_CURRENT_ROLE(self, node, output):
        output.write('CURRENT_ROLE')

    def SVFOP_CURRENT_SCHEMA(self, node, output):
        output.write('CURRENT_SCHEMA')

    def SVFOP_CURRENT_TIME(self, node, output):
        output.write('CURRENT_TIME')

    def SVFOP_CURRENT_TIMESTAMP(self, node, output):
        output.write('CURRENT_TIMESTAMP')

    def SVFOP_CURRENT_TIMESTAMP_N(self, node, output):  # pragma: no cover
        output.write('CURRENT_TIMESTAMP')
        with output.expression(True):
            output.write(str(node.typmod))

    def SVFOP_CURRENT_TIME_N(self, node, output):  # pragma: no cover
        output.write('CURRENT_TIME')
        with output.expression(True):
            output.write(str(node.typmod))

    def SVFOP_CURRENT_USER(self, node, output):
        output.write('CURRENT_USER')

    def SVFOP_LOCALTIME(self, node, output):
        output.write('LOCALTIME')

    def SVFOP_LOCALTIMESTAMP(self, node, output):
        output.write('LOCALTIMESTAMP')

    def SVFOP_LOCALTIMESTAMP_N(self, node, output):  # pragma: no cover
        output.write('LOCALTIMESTAMP')
        with output.expression(True):
            output.write(str(node.typmod))

    def SVFOP_LOCALTIME_N(self, node, output):  # pragma: no cover
        output.write('LOCALTIME')
        with output.expression(True):
            output.write(str(node.typmod))

    def SVFOP_SESSION_USER(self, node, output):
        output.write('SESSION_USER')

    def SVFOP_USER(self, node, output):
        output.write('USER')


sql_value_function_op_printer = SQLValueFunctionOpPrinter()


@node_printer(ast.SQLValueFunction)
def sql_value_function(node, output):
    sql_value_function_op_printer(node.op, node, output)


@node_printer(ast.String)
def string(node, output, is_name=False, is_symbol=False):
    output.print_node(node.sval, is_name=is_name, is_symbol=is_symbol)


@node_printer(ast.SubLink)
def sub_link(node, output):
    slt = enums.SubLinkType

    if node.subLinkType == slt.EXISTS_SUBLINK:
        output.write('EXISTS ')
    elif node.subLinkType == slt.ALL_SUBLINK:
        output.print_node(node.testexpr)
        output.write(' ')
        output.write(get_string_value(node.operName))
        output.write(' ALL ')
    elif node.subLinkType == slt.ANY_SUBLINK:
        output.print_node(node.testexpr)
        if node.operName:
            output.write(' ')
            output.write(get_string_value(node.operName))
            output.write(' ANY ')
        else:
            output.write(' IN ')
    elif node.subLinkType == slt.EXPR_SUBLINK:
        pass
    elif node.subLinkType == slt.ARRAY_SUBLINK:
        output.write('ARRAY')
    elif node.subLinkType in (slt.MULTIEXPR_SUBLINK,
                              slt.ROWCOMPARE_SUBLINK):  # pragma: no cover
        # FIXME: figure out how the get here
        raise NotImplementedError('SubLink of type %s not supported yet'
                                  % node.subLinkType)

    with output.expression(True):
        with output.push_indent():
            output.print_node(node.subselect)


@node_printer(ast.TransactionStmt)
def transaction_stmt(node, output):
    tsk = enums.TransactionStmtKind
    if node.kind == tsk.TRANS_STMT_BEGIN:
        output.write('BEGIN ')
        if node.options:
            output.print_list(node.options)
    elif node.kind == tsk.TRANS_STMT_START:
        output.write('START TRANSACTION ')
        if node.options:
            output.print_list(node.options)
    elif node.kind == tsk.TRANS_STMT_COMMIT:
        output.write('COMMIT ')
        if node.chain:
            output.write('AND CHAIN ')
    elif node.kind == tsk.TRANS_STMT_ROLLBACK:
        output.write('ROLLBACK ')
        if node.chain:
            output.write('AND CHAIN ')
    elif node.kind == tsk.TRANS_STMT_SAVEPOINT:
        output.write('SAVEPOINT ')
        output.write(node.savepoint_name)
    elif node.kind == tsk.TRANS_STMT_RELEASE:
        output.write('RELEASE ')
        output.write(node.savepoint_name)
    elif node.kind == tsk.TRANS_STMT_ROLLBACK_TO:
        output.write('ROLLBACK TO SAVEPOINT ')
        output.write(node.savepoint_name)
    elif node.kind == tsk.TRANS_STMT_PREPARE:
        output.write('PREPARE TRANSACTION ')
        output.write("'%s'" % node.gid)
    elif node.kind == tsk.TRANS_STMT_COMMIT_PREPARED:
        output.write('COMMIT PREPARED ')
        output.write("'%s'" % node.gid)
    elif node.kind == tsk.TRANS_STMT_ROLLBACK_PREPARED:
        output.write('ROLLBACK PREPARED ')
        output.write("'%s'" % node.gid)


@node_printer(ast.TransactionStmt, ast.DefElem)
def transaction_stmt_def_elem(node, output):
    value = node.defname
    argv = node.arg.val
    if value == 'transaction_isolation':
        output.write('ISOLATION LEVEL ')
        output.write(argv.sval.upper())
    elif value == 'transaction_read_only':
        output.write('READ ')
        if argv.ival == 0:
            output.write('WRITE')
        else:
            output.write('ONLY')
    elif value == 'transaction_deferrable':
        if argv.ival == 0:
            output.write('NOT ')
        output.write('DEFERRABLE')
    else:  # pragma: no cover
        raise NotImplementedError('Unhandled defname value %r' % value)


@node_printer(ast.TruncateStmt)
def truncate_stmt(node, output):
    output.write('TRUNCATE TABLE ')
    output.print_list(node.relations)
    if node.restart_seqs:
        output.write(' RESTART IDENTITY')
    if node.behavior == enums.DropBehavior.DROP_CASCADE:
        output.write(' CASCADE')


@node_printer(ast.TypeCast)
def type_cast(node, output):
    if isinstance(node.arg, ast.A_Const):
        fqtn = '.'.join(n.sval for n in node.typeName.names)

        if fqtn == 'pg_catalog.bpchar' and node.typeName.typmods is None:
            output.write('char ')
            output.print_node(node.arg)
            return

    output.write('CAST')
    with output.expression(True):
        output.print_node(node.arg)
        output.write(' AS ')
        output.print_node(node.typeName)


# Constants taken from PG's include/utils/datetime.h: seem safe to assume they won't change

MONTH = 1 << 1
YEAR = 1 << 2
DAY = 1 << 3
HOUR = 1 << 10
MINUTE = 1 << 11
SECOND = 1 << 12

# Map interval's typmod to string representation
interval_ranges = {
    YEAR:                         'year',
    MONTH:                        'month',
    DAY:                          'day',
    HOUR:                         'hour',
    MINUTE:                       'minute',
    SECOND:                       'second',
    YEAR | MONTH:                 'year to month',
    DAY | HOUR:                   'day to hour',
    DAY | HOUR | MINUTE:          'day to minute',
    DAY | HOUR | MINUTE | SECOND: 'day to second',
    HOUR | MINUTE:                'hour to minute',
    HOUR | MINUTE | SECOND:       'hour to second',
    MINUTE | SECOND:              'minute to second',
}
del MONTH, YEAR, DAY, HOUR, MINUTE, SECOND


# Map system type name to generic one
system_types = {
    'pg_catalog.bool':        ('boolean', ''),
    'pg_catalog.bpchar':      ('char', ''),
    'pg_catalog.float4':      ('real', ''),
    'pg_catalog.float8':      ('double precision', ''),
    'pg_catalog.int2':        ('smallint', ''),
    'pg_catalog.int4':        ('integer', ''),
    'pg_catalog.int8':        ('bigint', ''),
    'pg_catalog.interval':    ('interval', ''),
    'pg_catalog.numeric':     ('numeric', ''),
    'pg_catalog.time':        ('time', ''),
    'pg_catalog.timestamp':   ('timestamp', ''),
    'pg_catalog.timestamptz': ('timestamp', ' with time zone'),
    'pg_catalog.timetz':      ('time', ' with time zone'),
    'pg_catalog.varbit':      ('bit varying', ''),
    'pg_catalog.varchar':     ('varchar', ''),
}


@node_printer(ast.TypeName)
def type_name(node, output):
    if node.setof:
        output.writes('SETOF')
    name = '.'.join(n.sval for n in node.names)
    suffix = ''
    if name in system_types:
        prefix, suffix = system_types[name]
        output.write(prefix)
    else:
        if name == 'char':
            output.write('"char"')
        else:
            output.print_name(node.names)
    if node.pct_type:
        output.write('%TYPE')
    else:
        if node.typmods:
            if name == 'pg_catalog.interval':
                typmod = node.typmods[0].val.ival
                if typmod in interval_ranges:
                    output.swrite(interval_ranges[typmod])
                if len(node.typmods) == 2:
                    output.write(' ')
                    with output.expression(True):
                        output.print_node(node.typmods[1])
            else:
                # Simplify "char(1)" to just "char"
                if ((name != 'pg_catalog.bpchar'
                     or len(node.typmods) > 1
                     or node.typmods[0].val.ival != 1)):
                    with output.expression(True):
                        output.print_list(node.typmods, ',', standalone_items=False)
        output.write(suffix)
        if node.arrayBounds:
            for ab in node.arrayBounds:
                output.write('[')
                if ab.ival >= 0:
                    output.print_node(ab)
                output.write(']')


@node_printer(ast.VariableSetStmt, ast.TypeCast)
def variable_set_stmt_type_cast(node, output):
    # This is a variant of the standard TypeCast printer, to handle the special case of
    # ”SET TIME ZONE INTERVAL 'xx' hour TO minute”, not as "CAST('xx' AS interval...)"
    type_name = '.'.join(n.sval for n in node.typeName.names)
    if type_name == 'pg_catalog.interval':
        output.write('INTERVAL ')
        output.print_node(node.arg)
        typmod = node.typeName.typmods[0].val.ival
        if typmod in interval_ranges:
            output.swrite(interval_ranges[typmod])
    else:
        raise NotImplementedError('Unhandled typecast to %r' % type_name)


@node_printer(ast.UpdateStmt)
def update_stmt(node, output):
    with output.push_indent():
        if node.withClause:
            output.write('WITH ')
            output.print_node(node.withClause)
            output.newline()
            output.space(2)
            output.indent()

        output.write('UPDATE ')
        output.print_node(node.relation)
        output.newline()
        output.write('SET ')
        output.print_list(node.targetList)
        if node.fromClause:
            output.newline()
            output.write('FROM ')
            output.print_list(node.fromClause)
        if node.whereClause:
            output.newline()
            output.write('WHERE ')
            output.print_node(node.whereClause)
        if node.returningList:
            output.newline()
            output.write('RETURNING ')
            first = True
            for elem in node.returningList:
                if first:
                    first = False
                else:
                    output.write(', ')
                output.print_node(elem.val)
                if elem.name:
                    output.write(' AS ')
                    output.print_name(elem.name)
        if node.withClause:
            output.dedent()


@node_printer(ast.UnlistenStmt)
def unlisten_stmt(node, output):
    output.write('UNLISTEN ')
    if node.conditionname:
        output.print_name(node.conditionname)
    else:
        output.write('*')


@node_printer(ast.WithClause)
def with_clause(node, output):
    relindent = -2
    if node.recursive:
        relindent -= output.write('RECURSIVE ')
    output.print_list(node.ctes, relative_indent=relindent)


@node_printer(ast.WindowDef)
def window_def(node, output):
    if node.name:
        output.print_name(node.name)
        output.write(' AS ')
    with output.expression(True):
        if node.refname:
            output.print_name(node.refname)
        with output.push_indent():
            if node.partitionClause:
                output.write('PARTITION BY ')
                output.print_list(node.partitionClause)
            if node.orderClause:
                if node.partitionClause:
                    output.newline()
                output.write('ORDER BY ')
                output.print_list(node.orderClause)
            if node.frameOptions & enums.FRAMEOPTION_NONDEFAULT:
                if node.partitionClause or node.orderClause:
                    output.newline()
                fo = node.frameOptions
                if fo & enums.FRAMEOPTION_RANGE:
                    output.writes('RANGE')
                elif fo & enums.FRAMEOPTION_ROWS:
                    output.writes('ROWS')
                elif fo & enums.FRAMEOPTION_GROUPS:
                    output.writes('GROUPS')
                if fo & enums.FRAMEOPTION_BETWEEN:
                    output.writes('BETWEEN')
                if fo & enums.FRAMEOPTION_START_UNBOUNDED_PRECEDING:
                    output.writes('UNBOUNDED PRECEDING')
                elif fo & enums.FRAMEOPTION_START_UNBOUNDED_FOLLOWING:  # pragma: no cover
                    # Disallowed
                    #output.writes('UNBOUNDED FOLLOWING')
                    raise RuntimeError('Unexpected "UNBOUNDED FOLLOWING" disallowed option')
                elif fo & enums.FRAMEOPTION_START_CURRENT_ROW:
                    output.writes('CURRENT ROW')
                elif fo & enums.FRAMEOPTION_START_OFFSET_PRECEDING:
                    output.print_node(node.startOffset)
                    output.swrites('PRECEDING')
                elif fo & enums.FRAMEOPTION_START_OFFSET_FOLLOWING:
                    output.print_node(node.startOffset)
                    output.swrites('FOLLOWING')
                if fo & enums.FRAMEOPTION_BETWEEN:
                    output.writes('AND')
                    if fo & enums.FRAMEOPTION_END_UNBOUNDED_PRECEDING:  # pragma: no cover
                        # Disallowed
                        #output.writes('UNBOUNDED PRECEDING')
                        raise RuntimeError('Unexpected "UNBOUNDED PRECEDING" disallowed option')
                    elif fo & enums.FRAMEOPTION_END_UNBOUNDED_FOLLOWING:
                        output.writes('UNBOUNDED FOLLOWING')
                    elif fo & enums.FRAMEOPTION_END_CURRENT_ROW:
                        output.writes('CURRENT ROW')
                    elif fo & enums.FRAMEOPTION_END_OFFSET_PRECEDING:
                        output.print_node(node.endOffset)
                        output.swrites('PRECEDING')
                    elif fo & enums.FRAMEOPTION_END_OFFSET_FOLLOWING:
                        output.print_node(node.endOffset)
                        output.swrites('FOLLOWING')
                    if fo & enums.FRAMEOPTION_EXCLUDE_CURRENT_ROW:
                        output.swrite('EXCLUDE CURRENT ROW')
                    elif fo & enums.FRAMEOPTION_EXCLUDE_GROUP:
                        output.swrite('EXCLUDE GROUP')
                    elif fo & enums.FRAMEOPTION_EXCLUDE_TIES:
                        output.swrite('EXCLUDE TIES')


def print_indirection(node, output):
    for subnode in node:
        if isinstance(subnode, ast.String):
            output.write('.')
        output.print_node(subnode, is_name=True)


@node_printer((ast.MergeWhenClause, ast.OnConflictClause, ast.UpdateStmt), ast.ResTarget)
def update_stmt_res_target(node, output):
    if isinstance(node.val, ast.MultiAssignRef):
        if node.val.colno == 1:
            output.write('( ')
            output.indent(-2)
        output.print_name(node.name)
        if node.indirection:
            print_indirection(node.indirection, output)
        if node.val.colno == node.val.ncolumns:
            output.dedent()
            output.write(') = ')
            output.print_node(node.val)
    else:
        parent_node = abs(node.ancestors).node
        is_merge_insert = (isinstance(parent_node, ast.MergeWhenClause)
                           and parent_node.commandType == enums.CmdType.CMD_INSERT)
        if is_merge_insert:
            output.print_name(node.name)
        else:
            if node.name:
                output.print_name(node.name)
                if node.indirection:
                    print_indirection(node.indirection, output)
                output.write(' = ')
            output.print_node(node.val)


class XmlOptionTypePrinter(IntEnumPrinter):
    enum = enums.XmlOptionType

    def XMLOPTION_DOCUMENT(self, node, output):
        output.write('document ')

    def XMLOPTION_CONTENT(self, node, output):
        output.write('content ')


xml_option_type_printer = XmlOptionTypePrinter()


class XmlStandaloneTypePrinter(IntEnumPrinter):
    enum = enums.XmlStandaloneType

    def XML_STANDALONE_YES(self, node, output):
        output.write(', STANDALONE YES')

    def XML_STANDALONE_NO(self, node, output):
        output.write(', STANDALONE NO')

    def XML_STANDALONE_NO_VALUE(self, node, output):
        output.write(', STANDALONE NO VALUE')

    def XML_STANDALONE_OMITTED(self, node, output):
        pass


xml_standalone_type_printer = XmlStandaloneTypePrinter()


class XmlExprOpPrinter(IntEnumPrinter):
    enum = enums.XmlExprOp

    def IS_XMLCONCAT(self, node, output):  # XMLCONCAT(args)
        output.write('xmlconcat')
        with output.expression(True):
            output.print_list(node.args)

    def IS_XMLELEMENT(self, node, output):  # XMLELEMENT(name, xml_attributes, args)
        output.write('xmlelement(name ')
        output.print_name(node.name)
        if node.named_args:
            output.write(', xmlattributes')
            with output.expression(True):
                output.print_list(node.named_args)
        if node.args:
            output.write(', ')
            output.print_list(node.args)
        output.write(')')

    def IS_XMLFOREST(self, node, output):  # XMLFOREST(xml_attributes)
        output.write('xmlforest')
        with output.expression(True):
            output.print_list(node.named_args)

    def IS_XMLPARSE(self, node, output):  # XMLPARSE(text, is_doc, preserve_ws)
        output.write('xmlparse')
        with output.expression(True):
            xml_option_type_printer(node.xmloption, node, output)
            arg, preserve_ws = node.args
            output.print_node(arg)
            if preserve_ws.val.boolval:
                # FIXME: find a way to get here
                output.write(' PRESERVE WHITESPACE')

    def IS_XMLPI(self, node, output):  # XMLPI(name [, args])
        output.write('xmlpi')
        with output.expression(True):
            output.write('name ')
            output.print_name(node.name)
            if node.args:
                output.write(', ')
                output.print_list(node.args)

    def IS_XMLROOT(self, node, output):  # XMLROOT(xml, version, standalone)
        output.write('xmlroot')
        with output.expression(True):
            xml, version, standalone = node.args
            output.print_node(xml)
            output.write(', version ')
            if version.isnull:
                output.write('NO VALUE')
            else:
                output.print_node(version)
            xml_standalone_type_printer(standalone.val, node, output)

    def IS_XMLSERIALIZE(self, node, output):  # XMLSERIALIZE(is_document, xmlval)
        raise NotImplementedError('IS_XMLSERIALIZE??')

    def IS_DOCUMENT(self, node, output):  # xmlval IS DOCUMENT
        output.print_node(node.args[0])
        output.write(' IS DOCUMENT')


xml_expr_op_printer = XmlExprOpPrinter()


@node_printer(ast.XmlExpr)
def xml_expr(node, output):
    xml_expr_op_printer(node.op, node, output)


@node_printer(ast.XmlSerialize)
def xml_serialize(node, output):
    output.write('xmlserialize')
    with output.expression(True):
        xml_option_type_printer(node.xmloption, node, output)
        output.print_node(node.expr)
        output.write(' AS ')
        output.print_node(node.typeName)
        if node.indent:
            output.write('INDENT')
