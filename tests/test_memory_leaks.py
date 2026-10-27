# -*- coding: utf-8 -*-
# :Project:   pglast — Memory leaks tests
# :Created:   mar 21 ott 2026 18:40:00 CEST
# :Author:    r3gardless <pidaoh@g.skku.edu>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2026 Lele Gaifax
#

import ctypes
import ctypes.util
import gc

import pytest

from pglast import parser


tracemalloc = pytest.importorskip("tracemalloc")


# tracemalloc sees only the memory allocated through Python: what libpg_query mallocs is
# invisible to it, so on glibc check the C heap with mallinfo2() as well

def _get_c_heap_usage():
    try:
        libc = ctypes.CDLL(ctypes.util.find_library('c'))
        mallinfo2 = libc.mallinfo2
    except (AttributeError, OSError, TypeError):
        return None

    class MallInfo2(ctypes.Structure):
        _fields_ = [(name, ctypes.c_size_t)
                    for name in ('arena', 'ordblks', 'smblks', 'hblks', 'hblkhd', 'usmblks',
                                 'fsmblks', 'uordblks', 'fordblks', 'keepcost')]

    mallinfo2.restype = MallInfo2
    return lambda: mallinfo2().uordblks


c_heap_usage = _get_c_heap_usage()

PROTOBUF = parser.parse_sql_protobuf('SELECT a FROM t WHERE b = 1')
PLPGSQL = 'CREATE FUNCTION f() RETURNS int LANGUAGE plpgsql AS $$ BEGIN RETURN 1%s END $$'

CASES = {
    'parse_sql': (parser.parse_sql, 'SELECT a FROM t WHERE b = 1'),
    'parse_sql-error': (parser.parse_sql, 'SELEC 1'),
    'parse_sql_json': (parser.parse_sql_json, 'SELECT a FROM t WHERE b = 1'),
    'parse_sql_json-error': (parser.parse_sql_json, 'SELEC 1'),
    'parse_sql_protobuf': (parser.parse_sql_protobuf, 'SELECT a FROM t WHERE b = 1'),
    'parse_sql_protobuf-error': (parser.parse_sql_protobuf, 'SELEC 1'),
    'parse_plpgsql_json': (parser.parse_plpgsql_json, PLPGSQL % ';'),
    'parse_plpgsql_json-error': (parser.parse_plpgsql_json, PLPGSQL % ''),
    'fingerprint': (parser.fingerprint, 'SELECT a FROM t WHERE b = 1'),
    'fingerprint-error': (parser.fingerprint, 'SELEC 1'),
    'normalize': (parser.normalize, 'SELECT a FROM t WHERE b = 1'),
    'normalize-error': (parser.normalize, 'SELEC 1'),
    'normalize-utility': (lambda s: parser.normalize(s, utility_only=True),
                          "CREATE ROLE r PASSWORD 'secret'"),
    'normalize-utility-error': (lambda s: parser.normalize(s, utility_only=True), 'SELEC 1'),
    'split': (parser.split, 'SELECT 1; SELECT 2'),
    'split-error': (parser.split, 'SELECT 1; SELEC 2'),
    'split-scanner': (lambda s: parser.split(s, with_parser=False), 'SELECT 1; SELECT 2'),
    'split-scanner-error': (lambda s: parser.split(s, with_parser=False), "SELECT 'x"),
    'comments': (parser.comments, 'SELECT 1 -- one'),
    'comments-error': (parser.comments, "SELECT 'x"),
    'deparse_protobuf': (parser.deparse_protobuf, PROTOBUF),
    'scan': (parser.scan, 'SELECT a FROM t'),
    'scan-error': (parser.scan, "SELECT 'x"),
}


def call(function, argument, times):
    for _ in range(times):
        try:
            function(argument)
        except parser.ParseError:
            pass


@pytest.mark.parametrize('function,argument', CASES.values(), ids=CASES.keys())
def test_no_python_leaks(function, argument):
    call(function, argument, 100)

    tracemalloc.start()
    snapshot1 = tracemalloc.take_snapshot().filter_traces((
        tracemalloc.Filter(True, __file__),))

    call(function, argument, 1000)
    gc.collect()

    snapshot2 = tracemalloc.take_snapshot().filter_traces((
        tracemalloc.Filter(True, __file__),))
    tracemalloc.stop()

    for stat in snapshot2.compare_to(snapshot1, 'lineno')[:10]:
        assert stat.count_diff <= 5


KNOWN_C_LEAKS = {
    'comments-error': ("libpg_query's pg_query_free_deparse_comments_result() does not free"
                       " the error, https://github.com/pganalyze/libpg_query/issues/390"),
}


def c_leaks_cases():
    for name, case in CASES.items():
        if name in KNOWN_C_LEAKS:
            yield pytest.param(*case, id=name,
                               marks=pytest.mark.xfail(reason=KNOWN_C_LEAKS[name]))
        else:
            yield pytest.param(*case, id=name)


@pytest.mark.skipif(c_heap_usage is None, reason="mallinfo2() not available")
@pytest.mark.parametrize('function,argument', list(c_leaks_cases()))
def test_no_c_leaks(function, argument):
    times = 10000

    call(function, argument, 1000)
    gc.collect()
    before = c_heap_usage()

    call(function, argument, times)
    gc.collect()
    after = c_heap_usage()

    # Leaks fixed so far were 32 bytes or more per call
    assert after - before < times
