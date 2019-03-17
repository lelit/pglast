# -*- coding: utf-8 -*-
# :Project:   pglast -- Assert printers eat their own result
# :Created:   dom 17 mar 2019 09:24:11 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2019 Lele Gaifax
#

from pathlib import Path

import pytest

from pglast import Node, _remove_stmt_len_and_location
from pglast.parser import parse_sql
from pglast.printer import RawStream, IndentedStream
import pglast.printers


# Make pyflakes happy
pglast.printers


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

    _remove_stmt_len_and_location(orig_ast)

    serialized = RawStream()(Node(orig_ast))
    try:
        serialized_ast = parse_sql(serialized)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not reparse %r" % (src, lineno, serialized))
    _remove_stmt_len_and_location(serialized_ast)
    assert orig_ast == serialized_ast, "%s:%s:%r != %r" % (src, lineno, statement, serialized)

    indented = IndentedStream()(Node(orig_ast))
    try:
        indented_ast = parse_sql(indented)
    except:  # noqa
        raise RuntimeError("%s:%d:Could not reparse %r" % (src, lineno, indented))
    _remove_stmt_len_and_location(indented_ast)
    assert orig_ast == indented_ast, "%s:%d:%r != %r" % (src, lineno, statement, indented)

    # Run ``pytest -s tests/`` to see the following output
    print()
    print(indented)


def test_stream_call_with_single_node():
    # See https://github.com/lelit/pglast/pull/10
    parsed = parse_sql('select a from x; select b from y')
    node = Node(parsed[0])
    result = RawStream()(node)
    assert result == 'SELECT a FROM x'
    node = Node(parsed[1])
    result = RawStream()(node)
    assert result == 'SELECT b FROM y'
