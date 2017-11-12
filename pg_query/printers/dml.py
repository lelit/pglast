# -*- coding: utf-8 -*-
# :Project:   pg_query -- Printer functions for SQL DML nodes
# :Created:   sab 05 ago 2017 16:34:08 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

from .. import enums
from ..node import Missing
from ..printer import node_printer


@node_printer('A_ArrayExpr')
def a_array_expr(node, output):
    output.write('ARRAY[')
    output.print_list(node.elements)
    output.write(']')


@node_printer('A_Const')
def a_const(node, output):
    output.print(node.val)


@node_printer('A_Expr')
def a_expr(node, output):
    aek = enums.A_Expr_Kind

    if node.kind == aek.AEXPR_OP:
        op = output.concat_nodes(node.name)
        with output.expression():
            output.print(node.lexpr)
            output.write(' ' + op + ' ')
            output.print(node.rexpr)
    elif node.kind == aek.AEXPR_OP_ANY:
        output.print(node.lexpr)
        output.swrites(output.concat_nodes(node.name))
        output.write('ANY (')
        output.print(node.rexpr)
        output.write(')')
    elif node.kind == aek.AEXPR_OP_ALL:
        output.print(node.lexpr)
        output.swrites(output.concat_nodes(node.name))
        output.write('ALL (')
        output.print(node.rexpr)
        output.write(')')
    elif node.kind == aek.AEXPR_DISTINCT:
        output.print(node.lexpr)
        output.swrites('IS DISTINCT FROM')
        output.print(node.rexpr)
    elif node.kind == aek.AEXPR_NOT_DISTINCT:
        output.print(node.lexpr)
        output.swrites('IS NOT DISTINCT FROM')
        output.print(node.rexpr)
    elif node.kind == aek.AEXPR_NULLIF:
        output.write('NULLIF(')
        output.print_list((node.lexpr, node.rexpr))
        output.write(')')
    elif node.kind == aek.AEXPR_OF:
        output.print(node.lexpr)
        output.swrites('IS')
        if node.name[0].str.value == '<>':
            output.writes('NOT')
        output.write('OF (')
        output.print_list(node.rexpr)
        output.write(')')
    elif node.kind == aek.AEXPR_IN:
        output.print(node.lexpr)
        if node.name[0].str.value == '<>':
            output.swrites('NOT')
        output.swrite('IN (')
        output.print_list(node.rexpr)
        output.write(')')
    elif node.kind == aek.AEXPR_LIKE:
        output.print(node.lexpr)
        if node.name[0].str.value == '!~~':
            output.swrites('NOT')
        output.swrites('LIKE')
        output.print(node.rexpr)
    elif node.kind == aek.AEXPR_ILIKE:
        output.print(node.lexpr)
        if node.name[0].str.value == '!~~*':
            output.swrites('NOT')
        output.swrites('ILIKE')
        output.print(node.rexpr)
    elif node.kind == aek.AEXPR_SIMILAR:
        output.print(node.lexpr)
        if node.name[0].str.value == '!~':
            output.swrites('NOT')
        output.swrites('SIMILAR TO')
        assert (node.rexpr.node_tag == 'FuncCall'
                and node.rexpr.funcname[1].str == 'similar_escape')
        pattern = node.rexpr.args[0]
        escape = node.rexpr.args[1]
        output.print(pattern)
        if escape.val.node_tag != 'Null':
            output.swrites('ESCAPE')
            output.print(escape)
    elif node.kind == aek.AEXPR_BETWEEN:
        output.print(node.lexpr)
        output.swrites('BETWEEN')
        output.print_list(node.rexpr, 'AND', relative_indent=-4)
    elif node.kind == aek.AEXPR_NOT_BETWEEN:
        output.print(node.lexpr)
        output.swrites('NOT BETWEEN')
        output.print_list(node.rexpr, 'AND', relative_indent=-4)
    elif node.kind == aek.AEXPR_BETWEEN_SYM:
        output.print(node.lexpr)
        output.swrites('BETWEEN SYMMETRIC')
        output.print_list(node.rexpr, 'AND', relative_indent=-4)
    elif node.kind == aek.AEXPR_NOT_BETWEEN_SYM:
        output.print(node.lexpr)
        output.swrites('NOT BETWEEN SYMMETRIC')
        output.print_list(node.rexpr, 'AND', relative_indent=-4)
    elif node.kind == aek.AEXPR_PAREN:  # pragma: no cover
        # FIXME: accordingly with the documentation of the A_Expr_Kind typedef, AEXPR_PAREN is
        # a “nameless dummy node for parentheses”. What does that mean? I wasn't able to
        # “produce” it in any way...
        raise NotImplementedError("Expression of kind %s not implemented yet"
                                  % aek.AEXPR_PAREN)


@node_printer('A_Indices')
def a_indices(node, output):
    output.write('[')
    if node.is_slice:
        if node.lidx:
            output.print(node.lidx)
        output.write(':')
        if node.uidx:
            output.print(node.uidx)
    else:
        output.print(node.uidx)
    output.write(']')


@node_printer('A_Indirection')
def a_indirection(node, output):
    output.print(node.arg)
    output.print_list(node.indirection, '', standalone_items=False)


@node_printer('A_Star')
def a_star(node, output):
    output.write('*')


@node_printer('Alias')
def alias(node, output):
    output.print(node.aliasname, is_name=True)
    if node.colnames:
        output.swrite('(')
        output.print_list(node.colnames, sep=', ', are_names=True)
        output.write(')')


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
                relindent = -3 if not in_res_target and outer_exp_level == 0 else None
                output.print_list(node.args, 'OR', relative_indent=relindent)
        else:
            output.writes('NOT')
            output.print(node.args[0])


@node_printer('CaseExpr')
def case_expr(node, output):
    with output.push_indent():
        output.writes('CASE')
        if node.arg:
            output.print(node.arg)
        output.newline()
        output.write('  ')
        with output.push_indent():
            output.print_list(node.args, '')
            if node.defresult:
                output.newline()
                output.writes('ELSE')
                output.print(node.defresult)
        output.newline()
        output.write('END')


@node_printer('CaseWhen')
def case_when(node, output):
    output.writes('WHEN')
    with output.push_indent(-3):
        output.print(node.expr)
        output.newline()
        output.writes('THEN')
        output.print(node.result)


@node_printer('CoalesceExpr')
def coalesce_expr(node, output):
    output.write('COALESCE(')
    output.print_list(node.args)
    output.write(')')


@node_printer('CollateClause')
def collate_clause(node, output):
    if node.arg:
        output.print(node.arg)
    output.swrite('COLLATE ')
    output.print_list(node.collname, are_names=True)


@node_printer('ColumnRef')
def column_ref(node, output):
    output.print_list(node.fields, '.', standalone_items=False, are_names=True)


@node_printer('CommonTableExpr')
def common_table_expr(node, output):
    output.print(node.ctename, is_name=True)
    if node.aliascolnames:
        output.write('(')
        if len(node.aliascolnames) > 1:
            output.write('  ')
        output.print_list(node.aliascolnames, are_names=True)
        output.write(')')
        output.newline()

    output.swrite('AS (')
    output.print(node.ctequery)
    output.write(')')
    output.newline()


@node_printer('DeleteStmt')
def delete_stmt(node, output):
    with output.push_indent():
        if node.withClause:
            output.write('WITH ')
            output.print(node.withClause)
            output.newline()
            output.write('  ')
            output.indent()

        output.write('DELETE FROM ')
        output.print(node.relation)
        if node.usingClause:
            output.newline()
            output.write('USING ')
            output.print_list(node.usingClause)
        if node.whereClause:
            output.newline()
            output.write('WHERE ')
            output.print(node.whereClause)
        if node.returningList:
            output.newline()
            output.write('RETURNING ')
            output.print_list(node.returningList)

        if node.withClause:
            output.dedent()


@node_printer('Float')
def float(node, output):
    output.print(node.str)


@node_printer('FuncCall')
def func_call(node, output):
    output.print_list(node.funcname, '.', standalone_items=False, are_names=True)
    output.write('(')
    if node.agg_distinct:
        output.writes('DISTINCT')
    if node.args is Missing:
        if node.agg_star:
            output.write('*')
    else:
        output.print_list(node.args)
    if node.agg_order:
        if node.agg_within_group is Missing:
            output.swrites('ORDER BY')
            output.print_list(node.agg_order)
        else:
            output.writes(') WITHIN GROUP (ORDER BY')
            output.print_list(node.agg_order)
    output.write(')')
    if node.agg_filter:
        output.swrites('FILTER (WHERE')
        output.print(node.agg_filter)
        output.write(')')
    if node.over:
        output.swrite('OVER ')
        output.print(node.over)


@node_printer('IndexElem')
def index_elem(node, output):
    if node.name is not Missing:
        output.print(node.name, is_name=True)
    else:
        output.write('(')
        output.print(node.expr)
        output.write(')')
    if node.collation:
        output.swrite('COLLATE ')
        output.print_list(node.collation, are_names=True, standalone_items=False)
    if node.opclass:
        output.write(' ')
        output.print_list(node.opclass, are_names=True, standalone_items=False)
    if node.ordering != enums.SortByDir.SORTBY_DEFAULT:
        if node.ordering == enums.SortByDir.SORTBY_ASC:
            output.swrite('ASC')
        elif node.ordering == enums.SortByDir.SORTBY_DESC:
            output.swrite('DESC')
        elif node.ordering == enums.SortByDir.SORTBY_USING:
            raise NotImplementedError
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
        output.print(node.conname, is_name=True)
    if node.indexElems:
        output.swrite('(')
        output.print_list(node.indexElems)
        output.write(')')
    if node.whereClause:
        output.swrite('WHERE ')
        output.print(node.whereClause)


@node_printer('Integer')
def integer(node, output):
    output.print(node.ival)


@node_printer('InsertStmt')
def insert_stmt(node, output):
    with output.push_indent():
        if node.withClause:
            output.write('WITH ')
            output.print(node.withClause)
            output.newline()
            output.write('  ')
            output.indent()

        output.write('INSERT INTO ')
        output.print(node.relation)
        if node.cols:
            output.write(' (')
            output.print_list(node.cols, ', ', are_names=True)
            output.write(')')
        else:
            output.write(' ')
        if node.selectStmt:
            output.newline()
            output.print(node.selectStmt)
        else:
            output.write('DEFAULT VALUES')
        if node.onConflictClause:
            output.newline()
            output.write('ON CONFLICT ')
            output.print(node.onConflictClause)
        if node.returningList:
            output.newline()
            output.write('RETURNING ')
            output.print_list(node.returningList, ', ', are_names=True)

        if node.withClause:
            output.dedent()


@node_printer('JoinExpr')
def join_expr(node, output):
    if node.alias:
        output.write('(')

    output.print(node.larg)
    output.newline()

    with output.push_indent():
        if node.isNatural:
            output.write('NATURAL ')

        jt = enums.JoinType
        if node.jointype == jt.JOIN_INNER:
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
            output.print(node.rarg)
            output.newline()
        else:
            output.print(node.rarg)

        if node.usingClause:
            output.swrite('USING (')
            output.print_list(node.usingClause)
            output.write(')')
        elif node.quals:
            output.swrite('ON ')
            output.print(node.quals)

        if node.alias:
            output.writes(') AS')
            output.print(node.alias)

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
    output.print(node.source)


@node_printer('NullTest')
def null_test(node, output):
    output.print(node.arg)
    output.write(' IS')
    if node.nulltesttype == enums.NullTestType.IS_NOT_NULL:
        output.write(' NOT')
    output.write(' NULL')


@node_printer('ParamRef')
def param_ref(node, output):
    output.write('$%d' % node.number.value)


@node_printer('OnConflictClause')
def on_conflict_clause(node, output):
    oca = enums.OnConflictAction
    if node.infer:
        output.print(node.infer)
    if node.action == oca.ONCONFLICT_NOTHING:
        output.write('DO NOTHING')
    elif node.action == oca.ONCONFLICT_UPDATE:
        output.newline()
        with output.push_indent(3):
            output.write('DO UPDATE')
            output.newline()
            output.write('   SET ')
            output.print_list(node.targetList)
            if node.whereClause:
                output.newline()
                output.write('   WHERE ')
                output.print(node.whereClause)


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
        output.print(fun)
        if cdefs:
            # FIXME: find a way to get here
            output.write(' AS ')
            output.print_list(cdefs)
    if node.is_rowsfrom:
        output.write(')')
    if node.ordinality:
        output.write(' WITH ORDINALITY')
    if node.alias:
        output.write(' AS ')
        output.print(node.alias)


@node_printer('RangeSubselect')
def range_subselect(node, output):
    if node.lateral:
        output.write('LATERAL')
    output.maybe_write_space()
    output.write('(')
    with output.push_indent():
        output.print(node.subquery)
    output.write(')')
    if node.alias:
        output.write(' AS ')
        output.print(node.alias, is_name=True)


@node_printer('RangeVar')
def range_var(node, output):
    if not node.inh or not node.inh.value:
        output.write('ONLY ')
    if node.schemaname:
        output.print(node.schemaname, is_name=True)
        output.write('.')
    output.print(node.relname, is_name=True)
    alias = node.alias
    if alias:
        output.write(' AS ')
        output.print(alias, is_name=True)


@node_printer('RawStmt')
def raw_stmt(node, output):
    output.print(node.stmt)


@node_printer('ResTarget')
def res_target(node, output):
    if node.parent_node.node_tag in ('OnConflictClause', 'UpdateStmt'):
        if node.val.node_tag == 'MultiAssignRef':
            if node.val.colno == 1:
                output.write('(  ')
                output.indent(-2)
            output.print(node.name, is_name=True)
            if node.val.colno.value == node.val.ncolumns.value:
                output.dedent()
                output.write(') = ')
                output.print(node.val)
        else:
            if node.name:
                output.print(node.name, is_name=True)
                if node.indirection:
                    output.print_list(node.indirection, '', standalone_items=False)
                output.write(' = ')
            output.print(node.val)
    else:
        if node.val:
            output.print(node.val)
            if node.name:
                output.write(' AS ')
                output.print(node.name, is_name=True)
        else:
            output.print(node.name, is_name=True)
        if node.indirection:
            output.print_list(node.indirection, '', standalone_items=False)


@node_printer('RowExpr')
def row_expr(node, output):
    output.write('ROW(')
    output.print_list(node.args)
    output.write(')')


@node_printer('SelectStmt')
def select_stmt(node, output):
    with output.push_indent():
        if node.withClause:
            output.write('WITH ')
            output.print(node.withClause)
            output.newline()
            output.write('  ')
            output.indent()

        if node.valuesLists:
            # Is this a SELECT ... FROM (VALUES (...))?
            require_parens = node.parent_node.node_tag == 'RangeSubselect'
            if require_parens:
                output.write('(')
            output.write('VALUES ')
            output.print_lists(node.valuesLists)
            if require_parens:
                output.write(')')
        elif node.targetList is Missing:
            with output.push_indent():
                output.print(node.larg)
                output.newline()
                output.newline()
                so = enums.SetOperation
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
                output.print(node.rarg)
        else:
            output.write('SELECT')
            if node.distinctClause:
                output.write(' DISTINCT')
                if node.distinctClause[0]:
                    output.write(' ON (')
                    output.print_list(node.distinctClause)
                    output.write(')')
            output.write(' ')
            output.print_list(node.targetList)
            if node.fromClause:
                output.newline()
                output.write('FROM ')
                output.print_list(node.fromClause)
            if node.whereClause:
                output.newline()
                output.write('WHERE ')
                output.print(node.whereClause)
            if node.groupClause:
                output.newline()
                output.write('GROUP BY ')
                output.print_list(node.groupClause)
            if node.havingClause:
                output.newline()
                output.write('HAVING ')
                output.print(node.havingClause)
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
                output.write('LIMIT ')
                output.print(node.limitCount)
            if node.limitOffset:
                output.newline()
                output.write('OFFSET ')
                output.print(node.limitOffset)
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
    output.print(node.node)
    sbd = enums.SortByDir
    if node.sortby_dir == sbd.SORTBY_ASC:
        output.swrite('ASC')
    elif node.sortby_dir == sbd.SORTBY_DESC:
        output.swrite('DESC')
    elif node.sortby_dir == sbd.SORTBY_USING:
        output.swrites('USING')
        output.print_list(node.useOp)
    sbn = enums.SortByNulls
    if node.sortby_nulls != sbn.SORTBY_NULLS_DEFAULT:
        output.swrites('NULLS')
        output.write('FIRST' if node.sortby_nulls == sbn.SORTBY_NULLS_FIRST else 'LAST')


@node_printer('SQLValueFunction')
def sql_value_function(node, output):
    svfo = enums.SQLValueFunctionOp
    if node.op == svfo.SVFOP_CURRENT_DATE:
        output.write('CURRENT_DATE')
    elif node.op == svfo.SVFOP_CURRENT_TIME:
        output.write('CURRENT_TIME')
    elif node.op == svfo.SVFOP_CURRENT_TIME_N:  # pragma: no cover
        # FIXME: understand the meaning of this
        raise NotImplementedError('CURRENT_TIME_N')
    elif node.op == svfo.SVFOP_CURRENT_TIMESTAMP:
        output.write('CURRENT_TIMESTAMP')
    elif node.op == svfo.SVFOP_CURRENT_TIMESTAMP_N:  # pragma: no cover
        # FIXME: understand the meaning of this
        raise NotImplementedError('CURRENT_TIMESTAMP_N')
    elif node.op == svfo.SVFOP_LOCALTIME:
        output.write('LOCALTIME')
    elif node.op == svfo.SVFOP_LOCALTIME_N:  # pragma: no cover
        # FIXME: understand the meaning of this
        raise NotImplementedError('LOCALTIME_N')
    elif node.op == svfo.SVFOP_LOCALTIMESTAMP:
        output.write('LOCALTIMESTAMP')
    elif node.op == svfo.SVFOP_LOCALTIMESTAMP_N:  # pragma: no cover
        # FIXME: understand the meaning of this
        raise NotImplementedError('LOCALTIMESTAMP_N')
    elif node.op == svfo.SVFOP_CURRENT_ROLE:
        output.write('CURRENT_ROLE')
    elif node.op == svfo.SVFOP_CURRENT_USER:
        output.write('CURRENT_USER')
    elif node.op == svfo.SVFOP_USER:
        output.write('USER')
    elif node.op == svfo.SVFOP_SESSION_USER:
        output.write('SESSION_USER')
    elif node.op == svfo.SVFOP_CURRENT_CATALOG:
        output.write('CURRENT_CATALOG')
    elif node.op == svfo.SVFOP_CURRENT_SCHEMA:
        output.write('CURRENT_SCHEMA')


@node_printer('String')
def string(node, output, is_name=None):
    output.print(node.str, is_name=is_name)


@node_printer('SubLink')
def sub_link(node, output):
    slt = enums.SubLinkType

    if node.subLinkType == slt.EXISTS_SUBLINK:
        output.write('EXISTS ')
    elif node.subLinkType == slt.ALL_SUBLINK:
        output.print(node.testexpr)
        output.write(' ')
        output.print_list(node.operName, ' ', standalone_items=False)
        output.swrite('ALL ')
    elif node.subLinkType == slt.ANY_SUBLINK:
        output.print(node.testexpr)
        output.swrite('IN ')
    elif node.subLinkType == slt.ROWCOMPARE_SUBLINK:  # pragma: no cover
        # FIXME: figure out how the get here
        raise NotImplementedError("SubLink of type %s not supported yet"
                                  % slt.ROWCOMPARE_SUBLINK)
    elif node.subLinkType == slt.EXPR_SUBLINK:
        pass
    elif node.subLinkType == slt.MULTIEXPR_SUBLINK:  # pragma: no cover
        # FIXME: figure out how the get here
        raise NotImplementedError("SubLink of type %s not supported yet"
                                  % slt.MULTIEXPR_SUBLINK)
    elif node.subLinkType == slt.ARRAY_SUBLINK:
        output.write('ARRAY')

    output.write('(')
    with output.push_indent():
        output.print(node.subselect)
    output.write(')')


@node_printer('TypeCast')
def type_cast(node, output):
    output.print(node.arg)
    output.write('::')
    output.print(node.typeName)


# Constants taken from PG's include/utils/datetime.h: seem safe to assume they won't change

MONTH = 1 << 1
YEAR = 1 << 2
DAY = 1 << 3
HOUR = 1 << 10
MINUTE = 1 << 11
SECOND = 1 << 12

# Map interval's typmod to string representation
interval_ranges = {
    YEAR:                         "year",
    MONTH:                        "month",
    DAY:                          "day",
    HOUR:                         "hour",
    MINUTE:                       "minute",
    SECOND:                       "second",
    YEAR | MONTH:                 "year to month",
    DAY | HOUR:                   "day to hour",
    DAY | HOUR | MINUTE:          "day to minute",
    DAY | HOUR | MINUTE | SECOND: "day to second",
    HOUR | MINUTE:                "hour to minute",
    HOUR | MINUTE | SECOND:       "hour to second",
    MINUTE | SECOND:              "minute to second",
}
del MONTH, YEAR, DAY, HOUR, MINUTE, SECOND


# Map system type name to generic one
system_types = {
    'pg_catalog.bool':        'boolean',
    'pg_catalog.bpchar':      'char',
    'pg_catalog.float4':      'real',
    'pg_catalog.float8':      'double precision',
    'pg_catalog.int2':        'smallint',
    'pg_catalog.int4':        'integer',
    'pg_catalog.int8':        'bigint',
    'pg_catalog.interval':    'interval',
    'pg_catalog.numeric':     'numeric',
    'pg_catalog.time':        'time',
    'pg_catalog.timestamp':   'timestamp',
    'pg_catalog.timestamptz': 'timestamp with time zone',
    'pg_catalog.timetz':      'time with time zone',
    'pg_catalog.varchar':     'varchar',
}


@node_printer('TypeName')
def type_name(node, output):
    if node.setof:
        # FIXME: is this used only by plpgsql?
        output.writes('SETOF')
    name = '.'.join(n.str.value for n in node.names)
    if name in system_types:
        output.write(system_types[name])
    else:
        output.print_list(node.names, '.', standalone_items=False, are_names=True)
    if node.pct_type:
        # FIXME: is this used only by plpgsql?
        output.write('%TYPE')
    else:
        if node.typmods:
            if name == 'pg_catalog.interval':
                typmod = node.typmods[0].val.ival.value
                output.swrite(interval_ranges[typmod])
                if len(node.typmods) == 2:
                    output.write(' (')
                    output.print(node.typmods[1])
                    output.write(')')
            else:
                output.write('(')
                output.print_list(node.typmods, ',', standalone_items=False)
                output.write(')')
        if node.arrayBounds:
            for ab in node.arrayBounds:
                output.write('[')
                if ab.ival.value >= 0:
                    output.print(ab)
                output.write(']')


@node_printer('UpdateStmt')
def update_stmt(node, output):
    with output.push_indent():
        if node.withClause:
            output.write('WITH ')
            output.print(node.withClause)
            output.newline()
            output.write('  ')
            output.indent()

        output.write('UPDATE ')
        output.print(node.relation)
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
            output.print(node.whereClause)
        if node.returningList:
            output.newline()
            output.write('RETURNING ')
            output.print_list(node.returningList, ', ', are_names=True)

        if node.withClause:
            output.dedent()


@node_printer('WindowDef')
def window_def(node, output):
    empty = node.partitionClause is Missing and node.orderClause is Missing
    if node.name:
        output.print(node.name, is_name=True)
        if not empty:
            output.write(' AS ')
    if node.refname:
        output.write('(')
        output.print(node.refname, is_name=True)
        output.write(')')
        if not empty:
            # FIXME: find a way to get here
            output.write(' AS ')
    if not empty or (node.name is Missing and node.refname is Missing):
        output.write('(')
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
                if fo & enums.FRAMEOPTION_BETWEEN:
                    output.writes('BETWEEN')
                if fo & enums.FRAMEOPTION_START_UNBOUNDED_PRECEDING:
                    output.writes('UNBOUNDED PRECEDING')
                elif fo & enums.FRAMEOPTION_START_UNBOUNDED_FOLLOWING:  # pragma: no cover
                    # Disallowed
                    assert False
                    output.writes('UNBOUNDED FOLLOWING')
                elif fo & enums.FRAMEOPTION_START_CURRENT_ROW:
                    output.writes('CURRENT ROW')
                elif fo & enums.FRAMEOPTION_START_VALUE_PRECEDING:
                    output.print(node.startOffset)
                    output.swrites('PRECEDING')
                elif fo & enums.FRAMEOPTION_START_VALUE_FOLLOWING:
                    output.print(node.startOffset)
                    output.swrites('FOLLOWING')
                if fo & enums.FRAMEOPTION_BETWEEN:
                    output.writes('AND')
                if fo & enums.FRAMEOPTION_END_UNBOUNDED_PRECEDING:  # pragma: no cover
                    # Disallowed
                    assert False
                    output.writes('UNBOUNDED PRECEDING')
                elif fo & enums.FRAMEOPTION_END_UNBOUNDED_FOLLOWING:
                    output.writes('UNBOUNDED FOLLOWING')
                elif fo & enums.FRAMEOPTION_END_CURRENT_ROW:
                    output.writes('CURRENT ROW')
                elif fo & enums.FRAMEOPTION_END_VALUE_PRECEDING:
                    output.print(node.endOffset)
                    output.swrites('PRECEDING')
                elif fo & enums.FRAMEOPTION_END_VALUE_FOLLOWING:
                    output.print(node.endOffset)
                    output.swrites('FOLLOWING')
        output.write(')')


@node_printer('WithClause')
def with_clause(node, output):
    relindent = -3
    if node.recursive:
        relindent -= output.write('RECURSIVE ')
    output.print_list(node.ctes, relative_indent=relindent)
