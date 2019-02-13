# -*- coding: utf-8 -*-
# :Project:   pglast -- Tests on the printer.py module
# :Created:   sab 05 ago 2017 10:31:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019 Lele Gaifax
#

import pytest

from pglast import Node, printer, split


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
            output.print_node(node.bar)

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
            output.print_node(node.x)
            output.separator()
            output.write(',')
            output.separator()
            if node.y:
                output.write('y')
                output.print_node(node.y)
            else:
                if output.test_child_z_is_expression:
                    with output.push_indent(2, relative=False):
                        output.print_list(node.z, '+')
                else:
                    output.print_list(node.z, '/', standalone_items=False)
            output.write('}')

        output = printer.RawStream()
        output.test_child_z_is_expression = True
        result = output(root)
        assert result == 'bar = a({x0, y0} * {x1,{x2, y2} + {x3,{x4, y4} + {x5, y5}}})'

        output = printer.RawStream()
        output.test_child_z_is_expression = False
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


def test_raw_stream_invalid_call():
    with pytest.raises(ValueError) as exc:
        printer.RawStream()(1)


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
            output.print_node(node.bar)

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
            output.print_node(node.x)
            output.swrites(',')
            if node.y:
                output.write('y')
                output.print_node(node.y)
            else:
                if output.test_child_z_is_expression:
                    with output.push_indent(2, relative=False):
                        output.print_list(node.z, '+')
                else:
                    list_sep = output.test_child_z_list_sep
                    output.print_list(node.z, list_sep, standalone_items=len(list_sep) == 2)
            output.write('}')

        output = printer.IndentedStream()
        output.test_child_z_is_expression = True
        output.test_child_z_list_sep = '/'
        result = output(root)
        assert result == """\
bar = a({x0, y0}
      * {x1,{x2, y2}
           + {x3,{x4, y4}
                + {x5, y5}}})"""

        output = printer.IndentedStream()
        output.test_child_z_is_expression = False
        output.test_child_z_list_sep = '/'
        result = output(root)
        assert result == """\
bar = a({x0, y0}
      * {x1,{x2, y2} / {x3,{x4, y4} / {x5, y5}}})"""

        output = printer.IndentedStream()
        output.test_child_z_is_expression = False
        output.test_child_z_list_sep = '//'
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


def test_names_and_symbols():
    ptree = [{'TestRoot': {
        'a': {
            "String": {
                "str": "Sum"
            }},
        'b': [{
            "String": {
                "str": "foo"
            }}],
        'c': [{
            "String": {
                "str": "table"
            }
        }, {
            "String": {
                "str": "bar"
            }}],
        'd': [{
            "String": {
                "str": "Schema"
            }
        }, {
            "String": {
                "str": "="
            }
        }],
    }}]

    first_node = Node(ptree)[0]

    def do(meth, node):
        output = printer.RawStream()
        getattr(output, meth)(node)
        return output.getvalue()

    assert do('print_name', first_node.a) == '"Sum"'
    assert do('print_name', first_node.b) == 'foo'
    assert do('print_name', first_node.c) == '"table".bar'
    assert do('print_name', first_node.d) == '"Schema"."="'

    assert do('print_symbol', first_node.a) == 'Sum'
    assert do('print_symbol', first_node.b) == 'foo'
    assert do('print_symbol', first_node.c) == '"table".bar'
    assert do('print_symbol', first_node.d) == '"Schema".='


def test_split():
    result = split('select a from b')
    assert next(result) == 'SELECT a FROM b'
    with pytest.raises(StopIteration):
        next(result)

    result = split('select a from b; select b from a')
    assert next(result) == 'SELECT a FROM b'
    assert next(result) == 'SELECT b FROM a'
    with pytest.raises(StopIteration):
        next(result)

    result = split('select a from b', stream_class=printer.IndentedStream)
    assert next(result) == 'SELECT a\nFROM b'
    with pytest.raises(StopIteration):
        next(result)
