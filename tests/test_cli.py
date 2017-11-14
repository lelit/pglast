# -*- coding: utf-8 -*-
# :Project:   pg_query -- Test the __main__.py module
# :Created:   lun 07 ago 2017 12:50:37 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

try:
    from contextlib import _RedirectStream, redirect_stdout
except ImportError:
    # Python 3.4
    from contextlib import redirect_stdout
    import sys

    class redirect_stdin:
        def __init__(self, new_target):
            self._new_target = new_target
            # We use a list of old targets to make this CM re-entrant
            self._old_targets = []

        def __enter__(self):
            self._old_targets.append(sys.stdin)
            sys.stdin = self._new_target
            return self._new_target

        def __exit__(self, exctype, excinst, exctb):
            sys.stdin = self._old_targets.pop()
else:
    class redirect_stdin(_RedirectStream):
        _stream = "stdin"

from io import StringIO

import pytest

from pg_query.__main__ import main


class UnclosableStream(StringIO):
    def close(self):
        pass


def test_cli_workhorse():
    with StringIO() as output:
        with redirect_stdout(output):
            with pytest.raises(SystemExit) as status:
                main(['-h'])
            assert status.value.args[0] == 0
        assert 'usage:' in output.getvalue()

    with StringIO("Select foo,bar Fron sometable") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                with pytest.raises(SystemExit) as status:
                    main([])
                assert str(status.value.args[0]) == \
                    'syntax error at or near "sometable", at location 21'

    with StringIO("Select foo,bar From sometable Where foo<>0") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main([])
            assert output.getvalue() == """\
SELECT foo
     , bar
FROM sometable
WHERE foo <> 0
"""

    with StringIO("Select 1") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--parse-tree'])
            assert '"ival": 1' in output.getvalue()

    with StringIO("Select 1") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--parse-tree', '--no-location'])
            assert '"location":' not in output.getvalue()

    with StringIO("Select 'abcdef'") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--split-string-literals', '0'])
            assert output.getvalue() == "SELECT 'abcdef'\n"

    with StringIO("Select 'abcdef'") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--split-string-literals', '3'])
            assert output.getvalue() == """\
SELECT 'abc'
       'def'
"""
