# -*- coding: utf-8 -*-
# :Project:   pglast -- Test the node.py module
# :Created:   ven 04 ago 2017 09:31:57 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018 Lele Gaifax
#

import enum

import pytest

from pglast import Missing, Node
from pglast.node import Base, List, Scalar


class DummyEnum(str, enum.Enum):
    A = 'a'
    B = 'b'


class DummyIntEnum(enum.IntEnum):
    ZERO = 0
    ONE = 1


def test_bad_base_construction():
    pytest.raises(ValueError, Base, {})
    pytest.raises(ValueError, Base, [])
    pytest.raises(ValueError, Base, {'Foo': 'bar', 'Bar': 'foo'})
    pytest.raises(ValueError, Base, {'Foo': {'some': 'value'}}, parent=1.0)
    pytest.raises(ValueError, Base, {'Foo': {'some': 'value'}}, name=1.0)
    pytest.raises(ValueError, Base, set())


def test_basic():
    ptree = [{'Foo': {'bar': {'Bar': {'a': 1, 'b': 'b', 'c': None, 'd': 0}}}},
             {'Foo': {'bar': {'Bar': {'a': 0, 'f': False, 't': True, 'c': [
                 {'C': {'x': 0, 'y': 0}},
                 {'C': {'x': 0, 'y': 0}}
             ]}}}}]

    root = Node(ptree)
    assert root.parent_node is None
    assert root.parent_attribute is None
    assert isinstance(root, List)
    assert len(root) == 2
    assert repr(root) == '[2*{Foo}]'
    assert str(root) == 'None=[2*{Foo}]'
    with pytest.raises(AttributeError):
        root.not_there

    foo1 = root[0]
    assert foo1 != root
    assert foo1.node_tag == 'Foo'
    assert foo1.parse_tree == {'bar': {'Bar': {'a': 1, 'b': 'b', 'c': None, 'd': 0}}}
    assert foo1.parent_node is None
    assert foo1.parent_attribute == (None, 0)
    assert repr(foo1) == '{Foo}'
    assert str(foo1) == 'None[0]={Foo}'
    assert foo1.attribute_names == {'bar'}
    assert foo1.not_there is Missing
    assert not foo1.not_there
    assert repr(foo1.not_there) == 'MISSING'
    with pytest.raises(ValueError):
        foo1[1.0]

    bar1 = foo1.bar
    assert bar1 != foo1
    assert bar1.node_tag == 'Bar'
    assert bar1.parent_node is foo1
    assert bar1.parent_attribute == 'bar'
    assert bar1.attribute_names == {'a', 'b', 'c', 'd'}
    assert foo1[bar1.parent_attribute] == bar1
    assert repr(bar1.a) == '<1>'
    assert repr(bar1.b) == "<'b'>"
    assert repr(bar1.c) == '<None>'
    assert bar1.a & 1
    with pytest.raises(ValueError):
        bar1.a & 'a'
    with pytest.raises(ValueError):
        bar1.b & 1

    # __str__
    assert str(bar1) == 'bar={Bar}'
    assert str(bar1.a) == 'a=<1>'
    assert str(bar1.b) == "b=<'b'>"

    # Scalar.__bool__
    assert bar1.a
    assert bar1.b
    assert bar1.c.value is None
    assert not bar1.c
    assert bar1.d

    # Scalar.__eq__
    assert bar1.a == 1
    assert bar1.a == DummyIntEnum.ONE
    assert bar1.a != DummyIntEnum.ZERO
    assert bar1.b == 'b'
    assert bar1.b == DummyEnum.B
    assert bar1.b != DummyEnum.A

    foo2 = root[1]
    assert foo2 != foo1

    bar2 = foo2['bar']
    assert bar2 != bar1
    assert bar2.parent_attribute == 'bar'
    assert bar2.attribute_names == {'a', 'c', 'f', 't'}
    assert bar2.a == DummyIntEnum.ZERO
    assert bar2.a != DummyIntEnum.ONE
    assert not bar2.f
    assert bar2.t
    assert repr(bar2.f) == '<False>'
    assert repr(bar2.t) == '<True>'

    c = bar2.c
    assert isinstance(c, List)
    assert len(c) == 2
    assert repr(c) == '[2*{C}]'

    c1 = c[0]
    c2 = c[1]
    assert c1.parent_attribute == ('c', 0)
    assert c2.parent_attribute == ('c', 1)
    assert c1 != c2
    assert c1.parent_node[c1.parent_attribute] == c1
    assert str(c1) == 'c[0]={C}'
    assert str(c2) == 'c[1]={C}'

    x1 = c1['x']
    x2 = c2['x']
    assert isinstance(x1, Scalar)
    assert x1 != x2
    assert x1.value == x2.value


def test_string_value():
    ptree = [{'Foo': {'ok': {'String': {'str': 'foo'}},
                      'ko': {'Float': {'float': 3.14159}}}},
             {'Bar': {'ok': [{'String': {'str': 'bar'}}],
                      'ko': [{'String': {'str': 'bar1'}},
                             {'String': {'str': 'bar2'}}]}},
             {'Foo': {'ko': [{'Float': {'float': 3.14159}}]}}]
    root = Node(ptree)
    assert root[0].ok.string_value == 'foo'
    assert root[1].ok.string_value == 'bar'
    with pytest.raises(TypeError):
        root[0].ko.string_value
    with pytest.raises(TypeError):
        root[1].ko.string_value
    with pytest.raises(TypeError):
        root[2].ko.string_value


def test_nested_lists():
    ptree = [{'Foo': {'bar': {'Bar': {'a': [
        [{'B': {'x': 0, 'y': 0}}, None],
        [{'B': {'x': 1, 'y': 1}}, None],
    ]}}}}]

    root = Node(ptree)
    foo1 = root[0]
    a = foo1.bar.a
    assert isinstance(a, List)
    assert isinstance(a[0], List)
    a00 = a[0][0]
    assert a00.node_tag == 'B'
    assert a00.x.value == a00.y.value == 0
    assert a00.parent_attribute == (('a', 0), 0)
    assert a00.parent_node[a00.parent_attribute] == a00
    a01 = a[0][1]
    assert a01.value is None
    assert a01.parent_attribute == (('a', 0), 1)
    assert a01.parent_node[a01.parent_attribute] == a01


def test_traverse():
    ptree = [{'Foo': {'bar': {'Bar': {'a': 1, 'b': 'b'}}}}]

    root = Node(ptree)
    assert tuple(root.traverse()) == (
        root[0],
        root[0].bar,
        root[0].bar['a'],
        root[0].bar.b,
    )

    ptree = [{'Foo': {'bar': {'Bar': {'a': 1, 'b': 'b'}}}},
             {'Foo': {'bar': {'Bar': {'a': 0, 'c': [
                 {'C': {'x': 0, 'y': 0}},
                 {'C': {'x': 0, 'y': 0}}
             ]}}}}]

    root = Node(ptree)
    assert tuple(root.traverse()) == (
        root[0],
        root[0].bar,
        root[0].bar['a'],
        root[0].bar.b,
        root[1],
        root[1].bar,
        root[1].bar['a'],
        root[1].bar.c[0],
        root[1].bar.c[0].x,
        root[1].bar.c[0].y,
        root[1].bar.c[1],
        root[1].bar.c[1].x,
        root[1].bar.c[1].y,
    )

    ptree = [{'Foo': {'bar': {'Bar': {'a': [
        [{'B': {'x': 0, 'y': 0}}, None],
        [{'B': {'x': 1, 'y': 1}}, None],
    ]}}}}]

    root = Node(ptree)
    assert tuple(root.traverse()) == (
        root[0],
        root[0].bar,
        root[0].bar.a[0][0],
        root[0].bar.a[0][0].x,
        root[0].bar.a[0][0].y,
        root[0].bar.a[0][1],
        root[0].bar.a[1][0],
        root[0].bar.a[1][0].x,
        root[0].bar.a[1][0].y,
        root[0].bar.a[1][1],
    )
