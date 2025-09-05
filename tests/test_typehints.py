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
    
    # These should work fine
    first_stmt: Node = result[0]
    stmt_count: int = len(result)


def stub_parse_sql_empty() -> None:
    """Stub function to test parse_sql with empty input."""
    from typing import Tuple
    from pglast import parse_sql
    from pglast.ast import Node
    
    empty_query: str = ""
    empty_result: Tuple[Node, ...] = parse_sql(empty_query)
    
    # Should be empty tuple
    count: int = len(empty_result)


def stub_parser_functions() -> None:
    """Stub function to test other parser function type hints."""
    from typing import Tuple, List
    from pglast.parser import get_postgresql_version, fingerprint, scan, split, Token
    
    query: str = "SELECT name FROM users WHERE id = 1"
    
    # Test get_postgresql_version
    version: Tuple[int, int] = get_postgresql_version()
    major: int = version[0]
    minor: int = version[1]
    
    # Test fingerprint
    fp: str = fingerprint(query)
    fp_length: int = len(fp)
    
    # Test scan
    tokens: List[Token] = scan(query)
    first_token: Token = tokens[0]
    token_start: int = first_token.start
    
    # Test split
    statements: Tuple[str, ...] = split("SELECT 1; SELECT 2;")
    first_stmt: str = statements[0]


def stub_prettify_function() -> None:
    """Stub function to test prettify type hints."""
    from pglast import prettify
    
    query: str = "select   1"
    
    # Test basic prettify
    pretty: str = prettify(query)
    pretty_length: int = len(pretty)
    
    # Test with options
    pretty_with_options: str = prettify(query, safety_belt=True, preserve_comments=False)


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
    first_item: Dict[str, Any] = result[0]


def stub_type_errors() -> None:
    """Stub function that should cause mypy errors - used to test that mypy is working."""
    from pglast import parse_sql
    
    query: str = "SELECT 1"
    # This should cause a mypy error - assigning tuple to int
    wrong_type: int = parse_sql(query)  # type: ignore


def _run_mypy_on_stub(stub_function, should_pass: bool = True) -> None:
    """
    Helper function to run mypy on a stub function.
    
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
            # Run mypy with explicit file path and follow-imports=silent to avoid scanning pglast source
            result = subprocess.run(
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
                assert result.returncode == 0, f"mypy found unexpected type errors in {stub_function.__name__}:\n{result.stdout}\n{result.stderr}"
            else:
                assert result.returncode != 0, f"mypy should have found type errors in {stub_function.__name__} but didn't:\n{result.stdout}\n{result.stderr}"
                
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
