# -*- coding: utf-8 -*-
# :Project:   pglast -- Printer functions for SQL DML nodes
# :Created:   sab 05 ago 2017 16:34:08 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2020, 2021, 2022 Lele Gaifax
#

from .. import enums
from ..node import Missing, List
from . import IntEnumPrinter, node_printer


@node_printer('A_ArrayExpr')
def a_array_expr(node, output):
    output.write('ARRAY[')
    if node.elements:
        output.print_list(node.elements)
    output.write(']')


@node_printer('A_Const')
def a_const(node, output):
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
        if node.lexpr.node_tag == 'BoolExpr':
            output.write('(')
        output.print_node(node.lexpr)
        if node.lexpr.node_tag == 'BoolExpr':
            output.write(') ')
        output.swrite('IS DISTINCT FROM ')
        output.print_node(node.rexpr)

    def AEXPR_ILIKE(self, node, output):
        output.print_node(node.lexpr)
        if node.name.string_value == '!~~*':
            output.swrites('NOT')
        output.swrite('ILIKE ')
        output.print_node(node.rexpr)

    def AEXPR_IN(self, node, output):
        output.print_node(node.lexpr)
        if node.name.string_value == '<>':
            output.swrites('NOT')
        output.swrite('IN (')
        output.print_list(node.rexpr)
        output.write(')')

    def AEXPR_LIKE(self, node, output):
        output.print_node(node.lexpr)
        if node.name.string_value == '!~~':
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
        output.write('NULLIF(')
        output.print_list((node.lexpr, node.rexpr))
        output.write(')')

    def AEXPR_OF(self, node, output):
        output.print_node(node.lexpr)
        output.swrites('IS')
        if node.name.string_value == '<>':
            output.writes('NOT')
        output.write('OF (')
        output.print_list(node.rexpr)
        output.write(')')

    def AEXPR_OP(self, node, output):
        with output.expression():
            # lexpr is optional because these are valid: -(1+1), +(1+1), ~(1+1)
            if node.lexpr is not Missing:
                if node.lexpr.node_tag == 'A_Expr':
                    if node.lexpr.kind == node.kind and node.lexpr.name == node.name:
                        output.print_node(node.lexpr)
                    else:
                        with output.expression():
                            output.print_node(node.lexpr)
                else:
                    output.print_node(node.lexpr)
                output.write(' ')
            if isinstance(node.name, List) and len(node.name) > 1:
                output.write('OPERATOR(')
                output.print_symbol(node.name)
                output.write(') ')
            else:
                output.print_symbol(node.name)
                output.write(' ')
            if node.rexpr is not Missing:
                if node.rexpr.node_tag == 'A_Expr':
                    if node.rexpr.kind == node.kind and node.rexpr.name == node.name:
                        output.print_node(node.rexpr)
                    else:
                        with output.expression():
                            output.print_node(node.rexpr)
                else:
                    output.print_node(node.rexpr)

    def AEXPR_OP_ALL(self, node, output):
        output.print_node(node.lexpr)
        output.write(' ')
        output.write(node.name.string_value)
        output.write(' ALL(')
        output.print_node(node.rexpr)
        output.write(')')

    def AEXPR_OP_ANY(self, node, output):
        output.print_node(node.lexpr)
        output.write(' ')
        output.write(node.name.string_value)
        output.write(' ANY(')
        output.print_node(node.rexpr)
        output.write(')')

    def AEXPR_PAREN(self, node, output):  # pragma: no cover
        # FIXME: accordingly with the documentation of the A_Expr_Kind typedef, AEXPR_PAREN is
        # a “nameless dummy node for parentheses”. What does that mean? I wasn't able to
        # “produce” it in any way...
        raise NotImplementedError("Expression of kind %s not implemented yet"
                                  % self.enum.AEXPR_PAREN)

    def AEXPR_SIMILAR(self, node, output):
        output.print_node(node.lexpr)
        if node.name.string_value == '!~':
            output.swrites('NOT')
        output.swrite('SIMILAR TO ')
        if ((node.rexpr.node_tag != 'FuncCall'
             or node.rexpr.funcname[1].val.value != 'similar_to_escape')):
            raise RuntimeError('Expected a FuncCall to "similar_to_escape", got %r',
                               node.rexpr)
        pattern = node.rexpr.args[0]
        output.print_node(pattern)
        if len(node.rexpr.args) > 1:
            output.swrite('ESCAPE ')
            output.print_node(node.rexpr.args[1])


a_expr_kind_printer = AExprKindPrinter()


@node_printer('A_Expr')
def a_expr(node, output):
    a_expr_kind_printer(node.kind, node, output)


@node_printer('A_Indices')
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


@node_printer('A_Indirection')
def a_indirection(node, output):
    bracket = ((node.arg.node_tag in ('A_ArrayExpr', 'A_Expr', 'A_Indirection', 'FuncCall',
                                      'RowExpr', 'TypeCast'))
               or
               (node.arg.node_tag == 'ColumnRef'
                and node.indirection[0].node_tag != 'A_Indices'))
    if bracket:
        output.write('(')
    output.print_node(node.arg)
    if bracket:
        output.write(')')
    output.print_list(node.indirection, '', standalone_items=False)


@node_printer('A_Indirection', 'A_Star')
def a_indirection_a_star(node, output):
    output.pending_separator = False
    output.write('.')
    a_star(node, output)


@node_printer('A_Indirection', 'ColumnRef')
def a_indirection_column_ref(node, output):
    output.write('(')
    column_ref(node, output)
    output.write(')')


@node_printer('A_Indirection', 'FuncCall')
def a_indirection_func_call(node, output):
    output.write('(')
    func_call(node, output)
    output.write(')')


@node_printer('A_Indirection', 'String')
def a_indirection_field(node, output):
    output.write('.')
    string(node, output, is_name=True)


@node_printer('A_Star')
def a_star(node, output):
    output.write('*')


@node_printer('Alias')
def alias(node, output):
    output.print_name(node.aliasname)
    if node.colnames:
        output.swrite('(')
        output.print_name(node.colnames, sep=',')
        output.write(')')


@node_printer('BitString')
def bitstring(node, output):
    output.write(f"{node.val.value[0]}'")
    output.write(node.val.value[1:])
    output.write("'")


@node_printer('BoolExpr')
def bool_expr(node, output):
    bet = enums.BoolExprType
    outer_exp_level = output.expression_level
    with output.expression():
        in_res_target = node.parent_node.node_tag == 'ResTarget'
        if node.boolop == bet.AND_EXPR:
            relindent = -4 if not in_res_target and outer_exp_level == 0 else None
            output.print_list(node.args, 'AND', relative_indent=relindent)
        elif node.boolop == bet.OR_EXPR:
            with output.expression():
                relindent = -4 if not in_res_target and outer_exp_level == 0 else None
                output.print_list(node.args, 'OR', relative_indent=relindent)
        else:
            output.writes('NOT')
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


@node_printer('BooleanTest')
def boolean_test(node, output):
    output.print_node(node.arg)
    output.write(' IS ')
    boolean_test_printer(node.booltesttype, node, output)


@node_printer('CallStmt')
def call_stmt(node, output):
    output.write('CALL ')
    output.print_node(node.funccall)


@node_printer('CaseExpr')
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


@node_printer('CaseWhen')
def case_when(node, output):
    output.write('WHEN ')
    with output.push_indent(-3):
        with output.expression():
            output.print_node(node.expr)
        output.newline()
        output.write('THEN ')
        output.print_node(node.result)


@node_printer('CoalesceExpr')
def coalesce_expr(node, output):
    output.write('COALESCE(')
    output.print_list(node.args)
    output.write(')')


@node_printer('CollateClause')
def collate_clause(node, output):
    if node.arg:
        with output.expression():
            output.print_node(node.arg)
    output.swrite('COLLATE ')
    output.print_name(node.collname, '.')


@node_printer('ColumnRef')
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


@node_printer('CommonTableExpr')
def common_table_expr(node, output):
    output.print_name(node.ctename)
    if node.aliascolnames:
        output.write('(')
        if len(node.aliascolnames) > 1:
            output.space(2)
        output.print_name(node.aliascolnames, ',')
        output.write(')')
        output.indent(-1, False)
        output.newline()

    output.swrite('AS')
    cte_materialize_printer(node.ctematerialized, node, output)
    output.write(' (')
    output.print_node(node.ctequery)
    output.write(')')
    if node.aliascolnames:
        output.dedent()
    output.newline()


@node_printer('ConstraintsSetStmt')
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


@node_printer('CopyStmt')
def copy_stmt(node, output):
    output.write('COPY ')
    if node.relation:
        output.print_node(node.relation)
        if node.attlist:
            output.write(' (')
            output.print_list(node.attlist, are_names=True)
            output.write(')')
    if node.query:
        output.write(' (')
        with output.push_indent():
            output.print_node(node.query)
        output.write(')')
    if node.is_from:
        output.write(' FROM ')
    else:
        output.write(' TO ')
    if node.is_program:
        output.write('PROGRAM ')
    if node.filename:
        output.print_node(node.filename)
    else:
        if node.is_from:
            output.write('STDIN')
        else:
            output.write('STDOUT')
    if node.options:
        output.newline()
        output.write('WITH (')
        output.print_list(node.options)
        output.write(')')
    if node.whereClause:
        output.newline()
        output.write('WHERE ')
        output.print_node(node.whereClause)


@node_printer('CopyStmt', 'DefElem')
def copy_stmt_def_elem(node, output):
    option = node.defname.value
    argv = node.arg
    if option == 'format':
        output.write('FORMAT ')
        output.print_symbol(argv)
    elif option == 'freeze':
        output.write('FREEZE')
        if argv:
            output.swrite(str(argv.val.value))
    elif option == 'delimiter':
        output.write('DELIMITER ')
        output.print_node(argv)
    elif option == 'null':
        output.write('NULL ')
        output.print_node(argv)
    elif option == 'header':
        output.write('HEADER')
        if argv:
            output.swrite(str(argv.val.value))
    elif option == 'quote':
        output.write('QUOTE ')
        output.print_node(argv)
    elif option == 'escape':
        output.write('ESCAPE ')
        output.print_node(argv)
    elif option == 'force_quote':
        output.write('FORCE_QUOTE ')
        # If it is a list print it.
        if isinstance(argv, List):
            output.write('(')
            output.print_list(argv, are_names=True)
            output.write(')')
        else:
            output.write('* ')
    elif option == 'force_null':
        output.write('FORCE_NULL (')
        output.print_list(argv, are_names=True)
        output.write(')')
    elif option == 'force_not_null':
        output.write('FORCE_NOT_NULL (')
        output.print_list(argv, are_names=True)
        output.write(')')
    elif option == 'encoding':
        output.write('ENCODING ')
        output.print_node(argv)
    else:
        raise NotImplementedError(option)


@node_printer('DeclareCursorStmt')
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


@node_printer('DeleteStmt')
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


@node_printer('ExecuteStmt')
def execute_stmt(node, output):
    output.write('EXECUTE ')
    output.print_node(node.name, is_name=True)
    if node.params:
        output.write('(')
        output.print_list(node.params)
        output.write(')')


@node_printer('ExplainStmt')
def explain_stmt(node, output):
    output.write('EXPLAIN ')
    if node.options:
        output.write('(')
        output.print_list(node.options)
        output.write(')')
        output.newline()
        output.space(2)
    output.print_node(node.query)


@node_printer('ExplainStmt', 'DefElem')
def explain_stmt_def_elem(node, output):
    output.print_symbol(node.defname)
    if node.arg is not Missing:
        output.write(' ')
        output.print_symbol(node.arg)


class FetchDirectionPrinter(IntEnumPrinter):
    enum = enums.FetchDirection

    def FETCH_FORWARD(self, node, output):
        if node.howMany == enums.FETCH_ALL:
            output.write('ALL ')
        elif node.howMany != 1:
            output.write(f'FORWARD {node.howMany.value} ')

    def FETCH_BACKWARD(self, node, output):
        if node.howMany == enums.FETCH_ALL:
            output.write('BACKWARD ALL ')
        elif node.howMany != 1:
            output.write(f'BACKWARD {node.howMany.value} ')
        else:
            output.write('PRIOR ')

    def FETCH_ABSOLUTE(self, node, output):
        if node.howMany == 1:
            output.write('FIRST ')
        elif node.howMany == -1:
            output.write('LAST ')
        else:
            output.write(f'ABSOLUTE {node.howMany.value} ')

    def FETCH_RELATIVE(self, node, output):
        output.write(f'RELATIVE {node.howMany.value} ')


fetch_direction_printer = FetchDirectionPrinter()


@node_printer('FetchStmt')
def fetch_stmt(node, output):
    output.write('MOVE ' if node.ismove else 'FETCH ')
    fetch_direction_printer(node.direction, node, output)
    output.print_name(node.portalname)


@node_printer('Float')
def float(node, output):
    output.print_node(node.val)


@node_printer('FuncCall')
def func_call(node, output):
    name = '.'.join(n.val.value for n in node.funcname)
    special_printer = output.get_printer_for_function(name)
    if special_printer is not None:
        special_printer(node, output)
        return

    output.print_name(node.funcname)
    output.write('(')
    if node.agg_distinct:
        output.writes('DISTINCT')
    if node.args is Missing:
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
    output.write(')')
    if node.agg_filter:
        output.swrites('FILTER (WHERE')
        output.print_node(node.agg_filter)
        output.write(')')
    if node.over:
        output.swrite('OVER ')
        output.print_node(node.over)


@node_printer('FuncCall', 'WindowDef')
def func_call_window_def(node, output):
    if node.name:
        output.print_name(node.name)
    else:
        window_def(node, output)


@node_printer('GroupingSet')
def grouping_set(node, output):
    kind = node.kind
    if kind == enums.GroupingSetKind.GROUPING_SET_CUBE:
        output.write('CUBE (')
    elif kind == enums.GroupingSetKind.GROUPING_SET_ROLLUP:
        output.write('ROLLUP (')
    elif kind == enums.GroupingSetKind.GROUPING_SET_SETS:
        output.write('GROUPING SETS (')
    elif kind == enums.GroupingSetKind.GROUPING_SET_EMPTY:
        output.write('()')
        return
    elif kind == enums.GroupingSetKind.GROUPING_SET_SIMPLE:
        # No idea how to reach this branch
        output.write('SIMPLE (')
    else:  # pragma: no cover
        raise NotImplementedError('Unhandled grouping set kind: %s' % kind)
    output.print_list(node.content, ',')
    output.write(')')


@node_printer('GroupingFunc')
def grouping_func(node, output):
    output.write(' GROUPING(')
    output.print_list(node.args)
    output.write(')')


@node_printer('IndexElem')
def index_elem(node, output):
    if node.name is not Missing:
        output.print_name(node.name)
    else:
        output.write('(')
        output.print_node(node.expr)
        output.write(')')
    if node.collation:
        output.swrite('COLLATE ')
        output.print_name(node.collation, ',')
    if node.opclass:
        output.write(' ')
        output.print_name(node.opclass, '.')
        if node.opclassopts:
            output.write(' (')
            output.print_list(node.opclassopts)
            output.write(')')
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


@node_printer('InferClause')
def infer_clause(node, output):
    if node.conname:
        output.swrite('ON CONSTRAINT ')
        output.print_name(node.conname)
    if node.indexElems:
        output.swrite('(')
        output.print_list(node.indexElems)
        output.write(')')
    if node.whereClause:
        output.swrite('WHERE ')
        output.print_node(node.whereClause)


@node_printer('Integer')
def integer(node, output):
    output.print_node(node.val)


@node_printer('InsertStmt')
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
            output.write(' (')
            output.print_list(node.cols)
            output.write(')')
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


@node_printer('IntoClause')
def into_clause(node, output):
    output.print_node(node.rel)
    if node.colNames:
        output.write(' (')
        output.print_name(node.colNames, ',')
        output.write(')')
    output.newline()
    with output.push_indent(2):
        if node.accessMethod:
            output.write('USING ')
            output.print_name(node.accessMethod)
            output.newline()
        if node.options:
            output.write('WITH (')
            output.print_list(node.options)
            output.write(')')
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


@node_printer('JoinExpr')
def join_expr(node, output):
    if node.alias:
        output.write('(')

    with output.push_indent():
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

        output.swrites('JOIN')

        if node.rarg.node_tag == 'JoinExpr':
            output.indent(3, relative=False)
            # need this for:
            # tests/test_printers_roundtrip.py::test_pg_regress_corpus[join.sql] -
            # AssertionError: Statement “select * from   int8_tbl x cross join (int4_tbl x cross join lateral (select x.f1) ss)”
            # from libpg_query/test/sql/postgres_regress/join.sql at line 1998
            if not node.rarg.alias:
                output.write(' (')
            output.print_node(node.rarg)
            if not node.rarg.alias:
                output.write(')')
            output.newline()
        else:
            output.print_node(node.rarg)

        if node.usingClause:
            output.swrite('USING (')
            output.print_name(node.usingClause, ',')
            output.write(')')
        elif node.quals:
            output.swrite('ON ')
            output.print_node(node.quals)

        if node.alias:
            output.writes(') AS')
            output.print_name(node.alias)

        if node.rarg.node_tag == 'JoinExpr':
            output.dedent()


@node_printer('LockingClause')
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


@node_printer('ListenStmt')
def listen_stmt(node, output):
    output.write('LISTEN ')
    output.print_name(node.conditionname)


@node_printer('MinMaxExpr')
def min_max_expr(node, output):
    if node.op == enums.MinMaxOp.IS_GREATEST:
        output.write('GREATEST(')
    else:
        output.write('LEAST(')
    output.print_list(node.args)
    output.write(')')


@node_printer('MultiAssignRef')
def multi_assign_ref(node, output):
    output.print_node(node.source)


@node_printer('NamedArgExpr')
def named_arg_expr(node, output):
    output.print_name(node.name)
    output.write(' => ')
    output.print_node(node.arg)


@node_printer('Null')
def null(node, output):
    output.write('NULL')


@node_printer('NullTest')
def null_test(node, output):
    with output.expression():
        output.print_node(node.arg)
        output.write(' IS')
        if node.nulltesttype == enums.NullTestType.IS_NOT_NULL:
            output.write(' NOT')
        output.write(' NULL')


@node_printer('ParamRef')
def param_ref(node, output):
    if node.number is Missing:  # pragma: no cover
        # NB: standard PG does not allow "?"-style param placeholders, this is a minor
        # deviation introduced by libpg_query; in version 2 apparently the case is merged
        # back to the standard style below
        output.write('?')
    else:
        output.write('$%d' % node.number.value)


@node_printer('PrepareStmt')
def prepare_stmt(node, output):
    output.write('PREPARE ')
    output.print_node(node.name, is_name=True)
    if node.argtypes:
        output.write('(')
        output.print_list(node.argtypes)
        output.write(')')
    output.write(' AS')
    output.newline()
    with output.push_indent(2):
        output.print_node(node.query)


@node_printer('OnConflictClause')
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


def print_transaction_mode_list(node, output):
    first = True
    for elem in node:
        if first:
            first = False
        else:
            output.write(', ')
        if elem.defname == 'transaction_isolation':
            output.write('ISOLATION LEVEL ')
            if elem.arg.val.val == 'read uncommitted':
                output.write('READ UNCOMMITTED')
            elif elem.arg.val.val == 'read committed':
                output.write('READ COMMITTED')
            elif elem.arg.val.val == 'repeatable read':
                output.write('REPEATABLE READ')
            elif elem.arg.val.val == 'serializable':
                output.write('SERIALIZABLE')
        elif elem.defname == 'transaction_read_only':
            if elem.arg.val.val == 1:
                output.write('READ ONLY')
            elif elem.arg.val.val == 0:
                output.write('READ WRITE')
        elif elem.defname == 'transaction_deferrable':
            if elem.arg.val.val == 1:
                output.write('DEFERRABLE')
            elif elem.arg.val.val == 0:
                output.write('NOT DEFERRABLE')


@node_printer('RangeFunction')
def range_function(node, output):
    if node.lateral:
        output.write('LATERAL ')
    if node.is_rowsfrom:
        output.write('ROWS FROM (')
    first = True
    for fun, cdefs in node.functions:
        if first:
            first = False
        else:
            output.write(', ')
        output.print_node(fun)
        if cdefs:
            # FIXME: find a way to get here
            output.write(' AS (')
            output.print_list(cdefs)
            output.write(')')
    if node.is_rowsfrom:
        output.write(')')
    if node.ordinality:
        output.write(' WITH ORDINALITY')
    if node.alias:
        output.write(' AS ')
        output.print_node(node.alias)
    if node.coldeflist:
        if not node.alias:
            output.write(' AS ')
        output.write('(')
        output.print_list(node.coldeflist, ',')
        output.write(')')


@node_printer('RangeSubselect')
def range_subselect(node, output):
    if node.lateral:
        output.write('LATERAL')
    output.maybe_write_space()
    output.write('(')
    with output.push_indent():
        output.print_node(node.subquery)
    output.write(')')
    if node.alias:
        output.write(' AS ')
        output.print_name(node.alias)


@node_printer('RangeTableFunc')
def range_table_func(node, output):
    if node.lateral:
        output.write('LATERAL ')
    output.write('xmltable(')
    with output.push_indent():
        if node.namespaces:
            output.write('xmlnamespaces(')
            output.print_list(node.namespaces)
            output.writes('),')
            output.newline()
        with output.expression():
            output.print_node(node.rowexpr)
        output.newline()
        output.write('PASSING ')
        output.print_node(node.docexpr)
        output.newline()
        output.write('COLUMNS ')
        output.print_list(node.columns)
        output.write(')')
    if node.alias:
        # FIXME: find a way to get here
        output.write(' AS ')
        output.print_node(node.alias)


@node_printer('RangeTableFunc', 'ResTarget')
def range_table_func_res_target(node, output):
    if not node.name:
        output.write('DEFAULT ')
    output.print_node(node.val)
    if node.name:
        output.write(' AS ')
        output.print_name(node.name)


@node_printer('RangeTableFuncCol')
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


@node_printer('RangeVar')
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


@node_printer('RangeTableSample')
def range_table_sample(node, output):
    output.print_node(node.relation)
    output.write(' TABLESAMPLE ')
    output.print_name(node.method, ' ')
    output.write('(')
    output.print_list(node.args, ' ')
    output.write(') ')
    if node.repeatable:
        output.write('REPEATABLE (')
        output.print_node(node.repeatable)
        output.write(')')


@node_printer('RawStmt')
def raw_stmt(node, output):
    output.print_node(node.stmt)


@node_printer('ResTarget')
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


@node_printer('RowExpr')
def row_expr(node, output):
    if node.row_format == enums.CoercionForm.COERCE_EXPLICIT_CALL:
        output.write('ROW(')
        if node.args:
            output.print_list(node.args)
        output.write(')')
    elif node.row_format == enums.CoercionForm.COERCE_IMPLICIT_CAST:
        output.write('(')
        output.print_list(node.args)
        output.write(')')
    else:
        raise NotImplementedError('Coercion type not implemented: %s' %
                                  node.row_format)


def _select_needs_to_be_wrapped_in_parens(node):
    # Accordingly with https://www.postgresql.org/docs/current/sql-select.html, a SELECT
    # statement on either sides of UNION/INTERSECT/EXCEPT must be wrapped in parens if it
    # contains ORDER BY/LIMIT/... or is a nested UNION/INTERSECT/EXCEPT
    return (node.sortClause
            or node.limitCount
            or node.limitOffset
            or node.lockingClause
            or node.withClause
            or node.op != enums.SetOperation.SETOP_NONE)


@node_printer('SelectStmt')
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
            require_parens = node.parent_node.node_tag == 'RangeSubselect'
            if require_parens:
                output.write('(')
            output.write('VALUES ')
            output.print_lists(node.valuesLists)
            if require_parens:
                output.write(')')
        elif node.op != so.SETOP_NONE and (node.larg or node.rarg):
            with output.push_indent():
                if node.larg:
                    if _select_needs_to_be_wrapped_in_parens(node.larg):
                        output.write('(')
                        output.print_node(node.larg)
                        output.write(')')
                    else:
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
                    if _select_needs_to_be_wrapped_in_parens(node.rarg):
                        output.write('(')
                        output.print_node(node.rarg)
                        output.write(')')
                    else:
                        output.print_node(node.rarg)
        else:
            output.write('SELECT')
            if node.distinctClause:
                output.write(' DISTINCT')
                if node.distinctClause[0]:
                    output.write(' ON (')
                    output.print_list(node.distinctClause)
                    output.write(')')
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
            # FIXME do we need add '()' for all ?
            if ((node.limitCount
                 and node.limitCount.node_tag == "A_Expr"
                 and node.limitCount.kind == enums.A_Expr_Kind.AEXPR_OP)):
                output.write('(')
            output.print_node(node.limitCount)
            if ((node.limitCount
                 and node.limitCount.node_tag == "A_Expr"
                 and node.limitCount.kind == enums.A_Expr_Kind.AEXPR_OP)):
                output.write(')')
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


@node_printer('SetToDefault')
def set_to_default(node, output):
    output.write('DEFAULT')


@node_printer('SortBy')
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
        output.write('CURRENT_TIMESTAMP(')
        output.write(str(node.typmod.value))
        output.write(')')

    def SVFOP_CURRENT_TIME_N(self, node, output):  # pragma: no cover
        output.write('CURRENT_TIME(')
        output.write(str(node.typmod.value))
        output.write(')')

    def SVFOP_CURRENT_USER(self, node, output):
        output.write('CURRENT_USER')

    def SVFOP_LOCALTIME(self, node, output):
        output.write('LOCALTIME')

    def SVFOP_LOCALTIMESTAMP(self, node, output):
        output.write('LOCALTIMESTAMP')

    def SVFOP_LOCALTIMESTAMP_N(self, node, output):  # pragma: no cover
        output.write('LOCALTIMESTAMP(')
        output.write(str(node.typmod.value))
        output.write(')')

    def SVFOP_LOCALTIME_N(self, node, output):  # pragma: no cover
        output.write('LOCALTIME(')
        output.write(str(node.typmod.value))
        output.write(')')

    def SVFOP_SESSION_USER(self, node, output):
        output.write('SESSION_USER')

    def SVFOP_USER(self, node, output):
        output.write('USER')


sql_value_function_op_printer = SQLValueFunctionOpPrinter()


@node_printer('SQLValueFunction')
def sql_value_function(node, output):
    sql_value_function_op_printer(node.op, node, output)


@node_printer('String')
def string(node, output, is_name=False, is_symbol=False):
    output.print_node(node.val, is_name=is_name, is_symbol=is_symbol)


@node_printer('SubLink')
def sub_link(node, output):
    slt = enums.SubLinkType

    if node.subLinkType == slt.EXISTS_SUBLINK:
        output.write('EXISTS ')
    elif node.subLinkType == slt.ALL_SUBLINK:
        output.print_node(node.testexpr)
        output.write(' ')
        output.write(node.operName.string_value)
        output.write(' ALL ')
    elif node.subLinkType == slt.ANY_SUBLINK:
        output.print_node(node.testexpr)
        if node.operName:
            output.write(' ')
            output.write(node.operName.string_value)
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

    output.write('(')
    with output.push_indent():
        output.print_node(node.subselect)
    output.write(')')


@node_printer('TransactionStmt')
def transaction_stmt(node, output):
    tsk = enums.TransactionStmtKind
    if node.kind.value == tsk.TRANS_STMT_BEGIN:
        output.write('BEGIN ')
        if node.options:
            output.print_list(node.options)
    elif node.kind.value == tsk.TRANS_STMT_START:
        output.write('START TRANSACTION ')
        if node.options:
            output.print_list(node.options)
    elif node.kind.value == tsk.TRANS_STMT_COMMIT:
        output.write('COMMIT ')
        if node.chain:
            output.write('AND CHAIN ')
    elif node.kind.value == tsk.TRANS_STMT_ROLLBACK:
        output.write('ROLLBACK ')
        if node.chain:
            output.write('AND CHAIN ')
    elif node.kind.value == tsk.TRANS_STMT_SAVEPOINT:
        output.write('SAVEPOINT ')
        output.write(node.savepoint_name.value)
    elif node.kind.value == tsk.TRANS_STMT_RELEASE:
        output.write('RELEASE ')
        output.write(node.savepoint_name.value)
    elif node.kind.value == tsk.TRANS_STMT_ROLLBACK_TO:
        output.write('ROLLBACK TO SAVEPOINT ')
        output.write(node.savepoint_name.value)
    elif node.kind.value == tsk.TRANS_STMT_PREPARE:
        output.write('PREPARE TRANSACTION ')
        output.write("'%s'" % node.gid.value)
    elif node.kind.value == tsk.TRANS_STMT_COMMIT_PREPARED:
        output.write('COMMIT PREPARED ')
        output.write("'%s'" % node.gid.value)
    elif node.kind.value == tsk.TRANS_STMT_ROLLBACK_PREPARED:
        output.write('ROLLBACK PREPARED ')
        output.write("'%s'" % node.gid.value)


@node_printer('TransactionStmt', 'DefElem')
def transaction_stmt_def_elem(node, output):
    value = node.defname.value
    argv = node.arg.val
    if value == 'transaction_isolation':
        output.write('ISOLATION LEVEL ')
        output.write(argv.val.value.upper())
    elif value == 'transaction_read_only':
        output.write('READ ')
        if argv.val.value == 0:
            output.write('WRITE')
        else:
            output.write('ONLY')
    elif value == 'transaction_deferrable':
        if argv.val.value == 0:
            output.write('NOT ')
        output.write('DEFERRABLE')
    else:  # pragma: no cover
        raise NotImplementedError('Unhandled defname value %r' % value)


@node_printer('TruncateStmt')
def truncate_stmt(node, output):
    output.write('TRUNCATE TABLE ')
    output.print_list(node.relations)
    if node.restart_seqs:
        output.write(' RESTART IDENTITY')
    if node.behavior == enums.DropBehavior.DROP_CASCADE:
        output.write(' CASCADE')


@node_printer('TypeCast')
def type_cast(node, output):
    if node.arg.node_tag == 'A_Const':
        # Special case for boolean constants
        if ((node.arg.val.node_tag != 'Null'
             and node.arg.val.val.value in ('t', 'f')
             and '.'.join(n.val.value for n in node.typeName.names) == 'pg_catalog.bool')):
            output.write('TRUE' if node.arg.val.val == 't' else 'FALSE')
            return
        # Special case for bpchar
        elif (('.'.join(n.val.value for n in node.typeName.names) == 'pg_catalog.bpchar'
               and not node.typeName.typmods)):
            output.write('char ')
            output.print_node(node.arg)
            return
    # FIXME: all other case using CAST
    output.write('CAST(')
    with output.expression():
        output.print_node(node.arg)
    output.write(' AS ')
    output.print_node(node.typeName)
    output.write(')')


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


@node_printer('TypeName')
def type_name(node, output):
    if node.setof:
        # FIXME: is this used only by plpgsql?
        output.writes('SETOF')
    name = '.'.join(n.val.value for n in node.names)
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
        # FIXME: is this used only by plpgsql?
        output.write('%TYPE')
    else:
        if node.typmods:
            if name == 'pg_catalog.interval':
                typmod = node.typmods[0].val.val.value
                if typmod in interval_ranges:
                    output.swrite(interval_ranges[typmod])
                if len(node.typmods) == 2:
                    output.write(' (')
                    output.print_node(node.typmods[1])
                    output.write(')')
            else:
                output.write('(')
                output.print_list(node.typmods, ',', standalone_items=False)
                output.write(')')
        output.write(suffix)
        if node.arrayBounds:
            for ab in node.arrayBounds:
                output.write('[')
                if ab.val.value >= 0:
                    output.print_node(ab)
                output.write(']')


@node_printer('UpdateStmt')
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


@node_printer('UnlistenStmt')
def unlisten_stmt(node, output):
    output.write('UNLISTEN ')
    if node.conditionname:
        output.print_name(node.conditionname)
    else:
        output.write('*')


@node_printer('VariableSetStmt')
def variable_set_stmt(node, output):
    vsk = enums.VariableSetKind
    if node.kind == vsk.VAR_RESET:
        output.write('RESET ')
        output.print_name(node.name)
    elif node.kind == vsk.VAR_RESET_ALL:
        output.write('RESET ALL')
    else:
        output.write('SET ')
        if node.is_local:
            output.write('LOCAL ')
        if node.name == 'timezone':
            output.write('TIME ZONE ')
        elif node.name == 'TRANSACTION':
            output.write('TRANSACTION ')
            print_transaction_mode_list(node.args, output)
        elif node.name == 'SESSION CHARACTERISTICS':
            output.write('SESSION CHARACTERISTICS AS TRANSACTION ')
            print_transaction_mode_list(node.args, output)
        elif node.name == 'TRANSACTION SNAPSHOT':
            output.write('TRANSACTION SNAPSHOT ')
            output.print_list(node.args, ',')
        else:
            output.print_name(node.name)
            output.write(' TO ')
        if node.kind == vsk.VAR_SET_VALUE:
            output.print_list(node.args)
        elif node.kind == vsk.VAR_SET_DEFAULT:
            output.write('DEFAULT')
        elif node.kind == vsk.VAR_SET_MULTI:
            pass
        else:
            raise NotImplementedError("SET statement of kind %s not implemented yet"
                                      % node.kind)


@node_printer('WithClause')
def with_clause(node, output):
    relindent = -2
    if node.recursive:
        relindent -= output.write('RECURSIVE ')
    output.print_list(node.ctes, relative_indent=relindent)


@node_printer('WindowDef')
def window_def(node, output):
    if node.name:
        output.print_name(node.name)
        output.write(' AS ')
    output.write('(')
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
    output.write(')')


def print_indirection(node, output):
    for idx, subnode in enumerate(node):
        if subnode.node_tag == 'String':
            output.write('.')
        output.print_node(subnode, is_name=True)


@node_printer(('OnConflictClause', 'UpdateStmt'), 'ResTarget')
def update_stmt_res_target(node, output):
    if node.val.node_tag == 'MultiAssignRef':
        if node.val.colno == 1:
            output.write('( ')
            output.indent(-2)
        output.print_name(node.name)
        if node.indirection:
            print_indirection(node.indirection, output)
        if node.val.colno.value == node.val.ncolumns.value:
            output.dedent()
            output.write(') = ')
            output.print_node(node.val)
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
        output.write('xmlconcat(')
        output.print_list(node.args)
        output.write(')')

    def IS_XMLELEMENT(self, node, output):  # XMLELEMENT(name, xml_attributes, args)
        output.write('xmlelement(name ')
        output.print_name(node.name)
        if node.named_args:
            output.write(', xmlattributes(')
            output.print_list(node.named_args)
            output.write(')')
        if node.args:
            output.write(', ')
            output.print_list(node.args)
        output.write(')')

    def IS_XMLFOREST(self, node, output):  # XMLFOREST(xml_attributes)
        output.write('xmlforest(')
        output.print_list(node.named_args)
        output.write(')')

    def IS_XMLPARSE(self, node, output):  # XMLPARSE(text, is_doc, preserve_ws)
        output.write('xmlparse(')
        xml_option_type_printer(node.xmloption, node, output)
        arg, preserve_ws = node.args
        output.print_node(arg)
        if preserve_ws.arg.val.val.value == 't':
            output.write(' PRESERVE WHITESPACE')
        output.write(')')

    def IS_XMLPI(self, node, output):  # XMLPI(name [, args])
        output.write('xmlpi(name ')
        output.print_name(node.name)
        if node.args:
            output.write(', ')
            output.print_list(node.args)
        output.write(')')

    def IS_XMLROOT(self, node, output):  # XMLROOT(xml, version, standalone)
        output.write('xmlroot(')
        xml, version, standalone = node.args
        output.print_node(xml)
        output.write(', version ')
        if version.val.node_tag == 'Null':
            output.write('NO VALUE')
        else:
            output.print_node(version)
        xml_standalone_type_printer(standalone.val.val, node, output)
        output.write(')')

    def IS_XMLSERIALIZE(self, node, output):  # XMLSERIALIZE(is_document, xmlval)
        raise NotImplementedError('IS_XMLSERIALIZE??')

    def IS_DOCUMENT(self, node, output):  # xmlval IS DOCUMENT
        output.print_node(node.args[0])
        output.write(' IS DOCUMENT')


xml_expr_op_printer = XmlExprOpPrinter()


@node_printer('XmlExpr')
def xml_expr(node, output):
    xml_expr_op_printer(node.op, node, output)


@node_printer('XmlSerialize')
def xml_serialize(node, output):
    output.write('xmlserialize(')
    xml_option_type_printer(node.xmloption, node, output)
    output.print_node(node.expr)
    output.write(' AS ')
    output.print_node(node.typeName)
    output.write(')')
