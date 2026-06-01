# -*- coding: utf-8 -*-
# :Project:   pglast — Type stubs for pglast.visitors module
# :License:   GNU General Public License version 3 or later
#

from collections.abc import Callable, Generator
from typing import Any

from . import ast

NodeOrNodes = ast.Node | tuple[Any, ...]

class ActionMeta(type):
    def __repr__(cls) -> str: ...

class Action(metaclass=ActionMeta):
    def __new__(cls) -> Any: ...

class Add(Action):
    pass

class Continue(Action):
    pass

class Delete(Action):
    pass

class Skip(Action):
    pass

class Ancestor:
    parent: Ancestor | None
    node: Any
    member: str | int | None
    pending_update: Any

    def __init__(
        self,
        parent: Ancestor | None = None,
        node: Any = None,
        member: str | int | None = None,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __getitem__(self, n: int) -> Any: ...
    def __abs__(self) -> Ancestor | None: ...
    def find_nearest(self, cls: type[Any]) -> Ancestor | None: ...
    def __contains__(self, cls: type[Any]) -> bool: ...
    def __truediv__(
        self,
        node_and_member: tuple[Any, str | int | None],
    ) -> Ancestor: ...
    def __matmul__(self, root: Any) -> Any: ...
    def update(self, new_value: Any) -> Ancestor: ...
    def apply(self) -> None: ...

class Visitor:
    root: Any
    visit: Callable[[Ancestor, ast.Node], Any] | None

    def __call__(self, node: NodeOrNodes) -> Any: ...
    def iterate(
        self,
        node: NodeOrNodes,
    ) -> Generator[tuple[Ancestor, ast.Node], Any, None]: ...

class ReferencedRelations(Visitor):
    cte_names: set[str]
    skip_with_clause: Any
    r_names: set[str]

    def __init__(
        self,
        cte_names: set[str] | None = None,
        skip_with_clause: Any = None,
    ) -> None: ...
    def __call__(self, node: NodeOrNodes) -> set[str]: ...
    def visit_DropStmt(self, ancestors: Ancestor, node: ast.DropStmt) -> None: ...
    def visit_SelectStmt(self, ancestors: Ancestor, node: ast.SelectStmt) -> Any: ...
    visit_UpdateStmt: Callable[[Ancestor, ast.UpdateStmt], Any]
    visit_InsertStmt: Callable[[Ancestor, ast.InsertStmt], Any]
    visit_DeleteStmt: Callable[[Ancestor, ast.DeleteStmt], Any]
    def visit_WithClause(self, ancestors: Ancestor, node: ast.WithClause) -> Any: ...
    def visit_RangeVar(self, ancestors: Ancestor, node: ast.RangeVar) -> None: ...

def referenced_relations(stmt: str | NodeOrNodes) -> set[str]: ...
