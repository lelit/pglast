# -*- coding: utf-8 -*-
# :Project:   pglast -- Tests on the visitors module
# :Created:   mar 11 mag 2021, 08:36:23
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021 Lele Gaifax
#

import pytest

from pglast import parse_sql, visitors


def test_referenced_tables():
    rr = visitors.referenced_relations

    assert rr('select 1') == set()
    assert rr('select 1 from schemata.relation') == {'schemata.relation'}
    assert rr('WITH q1(x,y) AS (SELECT 1,2) SELECT * FROM q1, q2') == {'q2'}
    assert rr('create table foo (int a, int b references f(id))') == {'foo', 'f'}
    assert rr('create view foo.bar as select 1 from there') == {'foo.bar', 'there'}
    assert rr('drop view foo.bar, bar.foo') == {'foo.bar', 'bar.foo'}
    assert rr('drop table foo.bar, bar.foo') == {'foo.bar', 'bar.foo'}
    assert rr('select a from b.c.d') == {'b.c.d'}


def test_visitor_class():
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

    stmt = raw[0].stmt
    assert counter(raw[0].stmt) == 4

    with pytest.raises(ValueError):
        visitors.Visitor()('foo')
