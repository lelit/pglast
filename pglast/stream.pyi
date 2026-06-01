# -*- coding: utf-8 -*-
# :Project:   pglast — Type stubs for pglast.stream module
# :License:   GNU General Public License version 3 or later
#

from collections.abc import Callable, Iterable, Sequence
from contextlib import AbstractContextManager
from io import StringIO
from re import Match
from typing import Any, TextIO

from . import Comment
from . import ast

SQLInput = str | ast.Node | tuple[ast.Node, ...]
Printer = Callable[..., Any]

is_simple_name: Callable[[str], Match[str] | None]

def maybe_double_quote_name(name: str) -> str: ...

class OutputStream(StringIO):
    pending_separator: bool
    last_emitted_char: str

    def __init__(self) -> None: ...
    def show(self, where: TextIO = ...) -> None: ...
    def separator(self) -> None: ...
    def maybe_write_space(
        self,
        nextc: str | None = None,
        _special_chars: set[str] = ...,
    ) -> int: ...
    def write(self, s: str, /) -> int: ...
    def writes(self, s: str) -> int: ...
    def swrite(self, s: str) -> int: ...
    def swrites(self, s: str) -> int: ...

class RawStream(OutputStream):
    current_column: int
    separate_statements: int
    special_functions: bool
    comma_at_eoln: bool
    semicolon_after_last_statement: bool
    comments: list[Comment] | None
    remove_pg_catalog_from_functions: bool

    def __init__(
        self,
        separate_statements: int = 1,
        special_functions: bool = False,
        comma_at_eoln: bool = False,
        semicolon_after_last_statement: bool = False,
        comments: list[Comment] | None = None,
        remove_pg_catalog_from_functions: bool = False,
    ) -> None: ...
    def show(self, where: TextIO = ...) -> None: ...
    def __call__(self, sql: SQLInput, plpgsql: bool = False) -> str: ...
    def dedent(self) -> None: ...
    def get_printer_for_function(self, name: str) -> Printer | None: ...
    def indent(self, amount: int = 0, relative: bool = True) -> None: ...
    def newline(self) -> None: ...
    def space(self, count: int = 1, force: bool = False) -> None: ...
    def push_indent(
        self,
        amount: int = 0,
        relative: bool = True,
    ) -> AbstractContextManager[None]: ...
    def expression(self, need_parens: bool) -> AbstractContextManager[None]: ...
    def write_quoted_string(self, s: str) -> None: ...
    def print_comment(self, comment: Comment) -> None: ...
    def print_name(self, nodes: Any, sep: str = ".") -> None: ...
    def print_symbol(self, nodes: Any, sep: str = ".") -> None: ...
    def print_node(
        self,
        node: Any,
        is_name: bool = False,
        is_symbol: bool = False,
    ) -> None: ...
    def print_list(
        self,
        nodes: Sequence[Any],
        sep: str = ",",
        relative_indent: int | None = None,
        standalone_items: bool | None = None,
        are_names: bool = False,
        is_symbol: bool = False,
        item_needs_parens: Callable[[Any], bool] | None = None,
    ) -> None: ...
    def print_lists(
        self,
        lists: Iterable[Sequence[Any]],
        sep: str = ",",
        relative_indent: int | None = None,
        standalone_items: bool | None = None,
        are_names: bool = False,
        sublist_open: str = "(",
        sublist_close: str = ")",
        sublist_sep: str = ",",
        sublist_relative_indent: int | None = None,
    ) -> None: ...

class IndentedStream(RawStream):
    compact_lists_margin: int | None
    split_string_literals_threshold: int | None
    current_indent: int
    indentation_stack: list[int]

    def __init__(
        self,
        compact_lists_margin: int | None = None,
        split_string_literals_threshold: int | None = None,
        **options: Any,
    ) -> None: ...
    def show(self, where: TextIO = ...) -> None: ...
    def dedent(self) -> None: ...
    def indent(self, amount: int = 0, relative: bool = True) -> None: ...
    def push_indent(
        self,
        amount: int = 0,
        relative: bool = True,
    ) -> AbstractContextManager[None]: ...
    def newline(self) -> None: ...
    def space(self, count: int = 1, force: bool = False) -> None: ...
    def print_comment(self, comment: Comment) -> None: ...
    def print_list(
        self,
        nodes: Sequence[Any],
        sep: str = ",",
        relative_indent: int | None = None,
        standalone_items: bool | None = None,
        are_names: bool = False,
        is_symbol: bool = False,
        item_needs_parens: Callable[[Any], bool] | None = None,
    ) -> None: ...
    def write_quoted_string(self, s: str) -> None: ...
    def write(self, s: str, /) -> int: ...
