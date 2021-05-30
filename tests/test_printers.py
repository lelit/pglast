# -*- coding: utf-8 -*-
# :Project:   pglast -- Tests on the printers registry
# :Created:   sab 05 ago 2017 10:31:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021 Lele Gaifax
#

import warnings

import pytest

from pglast import enums, prettify
from pglast.node import Missing, Scalar
from pglast.printers import IntEnumPrinter, NODE_PRINTERS, PrinterAlreadyPresentError
from pglast.printers import get_printer_for_node_tag, node_printer


def test_registry():
    with pytest.raises(NotImplementedError):
        get_printer_for_node_tag(None, 'non_existing')

    with pytest.raises(ValueError):
        @node_printer()
        def tag(node, output):
            pass

    with pytest.raises(ValueError):
        @node_printer(1)
        def invalid_tag(node, output):
            pass

    with pytest.raises(ValueError):
        @node_printer('one', 'two', 'three')
        def too_many_tags1(node, output):
            pass

    with pytest.raises(ValueError):
        @node_printer('one', 'two', 'three', check_tags=False)
        def too_many_tags2(node, output):
            pass

    try:
        @node_printer('test_tag1', check_tags=False)
        def tag1(node, output):
            pass

        assert get_printer_for_node_tag(None, 'test_tag1') is tag1

        with pytest.raises(PrinterAlreadyPresentError):
            @node_printer('test_tag1', check_tags=False)
            def tag3(node, output):
                pass

        @node_printer('test_tag1', override=True, check_tags=False)
        def tag1_bis(node, output):
            pass

        assert get_printer_for_node_tag(None, 'test_tag1') is tag1_bis

        @node_printer('test_tag_3', check_tags=False)
        def generic_tag3(node, output):
            pass

        @node_printer('test_tag_1', 'test_tag_3', check_tags=False)
        def specific_tag3(node, output):
            pass

        @node_printer(('test_tag_a', 'test_tag_b'), 'test_tag_3', check_tags=False)
        def specific_tag4(node, output):
            pass

        assert get_printer_for_node_tag(None, 'test_tag_3') is generic_tag3
        assert get_printer_for_node_tag('Foo', 'test_tag_3') is generic_tag3
        assert get_printer_for_node_tag('test_tag_1', 'test_tag_3') is specific_tag3
        assert get_printer_for_node_tag('test_tag_a', 'test_tag_3') is specific_tag4
        assert get_printer_for_node_tag('test_tag_b', 'test_tag_3') is specific_tag4
    finally:
        NODE_PRINTERS.pop('test_tag1', None)


def test_prettify_safety_belt():
    raw_stmt_printer = NODE_PRINTERS.pop('RawStmt', None)
    try:
        @node_printer('RawStmt')
        def raw_stmt_1(node, output):
            output.write('Yeah')

        output = prettify('select 42')
        assert output == 'Yeah'

        with warnings.catch_warnings(record=True) as w:
            output = prettify('select 42', safety_belt=True)
            assert output == 'select 42'
            assert 'Detected a bug' in str(w[0].message)

        @node_printer('RawStmt', override=True)
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
            NODE_PRINTERS['RawStmt'] = raw_stmt_printer
        else:
            NODE_PRINTERS.pop('RawStmt', None)


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
        lwp(None, object(), result)

    with pytest.raises(ValueError):
        lwp('FooBar', object(), result)

    lwp(Scalar('LockWaitBlock'), object(), result)
    assert result == ['block']*2

    with pytest.raises(ValueError):
        lwp(Scalar('FooBar'), object(), result)

    lwp(Scalar(0), object(), result)
    assert result == ['block']*3

    lwp(Missing, object(), result)
    assert result == ['block']*4


def test_not_int_enum_printer():
    class NotIntEnum(IntEnumPrinter):
        enum = enums.FunctionParameterMode

    with pytest.raises(ValueError):
        NotIntEnum()
