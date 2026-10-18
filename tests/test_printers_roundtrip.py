# -*- coding: utf-8 -*-
# :Project:   pglast — Assert printers eat their own result
# :Created:   dom 17 mar 2019 09:24:11 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2019, 2021, 2022, 2023, 2024, 2026 Lele Gaifax
#

import codecs
from os import environ
from pathlib import Path
from re import sub, subn
from shutil import which
from subprocess import check_output
import sys

from pycparser import c_ast, c_parser
import pytest

from pglast import enums, parse_sql, split
from pglast.parser import ParseError
from pglast.stream import RawStream, IndentedStream
import pglast.printers  # noqa


this = Path(__file__)
this_dir = this.parent
tests_dir = this_dir / this.stem
libpg_query_test_dir = this_dir / '..' / 'libpg_query' / 'test'


def statements(src):
    lineno = 1
    for statement in src.read_text().split('\n\n'):
        yield lineno, statement.strip()
        lineno += statement.count('\n') + 2


def make_id(arg):
    if isinstance(arg, Path):
        return str(arg.relative_to(this_dir))
    elif isinstance(arg, int):
        return str(arg)


deparse_tests_file = libpg_query_test_dir / 'deparse_tests.c'

# How the deparser corpus below is labelled in test ids, like the corpora are by ``make_id()``.
deparse_tests_name = 'libpg_query/test/deparse_tests.c'


def c_string_literal(token):
    """Decode a C string literal, as pycparser hands it over, quotes included.

    The escapes are the compiler's, while the raw non-ASCII bytes must be left alone for the final
    UTF-8 decoding: ``bytes.decode()`` with ``unicode_escape`` would needlessly mangle them.
    """
    assert token.startswith('"') and token.endswith('"'), token
    decoded, _ = codecs.escape_decode(token[1:-1].encode('utf-8'))
    return decoded.decode('utf-8')


def read_deparse_tests():
    """Return the ``(lineno, statement)`` pairs of libpg_query's ``test/deparse_tests.c``."""

    # Handle the case when we have no checked out libpg_query tree
    if not deparse_tests_file.exists():
        return []

    cpp = environ.get('CPP') or which('clang') or 'cpp'
    tree = c_parser.CParser().parse(check_output([cpp, '-E', '-P', str(deparse_tests_file)],
                                                text=True))
    array = next(d for d in tree.ext if isinstance(d, c_ast.Decl) and d.name == 'tests')
    assert isinstance(array.type, c_ast.ArrayDecl), array.type.type

    return [(item.coord.line, c_string_literal(item.value))
            for item in array.init.exprs
            # skip ending NULL
            if isinstance(item, c_ast.Constant) and item.type == 'string']


deparse_tests_statements = read_deparse_tests()

def corpus_statements():
    """
    Yield the ``(origin, lineno, statement)`` triples of pglast's corpora and the deparser one.
    """
    for src in sorted(tests_dir.glob('**/*.sql')):
        for lineno, statement in statements(src):
            yield src, lineno, statement
    for lineno, statement in deparse_tests_statements:
        yield deparse_tests_name, lineno, statement


@pytest.mark.parametrize('src,lineno,statement', corpus_statements(), ids=make_id)
@pytest.mark.parametrize('special_functions', (False, True))
def test_printers_roundtrip(src, lineno, statement, special_functions):
    try:
        orig_ast = parse_sql(statement)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not parse “%s”" % (src, lineno, statement))

    serialized = RawStream(special_functions=special_functions)(orig_ast)
    try:
        serialized_ast = parse_sql(serialized)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not reparse “%s”" % (src, lineno, serialized))

    assert orig_ast == serialized_ast, ("Statement “%s” from %s at line %d != “%s”"
                                      % (statement, src, lineno, serialized))

    indented = IndentedStream(special_functions=special_functions)(orig_ast)
    try:
        indented_ast = parse_sql(indented)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not reparse “%s”" % (src, lineno, indented))

    assert orig_ast == indented_ast, ("Statement “%s” from %s at line %d != “%s”"
                                      % (statement, src, lineno, indented))

    # Run ``pytest -s tests/`` to see the following output
    print()
    print(indented)


@pytest.mark.parametrize('statement,explicit_statement,bare_comma_call', (
    (
        "SELECT position('a' IN 'abc')",
        "SELECT pg_catalog.position('abc', 'a')",
        "SELECT position('abc', 'a')",
    ),
    (
        "SELECT extract(year FROM now())",
        "SELECT pg_catalog.extract('year', now())",
        "SELECT extract('year', now())",
    ),
))
@pytest.mark.parametrize('stream_class', (RawStream, IndentedStream))
@pytest.mark.parametrize('special_functions', (False, True))
def test_special_function_sql_syntax_roundtrip_preserves_funcformat(
        stream_class, special_functions, statement, explicit_statement, bare_comma_call):
    explicit_call = parse_sql(explicit_statement)
    sql_syntax = parse_sql(statement)

    assert explicit_call[0].stmt.targetList[0].val.funcformat == enums.CoercionForm.COERCE_EXPLICIT_CALL
    assert sql_syntax[0].stmt.targetList[0].val.funcformat == enums.CoercionForm.COERCE_SQL_SYNTAX
    with pytest.raises(ParseError):
        parse_sql(bare_comma_call)

    # AST equality ignores funcformat, so check it explicitly for both forms.
    for parsed, expected_format in (
            (explicit_call, enums.CoercionForm.COERCE_EXPLICIT_CALL),
            (sql_syntax, enums.CoercionForm.COERCE_SQL_SYNTAX)):
        serialized = stream_class(special_functions=special_functions)(parsed)
        serialized_syntax = parse_sql(serialized)
        assert serialized_syntax == parsed, serialized
        assert serialized_syntax[0].stmt.targetList[0].val.funcformat == expected_format, serialized


@pytest.mark.parametrize('stream_class', (RawStream, IndentedStream))
@pytest.mark.parametrize('special_functions', (False, True))
@pytest.mark.parametrize('schema', ('', 'pg_catalog.', 'custom_schema.'))
@pytest.mark.parametrize('cast_arguments', (False, True))
@pytest.mark.parametrize('name,arguments', (
    ('extract', ("'epoch'", 'now()')),
    ('position', ('needle', 'haystack')),
    ('substring', ('value', '2', '4')),
    ('overlay', ('value', "'replacement'", '2', '4')),
    ('overlay', ('value', "'replacement'", '2')),
    ('trim', ('value',)),
    ('normalize', ('value', "'NFC'")),
    ('is_normalized', ('value', "'NFC'")),
))
@pytest.mark.parametrize('call', (
    '({args})',
    '(DISTINCT {args})',
    '({args} ORDER BY sort_key)',
    '({args}) WITHIN GROUP (ORDER BY sort_key)',
    '({args}) FILTER (WHERE enabled)',
    '({args}) FILTER (WHERE enabled) OVER (PARTITION BY group_key ORDER BY sort_key)',
    '({variadic_args})',
    '(*)',
))
def test_keyword_function_roundtrip(
        stream_class, special_functions, schema, cast_arguments, name, arguments, call):
    if cast_arguments:
        arguments = tuple(f'CAST({argument} AS text)' for argument in arguments)
    call = call.format(args=', '.join(arguments),
                       variadic_args=', '.join((*arguments[:-1], 'VARIADIC ' + arguments[-1])))
    statement = f'SELECT {schema}"{name}"{call} FROM t'
    parsed = parse_sql(statement)
    serialized = stream_class(special_functions=special_functions)(parsed)
    assert parse_sql(serialized) == parsed, serialized


@pytest.mark.parametrize('statement', (
    "SELECT pg_catalog.extract('year', now())",
    "SELECT pg_catalog.position('abc', 'a')",
))
def test_remove_pg_catalog_keeps_required_function_schema(statement):
    serialized = RawStream(remove_pg_catalog_from_functions=True)(parse_sql(statement))

    assert serialized == statement


@pytest.mark.parametrize('src,lineno,statement', corpus_statements(), ids=make_id)
def test_stream_call_with_single_node(src, lineno, statement):
    # See https://github.com/lelit/pglast/pull/10 and https://github.com/lelit/pglast/issues/79
    try:
        parsed = parse_sql(statement)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not parse “%s”" % (src, lineno, statement))
    for rawstmt in parsed:
        stmt = rawstmt.stmt
        assert stmt is not None
        try:
            RawStream()(stmt)
        except Exception:
            raise AssertionError('Could not serialize single statement %r' % stmt)


pg_regressions_dir = libpg_query_test_dir / 'sql' / 'postgres_regress'

# Following scripts contain intentional errors which are difficult to isolate, or
# are systems specific
skip_for_good_reasons = {
    'collate.icu.utf8.sql',
    'collate.windows.win1252.sql',
    'unicode.sql',
}


@pytest.mark.parametrize('filename',
                         [src.name for src in sorted(pg_regressions_dir.glob('*.sql'))
                          if src.name not in skip_for_good_reasons],
                         ids=make_id)
@pytest.mark.parametrize('special_functions', (False, True))
def test_pg_regress_corpus(filename, special_functions):
    # we do this dance to minimize the length of the test name
    src = pg_regressions_dir / filename
    source = src.read_text()
    try:
        slices = split(source, with_parser=False, only_slices=True)
    except Exception:
        return

    for slice in slices:
        stmt = source[slice]
        lineno = source[:slice.start].count('\n') + 1

        # Remove comments and replace \n to make it easier cut&pasting the stmt
        # in `pgpp -t`

        trimmed_stmt = stmt.strip()
        while trimmed_stmt.startswith('--'):
            trimmed_stmt = sub(r'--.*\n', '', trimmed_stmt)
            lineno += 1
        trimmed_stmt = subn(r'[\n\t]+', ' ', trimmed_stmt)[0].strip()

        rel_src = src.relative_to(this_dir / '..')
        try:
            orig_ast = parse_sql(stmt)
        except ParseError:
            continue
        except Exception as e:
            raise RuntimeError("Statement “%s” from %s at line %d, could not parse: %s"
                               % (trimmed_stmt, rel_src, lineno, e))

        try:
            serialized = RawStream(special_functions=special_functions)(orig_ast)
        except NotImplementedError as e:
            raise NotImplementedError("Statement “%s” from %s at line %d, could not reprint: %s"
                                      % (trimmed_stmt, rel_src, lineno, e))
        except Exception as e:
            raise RuntimeError("Statement “%s” from %s at line %d, could not reprint: %s"
                               % (trimmed_stmt, rel_src, lineno, e))

        try:
            serialized_ast = parse_sql(serialized)
        except Exception as e:
            raise RuntimeError("Statement “%s” from %s at line %d, could not reparse “%s”: %s"
                               % (trimmed_stmt, rel_src, lineno, serialized, e))

        assert orig_ast == serialized_ast, "Statement “%s” from %s at line %d != “%s”" % (
            trimmed_stmt, rel_src, lineno, serialized)


@pytest.mark.parametrize('src,lineno,statement', corpus_statements(), ids=make_id)
def test_ast_serialization_roundtrip(src, lineno, statement):
    try:
        orig_ast = parse_sql(statement)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not parse %r" % (src, lineno, statement))

    stmt = orig_ast[0].stmt
    assert stmt is not None
    serialized = stmt()
    clone = stmt.__class__(serialized)
    assert stmt == clone
