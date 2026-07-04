# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: type stubs automatically extracted from struct_defs.json @ 18-latest-0-g6ced8d4
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021-2026 Lele Gaifax
#

from collections.abc import Callable, Iterator
from decimal import Decimal

from typing import Any, NamedTuple, overload

from . import enums


class SlotTypeInfo(NamedTuple):
    c_type: str
    py_type: Any
    adaptor: Callable[[Any], Any] | None


class __Omissis:
    def __eq__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...


Omissis: __Omissis


class Node:
    ancestors: Any
    _ATTRS_TO_IGNORE_IN_COMPARISON: set[str]

    def __init__(self, data: dict[str, Any]) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __call__(
        self,
        depth: int | None = None,
        ellipsis: Any = ...,
        skip_none: bool = False,
    ) -> dict[str, Any]: ...
    def __setattr__(self, name: str, value: Any) -> None: ...


class Expr(Node):
    pass


_NodePayload = dict[str, Any]
_ListInput = list[Any] | tuple[Any, ...]
_BitmapsetInput = set[int] | list[int] | tuple[int, ...]
_CharInput = str | int
_FloatStringInput = str | int | float | Decimal


class ATAlterConstraint(Node):
    conname: str | None
    alterEnforceability: bool | None
    is_enforced: bool | None
    alterDeferrability: bool | None
    deferrable: bool | None
    initdeferred: bool | None
    alterInheritability: bool | None
    noinherit: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, conname: str | None = None, alterEnforceability: bool | int | None = None, is_enforced: bool | int | None = None, alterDeferrability: bool | int | None = None, deferrable: bool | int | None = None, initdeferred: bool | int | None = None, alterInheritability: bool | int | None = None, noinherit: bool | int | None = None) -> None: ...  # noqa: E501


class A_ArrayExpr(Node):
    elements: tuple[Any, ...] | None
    list_start: int | None
    list_end: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, elements: _ListInput | None = None, list_start: int | None = None, list_end: int | None = None, location: int | None = None) -> None: ...  # noqa: E501



class ValUnion(Node):
    val: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, value: Node | None = None) -> None: ...


class A_Const(Node):
    isnull: bool | None
    val: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, isnull: bool | int | None = None, val: Node | None = None) -> None: ...  # noqa: E501


class A_Expr(Node):
    kind: enums.A_Expr_Kind | None
    name: tuple[Any, ...] | None
    lexpr: Node | None
    rexpr: Node | None
    rexpr_list_start: int | None
    rexpr_list_end: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.A_Expr_Kind | int | str | dict[str, Any] | None = None, name: _ListInput | None = None, lexpr: Node | _NodePayload | None = None, rexpr: Node | _NodePayload | None = None, rexpr_list_start: int | None = None, rexpr_list_end: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class A_Indices(Node):
    is_slice: bool | None
    lidx: Node | None
    uidx: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, is_slice: bool | int | None = None, lidx: Node | _NodePayload | None = None, uidx: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class A_Indirection(Node):
    arg: Node | None
    indirection: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Node | _NodePayload | None = None, indirection: _ListInput | None = None) -> None: ...  # noqa: E501


class A_Star(Node):
    def __init__(self) -> None: ...


class AccessPriv(Node):
    priv_name: str | None
    cols: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, priv_name: str | None = None, cols: _ListInput | None = None) -> None: ...  # noqa: E501


class Aggref(Expr):
    aggargtypes: tuple[Any, ...] | None
    aggdirectargs: tuple[Any, ...] | None
    args: tuple[Any, ...] | None
    aggorder: tuple[Any, ...] | None
    aggdistinct: tuple[Any, ...] | None
    aggfilter: Expr | None
    aggstar: bool | None
    aggvariadic: bool | None
    aggkind: str | None
    agglevelsup: int | None
    aggsplit: enums.AggSplit | None
    aggno: int | None
    aggtransno: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, aggargtypes: _ListInput | None = None, aggdirectargs: _ListInput | None = None, args: _ListInput | None = None, aggorder: _ListInput | None = None, aggdistinct: _ListInput | None = None, aggfilter: Expr | _NodePayload | None = None, aggstar: bool | int | None = None, aggvariadic: bool | int | None = None, aggkind: _CharInput | None = None, agglevelsup: int | None = None, aggsplit: enums.AggSplit | int | str | dict[str, Any] | None = None, aggno: int | None = None, aggtransno: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class Alias(Node):
    aliasname: str | None
    colnames: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, aliasname: str | None = None, colnames: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterCollationStmt(Node):
    collname: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, collname: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterDatabaseRefreshCollStmt(Node):
    dbname: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, dbname: str | None = None) -> None: ...  # noqa: E501


class AlterDatabaseSetStmt(Node):
    dbname: str | None
    setstmt: VariableSetStmt | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, dbname: str | None = None, setstmt: VariableSetStmt | _NodePayload | None = None) -> None: ...  # noqa: E501


class AlterDatabaseStmt(Node):
    dbname: str | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, dbname: str | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterDefaultPrivilegesStmt(Node):
    options: tuple[Any, ...] | None
    action: GrantStmt | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, options: _ListInput | None = None, action: GrantStmt | _NodePayload | None = None) -> None: ...  # noqa: E501


class AlterDomainStmt(Node):
    subtype: str | None
    typeName: tuple[Any, ...] | None
    name: str | None
    def_: Node | None
    behavior: enums.DropBehavior | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, subtype: _CharInput | None = None, typeName: _ListInput | None = None, name: str | None = None, def_: Node | _NodePayload | None = None, behavior: enums.DropBehavior | int | str | dict[str, Any] | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class AlterEnumStmt(Node):
    typeName: tuple[Any, ...] | None
    oldVal: str | None
    newVal: str | None
    newValNeighbor: str | None
    newValIsAfter: bool | None
    skipIfNewValExists: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, typeName: _ListInput | None = None, oldVal: str | None = None, newVal: str | None = None, newValNeighbor: str | None = None, newValIsAfter: bool | int | None = None, skipIfNewValExists: bool | int | None = None) -> None: ...  # noqa: E501


class AlterEventTrigStmt(Node):
    trigname: str | None
    tgenabled: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, trigname: str | None = None, tgenabled: _CharInput | None = None) -> None: ...  # noqa: E501


class AlterExtensionContentsStmt(Node):
    extname: str | None
    action: int | None
    objtype: enums.ObjectType | None
    object: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, extname: str | None = None, action: int | None = None, objtype: enums.ObjectType | int | str | dict[str, Any] | None = None, object: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class AlterExtensionStmt(Node):
    extname: str | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, extname: str | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterFdwStmt(Node):
    fdwname: str | None
    func_options: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, fdwname: str | None = None, func_options: _ListInput | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterForeignServerStmt(Node):
    servername: str | None
    version: str | None
    options: tuple[Any, ...] | None
    has_version: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, servername: str | None = None, version: str | None = None, options: _ListInput | None = None, has_version: bool | int | None = None) -> None: ...  # noqa: E501


class AlterFunctionStmt(Node):
    objtype: enums.ObjectType | None
    func: ObjectWithArgs | None
    actions: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, objtype: enums.ObjectType | int | str | dict[str, Any] | None = None, func: ObjectWithArgs | _NodePayload | None = None, actions: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterObjectDependsStmt(Node):
    objectType: enums.ObjectType | None
    relation: RangeVar | None
    object: Node | None
    extname: String | None
    remove: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, objectType: enums.ObjectType | int | str | dict[str, Any] | None = None, relation: RangeVar | _NodePayload | None = None, object: Node | _NodePayload | None = None, extname: String | _NodePayload | None = None, remove: bool | int | None = None) -> None: ...  # noqa: E501


class AlterObjectSchemaStmt(Node):
    objectType: enums.ObjectType | None
    relation: RangeVar | None
    object: Node | None
    newschema: str | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, objectType: enums.ObjectType | int | str | dict[str, Any] | None = None, relation: RangeVar | _NodePayload | None = None, object: Node | _NodePayload | None = None, newschema: str | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class AlterOpFamilyStmt(Node):
    opfamilyname: tuple[Any, ...] | None
    amname: str | None
    isDrop: bool | None
    items: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, opfamilyname: _ListInput | None = None, amname: str | None = None, isDrop: bool | int | None = None, items: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterOperatorStmt(Node):
    opername: ObjectWithArgs | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, opername: ObjectWithArgs | _NodePayload | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterOwnerStmt(Node):
    objectType: enums.ObjectType | None
    relation: RangeVar | None
    object: Node | None
    newowner: RoleSpec | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, objectType: enums.ObjectType | int | str | dict[str, Any] | None = None, relation: RangeVar | _NodePayload | None = None, object: Node | _NodePayload | None = None, newowner: RoleSpec | _NodePayload | None = None) -> None: ...  # noqa: E501


class AlterPolicyStmt(Node):
    policy_name: str | None
    table: RangeVar | None
    roles: tuple[Any, ...] | None
    qual: Node | None
    with_check: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, policy_name: str | None = None, table: RangeVar | _NodePayload | None = None, roles: _ListInput | None = None, qual: Node | _NodePayload | None = None, with_check: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class AlterPublicationStmt(Node):
    pubname: str | None
    options: tuple[Any, ...] | None
    pubobjects: tuple[Any, ...] | None
    for_all_tables: bool | None
    action: enums.AlterPublicationAction | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, pubname: str | None = None, options: _ListInput | None = None, pubobjects: _ListInput | None = None, for_all_tables: bool | int | None = None, action: enums.AlterPublicationAction | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class AlterRoleSetStmt(Node):
    role: RoleSpec | None
    database: str | None
    setstmt: VariableSetStmt | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, role: RoleSpec | _NodePayload | None = None, database: str | None = None, setstmt: VariableSetStmt | _NodePayload | None = None) -> None: ...  # noqa: E501


class AlterRoleStmt(Node):
    role: RoleSpec | None
    options: tuple[Any, ...] | None
    action: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, role: RoleSpec | _NodePayload | None = None, options: _ListInput | None = None, action: int | None = None) -> None: ...  # noqa: E501


class AlterSeqStmt(Node):
    sequence: RangeVar | None
    options: tuple[Any, ...] | None
    for_identity: bool | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, sequence: RangeVar | _NodePayload | None = None, options: _ListInput | None = None, for_identity: bool | int | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class AlterStatsStmt(Node):
    defnames: tuple[Any, ...] | None
    stxstattarget: Node | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, defnames: _ListInput | None = None, stxstattarget: Node | _NodePayload | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class AlterSubscriptionStmt(Node):
    kind: enums.AlterSubscriptionType | None
    subname: str | None
    conninfo: str | None
    publication: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.AlterSubscriptionType | int | str | dict[str, Any] | None = None, subname: str | None = None, conninfo: str | None = None, publication: _ListInput | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterSystemStmt(Node):
    setstmt: VariableSetStmt | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, setstmt: VariableSetStmt | _NodePayload | None = None) -> None: ...  # noqa: E501


class AlterTSConfigurationStmt(Node):
    kind: enums.AlterTSConfigType | None
    cfgname: tuple[Any, ...] | None
    tokentype: tuple[Any, ...] | None
    dicts: tuple[Any, ...] | None
    override: bool | None
    replace: bool | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.AlterTSConfigType | int | str | dict[str, Any] | None = None, cfgname: _ListInput | None = None, tokentype: _ListInput | None = None, dicts: _ListInput | None = None, override: bool | int | None = None, replace: bool | int | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class AlterTSDictionaryStmt(Node):
    dictname: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, dictname: _ListInput | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterTableCmd(Node):
    subtype: enums.AlterTableType | None
    name: str | None
    num: int | None
    newowner: RoleSpec | None
    def_: Node | None
    behavior: enums.DropBehavior | None
    missing_ok: bool | None
    recurse: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, subtype: enums.AlterTableType | int | str | dict[str, Any] | None = None, name: str | None = None, num: int | None = None, newowner: RoleSpec | _NodePayload | None = None, def_: Node | _NodePayload | None = None, behavior: enums.DropBehavior | int | str | dict[str, Any] | None = None, missing_ok: bool | int | None = None, recurse: bool | int | None = None) -> None: ...  # noqa: E501


class AlterTableMoveAllStmt(Node):
    orig_tablespacename: str | None
    objtype: enums.ObjectType | None
    roles: tuple[Any, ...] | None
    new_tablespacename: str | None
    nowait: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, orig_tablespacename: str | None = None, objtype: enums.ObjectType | int | str | dict[str, Any] | None = None, roles: _ListInput | None = None, new_tablespacename: str | None = None, nowait: bool | int | None = None) -> None: ...  # noqa: E501


class AlterTableSpaceOptionsStmt(Node):
    tablespacename: str | None
    options: tuple[Any, ...] | None
    isReset: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, tablespacename: str | None = None, options: _ListInput | None = None, isReset: bool | int | None = None) -> None: ...  # noqa: E501


class AlterTableStmt(Node):
    relation: RangeVar | None
    cmds: tuple[Any, ...] | None
    objtype: enums.ObjectType | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, cmds: _ListInput | None = None, objtype: enums.ObjectType | int | str | dict[str, Any] | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class AlterTypeStmt(Node):
    typeName: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, typeName: _ListInput | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class AlterUserMappingStmt(Node):
    user: RoleSpec | None
    servername: str | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, user: RoleSpec | _NodePayload | None = None, servername: str | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class AlternativeSubPlan(Expr):
    subplans: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, subplans: _ListInput | None = None) -> None: ...  # noqa: E501


class ArrayCoerceExpr(Expr):
    arg: Expr | None
    elemexpr: Expr | None
    resulttypmod: int | None
    coerceformat: enums.CoercionForm | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, elemexpr: Expr | _NodePayload | None = None, resulttypmod: int | None = None, coerceformat: enums.CoercionForm | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class ArrayExpr(Expr):
    elements: tuple[Any, ...] | None
    multidims: bool | None
    list_start: int | None
    list_end: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, elements: _ListInput | None = None, multidims: bool | int | None = None, list_start: int | None = None, list_end: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class BitString(Node):
    bsval: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, bsval: str | None = None) -> None: ...  # noqa: E501


class BoolExpr(Expr):
    boolop: enums.BoolExprType | None
    args: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, boolop: enums.BoolExprType | int | str | dict[str, Any] | None = None, args: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class Boolean(Node):
    boolval: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, boolval: bool | int | None = None) -> None: ...  # noqa: E501


class BooleanTest(Expr):
    arg: Expr | None
    booltesttype: enums.BoolTestType | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, booltesttype: enums.BoolTestType | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CTECycleClause(Node):
    cycle_col_list: tuple[Any, ...] | None
    cycle_mark_column: str | None
    cycle_mark_value: Node | None
    cycle_mark_default: Node | None
    cycle_path_column: str | None
    location: int | None
    cycle_mark_typmod: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, cycle_col_list: _ListInput | None = None, cycle_mark_column: str | None = None, cycle_mark_value: Node | _NodePayload | None = None, cycle_mark_default: Node | _NodePayload | None = None, cycle_path_column: str | None = None, location: int | None = None, cycle_mark_typmod: int | None = None) -> None: ...  # noqa: E501


class CTESearchClause(Node):
    search_col_list: tuple[Any, ...] | None
    search_breadth_first: bool | None
    search_seq_column: str | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, search_col_list: _ListInput | None = None, search_breadth_first: bool | int | None = None, search_seq_column: str | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CallContext(Node):
    atomic: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, atomic: bool | int | None = None) -> None: ...  # noqa: E501


class CallStmt(Node):
    funccall: FuncCall | None
    funcexpr: FuncExpr | None
    outargs: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, funccall: FuncCall | _NodePayload | None = None, funcexpr: FuncExpr | _NodePayload | None = None, outargs: _ListInput | None = None) -> None: ...  # noqa: E501


class CaseExpr(Expr):
    arg: Expr | None
    args: tuple[Any, ...] | None
    defresult: Expr | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, args: _ListInput | None = None, defresult: Expr | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CaseTestExpr(Expr):
    typeMod: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, typeMod: int | None = None) -> None: ...  # noqa: E501


class CaseWhen(Expr):
    expr: Expr | None
    result: Expr | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, expr: Expr | _NodePayload | None = None, result: Expr | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CheckPointStmt(Node):
    def __init__(self) -> None: ...


class ClosePortalStmt(Node):
    portalname: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, portalname: str | None = None) -> None: ...  # noqa: E501


class ClusterStmt(Node):
    relation: RangeVar | None
    indexname: str | None
    params: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, indexname: str | None = None, params: _ListInput | None = None) -> None: ...  # noqa: E501


class CoalesceExpr(Expr):
    args: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, args: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CoerceToDomain(Expr):
    arg: Expr | None
    resulttypmod: int | None
    coercionformat: enums.CoercionForm | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, resulttypmod: int | None = None, coercionformat: enums.CoercionForm | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CoerceToDomainValue(Expr):
    typeMod: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, typeMod: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CoerceViaIO(Expr):
    arg: Expr | None
    coerceformat: enums.CoercionForm | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, coerceformat: enums.CoercionForm | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CollateClause(Node):
    arg: Node | None
    collname: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Node | _NodePayload | None = None, collname: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CollateExpr(Expr):
    arg: Expr | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class ColumnDef(Node):
    colname: str | None
    typeName: TypeName | None
    compression: str | None
    inhcount: int | None
    is_local: bool | None
    is_not_null: bool | None
    is_from_type: bool | None
    storage: str | None
    storage_name: str | None
    raw_default: Node | None
    cooked_default: Node | None
    identity: str | None
    identitySequence: RangeVar | None
    generated: str | None
    collClause: CollateClause | None
    constraints: tuple[Any, ...] | None
    fdwoptions: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, colname: str | None = None, typeName: TypeName | _NodePayload | None = None, compression: str | None = None, inhcount: int | None = None, is_local: bool | int | None = None, is_not_null: bool | int | None = None, is_from_type: bool | int | None = None, storage: _CharInput | None = None, storage_name: str | None = None, raw_default: Node | _NodePayload | None = None, cooked_default: Node | _NodePayload | None = None, identity: _CharInput | None = None, identitySequence: RangeVar | _NodePayload | None = None, generated: _CharInput | None = None, collClause: CollateClause | _NodePayload | None = None, constraints: _ListInput | None = None, fdwoptions: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class ColumnRef(Node):
    fields: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, fields: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CommentStmt(Node):
    objtype: enums.ObjectType | None
    object: Node | None
    comment: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, objtype: enums.ObjectType | int | str | dict[str, Any] | None = None, object: Node | _NodePayload | None = None, comment: str | None = None) -> None: ...  # noqa: E501


class CommonTableExpr(Node):
    ctename: str | None
    aliascolnames: tuple[Any, ...] | None
    ctematerialized: enums.CTEMaterialize | None
    ctequery: Node | None
    search_clause: CTESearchClause | None
    cycle_clause: CTECycleClause | None
    location: int | None
    cterecursive: bool | None
    cterefcount: int | None
    ctecolnames: tuple[Any, ...] | None
    ctecoltypes: tuple[Any, ...] | None
    ctecoltypmods: tuple[Any, ...] | None
    ctecolcollations: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, ctename: str | None = None, aliascolnames: _ListInput | None = None, ctematerialized: enums.CTEMaterialize | int | str | dict[str, Any] | None = None, ctequery: Node | _NodePayload | None = None, search_clause: CTESearchClause | _NodePayload | None = None, cycle_clause: CTECycleClause | _NodePayload | None = None, location: int | None = None, cterecursive: bool | int | None = None, cterefcount: int | None = None, ctecolnames: _ListInput | None = None, ctecoltypes: _ListInput | None = None, ctecoltypmods: _ListInput | None = None, ctecolcollations: _ListInput | None = None) -> None: ...  # noqa: E501


class CompositeTypeStmt(Node):
    typevar: RangeVar | None
    coldeflist: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, typevar: RangeVar | _NodePayload | None = None, coldeflist: _ListInput | None = None) -> None: ...  # noqa: E501


class Constraint(Node):
    contype: enums.ConstrType | None
    conname: str | None
    deferrable: bool | None
    initdeferred: bool | None
    is_enforced: bool | None
    skip_validation: bool | None
    initially_valid: bool | None
    is_no_inherit: bool | None
    raw_expr: Node | None
    cooked_expr: str | None
    generated_when: str | None
    generated_kind: str | None
    nulls_not_distinct: bool | None
    keys: tuple[Any, ...] | None
    without_overlaps: bool | None
    including: tuple[Any, ...] | None
    exclusions: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    indexname: str | None
    indexspace: str | None
    reset_default_tblspc: bool | None
    access_method: str | None
    where_clause: Node | None
    pktable: RangeVar | None
    fk_attrs: tuple[Any, ...] | None
    pk_attrs: tuple[Any, ...] | None
    fk_with_period: bool | None
    pk_with_period: bool | None
    fk_matchtype: str | None
    fk_upd_action: str | None
    fk_del_action: str | None
    fk_del_set_cols: tuple[Any, ...] | None
    old_conpfeqop: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, contype: enums.ConstrType | int | str | dict[str, Any] | None = None, conname: str | None = None, deferrable: bool | int | None = None, initdeferred: bool | int | None = None, is_enforced: bool | int | None = None, skip_validation: bool | int | None = None, initially_valid: bool | int | None = None, is_no_inherit: bool | int | None = None, raw_expr: Node | _NodePayload | None = None, cooked_expr: str | None = None, generated_when: _CharInput | None = None, generated_kind: _CharInput | None = None, nulls_not_distinct: bool | int | None = None, keys: _ListInput | None = None, without_overlaps: bool | int | None = None, including: _ListInput | None = None, exclusions: _ListInput | None = None, options: _ListInput | None = None, indexname: str | None = None, indexspace: str | None = None, reset_default_tblspc: bool | int | None = None, access_method: str | None = None, where_clause: Node | _NodePayload | None = None, pktable: RangeVar | _NodePayload | None = None, fk_attrs: _ListInput | None = None, pk_attrs: _ListInput | None = None, fk_with_period: bool | int | None = None, pk_with_period: bool | int | None = None, fk_matchtype: _CharInput | None = None, fk_upd_action: _CharInput | None = None, fk_del_action: _CharInput | None = None, fk_del_set_cols: _ListInput | None = None, old_conpfeqop: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class ConstraintsSetStmt(Node):
    constraints: tuple[Any, ...] | None
    deferred: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, constraints: _ListInput | None = None, deferred: bool | int | None = None) -> None: ...  # noqa: E501


class ConvertRowtypeExpr(Expr):
    arg: Expr | None
    convertformat: enums.CoercionForm | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, convertformat: enums.CoercionForm | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class CopyStmt(Node):
    relation: RangeVar | None
    query: Node | None
    attlist: tuple[Any, ...] | None
    is_from: bool | None
    is_program: bool | None
    filename: str | None
    options: tuple[Any, ...] | None
    whereClause: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, query: Node | _NodePayload | None = None, attlist: _ListInput | None = None, is_from: bool | int | None = None, is_program: bool | int | None = None, filename: str | None = None, options: _ListInput | None = None, whereClause: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class CreateAmStmt(Node):
    amname: str | None
    handler_name: tuple[Any, ...] | None
    amtype: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, amname: str | None = None, handler_name: _ListInput | None = None, amtype: _CharInput | None = None) -> None: ...  # noqa: E501


class CreateCastStmt(Node):
    sourcetype: TypeName | None
    targettype: TypeName | None
    func: ObjectWithArgs | None
    context: enums.CoercionContext | None
    inout: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, sourcetype: TypeName | _NodePayload | None = None, targettype: TypeName | _NodePayload | None = None, func: ObjectWithArgs | _NodePayload | None = None, context: enums.CoercionContext | int | str | dict[str, Any] | None = None, inout: bool | int | None = None) -> None: ...  # noqa: E501


class CreateConversionStmt(Node):
    conversion_name: tuple[Any, ...] | None
    for_encoding_name: str | None
    to_encoding_name: str | None
    func_name: tuple[Any, ...] | None
    def_: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, conversion_name: _ListInput | None = None, for_encoding_name: str | None = None, to_encoding_name: str | None = None, func_name: _ListInput | None = None, def_: bool | int | None = None) -> None: ...  # noqa: E501


class CreateDomainStmt(Node):
    domainname: tuple[Any, ...] | None
    typeName: TypeName | None
    collClause: CollateClause | None
    constraints: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, domainname: _ListInput | None = None, typeName: TypeName | _NodePayload | None = None, collClause: CollateClause | _NodePayload | None = None, constraints: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateEnumStmt(Node):
    typeName: tuple[Any, ...] | None
    vals: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, typeName: _ListInput | None = None, vals: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateEventTrigStmt(Node):
    trigname: str | None
    eventname: str | None
    whenclause: tuple[Any, ...] | None
    funcname: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, trigname: str | None = None, eventname: str | None = None, whenclause: _ListInput | None = None, funcname: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateExtensionStmt(Node):
    extname: str | None
    if_not_exists: bool | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, extname: str | None = None, if_not_exists: bool | int | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateFdwStmt(Node):
    fdwname: str | None
    func_options: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, fdwname: str | None = None, func_options: _ListInput | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateForeignServerStmt(Node):
    servername: str | None
    servertype: str | None
    version: str | None
    fdwname: str | None
    if_not_exists: bool | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, servername: str | None = None, servertype: str | None = None, version: str | None = None, fdwname: str | None = None, if_not_exists: bool | int | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateForeignTableStmt(Node):
    base: CreateStmt | None
    servername: str | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, base: CreateStmt | _NodePayload | None = None, servername: str | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateFunctionStmt(Node):
    is_procedure: bool | None
    replace: bool | None
    funcname: tuple[Any, ...] | None
    parameters: tuple[Any, ...] | None
    returnType: TypeName | None
    options: tuple[Any, ...] | None
    sql_body: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, is_procedure: bool | int | None = None, replace: bool | int | None = None, funcname: _ListInput | None = None, parameters: _ListInput | None = None, returnType: TypeName | _NodePayload | None = None, options: _ListInput | None = None, sql_body: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class CreateOpClassItem(Node):
    itemtype: int | None
    name: ObjectWithArgs | None
    number: int | None
    order_family: tuple[Any, ...] | None
    class_args: tuple[Any, ...] | None
    storedtype: TypeName | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, itemtype: int | None = None, name: ObjectWithArgs | _NodePayload | None = None, number: int | None = None, order_family: _ListInput | None = None, class_args: _ListInput | None = None, storedtype: TypeName | _NodePayload | None = None) -> None: ...  # noqa: E501


class CreateOpClassStmt(Node):
    opclassname: tuple[Any, ...] | None
    opfamilyname: tuple[Any, ...] | None
    amname: str | None
    datatype: TypeName | None
    items: tuple[Any, ...] | None
    isDefault: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, opclassname: _ListInput | None = None, opfamilyname: _ListInput | None = None, amname: str | None = None, datatype: TypeName | _NodePayload | None = None, items: _ListInput | None = None, isDefault: bool | int | None = None) -> None: ...  # noqa: E501


class CreateOpFamilyStmt(Node):
    opfamilyname: tuple[Any, ...] | None
    amname: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, opfamilyname: _ListInput | None = None, amname: str | None = None) -> None: ...  # noqa: E501


class CreatePLangStmt(Node):
    replace: bool | None
    plname: str | None
    plhandler: tuple[Any, ...] | None
    plinline: tuple[Any, ...] | None
    plvalidator: tuple[Any, ...] | None
    pltrusted: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, replace: bool | int | None = None, plname: str | None = None, plhandler: _ListInput | None = None, plinline: _ListInput | None = None, plvalidator: _ListInput | None = None, pltrusted: bool | int | None = None) -> None: ...  # noqa: E501


class CreatePolicyStmt(Node):
    policy_name: str | None
    table: RangeVar | None
    cmd_name: str | None
    permissive: bool | None
    roles: tuple[Any, ...] | None
    qual: Node | None
    with_check: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, policy_name: str | None = None, table: RangeVar | _NodePayload | None = None, cmd_name: str | None = None, permissive: bool | int | None = None, roles: _ListInput | None = None, qual: Node | _NodePayload | None = None, with_check: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class CreatePublicationStmt(Node):
    pubname: str | None
    options: tuple[Any, ...] | None
    pubobjects: tuple[Any, ...] | None
    for_all_tables: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, pubname: str | None = None, options: _ListInput | None = None, pubobjects: _ListInput | None = None, for_all_tables: bool | int | None = None) -> None: ...  # noqa: E501


class CreateRangeStmt(Node):
    typeName: tuple[Any, ...] | None
    params: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, typeName: _ListInput | None = None, params: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateRoleStmt(Node):
    stmt_type: enums.RoleStmtType | None
    role: str | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, stmt_type: enums.RoleStmtType | int | str | dict[str, Any] | None = None, role: str | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateSchemaStmt(Node):
    schemaname: str | None
    authrole: RoleSpec | None
    schemaElts: tuple[Any, ...] | None
    if_not_exists: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, schemaname: str | None = None, authrole: RoleSpec | _NodePayload | None = None, schemaElts: _ListInput | None = None, if_not_exists: bool | int | None = None) -> None: ...  # noqa: E501


class CreateSeqStmt(Node):
    sequence: RangeVar | None
    options: tuple[Any, ...] | None
    for_identity: bool | None
    if_not_exists: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, sequence: RangeVar | _NodePayload | None = None, options: _ListInput | None = None, for_identity: bool | int | None = None, if_not_exists: bool | int | None = None) -> None: ...  # noqa: E501


class CreateStatsStmt(Node):
    defnames: tuple[Any, ...] | None
    stat_types: tuple[Any, ...] | None
    exprs: tuple[Any, ...] | None
    relations: tuple[Any, ...] | None
    stxcomment: str | None
    transformed: bool | None
    if_not_exists: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, defnames: _ListInput | None = None, stat_types: _ListInput | None = None, exprs: _ListInput | None = None, relations: _ListInput | None = None, stxcomment: str | None = None, transformed: bool | int | None = None, if_not_exists: bool | int | None = None) -> None: ...  # noqa: E501


class CreateStmt(Node):
    relation: RangeVar | None
    tableElts: tuple[Any, ...] | None
    inhRelations: tuple[Any, ...] | None
    partbound: PartitionBoundSpec | None
    partspec: PartitionSpec | None
    ofTypename: TypeName | None
    constraints: tuple[Any, ...] | None
    nnconstraints: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    oncommit: enums.OnCommitAction | None
    tablespacename: str | None
    accessMethod: str | None
    if_not_exists: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, tableElts: _ListInput | None = None, inhRelations: _ListInput | None = None, partbound: PartitionBoundSpec | _NodePayload | None = None, partspec: PartitionSpec | _NodePayload | None = None, ofTypename: TypeName | _NodePayload | None = None, constraints: _ListInput | None = None, nnconstraints: _ListInput | None = None, options: _ListInput | None = None, oncommit: enums.OnCommitAction | int | str | dict[str, Any] | None = None, tablespacename: str | None = None, accessMethod: str | None = None, if_not_exists: bool | int | None = None) -> None: ...  # noqa: E501


class CreateSubscriptionStmt(Node):
    subname: str | None
    conninfo: str | None
    publication: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, subname: str | None = None, conninfo: str | None = None, publication: _ListInput | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateTableAsStmt(Node):
    query: Node | None
    into: IntoClause | None
    objtype: enums.ObjectType | None
    is_select_into: bool | None
    if_not_exists: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, query: Node | _NodePayload | None = None, into: IntoClause | _NodePayload | None = None, objtype: enums.ObjectType | int | str | dict[str, Any] | None = None, is_select_into: bool | int | None = None, if_not_exists: bool | int | None = None) -> None: ...  # noqa: E501


class CreateTableSpaceStmt(Node):
    tablespacename: str | None
    owner: RoleSpec | None
    location: str | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, tablespacename: str | None = None, owner: RoleSpec | _NodePayload | None = None, location: str | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class CreateTransformStmt(Node):
    replace: bool | None
    type_name: TypeName | None
    lang: str | None
    fromsql: ObjectWithArgs | None
    tosql: ObjectWithArgs | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, replace: bool | int | None = None, type_name: TypeName | _NodePayload | None = None, lang: str | None = None, fromsql: ObjectWithArgs | _NodePayload | None = None, tosql: ObjectWithArgs | _NodePayload | None = None) -> None: ...  # noqa: E501


class CreateTrigStmt(Node):
    replace: bool | None
    isconstraint: bool | None
    trigname: str | None
    relation: RangeVar | None
    funcname: tuple[Any, ...] | None
    args: tuple[Any, ...] | None
    row: bool | None
    timing: int | None
    events: int | None
    columns: tuple[Any, ...] | None
    whenClause: Node | None
    transitionRels: tuple[Any, ...] | None
    deferrable: bool | None
    initdeferred: bool | None
    constrrel: RangeVar | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, replace: bool | int | None = None, isconstraint: bool | int | None = None, trigname: str | None = None, relation: RangeVar | _NodePayload | None = None, funcname: _ListInput | None = None, args: _ListInput | None = None, row: bool | int | None = None, timing: int | None = None, events: int | None = None, columns: _ListInput | None = None, whenClause: Node | _NodePayload | None = None, transitionRels: _ListInput | None = None, deferrable: bool | int | None = None, initdeferred: bool | int | None = None, constrrel: RangeVar | _NodePayload | None = None) -> None: ...  # noqa: E501


class CreateUserMappingStmt(Node):
    user: RoleSpec | None
    servername: str | None
    if_not_exists: bool | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, user: RoleSpec | _NodePayload | None = None, servername: str | None = None, if_not_exists: bool | int | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class CreatedbStmt(Node):
    dbname: str | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, dbname: str | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class CurrentOfExpr(Expr):
    cvarno: int | None
    cursor_name: str | None
    cursor_param: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, cvarno: int | None = None, cursor_name: str | None = None, cursor_param: int | None = None) -> None: ...  # noqa: E501


class DeallocateStmt(Node):
    name: str | None
    isall: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, isall: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class DeclareCursorStmt(Node):
    portalname: str | None
    options: int | None
    query: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, portalname: str | None = None, options: int | None = None, query: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class DefElem(Node):
    defnamespace: str | None
    defname: str | None
    arg: Node | None
    defaction: enums.DefElemAction | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, defnamespace: str | None = None, defname: str | None = None, arg: Node | _NodePayload | None = None, defaction: enums.DefElemAction | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class DefineStmt(Node):
    kind: enums.ObjectType | None
    oldstyle: bool | None
    defnames: tuple[Any, ...] | None
    args: tuple[Any, ...] | None
    definition: tuple[Any, ...] | None
    if_not_exists: bool | None
    replace: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.ObjectType | int | str | dict[str, Any] | None = None, oldstyle: bool | int | None = None, defnames: _ListInput | None = None, args: _ListInput | None = None, definition: _ListInput | None = None, if_not_exists: bool | int | None = None, replace: bool | int | None = None) -> None: ...  # noqa: E501


class DeleteStmt(Node):
    relation: RangeVar | None
    usingClause: tuple[Any, ...] | None
    whereClause: Node | None
    returningClause: ReturningClause | None
    withClause: WithClause | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, usingClause: _ListInput | None = None, whereClause: Node | _NodePayload | None = None, returningClause: ReturningClause | _NodePayload | None = None, withClause: WithClause | _NodePayload | None = None) -> None: ...  # noqa: E501


class DiscardStmt(Node):
    target: enums.DiscardMode | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, target: enums.DiscardMode | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class DoStmt(Node):
    args: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, args: _ListInput | None = None) -> None: ...  # noqa: E501


class DropOwnedStmt(Node):
    roles: tuple[Any, ...] | None
    behavior: enums.DropBehavior | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, roles: _ListInput | None = None, behavior: enums.DropBehavior | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class DropRoleStmt(Node):
    roles: tuple[Any, ...] | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, roles: _ListInput | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class DropStmt(Node):
    objects: tuple[Any, ...] | None
    removeType: enums.ObjectType | None
    behavior: enums.DropBehavior | None
    missing_ok: bool | None
    concurrent: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, objects: _ListInput | None = None, removeType: enums.ObjectType | int | str | dict[str, Any] | None = None, behavior: enums.DropBehavior | int | str | dict[str, Any] | None = None, missing_ok: bool | int | None = None, concurrent: bool | int | None = None) -> None: ...  # noqa: E501


class DropSubscriptionStmt(Node):
    subname: str | None
    missing_ok: bool | None
    behavior: enums.DropBehavior | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, subname: str | None = None, missing_ok: bool | int | None = None, behavior: enums.DropBehavior | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class DropTableSpaceStmt(Node):
    tablespacename: str | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, tablespacename: str | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class DropUserMappingStmt(Node):
    user: RoleSpec | None
    servername: str | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, user: RoleSpec | _NodePayload | None = None, servername: str | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class DropdbStmt(Node):
    dbname: str | None
    missing_ok: bool | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, dbname: str | None = None, missing_ok: bool | int | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class ExecuteStmt(Node):
    name: str | None
    params: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, params: _ListInput | None = None) -> None: ...  # noqa: E501


class ExplainStmt(Node):
    query: Node | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, query: Node | _NodePayload | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class FetchStmt(Node):
    direction: enums.FetchDirection | None
    howMany: int | None
    portalname: str | None
    ismove: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, direction: enums.FetchDirection | int | str | dict[str, Any] | None = None, howMany: int | None = None, portalname: str | None = None, ismove: bool | int | None = None) -> None: ...  # noqa: E501


class FieldSelect(Expr):
    arg: Expr | None
    fieldnum: int | None
    resulttypmod: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, fieldnum: int | None = None, resulttypmod: int | None = None) -> None: ...  # noqa: E501


class FieldStore(Expr):
    arg: Expr | None
    newvals: tuple[Any, ...] | None
    fieldnums: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, newvals: _ListInput | None = None, fieldnums: _ListInput | None = None) -> None: ...  # noqa: E501


class Float(Node):
    fval: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, fval: _FloatStringInput | None = None) -> None: ...  # noqa: E501


class FromExpr(Node):
    fromlist: tuple[Any, ...] | None
    quals: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, fromlist: _ListInput | None = None, quals: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class FuncCall(Node):
    funcname: tuple[Any, ...] | None
    args: tuple[Any, ...] | None
    agg_order: tuple[Any, ...] | None
    agg_filter: Node | None
    over: WindowDef | None
    agg_within_group: bool | None
    agg_star: bool | None
    agg_distinct: bool | None
    func_variadic: bool | None
    funcformat: enums.CoercionForm | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, funcname: _ListInput | None = None, args: _ListInput | None = None, agg_order: _ListInput | None = None, agg_filter: Node | _NodePayload | None = None, over: WindowDef | _NodePayload | None = None, agg_within_group: bool | int | None = None, agg_star: bool | int | None = None, agg_distinct: bool | int | None = None, func_variadic: bool | int | None = None, funcformat: enums.CoercionForm | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class FuncExpr(Expr):
    funcretset: bool | None
    funcvariadic: bool | None
    funcformat: enums.CoercionForm | None
    args: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, funcretset: bool | int | None = None, funcvariadic: bool | int | None = None, funcformat: enums.CoercionForm | int | str | dict[str, Any] | None = None, args: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class FunctionParameter(Node):
    name: str | None
    argType: TypeName | None
    mode: enums.FunctionParameterMode | None
    defexpr: Node | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, argType: TypeName | _NodePayload | None = None, mode: enums.FunctionParameterMode | int | str | dict[str, Any] | None = None, defexpr: Node | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class GrantRoleStmt(Node):
    granted_roles: tuple[Any, ...] | None
    grantee_roles: tuple[Any, ...] | None
    is_grant: bool | None
    opt: tuple[Any, ...] | None
    grantor: RoleSpec | None
    behavior: enums.DropBehavior | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, granted_roles: _ListInput | None = None, grantee_roles: _ListInput | None = None, is_grant: bool | int | None = None, opt: _ListInput | None = None, grantor: RoleSpec | _NodePayload | None = None, behavior: enums.DropBehavior | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class GrantStmt(Node):
    is_grant: bool | None
    targtype: enums.GrantTargetType | None
    objtype: enums.ObjectType | None
    objects: tuple[Any, ...] | None
    privileges: tuple[Any, ...] | None
    grantees: tuple[Any, ...] | None
    grant_option: bool | None
    grantor: RoleSpec | None
    behavior: enums.DropBehavior | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, is_grant: bool | int | None = None, targtype: enums.GrantTargetType | int | str | dict[str, Any] | None = None, objtype: enums.ObjectType | int | str | dict[str, Any] | None = None, objects: _ListInput | None = None, privileges: _ListInput | None = None, grantees: _ListInput | None = None, grant_option: bool | int | None = None, grantor: RoleSpec | _NodePayload | None = None, behavior: enums.DropBehavior | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class GroupingFunc(Expr):
    args: tuple[Any, ...] | None
    refs: tuple[Any, ...] | None
    agglevelsup: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, args: _ListInput | None = None, refs: _ListInput | None = None, agglevelsup: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class GroupingSet(Node):
    kind: enums.GroupingSetKind | None
    content: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.GroupingSetKind | int | str | dict[str, Any] | None = None, content: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class ImportForeignSchemaStmt(Node):
    server_name: str | None
    remote_schema: str | None
    local_schema: str | None
    list_type: enums.ImportForeignSchemaType | None
    table_list: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, server_name: str | None = None, remote_schema: str | None = None, local_schema: str | None = None, list_type: enums.ImportForeignSchemaType | int | str | dict[str, Any] | None = None, table_list: _ListInput | None = None, options: _ListInput | None = None) -> None: ...  # noqa: E501


class IndexElem(Node):
    name: str | None
    expr: Node | None
    indexcolname: str | None
    collation: tuple[Any, ...] | None
    opclass: tuple[Any, ...] | None
    opclassopts: tuple[Any, ...] | None
    ordering: enums.SortByDir | None
    nulls_ordering: enums.SortByNulls | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, expr: Node | _NodePayload | None = None, indexcolname: str | None = None, collation: _ListInput | None = None, opclass: _ListInput | None = None, opclassopts: _ListInput | None = None, ordering: enums.SortByDir | int | str | dict[str, Any] | None = None, nulls_ordering: enums.SortByNulls | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class IndexStmt(Node):
    idxname: str | None
    relation: RangeVar | None
    accessMethod: str | None
    tableSpace: str | None
    indexParams: tuple[Any, ...] | None
    indexIncludingParams: tuple[Any, ...] | None
    options: tuple[Any, ...] | None
    whereClause: Node | None
    excludeOpNames: tuple[Any, ...] | None
    idxcomment: str | None
    oldNumber: int | None
    oldCreateSubid: int | None
    oldFirstRelfilelocatorSubid: int | None
    unique: bool | None
    nulls_not_distinct: bool | None
    primary: bool | None
    isconstraint: bool | None
    iswithoutoverlaps: bool | None
    deferrable: bool | None
    initdeferred: bool | None
    transformed: bool | None
    concurrent: bool | None
    if_not_exists: bool | None
    reset_default_tblspc: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, idxname: str | None = None, relation: RangeVar | _NodePayload | None = None, accessMethod: str | None = None, tableSpace: str | None = None, indexParams: _ListInput | None = None, indexIncludingParams: _ListInput | None = None, options: _ListInput | None = None, whereClause: Node | _NodePayload | None = None, excludeOpNames: _ListInput | None = None, idxcomment: str | None = None, oldNumber: int | None = None, oldCreateSubid: int | None = None, oldFirstRelfilelocatorSubid: int | None = None, unique: bool | int | None = None, nulls_not_distinct: bool | int | None = None, primary: bool | int | None = None, isconstraint: bool | int | None = None, iswithoutoverlaps: bool | int | None = None, deferrable: bool | int | None = None, initdeferred: bool | int | None = None, transformed: bool | int | None = None, concurrent: bool | int | None = None, if_not_exists: bool | int | None = None, reset_default_tblspc: bool | int | None = None) -> None: ...  # noqa: E501


class InferClause(Node):
    indexElems: tuple[Any, ...] | None
    whereClause: Node | None
    conname: str | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, indexElems: _ListInput | None = None, whereClause: Node | _NodePayload | None = None, conname: str | None = None, location: int | None = None) -> None: ...  # noqa: E501


class InferenceElem(Expr):
    expr: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, expr: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class InlineCodeBlock(Node):
    source_text: str | None
    langIsTrusted: bool | None
    atomic: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, source_text: str | None = None, langIsTrusted: bool | int | None = None, atomic: bool | int | None = None) -> None: ...  # noqa: E501


class InsertStmt(Node):
    relation: RangeVar | None
    cols: tuple[Any, ...] | None
    selectStmt: Node | None
    onConflictClause: OnConflictClause | None
    returningClause: ReturningClause | None
    withClause: WithClause | None
    override: enums.OverridingKind | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, cols: _ListInput | None = None, selectStmt: Node | _NodePayload | None = None, onConflictClause: OnConflictClause | _NodePayload | None = None, returningClause: ReturningClause | _NodePayload | None = None, withClause: WithClause | _NodePayload | None = None, override: enums.OverridingKind | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class Integer(Node):
    ival: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, ival: int | None = None) -> None: ...  # noqa: E501


class IntoClause(Node):
    rel: RangeVar | None
    colNames: tuple[Any, ...] | None
    accessMethod: str | None
    options: tuple[Any, ...] | None
    onCommit: enums.OnCommitAction | None
    tableSpaceName: str | None
    viewQuery: Query | None
    skipData: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, rel: RangeVar | _NodePayload | None = None, colNames: _ListInput | None = None, accessMethod: str | None = None, options: _ListInput | None = None, onCommit: enums.OnCommitAction | int | str | dict[str, Any] | None = None, tableSpaceName: str | None = None, viewQuery: Query | _NodePayload | None = None, skipData: bool | int | None = None) -> None: ...  # noqa: E501


class JoinExpr(Node):
    jointype: enums.JoinType | None
    isNatural: bool | None
    larg: Node | None
    rarg: Node | None
    usingClause: tuple[Any, ...] | None
    join_using_alias: Alias | None
    quals: Node | None
    alias: Alias | None
    rtindex: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, jointype: enums.JoinType | int | str | dict[str, Any] | None = None, isNatural: bool | int | None = None, larg: Node | _NodePayload | None = None, rarg: Node | _NodePayload | None = None, usingClause: _ListInput | None = None, join_using_alias: Alias | _NodePayload | None = None, quals: Node | _NodePayload | None = None, alias: Alias | _NodePayload | None = None, rtindex: int | None = None) -> None: ...  # noqa: E501


class JsonAggConstructor(Node):
    output: JsonOutput | None
    agg_filter: Node | None
    agg_order: tuple[Any, ...] | None
    over: WindowDef | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, output: JsonOutput | _NodePayload | None = None, agg_filter: Node | _NodePayload | None = None, agg_order: _ListInput | None = None, over: WindowDef | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonArgument(Node):
    val: JsonValueExpr | None
    name: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, val: JsonValueExpr | _NodePayload | None = None, name: str | None = None) -> None: ...  # noqa: E501


class JsonArrayAgg(Node):
    constructor: JsonAggConstructor | None
    arg: JsonValueExpr | None
    absent_on_null: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, constructor: JsonAggConstructor | _NodePayload | None = None, arg: JsonValueExpr | _NodePayload | None = None, absent_on_null: bool | int | None = None) -> None: ...  # noqa: E501


class JsonArrayConstructor(Node):
    exprs: tuple[Any, ...] | None
    output: JsonOutput | None
    absent_on_null: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, exprs: _ListInput | None = None, output: JsonOutput | _NodePayload | None = None, absent_on_null: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonArrayQueryConstructor(Node):
    query: Node | None
    output: JsonOutput | None
    format: JsonFormat | None
    absent_on_null: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, query: Node | _NodePayload | None = None, output: JsonOutput | _NodePayload | None = None, format: JsonFormat | _NodePayload | None = None, absent_on_null: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonBehavior(Node):
    btype: enums.JsonBehaviorType | None
    expr: Node | None
    coerce: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, btype: enums.JsonBehaviorType | int | str | dict[str, Any] | None = None, expr: Node | _NodePayload | None = None, coerce: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonConstructorExpr(Expr):
    type: enums.JsonConstructorType | None
    args: tuple[Any, ...] | None
    func: Expr | None
    coercion: Expr | None
    returning: JsonReturning | None
    absent_on_null: bool | None
    unique: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, type: enums.JsonConstructorType | int | str | dict[str, Any] | None = None, args: _ListInput | None = None, func: Expr | _NodePayload | None = None, coercion: Expr | _NodePayload | None = None, returning: JsonReturning | _NodePayload | None = None, absent_on_null: bool | int | None = None, unique: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonExpr(Expr):
    op: enums.JsonExprOp | None
    column_name: str | None
    formatted_expr: Node | None
    format: JsonFormat | None
    path_spec: Node | None
    returning: JsonReturning | None
    passing_names: tuple[Any, ...] | None
    passing_values: tuple[Any, ...] | None
    on_empty: JsonBehavior | None
    on_error: JsonBehavior | None
    use_io_coercion: bool | None
    use_json_coercion: bool | None
    wrapper: enums.JsonWrapper | None
    omit_quotes: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, op: enums.JsonExprOp | int | str | dict[str, Any] | None = None, column_name: str | None = None, formatted_expr: Node | _NodePayload | None = None, format: JsonFormat | _NodePayload | None = None, path_spec: Node | _NodePayload | None = None, returning: JsonReturning | _NodePayload | None = None, passing_names: _ListInput | None = None, passing_values: _ListInput | None = None, on_empty: JsonBehavior | _NodePayload | None = None, on_error: JsonBehavior | _NodePayload | None = None, use_io_coercion: bool | int | None = None, use_json_coercion: bool | int | None = None, wrapper: enums.JsonWrapper | int | str | dict[str, Any] | None = None, omit_quotes: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonFormat(Node):
    format_type: enums.JsonFormatType | None
    encoding: enums.JsonEncoding | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, format_type: enums.JsonFormatType | int | str | dict[str, Any] | None = None, encoding: enums.JsonEncoding | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonFuncExpr(Node):
    op: enums.JsonExprOp | None
    column_name: str | None
    context_item: JsonValueExpr | None
    pathspec: Node | None
    passing: tuple[Any, ...] | None
    output: JsonOutput | None
    on_empty: JsonBehavior | None
    on_error: JsonBehavior | None
    wrapper: enums.JsonWrapper | None
    quotes: enums.JsonQuotes | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, op: enums.JsonExprOp | int | str | dict[str, Any] | None = None, column_name: str | None = None, context_item: JsonValueExpr | _NodePayload | None = None, pathspec: Node | _NodePayload | None = None, passing: _ListInput | None = None, output: JsonOutput | _NodePayload | None = None, on_empty: JsonBehavior | _NodePayload | None = None, on_error: JsonBehavior | _NodePayload | None = None, wrapper: enums.JsonWrapper | int | str | dict[str, Any] | None = None, quotes: enums.JsonQuotes | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonIsPredicate(Node):
    expr: Node | None
    format: JsonFormat | None
    item_type: enums.JsonValueType | None
    unique_keys: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, expr: Node | _NodePayload | None = None, format: JsonFormat | _NodePayload | None = None, item_type: enums.JsonValueType | int | str | dict[str, Any] | None = None, unique_keys: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonKeyValue(Node):
    key: Expr | None
    value: JsonValueExpr | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, key: Expr | _NodePayload | None = None, value: JsonValueExpr | _NodePayload | None = None) -> None: ...  # noqa: E501


class JsonObjectAgg(Node):
    constructor: JsonAggConstructor | None
    arg: JsonKeyValue | None
    absent_on_null: bool | None
    unique: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, constructor: JsonAggConstructor | _NodePayload | None = None, arg: JsonKeyValue | _NodePayload | None = None, absent_on_null: bool | int | None = None, unique: bool | int | None = None) -> None: ...  # noqa: E501


class JsonObjectConstructor(Node):
    exprs: tuple[Any, ...] | None
    output: JsonOutput | None
    absent_on_null: bool | None
    unique: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, exprs: _ListInput | None = None, output: JsonOutput | _NodePayload | None = None, absent_on_null: bool | int | None = None, unique: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonOutput(Node):
    typeName: TypeName | None
    returning: JsonReturning | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, typeName: TypeName | _NodePayload | None = None, returning: JsonReturning | _NodePayload | None = None) -> None: ...  # noqa: E501


class JsonParseExpr(Node):
    expr: JsonValueExpr | None
    output: JsonOutput | None
    unique_keys: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, expr: JsonValueExpr | _NodePayload | None = None, output: JsonOutput | _NodePayload | None = None, unique_keys: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonReturning(Node):
    format: JsonFormat | None
    typmod: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, format: JsonFormat | _NodePayload | None = None, typmod: int | None = None) -> None: ...  # noqa: E501


class JsonScalarExpr(Node):
    expr: Expr | None
    output: JsonOutput | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, expr: Expr | _NodePayload | None = None, output: JsonOutput | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonSerializeExpr(Node):
    expr: JsonValueExpr | None
    output: JsonOutput | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, expr: JsonValueExpr | _NodePayload | None = None, output: JsonOutput | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonTable(Node):
    context_item: JsonValueExpr | None
    pathspec: JsonTablePathSpec | None
    passing: tuple[Any, ...] | None
    columns: tuple[Any, ...] | None
    on_error: JsonBehavior | None
    alias: Alias | None
    lateral: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, context_item: JsonValueExpr | _NodePayload | None = None, pathspec: JsonTablePathSpec | _NodePayload | None = None, passing: _ListInput | None = None, columns: _ListInput | None = None, on_error: JsonBehavior | _NodePayload | None = None, alias: Alias | _NodePayload | None = None, lateral: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonTableColumn(Node):
    coltype: enums.JsonTableColumnType | None
    name: str | None
    typeName: TypeName | None
    pathspec: JsonTablePathSpec | None
    format: JsonFormat | None
    wrapper: enums.JsonWrapper | None
    quotes: enums.JsonQuotes | None
    columns: tuple[Any, ...] | None
    on_empty: JsonBehavior | None
    on_error: JsonBehavior | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, coltype: enums.JsonTableColumnType | int | str | dict[str, Any] | None = None, name: str | None = None, typeName: TypeName | _NodePayload | None = None, pathspec: JsonTablePathSpec | _NodePayload | None = None, format: JsonFormat | _NodePayload | None = None, wrapper: enums.JsonWrapper | int | str | dict[str, Any] | None = None, quotes: enums.JsonQuotes | int | str | dict[str, Any] | None = None, columns: _ListInput | None = None, on_empty: JsonBehavior | _NodePayload | None = None, on_error: JsonBehavior | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonTablePathSpec(Node):
    string: Node | None
    name: str | None
    name_location: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, string: Node | _NodePayload | None = None, name: str | None = None, name_location: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class JsonValueExpr(Node):
    raw_expr: Expr | None
    formatted_expr: Expr | None
    format: JsonFormat | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, raw_expr: Expr | _NodePayload | None = None, formatted_expr: Expr | _NodePayload | None = None, format: JsonFormat | _NodePayload | None = None) -> None: ...  # noqa: E501


class ListenStmt(Node):
    conditionname: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, conditionname: str | None = None) -> None: ...  # noqa: E501


class LoadStmt(Node):
    filename: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, filename: str | None = None) -> None: ...  # noqa: E501


class LockStmt(Node):
    relations: tuple[Any, ...] | None
    mode: int | None
    nowait: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relations: _ListInput | None = None, mode: int | None = None, nowait: bool | int | None = None) -> None: ...  # noqa: E501


class LockingClause(Node):
    lockedRels: tuple[Any, ...] | None
    strength: enums.LockClauseStrength | None
    waitPolicy: enums.LockWaitPolicy | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, lockedRels: _ListInput | None = None, strength: enums.LockClauseStrength | int | str | dict[str, Any] | None = None, waitPolicy: enums.LockWaitPolicy | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class MergeAction(Node):
    matchKind: enums.MergeMatchKind | None
    commandType: enums.CmdType | None
    override: enums.OverridingKind | None
    qual: Node | None
    targetList: tuple[Any, ...] | None
    updateColnos: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, matchKind: enums.MergeMatchKind | int | str | dict[str, Any] | None = None, commandType: enums.CmdType | int | str | dict[str, Any] | None = None, override: enums.OverridingKind | int | str | dict[str, Any] | None = None, qual: Node | _NodePayload | None = None, targetList: _ListInput | None = None, updateColnos: _ListInput | None = None) -> None: ...  # noqa: E501


class MergeStmt(Node):
    relation: RangeVar | None
    sourceRelation: Node | None
    joinCondition: Node | None
    mergeWhenClauses: tuple[Any, ...] | None
    returningClause: ReturningClause | None
    withClause: WithClause | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, sourceRelation: Node | _NodePayload | None = None, joinCondition: Node | _NodePayload | None = None, mergeWhenClauses: _ListInput | None = None, returningClause: ReturningClause | _NodePayload | None = None, withClause: WithClause | _NodePayload | None = None) -> None: ...  # noqa: E501


class MergeSupportFunc(Expr):
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, location: int | None = None) -> None: ...  # noqa: E501


class MergeWhenClause(Node):
    matchKind: enums.MergeMatchKind | None
    commandType: enums.CmdType | None
    override: enums.OverridingKind | None
    condition: Node | None
    targetList: tuple[Any, ...] | None
    values: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, matchKind: enums.MergeMatchKind | int | str | dict[str, Any] | None = None, commandType: enums.CmdType | int | str | dict[str, Any] | None = None, override: enums.OverridingKind | int | str | dict[str, Any] | None = None, condition: Node | _NodePayload | None = None, targetList: _ListInput | None = None, values: _ListInput | None = None) -> None: ...  # noqa: E501


class MinMaxExpr(Expr):
    op: enums.MinMaxOp | None
    args: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, op: enums.MinMaxOp | int | str | dict[str, Any] | None = None, args: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class MultiAssignRef(Node):
    source: Node | None
    colno: int | None
    ncolumns: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, source: Node | _NodePayload | None = None, colno: int | None = None, ncolumns: int | None = None) -> None: ...  # noqa: E501


class NamedArgExpr(Expr):
    arg: Expr | None
    name: str | None
    argnumber: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, name: str | None = None, argnumber: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class NotifyStmt(Node):
    conditionname: str | None
    payload: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, conditionname: str | None = None, payload: str | None = None) -> None: ...  # noqa: E501


class NullTest(Expr):
    arg: Expr | None
    nulltesttype: enums.NullTestType | None
    argisrow: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, nulltesttype: enums.NullTestType | int | str | dict[str, Any] | None = None, argisrow: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class ObjectWithArgs(Node):
    objname: tuple[Any, ...] | None
    objargs: tuple[Any, ...] | None
    objfuncargs: tuple[Any, ...] | None
    args_unspecified: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, objname: _ListInput | None = None, objargs: _ListInput | None = None, objfuncargs: _ListInput | None = None, args_unspecified: bool | int | None = None) -> None: ...  # noqa: E501


class OnConflictClause(Node):
    action: enums.OnConflictAction | None
    infer: InferClause | None
    targetList: tuple[Any, ...] | None
    whereClause: Node | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, action: enums.OnConflictAction | int | str | dict[str, Any] | None = None, infer: InferClause | _NodePayload | None = None, targetList: _ListInput | None = None, whereClause: Node | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class OnConflictExpr(Node):
    action: enums.OnConflictAction | None
    arbiterElems: tuple[Any, ...] | None
    arbiterWhere: Node | None
    onConflictSet: tuple[Any, ...] | None
    onConflictWhere: Node | None
    exclRelIndex: int | None
    exclRelTlist: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, action: enums.OnConflictAction | int | str | dict[str, Any] | None = None, arbiterElems: _ListInput | None = None, arbiterWhere: Node | _NodePayload | None = None, onConflictSet: _ListInput | None = None, onConflictWhere: Node | _NodePayload | None = None, exclRelIndex: int | None = None, exclRelTlist: _ListInput | None = None) -> None: ...  # noqa: E501


class OpExpr(Expr):
    opretset: bool | None
    args: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, opretset: bool | int | None = None, args: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class PLAssignStmt(Node):
    name: str | None
    indirection: tuple[Any, ...] | None
    nnames: int | None
    val: SelectStmt | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, indirection: _ListInput | None = None, nnames: int | None = None, val: SelectStmt | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class Param(Expr):
    paramkind: enums.ParamKind | None
    paramid: int | None
    paramtypmod: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, paramkind: enums.ParamKind | int | str | dict[str, Any] | None = None, paramid: int | None = None, paramtypmod: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class ParamRef(Node):
    number: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, number: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class PartitionBoundSpec(Node):
    strategy: str | None
    is_default: bool | None
    modulus: int | None
    remainder: int | None
    listdatums: tuple[Any, ...] | None
    lowerdatums: tuple[Any, ...] | None
    upperdatums: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, strategy: _CharInput | None = None, is_default: bool | int | None = None, modulus: int | None = None, remainder: int | None = None, listdatums: _ListInput | None = None, lowerdatums: _ListInput | None = None, upperdatums: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class PartitionCmd(Node):
    name: RangeVar | None
    bound: PartitionBoundSpec | None
    concurrent: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: RangeVar | _NodePayload | None = None, bound: PartitionBoundSpec | _NodePayload | None = None, concurrent: bool | int | None = None) -> None: ...  # noqa: E501


class PartitionElem(Node):
    name: str | None
    expr: Node | None
    collation: tuple[Any, ...] | None
    opclass: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, expr: Node | _NodePayload | None = None, collation: _ListInput | None = None, opclass: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class PartitionRangeDatum(Node):
    kind: enums.PartitionRangeDatumKind | None
    value: Node | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.PartitionRangeDatumKind | int | str | dict[str, Any] | None = None, value: Node | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class PartitionSpec(Node):
    strategy: enums.PartitionStrategy | None
    partParams: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, strategy: enums.PartitionStrategy | int | str | dict[str, Any] | None = None, partParams: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class PrepareStmt(Node):
    name: str | None
    argtypes: tuple[Any, ...] | None
    query: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, argtypes: _ListInput | None = None, query: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class PublicationObjSpec(Node):
    pubobjtype: enums.PublicationObjSpecType | None
    name: str | None
    pubtable: PublicationTable | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, pubobjtype: enums.PublicationObjSpecType | int | str | dict[str, Any] | None = None, name: str | None = None, pubtable: PublicationTable | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class PublicationTable(Node):
    relation: RangeVar | None
    whereClause: Node | None
    columns: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, whereClause: Node | _NodePayload | None = None, columns: _ListInput | None = None) -> None: ...  # noqa: E501


class Query(Node):
    commandType: enums.CmdType | None
    querySource: enums.QuerySource | None
    canSetTag: bool | None
    utilityStmt: Node | None
    resultRelation: int | None
    hasAggs: bool | None
    hasWindowFuncs: bool | None
    hasTargetSRFs: bool | None
    hasSubLinks: bool | None
    hasDistinctOn: bool | None
    hasRecursive: bool | None
    hasModifyingCTE: bool | None
    hasForUpdate: bool | None
    hasRowSecurity: bool | None
    hasGroupRTE: bool | None
    isReturn: bool | None
    cteList: tuple[Any, ...] | None
    rtable: tuple[Any, ...] | None
    rteperminfos: tuple[Any, ...] | None
    jointree: FromExpr | None
    mergeActionList: tuple[Any, ...] | None
    mergeTargetRelation: int | None
    mergeJoinCondition: Node | None
    targetList: tuple[Any, ...] | None
    override: enums.OverridingKind | None
    onConflict: OnConflictExpr | None
    returningOldAlias: str | None
    returningNewAlias: str | None
    returningList: tuple[Any, ...] | None
    groupClause: tuple[Any, ...] | None
    groupDistinct: bool | None
    groupingSets: tuple[Any, ...] | None
    havingQual: Node | None
    windowClause: tuple[Any, ...] | None
    distinctClause: tuple[Any, ...] | None
    sortClause: tuple[Any, ...] | None
    limitOffset: Node | None
    limitCount: Node | None
    limitOption: enums.LimitOption | None
    rowMarks: tuple[Any, ...] | None
    setOperations: Node | None
    constraintDeps: tuple[Any, ...] | None
    withCheckOptions: tuple[Any, ...] | None
    stmt_location: int | None
    stmt_len: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, commandType: enums.CmdType | int | str | dict[str, Any] | None = None, querySource: enums.QuerySource | int | str | dict[str, Any] | None = None, canSetTag: bool | int | None = None, utilityStmt: Node | _NodePayload | None = None, resultRelation: int | None = None, hasAggs: bool | int | None = None, hasWindowFuncs: bool | int | None = None, hasTargetSRFs: bool | int | None = None, hasSubLinks: bool | int | None = None, hasDistinctOn: bool | int | None = None, hasRecursive: bool | int | None = None, hasModifyingCTE: bool | int | None = None, hasForUpdate: bool | int | None = None, hasRowSecurity: bool | int | None = None, hasGroupRTE: bool | int | None = None, isReturn: bool | int | None = None, cteList: _ListInput | None = None, rtable: _ListInput | None = None, rteperminfos: _ListInput | None = None, jointree: FromExpr | _NodePayload | None = None, mergeActionList: _ListInput | None = None, mergeTargetRelation: int | None = None, mergeJoinCondition: Node | _NodePayload | None = None, targetList: _ListInput | None = None, override: enums.OverridingKind | int | str | dict[str, Any] | None = None, onConflict: OnConflictExpr | _NodePayload | None = None, returningOldAlias: str | None = None, returningNewAlias: str | None = None, returningList: _ListInput | None = None, groupClause: _ListInput | None = None, groupDistinct: bool | int | None = None, groupingSets: _ListInput | None = None, havingQual: Node | _NodePayload | None = None, windowClause: _ListInput | None = None, distinctClause: _ListInput | None = None, sortClause: _ListInput | None = None, limitOffset: Node | _NodePayload | None = None, limitCount: Node | _NodePayload | None = None, limitOption: enums.LimitOption | int | str | dict[str, Any] | None = None, rowMarks: _ListInput | None = None, setOperations: Node | _NodePayload | None = None, constraintDeps: _ListInput | None = None, withCheckOptions: _ListInput | None = None, stmt_location: int | None = None, stmt_len: int | None = None) -> None: ...  # noqa: E501


class RTEPermissionInfo(Node):
    inh: bool | None
    requiredPerms: int | None
    selectedCols: set[int] | None
    insertedCols: set[int] | None
    updatedCols: set[int] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, inh: bool | int | None = None, requiredPerms: int | None = None, selectedCols: _BitmapsetInput | None = None, insertedCols: _BitmapsetInput | None = None, updatedCols: _BitmapsetInput | None = None) -> None: ...  # noqa: E501


class RangeFunction(Node):
    lateral: bool | None
    ordinality: bool | None
    is_rowsfrom: bool | None
    functions: tuple[Any, ...] | None
    alias: Alias | None
    coldeflist: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, lateral: bool | int | None = None, ordinality: bool | int | None = None, is_rowsfrom: bool | int | None = None, functions: _ListInput | None = None, alias: Alias | _NodePayload | None = None, coldeflist: _ListInput | None = None) -> None: ...  # noqa: E501


class RangeSubselect(Node):
    lateral: bool | None
    subquery: Node | None
    alias: Alias | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, lateral: bool | int | None = None, subquery: Node | _NodePayload | None = None, alias: Alias | _NodePayload | None = None) -> None: ...  # noqa: E501


class RangeTableFunc(Node):
    lateral: bool | None
    docexpr: Node | None
    rowexpr: Node | None
    namespaces: tuple[Any, ...] | None
    columns: tuple[Any, ...] | None
    alias: Alias | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, lateral: bool | int | None = None, docexpr: Node | _NodePayload | None = None, rowexpr: Node | _NodePayload | None = None, namespaces: _ListInput | None = None, columns: _ListInput | None = None, alias: Alias | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class RangeTableFuncCol(Node):
    colname: str | None
    typeName: TypeName | None
    for_ordinality: bool | None
    is_not_null: bool | None
    colexpr: Node | None
    coldefexpr: Node | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, colname: str | None = None, typeName: TypeName | _NodePayload | None = None, for_ordinality: bool | int | None = None, is_not_null: bool | int | None = None, colexpr: Node | _NodePayload | None = None, coldefexpr: Node | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class RangeTableSample(Node):
    relation: Node | None
    method: tuple[Any, ...] | None
    args: tuple[Any, ...] | None
    repeatable: Node | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: Node | _NodePayload | None = None, method: _ListInput | None = None, args: _ListInput | None = None, repeatable: Node | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class RangeTblEntry(Node):
    alias: Alias | None
    eref: Alias | None
    rtekind: enums.RTEKind | None
    inh: bool | None
    relkind: str | None
    rellockmode: int | None
    perminfoindex: int | None
    tablesample: TableSampleClause | None
    subquery: Query | None
    security_barrier: bool | None
    jointype: enums.JoinType | None
    joinmergedcols: int | None
    joinaliasvars: tuple[Any, ...] | None
    joinleftcols: tuple[Any, ...] | None
    joinrightcols: tuple[Any, ...] | None
    join_using_alias: Alias | None
    functions: tuple[Any, ...] | None
    funcordinality: bool | None
    tablefunc: TableFunc | None
    values_lists: tuple[Any, ...] | None
    ctename: str | None
    ctelevelsup: int | None
    self_reference: bool | None
    coltypes: tuple[Any, ...] | None
    coltypmods: tuple[Any, ...] | None
    colcollations: tuple[Any, ...] | None
    enrname: str | None
    enrtuples: float | None
    groupexprs: tuple[Any, ...] | None
    lateral: bool | None
    inFromCl: bool | None
    securityQuals: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, alias: Alias | _NodePayload | None = None, eref: Alias | _NodePayload | None = None, rtekind: enums.RTEKind | int | str | dict[str, Any] | None = None, inh: bool | int | None = None, relkind: _CharInput | None = None, rellockmode: int | None = None, perminfoindex: int | None = None, tablesample: TableSampleClause | _NodePayload | None = None, subquery: Query | _NodePayload | None = None, security_barrier: bool | int | None = None, jointype: enums.JoinType | int | str | dict[str, Any] | None = None, joinmergedcols: int | None = None, joinaliasvars: _ListInput | None = None, joinleftcols: _ListInput | None = None, joinrightcols: _ListInput | None = None, join_using_alias: Alias | _NodePayload | None = None, functions: _ListInput | None = None, funcordinality: bool | int | None = None, tablefunc: TableFunc | _NodePayload | None = None, values_lists: _ListInput | None = None, ctename: str | None = None, ctelevelsup: int | None = None, self_reference: bool | int | None = None, coltypes: _ListInput | None = None, coltypmods: _ListInput | None = None, colcollations: _ListInput | None = None, enrname: str | None = None, enrtuples: float | None = None, groupexprs: _ListInput | None = None, lateral: bool | int | None = None, inFromCl: bool | int | None = None, securityQuals: _ListInput | None = None) -> None: ...  # noqa: E501


class RangeTblFunction(Node):
    funcexpr: Node | None
    funccolcount: int | None
    funccolnames: tuple[Any, ...] | None
    funccoltypes: tuple[Any, ...] | None
    funccoltypmods: tuple[Any, ...] | None
    funccolcollations: tuple[Any, ...] | None
    funcparams: set[int] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, funcexpr: Node | _NodePayload | None = None, funccolcount: int | None = None, funccolnames: _ListInput | None = None, funccoltypes: _ListInput | None = None, funccoltypmods: _ListInput | None = None, funccolcollations: _ListInput | None = None, funcparams: _BitmapsetInput | None = None) -> None: ...  # noqa: E501


class RangeTblRef(Node):
    rtindex: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, rtindex: int | None = None) -> None: ...  # noqa: E501


class RangeVar(Node):
    catalogname: str | None
    schemaname: str | None
    relname: str | None
    inh: bool | None
    relpersistence: str | None
    alias: Alias | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, catalogname: str | None = None, schemaname: str | None = None, relname: str | None = None, inh: bool | int | None = None, relpersistence: _CharInput | None = None, alias: Alias | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class RawStmt(Node):
    stmt: Node
    stmt_location: int | None
    stmt_len: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, stmt: Node | _NodePayload | None = None, stmt_location: int | None = None, stmt_len: int | None = None) -> None: ...  # noqa: E501


class ReassignOwnedStmt(Node):
    roles: tuple[Any, ...] | None
    newrole: RoleSpec | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, roles: _ListInput | None = None, newrole: RoleSpec | _NodePayload | None = None) -> None: ...  # noqa: E501


class RefreshMatViewStmt(Node):
    concurrent: bool | None
    skipData: bool | None
    relation: RangeVar | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, concurrent: bool | int | None = None, skipData: bool | int | None = None, relation: RangeVar | _NodePayload | None = None) -> None: ...  # noqa: E501


class ReindexStmt(Node):
    kind: enums.ReindexObjectType | None
    relation: RangeVar | None
    name: str | None
    params: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.ReindexObjectType | int | str | dict[str, Any] | None = None, relation: RangeVar | _NodePayload | None = None, name: str | None = None, params: _ListInput | None = None) -> None: ...  # noqa: E501


class RelabelType(Expr):
    arg: Expr | None
    resulttypmod: int | None
    relabelformat: enums.CoercionForm | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Expr | _NodePayload | None = None, resulttypmod: int | None = None, relabelformat: enums.CoercionForm | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class RenameStmt(Node):
    renameType: enums.ObjectType | None
    relationType: enums.ObjectType | None
    relation: RangeVar | None
    object: Node | None
    subname: str | None
    newname: str | None
    behavior: enums.DropBehavior | None
    missing_ok: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, renameType: enums.ObjectType | int | str | dict[str, Any] | None = None, relationType: enums.ObjectType | int | str | dict[str, Any] | None = None, relation: RangeVar | _NodePayload | None = None, object: Node | _NodePayload | None = None, subname: str | None = None, newname: str | None = None, behavior: enums.DropBehavior | int | str | dict[str, Any] | None = None, missing_ok: bool | int | None = None) -> None: ...  # noqa: E501


class ReplicaIdentityStmt(Node):
    identity_type: str | None
    name: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, identity_type: _CharInput | None = None, name: str | None = None) -> None: ...  # noqa: E501


class ResTarget(Node):
    name: str | None
    indirection: tuple[Any, ...] | None
    val: Node | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, indirection: _ListInput | None = None, val: Node | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class ReturnStmt(Node):
    returnval: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, returnval: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class ReturningClause(Node):
    options: tuple[Any, ...] | None
    exprs: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, options: _ListInput | None = None, exprs: _ListInput | None = None) -> None: ...  # noqa: E501


class ReturningExpr(Expr):
    retlevelsup: int | None
    retold: bool | None
    retexpr: Expr | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, retlevelsup: int | None = None, retold: bool | int | None = None, retexpr: Expr | _NodePayload | None = None) -> None: ...  # noqa: E501


class ReturningOption(Node):
    option: enums.ReturningOptionKind | None
    value: str | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, option: enums.ReturningOptionKind | int | str | dict[str, Any] | None = None, value: str | None = None, location: int | None = None) -> None: ...  # noqa: E501


class RoleSpec(Node):
    roletype: enums.RoleSpecType | None
    rolename: str | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, roletype: enums.RoleSpecType | int | str | dict[str, Any] | None = None, rolename: str | None = None, location: int | None = None) -> None: ...  # noqa: E501


class RowCompareExpr(Expr):
    cmptype: enums.CompareType | None
    opnos: tuple[Any, ...] | None
    opfamilies: tuple[Any, ...] | None
    inputcollids: tuple[Any, ...] | None
    largs: tuple[Any, ...] | None
    rargs: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, cmptype: enums.CompareType | int | str | dict[str, Any] | None = None, opnos: _ListInput | None = None, opfamilies: _ListInput | None = None, inputcollids: _ListInput | None = None, largs: _ListInput | None = None, rargs: _ListInput | None = None) -> None: ...  # noqa: E501


class RowExpr(Expr):
    args: tuple[Any, ...] | None
    row_format: enums.CoercionForm | None
    colnames: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, args: _ListInput | None = None, row_format: enums.CoercionForm | int | str | dict[str, Any] | None = None, colnames: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class RowMarkClause(Node):
    rti: int | None
    strength: enums.LockClauseStrength | None
    waitPolicy: enums.LockWaitPolicy | None
    pushedDown: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, rti: int | None = None, strength: enums.LockClauseStrength | int | str | dict[str, Any] | None = None, waitPolicy: enums.LockWaitPolicy | int | str | dict[str, Any] | None = None, pushedDown: bool | int | None = None) -> None: ...  # noqa: E501


class RuleStmt(Node):
    relation: RangeVar | None
    rulename: str | None
    whereClause: Node | None
    event: enums.CmdType | None
    instead: bool | None
    actions: tuple[Any, ...] | None
    replace: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, rulename: str | None = None, whereClause: Node | _NodePayload | None = None, event: enums.CmdType | int | str | dict[str, Any] | None = None, instead: bool | int | None = None, actions: _ListInput | None = None, replace: bool | int | None = None) -> None: ...  # noqa: E501


class SQLValueFunction(Expr):
    op: enums.SQLValueFunctionOp | None
    typmod: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, op: enums.SQLValueFunctionOp | int | str | dict[str, Any] | None = None, typmod: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class ScalarArrayOpExpr(Expr):
    useOr: bool | None
    args: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, useOr: bool | int | None = None, args: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class SecLabelStmt(Node):
    objtype: enums.ObjectType | None
    object: Node | None
    provider: str | None
    label: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, objtype: enums.ObjectType | int | str | dict[str, Any] | None = None, object: Node | _NodePayload | None = None, provider: str | None = None, label: str | None = None) -> None: ...  # noqa: E501


class SelectStmt(Node):
    distinctClause: tuple[Any, ...] | None
    intoClause: IntoClause | None
    targetList: tuple[Any, ...] | None
    fromClause: tuple[Any, ...] | None
    whereClause: Node | None
    groupClause: tuple[Any, ...] | None
    groupDistinct: bool | None
    havingClause: Node | None
    windowClause: tuple[Any, ...] | None
    valuesLists: tuple[Any, ...] | None
    sortClause: tuple[Any, ...] | None
    limitOffset: Node | None
    limitCount: Node | None
    limitOption: enums.LimitOption | None
    lockingClause: tuple[Any, ...] | None
    withClause: WithClause | None
    op: enums.SetOperation | None
    all: bool | None
    larg: SelectStmt | None
    rarg: SelectStmt | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, distinctClause: _ListInput | None = None, intoClause: IntoClause | _NodePayload | None = None, targetList: _ListInput | None = None, fromClause: _ListInput | None = None, whereClause: Node | _NodePayload | None = None, groupClause: _ListInput | None = None, groupDistinct: bool | int | None = None, havingClause: Node | _NodePayload | None = None, windowClause: _ListInput | None = None, valuesLists: _ListInput | None = None, sortClause: _ListInput | None = None, limitOffset: Node | _NodePayload | None = None, limitCount: Node | _NodePayload | None = None, limitOption: enums.LimitOption | int | str | dict[str, Any] | None = None, lockingClause: _ListInput | None = None, withClause: WithClause | _NodePayload | None = None, op: enums.SetOperation | int | str | dict[str, Any] | None = None, all: bool | int | None = None, larg: SelectStmt | _NodePayload | None = None, rarg: SelectStmt | _NodePayload | None = None) -> None: ...  # noqa: E501


class SetOperationStmt(Node):
    op: enums.SetOperation | None
    all: bool | None
    larg: Node | None
    rarg: Node | None
    colTypes: tuple[Any, ...] | None
    colTypmods: tuple[Any, ...] | None
    colCollations: tuple[Any, ...] | None
    groupClauses: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, op: enums.SetOperation | int | str | dict[str, Any] | None = None, all: bool | int | None = None, larg: Node | _NodePayload | None = None, rarg: Node | _NodePayload | None = None, colTypes: _ListInput | None = None, colTypmods: _ListInput | None = None, colCollations: _ListInput | None = None, groupClauses: _ListInput | None = None) -> None: ...  # noqa: E501


class SetToDefault(Expr):
    typeMod: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, typeMod: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class SortBy(Node):
    node: Node | None
    sortby_dir: enums.SortByDir | None
    sortby_nulls: enums.SortByNulls | None
    useOp: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, node: Node | _NodePayload | None = None, sortby_dir: enums.SortByDir | int | str | dict[str, Any] | None = None, sortby_nulls: enums.SortByNulls | int | str | dict[str, Any] | None = None, useOp: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class SortGroupClause(Node):
    tleSortGroupRef: int | None
    reverse_sort: bool | None
    nulls_first: bool | None
    hashable: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, tleSortGroupRef: int | None = None, reverse_sort: bool | int | None = None, nulls_first: bool | int | None = None, hashable: bool | int | None = None) -> None: ...  # noqa: E501


class StatsElem(Node):
    name: str | None
    expr: Node | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, expr: Node | _NodePayload | None = None) -> None: ...  # noqa: E501


class String(Node):
    sval: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, sval: str | None = None) -> None: ...  # noqa: E501


class SubLink(Expr):
    subLinkType: enums.SubLinkType | None
    subLinkId: int | None
    testexpr: Node | None
    operName: tuple[Any, ...] | None
    subselect: Node | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, subLinkType: enums.SubLinkType | int | str | dict[str, Any] | None = None, subLinkId: int | None = None, testexpr: Node | _NodePayload | None = None, operName: _ListInput | None = None, subselect: Node | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class SubPlan(Expr):
    subLinkType: enums.SubLinkType | None
    testexpr: Node | None
    paramIds: tuple[Any, ...] | None
    plan_id: int | None
    plan_name: str | None
    firstColTypmod: int | None
    useHashTable: bool | None
    unknownEqFalse: bool | None
    parallel_safe: bool | None
    setParam: tuple[Any, ...] | None
    parParam: tuple[Any, ...] | None
    args: tuple[Any, ...] | None
    startup_cost: float | None
    per_call_cost: float | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, subLinkType: enums.SubLinkType | int | str | dict[str, Any] | None = None, testexpr: Node | _NodePayload | None = None, paramIds: _ListInput | None = None, plan_id: int | None = None, plan_name: str | None = None, firstColTypmod: int | None = None, useHashTable: bool | int | None = None, unknownEqFalse: bool | int | None = None, parallel_safe: bool | int | None = None, setParam: _ListInput | None = None, parParam: _ListInput | None = None, args: _ListInput | None = None, startup_cost: float | None = None, per_call_cost: float | None = None) -> None: ...  # noqa: E501


class SubscriptingRef(Expr):
    reftypmod: int | None
    refupperindexpr: tuple[Any, ...] | None
    reflowerindexpr: tuple[Any, ...] | None
    refexpr: Expr | None
    refassgnexpr: Expr | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, reftypmod: int | None = None, refupperindexpr: _ListInput | None = None, reflowerindexpr: _ListInput | None = None, refexpr: Expr | _NodePayload | None = None, refassgnexpr: Expr | _NodePayload | None = None) -> None: ...  # noqa: E501


class TableFunc(Node):
    functype: enums.TableFuncType | None
    ns_uris: tuple[Any, ...] | None
    ns_names: tuple[Any, ...] | None
    docexpr: Node | None
    rowexpr: Node | None
    colnames: tuple[Any, ...] | None
    coltypes: tuple[Any, ...] | None
    coltypmods: tuple[Any, ...] | None
    colcollations: tuple[Any, ...] | None
    colexprs: tuple[Any, ...] | None
    coldefexprs: tuple[Any, ...] | None
    colvalexprs: tuple[Any, ...] | None
    passingvalexprs: tuple[Any, ...] | None
    notnulls: set[int] | None
    plan: Node | None
    ordinalitycol: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, functype: enums.TableFuncType | int | str | dict[str, Any] | None = None, ns_uris: _ListInput | None = None, ns_names: _ListInput | None = None, docexpr: Node | _NodePayload | None = None, rowexpr: Node | _NodePayload | None = None, colnames: _ListInput | None = None, coltypes: _ListInput | None = None, coltypmods: _ListInput | None = None, colcollations: _ListInput | None = None, colexprs: _ListInput | None = None, coldefexprs: _ListInput | None = None, colvalexprs: _ListInput | None = None, passingvalexprs: _ListInput | None = None, notnulls: _BitmapsetInput | None = None, plan: Node | _NodePayload | None = None, ordinalitycol: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class TableLikeClause(Node):
    relation: RangeVar | None
    options: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, options: int | None = None) -> None: ...  # noqa: E501


class TableSampleClause(Node):
    args: tuple[Any, ...] | None
    repeatable: Expr | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, args: _ListInput | None = None, repeatable: Expr | _NodePayload | None = None) -> None: ...  # noqa: E501


class TargetEntry(Expr):
    expr: Expr | None
    resno: int | None
    resname: str | None
    ressortgroupref: int | None
    resorigcol: int | None
    resjunk: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, expr: Expr | _NodePayload | None = None, resno: int | None = None, resname: str | None = None, ressortgroupref: int | None = None, resorigcol: int | None = None, resjunk: bool | int | None = None) -> None: ...  # noqa: E501


class TransactionStmt(Node):
    kind: enums.TransactionStmtKind | None
    options: tuple[Any, ...] | None
    savepoint_name: str | None
    gid: str | None
    chain: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.TransactionStmtKind | int | str | dict[str, Any] | None = None, options: _ListInput | None = None, savepoint_name: str | None = None, gid: str | None = None, chain: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class TriggerTransition(Node):
    name: str | None
    isNew: bool | None
    isTable: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, isNew: bool | int | None = None, isTable: bool | int | None = None) -> None: ...  # noqa: E501


class TruncateStmt(Node):
    relations: tuple[Any, ...] | None
    restart_seqs: bool | None
    behavior: enums.DropBehavior | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relations: _ListInput | None = None, restart_seqs: bool | int | None = None, behavior: enums.DropBehavior | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class TypeCast(Node):
    arg: Node | None
    typeName: TypeName | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, arg: Node | _NodePayload | None = None, typeName: TypeName | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class TypeName(Node):
    names: tuple[Any, ...] | None
    setof: bool | None
    pct_type: bool | None
    typmods: tuple[Any, ...] | None
    typemod: int | None
    arrayBounds: tuple[Any, ...] | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, names: _ListInput | None = None, setof: bool | int | None = None, pct_type: bool | int | None = None, typmods: _ListInput | None = None, typemod: int | None = None, arrayBounds: _ListInput | None = None, location: int | None = None) -> None: ...  # noqa: E501


class UnlistenStmt(Node):
    conditionname: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, conditionname: str | None = None) -> None: ...  # noqa: E501


class UpdateStmt(Node):
    relation: RangeVar | None
    targetList: tuple[Any, ...] | None
    whereClause: Node | None
    fromClause: tuple[Any, ...] | None
    returningClause: ReturningClause | None
    withClause: WithClause | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, targetList: _ListInput | None = None, whereClause: Node | _NodePayload | None = None, fromClause: _ListInput | None = None, returningClause: ReturningClause | _NodePayload | None = None, withClause: WithClause | _NodePayload | None = None) -> None: ...  # noqa: E501


class VacuumRelation(Node):
    relation: RangeVar | None
    va_cols: tuple[Any, ...] | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, relation: RangeVar | _NodePayload | None = None, va_cols: _ListInput | None = None) -> None: ...  # noqa: E501


class VacuumStmt(Node):
    options: tuple[Any, ...] | None
    rels: tuple[Any, ...] | None
    is_vacuumcmd: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, options: _ListInput | None = None, rels: _ListInput | None = None, is_vacuumcmd: bool | int | None = None) -> None: ...  # noqa: E501


class Var(Expr):
    varno: int | None
    varattno: int | None
    vartypmod: int | None
    varnullingrels: set[int] | None
    varlevelsup: int | None
    varreturningtype: enums.VarReturningType | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, varno: int | None = None, varattno: int | None = None, vartypmod: int | None = None, varnullingrels: _BitmapsetInput | None = None, varlevelsup: int | None = None, varreturningtype: enums.VarReturningType | int | str | dict[str, Any] | None = None, location: int | None = None) -> None: ...  # noqa: E501


class VariableSetStmt(Node):
    kind: enums.VariableSetKind | None
    name: str | None
    args: tuple[Any, ...] | None
    jumble_args: bool | None
    is_local: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.VariableSetKind | int | str | dict[str, Any] | None = None, name: str | None = None, args: _ListInput | None = None, jumble_args: bool | int | None = None, is_local: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class VariableShowStmt(Node):
    name: str | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None) -> None: ...  # noqa: E501


class ViewStmt(Node):
    view: RangeVar | None
    aliases: tuple[Any, ...] | None
    query: Node | None
    replace: bool | None
    options: tuple[Any, ...] | None
    withCheckOption: enums.ViewCheckOption | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, view: RangeVar | _NodePayload | None = None, aliases: _ListInput | None = None, query: Node | _NodePayload | None = None, replace: bool | int | None = None, options: _ListInput | None = None, withCheckOption: enums.ViewCheckOption | int | str | dict[str, Any] | None = None) -> None: ...  # noqa: E501


class WindowClause(Node):
    name: str | None
    refname: str | None
    partitionClause: tuple[Any, ...] | None
    orderClause: tuple[Any, ...] | None
    frameOptions: int | None
    startOffset: Node | None
    endOffset: Node | None
    inRangeAsc: bool | None
    inRangeNullsFirst: bool | None
    winref: int | None
    copiedOrder: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, refname: str | None = None, partitionClause: _ListInput | None = None, orderClause: _ListInput | None = None, frameOptions: int | None = None, startOffset: Node | _NodePayload | None = None, endOffset: Node | _NodePayload | None = None, inRangeAsc: bool | int | None = None, inRangeNullsFirst: bool | int | None = None, winref: int | None = None, copiedOrder: bool | int | None = None) -> None: ...  # noqa: E501


class WindowDef(Node):
    name: str | None
    refname: str | None
    partitionClause: tuple[Any, ...] | None
    orderClause: tuple[Any, ...] | None
    frameOptions: int | None
    startOffset: Node | None
    endOffset: Node | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, name: str | None = None, refname: str | None = None, partitionClause: _ListInput | None = None, orderClause: _ListInput | None = None, frameOptions: int | None = None, startOffset: Node | _NodePayload | None = None, endOffset: Node | _NodePayload | None = None, location: int | None = None) -> None: ...  # noqa: E501


class WindowFunc(Expr):
    args: tuple[Any, ...] | None
    aggfilter: Expr | None
    runCondition: tuple[Any, ...] | None
    winref: int | None
    winstar: bool | None
    winagg: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, args: _ListInput | None = None, aggfilter: Expr | _NodePayload | None = None, runCondition: _ListInput | None = None, winref: int | None = None, winstar: bool | int | None = None, winagg: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class WindowFuncRunCondition(Expr):
    wfunc_left: bool | None
    arg: Expr | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, wfunc_left: bool | int | None = None, arg: Expr | _NodePayload | None = None) -> None: ...  # noqa: E501


class WithCheckOption(Node):
    kind: enums.WCOKind | None
    relname: str | None
    polname: str | None
    qual: Node | None
    cascaded: bool | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, kind: enums.WCOKind | int | str | dict[str, Any] | None = None, relname: str | None = None, polname: str | None = None, qual: Node | _NodePayload | None = None, cascaded: bool | int | None = None) -> None: ...  # noqa: E501


class WithClause(Node):
    ctes: tuple[Any, ...] | None
    recursive: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, ctes: _ListInput | None = None, recursive: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class XmlExpr(Expr):
    op: enums.XmlExprOp | None
    name: str | None
    named_args: tuple[Any, ...] | None
    arg_names: tuple[Any, ...] | None
    args: tuple[Any, ...] | None
    xmloption: enums.XmlOptionType | None
    indent: bool | None
    typmod: int | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, op: enums.XmlExprOp | int | str | dict[str, Any] | None = None, name: str | None = None, named_args: _ListInput | None = None, arg_names: _ListInput | None = None, args: _ListInput | None = None, xmloption: enums.XmlOptionType | int | str | dict[str, Any] | None = None, indent: bool | int | None = None, typmod: int | None = None, location: int | None = None) -> None: ...  # noqa: E501


class XmlSerialize(Node):
    xmloption: enums.XmlOptionType | None
    expr: Node | None
    typeName: TypeName | None
    indent: bool | None
    location: int | None
    @overload
    def __init__(self, data: _NodePayload, /) -> None: ...
    @overload
    def __init__(self, xmloption: enums.XmlOptionType | int | str | dict[str, Any] | None = None, expr: Node | _NodePayload | None = None, typeName: TypeName | _NodePayload | None = None, indent: bool | int | None = None, location: int | None = None) -> None: ...  # noqa: E501
