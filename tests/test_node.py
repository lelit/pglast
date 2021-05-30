# -*- coding: utf-8 -*-
# :Project:   pglast -- Test the node.py module
# :Created:   ven 04 ago 2017 09:31:57 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2021 Lele Gaifax
#

import pytest

from pglast import ast, Missing, Node, parse_sql
from pglast.node import Base, List


def test_bad_base_construction():
    pytest.raises(ValueError, Base, {}, parent=1.0)
    pytest.raises(ValueError, Base, [], name=1.0)
    pytest.raises(ValueError, Base, set())


def test_basic():
    root = Node(parse_sql('SELECT 1'))
    assert root.parent_node is None
    assert root.parent_attribute is None
    assert isinstance(root, List)
    assert len(root) == 1
    assert repr(root) == '[1*{RawStmt}]'
    with pytest.raises(AttributeError):
        root.not_there

    rawstmt = root[0]
    assert rawstmt != root
    assert rawstmt.node_tag == 'RawStmt'
    assert isinstance(rawstmt.ast_node, ast.RawStmt)
    assert rawstmt.parent_node is None
    assert rawstmt.parent_attribute == (None, 0)
    assert repr(rawstmt) == '{RawStmt}'
    assert rawstmt.attribute_names == ('stmt', 'stmt_location', 'stmt_len')
    with pytest.raises(ValueError):
        rawstmt[1.0]

    stmt = rawstmt.stmt
    assert stmt.node_tag == 'SelectStmt'
    assert stmt.parent_node is rawstmt
    assert stmt.parent_attribute == 'stmt'
    assert rawstmt[stmt.parent_attribute] == stmt
    assert stmt.whereClause is Missing
    assert not stmt.whereClause


def test_scalar():
    constraint = ast.Constraint()
    constraint.fk_matchtype = '\00'
    node = Node(constraint)
    assert not node.fk_matchtype
    assert node.fk_matchtype != 1


def test_traverse():
    root = Node(parse_sql('SELECT a, b, c FROM sometable'))
    assert [repr(n) for n in root.traverse()] == [
        "{RawStmt}",
        "{SelectStmt}",
        "<False>",
        "{RangeVar}",
        "<True>",
        "<20>",
        "<'sometable'>",
        "<'p'>",
        "<LimitOption.LIMIT_OPTION_DEFAULT: 0>",
        "<SetOperation.SETOP_NONE: 0>",
        "{ResTarget}",
        "<7>",
        "{ColumnRef}",
        "{String}",
        "<'a'>",
        "<7>",
        "{ResTarget}",
        "<10>",
        "{ColumnRef}",
        "{String}",
        "<'b'>",
        "<10>",
        "{ResTarget}",
        "<13>",
        "{ColumnRef}",
        "{String}",
        "<'c'>",
        "<13>",
        "<0>",
        "<0>",
    ]
