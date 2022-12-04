# -*- coding: utf-8 -*-
# :Project:   pglast -- Test the __main__.py module
# :Created:   lun 07 ago 2017 12:50:37 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2022 Lele Gaifax
#

from contextlib import _RedirectStream, redirect_stdout
from io import StringIO
from os import unlink
from tempfile import NamedTemporaryFile

import pytest

from pglast.__main__ import main


class redirect_stdin(_RedirectStream):
    _stream = "stdin"


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
                    'syntax error at or near "sometable", at index 20'

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

    output = NamedTemporaryFile(delete=False)
    try:
        main(['-S', "select 1", '-', output.name])
        with open(output.name) as f:
            assert f.read() == "SELECT 1\n"
    finally:
        unlink(output.name)

    with StringIO("Select 1") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--parse-tree'])
            assert "'val': {'@': 'Integer', 'ival': 1}" in output.getvalue()

    with StringIO("""\
CREATE FUNCTION add (a integer, b integer) RETURNS integer AS $$
BEGIN RETURN a + b; END;
$$ LANGUAGE plpgsql""") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--plpgsql', '--parse-tree'])
            assert '"PLpgSQL_function":' in output.getvalue()

    with StringIO("Select 1") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main([])
            assert output.getvalue() == "SELECT 1\n"

    with StringIO("Select 1;") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main([])
            assert output.getvalue() == "SELECT 1\n"

    with StringIO("Select 1; Select 2") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main([])
            assert output.getvalue() == "SELECT 1;\n\nSELECT 2\n"

    with StringIO("Select 1; Select 2") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--semicolon-after-last-statement'])
            assert output.getvalue() == "SELECT 1;\n\nSELECT 2;\n"

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

    with StringIO("Select /* one */ 1") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--preserve-comments'])
            assert output.getvalue() == "SELECT /* one */ 1\n"

    with StringIO("""\
select collation for ('abc'),
       normalize('abc', nfc),
       overlay('Txxxxas' placing 'hom' FROM 2 for 4),
       position('bc' in 'abcd'),
       trim(both '  abc  '),
       trim(both '*' from '***abc***'),
       trim(leading '*' from '***abc***'),
       trim(trailing '*' from '***abc***'),
       xmlexists('//town[text() = ''Toronto'']'
         passing '<towns><town>Toronto</town><town>Ottawa</town></towns>');
""") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--special-functions', '--compact-lists-margin', '100'])
            assert output.getvalue() == """\
SELECT COLLATION FOR ('abc')
     , normalize('abc', NFC)
     , overlay('Txxxxas' PLACING 'hom' FROM 2 FOR 4)
     , position('bc' IN 'abcd')
     , trim(BOTH FROM '  abc  ')
     , trim(BOTH '*' FROM '***abc***')
     , trim(LEADING '*' FROM '***abc***')
     , trim(TRAILING '*' FROM '***abc***')
     , xmlexists('//town[text() = ''Toronto'']'\
 PASSING BY REF '<towns><town>Toronto</town><town>Ottawa</town></towns>')
"""

    with StringIO("select extract(hour from t1.modtime), count(*) from t1") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--special-functions', '--compact-lists-margin', '120'])
            assert output.getvalue() == ("SELECT EXTRACT(HOUR FROM t1.modtime), count(*)\n"
                                         "FROM t1\n")

    with StringIO("select extract(hour from t1.modtime), count(*) from t1") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--special-functions', '--compact-lists-margin', '40'])
            assert output.getvalue() == ("SELECT EXTRACT(HOUR FROM t1.modtime)\n"
                                         "     , count(*)\n"
                                         "FROM t1\n")

    with StringIO("select substring('123' from 1 for 2)") as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--special-functions', '--compact-lists-margin', '40'])
            assert output.getvalue() == "SELECT substring('123' FROM 1 FOR 2)\n"

    in_stmt = """\
select substring('123',2,3),
       regexp_split_to_array('x,x,x', ','),
       btrim('xxx'), trim('xxx'),
       POSITION('hour' in trim(substring('xyz hour ',1,6)))
"""

    with StringIO(in_stmt) as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--compact-lists-margin', '100'])
            assert output.getvalue() == """\
SELECT substring('123', 2, 3)
     , regexp_split_to_array('x,x,x', ',')
     , btrim('xxx')
     , pg_catalog.btrim('xxx')
     , pg_catalog.position(pg_catalog.btrim(substring('xyz hour ', 1, 6)), 'hour')
"""

    with StringIO(in_stmt) as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--remove-pg_catalog-from-functions', '--compact-lists-margin', '100'])
            assert output.getvalue() == """\
SELECT substring('123', 2, 3)
     , regexp_split_to_array('x,x,x', ',')
     , btrim('xxx')
     , btrim('xxx')
     , pg_catalog.position(btrim(substring('xyz hour ', 1, 6)), 'hour')
"""

    with StringIO('SELECT NULLIF(1, 0)') as input:
        with UnclosableStream() as output:
            with redirect_stdin(input), redirect_stdout(output):
                main(['--remove-pg_catalog-from-functions'])
            assert output.getvalue() == "SELECT NULLIF(1, 0)\n"

