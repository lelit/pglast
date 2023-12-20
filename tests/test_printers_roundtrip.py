# -*- coding: utf-8 -*-
# :Project:   pglast -- Assert printers eat their own result
# :Created:   dom 17 mar 2019 09:24:11 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2019, 2021, 2022, 2023 Lele Gaifax
#

from pathlib import Path
from re import sub, subn

import pytest

from pglast import parse_sql, split
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
                         ((src, lineno, statement)
                          for src in sorted(tests_dir.glob('**/*.sql'))
                          for (lineno, statement) in statements(src)),
                         ids=make_id)
def test_printers_roundtrip(src, lineno, statement):
    try:
        orig_ast = parse_sql(statement)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not parse %r" % (src, lineno, statement))

    serialized = RawStream()(orig_ast)
    try:
        serialized_ast = parse_sql(serialized)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not reparse %r" % (src, lineno, serialized))

    assert orig_ast == serialized_ast, "%s:%s:%r != %r" % (src, lineno, statement, serialized)

    indented = IndentedStream()(orig_ast)
    try:
        indented_ast = parse_sql(indented)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not reparse %r" % (src, lineno, indented))

    assert orig_ast == indented_ast, "%s:%d:%r != %r" % (src, lineno, statement, indented)

    # Run ``pytest -s tests/`` to see the following output
    print()
    print(indented)


@pytest.mark.parametrize('src,lineno,statement',
                         ((src, lineno, statement)
                          for src in sorted(tests_dir.glob('**/*.sql'))
                          for (lineno, statement) in statements(src)),
                         ids=make_id)
def test_stream_call_with_single_node(src, lineno, statement):
    # See https://github.com/lelit/pglast/pull/10 and https://github.com/lelit/pglast/issues/79
    try:
        parsed = parse_sql(statement)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not parse %r" % (src, lineno, statement))
    for rawstmt in parsed:
        stmt = rawstmt.stmt
        try:
            RawStream()(stmt)
        except Exception:
            raise AssertionError('Could not serialize single statement %r' % stmt)


pg_regressions_dir = this_dir / '..' / 'libpg_query' / 'test' / 'sql' / 'postgres_regress'

# Following scripts contain intentional errors which are difficult to isolate, or
# are systems specific
skip_for_good_reasons = {'unicode.sql', 'collate.windows.win1252.sql'}


@pytest.mark.parametrize('filename',
                         (src.name for src in sorted(pg_regressions_dir.glob('*.sql'))
                          if src.name not in skip_for_good_reasons),
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
            raise RuntimeError("Statement “%s” from %s at line %d, could not reparse %r: %s"
                               % (trimmed_stmt, rel_src, lineno, serialized, e))

        assert orig_ast == serialized_ast, "Statement “%s” from %s at line %d != %r" % (
            trimmed_stmt, rel_src, lineno, serialized)
