# -*- coding: utf-8 -*-
# :Project:   pglast -- Tests on the printer.py module
# :Created:   sab 05 ago 2017 10:31:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021 Lele Gaifax
#

import pytest

from pglast import printer


def test_registry():
    with pytest.raises(NotImplementedError):
        printer.get_printer_for_node_tag(None, 'non_existing')

    with pytest.raises(ValueError):
        @printer.node_printer()
        def tag(node, output):
            pass

    with pytest.raises(ValueError):
        @printer.node_printer('one', 'two', 'three')
        def tag2(node, output):
            pass

    try:
        @printer.node_printer('test_tag1')
        def tag1(node, output):
            pass

        assert printer.get_printer_for_node_tag(None, 'test_tag1') is tag1

        with pytest.raises(printer.PrinterAlreadyPresentError):
            @printer.node_printer('test_tag1')
            def tag3(node, output):
                pass

        @printer.node_printer('test_tag1', override=True)  # noqa
        def tag2(node, output):
            pass

        assert printer.get_printer_for_node_tag(None, 'test_tag1') is tag2

        @printer.node_printer('test_tag_3')
        def generic_tag3(node, output):
            pass

        @printer.node_printer('test_tag_1', 'test_tag_3')
        def specific_tag3(node, output):
            pass

        @printer.node_printer(('test_tag_a', 'test_tag_b'), 'test_tag_3')
        def specific_tag4(node, output):
            pass

        assert printer.get_printer_for_node_tag(None, 'test_tag_3') is generic_tag3
        assert printer.get_printer_for_node_tag('Foo', 'test_tag_3') is generic_tag3
        assert printer.get_printer_for_node_tag('test_tag_1', 'test_tag_3') is specific_tag3
        assert printer.get_printer_for_node_tag('test_tag_a', 'test_tag_3') is specific_tag4
        assert printer.get_printer_for_node_tag('test_tag_b', 'test_tag_3') is specific_tag4
    finally:
        printer.NODE_PRINTERS.pop('test_tag1', None)


def test_output_stream():
    output = printer.OutputStream()
    output.writes('SELECT *')
    output.writes(' FROM')
    output.writes('table ')
    output.writes('WHERE')
    output.write('id = 1')

    assert output.getvalue() == 'SELECT * FROM table WHERE id = 1'


def test_raw_stream_with_sql():
    raw_stmt_printer = printer.NODE_PRINTERS.pop('RawStmt', None)
    try:
        @printer.node_printer('RawStmt')
        def raw_stmt(node, output):
            output.write('Yeah')

        output = printer.RawStream()
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah; Yeah'
    finally:
        if raw_stmt_printer is not None:
            printer.NODE_PRINTERS['RawStmt'] = raw_stmt_printer
        else:
            printer.NODE_PRINTERS.pop('RawStmt', None)


def test_raw_stream_invalid_call():
    with pytest.raises(ValueError) as exc:
        printer.RawStream()(1)


def test_indented_stream_with_sql():
    raw_stmt_printer = printer.NODE_PRINTERS.pop('RawStmt', None)
    try:
        @printer.node_printer('RawStmt')
        def raw_stmt(node, output):
            output.write('Yeah')

        output = printer.IndentedStream()
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah;\n\nYeah'

        output = printer.IndentedStream(separate_statements=False)
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah;\nYeah'
    finally:
        if raw_stmt_printer is not None:
            printer.NODE_PRINTERS['RawStmt'] = raw_stmt_printer
        else:
            printer.NODE_PRINTERS.pop('RawStmt', None)


def test_separate_statements():
    """Separate statements by ``separate_statements`` (int) newlines."""
    raw_stmt_printer = printer.NODE_PRINTERS.pop('RawStmt', None)
    try:
        @printer.node_printer('RawStmt')
        def raw_stmt(node, output):
            output.write('Yeah')

        output = printer.IndentedStream(separate_statements=2)
        result = output('SELECT 1; SELECT 2')
        assert result == 'Yeah;\n\n\nYeah'
    finally:
        if raw_stmt_printer is not None:
            printer.NODE_PRINTERS['RawStmt'] = raw_stmt_printer
        else:
            printer.NODE_PRINTERS.pop('RawStmt', None)


def test_special_function():
    output = printer.RawStream(special_functions=True)

    assert output.get_printer_for_function('foo.test_function') is None

    try:
        @printer.special_function('foo.test_function')
        def test(node, output):
            pass

        assert output.get_printer_for_function('foo.test_function') is test

        with pytest.raises(printer.PrinterAlreadyPresentError):
            @printer.special_function('foo.test_function')
            def test1(node, output):
                pass

        @printer.special_function('foo.test_function', override=True)
        def test_function(node, output):
            output.print_list(node.args, '-')

        result = output('SELECT foo.test_function(x, "Y") FROM sometable')
        assert result == 'SELECT x - "Y" FROM sometable'
    finally:
        printer.SPECIAL_FUNCTIONS.pop('foo.test_function')
