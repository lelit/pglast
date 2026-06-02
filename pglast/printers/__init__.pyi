# -*- coding: utf-8 -*-
# :Project:   pglast — Type stubs for pglast.printers package
# :License:   GNU General Public License version 3 or later
#

from collections.abc import Callable, Sequence
from enum import IntEnum
from typing import Any, Generic, TypeVar, overload

from .. import ast
from ..error import Error
from ..stream import RawStream
from . import ddl as ddl
from . import dml as dml
from . import sfuncs as sfuncs

Printer = Callable[..., Any]
PrinterKey = type[ast.Node] | tuple[type[ast.Node] | None, type[ast.Node]]
_T = TypeVar("_T")
_EnumT = TypeVar("_EnumT", bound=IntEnum)

NODE_PRINTERS: dict[PrinterKey, Printer]
SPECIAL_FUNCTIONS: dict[str, Printer]

class PrinterAlreadyPresentError(Error):
    pass

def get_printer_for_node(node: ast.Node) -> Printer: ...
def node_printer(
    *nodes: type[ast.Node] | Sequence[type[ast.Node]],
    override: bool = False,
) -> Callable[[Printer], Printer]: ...
def special_function(
    name: str,
    override: bool = False,
) -> Callable[[Printer], Printer]: ...
@overload
def get_special_function(name: str) -> Printer | None: ...
@overload
def get_special_function(name: str, default: _T) -> Printer | _T: ...

class IntEnumPrinter(Generic[_EnumT]):
    value_to_symbol: dict[int, str]

    def __init__(self) -> None: ...
    def __call__(
        self,
        value: _EnumT | ast.Integer | str | None,
        node: ast.Node,
        output: RawStream,
    ) -> None: ...

def get_string_value(lst: Sequence[ast.String]) -> str: ...
