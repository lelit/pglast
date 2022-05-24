# -*- coding: utf-8 -*-
# :Project:   pglast -- Tests on the visitors module
# :Created:   mar 11 mag 2021, 08:36:23
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021, 2022 Lele Gaifax
#

import pytest

from pglast import ast, enums, parse_sql, visitors
from pglast.stream import RawStream


def test_referenced_tables():
    rr = visitors.referenced_relations

    assert rr('select 1') == set()
    assert rr('select 1 from schemata.relation') == {'schemata.relation'}
    assert rr('with q1(x,y) as (select 1,2) select * from q1, q2') == {'q2'}
    assert rr('create table foo (int a, int b references f(id))') == {'foo', 'f'}
    assert rr('create view foo.bar as select 1 from there') == {'foo.bar', 'there'}
    assert rr('drop view foo.bar, bar.foo') == {'foo.bar', 'bar.foo'}
    assert rr('drop table foo.bar, bar.foo') == {'foo.bar', 'bar.foo'}
    assert rr('select a from b.c.d') == {'b.c.d'}


def test_visiting_path():
    from types import SimpleNamespace as SN

    root = SN(list=[SN(a='a'), SN(b='b')])
    proot = visitors.Ancestor()
    assert proot @ root is root
    assert None in proot
    assert list(proot) == [None]
    assert repr(proot) == 'ROOT'

    plist = proot / (root.list, 'list')
    assert plist @ root is root.list
    assert plist[0] is root.list
    assert plist[1] is None
    assert list(plist) == [None, 'list']
    assert repr(plist) == 'ROOT → list'

    pa = plist / (root.list[0], 0)
    assert pa @ root is root.list[0]
    assert pa[0] is root.list[0]
    assert pa[1] is root.list
    assert pa[2] is None
    assert list(pa) == [None, 'list', 0]
    assert repr(pa) == 'ROOT → list → 0'

    pb = plist / (root.list[1], 1)
    assert pb @ root is root.list[1]
    assert pb[0] is root.list[1]
    assert pb[1] is root.list
    assert pb[2] is None
    assert list(pb) == [None, 'list', 1]
    assert repr(pb) == 'ROOT → list → 1'


def test_invalid_argument():
    with pytest.raises(ValueError):
        visitors.Visitor()('foo')


def test_empty_visitor():
    v = visitors.Visitor()
    assert v(()) is None


def test_ancestors():
    class Checker(visitors.Visitor):
        def visit(self, ancestors, node):
            assert ancestors@self.root is node

    checker = Checker()

    raw = parse_sql('select 1')
    checker(raw)

    raw = parse_sql('SELECT * FROM ROWS FROM(generate_series(10,11), get_users())')
    checker(raw)


class CountAllNodes(visitors.Visitor):
    def __call__(self, node):
        self.count = 0
        super().__call__(node)
        return self.count

    def visit(self, ancestors, node):
        self.count += 1


def test_count_all_nodes():
    counter = CountAllNodes()

    raw = parse_sql('select 1')
    assert counter(raw) == 5
    assert counter(raw[0].stmt) == 4

    raw = parse_sql('SELECT * FROM ROWS FROM(generate_series(10,11), get_users())')
    assert counter(raw) == 14


def test_skip_action():
    sql = 'select 1 where a = 1'

    all_nodes_count = CountAllNodes()(parse_sql(sql))
    assert all_nodes_count == 11

    class CountNodesSkippingExprs(visitors.Visitor):
        def __call__(self, node):
            self.count = 0
            self.exprs = 0
            super().__call__(node)
            return self.count, self.exprs

        def visit(self, ancestors, node):
            if node.__class__.__name__ == 'A_Expr':
                self.exprs += CountAllNodes()(node)
                return visitors.Skip
            self.count += 1

    counter = CountNodesSkippingExprs()

    raw = parse_sql(sql)
    nodes, exprs = counter(raw)
    assert nodes == all_nodes_count - exprs

    class CountNodesSkippingTargets(visitors.Visitor):
        def __call__(self, node):
            self.count = 0
            self.targets = 0
            super().__call__(node)
            return self.count, self.targets

        def visit(self, ancestors, node):
            if node.__class__.__name__ == 'ResTarget':
                self.targets += CountAllNodes()(node)
                return visitors.Skip
            self.count += 1

    counter = CountNodesSkippingTargets()

    raw = parse_sql('select 1 where a = 1')
    nodes, targets = counter(raw)
    assert nodes == all_nodes_count - targets


def test_delete_action():
    class DropNullConstraint(visitors.Visitor):
        def visit_Constraint(self, ancestors, node):
            if node.contype == enums.ConstrType.CONSTR_NULL:
                return visitors.Delete

    raw = parse_sql('create table foo (a integer null, b integer not null)')
    DropNullConstraint()(raw)
    assert RawStream()(raw) == 'CREATE TABLE foo (a integer, b integer NOT NULL)'

    raw = parse_sql('create table foo (a integer null check (a <> 0))')
    DropNullConstraint()(raw)
    assert RawStream()(raw) == 'CREATE TABLE foo (a integer CHECK (a <> 0))'


def test_alter_node():
    class AddNullConstraint(visitors.Visitor):
        def visit_ColumnDef(self, ancestors, node):
            if node.colname == 'a':
                node.constraints = (
                    {'@': 'Constraint',
                     'contype': {'#': 'ConstrType', 'name': 'CONSTR_NOTNULL'}},)

        def visit_Constraint(self, ancestors, node):
            if ancestors[1].colname == 'b':
                return ast.Constraint(
                    contype=enums.ConstrType.CONSTR_CHECK,
                    raw_expr=ast.A_Expr(kind=enums.A_Expr_Kind.AEXPR_OP,
                                        lexpr=ast.ColumnRef(fields=(ast.String('b'),)),
                                        name=(ast.String('>'),),
                                        rexpr=ast.A_Const(val=ast.Integer(0))))

    raw = parse_sql('create table foo (a integer null, b integer check (b <> 0))')
    AddNullConstraint()(raw)
    assert RawStream()(raw) == 'CREATE TABLE foo (a integer NOT NULL, b integer CHECK (b > 0))'

    class DoubleAllIntegers(visitors.Visitor):
        def visit_Integer(self, ancestors, node):
            return ast.Integer(node.val * 2)

    raw = parse_sql('select 21')
    DoubleAllIntegers()(raw)
    assert RawStream()(raw) == 'SELECT 42'


def test_replace_root_node():
    class AndNowForSomethingCompletelyDifferent(visitors.Visitor):
        def visit_RawStmt(self, ancestors, node):
            return ast.RawStmt(stmt=ast.VariableShowStmt(name='all'))

    raw = parse_sql('select 1')
    new_root = AndNowForSomethingCompletelyDifferent()(raw)
    assert RawStream()(new_root) == 'SHOW ALL'

    raw = parse_sql('select 1')
    new_root = AndNowForSomethingCompletelyDifferent()(raw[0])
    assert RawStream()(new_root) == 'SHOW ALL'
