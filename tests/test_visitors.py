# -*- coding: utf-8 -*-
# :Project:   pglast -- Tests on the visitors module
# :Created:   mar 11 mag 2021, 08:36:23
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021 Lele Gaifax
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
    proot = visitors.VisitingPath()
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


def test_empty_visitor():
    v = visitors.Visitor()
    assert v(()) is None


def test_count_all_nodes():
    class CountNodes(visitors.Visitor):
        def __call__(self, node):
            self.count = 0
            super().__call__(node)
            return self.count

        def visit(self, path, node):
            self.count += 1

    counter = CountNodes()

    raw = parse_sql('select 1')
    assert counter(raw) == 5

    assert counter(raw[0].stmt) == 4

    with pytest.raises(ValueError):
        visitors.Visitor()('foo')


def test_skip_action():
    class CountNodes(visitors.Visitor):
        def __call__(self, node):
            self.count = 0
            super().__call__(node)
            return self.count

        def visit(self, path, node):
            if node.__class__.__name__ == 'A_Expr':
                return visitors.Skip
            self.count += 1

    counter = CountNodes()

    raw = parse_sql('select 1 where a = 1')
    assert counter(raw) == 5


def test_delete_action():
    class DropNullConstraint(visitors.Visitor):
        def visit_Constraint(self, path, node):
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
        def visit_ColumnDef(self, path, node):
            if node.colname == 'a':
                node.constraints = (
                    {'@': 'Constraint',
                     'contype': {'#': 'ConstrType', 'name': 'CONSTR_NOTNULL'}},)

        def visit_Constraint(self, path, node):
            if path[1].colname == 'b':
                return ast.Constraint(
                    contype=enums.ConstrType.CONSTR_CHECK,
                    raw_expr=ast.A_Expr(kind=enums.A_Expr_Kind.AEXPR_OP,
                                        lexpr=ast.ColumnRef(fields=(ast.String('b'),)),
                                        name=(ast.String('>'),),
                                        rexpr=ast.A_Const(val=ast.Integer(0))))

    raw = parse_sql('create table foo (a integer null, b integer check (b <> 0))')
    AddNullConstraint()(raw)
    assert RawStream()(raw) == 'CREATE TABLE foo (a integer NOT NULL, b integer CHECK (b > 0))'


def test_replace_root_node():
    class AndNowForSomethingCompletelyDifferent(visitors.Visitor):
        def visit_RawStmt(self, path, node):
            return ast.RawStmt(stmt=ast.VariableShowStmt(name='all'))

    raw = parse_sql('select 1')
    new_root = AndNowForSomethingCompletelyDifferent()(raw[0])
    assert RawStream()(new_root) == 'SHOW ALL'
