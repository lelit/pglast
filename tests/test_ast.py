# -*- coding: utf-8 -*-
# :Project:   pglast — Tests ast module
# :Created:   sab 29 mag 2021, 21:25:46
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021, 2022, 2023, 2024 Lele Gaifax
#

import pytest

from pglast import ast, enums, parse_sql


def test_compare():
    assert ast.String() != ast.Integer()


def test_bad_values():
    with pytest.raises(ValueError) as e:
        ast.VariableShowStmt({'@': 'SelectStmt'})
    assert "expected 'VariableShowStmt', got 'SelectStmt'" in str(e.value)


def test_call():
    raw = parse_sql('select 1')[0]
    assert raw(0) == {'@': 'RawStmt', 'stmt': ..., 'stmt_len': 0, 'stmt_location': 0}
    assert raw(1)['stmt']['targetList'] == ...
    assert raw(1)['stmt']['targetList'] != 1

    raw = parse_sql('alter table t add constraint c'
                    ' exclude using gist (f with operator(&&))')[0]
    assert raw.stmt.cmds[0].def_(None, skip_none=True)['exclusions'] == (
        ({'@': 'IndexElem',
          'name': 'f',
          'ordering': {'#': 'SortByDir',
                       'name': 'SORTBY_DEFAULT',
                       'value': 0},
          'nulls_ordering': {'#': 'SortByNulls',
                             'name': 'SORTBY_NULLS_DEFAULT',
                             'value': 0}},
         ({'@': 'String', 'sval': '&&'},)),
    )


def test_setattr():
    raw = ast.RawStmt()
    with pytest.raises(ValueError):
        raw.stmt = 'foo'
    raw.stmt = {'@': 'SelectStmt', 'all': True}
    with pytest.raises(ValueError):
        raw.stmt = {'@': 'SelectStmt', 'all': 'foo'}
    raw.stmt = {'@': 'SelectStmt',
                'fromClause': ({'@': 'RangeVar',
                                'relname': 'sometable',
                                'relpersistence': 'p'},)}
    raw.stmt = {'@': 'SelectStmt',
                'fromClause': ({'@': 'RangeVar',
                                'relname': 'sometable',
                                'relpersistence': ord('p')},)}
    with pytest.raises(ValueError):
        raw.stmt = {'@': 'SelectStmt',
                    'fromClause': ({'@': 'RangeVar',
                                    'relname': 'sometable',
                                    'relpersistence': 'foo'},)}
    raw.stmt = {'@': 'VariableShowStmt', 'name': 'all'}
    with pytest.raises(ValueError):
        raw.stmt = {'@': 'VariableShowStmt', 'name': True}
    with pytest.raises(ValueError):
        raw.stmt = {'@': 'SelectStmt', 'limitOption': {'#': 'foo'}}
    raw.stmt = {'@': 'SelectStmt', 'limitOption': {'#': 'LimitOption',
                                                   'name': 'LIMIT_OPTION_DEFAULT'}}
    raw.stmt = {'@': 'SelectStmt', 'limitOption': {'#': 'LimitOption',
                                                   'value': 0}}
    with pytest.raises(ValueError):
        raw.stmt = {'@': 'SelectStmt', 'limitOption': {'#': 'LimitOption'}}
    with pytest.raises(ValueError):
        raw.stmt = {'@': 'SelectStmt', 'limitOption': {'#': 'LimitOption',
                                                       'name': 'foo'}}
    with pytest.raises(ValueError):
        raw.stmt = {'@': 'SelectStmt', 'limitOption': {'#': 'LimitOption',
                                                       'value': -1}}
    raw.stmt = {'@': 'FunctionParameter'}
    raw.stmt.argType = {'@': 'TypeName'}
    raw.stmt = ast.CreateForeignTableStmt()
    raw.stmt.base = {'@': 'CreateStmt'}


def test_issue_97():
    ast.SubLink({
        "@": "SubLink",
        "subLinkType": enums.SubLinkType.ANY_SUBLINK,
        "testexpr": ast.ColumnRef(
            {
                "@": "ColumnRef",
                "fields": (
                    ast.String({"@": "String", "val": "tab"}),
                    ast.String({"@": "String", "val": "_id"}),
                ),
            }
        ),
    })


def test_issue_138():
    raw = parse_sql('select * from foo')[0]
    ast.RawStmt(raw())


def test_issue_153():
    selstmt = parse_sql('select t.y from f(5) as t')[0].stmt
    serialized = selstmt()
    assert serialized['@'] == 'SelectStmt'
    clone = ast.SelectStmt(serialized)
    orig_fromc = selstmt.fromClause[0]
    orig_fc_funcs = orig_fromc.functions
    clone_fromc = clone.fromClause[0]
    clone_fc_funcs = clone_fromc.functions
    assert orig_fc_funcs == clone_fc_funcs
    assert selstmt == clone


def test_issue_153b():
    serialized = {
        '@': 'RangeFunction',
        'alias': {'@': 'Alias', 'aliasname': 'tmp', 'colnames': None},
        'coldeflist': None,
        'functions': (({'@': 'FuncCall',
                        'agg_distinct': False,
                        'agg_filter': None,
                        'agg_order': None,
                        'agg_star': False,
                        'agg_within_group': False,
                        'args': ({'@': 'A_Const',
                                  'isnull': False,
                                  'val': {'@': 'Integer', 'ival': 5}},),
                        'func_variadic': False,
                        'funcformat': {'#': 'CoercionForm',
                                       'name': 'COERCE_EXPLICIT_CALL',
                                       'value': 0},
                        'funcname': ({'@': 'String', 'sval': 'f'},),
                        'location': 21,
                        'over': None},
                       None),),
        'is_rowsfrom': False,
        'lateral': False,
        'ordinality': False}
    rf = ast.RangeFunction(serialized)
    assert isinstance(rf.functions[0][0], ast.FuncCall)


@pytest.mark.parametrize('cls, attr, child', (
    (ast.NullTest, 'arg', ast.ColumnRef(fields=(ast.String(sval='x'),))),
    (ast.BooleanTest, 'arg', ast.ColumnRef()),
    (ast.CaseExpr, 'arg', ast.ColumnRef()),
    (ast.CaseWhen, 'expr', ast.A_Const(val=ast.Integer(ival=1))),
    (ast.RawStmt, 'stmt', ast.SelectStmt()),
    (ast.CallStmt, 'funccall', ast.FuncCall()),
    (ast.CreateForeignTableStmt, 'base', ast.CreateStmt()),
))
def test_first_field_child_payload(cls, attr, child):
    # A serialized child should behave like the equivalent node instance.
    expected = cls(**{attr: child})
    assert cls(**{attr: child()}) == expected
    assert cls(child()) == expected
    # The established whole-node serialization overload must still work.
    assert cls(expected()) == expected


def test_first_field_payload_validation():
    with pytest.raises(ValueError):
        ast.CallStmt(funccall={'@': 'ColumnRef'})
    with pytest.raises(ValueError):
        ast.NullTest(arg={'@': 'ColumnRef', 'fields': 123})
