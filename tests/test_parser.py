# -*- coding: utf-8 -*-
# :Project:   pglast -- Test the parser.pyx module
# :Created:   ven 04 ago 2017 08:37:10 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2023 Lele Gaifax
#

import json

import pytest

from pglast import Error, ast, parse_plpgsql, parse_sql
from pglast.parser import Displacements, ParseError, deparse_protobuf, fingerprint
from pglast.parser import get_postgresql_version, parse_sql_json, parse_sql_protobuf
from pglast.parser import scan, split


def test_parse_sql():
    assert parse_sql('') == ()
    assert parse_sql('-- nothing') == ()
    with pytest.raises(ParseError):
        parse_sql('foo')

    ptree = parse_sql('SELECT 1')
    assert isinstance(ptree, tuple)
    assert len(ptree) == 1
    rawstmt = ptree[0]
    assert isinstance(rawstmt, ast.RawStmt)


def test_parse_plpgsql():
    ptree = parse_plpgsql('CREATE FUNCTION add (a integer, b integer)'
                          ' RETURNS integer AS $$ BEGIN RETURN a + b; END; $$'
                          ' LANGUAGE plpgsql')
    assert len(ptree) == 1
    function = ptree[0]
    assert isinstance(function, dict)
    assert function.keys() == {'PLpgSQL_function'}

    # See https://github.com/pganalyze/libpg_query/issues/122
    ptree = parse_plpgsql("""\
CREATE OR REPLACE FUNCTION test_parse (
    p_time_start timestamptz,
    p_time_end timestamptz,
    p_time_interval interval default NULL
) RETURNS TABLE (
    ts timestamptz,
    arbitrary_return bigint
) AS $$
BEGIN
    IF p_time_interval IS NULL
        THEN p_time_interval := INTERVAL '1 hour';
    END IF;
    RETURN QUERY
    SELECT p_time_start + p_time_interval, 1234::bigint;
END; $$ LANGUAGE plpgsql;""")
    function = ptree[0]
    assert isinstance(function, dict)
    assert function.keys() == {'PLpgSQL_function'}


def test_fingerprint():
    sql1 = "SELECT a as b, c as d FROM atable AS btable WHERE a = 1 AND b in (1, 2)"
    sql2 = "SELECT a, c FROM atable WHERE a = 2 AND b IN (2, 3, 4) "
    assert fingerprint(sql1) == fingerprint(sql2)


def test_errors():
    with pytest.raises(Error) as exc:
        parse_sql('FooBar')
    assert exc.typename == 'ParseError'
    errmsg, index = exc.value.args
    assert errmsg == 'syntax error at or near "FooBar"'
    assert index == 0

    with pytest.raises(Error) as exc:
        parse_sql('SELECT foo FRON bar')
    assert exc.typename == 'ParseError'
    errmsg, index = exc.value.args
    assert errmsg == 'syntax error at or near "bar"'
    assert index == 16
    assert str(exc.value) == f'{errmsg}, at index {index}'

    with pytest.raises(Error) as exc:
        parse_plpgsql('CREATE FUMCTION add (a integer, b integer)'
                      ' RETURNS integer AS $$ BEGIN RETURN a + b; END; $$'
                      ' LANGUAGE plpgsql')
    assert exc.typename == 'ParseError'
    errmsg, index = exc.value.args
    assert errmsg == 'syntax error at or near "FUMCTION"'
    assert index == 7

    with pytest.raises(Error) as exc:
        fingerprint('SELECT foo FRON bar')
    assert exc.typename == 'ParseError'
    errmsg, index = exc.value.args
    assert errmsg == 'syntax error at or near "bar"'
    assert index == 16


def test_unicode():
    ptree = parse_sql('SELECT 1 AS "Naïve"')
    target = ptree[0].stmt.targetList[0]
    assert target.name == "Naïve"


def test_locations_fixup():
    sql = 'SELECT 1 AS "Naïve" /* there is an  "ı" with a  \u0308 above */ FROM somewhere'

    sql3 = ';'.join([sql]*3)
    ptree = parse_sql(sql3)
    assert len(ptree) == 3

    raw = ptree[0]
    assert raw.stmt_location == 0
    assert raw.stmt_len == len(sql)
    fromc = raw.stmt.fromClause[0]
    assert sql3[fromc.location:].startswith('somewhere')

    raw = ptree[1]
    assert raw.stmt_location == len(sql)+1
    assert raw.stmt_len == len(sql)
    fromc = raw.stmt.fromClause[0]
    assert sql3[fromc.location:].startswith('somewhere')

    raw = ptree[2]
    assert raw.stmt_location == len(sql)*2+2
    # For the last stmt, the stmt_len is 0...
    assert raw.stmt_len == 0
    fromc = raw.stmt.fromClause[0]
    assert sql3[fromc.location:].startswith('somewhere')


def test_pg_version():
    pg_version = get_postgresql_version()
    assert isinstance(pg_version, tuple)
    assert len(pg_version) == 2


def test_clone():
    from pglast import ast
    stmts = parse_sql('SELECT 1')
    stmt = stmts[0].stmt
    clone = ast.SelectStmt(stmt())
    assert clone is not stmt
    assert clone == stmt
    assert repr(clone) == repr(stmt)
    assert clone() == stmt()


def test_split():
    sql = 'select 1; select 2;    select "€€€€ ·";   select 4'
    expected = ('select 1', 'select 2', 'select "€€€€ ·"', 'select 4')
    assert split(sql) == expected
    assert tuple(sql[s] for s in split(sql, only_slices=True)) == expected


def test_scan():
    sql = 'select /* something here */ 1'
    result = scan(sql)
    assert result == [( 0,  5, 'SELECT',    'RESERVED_KEYWORD'),  # noqa E201
                      ( 7, 26, 'C_COMMENT', 'NO_KEYWORD'),        # noqa E201
                      (28, 28, 'ICONST',    'NO_KEYWORD')]
    assert sql[result[1].start:result[1].end+1] == '/* something here */'

    sql = 'select 0.01 as "€"   -- one €-cent'
    assert [sql[t.start:t.end+1] for t in scan(sql)] == [
        'select', '0.01', 'as', '"€"', '-- one €-cent']

    # Combining character
    sql = 'SELECT 1 AS "\u0101\u0301" -- etc'
    assert [sql[t.start:t.end+1] for t in scan(sql)] == [
        'SELECT', '1', 'AS', '"ā́"', '-- etc']

    # Invalid input, see https://github.com/pganalyze/libpg_query/issues/108
    sql = 'SELECT \\s 1'
    result = scan(sql)
    assert result == [( 0,  5, 'SELECT',   'RESERVED_KEYWORD'),  # noqa E201
                      ( 7,  7, 'ASCII_92', 'NO_KEYWORD'),        # noqa E201
                      ( 8,  8, 'IDENT',    'NO_KEYWORD'),        # noqa E201
                      (10, 10, 'ICONST',   'NO_KEYWORD')]
    assert sql[result[1].start] == '\\'


def test_deparse_protobuf():
    assert deparse_protobuf(parse_sql_protobuf('select 1')) == 'SELECT 1'


def test_parse_sql_json():
    # See issue #128

    def _find(tree, subtree_key):
        """ Recursive searcher. """
        for key, val in tree.items():
            if key == subtree_key:
                yield val
            elif type(val) == list:
                for i in val:
                    yield from _find(i, subtree_key)
            elif type(val) == dict:
                yield from _find(val, subtree_key)

    def used_tables(sql_query):
        disp = Displacements(sql_query)
        json_str = parse_sql_json(sql_query)
        parse_tree = json.loads(json_str)

        deps = set()
        for subtree in _find(parse_tree, 'RangeVar'):
            # Instead of using `schemaname` and `relname`, I use the location to
            # extract the dependency in a case-sensitive manner.
            tot_length = len(subtree['schemaname']) + len(subtree['relname']) + 1
            start_idx = disp(subtree['location'])
            dep = sql_query[start_idx:start_idx + tot_length]
            deps.add(dep)

        return deps

    # Note that the last word of first line is not "Satis" but "Satış" with a
    # dotless i and an s with cedilla.
    turkish_chars = '''
    select t1.Sales Satış
    from Schema.Table t1
    join Schema2.Table2 t2
    on t1.col = t2.col
    '''

    assert used_tables(turkish_chars) == {'Schema.Table', 'Schema2.Table2'}
