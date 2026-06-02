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
    node: ast.Node = stmt.stmt
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
                cwd=temp_dir,
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
        (stub_prettify_function, True),
        (stub_parse_plpgsql_function, True),
        (stub_ast_fields, True),
        (stub_ast_constructors, True),
        (stub_enums_and_streams, True),
        (stub_public_module_types, True),
        (stub_remaining_importable_modules, True),
        (stub_type_errors, False),
        (stub_ast_field_type_errors, False),
        (stub_ast_constructor_type_errors, False),
        (stub_stream_type_errors, False),
    )
)
def test_type_check(checker, stub_function, expected_to_pass) -> None:
    run_type_checker_on_stub(stub_function, checker, expected_to_pass)
