# -*- coding: utf-8 -*-
# :Project:   pglast — Serialization logic
# :Created:   mer 07 ott 2026 10:12:00 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2026 Lele Gaifax
#

from enum import IntEnum, auto

from . import ast, enums


class ExprPrec(IntEnum):
    """The precedence of the expression, from the loosest to the tightest.

    The value mirrors the order in which the corresponding rules appear in the PostgreSQL
    grammar, so that a node binding looser than another has a smaller value.
    """

    OR = 0               #: ``OR``
    AND = auto()         #: ``AND``
    NOT = auto()         #: ``NOT`` (right-associative)
    IS = auto()          #: ``IS``, ``ISNULL``, ``NOTNULL`` (non-associative)
    COMPARISON = auto()  #: ``< > = <= >= <>`` (non-associative)
    BETWEEN = auto()     #: ``BETWEEN IN LIKE ILIKE SIMILAR`` (non-associative)
    OP = auto()          #: ``Op``/``OPERATOR``, i.e. all other operators
    ADD = auto()         #: ``+ -``
    MUL = auto()         #: ``* / %``
    EXP = auto()         #: ``^``
    AT = auto()          #: ``AT TIME ZONE``, ``AT LOCAL``
    COLLATE = auto()     #: ``COLLATE``
    UMINUS = auto()      #: unary ``+ -`` (right-associative)
    ATOM = auto()        #: ``c_expr``, typecasts, and anything else that cannot be split apart


class ExprContext(IntEnum):
    """Which grammar rule a value is being printed into.

    This is *internal* vocabulary: it is never user visible.
    """

    A_EXPR = 0
    B_EXPR = auto()
    C_EXPR = auto()


class Side(IntEnum):
    """The side of an operator an operand appears on."""

    LEFT = 0
    RIGHT = auto()


_OPERATOR_PRECEDENCE = {
    '+': ExprPrec.ADD,
    '-': ExprPrec.ADD,
    '*': ExprPrec.MUL,
    '/': ExprPrec.MUL,
    '%': ExprPrec.MUL,
    '^': ExprPrec.EXP,
    '<': ExprPrec.COMPARISON,
    '>': ExprPrec.COMPARISON,
    '=': ExprPrec.COMPARISON,
    '<=': ExprPrec.COMPARISON,
    '>=': ExprPrec.COMPARISON,
    '<>': ExprPrec.COMPARISON,
    '!=': ExprPrec.COMPARISON,
}

_SUBQUERY_LIKE_OPERATORS = frozenset(('~~', '!~~', '~~*', '!~~*'))
"""
Operators that are output as ``[NOT] LIKE``/``[NOT] ILIKE``, with the precedence of
``BETWEEN``.
"""


def _operator_name(name):
    """
    Extract the plain name of an operator, or ``None`` if it cannot be determined.

    `name` is the ``A_Expr.name`` slot: a list of `.ast.String` nodes. An operator explicitly
    written as ``OPERATOR(schema.op)`` is a multi-element list, and is reported as ``None``
    because it always has the precedence of ``Op``.
    """

    if isinstance(name, str):
        return name
    if isinstance(name, ast.String):
        return name.sval
    if isinstance(name, (list, tuple)) and len(name) == 1:
        return _operator_name(name[0])
    return None


def operator_precedence(name):
    """Return the precedence of operator `name`.

    :param name: the ``A_Expr.name`` slot
    :returns: ExprPrec

    ``OPERATOR(schema.op)`` always has the precedence of ``Op``.
    """

    operator = _operator_name(name)
    if operator is None:
        return ExprPrec.OP
    return _OPERATOR_PRECEDENCE.get(operator, ExprPrec.OP)


def subquery_operator_precedence(name):
    """
    Return the precedence of operator `name`, as used in a subquery comparison.

    :param name: the ``A_Expr.name`` or ``SubLink.operName`` slot
    :returns: ExprPrec

    A subquery comparison using one of the ``LIKE``/``ILIKE`` operators is printed in that
    keyword form, so the operator binds like ``BETWEEN``; everything else behaves as in
    :func:`operator_precedence`.
    """

    operator = _operator_name(name)
    if operator in _SUBQUERY_LIKE_OPERATORS:
        return ExprPrec.BETWEEN
    return operator_precedence(name)


def special_function_name(node, stream):
    """
    Return the qualified name of the special function that `stream` will use to print `node`.

    :param node: an `.ast.Node` instance
    :param stream: the stream that is printing the node
    :returns: either ``None`` or the qualified name of a registered special function

    Only the functions whose *alternate* form changes the precedence of the node matter here:
    ``pg_catalog.timezone()`` is printed as ``AT TIME ZONE`` and ``pg_catalog.is_normalized()``
    as ``IS ... NORMALIZED``, both only when the ``special_functions`` option is enabled.
    Deferring to the stream keeps this in sync with what is actually emitted.
    """

    if not isinstance(node, ast.FuncCall):
        return None
    funcname = node.funcname
    if not funcname:
        return None
    name = '.'.join(n.sval for n in funcname)
    if stream.get_printer_for_function(name, node) is not None:
        return name


def expr_precedence(node, stream):
    """Return the precedence of the grammar rule that `node` is printed by.

    :param node: an `.ast.Node` instance
    :param stream: the stream that is printing the node
    :returns: ExprPrec
    """

    if node is None:
        return ExprPrec.ATOM

    if isinstance(node, ast.A_Expr):
        kind = node.kind
        if kind == enums.A_Expr_Kind.AEXPR_OP:
            if node.lexpr is None:
                # Prefix operators: unary + and - have UMINUS precedence, all others that of Op
                return (ExprPrec.UMINUS if operator_precedence(node.name) == ExprPrec.ADD
                        else ExprPrec.OP)
            return operator_precedence(node.name)
        if kind in (enums.A_Expr_Kind.AEXPR_OP_ANY, enums.A_Expr_Kind.AEXPR_OP_ALL):
            # The rule has Op precedence, but as a right operand the operator token may bind
            # looser
            return min(subquery_operator_precedence(node.name), ExprPrec.OP)
        if kind in (enums.A_Expr_Kind.AEXPR_DISTINCT, enums.A_Expr_Kind.AEXPR_NOT_DISTINCT):
            return ExprPrec.IS
        if kind == enums.A_Expr_Kind.AEXPR_NULLIF:
            return ExprPrec.ATOM
        # Everything else: IN, LIKE, ILIKE, SIMILAR TO, BETWEEN
        return ExprPrec.BETWEEN

    if isinstance(node, ast.BoolExpr):
        boolop = node.boolop
        if boolop == enums.BoolExprType.AND_EXPR:
            return ExprPrec.AND
        if boolop == enums.BoolExprType.NOT_EXPR:
            return ExprPrec.NOT
        return ExprPrec.OR

    if isinstance(node, (ast.NullTest, ast.BooleanTest, ast.JsonIsPredicate)):
        return ExprPrec.IS

    if isinstance(node, ast.CollateClause):
        return ExprPrec.COLLATE

    if isinstance(node, ast.XmlExpr):
        if node.op == enums.XmlExprOp.IS_DOCUMENT:
            return ExprPrec.IS
        return ExprPrec.ATOM

    if isinstance(node, ast.SubLink):
        if (node.subLinkType == enums.SubLinkType.ANY_SUBLINK
                and not node.operName):
            # IN (...)
            return ExprPrec.BETWEEN
        if node.subLinkType in (enums.SubLinkType.ANY_SUBLINK, enums.SubLinkType.ALL_SUBLINK):
            return min(subquery_operator_precedence(node.operName), ExprPrec.OP)
        return ExprPrec.ATOM

    if isinstance(node, ast.FuncCall):
        special = special_function_name(node, stream)
        if special == 'pg_catalog.timezone' and node.args and len(node.args) <= 2:
            return ExprPrec.AT
        if special == 'pg_catalog.is_normalized':
            return ExprPrec.IS
        return ExprPrec.ATOM

    return ExprPrec.ATOM


def is_subquery_comparison_form(node):
    """Whether `node` is a subquery comparison form: ``x = ANY (...)``, ``x < ALL (...)``.

    :param node: an `.ast.Node` instance
    :returns: bool

    ``x IN (...)`` and the like. As the left operand of an operator at the same precedence these
    never need parens (see :func:`needs_parens_for_precedence`); at any other precedence the
    normal rules apply, since dropping parens there can reassociate the expression or fail to
    parse: ``d = x = ANY(c)`` is rejected outright, and ``d || x = ANY(c)`` reparses with the
    comparison swallowing the concatenation.
    """

    if isinstance(node, ast.A_Expr):
        return node.kind in (enums.A_Expr_Kind.AEXPR_OP_ANY,
                             enums.A_Expr_Kind.AEXPR_OP_ALL,
                             enums.A_Expr_Kind.AEXPR_IN)
    if isinstance(node, ast.SubLink):
        return node.subLinkType in (enums.SubLinkType.ANY_SUBLINK,
                                    enums.SubLinkType.ALL_SUBLINK)
    return False


def needs_parens_for_precedence(node, parent_prec, side, stream):
    """Whether `node` needs parens as the `side` operand of an expression with `parent_prec`.

    :param node: an `.ast.Node` instance
    :param ExprPrec parent_prec: the precedence of the enclosing expression
    :param Side side: either :attr:`Side.LEFT` or :attr:`Side.RIGHT`
    :param stream: the stream that is printing the node
    :returns: bool
    """

    prec = expr_precedence(node, stream)

    if side == Side.LEFT and is_subquery_comparison_form(node) and prec == parent_prec:
        return False

    if prec != parent_prec:
        return prec < parent_prec

    if parent_prec in (ExprPrec.IS, ExprPrec.COMPARISON, ExprPrec.BETWEEN):
        return True
    if parent_prec in (ExprPrec.NOT, ExprPrec.UMINUS):
        # Right-associative prefix operators, e.g. "NOT NOT a"
        return False
    return side == Side.RIGHT


def is_b_expr_rule(node, stream):
    """Whether `node` is handled by a ``b_expr`` rule, so it may appear in a ``b_expr`` context.

    :param node: an `.ast.Node` instance
    :param stream: the stream that is printing the node
    :returns: bool

    Everything that is not handled by a ``b_expr`` rule (e.g. ``NOT``, ``IS NULL``, ``COLLATE``,
    ``AT TIME ZONE``) is only handled by the ``a_expr`` rule and needs explicit parens when used
    in a ``b_expr`` context.
    """

    if node is None:
        return True

    # These have their own "b_expr" rules (their operands get printed in a "b_expr" context as
    # well)
    if isinstance(node, ast.A_Expr):
        return node.kind in (enums.A_Expr_Kind.AEXPR_OP,
                             enums.A_Expr_Kind.AEXPR_DISTINCT,
                             enums.A_Expr_Kind.AEXPR_NOT_DISTINCT,
                             enums.A_Expr_Kind.AEXPR_NULLIF)  # function call syntax

    if isinstance(node, ast.XmlExpr) and node.op == enums.XmlExprOp.IS_DOCUMENT:
        return True

    # "row OVERLAPS row" cannot be ambiguous (so it has no precedence), but is only handled by
    # "a_expr"
    if (isinstance(node, ast.FuncCall)
            and special_function_name(node, stream) == 'pg_catalog.overlaps'
            and node.args is not None and len(node.args) == 4):
        return False

    return expr_precedence(node, stream) == ExprPrec.ATOM


def needs_parens_as_c_expr(node, stream):
    """Whether `node` needs parens when used in a ``c_expr`` context.

    :param node: an `.ast.Node` instance
    :param stream: the stream that is printing the node
    :returns: bool
    """

    return (expr_precedence(node, stream) != ExprPrec.ATOM
            or not is_b_expr_rule(node, stream))
