# -*- coding: utf-8 -*-
# :Project:   pglast -- Tests on the printers registry
# :Created:   sab 05 ago 2017 10:31:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2022 Lele Gaifax
#

import warnings

import pytest

from pglast import ast, enums, prettify
from pglast.printers import IntEnumPrinter, NODE_PRINTERS, PrinterAlreadyPresentError
from pglast.printers import get_printer_for_node, node_printer


def test_registry():
    with pytest.raises(ValueError):
        get_printer_for_node(None)

    with pytest.raises(ValueError):
        @node_printer()
        def missing_node(node, output):
            pass

    with pytest.raises(ValueError):
        @node_printer(1)
        def invalid_node(node, output):
            pass

    with pytest.raises(ValueError):
        @node_printer(ast.RawStmt, ast.SelectStmt, ast.UpdateStmt)
        def too_many_nodes(node, output):
            pass

    with pytest.raises(ValueError):
        @node_printer('RawStmt')
        def invalid_node(node, output):
            pass

    with pytest.raises(ValueError):
        @node_printer((ast.RawStmt, 'foo'), ast.SelectStmt)
        def invalid_parents(node, output):
            pass

    raw_stmt = NODE_PRINTERS.pop(ast.RawStmt)
    try:
        @node_printer(ast.RawStmt)
        def raw(node, output):
            pass

        assert NODE_PRINTERS[ast.RawStmt] is raw

        with pytest.raises(PrinterAlreadyPresentError):
            @node_printer(ast.RawStmt)
            def other_raw(node, output):
                pass
    finally:
        NODE_PRINTERS[ast.RawStmt] = raw_stmt


def test_prettify_safety_belt():
    raw_stmt_printer = NODE_PRINTERS.pop(ast.RawStmt, None)
    try:
        @node_printer(ast.RawStmt)
        def raw_stmt_1(node, output):
            output.write('Yeah')

        output = prettify('select 42')
        assert output == 'Yeah'

        with warnings.catch_warnings(record=True) as w:
            output = prettify('select 42', safety_belt=True)
            assert output == 'select 42'
            assert 'Detected a bug' in str(w[0].message)

        @node_printer(ast.RawStmt, override=True)
        def raw_stmt_2(node, output):
            output.write('select 1')

        output = prettify('select 42')
        assert output == 'select 1'

        with warnings.catch_warnings(record=True) as w:
            output = prettify('select 42', safety_belt=True)
            assert output == 'select 42'
            assert 'Detected a non-cosmetic difference' in str(w[0].message)
    finally:
        if raw_stmt_printer is not None:
            NODE_PRINTERS[ast.RawStmt] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop(ast.RawStmt, None)


def test_int_enum_printer():
    class LockWaitPrinter(IntEnumPrinter):
        enum = enums.LockWaitPolicy

        def LockWaitBlock(self, node, output):
            output.append('block')

    lwp = LockWaitPrinter()
    result = []
    lwp('LockWaitBlock', object(), result)
    assert result == ['block']

    with pytest.raises(NotImplementedError):
        lwp('LockWaitError', object(), result)

    with pytest.raises(ValueError):
        lwp('FooBar', object(), result)

    lwp(None, object(), result)
    assert result == ['block']*2


def test_not_int_enum_printer():
    class NotIntEnum(IntEnumPrinter):
        enum = enums.FunctionParameterMode

    with pytest.raises(ValueError):
        NotIntEnum()
