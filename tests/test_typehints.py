# -*- coding: utf-8 -*-
# :Project:   pglast — Test type hints for Cython functions
# :Created:   2025-01-27
# :Author:    Pierce Freeman <hi@pierce.dev>
# :License:   GNU General Public License version 3 or later
#

"""
Test module to validate that type hints work properly for pglast functions,
especially those originally implemented in Cython.
"""

import sys
import subprocess

import pytest


def stub_parse_sql_basic() -> None:
    """Stub function to test basic parse_sql type hints."""
    from pglast.ast import Node
    from pglast.parser import parse_sql

    query: str = "SELECT 1"
    result: tuple[Node, ...] = parse_sql(query)

    # Runtime type checks
    assert isinstance(result, tuple), f'Expected tuple, got {type(result)}'
    assert len(result) > 0, 'Expected non-empty result'
    assert isinstance(result[0], Node), f'Expected Node, got {type(result[0])}'

    # These should work fine
    first_stmt: Node = result[0]
    stmt_count: int = len(result)
    assert isinstance(first_stmt, Node), f'Expected Node, got {type(first_stmt)}'
    assert isinstance(stmt_count, int), f'Expected int, got {type(stmt_count)}'


def stub_parse_sql_empty() -> None:
    """Stub function to test parse_sql with empty input."""
    from pglast.ast import Node
    from pglast.parser import parse_sql

    empty_query: str = ''
    empty_result: tuple[Node, ...] = parse_sql(empty_query)

    # Runtime type checks
    assert isinstance(empty_result, tuple), f'Expected tuple, got {type(empty_result)}'
    assert len(empty_result) == 0, f'Expected empty tuple, got {len(empty_result)} items'

    # Should be empty tuple
    count: int = len(empty_result)
    assert isinstance(count, int), f'Expected int, got {type(count)}'
    assert count == 0, f'Expected 0, got {count}'


def stub_parser_functions() -> None:
    """Stub function to test other parser function type hints."""
    from pglast.parser import get_postgresql_version, fingerprint, scan, split, Token

    query: str = 'SELECT name FROM users WHERE id = 1'

    # Test get_postgresql_version
    version: tuple[int, int] = get_postgresql_version()
    assert isinstance(version, tuple), f'Expected tuple, got {type(version)}'
    assert len(version) == 2, f'Expected tuple of length 2, got {len(version)}'
    major: int = version[0]
    minor: int = version[1]
    assert isinstance(major, int), f'Expected int, got {type(major)}'
    assert isinstance(minor, int), f'Expected int, got {type(minor)}'

    # Test fingerprint
    fp: str = fingerprint(query)
    assert isinstance(fp, str), f'Expected str, got {type(fp)}'
    fp_length: int = len(fp)
    assert isinstance(fp_length, int), f'Expected int, got {type(fp_length)}'

    # Test scan
    tokens: list[Token] = scan(query)
    assert isinstance(tokens, list), f'Expected list, got {type(tokens)}'
    assert len(tokens) > 0, 'Expected non-empty token list'
    first_token: Token = tokens[0]
    assert isinstance(first_token, Token), f'Expected Token, got {type(first_token)}'
    token_start: int = first_token.start
    assert isinstance(token_start, int), f'Expected int, got {type(token_start)}'

    # Test split
    statements: tuple[str | slice, ...] = split('SELECT 1; SELECT 2;')
    assert isinstance(statements, tuple), f'Expected tuple, got {type(statements)}'
    assert len(statements) == 2, f'Expected 2 statements, got {len(statements)}'
    first_stmt: str | slice = statements[0]
    assert isinstance(first_stmt, str), f'Expected str, got {type(first_stmt)}'


def stub_parser_variables() -> None:
    """Stub function to test parser's exported variables."""
    from pglast.parser import LONG_MAX

    lm: int = LONG_MAX


def stub_prettify_function() -> None:
    """Stub function to test prettify type hints."""
    from pglast import prettify

    query: str = 'select 1'

    # Test basic prettify
    pretty: str = prettify(query)
    assert isinstance(pretty, str), f'Expected str, got {type(pretty)}'
    pretty_length: int = len(pretty)
    assert isinstance(pretty_length, int), f'Expected int, got {type(pretty_length)}'

    # Test with options
    pretty_options: str = prettify(query, safety_belt=True, preserve_comments=False)
    assert isinstance(pretty_options, str), f'Expected str, got {type(pretty_options)}'


def stub_parse_plpgsql_function() -> None:
    """Stub function to test parse_plpgsql type hints."""
    from typing import Any
    from pglast import parse_plpgsql

    plpgsql_stmt: str = '''
    CREATE FUNCTION add (a integer, b integer)
    RETURNS integer AS $$
    BEGIN
      RETURN a + b;
    END;
    $$ LANGUAGE plpgsql
    '''

    result: list[dict[str, Any]] = parse_plpgsql(plpgsql_stmt)
    assert isinstance(result, list), f'Expected list, got {type(result)}'
    assert len(result) > 0, 'Expected non-empty result'
    first_item: dict[str, Any] = result[0]
    assert isinstance(first_item, dict), f'Expected dict, got {type(first_item)}'


def stub_ast_fields() -> None:
    """Stub function to test generated AST field type hints."""
    from pglast import ast, parse_sql

    stmt = parse_sql('SELECT 1')[0]
    raw: ast.RawStmt = stmt
    node: ast.Node | None = stmt.stmt
    location: int | None = stmt.stmt_location
    length: int | None = stmt.stmt_len

    assert isinstance(raw, ast.RawStmt)
    assert isinstance(node, ast.Node)
    assert isinstance(location, int)
    assert isinstance(length, int)

    if isinstance(node, ast.SelectStmt):
        targets: tuple[object, ...] | None = node.targetList
        where_clause: ast.Node | None = node.whereClause
        select_all: bool | None = node.all

        assert targets is not None
        assert where_clause is None
        assert isinstance(select_all, bool)


def stub_ast_constructors() -> None:
    """Stub function to test permissive generated AST constructors."""
    from pglast import ast

    relation = ast.RangeVar(relname='users', inh=True, relpersistence='p')
    relname: str | None = relation.relname
    alias: ast.Alias | None = relation.alias

    const = ast.A_Const(isnull=False, val=ast.Integer(ival=1))
    value: ast.Node | None = const.val

    assert relname == 'users'
    assert alias is None
    assert isinstance(value, ast.Integer)


def stub_raw_expression_nodes() -> None:
    """Raw parser nodes are valid in fields declared Expr* by PostgreSQL."""
    from pglast import ast, enums

    column = ast.ColumnRef(fields=(ast.String(sval='x'),))
    literal = ast.A_Const(isnull=False, val=ast.Integer(ival=1))
    operator = ast.A_Expr(kind=enums.A_Expr_Kind.AEXPR_OP,
                          name=(ast.String(sval='='),), lexpr=column, rexpr=literal)
    for raw in (column, literal, operator):
        case = ast.CaseExpr(arg=raw, args=(ast.CaseWhen(expr=raw, result=raw),),
                            defresult=raw)
        when = ast.CaseWhen(expr=raw, result=raw)
        null_test = ast.NullTest(arg=raw, nulltesttype=enums.NullTestType.IS_NULL)
        boolean_test = ast.BooleanTest(arg=raw, booltesttype=enums.BoolTestType.IS_TRUE)
        assert case.arg is raw and case.defresult is raw
        assert when.expr is raw and when.result is raw
        assert null_test.arg is raw and boolean_test.arg is raw
        case.arg = raw
        case.defresult = raw
        when.expr = raw
        when.result = raw
        null_test.arg = raw
        boolean_test.arg = raw
        value: ast.Node | None = case.arg
        assert value is raw

    # Set another field so the first-argument whole-node payload overload is not used.
    payload = {'@': 'ColumnRef', 'fields': ({'@': 'String', 'sval': 'x'},)}
    assert ast.CaseExpr(arg=payload, location=0).arg == column
    assert ast.CaseWhen(expr=payload, result=payload).result == column
    assert ast.NullTest(arg=payload, location=0).arg == column
    assert ast.BooleanTest(arg=payload, location=0).arg == column
    assert ast.CaseExpr(arg=None, defresult=None).arg is None
    assert ast.CaseWhen(expr=None, result=None).result is None
    assert ast.NullTest(arg=None).arg is None
    assert ast.BooleanTest(arg=None).arg is None


def stub_expression_lists() -> None:
    """IN/BETWEEN accept lists and tuples, but expose tuples after adaptation."""
    from typing import Any

    from pglast import ast, enums

    column = ast.ColumnRef(fields=(ast.String(sval='x'),))
    literal = ast.A_Const(isnull=False, val=ast.Integer(ival=1))
    for kind in (enums.A_Expr_Kind.AEXPR_IN, enums.A_Expr_Kind.AEXPR_BETWEEN):
        for values in ((literal, literal), [literal, literal]):
            expression = ast.A_Expr(kind=kind, name=(ast.String(sval='='),),
                                    lexpr=column, rexpr=values)
            result: ast.Node | tuple[Any, ...] | None = expression.rexpr
            assert isinstance(result, tuple)
            assert result == (literal, literal)
        expression.rexpr = (literal,)
        assert expression.rexpr == (literal,)

    scalar = ast.A_Expr(kind=enums.A_Expr_Kind.AEXPR_OP, rexpr=literal)
    assert scalar.rexpr is literal
    scalar.rexpr = column
    assert scalar.rexpr is column
    assert ast.A_Expr(rexpr=None).rexpr is None
    payload = {'@': 'A_Const', 'isnull': False, 'val': {'@': 'Integer', 'ival': 1}}
    assert ast.A_Expr(rexpr=payload).rexpr == literal
    assert ast.A_Expr(rexpr=[payload]).rexpr == (literal,)
    assert ast.A_Expr(rexpr=(payload,)).rexpr == (literal,)


def stub_parsed_raw_expressions() -> None:
    """Read raw expressions from actual parser output with appropriate narrowing."""
    from pglast import ast, parse_sql

    simple = parse_sql('SELECT CASE x WHEN 1 THEN 2 ELSE 3 END')[0].stmt
    searched = parse_sql('SELECT CASE WHEN x = 1 THEN 2 ELSE 3 END')[0].stmt
    for stmt in (simple, searched):
        assert isinstance(stmt, ast.SelectStmt) and stmt.targetList
        case = stmt.targetList[0].val
        assert isinstance(case, ast.CaseExpr) and case.args
        assert case.arg is None or isinstance(case.arg, ast.ColumnRef)
        assert isinstance(case.defresult, ast.A_Const)
        when = case.args[0]
        assert isinstance(when, ast.CaseWhen)
        assert isinstance(when.expr, (ast.A_Const, ast.A_Expr))
        assert isinstance(when.result, ast.A_Const)

    for sql in ('SELECT x IS NULL', 'SELECT x IS TRUE'):
        stmt = parse_sql(sql)[0].stmt
        assert isinstance(stmt, ast.SelectStmt) and stmt.targetList
        test = stmt.targetList[0].val
        assert isinstance(test, (ast.NullTest, ast.BooleanTest))
        assert isinstance(test.arg, ast.ColumnRef)

    for sql in ('SELECT x IN (1, 2)', 'SELECT x BETWEEN 1 AND 2', 'SELECT x = 1'):
        stmt = parse_sql(sql)[0].stmt
        assert isinstance(stmt, ast.SelectStmt) and stmt.targetList
        expression = stmt.targetList[0].val
        assert isinstance(expression, ast.A_Expr)
        if isinstance(expression.rexpr, tuple):
            assert len(expression.rexpr) == 2
            assert all(isinstance(item, ast.A_Const) for item in expression.rexpr)
        else:
            assert isinstance(expression.rexpr, ast.A_Const)


def stub_raw_expression_type_errors() -> None:
    from pglast import ast

    ast.NullTest(arg=123)


def stub_expression_list_type_errors() -> None:
    from pglast import ast

    ast.A_Expr(rexpr=123)


def stub_list_valued_node_fields() -> None:
    """Node* fields can hold lists in ordinary raw parser output."""
    from pglast import ast, parse_sql

    name = ast.String(sval='mytable')
    option = ast.DefElem(defname='fillfactor', arg=ast.Integer(ival=40))
    statement = ast.SelectStmt()
    for values in ((name,), [name]):
        assert ast.SecLabelStmt(object=values).object == (name,)
        assert ast.DefElem(arg=values).arg == (name,)
    for options in ((option,), [option]):
        assert ast.AlterTableCmd(def_=options).def_ == (option,)
    for body in (((statement,),), [(statement,)]):
        assert ast.CreateFunctionStmt(sql_body=body).sql_body == ((statement,),)

    label = parse_sql('SECURITY LABEL FOR selinux ON TABLE mytable IS NULL')[0].stmt
    assert isinstance(label, ast.SecLabelStmt)
    assert isinstance(label.object, tuple) and isinstance(label.object[0], ast.String)
    alter = parse_sql('ALTER INDEX idx SET (fillfactor = 40)')[0].stmt
    assert isinstance(alter, ast.AlterTableStmt) and alter.cmds
    command = alter.cmds[0]
    assert isinstance(command, ast.AlterTableCmd)
    assert isinstance(command.def_, tuple) and isinstance(command.def_[0], ast.DefElem)
    function = parse_sql("CREATE FUNCTION f() RETURNS int LANGUAGE SQL AS 'SELECT 1'")[0].stmt
    assert isinstance(function, ast.CreateFunctionStmt) and function.options
    definition = function.options[1]
    assert isinstance(definition, ast.DefElem)
    assert isinstance(definition.arg, tuple) and isinstance(definition.arg[0], ast.String)
    atomic = parse_sql(
        'CREATE FUNCTION f() RETURNS int LANGUAGE SQL BEGIN ATOMIC SELECT 1; END'
    )[0].stmt
    assert isinstance(atomic, ast.CreateFunctionStmt)
    assert isinstance(atomic.sql_body, tuple) and isinstance(atomic.sql_body[0], tuple)
    assert isinstance(atomic.sql_body[0][0], ast.SelectStmt)


def stub_adapted_attribute_assignments() -> None:
    """Assignments accept constructor inputs and expose adapted values on reads."""
    from decimal import Decimal
    from typing import Any

    from pglast import ast, enums

    column = ast.ColumnRef()
    column.fields = [ast.String(sval='x')]
    fields: tuple[Any, ...] | None = column.fields
    assert isinstance(fields, tuple) and isinstance(fields[0], ast.String)
    expression = ast.A_Expr()
    expression.kind = 'AEXPR_IN'
    kind: enums.A_Expr_Kind | None = expression.kind
    assert kind is enums.A_Expr_Kind.AEXPR_IN
    expression.lexpr = {'@': 'ColumnRef', 'fields': ({'@': 'String', 'sval': 'x'},)}
    left: ast.Node | None = expression.lexpr
    assert isinstance(left, ast.ColumnRef)
    relation = ast.RangeVar()
    relation.alias = {'@': 'Alias', 'aliasname': 't'}
    alias: ast.Alias | None = relation.alias
    assert isinstance(alias, ast.Alias) and alias.aliasname == 't'
    relation.relpersistence = ord('p')
    persistence: str | None = relation.relpersistence
    assert persistence == 'p'
    relation.inh = 1
    inherited: bool | None = relation.inh
    assert inherited is True
    number = ast.Float()
    number.fval = Decimal('1.5')
    value: str | None = number.fval
    assert value == '1.5'
    foreign = ast.CreateForeignTableStmt()
    foreign.base = {'@': 'CreateStmt'}
    base: ast.CreateStmt | None = foreign.base
    assert isinstance(base, ast.CreateStmt)
    grouping = ast.Var()
    grouping.varnullingrels = [1, 2]
    cols: set[int] | None = grouping.varnullingrels
    assert cols == {1, 2}
    column.fields = None
    assert column.fields is None


def stub_invalid_attribute_assignment() -> None:
    from pglast import ast

    ast.ColumnRef().fields = 123


def stub_adapted_attribute_read_type_errors() -> None:
    from pglast import ast

    column = ast.ColumnRef()
    column.fields = [ast.String(sval='x')]
    _wrong: list[ast.Node] = column.fields


def stub_empty_raw_statement() -> None:
    """Manually constructed RawStmt nodes can have no statement."""
    from pglast import ast

    empty = ast.RawStmt()
    node: ast.Node | None = empty.stmt
    assert node is None
    assert ast.RawStmt(stmt=None).stmt is None
    assert ast.RawStmt({'@': 'RawStmt', 'stmt': None}).stmt is None
    empty.stmt = ast.SelectStmt()
    assert isinstance(empty.stmt, ast.SelectStmt)
    empty.stmt = None
    assert empty.stmt is None


def stub_unchecked_raw_statement_type_errors() -> None:
    from pglast import ast

    # The optional child must be narrowed before calling its serializer.
    ast.RawStmt().stmt()


def stub_enums_and_streams() -> None:
    """Stub function to test generated enum and stream type hints."""
    from pglast import enums, parse_sql
    from pglast.stream import IndentedStream, RawStream

    tag: enums.NodeTag = enums.NodeTag.T_RawStmt
    kind: enums.A_Expr_Kind = enums.A_Expr_Kind.AEXPR_OP
    lock_mode: int = enums.AccessShareLock

    raw_sql: str = RawStream()(parse_sql('SELECT 1'))
    pretty_sql: str = IndentedStream(compact_lists_margin=80)('SELECT 1')

    assert tag is enums.NodeTag.T_RawStmt
    assert kind is enums.A_Expr_Kind.AEXPR_OP
    assert isinstance(lock_mode, int)
    assert raw_sql == 'SELECT 1'
    assert pretty_sql == 'SELECT 1'


def stub_public_module_types() -> None:
    """Stub function to test handwritten public module type hints."""
    from pglast.parser import Comment, comments, split
    from pglast.visitors import referenced_relations

    statements: tuple[str, ...] = split('SELECT 1; SELECT 2')
    slices: tuple[slice, ...] = split('SELECT 1; SELECT 2', only_slices=True)
    parsed_comments: tuple[Comment, ...] = comments('SELECT 1 -- comment')
    relations: set[str] = referenced_relations('SELECT * FROM users')

    assert statements == ('SELECT 1', 'SELECT 2')
    assert slices == (slice(0, 8), slice(10, 18))
    assert parsed_comments[0].str == '-- comment'
    assert relations == {'users'}


def stub_precedence_types() -> None:
    """Stub function to test the public type hints of the precedence module."""
    from pglast import ast, parse_sql, visitors
    from pglast.precedence import (
        ExprContext,
        ExprPrec,
        Side,
        expr_precedence,
        is_b_expr_rule,
        is_subquery_comparison_form,
        needs_parens_as_c_expr,
        needs_parens_for_precedence,
        operator_precedence,
        subquery_operator_precedence,
    )
    from pglast.stream import IndentedStream, RawStream

    stream: RawStream = RawStream()
    tree = parse_sql('SELECT 1 + 2 * 3')
    visitors.populate_ancestors(tree)
    node: ast.Node | None = tree[0].stmt
    assert node is not None

    prec: ExprPrec = expr_precedence(node, stream)
    op_prec: ExprPrec = operator_precedence([ast.String(sval='+')])
    sub_prec: ExprPrec = subquery_operator_precedence(None)
    needs: bool = needs_parens_for_precedence(node, ExprPrec.ADD, Side.LEFT, stream)
    is_b: bool = is_b_expr_rule(node, stream)
    as_c: bool = needs_parens_as_c_expr(node, stream)
    sub_cmp: bool = is_subquery_comparison_form(node)

    ctx: ExprContext = ExprContext.A_EXPR
    assert ctx is ExprContext.A_EXPR
    assert Side.LEFT.value != Side.RIGHT.value
    assert isinstance(prec, ExprPrec)
    assert isinstance(op_prec, ExprPrec)
    assert isinstance(sub_prec, ExprPrec)
    assert needs or not needs
    assert is_b or not is_b
    assert as_c or not as_c
    assert not sub_cmp


def stub_stream_expr_context() -> None:
    """Stub function to test the expression context API of the streams."""
    from pglast import ast, parse_sql, visitors
    from pglast.precedence import ExprContext, ExprPrec, Side
    from pglast.stream import IndentedStream, RawStream

    tree = parse_sql('SELECT a + b * c')
    visitors.populate_ancestors(tree)
    node: ast.Node | None = tree[0].stmt
    assert node is not None

    for stream in (RawStream(), IndentedStream()):
        ctx: ExprContext = stream.expr_context
        assert ctx is ExprContext.A_EXPR

        with stream.push_expr_context(ExprContext.B_EXPR):
            stream.print_operand(node, ExprPrec.MUL, Side.LEFT)

        stream.print_operand(node, ExprPrec.MUL, Side.RIGHT, ExprContext.A_EXPR)
        stream.print_b_expr(node)

    assert RawStream().getvalue() == ''


def stub_remaining_importable_modules() -> None:
    """Stub function to test every remaining importable module has useful stubs."""
    from argparse import Namespace
    from typing import Any, Callable, Sequence

    from pglast import ast, enums, keywords
    from pglast.__main__ import main, workhorse
    from pglast.printers import ddl, dml, sfuncs

    reserved: set[str] = keywords.RESERVED_KEYWORDS
    unreserved: set[str] = keywords.UNRESERVED_KEYWORDS
    main_fn: Callable[[Sequence[str] | None], None] = main
    workhorse_fn: Callable[[Namespace], None] = workhorse
    select_printer: Callable[[ast.SelectStmt, Any], None] = dml.select_stmt
    access_printer: Callable[[ast.AccessPriv, Any], None] = ddl.access_priv
    special_printer: Callable[[ast.FuncCall, Any], None] = sfuncs.btrim
    alter_enum: type[enums.AlterTableType] = ddl.AlterTableTypePrinter.enum
    expr_enum: type[enums.A_Expr_Kind] = dml.AExprKindPrinter.enum

    assert 'select' in reserved
    assert 'abort' in unreserved
    assert main_fn is main
    assert workhorse_fn is workhorse
    assert select_printer is dml.select_stmt
    assert access_printer is ddl.access_priv
    assert special_printer is sfuncs.btrim
    assert alter_enum is enums.AlterTableType
    assert expr_enum is enums.A_Expr_Kind


def stub_type_errors() -> None:
    """
    Stub function that should cause type checker errors.
    """
    from pglast import parse_sql

    query: str = 'SELECT 1'
    # Intentional error, to assert that the type checker is not cheating
    _wrong_type: int = parse_sql(query)


def stub_ast_field_type_errors() -> None:
    """
    Stub function that should cause type checker errors on AST field access.
    """
    from pglast.parser import parse_sql

    _wrong_type: int = parse_sql('SELECT 1')[0].stmt


def stub_ast_constructor_type_errors() -> None:
    """
    Stub function that should cause type checker errors for invalid AST construction.
    """
    from pglast import ast

    ast.A_Const(isnull=False, val=1)
    ast.RangeVar(alias=1)
    ast.SelectStmt(all='yes')


def stub_stream_type_errors() -> None:
    """
    Stub function that should cause type checker errors for stream list inputs.
    """
    from pglast import ast
    from pglast.stream import RawStream

    nodes = (ast.String(sval='a'), ast.String(sval='b'))
    RawStream().print_list((node for node in nodes), sep='.')


def run_type_checker_on_stub(
    stub_function,
    checker: tuple[str, ...],
    should_pass: bool = True,
) -> None:
    """
    Helper function to run a type checker on a stub function and execute it for runtime
    validation.

    :param stub_function: the stub function to test
    :param checker: which checker
    :param should_pass: whether the check should pass (``True``) or fail (``False``)
    """
    import tempfile
    import os
    import inspect

    stub_function_name = stub_function.__name__
    source = inspect.getsource(stub_function)
    test_code = f"""# Test file for type specs validation

{source}


if __name__ == '__main__':
    {stub_function_name}()
"""

    # Neither type checker can follow the import hook that the editable install of the package
    # uses (`pglast` is then served by a meta path finder, not by a real directory in
    # site-packages); moreover `ty` does not honor PYTHONPATH. Running them from the project
    # directory makes the package resolvable as first-party code, which works in every mode.
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Create a temporary directory to isolate the test
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = os.path.join(temp_dir, f'{stub_function_name}.py')

        with open(temp_file, 'w') as f:
            f.write(test_code)

        try:
            result = subprocess.run(
                checker + (temp_file,),
                capture_output=True,
                text=True,
                cwd=project_dir,
            )
        except FileNotFoundError:
            pytest.skip(f'Could not execute type checker: {checker!r}')
            return

        if result.returncode and ': No module named ' in result.stderr:
            pytest.skip(f'Could not execute type checker: {checker!r}')
            return

        if should_pass:
            assert result.returncode == 0, (
                f'Type checker found unexpected type errors in {stub_function_name}:'
                f'\n{result.stdout}\n{result.stderr}'
            )

            # Dunno if this is useful or not: when the type checker is happy, also run the stub
            # function to validate runtime types
            runtime_result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                cwd=temp_dir
            )

            assert runtime_result.returncode == 0, (
                f'Runtime validation failed for {stub_function_name}:\n'
                f'{runtime_result.stdout}\n{runtime_result.stderr}'
            )

        else:
            assert result.returncode != 0, (
                f'Type checker should have found type errors in {stub_function_name}'
                f' but did not:\n{result.stdout}\n{result.stderr}'
            )


mypy_checker: tuple[str, ...] = (
    sys.executable,
    '-m',
    'mypy',
    '--strict',
    '--ignore-missing-imports',
)


ty_checker: tuple[str, ...] = (
    'ty',
    'check',
    '--python',
    sys.executable,
    '--ignore',
    'possibly-missing-import',
)


@pytest.mark.parametrize('checker', (ty_checker, mypy_checker))
@pytest.mark.parametrize(
    'stub_function, expected_to_pass',
    (
        (stub_parse_sql_basic, True),
        (stub_parse_sql_empty, True),
        (stub_parser_functions, True),
        (stub_parser_variables, True),
        (stub_prettify_function, True),
        (stub_parse_plpgsql_function, True),
        (stub_ast_fields, True),
        (stub_ast_constructors, True),
        (stub_raw_expression_nodes, True),
        (stub_expression_lists, True),
        (stub_list_valued_node_fields, True),
        (stub_parsed_raw_expressions, True),
        (stub_raw_expression_type_errors, False),
        (stub_expression_list_type_errors, False),
        (stub_adapted_attribute_assignments, True),
        (stub_invalid_attribute_assignment, False),
        (stub_adapted_attribute_read_type_errors, False),
        (stub_empty_raw_statement, True),
        (stub_unchecked_raw_statement_type_errors, False),
        (stub_enums_and_streams, True),
        (stub_public_module_types, True),
        (stub_precedence_types, True),
        (stub_stream_expr_context, True),
        (stub_remaining_importable_modules, True),
        (stub_type_errors, False),
        (stub_ast_field_type_errors, False),
        (stub_ast_constructor_type_errors, False),
        (stub_stream_type_errors, False),
    )
)
def test_type_check(checker, stub_function, expected_to_pass) -> None:
    run_type_checker_on_stub(stub_function, checker, expected_to_pass)
