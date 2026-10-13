# -*- coding: utf-8 -*-
# :Project:   pglast — Test precedence machinery
# :Created:   mer 07 ott 2026 10:30:00 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2026 Lele Gaifax
#

"""
Tests for the precedence/position aware parenthesization machinery, see issue #211.

These exercise :mod:`pglast.precedence` in isolation, checking the rules themselves rather than
the rendered SQL, which is covered by the roundtrip corpora.
"""

import pytest

from pglast import enums, parse_sql
from pglast.ast import SubLink
from pglast.precedence import (
    ExprContext,
    ExprPrec,
    Side,
    expr_precedence,
    is_b_expr_rule,
    is_subquery_comparison_form,
    needs_parens_as_c_expr,
    needs_parens_for_precedence,
    operator_precedence,
    subquery_operator_precedence,
)
from pglast.stream import RawStream


plain = RawStream()
"Stream with the default options."

special = RawStream(special_functions=True)
"Stream with the *special functions* mode enabled."


def expr(sql):
    "Parse `sql` as a single expression and return its node."

    return parse_sql('SELECT ' + sql)[0].stmt.targetList[0].val


@pytest.mark.parametrize('name, expected', (
    ('+', ExprPrec.ADD),
    ('-', ExprPrec.ADD),
    ('*', ExprPrec.MUL),
    ('/', ExprPrec.MUL),
    ('%', ExprPrec.MUL),
    ('^', ExprPrec.EXP),
    ('<', ExprPrec.COMPARISON),
    ('>', ExprPrec.COMPARISON),
    ('=', ExprPrec.COMPARISON),
    ('<=', ExprPrec.COMPARISON),
    ('>=', ExprPrec.COMPARISON),
    ('<>', ExprPrec.COMPARISON),
    ('!=', ExprPrec.COMPARISON),
    # Any other operator, including OPERATOR(schema.op), has the precedence of Op
    ('@>', ExprPrec.OP),
    ('||', ExprPrec.OP),
    ('#', ExprPrec.OP),
))
def test_operator_precedence(name, expected):
    assert operator_precedence([name]) == expected


def test_operator_precedence_qualified():
    "``OPERATOR(schema.op)`` is a multi-element name, always with the precedence of Op."

    # parse_sql gives A_Expr.name as a list of String nodes, here ['pg_catalog', '+']
    node = expr('1 OPERATOR(pg_catalog.+) 2')
    assert [s.sval for s in node.name] == ['pg_catalog', '+']
    assert operator_precedence(node.name) == ExprPrec.OP
    assert expr_precedence(node, plain) == ExprPrec.OP


def test_operator_precedence_unknown():
    assert operator_precedence(None) == ExprPrec.OP
    assert operator_precedence([]) == ExprPrec.OP


@pytest.mark.parametrize('name, expected', (
    # These are output as [NOT] LIKE / [NOT] ILIKE by the subquery operator printer
    ('~~', ExprPrec.BETWEEN),
    ('!~~', ExprPrec.BETWEEN),
    ('~~*', ExprPrec.BETWEEN),
    ('!~~*', ExprPrec.BETWEEN),
    # Everything else falls back to the plain operator precedence
    ('=', ExprPrec.COMPARISON),
    ('@>', ExprPrec.OP),
))
def test_subquery_operator_precedence(name, expected):
    assert subquery_operator_precedence([name]) == expected


@pytest.mark.parametrize('sql, expected', (
    ('1 + 2', ExprPrec.ADD),
    ('1 - 2', ExprPrec.ADD),
    ('1 * 2', ExprPrec.MUL),
    ('1 / 2', ExprPrec.MUL),
    ('1 ^ 2', ExprPrec.EXP),
    ('1 = 2', ExprPrec.COMPARISON),
    ('1 @> 2', ExprPrec.OP),
    # Unary + and - have UMINUS precedence, any other prefix operator that of Op
    ('-(1 + 1)', ExprPrec.UMINUS),
    ('- a', ExprPrec.UMINUS),
    ('~(1 + 1)', ExprPrec.OP),
    # NULLIF is printed with the function call syntax
    ('NULLIF(a, b)', ExprPrec.ATOM),
    # IS/IS DISTINCT FROM are non-associative
    ('a IS DISTINCT FROM b', ExprPrec.IS),
    ('a IS NOT DISTINCT FROM b', ExprPrec.IS),
    # IN, LIKE, ILIKE, SIMILAR TO and BETWEEN are all handled by the same rule
    ('a IN (1, 2)', ExprPrec.BETWEEN),
    ('a NOT IN (1, 2)', ExprPrec.BETWEEN),
    ('a LIKE b', ExprPrec.BETWEEN),
    ('a ILIKE b', ExprPrec.BETWEEN),
    ('a SIMILAR TO b', ExprPrec.BETWEEN),
    ('a BETWEEN b AND c', ExprPrec.BETWEEN),
    ('a NOT BETWEEN b AND c', ExprPrec.BETWEEN),
    # BoolExpr
    ('a AND b', ExprPrec.AND),
    ('a OR b', ExprPrec.OR),
    ('NOT a', ExprPrec.NOT),
    # NullTest/BooleanTest/JsonIsPredicate/XmlExpr IS DOCUMENT
    ('a IS NULL', ExprPrec.IS),
    ('a IS NOT NULL', ExprPrec.IS),
    ('a IS TRUE', ExprPrec.IS),
    ('a IS DOCUMENT', ExprPrec.IS),
    ('a IS JSON', ExprPrec.IS),
    # CollateClause
    ('a COLLATE "C"', ExprPrec.COLLATE),
    # Everything else is ATOM
    ('a', ExprPrec.ATOM),
    ('1', ExprPrec.ATOM),
    ('count(*)', ExprPrec.ATOM),
    ('a[1]', ExprPrec.ATOM),
    ('CAST(a AS int)', ExprPrec.ATOM),
    ('(SELECT 1)', ExprPrec.ATOM),
))
def test_expr_precedence(sql, expected):
    assert expr_precedence(expr(sql), plain) == expected


def test_expr_precedence_none():
    assert expr_precedence(None, plain) == ExprPrec.ATOM


def test_expr_precedence_sublink():
    "A ``SubLink`` with no ``operName`` is the ``IN (...)`` form, i.e. BETWEEN precedence."

    node = expr('a IN (SELECT 1)')
    assert isinstance(node, SubLink)
    assert node.subLinkType == enums.SubLinkType.ANY_SUBLINK
    assert node.operName is None
    assert expr_precedence(node, plain) == ExprPrec.BETWEEN

    # With an operator name it is a subquery comparison, with that operator's precedence
    node = expr('a = ANY(SELECT 1)')
    assert isinstance(node, SubLink)
    assert node.subLinkType == enums.SubLinkType.ANY_SUBLINK
    assert [s.sval for s in node.operName] == ['=']
    assert expr_precedence(node, plain) == ExprPrec.COMPARISON

    # Other SubLinks are atoms
    node = expr('EXISTS(SELECT 1)')
    assert node.subLinkType == enums.SubLinkType.EXISTS_SUBLINK
    assert expr_precedence(node, plain) == ExprPrec.ATOM


@pytest.mark.parametrize('sql, expected', (
    # The precedence is min(subquery_operator_precedence(name), OP)
    ('a = ANY(ARRAY[1, 2])', ExprPrec.COMPARISON),
    ('a < ALL(ARRAY[1, 2])', ExprPrec.COMPARISON),
    # The ~~ family is printed as LIKE/ILIKE, hence BETWEEN
    ('a ~~ ANY(ARRAY[1, 2])', ExprPrec.BETWEEN),
    ('a LIKE ANY(ARRAY[1, 2])', ExprPrec.BETWEEN),
))
def test_expr_precedence_op_any_all(sql, expected):
    node = expr(sql)
    assert node.kind in (enums.A_Expr_Kind.AEXPR_OP_ANY, enums.A_Expr_Kind.AEXPR_OP_ALL)
    assert expr_precedence(node, plain) == expected


def test_expr_precedence_special_functions_mode():
    # ``AT TIME ZONE`` and ``IS ... NORMALIZED`` depend on the stream's special_functions options
    assert expr_precedence(expr("a AT TIME ZONE 'UTC'"), plain) == ExprPrec.ATOM
    assert expr_precedence(expr("a AT TIME ZONE 'UTC'"), special) == ExprPrec.AT
    assert expr_precedence(expr("'x' IS NFC NORMALIZED"), plain) == ExprPrec.ATOM
    assert expr_precedence(expr("'x' IS NFC NORMALIZED"), special) == ExprPrec.IS


@pytest.mark.parametrize('sql, parent_prec, side, expected', (
    # Different precedence: parens iff the node binds looser than its parent
    ('1 * 2', ExprPrec.ADD, Side.RIGHT, False),
    ('1 + 2', ExprPrec.MUL, Side.LEFT, True),
    ('1 + 2', ExprPrec.MUL, Side.RIGHT, True),
    ('1 * 2', ExprPrec.ADD, Side.LEFT, False),
    # Same precedence, left-associative operators: only the right operand needs parens
    ('1 + 2', ExprPrec.ADD, Side.LEFT, False),
    ('1 + 2', ExprPrec.ADD, Side.RIGHT, True),
    ('1 * 2', ExprPrec.MUL, Side.RIGHT, True),
    # Non-associative: both sides need parens
    ('a IS NULL', ExprPrec.IS, Side.LEFT, True),
    ('a IS NULL', ExprPrec.IS, Side.RIGHT, True),
    ('a = b', ExprPrec.COMPARISON, Side.LEFT, True),
    ('a = b', ExprPrec.COMPARISON, Side.RIGHT, True),
    # Right-associative prefix operators never need parens
    ('NOT a', ExprPrec.NOT, Side.LEFT, False),
    ('NOT a', ExprPrec.NOT, Side.RIGHT, False),
    ('- a', ExprPrec.UMINUS, Side.LEFT, False),
    ('- a', ExprPrec.UMINUS, Side.RIGHT, False),
))
def test_needs_parens_for_precedence(sql, parent_prec, side, expected):
    assert needs_parens_for_precedence(expr(sql), parent_prec, side, plain) is expected


def test_needs_parens_for_precedence_subquery_comparison():
    "A subquery comparison form as the left operand at equal precedence needs no parens."

    node = expr('a = ANY(ARRAY[1, 2])')
    assert needs_parens_for_precedence(node, ExprPrec.COMPARISON, Side.LEFT, plain) is False

    # But the exception only applies as the left operand...
    assert needs_parens_for_precedence(node, ExprPrec.COMPARISON, Side.RIGHT, plain) is True

    # ... and only at the same precedence: as the left operand of a tighter operator it must stay
    # parenthesized, otherwise the comparison would swallow the concatenation
    assert needs_parens_for_precedence(node, ExprPrec.OP, Side.LEFT, plain) is True

    # The "x IN (...)" form is the same, and a non-form never gets the exception
    assert needs_parens_for_precedence(expr('a IN (1, 2)'), ExprPrec.BETWEEN, Side.LEFT,
                                       plain) is False
    assert needs_parens_for_precedence(expr('a IN (1, 2)'), ExprPrec.OP, Side.LEFT,
                                       plain) is True
    assert needs_parens_for_precedence(expr('a + b'), ExprPrec.ADD, Side.LEFT, plain) is False


def test_is_subquery_comparison_form():
    assert is_subquery_comparison_form(expr('a = ANY(ARRAY[1])'))
    assert is_subquery_comparison_form(expr('a < ALL(ARRAY[1])'))
    assert is_subquery_comparison_form(expr('a IN (1, 2)'))
    assert not is_subquery_comparison_form(expr('a = b'))
    assert not is_subquery_comparison_form(expr('a + b'))
    assert not is_subquery_comparison_form(None)


@pytest.mark.parametrize('sql, expected', (
    # A_Expr handled by a b_expr rule
    ('1 + 2', True),
    ('1 = 2', True),
    ('a IS DISTINCT FROM b', True),
    ('NULLIF(a, b)', True),
    # XmlExpr IS DOCUMENT has its own b_expr rule
    ('a IS DOCUMENT', True),
    # Everything else that is not a c_expr is only handled by the a_expr rule
    ('a IS NULL', False),
    ('a IS TRUE', False),
    ('a COLLATE "C"', False),
    ('a IN (1, 2)', False),
    ('a BETWEEN b AND c', False),
    ('NOT a', False),
    ('a AND b', False),
    # c_expr nodes
    ('a', True),
    ('1', True),
    ('count(*)', True),
))
def test_is_b_expr_rule(sql, expected):
    assert is_b_expr_rule(expr(sql), plain) is expected


def test_is_b_expr_rule_none():
    "A missing node is not something that needs to be protected."

    assert is_b_expr_rule(None, plain) is True


def test_is_b_expr_rule_overlaps():
    "``row OVERLAPS row`` has its own b_expr rule, but only in special functions mode."

    node = expr('(a, b) OVERLAPS (c, d)')
    assert len(node.args) == 4
    # In the default mode it is printed as a plain function call, i.e. an ATOM
    assert is_b_expr_rule(node, plain) is True
    # In special functions mode it becomes the OVERLAPS form, only handled by the a_expr rule
    assert is_b_expr_rule(node, special) is False

    # With a different number of args it is never the OVERLAPS form
    assert is_b_expr_rule(expr('overlaps(a, b)'), special) is True


@pytest.mark.parametrize('sql, expected', (
    # ATOM nodes are fine, but anything else needs parens
    ('a', False),
    ('1', False),
    ('count(*)', False),
    ('a + b', True),
    ('a IS NULL', True),
    ('a COLLATE "C"', True),
    # IS DOCUMENT is an a_expr-only rule, despite being an ATOM
    ('a IS DOCUMENT', True),
))
def test_needs_parens_as_c_expr(sql, expected):
    assert needs_parens_as_c_expr(expr(sql), plain) is expected


def test_expr_context_is_internal_vocabulary():
    "The context constants must be an IntEnum with the three grammar rules."

    assert issubclass(ExprContext, int)
    assert [c.name for c in ExprContext] == ['A_EXPR', 'B_EXPR', 'C_EXPR']


def test_expr_prec_is_ordered():
    "The precedence ordering must be looser-to-tighter."

    assert [p.name for p in ExprPrec] == [
        'OR', 'AND', 'NOT', 'IS', 'COMPARISON', 'BETWEEN', 'OP', 'ADD', 'MUL', 'EXP', 'AT',
        'COLLATE', 'UMINUS', 'ATOM',
    ]
    assert ExprPrec.OR < ExprPrec.ATOM
    assert ExprPrec.ADD < ExprPrec.MUL < ExprPrec.EXP < ExprPrec.AT
