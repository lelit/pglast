# -*- coding: utf-8 -*-
# :Project:   pglast -- Assert printers emit beautiful code
# :Created:   dom 17 mar 2019 10:46:03 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2019, 2020, 2021 Lele Gaifax
#

from ast import literal_eval
from pathlib import Path

import pytest

from pglast import _extract_comments
from pglast.stream import IndentedStream, RawStream
import pglast.printers  # noqa


this = Path(__file__)
this_dir = this.parent
tests_dir = this_dir / this.stem


def cases(src):
    lineno = 1
    for case in src.read_text().split('\n\n'):
        yield lineno, case.strip()
        lineno += case.count('\n') + 2


def make_id(arg):
    if isinstance(arg, Path):
        return str(arg.relative_to(this_dir))
    elif isinstance(arg, int):
        return str(arg)


# Prettification cases: each case may be composed by either two or three parts,
# respectively the original statement, the expected outcome and an optional options
# dictionary. The original and the expected statements are separated by a standalone "=",
# while the options dictionary is introduced by a standalone ":". Thus something like
# this:
#
#   RAW_STATEMENT
#   =
#   PRETTIFIED_STATEMENT
#
# or this:
#
#   RAW_STATEMENT
#   =
#   PRETTIFIED_STATEMENT
#   :
#   INDENTEDSTREAM_OPTIONS_DICTIONARY
#
# The prettified statement may contain standalone "\n\" lines, that are replaced with single
# newlines, to allow "empty lines"; in other words, the following expected statement
#
#   SELECT foo
#
#   INTERSECT
#
#   SELECT bar
#
# must be written as
#
#   SELECT foo
#   \n\
#   INTERSECT
#   \n\
#   SELECT bar
#
# When it ends with a "\", it is replaced with a final newline.

@pytest.mark.parametrize('src,lineno,case',
                         ((src, lineno, case)
                          for src in sorted(tests_dir.glob('**/*.sql'))
                          for (lineno, case) in cases(src)),
                         ids=make_id)
def test_prettification(src, lineno, case):
    parts = case.split('\n=\n')
    original = parts[0].strip()
    parts = parts[1].split('\n:\n')
    expected = parts[0].strip().replace('\\n\\\n', '\n').replace('\\s', ' ')
    if expected.endswith('\\'):
        expected = expected[:-1] + '\n'
    if len(parts) == 2:
        options = literal_eval(parts[1])
    else:
        options = {}
    if options.pop('preserve_comments', False):
        options['comments'] = _extract_comments(original)
    raw = options.pop('raw_stream', False)
    prettified = (RawStream if raw else IndentedStream)(**options)(original)
    assert expected == prettified, "%s:%d:%r != %r" % (src, lineno, expected, prettified)
