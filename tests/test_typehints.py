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
    from typing import Tuple
    from pglast import parse_sql
    from pglast.ast import Node

    query: str = "SELECT 1"
    result: Tuple[Node, ...] = parse_sql(query)

    # Runtime type checks
    assert isinstance(result, tuple), f"Expected tuple, got {type(result)}"
    assert len(result) > 0, "Expected non-empty result"
    assert isinstance(result[0], Node), f"Expected Node, got {type(result[0])}"

    # These should work fine
    first_stmt: Node = result[0]
    stmt_count: int = len(result)
    assert isinstance(stmt_count, int), f"Expected int, got {type(stmt_count)}"


def stub_parse_sql_empty() -> None:
    """Stub function to test parse_sql with empty input."""
    from typing import Tuple
    from pglast import parse_sql
    from pglast.ast import Node

    empty_query: str = ""
    empty_result: Tuple[Node, ...] = parse_sql(empty_query)

    # Runtime type checks
    assert isinstance(empty_result, tuple), f"Expected tuple, got {type(empty_result)}"
    assert len(empty_result) == 0, f"Expected empty tuple, got {len(empty_result)} items"

    # Should be empty tuple
    count: int = len(empty_result)
    assert isinstance(count, int), f"Expected int, got {type(count)}"
    assert count == 0, f"Expected 0, got {count}"


def stub_parser_functions() -> None:
    """Stub function to test other parser function type hints."""
    from typing import Tuple, List
    from pglast.parser import get_postgresql_version, fingerprint, scan, split, Token

    query: str = "SELECT name FROM users WHERE id = 1"

    # Test get_postgresql_version
    version: Tuple[int, int] = get_postgresql_version()
    assert isinstance(version, tuple), f"Expected tuple, got {type(version)}"
    assert len(version) == 2, f"Expected tuple of length 2, got {len(version)}"
    major: int = version[0]
    minor: int = version[1]
    assert isinstance(major, int), f"Expected int, got {type(major)}"
    assert isinstance(minor, int), f"Expected int, got {type(minor)}"

    # Test fingerprint
    fp: str = fingerprint(query)
    assert isinstance(fp, str), f"Expected str, got {type(fp)}"
    fp_length: int = len(fp)
    assert isinstance(fp_length, int), f"Expected int, got {type(fp_length)}"

    # Test scan
    tokens: List[Token] = scan(query)
    assert isinstance(tokens, list), f"Expected list, got {type(tokens)}"
    assert len(tokens) > 0, "Expected non-empty token list"
    first_token: Token = tokens[0]
    assert isinstance(first_token, Token), f"Expected Token, got {type(first_token)}"
    token_start: int = first_token.start
    assert isinstance(token_start, int), f"Expected int, got {type(token_start)}"

    # Test split
    statements: Tuple[str, ...] = split("SELECT 1; SELECT 2;")
    assert isinstance(statements, tuple), f"Expected tuple, got {type(statements)}"
    assert len(statements) == 2, f"Expected 2 statements, got {len(statements)}"
    first_stmt: str = statements[0]
    assert isinstance(first_stmt, str), f"Expected str, got {type(first_stmt)}"


def stub_prettify_function() -> None:
    """Stub function to test prettify type hints."""
    from pglast import prettify

    query: str = "select 1"

    # Test basic prettify
    pretty: str = prettify(query)
    assert isinstance(pretty, str), f"Expected str, got {type(pretty)}"
    pretty_length: int = len(pretty)
    assert isinstance(pretty_length, int), f"Expected int, got {type(pretty_length)}"

    # Test with options
    pretty_with_options: str = prettify(query, safety_belt=True, preserve_comments=False)
    assert isinstance(pretty_with_options, str), f"Expected str, got {type(pretty_with_options)}"


def stub_parse_plpgsql_function() -> None:
    """Stub function to test parse_plpgsql type hints."""
    from typing import List, Dict, Any
    from pglast import parse_plpgsql

    plpgsql_stmt: str = '''
    CREATE FUNCTION add (a integer, b integer)
    RETURNS integer AS $$
    BEGIN
      RETURN a + b;
    END;
    $$ LANGUAGE plpgsql
    '''

    result: List[Dict[str, Any]] = parse_plpgsql(plpgsql_stmt)
    assert isinstance(result, list), f"Expected list, got {type(result)}"
    assert len(result) > 0, "Expected non-empty result"
    first_item: Dict[str, Any] = result[0]
    assert isinstance(first_item, dict), f"Expected dict, got {type(first_item)}"


def stub_type_errors() -> None:
    """Stub function that should cause mypy errors - used to test that mypy is working."""
    from pglast import parse_sql

    query: str = "SELECT 1"
    # This should cause a mypy error - assigning tuple to int
    wrong_type: int = parse_sql(query)  # type: ignore


def _run_mypy_on_stub(stub_function, should_pass: bool = True) -> None:
    """
    Helper function to run mypy on a stub function and execute it for runtime validation.

    Args:
        stub_function: The stub function to test
        should_pass: Whether mypy should pass (True) or fail (False)
    """
    import tempfile
    import os
    import inspect

    # Get the source code of the stub function
    source = inspect.getsource(stub_function)

    # Create the full test file content
    test_code = f'''# Test file for mypy validation
{source}

if __name__ == "__main__":
    {stub_function.__name__}()
'''

    # Create a temporary directory to isolate the test
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = os.path.join(temp_dir, f"{stub_function.__name__}.py")

        with open(temp_file, 'w') as f:
            f.write(test_code)

        try:
            # First, run mypy type checking
            mypy_result = subprocess.run(
                [sys.executable, '-m', 'mypy',
                 '--ignore-missing-imports',
                 '--strict',
                 '--follow-imports=silent',
                 '--no-site-packages',
                 temp_file],
                capture_output=True,
                text=True,
                cwd=temp_dir  # Run from temp directory
            )

            if should_pass:
                assert mypy_result.returncode == 0, (
                    f"mypy found unexpected type errors in {stub_function.__name__}:"
                    f"\n{mypy_result.stdout}\n{mypy_result.stderr}"
                )

                # If mypy passes, also run the stub function to validate runtime types
                runtime_result = subprocess.run(
                    [sys.executable, temp_file],
                    capture_output=True,
                    text=True,
                    cwd=temp_dir
                )

                assert runtime_result.returncode == 0, (
                    f"Runtime validation failed for {stub_function.__name__}:\n"
                    f"{runtime_result.stdout}\n{runtime_result.stderr}"
                )

            else:
                assert mypy_result.returncode != 0, (
                    f"mypy should have found type errors in {stub_function.__name__}"
                    f" but didn't:\n{mypy_result.stdout}\n{mypy_result.stderr}"
                )

        except FileNotFoundError:
            pytest.skip("mypy not available")


def test_mypy_parse_sql_basic() -> None:
    """Test mypy validation for basic parse_sql usage."""
    _run_mypy_on_stub(stub_parse_sql_basic)


def test_mypy_parse_sql_empty() -> None:
    """Test mypy validation for parse_sql with empty input."""
    _run_mypy_on_stub(stub_parse_sql_empty)


def test_mypy_parser_functions() -> None:
    """Test mypy validation for other parser functions."""
    _run_mypy_on_stub(stub_parser_functions)


def test_mypy_prettify_function() -> None:
    """Test mypy validation for prettify function."""
    _run_mypy_on_stub(stub_prettify_function)


def test_mypy_parse_plpgsql_function() -> None:
    """Test mypy validation for parse_plpgsql function."""
    _run_mypy_on_stub(stub_parse_plpgsql_function)


def test_mypy_detects_type_errors() -> None:
    """Test that mypy properly detects type errors."""
    _run_mypy_on_stub(stub_type_errors, should_pass=False)
