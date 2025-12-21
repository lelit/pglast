# -*- coding: utf-8 -*-
# :Project:   pglast — Type stubs for pglast.parser module
# :Created:   2025-01-27
# :Author:    Pierce Freeman <hi@pierce.dev>
# :License:   GNU General Public License version 3 or later
#


from typing import Tuple, List, Union, NamedTuple, Optional
from .ast import Node
from .error import Error

class ParseError(Error):
    def __init__(self, message: str, location: Optional[int] = None) -> None: ...

class DeparseError(Error):
    def __init__(self, message: str, location: Optional[int] = None) -> None: ...

class Displacements:
    def __init__(self, s: str) -> None: ...
    def __call__(self, offset: int) -> Optional[int]: ...

class Token(NamedTuple):
    start: int
    end: int
    name: str
    kind: str

def get_postgresql_version() -> Tuple[int, int]: ...

def parse_sql(query: str) -> Tuple[Node, ...]: ...

def parse_sql_json(query: str) -> str: ...

def parse_sql_protobuf(query: str) -> bytes: ...

def parse_plpgsql_json(query: str) -> str: ...

def fingerprint(query: str) -> str: ...

def split(stmts: str, with_parser: bool = True, only_slices: bool = False) -> Tuple[Union[str, slice], ...]: ...

def deparse_protobuf(protobuf: bytes) -> str: ...

def scan(query: str) -> List[Token]: ...
