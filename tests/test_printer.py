# -*- coding: utf-8 -*-
# :Project:   pg_query -- Tests on the printer.py module
# :Created:   sab 05 ago 2017 10:31:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

import pytest

from pg_query import Node, printer


def test_registry():
    with pytest.raises(NotImplementedError):
        printer.get_printer_for_node_tag('non_existing')

    try:
        @printer.node_printer('test_tag1')
        def tag1(node, output):
            pass

        assert printer.get_printer_for_node_tag('test_tag1') is tag1

        with pytest.raises(printer.PrinterAlreadyPresentError):
            @printer.node_printer('test_tag1')
            def tag2(node, output):
                pass

        @printer.node_printer('test_tag1', override=True)
        def tag2(node, output):
            pass

        assert printer.get_printer_for_node_tag('test_tag1') is tag2
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


def test_raw_stream_basics():
    ptree = [{'TestRoot': {'bar': {'TestChild': {'a': [
        {'TestNiece': {'x': 0, 'y': 0}},
        {'TestNiece': {'x': 1, 'z': [
            {'TestNiece': {'x': 2, 'y': 2}},
            {'TestNiece': {'x': 3, 'z': [
                {'TestNiece': {'x': 4, 'y': 4}},
                {'TestNiece': {'x': 5, 'y': 5}},
            ]}}
        ]}},
    ]}}}}]

    root = Node(ptree)

    output = printer.RawStream()

    with pytest.raises(NotImplementedError) as exc:
        output(root)

    assert "'TestRoot'" in str(exc)

    try:
        @printer.node_printer('TestRoot')
        def test_root(node, output):
            output.write('bar = ')
            output.print(node.bar)

        @printer.node_printer('TestChild')
        def test_child(node, output):
            output.write('a(')
            with output.push_indent():
                output.print_list(node.a, '*')
            output.write(')')

        @printer.node_printer('TestNiece')
        def test_niece(node, output):
            output.write('{')
            output.write('x')
            output.print(node.x)
            output.separator()
            output.write(',')
            output.separator()
            if node.y:
                output.write('y')
                output.print(node.y)
            else:
                if output.options.get('test_child_z_is_expression', True):
                    with output.push_indent(2, relative=False):
                        output.print_list(node.z, '+')
                else:
                    output.print_list(node.z, '/', standalone_items=False)
            output.write('}')

        output = printer.RawStream()
        result = output(root)
        assert result == 'bar = a({x0, y0} * {x1,{x2, y2} + {x3,{x4, y4} + {x5, y5}}})'

        output = printer.RawStream(test_child_z_is_expression=False)
        result = output(root)
        assert result == 'bar = a({x0, y0} * {x1,{x2, y2} / {x3,{x4, y4} / {x5, y5}}})'
    finally:
        printer.NODE_PRINTERS.pop('TestRoot', None)
        printer.NODE_PRINTERS.pop('TestChild', None)
        printer.NODE_PRINTERS.pop('TestNiece', None)


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


def test_indented_stream_basics():
    ptree = [{'TestRoot': {'bar': {'TestChild': {'a': [
        {'TestNiece': {'x': 0, 'y': 0}},
        {'TestNiece': {'x': 1, 'z': [
            {'TestNiece': {'x': 2, 'y': 2}},
            {'TestNiece': {'x': 3, 'z': [
                {'TestNiece': {'x': 4, 'y': 4}},
                {'TestNiece': {'x': 5, 'y': 5}},
            ]}}
        ]}},
    ]}}}}]

    root = Node(ptree)

    output = printer.RawStream()

    with pytest.raises(NotImplementedError) as exc:
        output(root)

    assert "'TestRoot'" in str(exc)

    try:
        @printer.node_printer('TestRoot')
        def test_root(node, output):
            output.write('bar = ')
            output.print(node.bar)

        @printer.node_printer('TestChild')
        def test_child(node, output):
            output.write('a(')
            with output.push_indent():
                output.print_list(node.a, '*')
            output.write(')')

        @printer.node_printer('TestNiece')
        def test_niece(node, output):
            output.write('{')
            output.write('x')
            output.print(node.x)
            output.swrites(',')
            if node.y:
                output.write('y')
                output.print(node.y)
            else:
                if output.options.get('test_child_z_is_expression', True):
                    with output.push_indent(2, relative=False):
                        output.print_list(node.z, '+')
                else:
                    list_sep = output.options.get('test_child_z_list_sep', '/')
                    output.print_list(node.z, list_sep, standalone_items=len(list_sep)==2)
            output.write('}')

        output = printer.IndentedStream()
        result = output(root)
        assert result == """\
bar = a({x0, y0}
      * {x1,{x2, y2}
           + {x3,{x4, y4}
                + {x5, y5}}})"""

        output = printer.IndentedStream(align_expression_operands=False)
        result = output(root)
        assert result == """\
bar = a({x0, y0}
      * {x1,{x2, y2}
           + {x3,{x4, y4}
                + {x5, y5}}})"""

        output = printer.IndentedStream(test_child_z_is_expression=False)
        result = output(root)
        assert result == """\
bar = a({x0, y0}
      * {x1,{x2, y2} / {x3,{x4, y4} / {x5, y5}}})"""

        output = printer.IndentedStream(test_child_z_is_expression=False,
                                        test_child_z_list_sep='//')
        result = output(root)
        assert result == """\
bar = a({x0, y0}
      * {x1,   {x2, y2}
            // {x3,   {x4, y4}
                   // {x5, y5}}})"""
    finally:
        printer.NODE_PRINTERS.pop('TestRoot', None)
        printer.NODE_PRINTERS.pop('TestChild', None)
        printer.NODE_PRINTERS.pop('TestNiece', None)


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
