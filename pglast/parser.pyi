# -*- coding: utf-8 -*-
# :Project:   pglast — Type stubs for pglast.parser module
# :Created:   2025-01-27
# :Author:    Pierce Freeman <hi@pierce.dev>
# :License:   GNU General Public License version 3 or later
#

from typing import NamedTuple, Union

from .ast import Node
from .error import Error


class ParseError(Error):
    def __init__(self, message: str, location: Union[int, None] = None) -> None: ...


class DeparseError(Error):
    def __init__(self, message: str, location: Union[int, None] = None) -> None: ...


class Displacements:
    def __init__(self, s: str) -> None: ...
    def __call__(self, offset: int) -> Union[int, None]: ...


class Token(NamedTuple):
    start: int
    end: int
    name: str
    kind: str


def get_postgresql_version() -> tuple[int, int]: ...

def parse_sql(query: str) -> tuple[Node, ...]: ...

def parse_sql_json(query: str) -> str: ...

def parse_sql_protobuf(query: str) -> bytes: ...

def parse_plpgsql_json(query: str) -> str: ...

def fingerprint(query: str) -> str: ...

def split(
    stmts: str,
    with_parser: bool = True,
    only_slices: bool = False
) -> tuple[Union[str, slice], ...]: ...

def deparse_protobuf(protobuf: bytes) -> str: ...

def scan(query: str) -> list[Token]: ...
