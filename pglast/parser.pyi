# -*- coding: utf-8 -*-
# :Project:   pglast — Type stubs for pglast.parser module
# :Created:   2025-01-27
# :Author:    Pierce Freeman <hi@pierce.dev>
# :License:   GNU General Public License version 3 or later
#

from typing import Literal, NamedTuple, overload

from .ast import RawStmt
from .error import Error

LONG_MAX: int


LONG_MAX: int


class ParseError(Error):
    def __init__(self, message: str, location: int | None = None) -> None: ...


class DeparseError(Error):
    def __init__(self, message: str, location: int | None = None) -> None: ...


class Displacements:
    def __init__(self, s: str) -> None: ...
    def __call__(self, offset: int) -> int | None: ...


class Token(NamedTuple):
    start: int
    end: int
    name: str
    kind: str


def get_postgresql_version() -> tuple[int, int]: ...

def parse_sql(query: str) -> tuple[RawStmt, ...]: ...

def parse_sql_json(query: str) -> str: ...

def parse_sql_protobuf(query: str) -> bytes: ...

def parse_plpgsql_json(query: str) -> str: ...

def fingerprint(query: str) -> str: ...

@overload
def split(
    stmts: str,
    with_parser: bool = True,
    only_slices: Literal[False] = False,
) -> tuple[str, ...]: ...

@overload
def split(
    stmts: str,
    with_parser: bool = True,
    *,
    only_slices: Literal[True],
) -> tuple[slice, ...]: ...

@overload
def split(
    stmts: str,
    with_parser: bool,
    only_slices: Literal[True],
) -> tuple[slice, ...]: ...

@overload
def split(
    stmts: str,
    with_parser: bool = True,
    *,
    only_slices: bool,
) -> tuple[str | slice, ...]: ...

@overload
def split(
    stmts: str,
    with_parser: bool,
    only_slices: bool = False,
) -> tuple[str | slice, ...]: ...

def deparse_protobuf(
    protobuf: bytes,
    pretty_print: bool = False,
    indent_size: int = 4,
    max_line_length: int = 80,
    trailing_newline: bool = False,
    commas_start_of_line: bool = False,
) -> str: ...

def scan(query: str) -> list[Token]: ...

class Comment(NamedTuple):
    match_location: int
    newlines_before_comment: int
    newlines_after_comment: int
    str: str

def comments(query: str) -> tuple[Comment, ...]: ...
