# -*- coding: utf-8 -*-
# :Project:   pglast -- Tests ast module
# :Created:   sab 29 mag 2021, 21:25:46
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021 Lele Gaifax
#

import pytest

from pglast import ast, parse_sql


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
