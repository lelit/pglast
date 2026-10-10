# -*- coding: utf-8 -*-
# :Project:   pglast -- Test that printed SQL re-parses to the same tree
# :Created:   ven 09 ott 2026 10:23:41 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2026 Lele Gaifax
#

from pytest import mark

from pglast import parse_sql
from pglast.stream import IndentedStream, RawStream


# Each case is (input SQL, expected RawStream output). The expected output is what pglast's own
# rendering style produces; the invariant that makes it *correct* is asserted separately, by
# reparsing it and comparing the trees.
CASES = [
    # Multiplication binds tighter than addition: no parens around the rexpr
    ('SELECT 1 + 2 * 3',
     'SELECT 1 + 2 * 3'),
    ('SELECT 1 + 2 * 3 - 4 / 5',
     'SELECT 1 + 2 * 3 - 4 / 5'),
    # ... but a looser left operand keeps them
    ('SELECT (x - 1) * 3',
     'SELECT (x - 1) * 3'),
    # - is left-associative, so a nested right operand needs parens
    ('SELECT a - (b - c)',
     'SELECT a - (b - c)'),
    # BETWEEN lower bound is a b_expr: a BoolExpr is not one
    ('SELECT * FROM t WHERE a BETWEEN (b OR c) AND d',
     'SELECT * FROM t WHERE a BETWEEN (b OR c) AND d'),
    ('SELECT * FROM t WHERE a BETWEEN b AND (c OR d)',
     'SELECT * FROM t WHERE a BETWEEN b AND (c OR d)'),
    ('SELECT * FROM t WHERE a NOT BETWEEN (b OR c) AND d',
     'SELECT * FROM t WHERE a NOT BETWEEN (b OR c) AND d'),
    # Subquery comparison: the left operand binds against the operator token
    ('SELECT * FROM t WHERE (a OR b) = ANY(SELECT 1)',
     'SELECT * FROM t WHERE (a OR b) = ANY (SELECT 1)'),
    ('SELECT * FROM t WHERE (a OR b) = ANY(ARRAY[1,2])',
     'SELECT * FROM t WHERE (a OR b) = ANY(ARRAY[1, 2])'),
    ('SELECT * FROM t WHERE (a OR b) = ALL(ARRAY[1,2])',
     'SELECT * FROM t WHERE (a OR b) = ALL(ARRAY[1, 2])'),
    ('SELECT * FROM t WHERE (a OR b) IN (SELECT 1)',
     'SELECT * FROM t WHERE (a OR b) IN (SELECT 1)'),
    # A tighter left operand stays paren-free
    ('SELECT * FROM t WHERE a = ANY(c)',
     'SELECT * FROM t WHERE a = ANY(c)'),
    # A qualified operator keeps its OPERATOR(...) form in the ANY/ALL position
    ('SELECT * FROM t WHERE a OPERATOR(pg_catalog.=) ANY(ARRAY[1,2])',
     'SELECT * FROM t WHERE a OPERATOR(pg_catalog.=) ANY(ARRAY[1, 2])'),
    # A LIKE operator used as a subquery comparison operator is spelled out
    ("SELECT a LIKE ANY(ARRAY['x'])",
     "SELECT a LIKE ANY(ARRAY['x'])"),
    # IS DISTINCT FROM is non-associative: nested ones need parens
    ('SELECT * FROM t WHERE (a IS DISTINCT FROM b) IS DISTINCT FROM c',
     'SELECT * FROM t WHERE (a IS DISTINCT FROM b) IS DISTINCT FROM c'),
    # LIKE binds looser than ||: the concatenation needs no parens
    ('SELECT * FROM t WHERE (a || b) LIKE c',
     'SELECT * FROM t WHERE a || b LIKE c'),
    # IS is non-associative: a BoolExpr operand keeps its parens, a tighter one drops them
    ('SELECT (a AND b) IS NULL',
     'SELECT (a AND b) IS NULL'),
    ('SELECT (NOT a) IS NULL',
     'SELECT (NOT a) IS NULL'),
    ('SELECT (a = b) IS NULL',
     'SELECT a = b IS NULL'),
    ('SELECT (a || b) IS NULL',
     'SELECT a || b IS NULL'),
    ('SELECT (a OR b) IS TRUE',
     'SELECT (a OR b) IS TRUE'),
    ('SELECT (a = b) IS TRUE',
     'SELECT a = b IS TRUE'),
    # COLLATE binds tighter than IS but looser than a comparison
    ('SELECT (a IS NULL) COLLATE "C"',
     'SELECT (a IS NULL) COLLATE "C"'),
    ('SELECT (a || b) COLLATE "C"',
     'SELECT (a || b) COLLATE "C"'),
    ('SELECT a COLLATE "C"',
     'SELECT a COLLATE "C"'),
    # Indirection: only PARAM, ColumnRef+subscript and (SELECT ...) take it without parens
    ('SELECT (a IS NULL)[1]',
     'SELECT (a IS NULL)[1]'),
    ('SELECT (NOT a)[1]',
     'SELECT (NOT a)[1]'),
    ('SELECT (a OR b)[1]',
     'SELECT (a OR b)[1]'),
    ('SELECT (a.b)[1]',
     'SELECT (a.b)[1]'),
    ('SELECT (a COLLATE "C")[1]',
     'SELECT (a COLLATE "C")[1]'),
    # IS DOCUMENT / IS JSON behave like IS: a NOT operand keeps its parens, a tighter one drops them
    ('SELECT (NOT a) IS DOCUMENT',
     'SELECT (NOT a) IS DOCUMENT'),
    ('SELECT (NOT a) IS JSON',
     'SELECT (NOT a) IS JSON'),
    ('SELECT (a || b) IS DOCUMENT',
     'SELECT a || b IS DOCUMENT'),
    ('SELECT (a || b) IS JSON',
     'SELECT a || b IS JSON'),
]


@mark.parametrize('sql, expected', CASES)
def test_raw_rendering(sql, expected):
    assert RawStream()(sql) == expected


@mark.parametrize('sql, _expected', CASES)
def test_roundtrip_invariant(sql, _expected):
    # The whole point of the exercise: what pglast prints must re-parse to the same tree
    assert parse_sql(RawStream()(sql)) == parse_sql(sql)
    assert parse_sql(IndentedStream()(sql)) == parse_sql(sql)
