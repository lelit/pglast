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
    from typing import Union
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
    statements: tuple[Union[str, slice], ...] = split('SELECT 1; SELECT 2;')
    assert isinstance(statements, tuple), f'Expected tuple, got {type(statements)}'
    assert len(statements) == 2, f'Expected 2 statements, got {len(statements)}'
    first_stmt: Union[str, slice] = statements[0]
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


def stub_type_errors() -> None:
    """
    Stub function that should cause type checker errors.
    """
    from pglast import parse_sql

    query: str = 'SELECT 1'
    # Intentional error, to assert that the type checker is not cheating
    wrong_type: int = parse_sql(query)


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
        (stub_type_errors, False),
    )
)
def test_type_check(checker, stub_function, expected_to_pass) -> None:
    run_type_checker_on_stub(stub_function, checker, expected_to_pass)
