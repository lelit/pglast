# -*- coding: utf-8 -*-
# :Project:   pglast — Special functions
# :Created:   mer 22 nov 2017 08:34:34 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2021, 2022, 2024, 2026 Lele Gaifax
#

from .. import ast, enums
from ..precedence import ExprPrec, Side
from . import special_function

# reminder for not yet implemented special functions:
#
# treat(1 as int)
# 'foo' is nfc normalized
# 'foo' is not nfc normalized


def can_use_special_syntax(printer, node):
    "Return whether SQL special syntax can preserve this call's arguments and decorations."

    # User-registered printers own their rendering policy, including overrides.
    if printer not in _BUILTIN_PRINTERS:
        return True
    if (printer in (extract, position)
            and node.funcformat != enums.CoercionForm.COERCE_SQL_SYNTAX):
        return False
    # The built-in special-function printers do not emit ordinary-call decorations.
    if (node.agg_order or node.agg_filter or node.over or node.agg_within_group
            or node.agg_star or node.agg_distinct or node.func_variadic):
        return False
    if printer in (normalize, is_normalized):
        return _has_normalization_form(node.args)
    return True


def _has_normalization_form(args):
    "SQL normalization syntax permits an optional form keyword, not an expression."

    if not args or len(args) > 2:
        return False
    if len(args) == 1:
        return True
    form = args[1]
    return (isinstance(form, ast.A_Const)
            and isinstance(form.val, ast.String)
            and form.val.sval in ('NFC', 'NFD', 'NFKC', 'NFKD'))


def _print_trim(where, node, output):
    output.write('trim({}'.format(where))
    if len(node.args) > 1:
        output.write(' ')
        output.print_node(node.args[1])
    output.write(' FROM ')
    output.print_node(node.args[0])
    output.write(')')


@special_function('pg_catalog.btrim')
def btrim(node, output):
    """
    Emit function ``pg_catalog.btrim('  abc  ')`` as ``trim(BOTH FROM '  abc  ')``
    and ``pg_catalog.btrim('xxabcxx', 'x')`` as ``trim(BOTH 'x' FROM 'xxabcxx')``.
    """
    _print_trim('BOTH', node, output)


@special_function('pg_catalog.pg_collation_for')
def pg_collation_for(node, output):
    "Emit function ``pg_catalog.pg_collation_for(x)`` as ``COLLATION FOR (x)``."
    output.write('COLLATION FOR ')
    with output.expression(True):
        output.print_node(node.args[0])


@special_function('pg_catalog.extract')
def extract(node, output):
    """
    Emit function ``pg_catalog.extract(field, timestamp)`` as
    ``EXTRACT(field FROM timestamp).``.
    """
    output.write('EXTRACT')
    with output.expression(True):
        if isinstance(node.args[0], ast.A_Const):
            output.write(node.args[0].val.sval.upper())
        else:
            output.print_node(node.args[0])
        output.write(' FROM ')
        output.print_node(node.args[1])


@special_function('pg_catalog.ltrim')
def ltrim(node, output):
    """
    Emit function ``pg_catalog.ltrim('  abc  ')`` as ``trim(LEADING FROM '  abc  ')``
    and ``pg_catalog.ltrim('xxabcxx', 'x')`` as ``trim(LEADING 'x' FROM 'xxabcxx').``
    """
    _print_trim('LEADING', node, output)


# normalize(U&'\0061\0308bc', NFC)
@special_function('pg_catalog.normalize')
def normalize(node, output):
    """
    Emit function ``pg_catalog.normalize(a)`` as ``normalize(x)`` and function
    ``pg_catalog.normalize('a','b')`` as ``normalize('a', b)``.
    """
    output.write('normalize')
    with output.expression(True):
        output.print_node(node.args[0])
        if len(node.args) > 1:
            output.write(', ')
            output.write(node.args[1].val.sval.upper())


@special_function('pg_catalog.is_normalized')
def is_normalized(node, output):
    """
    Emit function ``pg_catalog.is_normalized(v, kind)`` as ``v IS kind NORMALIZED``.
    """
    output.print_operand(node.args[0], ExprPrec.IS, Side.LEFT)
    output.write(' IS ')
    if len(node.args) > 1:
        output.write(node.args[1].val.sval)
        output.write(' ')
    output.write('NORMALIZED')


@special_function('pg_catalog.overlaps')
def overlaps(node, output):
    "Emit function ``pg_catalog.overlaps(a, b, c, d)`` as ``(a, b) OVERLAPS (c, d)``."
    with output.expression(True):
        output.print_list((node.args[0], node.args[1]), standalone_items=False)
    output.write(' OVERLAPS ')
    with output.expression(True):
        output.print_list((node.args[2], node.args[3]), standalone_items=False)


@special_function('pg_catalog.overlay')
def overlay(node, output):
    """
    Emit function ``pg_catalog.overlay('Txxxxas','hom', 2, 4)`` as
    ``overlay('Txxxxas' PLACING 'hom' FROM 2 FOR 4)``."
    """
    output.write('overlay')
    with output.expression(True):
        output.print_node(node.args[0])
        output.write(' PLACING ')
        output.print_node(node.args[1])
        output.write(' FROM ')
        output.print_node(node.args[2])
        if len(node.args) > 3:
            output.write(' FOR ')
            output.print_node(node.args[3])


@special_function('pg_catalog.position')
def position(node, output):
    "Emit function ``pg_catalog.position('abcd', 'a')`` as ``position('a' IN 'abcd')``."
    output.write('position')
    with output.expression(True):
        # Both operands of POSITION are b_expr in gram.y
        output.print_b_expr(node.args[1])
        output.write(' IN ')
        output.print_b_expr(node.args[0])


@special_function('pg_catalog.rtrim')
def rtrim(node, output):
    """
    Emit function ``pg_catalog.rtrim('  abc  ')`` as ``trim(TRAILING FROM '  abc  ')``
    and ``pg_catalog.rtrim('xxabcxx', 'x')`` as ``trim(TRAILING 'x' FROM 'xxabcxx')``
    """
    _print_trim('TRAILING', node, output)


@special_function('pg_catalog.substring')
def substring(node, output):
    """
    Emit function ``pg_catalog.substring('Txxxxas', 2, 4)`` as
    ``substring('Txxxxas' FROM 2 FOR 4)`` and ``pg_catalog.substring('blabla', 2)``
    as ``substring('blabla' FROM 2)``.
    """
    output.write('substring')
    with output.expression(True):
        output.print_node(node.args[0])
        output.write(' FROM ')
        output.print_node(node.args[1])
        if len(node.args) > 2:
            output.write(' FOR ')
            output.print_node(node.args[2])


@special_function('pg_catalog.timezone')
def timezone(node, output):
    """
    Emit function ``pg_catalog.timezone(tz, timestamp)`` as ``timestamp AT TIME ZONE tz``.
    """
    if len(node.args) == 1:
        output.print_operand(node.args[0], ExprPrec.AT, Side.LEFT)
        output.write(' AT LOCAL')
    else:
        output.print_operand(node.args[1], ExprPrec.AT, Side.LEFT)
        output.write(' AT TIME ZONE ')
        output.print_operand(node.args[0], ExprPrec.AT, Side.RIGHT)


@special_function('pg_catalog.xmlexists')
def xmlexists(node, output):
    "Emit function ``pg_catalog.xmlexists(x, y)`` as ``xmlexists(x PASSING BY REF y)``."
    output.write('xmlexists')
    with output.expression(True):
        # Both operands of XMLEXISTS are c_expr in gram.y
        output.print_c_expr(node.args[0])
        output.write(' PASSING BY REF ')
        output.print_c_expr(node.args[1])


_BUILTIN_PRINTERS = (btrim, pg_collation_for, extract, ltrim, normalize, is_normalized,
                     overlaps, overlay, position, rtrim, substring, timezone, xmlexists)
