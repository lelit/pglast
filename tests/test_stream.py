# -*- coding: utf-8 -*-
# :Project:   pglast — Tests on the stream.py module
# :Created:   sab 05 ago 2017 10:31:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2022, 2024, 2026 Lele Gaifax
#

import pytest

from pglast import ast, parse_sql, visitors
from pglast.precedence import ExprContext, ExprPrec, Side
from pglast.printers import NODE_PRINTERS, PrinterAlreadyPresentError, SPECIAL_FUNCTIONS
from pglast.printers import node_printer, special_function
from pglast.stream import IndentedStream, OutputStream, RawStream


def test_output_stream():
    output = OutputStream()
    output.writes('SELECT *')
    output.writes(' FROM')
    output.writes('table ')
    output.writes('WHERE')
    output.write('id = 1')

    assert output.getvalue() == 'SELECT * FROM table WHERE id = 1'


def test_raw_stream_with_sql():
    raw_stmt_printer = NODE_PRINTERS.pop(ast.RawStmt, None)
    try:
        @node_printer(ast.RawStmt)
        def raw_stmt(node, output):
            output.write('Yeah')

        output = RawStream()
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah; Yeah'
    finally:
        if raw_stmt_printer is not None:
            NODE_PRINTERS[ast.RawStmt] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop(ast.RawStmt, None)


def test_raw_stream_with_empty_sql():
    output = RawStream()
    result = output('')
    assert result == ''
    result = output(' ')
    assert result == ''
    result = output(())
    assert result == ''


def test_raw_stream():
    raw_stmt_printer = NODE_PRINTERS.pop(ast.RawStmt, None)
    try:
        @node_printer(ast.RawStmt)
        def raw_stmt(node, output):
            output.write('Yeah')

        root = parse_sql('SELECT 1')
        output = RawStream()
        result = output(root)
        assert result == 'Yeah'
    finally:
        if raw_stmt_printer is not None:
            NODE_PRINTERS[ast.RawStmt] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop(ast.RawStmt, None)


def test_raw_stream_invalid_call():
    with pytest.raises(ValueError):
        RawStream()(1)
    with pytest.raises(ValueError):
        RawStream()((1,))


def test_indented_stream_with_sql():
    raw_stmt_printer = NODE_PRINTERS.pop(ast.RawStmt, None)
    try:
        @node_printer(ast.RawStmt)
        def raw_stmt(node, output):
            output.write('Yeah')

        output = IndentedStream()
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah;\n\nYeah'

        output = IndentedStream(separate_statements=False)
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah;\nYeah'
    finally:
        if raw_stmt_printer is not None:
            NODE_PRINTERS[ast.RawStmt] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop(ast.RawStmt, None)


@pytest.mark.parametrize('sql,threshold,expected', (
    ("SELECT 'abc\\'", 4, "SELECT 'abc\\'"),
    ("SELECT 'abc\\'", 3, "SELECT 'abc'\n       '\\'"),
    (r"SELECT 'abc\\'", 3, "SELECT 'abc'\n       '\\\\'"),
    ("SELECT 'abc\n\\'", 3, "SELECT E'abc'\n        '\\n\\\\'"),
))
def test_split_string_literals_ending_in_backslash(sql, threshold, expected):
    result = IndentedStream(split_string_literals_threshold=threshold)(parse_sql(sql))

    assert result == expected


def test_separate_statements():
    """Separate statements by ``separate_statements`` (int) newlines."""
    raw_stmt_printer = NODE_PRINTERS.pop(ast.RawStmt, None)
    try:
        @node_printer(ast.RawStmt)
        def raw_stmt(node, output):
            output.write('Yeah')

        output = IndentedStream(separate_statements=2)
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah;\n\n\nYeah'
    finally:
        if raw_stmt_printer is not None:
            NODE_PRINTERS[ast.RawStmt] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop(ast.RawStmt, None)


def test_special_function():
    output = RawStream(special_functions=True)

    assert output.get_printer_for_function('foo.test_function') is None

    try:
        @special_function('foo.test_function')
        def test(node, output):
            pass

        assert output.get_printer_for_function('foo.test_function') is test

        with pytest.raises(PrinterAlreadyPresentError):
            @special_function('foo.test_function')
            def test1(node, output):
                pass

        @special_function('foo.test_function', override=True)
        def test_function(node, output):
            output.print_list(node.args, '-')

        result = output('SELECT foo.test_function(x, "Y") FROM sometable')
        assert result == 'SELECT x - "Y" FROM sometable'
    finally:
        SPECIAL_FUNCTIONS.pop('foo.test_function')


def walked(sql):
    "Parse `sql` and populate the *ancestors* of the whole tree, then return the tree."

    tree = parse_sql(sql)
    visitors.populate_ancestors(tree)
    return tree


def first_expr(tree):
    "Return the first select target expression of a tree."

    return tree[0].stmt.targetList[0].val


def test_expr_context_default():
    assert RawStream().expr_context is ExprContext.A_EXPR


def test_push_expr_context():
    output = RawStream()

    with output.push_expr_context(ExprContext.B_EXPR):
        assert output.expr_context is ExprContext.B_EXPR
        with output.push_expr_context(ExprContext.C_EXPR):
            assert output.expr_context is ExprContext.C_EXPR
        assert output.expr_context is ExprContext.B_EXPR

    assert output.expr_context is ExprContext.A_EXPR


def test_push_expr_context_restores_after_error():
    output = RawStream()

    with pytest.raises(RuntimeError):
        with output.push_expr_context(ExprContext.B_EXPR):
            raise RuntimeError('boom')

    assert output.expr_context is ExprContext.A_EXPR


def test_print_operand_wraps_tighter_binding_on_the_left():
    "``(a + b) * c``: the ADD sub-expression must be parenthesized under MUL."

    tree = walked('SELECT (a + b) * c')
    star = first_expr(tree)
    plus = star.lexpr

    output = RawStream()
    output.print_operand(plus, ExprPrec.MUL, Side.LEFT)
    output.write(' * ')
    output.print_operand(star.rexpr, ExprPrec.MUL, Side.RIGHT)

    assert output.getvalue() == '(a + b) * c'


def test_print_operand_does_not_wrap_looser_binding():
    "``a + b * c``: the MUL sub-expression needs no parens under ADD."

    star = first_expr(walked('SELECT a + b * c')).rexpr

    output = RawStream()
    output.print_operand(star, ExprPrec.ADD, Side.RIGHT)

    assert output.getvalue() == 'b * c'


@pytest.mark.parametrize('side', (Side.LEFT, Side.RIGHT))
def test_print_operand_non_associative(side):
    "A non-associative operator at the same precedence always gets parens."

    output = RawStream()
    output.print_operand(first_expr(walked('SELECT a IS NULL')), ExprPrec.IS, side)

    assert output.getvalue() == '(a IS NULL)'


def test_print_operand_defaults_to_current_context():
    "Without an explicit ctx the operand inherits the current expression context."

    node = first_expr(walked('SELECT a IS NULL'))
    output = RawStream()

    with output.push_expr_context(ExprContext.B_EXPR):
        # At OR parent precedence the precedence rules alone would not add parens: it is the
        # b_expr context that forces them, since "IS NULL" is not a b_expr
        output.print_operand(node, ExprPrec.OR, Side.LEFT)

    assert output.getvalue() == '(a IS NULL)'


def test_print_operand_b_expr_context():
    "A b_expr operand in B_EXPR context is printed unwrapped, and in b_expr context."

    tree = walked('SELECT (a + b) * c')
    plus = first_expr(tree).lexpr
    output = RawStream()

    with output.push_expr_context(ExprContext.B_EXPR):
        output.print_operand(plus, ExprPrec.ADD, Side.LEFT)
        assert output.expr_context is ExprContext.B_EXPR

    assert output.getvalue() == 'a + b'
    assert output.expr_context is ExprContext.A_EXPR


def test_print_operand_switches_needed_operand_to_a_expr():
    "When parens are added the operand's context becomes a_expr, and is restored after."

    output = RawStream()

    with output.push_expr_context(ExprContext.B_EXPR):
        output.print_operand(first_expr(walked('SELECT a IS NULL')), ExprPrec.OR, Side.LEFT)
        assert output.expr_context is ExprContext.B_EXPR

    assert output.getvalue() == '(a IS NULL)'


def test_b_expr_wraps_non_b_expr():
    "A value that is not a b_expr is parenthesized, and printed in a_expr context."

    output = RawStream()
    output.print_b_expr(first_expr(walked('SELECT a IS NULL')))

    assert output.getvalue() == '(a IS NULL)'
    assert output.expr_context is ExprContext.A_EXPR


def test_b_expr_plain():
    "A b_expr value is printed as is, in b_expr context."

    tree = walked('SELECT (a + b) * c')
    plus = first_expr(tree).lexpr
    output = RawStream()

    output.print_b_expr(plus)
    assert output.expr_context is ExprContext.A_EXPR

    assert output.getvalue() == 'a + b'


def test_expression_still_emits_bare_container():
    "expression() remains the primitive for literal containers, independent of precedence."

    output = RawStream()

    with output.expression(True):
        output.print_node(first_expr(walked('SELECT (a + b) * c')).lexpr)

    assert output.getvalue() == '(a + b)'


def test_print_operand_on_indented_stream():
    "The new method is inherited by the prettifier, with no spurious whitespace."

    tree = walked('SELECT (a + b) * c')
    star = first_expr(tree)

    output = IndentedStream()
    output.print_operand(star.lexpr, ExprPrec.MUL, Side.LEFT)
    output.write(' * ')
    output.print_operand(star.rexpr, ExprPrec.MUL, Side.RIGHT)

    assert output.getvalue() == '(a + b) * c'
