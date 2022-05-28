# -*- coding: utf-8 -*-
# :Project:   pglast -- Tests on the stream.py module
# :Created:   sab 05 ago 2017 10:31:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2022 Lele Gaifax
#

import pytest

from pglast import ast, parse_sql
from pglast.printers import NODE_PRINTERS, PrinterAlreadyPresentError, SPECIAL_FUNCTIONS
from pglast.printers import node_printer, special_function
from pglast.stream import IndentedStream, OutputStream, RawStream


def test_output_stream():
    output = OutputStream()
    output.writes('SELECT *')
    output.writes(' FROM')
    output.writes('table ')
    output.writes('WHERE')
    output.write('id = 1')

    assert output.getvalue() == 'SELECT * FROM table WHERE id = 1'


def test_raw_stream_with_sql():
    raw_stmt_printer = NODE_PRINTERS.pop(ast.RawStmt, None)
    try:
        @node_printer(ast.RawStmt)
        def raw_stmt(node, output):
            output.write('Yeah')

        output = RawStream()
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah; Yeah'
    finally:
        if raw_stmt_printer is not None:
            NODE_PRINTERS[ast.RawStmt] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop(ast.RawStmt, None)


def test_raw_stream():
    raw_stmt_printer = NODE_PRINTERS.pop(ast.RawStmt, None)
    try:
        @node_printer(ast.RawStmt)
        def raw_stmt(node, output):
            output.write('Yeah')

        root = parse_sql('SELECT 1')
        output = RawStream()
        result = output(root)
        assert result == 'Yeah'
    finally:
        if raw_stmt_printer is not None:
            NODE_PRINTERS[ast.RawStmt] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop(ast.RawStmt, None)


def test_raw_stream_invalid_call():
    with pytest.raises(ValueError):
        RawStream()(1)


def test_indented_stream_with_sql():
    raw_stmt_printer = NODE_PRINTERS.pop(ast.RawStmt, None)
    try:
        @node_printer(ast.RawStmt)
        def raw_stmt(node, output):
            output.write('Yeah')

        output = IndentedStream()
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah;\n\nYeah'

        output = IndentedStream(separate_statements=False)
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah;\nYeah'
    finally:
        if raw_stmt_printer is not None:
            NODE_PRINTERS[ast.RawStmt] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop(ast.RawStmt, None)


def test_separate_statements():
    """Separate statements by ``separate_statements`` (int) newlines."""
    raw_stmt_printer = NODE_PRINTERS.pop(ast.RawStmt, None)
    try:
        @node_printer(ast.RawStmt)
        def raw_stmt(node, output):
            output.write('Yeah')

        output = IndentedStream(separate_statements=2)
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah;\n\n\nYeah'
    finally:
        if raw_stmt_printer is not None:
            NODE_PRINTERS[ast.RawStmt] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop(ast.RawStmt, None)


def test_special_function():
    output = RawStream(special_functions=True)

    assert output.get_printer_for_function('foo.test_function') is None

    try:
        @special_function('foo.test_function')
        def test(node, output):
            pass

        assert output.get_printer_for_function('foo.test_function') is test

        with pytest.raises(PrinterAlreadyPresentError):
            @special_function('foo.test_function')
            def test1(node, output):
                pass

        @special_function('foo.test_function', override=True)
        def test_function(node, output):
            output.print_list(node.args, '-')

        result = output('SELECT foo.test_function(x, "Y") FROM sometable')
        assert result == 'SELECT x - "Y" FROM sometable'
    finally:
        SPECIAL_FUNCTIONS.pop('foo.test_function')
