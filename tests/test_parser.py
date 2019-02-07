# -*- coding: utf-8 -*-
# :Project:   pglast -- Test the parser.pyx module
# :Created:   ven 04 ago 2017 08:37:10 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019 Lele Gaifax
#

import pytest

from pglast import (
    Error,
    get_postgresql_version,
    parse_plpgsql,
    parse_sql,
    _remove_stmt_len_and_location
)


def test_basic():
    ptree = parse_sql('SELECT 1')
    assert isinstance(ptree, list)
    assert len(ptree) == 1
    rawstmt = ptree[0]
    assert isinstance(rawstmt, dict)
    assert rawstmt.keys() == {'RawStmt'}

    ptree = parse_plpgsql('CREATE FUNCTION add (a integer, b integer)'
                          ' RETURNS integer AS $$ BEGIN RETURN a + b; END; $$'
                          ' LANGUAGE plpgsql')
    assert len(ptree) == 1
    function = ptree[0]
    assert isinstance(function, dict)
    assert function.keys() == {'PLpgSQL_function'}


def test_errors():
    with pytest.raises(Error) as exc:
        parse_sql('FooBar')
    assert exc.typename == 'ParseError'
    assert exc.value.location == 1
    assert 'syntax error ' in str(exc.value)

    with pytest.raises(Error) as exc:
        parse_sql('SELECT foo FRON bar')
    assert exc.typename == 'ParseError'
    assert exc.value.location == 17
    errmsg = str(exc.value)
    assert 'syntax error at or near "bar"' in errmsg
    assert 'location 17' in errmsg

    with pytest.raises(Error) as exc:
        parse_plpgsql('CREATE FUMCTION add (a integer, b integer)'
                      ' RETURNS integer AS $$ BEGIN RETURN a + b; END; $$'
                      ' LANGUAGE plpgsql')
    assert exc.typename == 'ParseError'
    assert exc.value.location == 8
    errmsg = str(exc.value)
    assert 'syntax error at or near "FUMCTION"' in errmsg
    assert 'location 8' in errmsg


def test_unicode():
    ptree = parse_sql('SELECT 1 AS "Naïve"')
    target =ptree[0]['RawStmt']['stmt']['SelectStmt']['targetList'][0]['ResTarget']
    assert target['name'] == "Naïve"


def test_pg_version():
    pg_version = get_postgresql_version()
    assert isinstance(pg_version, tuple)
    assert len(pg_version) == 3


def test_pointless_attributes_remotion():
    sql1 = parse_sql('select a from x; select b from y')
    sql2 = parse_sql('select a from x;\n\nselect b from y')
    assert sql1 != sql2
    _remove_stmt_len_and_location(sql1)
    _remove_stmt_len_and_location(sql2)
    assert sql1 == sql2
