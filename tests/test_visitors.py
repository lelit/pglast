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


@pytest.mark.parametrize('stmt,rnames', (
    # DDL
    ('alter table foo add foreign key (x) references bar (id)', {'foo', 'bar'}),
    ('create table foo (int a, int b references f(id))', {'foo', 'f'}),
    ('create view foo.bar as select 1 from there', {'foo.bar', 'there'}),
    ('drop table foo.bar, bar.foo', {'foo.bar', 'bar.foo'}),
    ('drop view foo.bar, bar.foo', {'foo.bar', 'bar.foo'}),
    ('drop view "my.schema".bar, bar."my.table", "foo.bar"',
     {'"my.schema".bar', 'bar."my.table"', '"foo.bar"'}),

    # DML
    ('insert into foo values (1)', {'foo'}),
    ('insert into foo select * from bar', {'foo', 'bar'}),
    ('select 1', set()),
    ('select 1 from schemata.relation', {'schemata.relation'}),
    ('select a from b.c.d', {'b.c.d'}),
    ('select * from "my.schema"."my.table"', {'"my.schema"."my.table"'}),
    ('update foo set a=1', {'foo'}),

    # CTE
    ('with q1(x,y) as (select 1,2) select * from q1, q2', {'q2'}),
    ('with my_ref as (select * from my_ref where a=1) select * from my_ref',
     {'my_ref'}),
    ('with cte1 as (select 1), cte2 as (select * from cte1) select * from cte2',
     set()),
    ('''
     with recursive t(n) as (values (1) union all select n+1 from t where n < 100)
       select sum(n) from t
     ''', set()),
    ('''
     with cte1 as (select 1)
       select * from (with cte2 as (select * from cte1)
                        select * from cte2) as a
     ''', set()),
    ('''
     with to_archive as (delete from products where date < '2010-11-01' returning *)
       insert into products_log select * from to_archive
     ''', {'products', 'products_log'}),
    ('with "foo.bar" as (select * from tab) select * from "foo.bar"', {'tab'}),
    ('select (with my_ref as (select 1) select 1) from my_ref', {'my_ref'}),
    ('''
     with cte1 as (select 1)
        , cte2 as (with cte1 as (select * from cte1) select * from cte1)
       select * from cte2
     ''', set()),
    ('''
     with recursive t1 as (
       insert into yy select * from t2 returning *
     ), t2 as (
       insert into y select * from y returning *
     )
     select 1;
     ''', {'y', 'yy'}),
    ('''
     with recursive t(a) as (
       select 11
       union all
       select a+1 from t where a < 50
     )
     delete from y using t where t.a = y.a returning y.a
     ''', {'y'}),
    ('''
     with t as (
         delete from y
         where a <= 10
         returning *
     )
     select * from t
     ''', {'y'}),
    ('''
     select count(*) from (
       with q1(x) as (select random() from generate_series(1, 5))
         select * from q1
       union
         select * from q1
     ) ss
     ''', set())
))
def test_referenced_tables(stmt, rnames):
    assert visitors.referenced_relations(stmt) == rnames


def test_visiting_path():
    from types import SimpleNamespace as SN

    root = SN(list=[SN(a='a'), SN(b='b')])
    proot = visitors.Ancestor()
    assert proot @ root is root
    assert repr(proot) == 'ROOT'

    plist = proot / (root.list, 'list')
    assert plist @ root is root.list
    assert plist[0] is root.list
    assert plist[1] is None
    assert repr(plist) == 'ROOT → list'

    pa = plist / (root.list[0], 0)
    assert pa @ root is root.list[0]
    assert pa[0] is root.list[0]
    assert pa[1] is root.list
    assert pa[2] is None
    assert repr(pa) == 'ROOT → list → 0'

    pb = plist / (root.list[1], 1)
    assert pb @ root is root.list[1]
    assert pb[0] is root.list[1]
    assert pb[1] is root.list
    assert pb[2] is None
    assert repr(pb) == 'ROOT → list → 1'


def test_invalid_argument():
    with pytest.raises(ValueError):
        visitors.Visitor()('foo')


def test_empty_visitor():
    v = visitors.Visitor()
    assert v(()) is None


def test_ancestors():
    class Checker(visitors.Visitor):
        def visit_RawStmt(self, ancestors, node):
            pass

        def visit(self, ancestors, node):
            assert ancestors@self.root is node
            assert ast.RawStmt in ancestors
            assert ast.InsertStmt not in ancestors

    checker = Checker()

    raw = parse_sql('select 1')
    checker(raw)

    raw = parse_sql('SELECT * FROM ROWS FROM(generate_series(10,11), get_users())')
    checker(raw)


def test_closest_node():
    class Checker(visitors.Visitor):
        def visit(self, ancestors, node):
            if isinstance(node, ast.FuncCall):
                assert isinstance(ancestors[0], tuple)
                assert isinstance(abs(ancestors).node, ast.RangeFunction)

    raw = parse_sql('SELECT * FROM ROWS FROM(generate_series(10,11), get_users())')
    Checker()(raw)


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

    class DeleteOddsInList(visitors.Visitor):
        def visit_A_Const(self, ancestors, node):
            if isinstance(node.val, ast.Integer):
                if node.val.ival % 2:
                    return visitors.Delete

    raw = parse_sql('INSERT INTO foo VALUES (1, 2, 3, 42, 43)')
    DeleteOddsInList()(raw)
    assert RawStream()(raw) == 'INSERT INTO foo VALUES (2, 42)'

    raw = parse_sql('INSERT INTO foo VALUES ((1, 2, 3, 42, 43),'
                    ' (2, 1, 4, 3, 5))')
    DeleteOddsInList()(raw)
    assert RawStream()(raw) == 'INSERT INTO foo VALUES ((2, 42), (2, 4))'

    raw = parse_sql('select true from foo where a in (1, 2, 3)')
    DeleteOddsInList()(raw)
    assert RawStream()(raw) == 'SELECT TRUE FROM foo WHERE a IN (2)'


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
            return ast.Integer(node.ival * 2)

    raw = parse_sql('select 21')
    DoubleAllIntegers()(raw)
    assert RawStream()(raw) == 'SELECT 42'

    class ReplaceConstantInList(visitors.Visitor):
        def visit_A_Const(self, ancestors, node):
            return ast.A_Const(val=ast.Integer(0))

    raw = parse_sql('INSERT INTO foo VALUES (42)')
    ReplaceConstantInList()(raw)
    assert RawStream()(raw) == 'INSERT INTO foo VALUES (0)'


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
