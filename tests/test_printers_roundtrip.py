# -*- coding: utf-8 -*-
# :Project:   pglast — Assert printers eat their own result
# :Created:   dom 17 mar 2019 09:24:11 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2019, 2021, 2022, 2023, 2024, 2026 Lele Gaifax
#

from pathlib import Path
from re import sub, subn
import sys

import pytest

from pglast import enums, parse_sql, split
from pglast.parser import ParseError
from pglast.stream import RawStream, IndentedStream
import pglast.printers  # noqa


this = Path(__file__)
this_dir = this.parent
tests_dir = this_dir / this.stem


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


@pytest.mark.parametrize('src,lineno,statement',
                         [(src, lineno, statement)
                          for src in sorted(tests_dir.glob('**/*.sql'))
                          for (lineno, statement) in statements(src)],
                         ids=make_id)
def test_printers_roundtrip(src, lineno, statement):
    try:
        orig_ast = parse_sql(statement)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not parse “%s”" % (src, lineno, statement))

    serialized = RawStream()(orig_ast)
    try:
        serialized_ast = parse_sql(serialized)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not reparse “%s”" % (src, lineno, serialized))

    assert orig_ast == serialized_ast, ("Statement “%s” from %s at line %d != “%s”"
                                      % (statement, src, lineno, serialized))

    indented = IndentedStream()(orig_ast)
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
def test_special_function_sql_syntax_roundtrip_preserves_funcformat(
        stream_class, statement, explicit_statement, bare_comma_call):
    explicit_call = parse_sql(explicit_statement)
    sql_syntax = parse_sql(statement)

    assert explicit_call[0].stmt.targetList[0].val.funcformat == enums.CoercionForm.COERCE_EXPLICIT_CALL
    assert sql_syntax[0].stmt.targetList[0].val.funcformat == enums.CoercionForm.COERCE_SQL_SYNTAX
    with pytest.raises(ParseError):
        parse_sql(bare_comma_call)

    serialized = stream_class()(sql_syntax)
    serialized_syntax = parse_sql(serialized)

    assert serialized_syntax[0].stmt.targetList[0].val.funcformat == enums.CoercionForm.COERCE_SQL_SYNTAX, serialized


@pytest.mark.parametrize('statement', (
    "SELECT pg_catalog.extract('year', now())",
    "SELECT pg_catalog.position('abc', 'a')",
))
def test_remove_pg_catalog_keeps_required_function_schema(statement):
    serialized = RawStream(remove_pg_catalog_from_functions=True)(parse_sql(statement))

    assert serialized == statement


@pytest.mark.parametrize('src,lineno,statement',
                         [(src, lineno, statement)
                          for src in sorted(tests_dir.glob('**/*.sql'))
                          for (lineno, statement) in statements(src)],
                         ids=make_id)
def test_stream_call_with_single_node(src, lineno, statement):
    # See https://github.com/lelit/pglast/pull/10 and https://github.com/lelit/pglast/issues/79
    try:
        parsed = parse_sql(statement)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not parse “%s”" % (src, lineno, statement))
    for rawstmt in parsed:
        stmt = rawstmt.stmt
        try:
            RawStream()(stmt)
        except Exception:
            raise AssertionError('Could not serialize single statement %r' % stmt)


pg_regressions_dir = this_dir / '..' / 'libpg_query' / 'test' / 'sql' / 'postgres_regress'

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
def test_pg_regress_corpus(filename):
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
            serialized = RawStream()(orig_ast)
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


@pytest.mark.parametrize('src,lineno,statement',
                         [(src, lineno, statement)
                          for src in sorted(tests_dir.glob('**/*.sql'))
                          for (lineno, statement) in statements(src)],
                         ids=make_id)
def test_ast_serialization_roundtrip(src, lineno, statement):
    try:
        orig_ast = parse_sql(statement)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not parse %r" % (src, lineno, statement))

    stmt = orig_ast[0].stmt
    serialized = stmt()
    clone = stmt.__class__(serialized)
    assert stmt == clone
