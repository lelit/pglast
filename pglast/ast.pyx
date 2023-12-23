# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from struct_defs.json @ 16-5.0.0-0-g2a00188
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021-2023 Lele Gaifax
#

#cython: language_level=3

from cpython.ref cimport Py_INCREF
from cpython.tuple cimport PyTuple_New, PyTuple_SET_ITEM

from pglast import ast, enums
from pglast cimport structs


cdef _pg_bitmapset_to_set(const structs.Bitmapset* bms):
    cdef set result
    cdef int m
    if bms is not NULL:
        result = set()
        m = structs.bms_next_member(bms, -1)
        while m >= 0:
            result.add(m)
            m = structs.bms_next_member(bms, m)
    else:
        result = None
    return result


cdef _pg_list_to_tuple(const structs.List* lst, offset_to_index):
    cdef tuple result
    cdef int i
    if lst is not NULL:
        result = PyTuple_New(lst.length)
        for i in range(lst.length):
            item = create(structs.list_nth(lst, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(result, i, item)
    else:
        result = None
    return result


cdef create_Query(structs.Query* data, offset_to_index):
    cdef object v_commandType = getattr(enums, 'CmdType')(data.commandType)
    cdef object v_querySource = getattr(enums, 'QuerySource')(data.querySource)
    cdef object v_canSetTag = bool(data.canSetTag)
    cdef object v_utilityStmt = create(data.utilityStmt, offset_to_index) if data.utilityStmt is not NULL else None
    cdef object v_resultRelation = data.resultRelation
    cdef object v_hasAggs = bool(data.hasAggs)
    cdef object v_hasWindowFuncs = bool(data.hasWindowFuncs)
    cdef object v_hasTargetSRFs = bool(data.hasTargetSRFs)
    cdef object v_hasSubLinks = bool(data.hasSubLinks)
    cdef object v_hasDistinctOn = bool(data.hasDistinctOn)
    cdef object v_hasRecursive = bool(data.hasRecursive)
    cdef object v_hasModifyingCTE = bool(data.hasModifyingCTE)
    cdef object v_hasForUpdate = bool(data.hasForUpdate)
    cdef object v_hasRowSecurity = bool(data.hasRowSecurity)
    cdef object v_isReturn = bool(data.isReturn)
    cdef tuple v_cteList = _pg_list_to_tuple(data.cteList, offset_to_index)
    cdef tuple v_rtable = _pg_list_to_tuple(data.rtable, offset_to_index)
    cdef tuple v_rteperminfos = _pg_list_to_tuple(data.rteperminfos, offset_to_index)
    cdef object v_jointree = create(data.jointree, offset_to_index) if data.jointree is not NULL else None
    cdef tuple v_mergeActionList = _pg_list_to_tuple(data.mergeActionList, offset_to_index)
    cdef object v_mergeUseOuterJoin = bool(data.mergeUseOuterJoin)
    cdef tuple v_targetList = _pg_list_to_tuple(data.targetList, offset_to_index)
    cdef object v_override = getattr(enums, 'OverridingKind')(data.override)
    cdef object v_onConflict = create(data.onConflict, offset_to_index) if data.onConflict is not NULL else None
    cdef tuple v_returningList = _pg_list_to_tuple(data.returningList, offset_to_index)
    cdef tuple v_groupClause = _pg_list_to_tuple(data.groupClause, offset_to_index)
    cdef object v_groupDistinct = bool(data.groupDistinct)
    cdef tuple v_groupingSets = _pg_list_to_tuple(data.groupingSets, offset_to_index)
    cdef object v_havingQual = create(data.havingQual, offset_to_index) if data.havingQual is not NULL else None
    cdef tuple v_windowClause = _pg_list_to_tuple(data.windowClause, offset_to_index)
    cdef tuple v_distinctClause = _pg_list_to_tuple(data.distinctClause, offset_to_index)
    cdef tuple v_sortClause = _pg_list_to_tuple(data.sortClause, offset_to_index)
    cdef object v_limitOffset = create(data.limitOffset, offset_to_index) if data.limitOffset is not NULL else None
    cdef object v_limitCount = create(data.limitCount, offset_to_index) if data.limitCount is not NULL else None
    cdef object v_limitOption = getattr(enums, 'LimitOption')(data.limitOption)
    cdef tuple v_rowMarks = _pg_list_to_tuple(data.rowMarks, offset_to_index)
    cdef object v_setOperations = create(data.setOperations, offset_to_index) if data.setOperations is not NULL else None
    cdef tuple v_constraintDeps = _pg_list_to_tuple(data.constraintDeps, offset_to_index)
    cdef tuple v_withCheckOptions = _pg_list_to_tuple(data.withCheckOptions, offset_to_index)
    cdef object v_stmt_location = offset_to_index(data.stmt_location)
    cdef object v_stmt_len = offset_to_index(data.stmt_location + data.stmt_len) - offset_to_index(data.stmt_location)
    return ast.Query(v_commandType, v_querySource, v_canSetTag, v_utilityStmt, v_resultRelation, v_hasAggs, v_hasWindowFuncs, v_hasTargetSRFs, v_hasSubLinks, v_hasDistinctOn, v_hasRecursive, v_hasModifyingCTE, v_hasForUpdate, v_hasRowSecurity, v_isReturn, v_cteList, v_rtable, v_rteperminfos, v_jointree, v_mergeActionList, v_mergeUseOuterJoin, v_targetList, v_override, v_onConflict, v_returningList, v_groupClause, v_groupDistinct, v_groupingSets, v_havingQual, v_windowClause, v_distinctClause, v_sortClause, v_limitOffset, v_limitCount, v_limitOption, v_rowMarks, v_setOperations, v_constraintDeps, v_withCheckOptions, v_stmt_location, v_stmt_len)


cdef create_TypeName(structs.TypeName* data, offset_to_index):
    cdef tuple v_names = _pg_list_to_tuple(data.names, offset_to_index)
    cdef object v_setof = bool(data.setof)
    cdef object v_pct_type = bool(data.pct_type)
    cdef tuple v_typmods = _pg_list_to_tuple(data.typmods, offset_to_index)
    cdef object v_typemod = data.typemod
    cdef tuple v_arrayBounds = _pg_list_to_tuple(data.arrayBounds, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.TypeName(v_names, v_setof, v_pct_type, v_typmods, v_typemod, v_arrayBounds, v_location)


cdef create_ColumnRef(structs.ColumnRef* data, offset_to_index):
    cdef tuple v_fields = _pg_list_to_tuple(data.fields, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.ColumnRef(v_fields, v_location)


cdef create_ParamRef(structs.ParamRef* data, offset_to_index):
    cdef object v_number = data.number
    cdef object v_location = offset_to_index(data.location)
    return ast.ParamRef(v_number, v_location)


cdef create_A_Expr(structs.A_Expr* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'A_Expr_Kind')(data.kind)
    cdef tuple v_name = _pg_list_to_tuple(data.name, offset_to_index)
    cdef object v_lexpr = create(data.lexpr, offset_to_index) if data.lexpr is not NULL else None
    cdef object v_rexpr = create(data.rexpr, offset_to_index) if data.rexpr is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.A_Expr(v_kind, v_name, v_lexpr, v_rexpr, v_location)


cdef create_TypeCast(structs.TypeCast* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_typeName = create(data.typeName, offset_to_index) if data.typeName is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.TypeCast(v_arg, v_typeName, v_location)


cdef create_CollateClause(structs.CollateClause* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef tuple v_collname = _pg_list_to_tuple(data.collname, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.CollateClause(v_arg, v_collname, v_location)


cdef create_RoleSpec(structs.RoleSpec* data, offset_to_index):
    cdef object v_roletype = getattr(enums, 'RoleSpecType')(data.roletype)
    cdef object v_rolename = data.rolename.decode("utf-8") if data.rolename is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.RoleSpec(v_roletype, v_rolename, v_location)


cdef create_FuncCall(structs.FuncCall* data, offset_to_index):
    cdef tuple v_funcname = _pg_list_to_tuple(data.funcname, offset_to_index)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef tuple v_agg_order = _pg_list_to_tuple(data.agg_order, offset_to_index)
    cdef object v_agg_filter = create(data.agg_filter, offset_to_index) if data.agg_filter is not NULL else None
    cdef object v_over = create(data.over, offset_to_index) if data.over is not NULL else None
    cdef object v_agg_within_group = bool(data.agg_within_group)
    cdef object v_agg_star = bool(data.agg_star)
    cdef object v_agg_distinct = bool(data.agg_distinct)
    cdef object v_func_variadic = bool(data.func_variadic)
    cdef object v_funcformat = getattr(enums, 'CoercionForm')(data.funcformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.FuncCall(v_funcname, v_args, v_agg_order, v_agg_filter, v_over, v_agg_within_group, v_agg_star, v_agg_distinct, v_func_variadic, v_funcformat, v_location)


cdef create_A_Star(structs.A_Star* data, offset_to_index):
    return ast.A_Star()


cdef create_A_Indices(structs.A_Indices* data, offset_to_index):
    cdef object v_is_slice = bool(data.is_slice)
    cdef object v_lidx = create(data.lidx, offset_to_index) if data.lidx is not NULL else None
    cdef object v_uidx = create(data.uidx, offset_to_index) if data.uidx is not NULL else None
    return ast.A_Indices(v_is_slice, v_lidx, v_uidx)


cdef create_A_Indirection(structs.A_Indirection* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef tuple v_indirection = _pg_list_to_tuple(data.indirection, offset_to_index)
    return ast.A_Indirection(v_arg, v_indirection)


cdef create_A_ArrayExpr(structs.A_ArrayExpr* data, offset_to_index):
    cdef tuple v_elements = _pg_list_to_tuple(data.elements, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.A_ArrayExpr(v_elements, v_location)


cdef create_ResTarget(structs.ResTarget* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef tuple v_indirection = _pg_list_to_tuple(data.indirection, offset_to_index)
    cdef object v_val = create(data.val, offset_to_index) if data.val is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.ResTarget(v_name, v_indirection, v_val, v_location)


cdef create_MultiAssignRef(structs.MultiAssignRef* data, offset_to_index):
    cdef object v_source = create(data.source, offset_to_index) if data.source is not NULL else None
    cdef object v_colno = data.colno
    cdef object v_ncolumns = data.ncolumns
    return ast.MultiAssignRef(v_source, v_colno, v_ncolumns)


cdef create_SortBy(structs.SortBy* data, offset_to_index):
    cdef object v_node = create(data.node, offset_to_index) if data.node is not NULL else None
    cdef object v_sortby_dir = getattr(enums, 'SortByDir')(data.sortby_dir)
    cdef object v_sortby_nulls = getattr(enums, 'SortByNulls')(data.sortby_nulls)
    cdef tuple v_useOp = _pg_list_to_tuple(data.useOp, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.SortBy(v_node, v_sortby_dir, v_sortby_nulls, v_useOp, v_location)


cdef create_WindowDef(structs.WindowDef* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_refname = data.refname.decode("utf-8") if data.refname is not NULL else None
    cdef tuple v_partitionClause = _pg_list_to_tuple(data.partitionClause, offset_to_index)
    cdef tuple v_orderClause = _pg_list_to_tuple(data.orderClause, offset_to_index)
    cdef object v_frameOptions = data.frameOptions
    cdef object v_startOffset = create(data.startOffset, offset_to_index) if data.startOffset is not NULL else None
    cdef object v_endOffset = create(data.endOffset, offset_to_index) if data.endOffset is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.WindowDef(v_name, v_refname, v_partitionClause, v_orderClause, v_frameOptions, v_startOffset, v_endOffset, v_location)


cdef create_RangeSubselect(structs.RangeSubselect* data, offset_to_index):
    cdef object v_lateral = bool(data.lateral)
    cdef object v_subquery = create(data.subquery, offset_to_index) if data.subquery is not NULL else None
    cdef object v_alias = create(data.alias, offset_to_index) if data.alias is not NULL else None
    return ast.RangeSubselect(v_lateral, v_subquery, v_alias)


cdef create_RangeFunction(structs.RangeFunction* data, offset_to_index):
    cdef object v_lateral = bool(data.lateral)
    cdef object v_ordinality = bool(data.ordinality)
    cdef object v_is_rowsfrom = bool(data.is_rowsfrom)
    cdef tuple v_functions = _pg_list_to_tuple(data.functions, offset_to_index)
    cdef object v_alias = create(data.alias, offset_to_index) if data.alias is not NULL else None
    cdef tuple v_coldeflist = _pg_list_to_tuple(data.coldeflist, offset_to_index)
    return ast.RangeFunction(v_lateral, v_ordinality, v_is_rowsfrom, v_functions, v_alias, v_coldeflist)


cdef create_RangeTableFunc(structs.RangeTableFunc* data, offset_to_index):
    cdef object v_lateral = bool(data.lateral)
    cdef object v_docexpr = create(data.docexpr, offset_to_index) if data.docexpr is not NULL else None
    cdef object v_rowexpr = create(data.rowexpr, offset_to_index) if data.rowexpr is not NULL else None
    cdef tuple v_namespaces = _pg_list_to_tuple(data.namespaces, offset_to_index)
    cdef tuple v_columns = _pg_list_to_tuple(data.columns, offset_to_index)
    cdef object v_alias = create(data.alias, offset_to_index) if data.alias is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.RangeTableFunc(v_lateral, v_docexpr, v_rowexpr, v_namespaces, v_columns, v_alias, v_location)


cdef create_RangeTableFuncCol(structs.RangeTableFuncCol* data, offset_to_index):
    cdef object v_colname = data.colname.decode("utf-8") if data.colname is not NULL else None
    cdef object v_typeName = create(data.typeName, offset_to_index) if data.typeName is not NULL else None
    cdef object v_for_ordinality = bool(data.for_ordinality)
    cdef object v_is_not_null = bool(data.is_not_null)
    cdef object v_colexpr = create(data.colexpr, offset_to_index) if data.colexpr is not NULL else None
    cdef object v_coldefexpr = create(data.coldefexpr, offset_to_index) if data.coldefexpr is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.RangeTableFuncCol(v_colname, v_typeName, v_for_ordinality, v_is_not_null, v_colexpr, v_coldefexpr, v_location)


cdef create_RangeTableSample(structs.RangeTableSample* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef tuple v_method = _pg_list_to_tuple(data.method, offset_to_index)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_repeatable = create(data.repeatable, offset_to_index) if data.repeatable is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.RangeTableSample(v_relation, v_method, v_args, v_repeatable, v_location)


cdef create_ColumnDef(structs.ColumnDef* data, offset_to_index):
    cdef object v_colname = data.colname.decode("utf-8") if data.colname is not NULL else None
    cdef object v_typeName = create(data.typeName, offset_to_index) if data.typeName is not NULL else None
    cdef object v_compression = data.compression.decode("utf-8") if data.compression is not NULL else None
    cdef object v_inhcount = data.inhcount
    cdef object v_is_local = bool(data.is_local)
    cdef object v_is_not_null = bool(data.is_not_null)
    cdef object v_is_from_type = bool(data.is_from_type)
    cdef object v_storage = chr(data.storage)
    cdef object v_storage_name = data.storage_name.decode("utf-8") if data.storage_name is not NULL else None
    cdef object v_raw_default = create(data.raw_default, offset_to_index) if data.raw_default is not NULL else None
    cdef object v_cooked_default = create(data.cooked_default, offset_to_index) if data.cooked_default is not NULL else None
    cdef object v_identity = chr(data.identity)
    cdef object v_identitySequence = create(data.identitySequence, offset_to_index) if data.identitySequence is not NULL else None
    cdef object v_generated = chr(data.generated)
    cdef object v_collClause = create(data.collClause, offset_to_index) if data.collClause is not NULL else None
    cdef tuple v_constraints = _pg_list_to_tuple(data.constraints, offset_to_index)
    cdef tuple v_fdwoptions = _pg_list_to_tuple(data.fdwoptions, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.ColumnDef(v_colname, v_typeName, v_compression, v_inhcount, v_is_local, v_is_not_null, v_is_from_type, v_storage, v_storage_name, v_raw_default, v_cooked_default, v_identity, v_identitySequence, v_generated, v_collClause, v_constraints, v_fdwoptions, v_location)


cdef create_TableLikeClause(structs.TableLikeClause* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_options = data.options
    return ast.TableLikeClause(v_relation, v_options)


cdef create_IndexElem(structs.IndexElem* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_expr = create(data.expr, offset_to_index) if data.expr is not NULL else None
    cdef object v_indexcolname = data.indexcolname.decode("utf-8") if data.indexcolname is not NULL else None
    cdef tuple v_collation = _pg_list_to_tuple(data.collation, offset_to_index)
    cdef tuple v_opclass = _pg_list_to_tuple(data.opclass, offset_to_index)
    cdef tuple v_opclassopts = _pg_list_to_tuple(data.opclassopts, offset_to_index)
    cdef object v_ordering = getattr(enums, 'SortByDir')(data.ordering)
    cdef object v_nulls_ordering = getattr(enums, 'SortByNulls')(data.nulls_ordering)
    return ast.IndexElem(v_name, v_expr, v_indexcolname, v_collation, v_opclass, v_opclassopts, v_ordering, v_nulls_ordering)


cdef create_DefElem(structs.DefElem* data, offset_to_index):
    cdef object v_defnamespace = data.defnamespace.decode("utf-8") if data.defnamespace is not NULL else None
    cdef object v_defname = data.defname.decode("utf-8") if data.defname is not NULL else None
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_defaction = getattr(enums, 'DefElemAction')(data.defaction)
    cdef object v_location = offset_to_index(data.location)
    return ast.DefElem(v_defnamespace, v_defname, v_arg, v_defaction, v_location)


cdef create_LockingClause(structs.LockingClause* data, offset_to_index):
    cdef tuple v_lockedRels = _pg_list_to_tuple(data.lockedRels, offset_to_index)
    cdef object v_strength = getattr(enums, 'LockClauseStrength')(data.strength)
    cdef object v_waitPolicy = getattr(enums, 'LockWaitPolicy')(data.waitPolicy)
    return ast.LockingClause(v_lockedRels, v_strength, v_waitPolicy)


cdef create_XmlSerialize(structs.XmlSerialize* data, offset_to_index):
    cdef object v_xmloption = getattr(enums, 'XmlOptionType')(data.xmloption)
    cdef object v_expr = create(data.expr, offset_to_index) if data.expr is not NULL else None
    cdef object v_typeName = create(data.typeName, offset_to_index) if data.typeName is not NULL else None
    cdef object v_indent = bool(data.indent)
    cdef object v_location = offset_to_index(data.location)
    return ast.XmlSerialize(v_xmloption, v_expr, v_typeName, v_indent, v_location)


cdef create_PartitionElem(structs.PartitionElem* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_expr = create(data.expr, offset_to_index) if data.expr is not NULL else None
    cdef tuple v_collation = _pg_list_to_tuple(data.collation, offset_to_index)
    cdef tuple v_opclass = _pg_list_to_tuple(data.opclass, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.PartitionElem(v_name, v_expr, v_collation, v_opclass, v_location)


cdef create_PartitionSpec(structs.PartitionSpec* data, offset_to_index):
    cdef object v_strategy = getattr(enums, 'PartitionStrategy')(chr(data.strategy))
    cdef tuple v_partParams = _pg_list_to_tuple(data.partParams, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.PartitionSpec(v_strategy, v_partParams, v_location)


cdef create_PartitionBoundSpec(structs.PartitionBoundSpec* data, offset_to_index):
    cdef object v_strategy = chr(data.strategy)
    cdef object v_is_default = bool(data.is_default)
    cdef object v_modulus = data.modulus
    cdef object v_remainder = data.remainder
    cdef tuple v_listdatums = _pg_list_to_tuple(data.listdatums, offset_to_index)
    cdef tuple v_lowerdatums = _pg_list_to_tuple(data.lowerdatums, offset_to_index)
    cdef tuple v_upperdatums = _pg_list_to_tuple(data.upperdatums, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.PartitionBoundSpec(v_strategy, v_is_default, v_modulus, v_remainder, v_listdatums, v_lowerdatums, v_upperdatums, v_location)


cdef create_PartitionRangeDatum(structs.PartitionRangeDatum* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'PartitionRangeDatumKind')(data.kind)
    cdef object v_value = create(data.value, offset_to_index) if data.value is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.PartitionRangeDatum(v_kind, v_value, v_location)


cdef create_PartitionCmd(structs.PartitionCmd* data, offset_to_index):
    cdef object v_name = create(data.name, offset_to_index) if data.name is not NULL else None
    cdef object v_bound = create(data.bound, offset_to_index) if data.bound is not NULL else None
    cdef object v_concurrent = bool(data.concurrent)
    return ast.PartitionCmd(v_name, v_bound, v_concurrent)


cdef create_RangeTblEntry(structs.RangeTblEntry* data, offset_to_index):
    cdef object v_rtekind = getattr(enums, 'RTEKind')(data.rtekind)
    cdef object v_relkind = chr(data.relkind)
    cdef object v_rellockmode = data.rellockmode
    cdef object v_tablesample = create(data.tablesample, offset_to_index) if data.tablesample is not NULL else None
    cdef object v_perminfoindex = data.perminfoindex
    cdef object v_subquery = create(data.subquery, offset_to_index) if data.subquery is not NULL else None
    cdef object v_security_barrier = bool(data.security_barrier)
    cdef object v_jointype = getattr(enums, 'JoinType')(data.jointype)
    cdef object v_joinmergedcols = data.joinmergedcols
    cdef tuple v_joinaliasvars = _pg_list_to_tuple(data.joinaliasvars, offset_to_index)
    cdef tuple v_joinleftcols = _pg_list_to_tuple(data.joinleftcols, offset_to_index)
    cdef tuple v_joinrightcols = _pg_list_to_tuple(data.joinrightcols, offset_to_index)
    cdef object v_join_using_alias = create(data.join_using_alias, offset_to_index) if data.join_using_alias is not NULL else None
    cdef tuple v_functions = _pg_list_to_tuple(data.functions, offset_to_index)
    cdef object v_funcordinality = bool(data.funcordinality)
    cdef object v_tablefunc = create(data.tablefunc, offset_to_index) if data.tablefunc is not NULL else None
    cdef tuple v_values_lists = _pg_list_to_tuple(data.values_lists, offset_to_index)
    cdef object v_ctename = data.ctename.decode("utf-8") if data.ctename is not NULL else None
    cdef object v_ctelevelsup = data.ctelevelsup
    cdef object v_self_reference = bool(data.self_reference)
    cdef tuple v_coltypes = _pg_list_to_tuple(data.coltypes, offset_to_index)
    cdef tuple v_coltypmods = _pg_list_to_tuple(data.coltypmods, offset_to_index)
    cdef tuple v_colcollations = _pg_list_to_tuple(data.colcollations, offset_to_index)
    cdef object v_enrname = data.enrname.decode("utf-8") if data.enrname is not NULL else None
    cdef object v_enrtuples = data.enrtuples
    cdef object v_alias = create(data.alias, offset_to_index) if data.alias is not NULL else None
    cdef object v_eref = create(data.eref, offset_to_index) if data.eref is not NULL else None
    cdef object v_lateral = bool(data.lateral)
    cdef object v_inh = bool(data.inh)
    cdef object v_inFromCl = bool(data.inFromCl)
    cdef tuple v_securityQuals = _pg_list_to_tuple(data.securityQuals, offset_to_index)
    return ast.RangeTblEntry(v_rtekind, v_relkind, v_rellockmode, v_tablesample, v_perminfoindex, v_subquery, v_security_barrier, v_jointype, v_joinmergedcols, v_joinaliasvars, v_joinleftcols, v_joinrightcols, v_join_using_alias, v_functions, v_funcordinality, v_tablefunc, v_values_lists, v_ctename, v_ctelevelsup, v_self_reference, v_coltypes, v_coltypmods, v_colcollations, v_enrname, v_enrtuples, v_alias, v_eref, v_lateral, v_inh, v_inFromCl, v_securityQuals)


cdef create_RTEPermissionInfo(structs.RTEPermissionInfo* data, offset_to_index):
    cdef object v_inh = bool(data.inh)
    cdef object v_requiredPerms = data.requiredPerms
    cdef set v_selectedCols = _pg_bitmapset_to_set(data.selectedCols)
    cdef set v_insertedCols = _pg_bitmapset_to_set(data.insertedCols)
    cdef set v_updatedCols = _pg_bitmapset_to_set(data.updatedCols)
    return ast.RTEPermissionInfo(v_inh, v_requiredPerms, v_selectedCols, v_insertedCols, v_updatedCols)


cdef create_RangeTblFunction(structs.RangeTblFunction* data, offset_to_index):
    cdef object v_funcexpr = create(data.funcexpr, offset_to_index) if data.funcexpr is not NULL else None
    cdef object v_funccolcount = data.funccolcount
    cdef tuple v_funccolnames = _pg_list_to_tuple(data.funccolnames, offset_to_index)
    cdef tuple v_funccoltypes = _pg_list_to_tuple(data.funccoltypes, offset_to_index)
    cdef tuple v_funccoltypmods = _pg_list_to_tuple(data.funccoltypmods, offset_to_index)
    cdef tuple v_funccolcollations = _pg_list_to_tuple(data.funccolcollations, offset_to_index)
    cdef set v_funcparams = _pg_bitmapset_to_set(data.funcparams)
    return ast.RangeTblFunction(v_funcexpr, v_funccolcount, v_funccolnames, v_funccoltypes, v_funccoltypmods, v_funccolcollations, v_funcparams)


cdef create_TableSampleClause(structs.TableSampleClause* data, offset_to_index):
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_repeatable = create(data.repeatable, offset_to_index) if data.repeatable is not NULL else None
    return ast.TableSampleClause(v_args, v_repeatable)


cdef create_WithCheckOption(structs.WithCheckOption* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'WCOKind')(data.kind)
    cdef object v_relname = data.relname.decode("utf-8") if data.relname is not NULL else None
    cdef object v_polname = data.polname.decode("utf-8") if data.polname is not NULL else None
    cdef object v_qual = create(data.qual, offset_to_index) if data.qual is not NULL else None
    cdef object v_cascaded = bool(data.cascaded)
    return ast.WithCheckOption(v_kind, v_relname, v_polname, v_qual, v_cascaded)


cdef create_SortGroupClause(structs.SortGroupClause* data, offset_to_index):
    cdef object v_tleSortGroupRef = data.tleSortGroupRef
    cdef object v_nulls_first = bool(data.nulls_first)
    cdef object v_hashable = bool(data.hashable)
    return ast.SortGroupClause(v_tleSortGroupRef, v_nulls_first, v_hashable)


cdef create_GroupingSet(structs.GroupingSet* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'GroupingSetKind')(data.kind)
    cdef tuple v_content = _pg_list_to_tuple(data.content, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.GroupingSet(v_kind, v_content, v_location)


cdef create_WindowClause(structs.WindowClause* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_refname = data.refname.decode("utf-8") if data.refname is not NULL else None
    cdef tuple v_partitionClause = _pg_list_to_tuple(data.partitionClause, offset_to_index)
    cdef tuple v_orderClause = _pg_list_to_tuple(data.orderClause, offset_to_index)
    cdef object v_frameOptions = data.frameOptions
    cdef object v_startOffset = create(data.startOffset, offset_to_index) if data.startOffset is not NULL else None
    cdef object v_endOffset = create(data.endOffset, offset_to_index) if data.endOffset is not NULL else None
    cdef tuple v_runCondition = _pg_list_to_tuple(data.runCondition, offset_to_index)
    cdef object v_inRangeAsc = bool(data.inRangeAsc)
    cdef object v_inRangeNullsFirst = bool(data.inRangeNullsFirst)
    cdef object v_winref = data.winref
    cdef object v_copiedOrder = bool(data.copiedOrder)
    return ast.WindowClause(v_name, v_refname, v_partitionClause, v_orderClause, v_frameOptions, v_startOffset, v_endOffset, v_runCondition, v_inRangeAsc, v_inRangeNullsFirst, v_winref, v_copiedOrder)


cdef create_RowMarkClause(structs.RowMarkClause* data, offset_to_index):
    cdef object v_rti = data.rti
    cdef object v_strength = getattr(enums, 'LockClauseStrength')(data.strength)
    cdef object v_waitPolicy = getattr(enums, 'LockWaitPolicy')(data.waitPolicy)
    cdef object v_pushedDown = bool(data.pushedDown)
    return ast.RowMarkClause(v_rti, v_strength, v_waitPolicy, v_pushedDown)


cdef create_WithClause(structs.WithClause* data, offset_to_index):
    cdef tuple v_ctes = _pg_list_to_tuple(data.ctes, offset_to_index)
    cdef object v_recursive = bool(data.recursive)
    cdef object v_location = offset_to_index(data.location)
    return ast.WithClause(v_ctes, v_recursive, v_location)


cdef create_InferClause(structs.InferClause* data, offset_to_index):
    cdef tuple v_indexElems = _pg_list_to_tuple(data.indexElems, offset_to_index)
    cdef object v_whereClause = create(data.whereClause, offset_to_index) if data.whereClause is not NULL else None
    cdef object v_conname = data.conname.decode("utf-8") if data.conname is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.InferClause(v_indexElems, v_whereClause, v_conname, v_location)


cdef create_OnConflictClause(structs.OnConflictClause* data, offset_to_index):
    cdef object v_action = getattr(enums, 'OnConflictAction')(data.action)
    cdef object v_infer = create(data.infer, offset_to_index) if data.infer is not NULL else None
    cdef tuple v_targetList = _pg_list_to_tuple(data.targetList, offset_to_index)
    cdef object v_whereClause = create(data.whereClause, offset_to_index) if data.whereClause is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.OnConflictClause(v_action, v_infer, v_targetList, v_whereClause, v_location)


cdef create_CTESearchClause(structs.CTESearchClause* data, offset_to_index):
    cdef tuple v_search_col_list = _pg_list_to_tuple(data.search_col_list, offset_to_index)
    cdef object v_search_breadth_first = bool(data.search_breadth_first)
    cdef object v_search_seq_column = data.search_seq_column.decode("utf-8") if data.search_seq_column is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.CTESearchClause(v_search_col_list, v_search_breadth_first, v_search_seq_column, v_location)


cdef create_CTECycleClause(structs.CTECycleClause* data, offset_to_index):
    cdef tuple v_cycle_col_list = _pg_list_to_tuple(data.cycle_col_list, offset_to_index)
    cdef object v_cycle_mark_column = data.cycle_mark_column.decode("utf-8") if data.cycle_mark_column is not NULL else None
    cdef object v_cycle_mark_value = create(data.cycle_mark_value, offset_to_index) if data.cycle_mark_value is not NULL else None
    cdef object v_cycle_mark_default = create(data.cycle_mark_default, offset_to_index) if data.cycle_mark_default is not NULL else None
    cdef object v_cycle_path_column = data.cycle_path_column.decode("utf-8") if data.cycle_path_column is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    cdef object v_cycle_mark_typmod = data.cycle_mark_typmod
    return ast.CTECycleClause(v_cycle_col_list, v_cycle_mark_column, v_cycle_mark_value, v_cycle_mark_default, v_cycle_path_column, v_location, v_cycle_mark_typmod)


cdef create_CommonTableExpr(structs.CommonTableExpr* data, offset_to_index):
    cdef object v_ctename = data.ctename.decode("utf-8") if data.ctename is not NULL else None
    cdef tuple v_aliascolnames = _pg_list_to_tuple(data.aliascolnames, offset_to_index)
    cdef object v_ctematerialized = getattr(enums, 'CTEMaterialize')(data.ctematerialized)
    cdef object v_ctequery = create(data.ctequery, offset_to_index) if data.ctequery is not NULL else None
    cdef object v_search_clause = create(data.search_clause, offset_to_index) if data.search_clause is not NULL else None
    cdef object v_cycle_clause = create(data.cycle_clause, offset_to_index) if data.cycle_clause is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    cdef object v_cterecursive = bool(data.cterecursive)
    cdef object v_cterefcount = data.cterefcount
    cdef tuple v_ctecolnames = _pg_list_to_tuple(data.ctecolnames, offset_to_index)
    cdef tuple v_ctecoltypes = _pg_list_to_tuple(data.ctecoltypes, offset_to_index)
    cdef tuple v_ctecoltypmods = _pg_list_to_tuple(data.ctecoltypmods, offset_to_index)
    cdef tuple v_ctecolcollations = _pg_list_to_tuple(data.ctecolcollations, offset_to_index)
    return ast.CommonTableExpr(v_ctename, v_aliascolnames, v_ctematerialized, v_ctequery, v_search_clause, v_cycle_clause, v_location, v_cterecursive, v_cterefcount, v_ctecolnames, v_ctecoltypes, v_ctecoltypmods, v_ctecolcollations)


cdef create_MergeWhenClause(structs.MergeWhenClause* data, offset_to_index):
    cdef object v_matched = bool(data.matched)
    cdef object v_commandType = getattr(enums, 'CmdType')(data.commandType)
    cdef object v_override = getattr(enums, 'OverridingKind')(data.override)
    cdef object v_condition = create(data.condition, offset_to_index) if data.condition is not NULL else None
    cdef tuple v_targetList = _pg_list_to_tuple(data.targetList, offset_to_index)
    cdef tuple v_values = _pg_list_to_tuple(data.values, offset_to_index)
    return ast.MergeWhenClause(v_matched, v_commandType, v_override, v_condition, v_targetList, v_values)


cdef create_MergeAction(structs.MergeAction* data, offset_to_index):
    cdef object v_matched = bool(data.matched)
    cdef object v_commandType = getattr(enums, 'CmdType')(data.commandType)
    cdef object v_override = getattr(enums, 'OverridingKind')(data.override)
    cdef object v_qual = create(data.qual, offset_to_index) if data.qual is not NULL else None
    cdef tuple v_targetList = _pg_list_to_tuple(data.targetList, offset_to_index)
    cdef tuple v_updateColnos = _pg_list_to_tuple(data.updateColnos, offset_to_index)
    return ast.MergeAction(v_matched, v_commandType, v_override, v_qual, v_targetList, v_updateColnos)


cdef create_TriggerTransition(structs.TriggerTransition* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_isNew = bool(data.isNew)
    cdef object v_isTable = bool(data.isTable)
    return ast.TriggerTransition(v_name, v_isNew, v_isTable)


cdef create_JsonOutput(structs.JsonOutput* data, offset_to_index):
    cdef object v_typeName = create(data.typeName, offset_to_index) if data.typeName is not NULL else None
    cdef object v_returning = create(data.returning, offset_to_index) if data.returning is not NULL else None
    return ast.JsonOutput(v_typeName, v_returning)


cdef create_JsonKeyValue(structs.JsonKeyValue* data, offset_to_index):
    cdef object v_key = create(data.key, offset_to_index) if data.key is not NULL else None
    cdef object v_value = create(data.value, offset_to_index) if data.value is not NULL else None
    return ast.JsonKeyValue(v_key, v_value)


cdef create_JsonObjectConstructor(structs.JsonObjectConstructor* data, offset_to_index):
    cdef tuple v_exprs = _pg_list_to_tuple(data.exprs, offset_to_index)
    cdef object v_output = create(data.output, offset_to_index) if data.output is not NULL else None
    cdef object v_absent_on_null = bool(data.absent_on_null)
    cdef object v_unique = bool(data.unique)
    cdef object v_location = offset_to_index(data.location)
    return ast.JsonObjectConstructor(v_exprs, v_output, v_absent_on_null, v_unique, v_location)


cdef create_JsonArrayConstructor(structs.JsonArrayConstructor* data, offset_to_index):
    cdef tuple v_exprs = _pg_list_to_tuple(data.exprs, offset_to_index)
    cdef object v_output = create(data.output, offset_to_index) if data.output is not NULL else None
    cdef object v_absent_on_null = bool(data.absent_on_null)
    cdef object v_location = offset_to_index(data.location)
    return ast.JsonArrayConstructor(v_exprs, v_output, v_absent_on_null, v_location)


cdef create_JsonArrayQueryConstructor(structs.JsonArrayQueryConstructor* data, offset_to_index):
    cdef object v_query = create(data.query, offset_to_index) if data.query is not NULL else None
    cdef object v_output = create(data.output, offset_to_index) if data.output is not NULL else None
    cdef object v_format = create(data.format, offset_to_index) if data.format is not NULL else None
    cdef object v_absent_on_null = bool(data.absent_on_null)
    cdef object v_location = offset_to_index(data.location)
    return ast.JsonArrayQueryConstructor(v_query, v_output, v_format, v_absent_on_null, v_location)


cdef create_JsonAggConstructor(structs.JsonAggConstructor* data, offset_to_index):
    cdef object v_output = create(data.output, offset_to_index) if data.output is not NULL else None
    cdef object v_agg_filter = create(data.agg_filter, offset_to_index) if data.agg_filter is not NULL else None
    cdef tuple v_agg_order = _pg_list_to_tuple(data.agg_order, offset_to_index)
    cdef object v_over = create(data.over, offset_to_index) if data.over is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.JsonAggConstructor(v_output, v_agg_filter, v_agg_order, v_over, v_location)


cdef create_JsonObjectAgg(structs.JsonObjectAgg* data, offset_to_index):
    cdef object v_constructor = create(data.constructor, offset_to_index) if data.constructor is not NULL else None
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_absent_on_null = bool(data.absent_on_null)
    cdef object v_unique = bool(data.unique)
    return ast.JsonObjectAgg(v_constructor, v_arg, v_absent_on_null, v_unique)


cdef create_JsonArrayAgg(structs.JsonArrayAgg* data, offset_to_index):
    cdef object v_constructor = create(data.constructor, offset_to_index) if data.constructor is not NULL else None
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_absent_on_null = bool(data.absent_on_null)
    return ast.JsonArrayAgg(v_constructor, v_arg, v_absent_on_null)


cdef create_RawStmt(structs.RawStmt* data, offset_to_index):
    cdef object v_stmt = create(data.stmt, offset_to_index) if data.stmt is not NULL else None
    cdef object v_stmt_location = offset_to_index(data.stmt_location)
    cdef object v_stmt_len = offset_to_index(data.stmt_location + data.stmt_len) - offset_to_index(data.stmt_location)
    return ast.RawStmt(v_stmt, v_stmt_location, v_stmt_len)


cdef create_InsertStmt(structs.InsertStmt* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef tuple v_cols = _pg_list_to_tuple(data.cols, offset_to_index)
    cdef object v_selectStmt = create(data.selectStmt, offset_to_index) if data.selectStmt is not NULL else None
    cdef object v_onConflictClause = create(data.onConflictClause, offset_to_index) if data.onConflictClause is not NULL else None
    cdef tuple v_returningList = _pg_list_to_tuple(data.returningList, offset_to_index)
    cdef object v_withClause = create(data.withClause, offset_to_index) if data.withClause is not NULL else None
    cdef object v_override = getattr(enums, 'OverridingKind')(data.override)
    return ast.InsertStmt(v_relation, v_cols, v_selectStmt, v_onConflictClause, v_returningList, v_withClause, v_override)


cdef create_DeleteStmt(structs.DeleteStmt* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef tuple v_usingClause = _pg_list_to_tuple(data.usingClause, offset_to_index)
    cdef object v_whereClause = create(data.whereClause, offset_to_index) if data.whereClause is not NULL else None
    cdef tuple v_returningList = _pg_list_to_tuple(data.returningList, offset_to_index)
    cdef object v_withClause = create(data.withClause, offset_to_index) if data.withClause is not NULL else None
    return ast.DeleteStmt(v_relation, v_usingClause, v_whereClause, v_returningList, v_withClause)


cdef create_UpdateStmt(structs.UpdateStmt* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef tuple v_targetList = _pg_list_to_tuple(data.targetList, offset_to_index)
    cdef object v_whereClause = create(data.whereClause, offset_to_index) if data.whereClause is not NULL else None
    cdef tuple v_fromClause = _pg_list_to_tuple(data.fromClause, offset_to_index)
    cdef tuple v_returningList = _pg_list_to_tuple(data.returningList, offset_to_index)
    cdef object v_withClause = create(data.withClause, offset_to_index) if data.withClause is not NULL else None
    return ast.UpdateStmt(v_relation, v_targetList, v_whereClause, v_fromClause, v_returningList, v_withClause)


cdef create_MergeStmt(structs.MergeStmt* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_sourceRelation = create(data.sourceRelation, offset_to_index) if data.sourceRelation is not NULL else None
    cdef object v_joinCondition = create(data.joinCondition, offset_to_index) if data.joinCondition is not NULL else None
    cdef tuple v_mergeWhenClauses = _pg_list_to_tuple(data.mergeWhenClauses, offset_to_index)
    cdef object v_withClause = create(data.withClause, offset_to_index) if data.withClause is not NULL else None
    return ast.MergeStmt(v_relation, v_sourceRelation, v_joinCondition, v_mergeWhenClauses, v_withClause)


cdef create_SelectStmt(structs.SelectStmt* data, offset_to_index):
    cdef tuple v_distinctClause = _pg_list_to_tuple(data.distinctClause, offset_to_index)
    cdef object v_intoClause = create(data.intoClause, offset_to_index) if data.intoClause is not NULL else None
    cdef tuple v_targetList = _pg_list_to_tuple(data.targetList, offset_to_index)
    cdef tuple v_fromClause = _pg_list_to_tuple(data.fromClause, offset_to_index)
    cdef object v_whereClause = create(data.whereClause, offset_to_index) if data.whereClause is not NULL else None
    cdef tuple v_groupClause = _pg_list_to_tuple(data.groupClause, offset_to_index)
    cdef object v_groupDistinct = bool(data.groupDistinct)
    cdef object v_havingClause = create(data.havingClause, offset_to_index) if data.havingClause is not NULL else None
    cdef tuple v_windowClause = _pg_list_to_tuple(data.windowClause, offset_to_index)
    cdef tuple v_valuesLists = _pg_list_to_tuple(data.valuesLists, offset_to_index)
    cdef tuple v_sortClause = _pg_list_to_tuple(data.sortClause, offset_to_index)
    cdef object v_limitOffset = create(data.limitOffset, offset_to_index) if data.limitOffset is not NULL else None
    cdef object v_limitCount = create(data.limitCount, offset_to_index) if data.limitCount is not NULL else None
    cdef object v_limitOption = getattr(enums, 'LimitOption')(data.limitOption)
    cdef tuple v_lockingClause = _pg_list_to_tuple(data.lockingClause, offset_to_index)
    cdef object v_withClause = create(data.withClause, offset_to_index) if data.withClause is not NULL else None
    cdef object v_op = getattr(enums, 'SetOperation')(data.op)
    cdef object v_all = bool(data.all)
    cdef object v_larg = create(data.larg, offset_to_index) if data.larg is not NULL else None
    cdef object v_rarg = create(data.rarg, offset_to_index) if data.rarg is not NULL else None
    return ast.SelectStmt(v_distinctClause, v_intoClause, v_targetList, v_fromClause, v_whereClause, v_groupClause, v_groupDistinct, v_havingClause, v_windowClause, v_valuesLists, v_sortClause, v_limitOffset, v_limitCount, v_limitOption, v_lockingClause, v_withClause, v_op, v_all, v_larg, v_rarg)


cdef create_SetOperationStmt(structs.SetOperationStmt* data, offset_to_index):
    cdef object v_op = getattr(enums, 'SetOperation')(data.op)
    cdef object v_all = bool(data.all)
    cdef object v_larg = create(data.larg, offset_to_index) if data.larg is not NULL else None
    cdef object v_rarg = create(data.rarg, offset_to_index) if data.rarg is not NULL else None
    cdef tuple v_colTypes = _pg_list_to_tuple(data.colTypes, offset_to_index)
    cdef tuple v_colTypmods = _pg_list_to_tuple(data.colTypmods, offset_to_index)
    cdef tuple v_colCollations = _pg_list_to_tuple(data.colCollations, offset_to_index)
    cdef tuple v_groupClauses = _pg_list_to_tuple(data.groupClauses, offset_to_index)
    return ast.SetOperationStmt(v_op, v_all, v_larg, v_rarg, v_colTypes, v_colTypmods, v_colCollations, v_groupClauses)


cdef create_ReturnStmt(structs.ReturnStmt* data, offset_to_index):
    cdef object v_returnval = create(data.returnval, offset_to_index) if data.returnval is not NULL else None
    return ast.ReturnStmt(v_returnval)


cdef create_PLAssignStmt(structs.PLAssignStmt* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef tuple v_indirection = _pg_list_to_tuple(data.indirection, offset_to_index)
    cdef object v_nnames = data.nnames
    cdef object v_val = create(data.val, offset_to_index) if data.val is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.PLAssignStmt(v_name, v_indirection, v_nnames, v_val, v_location)


cdef create_CreateSchemaStmt(structs.CreateSchemaStmt* data, offset_to_index):
    cdef object v_schemaname = data.schemaname.decode("utf-8") if data.schemaname is not NULL else None
    cdef object v_authrole = create(data.authrole, offset_to_index) if data.authrole is not NULL else None
    cdef tuple v_schemaElts = _pg_list_to_tuple(data.schemaElts, offset_to_index)
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateSchemaStmt(v_schemaname, v_authrole, v_schemaElts, v_if_not_exists)


cdef create_AlterTableStmt(structs.AlterTableStmt* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef tuple v_cmds = _pg_list_to_tuple(data.cmds, offset_to_index)
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterTableStmt(v_relation, v_cmds, v_objtype, v_missing_ok)


cdef create_ReplicaIdentityStmt(structs.ReplicaIdentityStmt* data, offset_to_index):
    cdef object v_identity_type = chr(data.identity_type)
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    return ast.ReplicaIdentityStmt(v_identity_type, v_name)


cdef create_AlterTableCmd(structs.AlterTableCmd* data, offset_to_index):
    cdef object v_subtype = getattr(enums, 'AlterTableType')(data.subtype)
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_num = data.num
    cdef object v_newowner = create(data.newowner, offset_to_index) if data.newowner is not NULL else None
    cdef object v_def_ = create(data.def_, offset_to_index) if data.def_ is not NULL else None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    cdef object v_missing_ok = bool(data.missing_ok)
    cdef object v_recurse = bool(data.recurse)
    return ast.AlterTableCmd(v_subtype, v_name, v_num, v_newowner, v_def_, v_behavior, v_missing_ok, v_recurse)


cdef create_AlterCollationStmt(structs.AlterCollationStmt* data, offset_to_index):
    cdef tuple v_collname = _pg_list_to_tuple(data.collname, offset_to_index)
    return ast.AlterCollationStmt(v_collname)


cdef create_AlterDomainStmt(structs.AlterDomainStmt* data, offset_to_index):
    cdef object v_subtype = chr(data.subtype)
    cdef tuple v_typeName = _pg_list_to_tuple(data.typeName, offset_to_index)
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_def_ = create(data.def_, offset_to_index) if data.def_ is not NULL else None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterDomainStmt(v_subtype, v_typeName, v_name, v_def_, v_behavior, v_missing_ok)


cdef create_GrantStmt(structs.GrantStmt* data, offset_to_index):
    cdef object v_is_grant = bool(data.is_grant)
    cdef object v_targtype = getattr(enums, 'GrantTargetType')(data.targtype)
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef tuple v_objects = _pg_list_to_tuple(data.objects, offset_to_index)
    cdef tuple v_privileges = _pg_list_to_tuple(data.privileges, offset_to_index)
    cdef tuple v_grantees = _pg_list_to_tuple(data.grantees, offset_to_index)
    cdef object v_grant_option = bool(data.grant_option)
    cdef object v_grantor = create(data.grantor, offset_to_index) if data.grantor is not NULL else None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.GrantStmt(v_is_grant, v_targtype, v_objtype, v_objects, v_privileges, v_grantees, v_grant_option, v_grantor, v_behavior)


cdef create_ObjectWithArgs(structs.ObjectWithArgs* data, offset_to_index):
    cdef tuple v_objname = _pg_list_to_tuple(data.objname, offset_to_index)
    cdef tuple v_objargs = _pg_list_to_tuple(data.objargs, offset_to_index)
    cdef tuple v_objfuncargs = _pg_list_to_tuple(data.objfuncargs, offset_to_index)
    cdef object v_args_unspecified = bool(data.args_unspecified)
    return ast.ObjectWithArgs(v_objname, v_objargs, v_objfuncargs, v_args_unspecified)


cdef create_AccessPriv(structs.AccessPriv* data, offset_to_index):
    cdef object v_priv_name = data.priv_name.decode("utf-8") if data.priv_name is not NULL else None
    cdef tuple v_cols = _pg_list_to_tuple(data.cols, offset_to_index)
    return ast.AccessPriv(v_priv_name, v_cols)


cdef create_GrantRoleStmt(structs.GrantRoleStmt* data, offset_to_index):
    cdef tuple v_granted_roles = _pg_list_to_tuple(data.granted_roles, offset_to_index)
    cdef tuple v_grantee_roles = _pg_list_to_tuple(data.grantee_roles, offset_to_index)
    cdef object v_is_grant = bool(data.is_grant)
    cdef tuple v_opt = _pg_list_to_tuple(data.opt, offset_to_index)
    cdef object v_grantor = create(data.grantor, offset_to_index) if data.grantor is not NULL else None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.GrantRoleStmt(v_granted_roles, v_grantee_roles, v_is_grant, v_opt, v_grantor, v_behavior)


cdef create_AlterDefaultPrivilegesStmt(structs.AlterDefaultPrivilegesStmt* data, offset_to_index):
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_action = create(data.action, offset_to_index) if data.action is not NULL else None
    return ast.AlterDefaultPrivilegesStmt(v_options, v_action)


cdef create_CopyStmt(structs.CopyStmt* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_query = create(data.query, offset_to_index) if data.query is not NULL else None
    cdef tuple v_attlist = _pg_list_to_tuple(data.attlist, offset_to_index)
    cdef object v_is_from = bool(data.is_from)
    cdef object v_is_program = bool(data.is_program)
    cdef object v_filename = data.filename.decode("utf-8") if data.filename is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_whereClause = create(data.whereClause, offset_to_index) if data.whereClause is not NULL else None
    return ast.CopyStmt(v_relation, v_query, v_attlist, v_is_from, v_is_program, v_filename, v_options, v_whereClause)


cdef create_VariableSetStmt(structs.VariableSetStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'VariableSetKind')(data.kind)
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_is_local = bool(data.is_local)
    return ast.VariableSetStmt(v_kind, v_name, v_args, v_is_local)


cdef create_VariableShowStmt(structs.VariableShowStmt* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    return ast.VariableShowStmt(v_name)


cdef create_CreateStmt(structs.CreateStmt* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef tuple v_tableElts = _pg_list_to_tuple(data.tableElts, offset_to_index)
    cdef tuple v_inhRelations = _pg_list_to_tuple(data.inhRelations, offset_to_index)
    cdef object v_partbound = create(data.partbound, offset_to_index) if data.partbound is not NULL else None
    cdef object v_partspec = create(data.partspec, offset_to_index) if data.partspec is not NULL else None
    cdef object v_ofTypename = create(data.ofTypename, offset_to_index) if data.ofTypename is not NULL else None
    cdef tuple v_constraints = _pg_list_to_tuple(data.constraints, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_oncommit = getattr(enums, 'OnCommitAction')(data.oncommit)
    cdef object v_tablespacename = data.tablespacename.decode("utf-8") if data.tablespacename is not NULL else None
    cdef object v_accessMethod = data.accessMethod.decode("utf-8") if data.accessMethod is not NULL else None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateStmt(v_relation, v_tableElts, v_inhRelations, v_partbound, v_partspec, v_ofTypename, v_constraints, v_options, v_oncommit, v_tablespacename, v_accessMethod, v_if_not_exists)


cdef create_Constraint(structs.Constraint* data, offset_to_index):
    cdef object v_contype = getattr(enums, 'ConstrType')(data.contype)
    cdef object v_conname = data.conname.decode("utf-8") if data.conname is not NULL else None
    cdef object v_deferrable = bool(data.deferrable)
    cdef object v_initdeferred = bool(data.initdeferred)
    cdef object v_location = offset_to_index(data.location)
    cdef object v_is_no_inherit = bool(data.is_no_inherit)
    cdef object v_raw_expr = create(data.raw_expr, offset_to_index) if data.raw_expr is not NULL else None
    cdef object v_cooked_expr = data.cooked_expr.decode("utf-8") if data.cooked_expr is not NULL else None
    cdef object v_generated_when = chr(data.generated_when)
    cdef object v_nulls_not_distinct = bool(data.nulls_not_distinct)
    cdef tuple v_keys = _pg_list_to_tuple(data.keys, offset_to_index)
    cdef tuple v_including = _pg_list_to_tuple(data.including, offset_to_index)
    cdef tuple v_exclusions = _pg_list_to_tuple(data.exclusions, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_indexname = data.indexname.decode("utf-8") if data.indexname is not NULL else None
    cdef object v_indexspace = data.indexspace.decode("utf-8") if data.indexspace is not NULL else None
    cdef object v_reset_default_tblspc = bool(data.reset_default_tblspc)
    cdef object v_access_method = data.access_method.decode("utf-8") if data.access_method is not NULL else None
    cdef object v_where_clause = create(data.where_clause, offset_to_index) if data.where_clause is not NULL else None
    cdef object v_pktable = create(data.pktable, offset_to_index) if data.pktable is not NULL else None
    cdef tuple v_fk_attrs = _pg_list_to_tuple(data.fk_attrs, offset_to_index)
    cdef tuple v_pk_attrs = _pg_list_to_tuple(data.pk_attrs, offset_to_index)
    cdef object v_fk_matchtype = chr(data.fk_matchtype)
    cdef object v_fk_upd_action = chr(data.fk_upd_action)
    cdef object v_fk_del_action = chr(data.fk_del_action)
    cdef tuple v_fk_del_set_cols = _pg_list_to_tuple(data.fk_del_set_cols, offset_to_index)
    cdef tuple v_old_conpfeqop = _pg_list_to_tuple(data.old_conpfeqop, offset_to_index)
    cdef object v_skip_validation = bool(data.skip_validation)
    cdef object v_initially_valid = bool(data.initially_valid)
    return ast.Constraint(v_contype, v_conname, v_deferrable, v_initdeferred, v_location, v_is_no_inherit, v_raw_expr, v_cooked_expr, v_generated_when, v_nulls_not_distinct, v_keys, v_including, v_exclusions, v_options, v_indexname, v_indexspace, v_reset_default_tblspc, v_access_method, v_where_clause, v_pktable, v_fk_attrs, v_pk_attrs, v_fk_matchtype, v_fk_upd_action, v_fk_del_action, v_fk_del_set_cols, v_old_conpfeqop, v_skip_validation, v_initially_valid)


cdef create_CreateTableSpaceStmt(structs.CreateTableSpaceStmt* data, offset_to_index):
    cdef object v_tablespacename = data.tablespacename.decode("utf-8") if data.tablespacename is not NULL else None
    cdef object v_owner = create(data.owner, offset_to_index) if data.owner is not NULL else None
    cdef object v_location = data.location.decode("utf-8") if data.location is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.CreateTableSpaceStmt(v_tablespacename, v_owner, v_location, v_options)


cdef create_DropTableSpaceStmt(structs.DropTableSpaceStmt* data, offset_to_index):
    cdef object v_tablespacename = data.tablespacename.decode("utf-8") if data.tablespacename is not NULL else None
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.DropTableSpaceStmt(v_tablespacename, v_missing_ok)


cdef create_AlterTableSpaceOptionsStmt(structs.AlterTableSpaceOptionsStmt* data, offset_to_index):
    cdef object v_tablespacename = data.tablespacename.decode("utf-8") if data.tablespacename is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_isReset = bool(data.isReset)
    return ast.AlterTableSpaceOptionsStmt(v_tablespacename, v_options, v_isReset)


cdef create_AlterTableMoveAllStmt(structs.AlterTableMoveAllStmt* data, offset_to_index):
    cdef object v_orig_tablespacename = data.orig_tablespacename.decode("utf-8") if data.orig_tablespacename is not NULL else None
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef tuple v_roles = _pg_list_to_tuple(data.roles, offset_to_index)
    cdef object v_new_tablespacename = data.new_tablespacename.decode("utf-8") if data.new_tablespacename is not NULL else None
    cdef object v_nowait = bool(data.nowait)
    return ast.AlterTableMoveAllStmt(v_orig_tablespacename, v_objtype, v_roles, v_new_tablespacename, v_nowait)


cdef create_CreateExtensionStmt(structs.CreateExtensionStmt* data, offset_to_index):
    cdef object v_extname = data.extname.decode("utf-8") if data.extname is not NULL else None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.CreateExtensionStmt(v_extname, v_if_not_exists, v_options)


cdef create_AlterExtensionStmt(structs.AlterExtensionStmt* data, offset_to_index):
    cdef object v_extname = data.extname.decode("utf-8") if data.extname is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.AlterExtensionStmt(v_extname, v_options)


cdef create_AlterExtensionContentsStmt(structs.AlterExtensionContentsStmt* data, offset_to_index):
    cdef object v_extname = data.extname.decode("utf-8") if data.extname is not NULL else None
    cdef object v_action = data.action
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_object = create(data.object, offset_to_index) if data.object is not NULL else None
    return ast.AlterExtensionContentsStmt(v_extname, v_action, v_objtype, v_object)


cdef create_CreateFdwStmt(structs.CreateFdwStmt* data, offset_to_index):
    cdef object v_fdwname = data.fdwname.decode("utf-8") if data.fdwname is not NULL else None
    cdef tuple v_func_options = _pg_list_to_tuple(data.func_options, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.CreateFdwStmt(v_fdwname, v_func_options, v_options)


cdef create_AlterFdwStmt(structs.AlterFdwStmt* data, offset_to_index):
    cdef object v_fdwname = data.fdwname.decode("utf-8") if data.fdwname is not NULL else None
    cdef tuple v_func_options = _pg_list_to_tuple(data.func_options, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.AlterFdwStmt(v_fdwname, v_func_options, v_options)


cdef create_CreateForeignServerStmt(structs.CreateForeignServerStmt* data, offset_to_index):
    cdef object v_servername = data.servername.decode("utf-8") if data.servername is not NULL else None
    cdef object v_servertype = data.servertype.decode("utf-8") if data.servertype is not NULL else None
    cdef object v_version = data.version.decode("utf-8") if data.version is not NULL else None
    cdef object v_fdwname = data.fdwname.decode("utf-8") if data.fdwname is not NULL else None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.CreateForeignServerStmt(v_servername, v_servertype, v_version, v_fdwname, v_if_not_exists, v_options)


cdef create_AlterForeignServerStmt(structs.AlterForeignServerStmt* data, offset_to_index):
    cdef object v_servername = data.servername.decode("utf-8") if data.servername is not NULL else None
    cdef object v_version = data.version.decode("utf-8") if data.version is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_has_version = bool(data.has_version)
    return ast.AlterForeignServerStmt(v_servername, v_version, v_options, v_has_version)


cdef create_CreateForeignTableStmt(structs.CreateForeignTableStmt* data, offset_to_index):

    cdef object v_base = create_CreateStmt(<structs.CreateStmt*> data, offset_to_index)
    cdef object v_servername = data.servername.decode("utf-8") if data.servername is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.CreateForeignTableStmt(v_base, v_servername, v_options)


cdef create_CreateUserMappingStmt(structs.CreateUserMappingStmt* data, offset_to_index):
    cdef object v_user = create(data.user, offset_to_index) if data.user is not NULL else None
    cdef object v_servername = data.servername.decode("utf-8") if data.servername is not NULL else None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.CreateUserMappingStmt(v_user, v_servername, v_if_not_exists, v_options)


cdef create_AlterUserMappingStmt(structs.AlterUserMappingStmt* data, offset_to_index):
    cdef object v_user = create(data.user, offset_to_index) if data.user is not NULL else None
    cdef object v_servername = data.servername.decode("utf-8") if data.servername is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.AlterUserMappingStmt(v_user, v_servername, v_options)


cdef create_DropUserMappingStmt(structs.DropUserMappingStmt* data, offset_to_index):
    cdef object v_user = create(data.user, offset_to_index) if data.user is not NULL else None
    cdef object v_servername = data.servername.decode("utf-8") if data.servername is not NULL else None
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.DropUserMappingStmt(v_user, v_servername, v_missing_ok)


cdef create_ImportForeignSchemaStmt(structs.ImportForeignSchemaStmt* data, offset_to_index):
    cdef object v_server_name = data.server_name.decode("utf-8") if data.server_name is not NULL else None
    cdef object v_remote_schema = data.remote_schema.decode("utf-8") if data.remote_schema is not NULL else None
    cdef object v_local_schema = data.local_schema.decode("utf-8") if data.local_schema is not NULL else None
    cdef object v_list_type = getattr(enums, 'ImportForeignSchemaType')(data.list_type)
    cdef tuple v_table_list = _pg_list_to_tuple(data.table_list, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.ImportForeignSchemaStmt(v_server_name, v_remote_schema, v_local_schema, v_list_type, v_table_list, v_options)


cdef create_CreatePolicyStmt(structs.CreatePolicyStmt* data, offset_to_index):
    cdef object v_policy_name = data.policy_name.decode("utf-8") if data.policy_name is not NULL else None
    cdef object v_table = create(data.table, offset_to_index) if data.table is not NULL else None
    cdef object v_cmd_name = data.cmd_name.decode("utf-8") if data.cmd_name is not NULL else None
    cdef object v_permissive = bool(data.permissive)
    cdef tuple v_roles = _pg_list_to_tuple(data.roles, offset_to_index)
    cdef object v_qual = create(data.qual, offset_to_index) if data.qual is not NULL else None
    cdef object v_with_check = create(data.with_check, offset_to_index) if data.with_check is not NULL else None
    return ast.CreatePolicyStmt(v_policy_name, v_table, v_cmd_name, v_permissive, v_roles, v_qual, v_with_check)


cdef create_AlterPolicyStmt(structs.AlterPolicyStmt* data, offset_to_index):
    cdef object v_policy_name = data.policy_name.decode("utf-8") if data.policy_name is not NULL else None
    cdef object v_table = create(data.table, offset_to_index) if data.table is not NULL else None
    cdef tuple v_roles = _pg_list_to_tuple(data.roles, offset_to_index)
    cdef object v_qual = create(data.qual, offset_to_index) if data.qual is not NULL else None
    cdef object v_with_check = create(data.with_check, offset_to_index) if data.with_check is not NULL else None
    return ast.AlterPolicyStmt(v_policy_name, v_table, v_roles, v_qual, v_with_check)


cdef create_CreateAmStmt(structs.CreateAmStmt* data, offset_to_index):
    cdef object v_amname = data.amname.decode("utf-8") if data.amname is not NULL else None
    cdef tuple v_handler_name = _pg_list_to_tuple(data.handler_name, offset_to_index)
    cdef object v_amtype = chr(data.amtype)
    return ast.CreateAmStmt(v_amname, v_handler_name, v_amtype)


cdef create_CreateTrigStmt(structs.CreateTrigStmt* data, offset_to_index):
    cdef object v_replace = bool(data.replace)
    cdef object v_isconstraint = bool(data.isconstraint)
    cdef object v_trigname = data.trigname.decode("utf-8") if data.trigname is not NULL else None
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef tuple v_funcname = _pg_list_to_tuple(data.funcname, offset_to_index)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_row = bool(data.row)
    cdef object v_timing = data.timing
    cdef object v_events = data.events
    cdef tuple v_columns = _pg_list_to_tuple(data.columns, offset_to_index)
    cdef object v_whenClause = create(data.whenClause, offset_to_index) if data.whenClause is not NULL else None
    cdef tuple v_transitionRels = _pg_list_to_tuple(data.transitionRels, offset_to_index)
    cdef object v_deferrable = bool(data.deferrable)
    cdef object v_initdeferred = bool(data.initdeferred)
    cdef object v_constrrel = create(data.constrrel, offset_to_index) if data.constrrel is not NULL else None
    return ast.CreateTrigStmt(v_replace, v_isconstraint, v_trigname, v_relation, v_funcname, v_args, v_row, v_timing, v_events, v_columns, v_whenClause, v_transitionRels, v_deferrable, v_initdeferred, v_constrrel)


cdef create_CreateEventTrigStmt(structs.CreateEventTrigStmt* data, offset_to_index):
    cdef object v_trigname = data.trigname.decode("utf-8") if data.trigname is not NULL else None
    cdef object v_eventname = data.eventname.decode("utf-8") if data.eventname is not NULL else None
    cdef tuple v_whenclause = _pg_list_to_tuple(data.whenclause, offset_to_index)
    cdef tuple v_funcname = _pg_list_to_tuple(data.funcname, offset_to_index)
    return ast.CreateEventTrigStmt(v_trigname, v_eventname, v_whenclause, v_funcname)


cdef create_AlterEventTrigStmt(structs.AlterEventTrigStmt* data, offset_to_index):
    cdef object v_trigname = data.trigname.decode("utf-8") if data.trigname is not NULL else None
    cdef object v_tgenabled = chr(data.tgenabled)
    return ast.AlterEventTrigStmt(v_trigname, v_tgenabled)


cdef create_CreatePLangStmt(structs.CreatePLangStmt* data, offset_to_index):
    cdef object v_replace = bool(data.replace)
    cdef object v_plname = data.plname.decode("utf-8") if data.plname is not NULL else None
    cdef tuple v_plhandler = _pg_list_to_tuple(data.plhandler, offset_to_index)
    cdef tuple v_plinline = _pg_list_to_tuple(data.plinline, offset_to_index)
    cdef tuple v_plvalidator = _pg_list_to_tuple(data.plvalidator, offset_to_index)
    cdef object v_pltrusted = bool(data.pltrusted)
    return ast.CreatePLangStmt(v_replace, v_plname, v_plhandler, v_plinline, v_plvalidator, v_pltrusted)


cdef create_CreateRoleStmt(structs.CreateRoleStmt* data, offset_to_index):
    cdef object v_stmt_type = getattr(enums, 'RoleStmtType')(data.stmt_type)
    cdef object v_role = data.role.decode("utf-8") if data.role is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.CreateRoleStmt(v_stmt_type, v_role, v_options)


cdef create_AlterRoleStmt(structs.AlterRoleStmt* data, offset_to_index):
    cdef object v_role = create(data.role, offset_to_index) if data.role is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_action = data.action
    return ast.AlterRoleStmt(v_role, v_options, v_action)


cdef create_AlterRoleSetStmt(structs.AlterRoleSetStmt* data, offset_to_index):
    cdef object v_role = create(data.role, offset_to_index) if data.role is not NULL else None
    cdef object v_database = data.database.decode("utf-8") if data.database is not NULL else None
    cdef object v_setstmt = create(data.setstmt, offset_to_index) if data.setstmt is not NULL else None
    return ast.AlterRoleSetStmt(v_role, v_database, v_setstmt)


cdef create_DropRoleStmt(structs.DropRoleStmt* data, offset_to_index):
    cdef tuple v_roles = _pg_list_to_tuple(data.roles, offset_to_index)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.DropRoleStmt(v_roles, v_missing_ok)


cdef create_CreateSeqStmt(structs.CreateSeqStmt* data, offset_to_index):
    cdef object v_sequence = create(data.sequence, offset_to_index) if data.sequence is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_for_identity = bool(data.for_identity)
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateSeqStmt(v_sequence, v_options, v_for_identity, v_if_not_exists)


cdef create_AlterSeqStmt(structs.AlterSeqStmt* data, offset_to_index):
    cdef object v_sequence = create(data.sequence, offset_to_index) if data.sequence is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_for_identity = bool(data.for_identity)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterSeqStmt(v_sequence, v_options, v_for_identity, v_missing_ok)


cdef create_DefineStmt(structs.DefineStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'ObjectType')(data.kind)
    cdef object v_oldstyle = bool(data.oldstyle)
    cdef tuple v_defnames = _pg_list_to_tuple(data.defnames, offset_to_index)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef tuple v_definition = _pg_list_to_tuple(data.definition, offset_to_index)
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef object v_replace = bool(data.replace)
    return ast.DefineStmt(v_kind, v_oldstyle, v_defnames, v_args, v_definition, v_if_not_exists, v_replace)


cdef create_CreateDomainStmt(structs.CreateDomainStmt* data, offset_to_index):
    cdef tuple v_domainname = _pg_list_to_tuple(data.domainname, offset_to_index)
    cdef object v_typeName = create(data.typeName, offset_to_index) if data.typeName is not NULL else None
    cdef object v_collClause = create(data.collClause, offset_to_index) if data.collClause is not NULL else None
    cdef tuple v_constraints = _pg_list_to_tuple(data.constraints, offset_to_index)
    return ast.CreateDomainStmt(v_domainname, v_typeName, v_collClause, v_constraints)


cdef create_CreateOpClassStmt(structs.CreateOpClassStmt* data, offset_to_index):
    cdef tuple v_opclassname = _pg_list_to_tuple(data.opclassname, offset_to_index)
    cdef tuple v_opfamilyname = _pg_list_to_tuple(data.opfamilyname, offset_to_index)
    cdef object v_amname = data.amname.decode("utf-8") if data.amname is not NULL else None
    cdef object v_datatype = create(data.datatype, offset_to_index) if data.datatype is not NULL else None
    cdef tuple v_items = _pg_list_to_tuple(data.items, offset_to_index)
    cdef object v_isDefault = bool(data.isDefault)
    return ast.CreateOpClassStmt(v_opclassname, v_opfamilyname, v_amname, v_datatype, v_items, v_isDefault)


cdef create_CreateOpClassItem(structs.CreateOpClassItem* data, offset_to_index):
    cdef object v_itemtype = data.itemtype
    cdef object v_name = create(data.name, offset_to_index) if data.name is not NULL else None
    cdef object v_number = data.number
    cdef tuple v_order_family = _pg_list_to_tuple(data.order_family, offset_to_index)
    cdef tuple v_class_args = _pg_list_to_tuple(data.class_args, offset_to_index)
    cdef object v_storedtype = create(data.storedtype, offset_to_index) if data.storedtype is not NULL else None
    return ast.CreateOpClassItem(v_itemtype, v_name, v_number, v_order_family, v_class_args, v_storedtype)


cdef create_CreateOpFamilyStmt(structs.CreateOpFamilyStmt* data, offset_to_index):
    cdef tuple v_opfamilyname = _pg_list_to_tuple(data.opfamilyname, offset_to_index)
    cdef object v_amname = data.amname.decode("utf-8") if data.amname is not NULL else None
    return ast.CreateOpFamilyStmt(v_opfamilyname, v_amname)


cdef create_AlterOpFamilyStmt(structs.AlterOpFamilyStmt* data, offset_to_index):
    cdef tuple v_opfamilyname = _pg_list_to_tuple(data.opfamilyname, offset_to_index)
    cdef object v_amname = data.amname.decode("utf-8") if data.amname is not NULL else None
    cdef object v_isDrop = bool(data.isDrop)
    cdef tuple v_items = _pg_list_to_tuple(data.items, offset_to_index)
    return ast.AlterOpFamilyStmt(v_opfamilyname, v_amname, v_isDrop, v_items)


cdef create_DropStmt(structs.DropStmt* data, offset_to_index):
    cdef tuple v_objects = _pg_list_to_tuple(data.objects, offset_to_index)
    cdef object v_removeType = getattr(enums, 'ObjectType')(data.removeType)
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    cdef object v_missing_ok = bool(data.missing_ok)
    cdef object v_concurrent = bool(data.concurrent)
    return ast.DropStmt(v_objects, v_removeType, v_behavior, v_missing_ok, v_concurrent)


cdef create_TruncateStmt(structs.TruncateStmt* data, offset_to_index):
    cdef tuple v_relations = _pg_list_to_tuple(data.relations, offset_to_index)
    cdef object v_restart_seqs = bool(data.restart_seqs)
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.TruncateStmt(v_relations, v_restart_seqs, v_behavior)


cdef create_CommentStmt(structs.CommentStmt* data, offset_to_index):
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_object = create(data.object, offset_to_index) if data.object is not NULL else None
    cdef object v_comment = data.comment.decode("utf-8") if data.comment is not NULL else None
    return ast.CommentStmt(v_objtype, v_object, v_comment)


cdef create_SecLabelStmt(structs.SecLabelStmt* data, offset_to_index):
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_object = create(data.object, offset_to_index) if data.object is not NULL else None
    cdef object v_provider = data.provider.decode("utf-8") if data.provider is not NULL else None
    cdef object v_label = data.label.decode("utf-8") if data.label is not NULL else None
    return ast.SecLabelStmt(v_objtype, v_object, v_provider, v_label)


cdef create_DeclareCursorStmt(structs.DeclareCursorStmt* data, offset_to_index):
    cdef object v_portalname = data.portalname.decode("utf-8") if data.portalname is not NULL else None
    cdef object v_options = data.options
    cdef object v_query = create(data.query, offset_to_index) if data.query is not NULL else None
    return ast.DeclareCursorStmt(v_portalname, v_options, v_query)


cdef create_ClosePortalStmt(structs.ClosePortalStmt* data, offset_to_index):
    cdef object v_portalname = data.portalname.decode("utf-8") if data.portalname is not NULL else None
    return ast.ClosePortalStmt(v_portalname)


cdef create_FetchStmt(structs.FetchStmt* data, offset_to_index):
    cdef object v_direction = getattr(enums, 'FetchDirection')(data.direction)
    cdef object v_howMany = data.howMany
    cdef object v_portalname = data.portalname.decode("utf-8") if data.portalname is not NULL else None
    cdef object v_ismove = bool(data.ismove)
    return ast.FetchStmt(v_direction, v_howMany, v_portalname, v_ismove)


cdef create_IndexStmt(structs.IndexStmt* data, offset_to_index):
    cdef object v_idxname = data.idxname.decode("utf-8") if data.idxname is not NULL else None
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_accessMethod = data.accessMethod.decode("utf-8") if data.accessMethod is not NULL else None
    cdef object v_tableSpace = data.tableSpace.decode("utf-8") if data.tableSpace is not NULL else None
    cdef tuple v_indexParams = _pg_list_to_tuple(data.indexParams, offset_to_index)
    cdef tuple v_indexIncludingParams = _pg_list_to_tuple(data.indexIncludingParams, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_whereClause = create(data.whereClause, offset_to_index) if data.whereClause is not NULL else None
    cdef tuple v_excludeOpNames = _pg_list_to_tuple(data.excludeOpNames, offset_to_index)
    cdef object v_idxcomment = data.idxcomment.decode("utf-8") if data.idxcomment is not NULL else None
    cdef object v_oldNumber = data.oldNumber
    cdef object v_oldCreateSubid = data.oldCreateSubid
    cdef object v_oldFirstRelfilelocatorSubid = data.oldFirstRelfilelocatorSubid
    cdef object v_unique = bool(data.unique)
    cdef object v_nulls_not_distinct = bool(data.nulls_not_distinct)
    cdef object v_primary = bool(data.primary)
    cdef object v_isconstraint = bool(data.isconstraint)
    cdef object v_deferrable = bool(data.deferrable)
    cdef object v_initdeferred = bool(data.initdeferred)
    cdef object v_transformed = bool(data.transformed)
    cdef object v_concurrent = bool(data.concurrent)
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef object v_reset_default_tblspc = bool(data.reset_default_tblspc)
    return ast.IndexStmt(v_idxname, v_relation, v_accessMethod, v_tableSpace, v_indexParams, v_indexIncludingParams, v_options, v_whereClause, v_excludeOpNames, v_idxcomment, v_oldNumber, v_oldCreateSubid, v_oldFirstRelfilelocatorSubid, v_unique, v_nulls_not_distinct, v_primary, v_isconstraint, v_deferrable, v_initdeferred, v_transformed, v_concurrent, v_if_not_exists, v_reset_default_tblspc)


cdef create_CreateStatsStmt(structs.CreateStatsStmt* data, offset_to_index):
    cdef tuple v_defnames = _pg_list_to_tuple(data.defnames, offset_to_index)
    cdef tuple v_stat_types = _pg_list_to_tuple(data.stat_types, offset_to_index)
    cdef tuple v_exprs = _pg_list_to_tuple(data.exprs, offset_to_index)
    cdef tuple v_relations = _pg_list_to_tuple(data.relations, offset_to_index)
    cdef object v_stxcomment = data.stxcomment.decode("utf-8") if data.stxcomment is not NULL else None
    cdef object v_transformed = bool(data.transformed)
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateStatsStmt(v_defnames, v_stat_types, v_exprs, v_relations, v_stxcomment, v_transformed, v_if_not_exists)


cdef create_StatsElem(structs.StatsElem* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_expr = create(data.expr, offset_to_index) if data.expr is not NULL else None
    return ast.StatsElem(v_name, v_expr)


cdef create_AlterStatsStmt(structs.AlterStatsStmt* data, offset_to_index):
    cdef tuple v_defnames = _pg_list_to_tuple(data.defnames, offset_to_index)
    cdef object v_stxstattarget = data.stxstattarget
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterStatsStmt(v_defnames, v_stxstattarget, v_missing_ok)


cdef create_CreateFunctionStmt(structs.CreateFunctionStmt* data, offset_to_index):
    cdef object v_is_procedure = bool(data.is_procedure)
    cdef object v_replace = bool(data.replace)
    cdef tuple v_funcname = _pg_list_to_tuple(data.funcname, offset_to_index)
    cdef tuple v_parameters = _pg_list_to_tuple(data.parameters, offset_to_index)
    cdef object v_returnType = create(data.returnType, offset_to_index) if data.returnType is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_sql_body = create(data.sql_body, offset_to_index) if data.sql_body is not NULL else None
    return ast.CreateFunctionStmt(v_is_procedure, v_replace, v_funcname, v_parameters, v_returnType, v_options, v_sql_body)


cdef create_FunctionParameter(structs.FunctionParameter* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_argType = create(data.argType, offset_to_index) if data.argType is not NULL else None
    cdef object v_mode = getattr(enums, 'FunctionParameterMode')(chr(data.mode))
    cdef object v_defexpr = create(data.defexpr, offset_to_index) if data.defexpr is not NULL else None
    return ast.FunctionParameter(v_name, v_argType, v_mode, v_defexpr)


cdef create_AlterFunctionStmt(structs.AlterFunctionStmt* data, offset_to_index):
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_func = create(data.func, offset_to_index) if data.func is not NULL else None
    cdef tuple v_actions = _pg_list_to_tuple(data.actions, offset_to_index)
    return ast.AlterFunctionStmt(v_objtype, v_func, v_actions)


cdef create_DoStmt(structs.DoStmt* data, offset_to_index):
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    return ast.DoStmt(v_args)


cdef create_InlineCodeBlock(structs.InlineCodeBlock* data, offset_to_index):
    cdef object v_source_text = data.source_text.decode("utf-8") if data.source_text is not NULL else None
    cdef object v_langIsTrusted = bool(data.langIsTrusted)
    cdef object v_atomic = bool(data.atomic)
    return ast.InlineCodeBlock(v_source_text, v_langIsTrusted, v_atomic)


cdef create_CallStmt(structs.CallStmt* data, offset_to_index):
    cdef object v_funccall = create(data.funccall, offset_to_index) if data.funccall is not NULL else None
    cdef object v_funcexpr = create(data.funcexpr, offset_to_index) if data.funcexpr is not NULL else None
    cdef tuple v_outargs = _pg_list_to_tuple(data.outargs, offset_to_index)
    return ast.CallStmt(v_funccall, v_funcexpr, v_outargs)


cdef create_CallContext(structs.CallContext* data, offset_to_index):
    cdef object v_atomic = bool(data.atomic)
    return ast.CallContext(v_atomic)


cdef create_RenameStmt(structs.RenameStmt* data, offset_to_index):
    cdef object v_renameType = getattr(enums, 'ObjectType')(data.renameType)
    cdef object v_relationType = getattr(enums, 'ObjectType')(data.relationType)
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_object = create(data.object, offset_to_index) if data.object is not NULL else None
    cdef object v_subname = data.subname.decode("utf-8") if data.subname is not NULL else None
    cdef object v_newname = data.newname.decode("utf-8") if data.newname is not NULL else None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.RenameStmt(v_renameType, v_relationType, v_relation, v_object, v_subname, v_newname, v_behavior, v_missing_ok)


cdef create_AlterObjectDependsStmt(structs.AlterObjectDependsStmt* data, offset_to_index):
    cdef object v_objectType = getattr(enums, 'ObjectType')(data.objectType)
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_object = create(data.object, offset_to_index) if data.object is not NULL else None
    cdef object v_extname = create(data.extname, offset_to_index) if data.extname is not NULL else None
    cdef object v_remove = bool(data.remove)
    return ast.AlterObjectDependsStmt(v_objectType, v_relation, v_object, v_extname, v_remove)


cdef create_AlterObjectSchemaStmt(structs.AlterObjectSchemaStmt* data, offset_to_index):
    cdef object v_objectType = getattr(enums, 'ObjectType')(data.objectType)
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_object = create(data.object, offset_to_index) if data.object is not NULL else None
    cdef object v_newschema = data.newschema.decode("utf-8") if data.newschema is not NULL else None
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterObjectSchemaStmt(v_objectType, v_relation, v_object, v_newschema, v_missing_ok)


cdef create_AlterOwnerStmt(structs.AlterOwnerStmt* data, offset_to_index):
    cdef object v_objectType = getattr(enums, 'ObjectType')(data.objectType)
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_object = create(data.object, offset_to_index) if data.object is not NULL else None
    cdef object v_newowner = create(data.newowner, offset_to_index) if data.newowner is not NULL else None
    return ast.AlterOwnerStmt(v_objectType, v_relation, v_object, v_newowner)


cdef create_AlterOperatorStmt(structs.AlterOperatorStmt* data, offset_to_index):
    cdef object v_opername = create(data.opername, offset_to_index) if data.opername is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.AlterOperatorStmt(v_opername, v_options)


cdef create_AlterTypeStmt(structs.AlterTypeStmt* data, offset_to_index):
    cdef tuple v_typeName = _pg_list_to_tuple(data.typeName, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.AlterTypeStmt(v_typeName, v_options)


cdef create_RuleStmt(structs.RuleStmt* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_rulename = data.rulename.decode("utf-8") if data.rulename is not NULL else None
    cdef object v_whereClause = create(data.whereClause, offset_to_index) if data.whereClause is not NULL else None
    cdef object v_event = getattr(enums, 'CmdType')(data.event)
    cdef object v_instead = bool(data.instead)
    cdef tuple v_actions = _pg_list_to_tuple(data.actions, offset_to_index)
    cdef object v_replace = bool(data.replace)
    return ast.RuleStmt(v_relation, v_rulename, v_whereClause, v_event, v_instead, v_actions, v_replace)


cdef create_NotifyStmt(structs.NotifyStmt* data, offset_to_index):
    cdef object v_conditionname = data.conditionname.decode("utf-8") if data.conditionname is not NULL else None
    cdef object v_payload = data.payload.decode("utf-8") if data.payload is not NULL else None
    return ast.NotifyStmt(v_conditionname, v_payload)


cdef create_ListenStmt(structs.ListenStmt* data, offset_to_index):
    cdef object v_conditionname = data.conditionname.decode("utf-8") if data.conditionname is not NULL else None
    return ast.ListenStmt(v_conditionname)


cdef create_UnlistenStmt(structs.UnlistenStmt* data, offset_to_index):
    cdef object v_conditionname = data.conditionname.decode("utf-8") if data.conditionname is not NULL else None
    return ast.UnlistenStmt(v_conditionname)


cdef create_TransactionStmt(structs.TransactionStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'TransactionStmtKind')(data.kind)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_savepoint_name = data.savepoint_name.decode("utf-8") if data.savepoint_name is not NULL else None
    cdef object v_gid = data.gid.decode("utf-8") if data.gid is not NULL else None
    cdef object v_chain = bool(data.chain)
    return ast.TransactionStmt(v_kind, v_options, v_savepoint_name, v_gid, v_chain)


cdef create_CompositeTypeStmt(structs.CompositeTypeStmt* data, offset_to_index):
    cdef object v_typevar = create(data.typevar, offset_to_index) if data.typevar is not NULL else None
    cdef tuple v_coldeflist = _pg_list_to_tuple(data.coldeflist, offset_to_index)
    return ast.CompositeTypeStmt(v_typevar, v_coldeflist)


cdef create_CreateEnumStmt(structs.CreateEnumStmt* data, offset_to_index):
    cdef tuple v_typeName = _pg_list_to_tuple(data.typeName, offset_to_index)
    cdef tuple v_vals = _pg_list_to_tuple(data.vals, offset_to_index)
    return ast.CreateEnumStmt(v_typeName, v_vals)


cdef create_CreateRangeStmt(structs.CreateRangeStmt* data, offset_to_index):
    cdef tuple v_typeName = _pg_list_to_tuple(data.typeName, offset_to_index)
    cdef tuple v_params = _pg_list_to_tuple(data.params, offset_to_index)
    return ast.CreateRangeStmt(v_typeName, v_params)


cdef create_AlterEnumStmt(structs.AlterEnumStmt* data, offset_to_index):
    cdef tuple v_typeName = _pg_list_to_tuple(data.typeName, offset_to_index)
    cdef object v_oldVal = data.oldVal.decode("utf-8") if data.oldVal is not NULL else None
    cdef object v_newVal = data.newVal.decode("utf-8") if data.newVal is not NULL else None
    cdef object v_newValNeighbor = data.newValNeighbor.decode("utf-8") if data.newValNeighbor is not NULL else None
    cdef object v_newValIsAfter = bool(data.newValIsAfter)
    cdef object v_skipIfNewValExists = bool(data.skipIfNewValExists)
    return ast.AlterEnumStmt(v_typeName, v_oldVal, v_newVal, v_newValNeighbor, v_newValIsAfter, v_skipIfNewValExists)


cdef create_ViewStmt(structs.ViewStmt* data, offset_to_index):
    cdef object v_view = create(data.view, offset_to_index) if data.view is not NULL else None
    cdef tuple v_aliases = _pg_list_to_tuple(data.aliases, offset_to_index)
    cdef object v_query = create(data.query, offset_to_index) if data.query is not NULL else None
    cdef object v_replace = bool(data.replace)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_withCheckOption = getattr(enums, 'ViewCheckOption')(data.withCheckOption)
    return ast.ViewStmt(v_view, v_aliases, v_query, v_replace, v_options, v_withCheckOption)


cdef create_LoadStmt(structs.LoadStmt* data, offset_to_index):
    cdef object v_filename = data.filename.decode("utf-8") if data.filename is not NULL else None
    return ast.LoadStmt(v_filename)


cdef create_CreatedbStmt(structs.CreatedbStmt* data, offset_to_index):
    cdef object v_dbname = data.dbname.decode("utf-8") if data.dbname is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.CreatedbStmt(v_dbname, v_options)


cdef create_AlterDatabaseStmt(structs.AlterDatabaseStmt* data, offset_to_index):
    cdef object v_dbname = data.dbname.decode("utf-8") if data.dbname is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.AlterDatabaseStmt(v_dbname, v_options)


cdef create_AlterDatabaseRefreshCollStmt(structs.AlterDatabaseRefreshCollStmt* data, offset_to_index):
    cdef object v_dbname = data.dbname.decode("utf-8") if data.dbname is not NULL else None
    return ast.AlterDatabaseRefreshCollStmt(v_dbname)


cdef create_AlterDatabaseSetStmt(structs.AlterDatabaseSetStmt* data, offset_to_index):
    cdef object v_dbname = data.dbname.decode("utf-8") if data.dbname is not NULL else None
    cdef object v_setstmt = create(data.setstmt, offset_to_index) if data.setstmt is not NULL else None
    return ast.AlterDatabaseSetStmt(v_dbname, v_setstmt)


cdef create_DropdbStmt(structs.DropdbStmt* data, offset_to_index):
    cdef object v_dbname = data.dbname.decode("utf-8") if data.dbname is not NULL else None
    cdef object v_missing_ok = bool(data.missing_ok)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.DropdbStmt(v_dbname, v_missing_ok, v_options)


cdef create_AlterSystemStmt(structs.AlterSystemStmt* data, offset_to_index):
    cdef object v_setstmt = create(data.setstmt, offset_to_index) if data.setstmt is not NULL else None
    return ast.AlterSystemStmt(v_setstmt)


cdef create_ClusterStmt(structs.ClusterStmt* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_indexname = data.indexname.decode("utf-8") if data.indexname is not NULL else None
    cdef tuple v_params = _pg_list_to_tuple(data.params, offset_to_index)
    return ast.ClusterStmt(v_relation, v_indexname, v_params)


cdef create_VacuumStmt(structs.VacuumStmt* data, offset_to_index):
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef tuple v_rels = _pg_list_to_tuple(data.rels, offset_to_index)
    cdef object v_is_vacuumcmd = bool(data.is_vacuumcmd)
    return ast.VacuumStmt(v_options, v_rels, v_is_vacuumcmd)


cdef create_VacuumRelation(structs.VacuumRelation* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef tuple v_va_cols = _pg_list_to_tuple(data.va_cols, offset_to_index)
    return ast.VacuumRelation(v_relation, v_va_cols)


cdef create_ExplainStmt(structs.ExplainStmt* data, offset_to_index):
    cdef object v_query = create(data.query, offset_to_index) if data.query is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.ExplainStmt(v_query, v_options)


cdef create_CreateTableAsStmt(structs.CreateTableAsStmt* data, offset_to_index):
    cdef object v_query = create(data.query, offset_to_index) if data.query is not NULL else None
    cdef object v_into = create(data.into, offset_to_index) if data.into is not NULL else None
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_is_select_into = bool(data.is_select_into)
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateTableAsStmt(v_query, v_into, v_objtype, v_is_select_into, v_if_not_exists)


cdef create_RefreshMatViewStmt(structs.RefreshMatViewStmt* data, offset_to_index):
    cdef object v_concurrent = bool(data.concurrent)
    cdef object v_skipData = bool(data.skipData)
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    return ast.RefreshMatViewStmt(v_concurrent, v_skipData, v_relation)


cdef create_CheckPointStmt(structs.CheckPointStmt* data, offset_to_index):
    return ast.CheckPointStmt()


cdef create_DiscardStmt(structs.DiscardStmt* data, offset_to_index):
    cdef object v_target = getattr(enums, 'DiscardMode')(data.target)
    return ast.DiscardStmt(v_target)


cdef create_LockStmt(structs.LockStmt* data, offset_to_index):
    cdef tuple v_relations = _pg_list_to_tuple(data.relations, offset_to_index)
    cdef object v_mode = data.mode
    cdef object v_nowait = bool(data.nowait)
    return ast.LockStmt(v_relations, v_mode, v_nowait)


cdef create_ConstraintsSetStmt(structs.ConstraintsSetStmt* data, offset_to_index):
    cdef tuple v_constraints = _pg_list_to_tuple(data.constraints, offset_to_index)
    cdef object v_deferred = bool(data.deferred)
    return ast.ConstraintsSetStmt(v_constraints, v_deferred)


cdef create_ReindexStmt(structs.ReindexStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'ReindexObjectType')(data.kind)
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef tuple v_params = _pg_list_to_tuple(data.params, offset_to_index)
    return ast.ReindexStmt(v_kind, v_relation, v_name, v_params)


cdef create_CreateConversionStmt(structs.CreateConversionStmt* data, offset_to_index):
    cdef tuple v_conversion_name = _pg_list_to_tuple(data.conversion_name, offset_to_index)
    cdef object v_for_encoding_name = data.for_encoding_name.decode("utf-8") if data.for_encoding_name is not NULL else None
    cdef object v_to_encoding_name = data.to_encoding_name.decode("utf-8") if data.to_encoding_name is not NULL else None
    cdef tuple v_func_name = _pg_list_to_tuple(data.func_name, offset_to_index)
    cdef object v_def_ = bool(data.def_)
    return ast.CreateConversionStmt(v_conversion_name, v_for_encoding_name, v_to_encoding_name, v_func_name, v_def_)


cdef create_CreateCastStmt(structs.CreateCastStmt* data, offset_to_index):
    cdef object v_sourcetype = create(data.sourcetype, offset_to_index) if data.sourcetype is not NULL else None
    cdef object v_targettype = create(data.targettype, offset_to_index) if data.targettype is not NULL else None
    cdef object v_func = create(data.func, offset_to_index) if data.func is not NULL else None
    cdef object v_context = getattr(enums, 'CoercionContext')(data.context)
    cdef object v_inout = bool(data.inout)
    return ast.CreateCastStmt(v_sourcetype, v_targettype, v_func, v_context, v_inout)


cdef create_CreateTransformStmt(structs.CreateTransformStmt* data, offset_to_index):
    cdef object v_replace = bool(data.replace)
    cdef object v_type_name = create(data.type_name, offset_to_index) if data.type_name is not NULL else None
    cdef object v_lang = data.lang.decode("utf-8") if data.lang is not NULL else None
    cdef object v_fromsql = create(data.fromsql, offset_to_index) if data.fromsql is not NULL else None
    cdef object v_tosql = create(data.tosql, offset_to_index) if data.tosql is not NULL else None
    return ast.CreateTransformStmt(v_replace, v_type_name, v_lang, v_fromsql, v_tosql)


cdef create_PrepareStmt(structs.PrepareStmt* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef tuple v_argtypes = _pg_list_to_tuple(data.argtypes, offset_to_index)
    cdef object v_query = create(data.query, offset_to_index) if data.query is not NULL else None
    return ast.PrepareStmt(v_name, v_argtypes, v_query)


cdef create_ExecuteStmt(structs.ExecuteStmt* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef tuple v_params = _pg_list_to_tuple(data.params, offset_to_index)
    return ast.ExecuteStmt(v_name, v_params)


cdef create_DeallocateStmt(structs.DeallocateStmt* data, offset_to_index):
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    return ast.DeallocateStmt(v_name)


cdef create_DropOwnedStmt(structs.DropOwnedStmt* data, offset_to_index):
    cdef tuple v_roles = _pg_list_to_tuple(data.roles, offset_to_index)
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.DropOwnedStmt(v_roles, v_behavior)


cdef create_ReassignOwnedStmt(structs.ReassignOwnedStmt* data, offset_to_index):
    cdef tuple v_roles = _pg_list_to_tuple(data.roles, offset_to_index)
    cdef object v_newrole = create(data.newrole, offset_to_index) if data.newrole is not NULL else None
    return ast.ReassignOwnedStmt(v_roles, v_newrole)


cdef create_AlterTSDictionaryStmt(structs.AlterTSDictionaryStmt* data, offset_to_index):
    cdef tuple v_dictname = _pg_list_to_tuple(data.dictname, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.AlterTSDictionaryStmt(v_dictname, v_options)


cdef create_AlterTSConfigurationStmt(structs.AlterTSConfigurationStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'AlterTSConfigType')(data.kind)
    cdef tuple v_cfgname = _pg_list_to_tuple(data.cfgname, offset_to_index)
    cdef tuple v_tokentype = _pg_list_to_tuple(data.tokentype, offset_to_index)
    cdef tuple v_dicts = _pg_list_to_tuple(data.dicts, offset_to_index)
    cdef object v_override = bool(data.override)
    cdef object v_replace = bool(data.replace)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterTSConfigurationStmt(v_kind, v_cfgname, v_tokentype, v_dicts, v_override, v_replace, v_missing_ok)


cdef create_PublicationTable(structs.PublicationTable* data, offset_to_index):
    cdef object v_relation = create(data.relation, offset_to_index) if data.relation is not NULL else None
    cdef object v_whereClause = create(data.whereClause, offset_to_index) if data.whereClause is not NULL else None
    cdef tuple v_columns = _pg_list_to_tuple(data.columns, offset_to_index)
    return ast.PublicationTable(v_relation, v_whereClause, v_columns)


cdef create_PublicationObjSpec(structs.PublicationObjSpec* data, offset_to_index):
    cdef object v_pubobjtype = getattr(enums, 'PublicationObjSpecType')(data.pubobjtype)
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_pubtable = create(data.pubtable, offset_to_index) if data.pubtable is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.PublicationObjSpec(v_pubobjtype, v_name, v_pubtable, v_location)


cdef create_CreatePublicationStmt(structs.CreatePublicationStmt* data, offset_to_index):
    cdef object v_pubname = data.pubname.decode("utf-8") if data.pubname is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef tuple v_pubobjects = _pg_list_to_tuple(data.pubobjects, offset_to_index)
    cdef object v_for_all_tables = bool(data.for_all_tables)
    return ast.CreatePublicationStmt(v_pubname, v_options, v_pubobjects, v_for_all_tables)


cdef create_AlterPublicationStmt(structs.AlterPublicationStmt* data, offset_to_index):
    cdef object v_pubname = data.pubname.decode("utf-8") if data.pubname is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef tuple v_pubobjects = _pg_list_to_tuple(data.pubobjects, offset_to_index)
    cdef object v_for_all_tables = bool(data.for_all_tables)
    cdef object v_action = getattr(enums, 'AlterPublicationAction')(data.action)
    return ast.AlterPublicationStmt(v_pubname, v_options, v_pubobjects, v_for_all_tables, v_action)


cdef create_CreateSubscriptionStmt(structs.CreateSubscriptionStmt* data, offset_to_index):
    cdef object v_subname = data.subname.decode("utf-8") if data.subname is not NULL else None
    cdef object v_conninfo = data.conninfo.decode("utf-8") if data.conninfo is not NULL else None
    cdef tuple v_publication = _pg_list_to_tuple(data.publication, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.CreateSubscriptionStmt(v_subname, v_conninfo, v_publication, v_options)


cdef create_AlterSubscriptionStmt(structs.AlterSubscriptionStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'AlterSubscriptionType')(data.kind)
    cdef object v_subname = data.subname.decode("utf-8") if data.subname is not NULL else None
    cdef object v_conninfo = data.conninfo.decode("utf-8") if data.conninfo is not NULL else None
    cdef tuple v_publication = _pg_list_to_tuple(data.publication, offset_to_index)
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    return ast.AlterSubscriptionStmt(v_kind, v_subname, v_conninfo, v_publication, v_options)


cdef create_DropSubscriptionStmt(structs.DropSubscriptionStmt* data, offset_to_index):
    cdef object v_subname = data.subname.decode("utf-8") if data.subname is not NULL else None
    cdef object v_missing_ok = bool(data.missing_ok)
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.DropSubscriptionStmt(v_subname, v_missing_ok, v_behavior)


cdef create_Alias(structs.Alias* data, offset_to_index):
    cdef object v_aliasname = data.aliasname.decode("utf-8") if data.aliasname is not NULL else None
    cdef tuple v_colnames = _pg_list_to_tuple(data.colnames, offset_to_index)
    return ast.Alias(v_aliasname, v_colnames)


cdef create_RangeVar(structs.RangeVar* data, offset_to_index):
    cdef object v_catalogname = data.catalogname.decode("utf-8") if data.catalogname is not NULL else None
    cdef object v_schemaname = data.schemaname.decode("utf-8") if data.schemaname is not NULL else None
    cdef object v_relname = data.relname.decode("utf-8") if data.relname is not NULL else None
    cdef object v_inh = bool(data.inh)
    cdef object v_relpersistence = chr(data.relpersistence)
    cdef object v_alias = create(data.alias, offset_to_index) if data.alias is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.RangeVar(v_catalogname, v_schemaname, v_relname, v_inh, v_relpersistence, v_alias, v_location)


cdef create_TableFunc(structs.TableFunc* data, offset_to_index):
    cdef tuple v_ns_uris = _pg_list_to_tuple(data.ns_uris, offset_to_index)
    cdef tuple v_ns_names = _pg_list_to_tuple(data.ns_names, offset_to_index)
    cdef object v_docexpr = create(data.docexpr, offset_to_index) if data.docexpr is not NULL else None
    cdef object v_rowexpr = create(data.rowexpr, offset_to_index) if data.rowexpr is not NULL else None
    cdef tuple v_colnames = _pg_list_to_tuple(data.colnames, offset_to_index)
    cdef tuple v_coltypes = _pg_list_to_tuple(data.coltypes, offset_to_index)
    cdef tuple v_coltypmods = _pg_list_to_tuple(data.coltypmods, offset_to_index)
    cdef tuple v_colcollations = _pg_list_to_tuple(data.colcollations, offset_to_index)
    cdef tuple v_colexprs = _pg_list_to_tuple(data.colexprs, offset_to_index)
    cdef tuple v_coldefexprs = _pg_list_to_tuple(data.coldefexprs, offset_to_index)
    cdef set v_notnulls = _pg_bitmapset_to_set(data.notnulls)
    cdef object v_ordinalitycol = data.ordinalitycol
    cdef object v_location = offset_to_index(data.location)
    return ast.TableFunc(v_ns_uris, v_ns_names, v_docexpr, v_rowexpr, v_colnames, v_coltypes, v_coltypmods, v_colcollations, v_colexprs, v_coldefexprs, v_notnulls, v_ordinalitycol, v_location)


cdef create_IntoClause(structs.IntoClause* data, offset_to_index):
    cdef object v_rel = create(data.rel, offset_to_index) if data.rel is not NULL else None
    cdef tuple v_colNames = _pg_list_to_tuple(data.colNames, offset_to_index)
    cdef object v_accessMethod = data.accessMethod.decode("utf-8") if data.accessMethod is not NULL else None
    cdef tuple v_options = _pg_list_to_tuple(data.options, offset_to_index)
    cdef object v_onCommit = getattr(enums, 'OnCommitAction')(data.onCommit)
    cdef object v_tableSpaceName = data.tableSpaceName.decode("utf-8") if data.tableSpaceName is not NULL else None
    cdef object v_viewQuery = create(data.viewQuery, offset_to_index) if data.viewQuery is not NULL else None
    cdef object v_skipData = bool(data.skipData)
    return ast.IntoClause(v_rel, v_colNames, v_accessMethod, v_options, v_onCommit, v_tableSpaceName, v_viewQuery, v_skipData)


cdef create_Var(structs.Var* data, offset_to_index):
    cdef object v_varno = data.varno
    cdef object v_varattno = data.varattno
    cdef object v_vartypmod = data.vartypmod
    cdef set v_varnullingrels = _pg_bitmapset_to_set(data.varnullingrels)
    cdef object v_varlevelsup = data.varlevelsup
    cdef object v_location = offset_to_index(data.location)
    return ast.Var(v_varno, v_varattno, v_vartypmod, v_varnullingrels, v_varlevelsup, v_location)


cdef create_Param(structs.Param* data, offset_to_index):
    cdef object v_paramkind = getattr(enums, 'ParamKind')(data.paramkind)
    cdef object v_paramid = data.paramid
    cdef object v_paramtypmod = data.paramtypmod
    cdef object v_location = offset_to_index(data.location)
    return ast.Param(v_paramkind, v_paramid, v_paramtypmod, v_location)


cdef create_Aggref(structs.Aggref* data, offset_to_index):
    cdef tuple v_aggargtypes = _pg_list_to_tuple(data.aggargtypes, offset_to_index)
    cdef tuple v_aggdirectargs = _pg_list_to_tuple(data.aggdirectargs, offset_to_index)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef tuple v_aggorder = _pg_list_to_tuple(data.aggorder, offset_to_index)
    cdef tuple v_aggdistinct = _pg_list_to_tuple(data.aggdistinct, offset_to_index)
    cdef object v_aggfilter = create(data.aggfilter, offset_to_index) if data.aggfilter is not NULL else None
    cdef object v_aggstar = bool(data.aggstar)
    cdef object v_aggvariadic = bool(data.aggvariadic)
    cdef object v_aggkind = chr(data.aggkind)
    cdef object v_agglevelsup = data.agglevelsup
    cdef object v_aggsplit = getattr(enums, 'AggSplit')(data.aggsplit)
    cdef object v_aggno = data.aggno
    cdef object v_aggtransno = data.aggtransno
    cdef object v_location = offset_to_index(data.location)
    return ast.Aggref(v_aggargtypes, v_aggdirectargs, v_args, v_aggorder, v_aggdistinct, v_aggfilter, v_aggstar, v_aggvariadic, v_aggkind, v_agglevelsup, v_aggsplit, v_aggno, v_aggtransno, v_location)


cdef create_GroupingFunc(structs.GroupingFunc* data, offset_to_index):
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef tuple v_refs = _pg_list_to_tuple(data.refs, offset_to_index)
    cdef object v_agglevelsup = data.agglevelsup
    cdef object v_location = offset_to_index(data.location)
    return ast.GroupingFunc(v_args, v_refs, v_agglevelsup, v_location)


cdef create_WindowFunc(structs.WindowFunc* data, offset_to_index):
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_aggfilter = create(data.aggfilter, offset_to_index) if data.aggfilter is not NULL else None
    cdef object v_winref = data.winref
    cdef object v_winstar = bool(data.winstar)
    cdef object v_winagg = bool(data.winagg)
    cdef object v_location = offset_to_index(data.location)
    return ast.WindowFunc(v_args, v_aggfilter, v_winref, v_winstar, v_winagg, v_location)


cdef create_SubscriptingRef(structs.SubscriptingRef* data, offset_to_index):
    cdef object v_reftypmod = data.reftypmod
    cdef tuple v_refupperindexpr = _pg_list_to_tuple(data.refupperindexpr, offset_to_index)
    cdef tuple v_reflowerindexpr = _pg_list_to_tuple(data.reflowerindexpr, offset_to_index)
    cdef object v_refexpr = create(data.refexpr, offset_to_index) if data.refexpr is not NULL else None
    cdef object v_refassgnexpr = create(data.refassgnexpr, offset_to_index) if data.refassgnexpr is not NULL else None
    return ast.SubscriptingRef(v_reftypmod, v_refupperindexpr, v_reflowerindexpr, v_refexpr, v_refassgnexpr)


cdef create_FuncExpr(structs.FuncExpr* data, offset_to_index):
    cdef object v_funcretset = bool(data.funcretset)
    cdef object v_funcvariadic = bool(data.funcvariadic)
    cdef object v_funcformat = getattr(enums, 'CoercionForm')(data.funcformat)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.FuncExpr(v_funcretset, v_funcvariadic, v_funcformat, v_args, v_location)


cdef create_NamedArgExpr(structs.NamedArgExpr* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef object v_argnumber = data.argnumber
    cdef object v_location = offset_to_index(data.location)
    return ast.NamedArgExpr(v_arg, v_name, v_argnumber, v_location)


cdef create_OpExpr(structs.OpExpr* data, offset_to_index):
    cdef object v_opretset = bool(data.opretset)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.OpExpr(v_opretset, v_args, v_location)


cdef create_ScalarArrayOpExpr(structs.ScalarArrayOpExpr* data, offset_to_index):
    cdef object v_useOr = bool(data.useOr)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.ScalarArrayOpExpr(v_useOr, v_args, v_location)


cdef create_BoolExpr(structs.BoolExpr* data, offset_to_index):
    cdef object v_boolop = getattr(enums, 'BoolExprType')(data.boolop)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.BoolExpr(v_boolop, v_args, v_location)


cdef create_SubLink(structs.SubLink* data, offset_to_index):
    cdef object v_subLinkType = getattr(enums, 'SubLinkType')(data.subLinkType)
    cdef object v_subLinkId = data.subLinkId
    cdef object v_testexpr = create(data.testexpr, offset_to_index) if data.testexpr is not NULL else None
    cdef tuple v_operName = _pg_list_to_tuple(data.operName, offset_to_index)
    cdef object v_subselect = create(data.subselect, offset_to_index) if data.subselect is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.SubLink(v_subLinkType, v_subLinkId, v_testexpr, v_operName, v_subselect, v_location)


cdef create_SubPlan(structs.SubPlan* data, offset_to_index):
    cdef object v_subLinkType = getattr(enums, 'SubLinkType')(data.subLinkType)
    cdef object v_testexpr = create(data.testexpr, offset_to_index) if data.testexpr is not NULL else None
    cdef tuple v_paramIds = _pg_list_to_tuple(data.paramIds, offset_to_index)
    cdef object v_plan_id = data.plan_id
    cdef object v_plan_name = data.plan_name.decode("utf-8") if data.plan_name is not NULL else None
    cdef object v_firstColTypmod = data.firstColTypmod
    cdef object v_useHashTable = bool(data.useHashTable)
    cdef object v_unknownEqFalse = bool(data.unknownEqFalse)
    cdef object v_parallel_safe = bool(data.parallel_safe)
    cdef tuple v_setParam = _pg_list_to_tuple(data.setParam, offset_to_index)
    cdef tuple v_parParam = _pg_list_to_tuple(data.parParam, offset_to_index)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_startup_cost = data.startup_cost
    cdef object v_per_call_cost = data.per_call_cost
    return ast.SubPlan(v_subLinkType, v_testexpr, v_paramIds, v_plan_id, v_plan_name, v_firstColTypmod, v_useHashTable, v_unknownEqFalse, v_parallel_safe, v_setParam, v_parParam, v_args, v_startup_cost, v_per_call_cost)


cdef create_AlternativeSubPlan(structs.AlternativeSubPlan* data, offset_to_index):
    cdef tuple v_subplans = _pg_list_to_tuple(data.subplans, offset_to_index)
    return ast.AlternativeSubPlan(v_subplans)


cdef create_FieldSelect(structs.FieldSelect* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_fieldnum = data.fieldnum
    cdef object v_resulttypmod = data.resulttypmod
    return ast.FieldSelect(v_arg, v_fieldnum, v_resulttypmod)


cdef create_FieldStore(structs.FieldStore* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef tuple v_newvals = _pg_list_to_tuple(data.newvals, offset_to_index)
    cdef tuple v_fieldnums = _pg_list_to_tuple(data.fieldnums, offset_to_index)
    return ast.FieldStore(v_arg, v_newvals, v_fieldnums)


cdef create_RelabelType(structs.RelabelType* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_resulttypmod = data.resulttypmod
    cdef object v_relabelformat = getattr(enums, 'CoercionForm')(data.relabelformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.RelabelType(v_arg, v_resulttypmod, v_relabelformat, v_location)


cdef create_CoerceViaIO(structs.CoerceViaIO* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_coerceformat = getattr(enums, 'CoercionForm')(data.coerceformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.CoerceViaIO(v_arg, v_coerceformat, v_location)


cdef create_ArrayCoerceExpr(structs.ArrayCoerceExpr* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_elemexpr = create(data.elemexpr, offset_to_index) if data.elemexpr is not NULL else None
    cdef object v_resulttypmod = data.resulttypmod
    cdef object v_coerceformat = getattr(enums, 'CoercionForm')(data.coerceformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.ArrayCoerceExpr(v_arg, v_elemexpr, v_resulttypmod, v_coerceformat, v_location)


cdef create_ConvertRowtypeExpr(structs.ConvertRowtypeExpr* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_convertformat = getattr(enums, 'CoercionForm')(data.convertformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.ConvertRowtypeExpr(v_arg, v_convertformat, v_location)


cdef create_CollateExpr(structs.CollateExpr* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.CollateExpr(v_arg, v_location)


cdef create_CaseExpr(structs.CaseExpr* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_defresult = create(data.defresult, offset_to_index) if data.defresult is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.CaseExpr(v_arg, v_args, v_defresult, v_location)


cdef create_CaseWhen(structs.CaseWhen* data, offset_to_index):
    cdef object v_expr = create(data.expr, offset_to_index) if data.expr is not NULL else None
    cdef object v_result = create(data.result, offset_to_index) if data.result is not NULL else None
    cdef object v_location = offset_to_index(data.location)
    return ast.CaseWhen(v_expr, v_result, v_location)


cdef create_CaseTestExpr(structs.CaseTestExpr* data, offset_to_index):
    cdef object v_typeMod = data.typeMod
    return ast.CaseTestExpr(v_typeMod)


cdef create_ArrayExpr(structs.ArrayExpr* data, offset_to_index):
    cdef tuple v_elements = _pg_list_to_tuple(data.elements, offset_to_index)
    cdef object v_multidims = bool(data.multidims)
    cdef object v_location = offset_to_index(data.location)
    return ast.ArrayExpr(v_elements, v_multidims, v_location)


cdef create_RowExpr(structs.RowExpr* data, offset_to_index):
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_row_format = getattr(enums, 'CoercionForm')(data.row_format)
    cdef tuple v_colnames = _pg_list_to_tuple(data.colnames, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.RowExpr(v_args, v_row_format, v_colnames, v_location)


cdef create_RowCompareExpr(structs.RowCompareExpr* data, offset_to_index):
    cdef object v_rctype = getattr(enums, 'RowCompareType')(data.rctype)
    cdef tuple v_opnos = _pg_list_to_tuple(data.opnos, offset_to_index)
    cdef tuple v_opfamilies = _pg_list_to_tuple(data.opfamilies, offset_to_index)
    cdef tuple v_inputcollids = _pg_list_to_tuple(data.inputcollids, offset_to_index)
    cdef tuple v_largs = _pg_list_to_tuple(data.largs, offset_to_index)
    cdef tuple v_rargs = _pg_list_to_tuple(data.rargs, offset_to_index)
    return ast.RowCompareExpr(v_rctype, v_opnos, v_opfamilies, v_inputcollids, v_largs, v_rargs)


cdef create_CoalesceExpr(structs.CoalesceExpr* data, offset_to_index):
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.CoalesceExpr(v_args, v_location)


cdef create_MinMaxExpr(structs.MinMaxExpr* data, offset_to_index):
    cdef object v_op = getattr(enums, 'MinMaxOp')(data.op)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_location = offset_to_index(data.location)
    return ast.MinMaxExpr(v_op, v_args, v_location)


cdef create_SQLValueFunction(structs.SQLValueFunction* data, offset_to_index):
    cdef object v_op = getattr(enums, 'SQLValueFunctionOp')(data.op)
    cdef object v_typmod = data.typmod
    cdef object v_location = offset_to_index(data.location)
    return ast.SQLValueFunction(v_op, v_typmod, v_location)


cdef create_XmlExpr(structs.XmlExpr* data, offset_to_index):
    cdef object v_op = getattr(enums, 'XmlExprOp')(data.op)
    cdef object v_name = data.name.decode("utf-8") if data.name is not NULL else None
    cdef tuple v_named_args = _pg_list_to_tuple(data.named_args, offset_to_index)
    cdef tuple v_arg_names = _pg_list_to_tuple(data.arg_names, offset_to_index)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_xmloption = getattr(enums, 'XmlOptionType')(data.xmloption)
    cdef object v_indent = bool(data.indent)
    cdef object v_typmod = data.typmod
    cdef object v_location = offset_to_index(data.location)
    return ast.XmlExpr(v_op, v_name, v_named_args, v_arg_names, v_args, v_xmloption, v_indent, v_typmod, v_location)


cdef create_JsonFormat(structs.JsonFormat* data, offset_to_index):
    cdef object v_format_type = getattr(enums, 'JsonFormatType')(data.format_type)
    cdef object v_encoding = getattr(enums, 'JsonEncoding')(data.encoding)
    cdef object v_location = offset_to_index(data.location)
    return ast.JsonFormat(v_format_type, v_encoding, v_location)


cdef create_JsonReturning(structs.JsonReturning* data, offset_to_index):
    cdef object v_format = create(data.format, offset_to_index) if data.format is not NULL else None
    cdef object v_typmod = data.typmod
    return ast.JsonReturning(v_format, v_typmod)


cdef create_JsonValueExpr(structs.JsonValueExpr* data, offset_to_index):
    cdef object v_raw_expr = create(data.raw_expr, offset_to_index) if data.raw_expr is not NULL else None
    cdef object v_formatted_expr = create(data.formatted_expr, offset_to_index) if data.formatted_expr is not NULL else None
    cdef object v_format = create(data.format, offset_to_index) if data.format is not NULL else None
    return ast.JsonValueExpr(v_raw_expr, v_formatted_expr, v_format)


cdef create_JsonConstructorExpr(structs.JsonConstructorExpr* data, offset_to_index):
    cdef object v_type = getattr(enums, 'JsonConstructorType')(data.type)
    cdef tuple v_args = _pg_list_to_tuple(data.args, offset_to_index)
    cdef object v_func = create(data.func, offset_to_index) if data.func is not NULL else None
    cdef object v_coercion = create(data.coercion, offset_to_index) if data.coercion is not NULL else None
    cdef object v_returning = create(data.returning, offset_to_index) if data.returning is not NULL else None
    cdef object v_absent_on_null = bool(data.absent_on_null)
    cdef object v_unique = bool(data.unique)
    cdef object v_location = offset_to_index(data.location)
    return ast.JsonConstructorExpr(v_type, v_args, v_func, v_coercion, v_returning, v_absent_on_null, v_unique, v_location)


cdef create_JsonIsPredicate(structs.JsonIsPredicate* data, offset_to_index):
    cdef object v_expr = create(data.expr, offset_to_index) if data.expr is not NULL else None
    cdef object v_format = create(data.format, offset_to_index) if data.format is not NULL else None
    cdef object v_item_type = getattr(enums, 'JsonValueType')(data.item_type)
    cdef object v_unique_keys = bool(data.unique_keys)
    cdef object v_location = offset_to_index(data.location)
    return ast.JsonIsPredicate(v_expr, v_format, v_item_type, v_unique_keys, v_location)


cdef create_NullTest(structs.NullTest* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_nulltesttype = getattr(enums, 'NullTestType')(data.nulltesttype)
    cdef object v_argisrow = bool(data.argisrow)
    cdef object v_location = offset_to_index(data.location)
    return ast.NullTest(v_arg, v_nulltesttype, v_argisrow, v_location)


cdef create_BooleanTest(structs.BooleanTest* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_booltesttype = getattr(enums, 'BoolTestType')(data.booltesttype)
    cdef object v_location = offset_to_index(data.location)
    return ast.BooleanTest(v_arg, v_booltesttype, v_location)


cdef create_CoerceToDomain(structs.CoerceToDomain* data, offset_to_index):
    cdef object v_arg = create(data.arg, offset_to_index) if data.arg is not NULL else None
    cdef object v_resulttypmod = data.resulttypmod
    cdef object v_coercionformat = getattr(enums, 'CoercionForm')(data.coercionformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.CoerceToDomain(v_arg, v_resulttypmod, v_coercionformat, v_location)


cdef create_CoerceToDomainValue(structs.CoerceToDomainValue* data, offset_to_index):
    cdef object v_typeMod = data.typeMod
    cdef object v_location = offset_to_index(data.location)
    return ast.CoerceToDomainValue(v_typeMod, v_location)


cdef create_SetToDefault(structs.SetToDefault* data, offset_to_index):
    cdef object v_typeMod = data.typeMod
    cdef object v_location = offset_to_index(data.location)
    return ast.SetToDefault(v_typeMod, v_location)


cdef create_CurrentOfExpr(structs.CurrentOfExpr* data, offset_to_index):
    cdef object v_cvarno = data.cvarno
    cdef object v_cursor_name = data.cursor_name.decode("utf-8") if data.cursor_name is not NULL else None
    cdef object v_cursor_param = data.cursor_param
    return ast.CurrentOfExpr(v_cvarno, v_cursor_name, v_cursor_param)


cdef create_InferenceElem(structs.InferenceElem* data, offset_to_index):
    cdef object v_expr = create(data.expr, offset_to_index) if data.expr is not NULL else None
    return ast.InferenceElem(v_expr)


cdef create_TargetEntry(structs.TargetEntry* data, offset_to_index):
    cdef object v_expr = create(data.expr, offset_to_index) if data.expr is not NULL else None
    cdef object v_resno = data.resno
    cdef object v_resname = data.resname.decode("utf-8") if data.resname is not NULL else None
    cdef object v_ressortgroupref = data.ressortgroupref
    cdef object v_resorigcol = data.resorigcol
    cdef object v_resjunk = bool(data.resjunk)
    return ast.TargetEntry(v_expr, v_resno, v_resname, v_ressortgroupref, v_resorigcol, v_resjunk)


cdef create_RangeTblRef(structs.RangeTblRef* data, offset_to_index):
    cdef object v_rtindex = data.rtindex
    return ast.RangeTblRef(v_rtindex)


cdef create_JoinExpr(structs.JoinExpr* data, offset_to_index):
    cdef object v_jointype = getattr(enums, 'JoinType')(data.jointype)
    cdef object v_isNatural = bool(data.isNatural)
    cdef object v_larg = create(data.larg, offset_to_index) if data.larg is not NULL else None
    cdef object v_rarg = create(data.rarg, offset_to_index) if data.rarg is not NULL else None
    cdef tuple v_usingClause = _pg_list_to_tuple(data.usingClause, offset_to_index)
    cdef object v_join_using_alias = create(data.join_using_alias, offset_to_index) if data.join_using_alias is not NULL else None
    cdef object v_quals = create(data.quals, offset_to_index) if data.quals is not NULL else None
    cdef object v_alias = create(data.alias, offset_to_index) if data.alias is not NULL else None
    cdef object v_rtindex = data.rtindex
    return ast.JoinExpr(v_jointype, v_isNatural, v_larg, v_rarg, v_usingClause, v_join_using_alias, v_quals, v_alias, v_rtindex)


cdef create_FromExpr(structs.FromExpr* data, offset_to_index):
    cdef tuple v_fromlist = _pg_list_to_tuple(data.fromlist, offset_to_index)
    cdef object v_quals = create(data.quals, offset_to_index) if data.quals is not NULL else None
    return ast.FromExpr(v_fromlist, v_quals)


cdef create_OnConflictExpr(structs.OnConflictExpr* data, offset_to_index):
    cdef object v_action = getattr(enums, 'OnConflictAction')(data.action)
    cdef tuple v_arbiterElems = _pg_list_to_tuple(data.arbiterElems, offset_to_index)
    cdef object v_arbiterWhere = create(data.arbiterWhere, offset_to_index) if data.arbiterWhere is not NULL else None
    cdef tuple v_onConflictSet = _pg_list_to_tuple(data.onConflictSet, offset_to_index)
    cdef object v_onConflictWhere = create(data.onConflictWhere, offset_to_index) if data.onConflictWhere is not NULL else None
    cdef object v_exclRelIndex = data.exclRelIndex
    cdef tuple v_exclRelTlist = _pg_list_to_tuple(data.exclRelTlist, offset_to_index)
    return ast.OnConflictExpr(v_action, v_arbiterElems, v_arbiterWhere, v_onConflictSet, v_onConflictWhere, v_exclRelIndex, v_exclRelTlist)


cdef create_Integer(structs.Integer* data, offset_to_index):
    cdef object v_ival = data.ival
    return ast.Integer(v_ival)


cdef create_Float(structs.Float* data, offset_to_index):
    cdef object v_fval = data.fval.decode("utf-8") if data.fval is not NULL else None
    return ast.Float(v_fval)


cdef create_Boolean(structs.Boolean* data, offset_to_index):
    cdef object v_boolval = bool(data.boolval)
    return ast.Boolean(v_boolval)


cdef create_String(structs.String* data, offset_to_index):
    cdef object v_sval = data.sval.decode("utf-8") if data.sval is not NULL else None
    return ast.String(v_sval)


cdef create_BitString(structs.BitString* data, offset_to_index):
    cdef object v_bsval = data.bsval.decode("utf-8") if data.bsval is not NULL else None
    return ast.BitString(v_bsval)


cdef create_A_Const(structs.A_Const* data, offset_to_index):
    cdef object v_isnull = bool(data.isnull)
    cdef object v_val
    if data.isnull:
        v_val = None
    elif data.val.boolval.type == structs.T_Boolean:
        v_val = ast.Boolean(data.val.boolval.boolval)
    elif data.val.ival.type == structs.T_Integer:
        v_val = ast.Integer(data.val.ival.ival)
    elif data.val.fval.type == structs.T_Float:
        v_val = ast.Float(data.val.fval.fval.decode("utf-8"))
    elif data.val.bsval.type == structs.T_BitString:
        v_val = ast.BitString(data.val.bsval.bsval.decode("utf-8"))
    elif data.val.sval.type == structs.T_String:
        v_val = ast.String(data.val.sval.sval.decode("utf-8"))
    else:
        v_val = data.val.node
    return ast.A_Const(v_isnull, v_val)


cdef create(void* data, offset_to_index):
    if data is NULL:
        return None

    cdef tuple t
    cdef int i
    cdef str s
    cdef int tag = structs.nodeTag(data)

    if tag == structs.T_List:
         return _pg_list_to_tuple(<structs.List *> data, offset_to_index)
    elif tag == structs.T_Alias:
        return create_Alias(<structs.Alias*> data, offset_to_index)
    elif tag == structs.T_RangeVar:
        return create_RangeVar(<structs.RangeVar*> data, offset_to_index)
    elif tag == structs.T_TableFunc:
        return create_TableFunc(<structs.TableFunc*> data, offset_to_index)
    elif tag == structs.T_IntoClause:
        return create_IntoClause(<structs.IntoClause*> data, offset_to_index)
    elif tag == structs.T_Var:
        return create_Var(<structs.Var*> data, offset_to_index)
    elif tag == structs.T_Param:
        return create_Param(<structs.Param*> data, offset_to_index)
    elif tag == structs.T_Aggref:
        return create_Aggref(<structs.Aggref*> data, offset_to_index)
    elif tag == structs.T_GroupingFunc:
        return create_GroupingFunc(<structs.GroupingFunc*> data, offset_to_index)
    elif tag == structs.T_WindowFunc:
        return create_WindowFunc(<structs.WindowFunc*> data, offset_to_index)
    elif tag == structs.T_SubscriptingRef:
        return create_SubscriptingRef(<structs.SubscriptingRef*> data, offset_to_index)
    elif tag == structs.T_FuncExpr:
        return create_FuncExpr(<structs.FuncExpr*> data, offset_to_index)
    elif tag == structs.T_NamedArgExpr:
        return create_NamedArgExpr(<structs.NamedArgExpr*> data, offset_to_index)
    elif tag == structs.T_OpExpr:
        return create_OpExpr(<structs.OpExpr*> data, offset_to_index)
    elif tag == structs.T_ScalarArrayOpExpr:
        return create_ScalarArrayOpExpr(<structs.ScalarArrayOpExpr*> data, offset_to_index)
    elif tag == structs.T_BoolExpr:
        return create_BoolExpr(<structs.BoolExpr*> data, offset_to_index)
    elif tag == structs.T_SubLink:
        return create_SubLink(<structs.SubLink*> data, offset_to_index)
    elif tag == structs.T_SubPlan:
        return create_SubPlan(<structs.SubPlan*> data, offset_to_index)
    elif tag == structs.T_AlternativeSubPlan:
        return create_AlternativeSubPlan(<structs.AlternativeSubPlan*> data, offset_to_index)
    elif tag == structs.T_FieldSelect:
        return create_FieldSelect(<structs.FieldSelect*> data, offset_to_index)
    elif tag == structs.T_FieldStore:
        return create_FieldStore(<structs.FieldStore*> data, offset_to_index)
    elif tag == structs.T_RelabelType:
        return create_RelabelType(<structs.RelabelType*> data, offset_to_index)
    elif tag == structs.T_CoerceViaIO:
        return create_CoerceViaIO(<structs.CoerceViaIO*> data, offset_to_index)
    elif tag == structs.T_ArrayCoerceExpr:
        return create_ArrayCoerceExpr(<structs.ArrayCoerceExpr*> data, offset_to_index)
    elif tag == structs.T_ConvertRowtypeExpr:
        return create_ConvertRowtypeExpr(<structs.ConvertRowtypeExpr*> data, offset_to_index)
    elif tag == structs.T_CollateExpr:
        return create_CollateExpr(<structs.CollateExpr*> data, offset_to_index)
    elif tag == structs.T_CaseExpr:
        return create_CaseExpr(<structs.CaseExpr*> data, offset_to_index)
    elif tag == structs.T_CaseWhen:
        return create_CaseWhen(<structs.CaseWhen*> data, offset_to_index)
    elif tag == structs.T_CaseTestExpr:
        return create_CaseTestExpr(<structs.CaseTestExpr*> data, offset_to_index)
    elif tag == structs.T_ArrayExpr:
        return create_ArrayExpr(<structs.ArrayExpr*> data, offset_to_index)
    elif tag == structs.T_RowExpr:
        return create_RowExpr(<structs.RowExpr*> data, offset_to_index)
    elif tag == structs.T_RowCompareExpr:
        return create_RowCompareExpr(<structs.RowCompareExpr*> data, offset_to_index)
    elif tag == structs.T_CoalesceExpr:
        return create_CoalesceExpr(<structs.CoalesceExpr*> data, offset_to_index)
    elif tag == structs.T_MinMaxExpr:
        return create_MinMaxExpr(<structs.MinMaxExpr*> data, offset_to_index)
    elif tag == structs.T_SQLValueFunction:
        return create_SQLValueFunction(<structs.SQLValueFunction*> data, offset_to_index)
    elif tag == structs.T_XmlExpr:
        return create_XmlExpr(<structs.XmlExpr*> data, offset_to_index)
    elif tag == structs.T_JsonFormat:
        return create_JsonFormat(<structs.JsonFormat*> data, offset_to_index)
    elif tag == structs.T_JsonReturning:
        return create_JsonReturning(<structs.JsonReturning*> data, offset_to_index)
    elif tag == structs.T_JsonValueExpr:
        return create_JsonValueExpr(<structs.JsonValueExpr*> data, offset_to_index)
    elif tag == structs.T_JsonConstructorExpr:
        return create_JsonConstructorExpr(<structs.JsonConstructorExpr*> data, offset_to_index)
    elif tag == structs.T_JsonIsPredicate:
        return create_JsonIsPredicate(<structs.JsonIsPredicate*> data, offset_to_index)
    elif tag == structs.T_NullTest:
        return create_NullTest(<structs.NullTest*> data, offset_to_index)
    elif tag == structs.T_BooleanTest:
        return create_BooleanTest(<structs.BooleanTest*> data, offset_to_index)
    elif tag == structs.T_CoerceToDomain:
        return create_CoerceToDomain(<structs.CoerceToDomain*> data, offset_to_index)
    elif tag == structs.T_CoerceToDomainValue:
        return create_CoerceToDomainValue(<structs.CoerceToDomainValue*> data, offset_to_index)
    elif tag == structs.T_SetToDefault:
        return create_SetToDefault(<structs.SetToDefault*> data, offset_to_index)
    elif tag == structs.T_CurrentOfExpr:
        return create_CurrentOfExpr(<structs.CurrentOfExpr*> data, offset_to_index)
    elif tag == structs.T_InferenceElem:
        return create_InferenceElem(<structs.InferenceElem*> data, offset_to_index)
    elif tag == structs.T_TargetEntry:
        return create_TargetEntry(<structs.TargetEntry*> data, offset_to_index)
    elif tag == structs.T_RangeTblRef:
        return create_RangeTblRef(<structs.RangeTblRef*> data, offset_to_index)
    elif tag == structs.T_JoinExpr:
        return create_JoinExpr(<structs.JoinExpr*> data, offset_to_index)
    elif tag == structs.T_FromExpr:
        return create_FromExpr(<structs.FromExpr*> data, offset_to_index)
    elif tag == structs.T_OnConflictExpr:
        return create_OnConflictExpr(<structs.OnConflictExpr*> data, offset_to_index)
    elif tag == structs.T_Query:
        return create_Query(<structs.Query*> data, offset_to_index)
    elif tag == structs.T_TypeName:
        return create_TypeName(<structs.TypeName*> data, offset_to_index)
    elif tag == structs.T_ColumnRef:
        return create_ColumnRef(<structs.ColumnRef*> data, offset_to_index)
    elif tag == structs.T_ParamRef:
        return create_ParamRef(<structs.ParamRef*> data, offset_to_index)
    elif tag == structs.T_A_Expr:
        return create_A_Expr(<structs.A_Expr*> data, offset_to_index)
    elif tag == structs.T_A_Const:
        return create_A_Const(<structs.A_Const*> data, offset_to_index)
    elif tag == structs.T_TypeCast:
        return create_TypeCast(<structs.TypeCast*> data, offset_to_index)
    elif tag == structs.T_CollateClause:
        return create_CollateClause(<structs.CollateClause*> data, offset_to_index)
    elif tag == structs.T_RoleSpec:
        return create_RoleSpec(<structs.RoleSpec*> data, offset_to_index)
    elif tag == structs.T_FuncCall:
        return create_FuncCall(<structs.FuncCall*> data, offset_to_index)
    elif tag == structs.T_A_Star:
        return create_A_Star(<structs.A_Star*> data, offset_to_index)
    elif tag == structs.T_A_Indices:
        return create_A_Indices(<structs.A_Indices*> data, offset_to_index)
    elif tag == structs.T_A_Indirection:
        return create_A_Indirection(<structs.A_Indirection*> data, offset_to_index)
    elif tag == structs.T_A_ArrayExpr:
        return create_A_ArrayExpr(<structs.A_ArrayExpr*> data, offset_to_index)
    elif tag == structs.T_ResTarget:
        return create_ResTarget(<structs.ResTarget*> data, offset_to_index)
    elif tag == structs.T_MultiAssignRef:
        return create_MultiAssignRef(<structs.MultiAssignRef*> data, offset_to_index)
    elif tag == structs.T_SortBy:
        return create_SortBy(<structs.SortBy*> data, offset_to_index)
    elif tag == structs.T_WindowDef:
        return create_WindowDef(<structs.WindowDef*> data, offset_to_index)
    elif tag == structs.T_RangeSubselect:
        return create_RangeSubselect(<structs.RangeSubselect*> data, offset_to_index)
    elif tag == structs.T_RangeFunction:
        return create_RangeFunction(<structs.RangeFunction*> data, offset_to_index)
    elif tag == structs.T_RangeTableFunc:
        return create_RangeTableFunc(<structs.RangeTableFunc*> data, offset_to_index)
    elif tag == structs.T_RangeTableFuncCol:
        return create_RangeTableFuncCol(<structs.RangeTableFuncCol*> data, offset_to_index)
    elif tag == structs.T_RangeTableSample:
        return create_RangeTableSample(<structs.RangeTableSample*> data, offset_to_index)
    elif tag == structs.T_ColumnDef:
        return create_ColumnDef(<structs.ColumnDef*> data, offset_to_index)
    elif tag == structs.T_TableLikeClause:
        return create_TableLikeClause(<structs.TableLikeClause*> data, offset_to_index)
    elif tag == structs.T_IndexElem:
        return create_IndexElem(<structs.IndexElem*> data, offset_to_index)
    elif tag == structs.T_DefElem:
        return create_DefElem(<structs.DefElem*> data, offset_to_index)
    elif tag == structs.T_LockingClause:
        return create_LockingClause(<structs.LockingClause*> data, offset_to_index)
    elif tag == structs.T_XmlSerialize:
        return create_XmlSerialize(<structs.XmlSerialize*> data, offset_to_index)
    elif tag == structs.T_PartitionElem:
        return create_PartitionElem(<structs.PartitionElem*> data, offset_to_index)
    elif tag == structs.T_PartitionSpec:
        return create_PartitionSpec(<structs.PartitionSpec*> data, offset_to_index)
    elif tag == structs.T_PartitionBoundSpec:
        return create_PartitionBoundSpec(<structs.PartitionBoundSpec*> data, offset_to_index)
    elif tag == structs.T_PartitionRangeDatum:
        return create_PartitionRangeDatum(<structs.PartitionRangeDatum*> data, offset_to_index)
    elif tag == structs.T_PartitionCmd:
        return create_PartitionCmd(<structs.PartitionCmd*> data, offset_to_index)
    elif tag == structs.T_RangeTblEntry:
        return create_RangeTblEntry(<structs.RangeTblEntry*> data, offset_to_index)
    elif tag == structs.T_RTEPermissionInfo:
        return create_RTEPermissionInfo(<structs.RTEPermissionInfo*> data, offset_to_index)
    elif tag == structs.T_RangeTblFunction:
        return create_RangeTblFunction(<structs.RangeTblFunction*> data, offset_to_index)
    elif tag == structs.T_TableSampleClause:
        return create_TableSampleClause(<structs.TableSampleClause*> data, offset_to_index)
    elif tag == structs.T_WithCheckOption:
        return create_WithCheckOption(<structs.WithCheckOption*> data, offset_to_index)
    elif tag == structs.T_SortGroupClause:
        return create_SortGroupClause(<structs.SortGroupClause*> data, offset_to_index)
    elif tag == structs.T_GroupingSet:
        return create_GroupingSet(<structs.GroupingSet*> data, offset_to_index)
    elif tag == structs.T_WindowClause:
        return create_WindowClause(<structs.WindowClause*> data, offset_to_index)
    elif tag == structs.T_RowMarkClause:
        return create_RowMarkClause(<structs.RowMarkClause*> data, offset_to_index)
    elif tag == structs.T_WithClause:
        return create_WithClause(<structs.WithClause*> data, offset_to_index)
    elif tag == structs.T_InferClause:
        return create_InferClause(<structs.InferClause*> data, offset_to_index)
    elif tag == structs.T_OnConflictClause:
        return create_OnConflictClause(<structs.OnConflictClause*> data, offset_to_index)
    elif tag == structs.T_CTESearchClause:
        return create_CTESearchClause(<structs.CTESearchClause*> data, offset_to_index)
    elif tag == structs.T_CTECycleClause:
        return create_CTECycleClause(<structs.CTECycleClause*> data, offset_to_index)
    elif tag == structs.T_CommonTableExpr:
        return create_CommonTableExpr(<structs.CommonTableExpr*> data, offset_to_index)
    elif tag == structs.T_MergeWhenClause:
        return create_MergeWhenClause(<structs.MergeWhenClause*> data, offset_to_index)
    elif tag == structs.T_MergeAction:
        return create_MergeAction(<structs.MergeAction*> data, offset_to_index)
    elif tag == structs.T_TriggerTransition:
        return create_TriggerTransition(<structs.TriggerTransition*> data, offset_to_index)
    elif tag == structs.T_JsonOutput:
        return create_JsonOutput(<structs.JsonOutput*> data, offset_to_index)
    elif tag == structs.T_JsonKeyValue:
        return create_JsonKeyValue(<structs.JsonKeyValue*> data, offset_to_index)
    elif tag == structs.T_JsonObjectConstructor:
        return create_JsonObjectConstructor(<structs.JsonObjectConstructor*> data, offset_to_index)
    elif tag == structs.T_JsonArrayConstructor:
        return create_JsonArrayConstructor(<structs.JsonArrayConstructor*> data, offset_to_index)
    elif tag == structs.T_JsonArrayQueryConstructor:
        return create_JsonArrayQueryConstructor(<structs.JsonArrayQueryConstructor*> data, offset_to_index)
    elif tag == structs.T_JsonAggConstructor:
        return create_JsonAggConstructor(<structs.JsonAggConstructor*> data, offset_to_index)
    elif tag == structs.T_JsonObjectAgg:
        return create_JsonObjectAgg(<structs.JsonObjectAgg*> data, offset_to_index)
    elif tag == structs.T_JsonArrayAgg:
        return create_JsonArrayAgg(<structs.JsonArrayAgg*> data, offset_to_index)
    elif tag == structs.T_RawStmt:
        return create_RawStmt(<structs.RawStmt*> data, offset_to_index)
    elif tag == structs.T_InsertStmt:
        return create_InsertStmt(<structs.InsertStmt*> data, offset_to_index)
    elif tag == structs.T_DeleteStmt:
        return create_DeleteStmt(<structs.DeleteStmt*> data, offset_to_index)
    elif tag == structs.T_UpdateStmt:
        return create_UpdateStmt(<structs.UpdateStmt*> data, offset_to_index)
    elif tag == structs.T_MergeStmt:
        return create_MergeStmt(<structs.MergeStmt*> data, offset_to_index)
    elif tag == structs.T_SelectStmt:
        return create_SelectStmt(<structs.SelectStmt*> data, offset_to_index)
    elif tag == structs.T_SetOperationStmt:
        return create_SetOperationStmt(<structs.SetOperationStmt*> data, offset_to_index)
    elif tag == structs.T_ReturnStmt:
        return create_ReturnStmt(<structs.ReturnStmt*> data, offset_to_index)
    elif tag == structs.T_PLAssignStmt:
        return create_PLAssignStmt(<structs.PLAssignStmt*> data, offset_to_index)
    elif tag == structs.T_CreateSchemaStmt:
        return create_CreateSchemaStmt(<structs.CreateSchemaStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTableStmt:
        return create_AlterTableStmt(<structs.AlterTableStmt*> data, offset_to_index)
    elif tag == structs.T_ReplicaIdentityStmt:
        return create_ReplicaIdentityStmt(<structs.ReplicaIdentityStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTableCmd:
        return create_AlterTableCmd(<structs.AlterTableCmd*> data, offset_to_index)
    elif tag == structs.T_AlterCollationStmt:
        return create_AlterCollationStmt(<structs.AlterCollationStmt*> data, offset_to_index)
    elif tag == structs.T_AlterDomainStmt:
        return create_AlterDomainStmt(<structs.AlterDomainStmt*> data, offset_to_index)
    elif tag == structs.T_GrantStmt:
        return create_GrantStmt(<structs.GrantStmt*> data, offset_to_index)
    elif tag == structs.T_ObjectWithArgs:
        return create_ObjectWithArgs(<structs.ObjectWithArgs*> data, offset_to_index)
    elif tag == structs.T_AccessPriv:
        return create_AccessPriv(<structs.AccessPriv*> data, offset_to_index)
    elif tag == structs.T_GrantRoleStmt:
        return create_GrantRoleStmt(<structs.GrantRoleStmt*> data, offset_to_index)
    elif tag == structs.T_AlterDefaultPrivilegesStmt:
        return create_AlterDefaultPrivilegesStmt(<structs.AlterDefaultPrivilegesStmt*> data, offset_to_index)
    elif tag == structs.T_CopyStmt:
        return create_CopyStmt(<structs.CopyStmt*> data, offset_to_index)
    elif tag == structs.T_VariableSetStmt:
        return create_VariableSetStmt(<structs.VariableSetStmt*> data, offset_to_index)
    elif tag == structs.T_VariableShowStmt:
        return create_VariableShowStmt(<structs.VariableShowStmt*> data, offset_to_index)
    elif tag == structs.T_CreateStmt:
        return create_CreateStmt(<structs.CreateStmt*> data, offset_to_index)
    elif tag == structs.T_Constraint:
        return create_Constraint(<structs.Constraint*> data, offset_to_index)
    elif tag == structs.T_CreateTableSpaceStmt:
        return create_CreateTableSpaceStmt(<structs.CreateTableSpaceStmt*> data, offset_to_index)
    elif tag == structs.T_DropTableSpaceStmt:
        return create_DropTableSpaceStmt(<structs.DropTableSpaceStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTableSpaceOptionsStmt:
        return create_AlterTableSpaceOptionsStmt(<structs.AlterTableSpaceOptionsStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTableMoveAllStmt:
        return create_AlterTableMoveAllStmt(<structs.AlterTableMoveAllStmt*> data, offset_to_index)
    elif tag == structs.T_CreateExtensionStmt:
        return create_CreateExtensionStmt(<structs.CreateExtensionStmt*> data, offset_to_index)
    elif tag == structs.T_AlterExtensionStmt:
        return create_AlterExtensionStmt(<structs.AlterExtensionStmt*> data, offset_to_index)
    elif tag == structs.T_AlterExtensionContentsStmt:
        return create_AlterExtensionContentsStmt(<structs.AlterExtensionContentsStmt*> data, offset_to_index)
    elif tag == structs.T_CreateFdwStmt:
        return create_CreateFdwStmt(<structs.CreateFdwStmt*> data, offset_to_index)
    elif tag == structs.T_AlterFdwStmt:
        return create_AlterFdwStmt(<structs.AlterFdwStmt*> data, offset_to_index)
    elif tag == structs.T_CreateForeignServerStmt:
        return create_CreateForeignServerStmt(<structs.CreateForeignServerStmt*> data, offset_to_index)
    elif tag == structs.T_AlterForeignServerStmt:
        return create_AlterForeignServerStmt(<structs.AlterForeignServerStmt*> data, offset_to_index)
    elif tag == structs.T_CreateForeignTableStmt:
        return create_CreateForeignTableStmt(<structs.CreateForeignTableStmt*> data, offset_to_index)
    elif tag == structs.T_CreateUserMappingStmt:
        return create_CreateUserMappingStmt(<structs.CreateUserMappingStmt*> data, offset_to_index)
    elif tag == structs.T_AlterUserMappingStmt:
        return create_AlterUserMappingStmt(<structs.AlterUserMappingStmt*> data, offset_to_index)
    elif tag == structs.T_DropUserMappingStmt:
        return create_DropUserMappingStmt(<structs.DropUserMappingStmt*> data, offset_to_index)
    elif tag == structs.T_ImportForeignSchemaStmt:
        return create_ImportForeignSchemaStmt(<structs.ImportForeignSchemaStmt*> data, offset_to_index)
    elif tag == structs.T_CreatePolicyStmt:
        return create_CreatePolicyStmt(<structs.CreatePolicyStmt*> data, offset_to_index)
    elif tag == structs.T_AlterPolicyStmt:
        return create_AlterPolicyStmt(<structs.AlterPolicyStmt*> data, offset_to_index)
    elif tag == structs.T_CreateAmStmt:
        return create_CreateAmStmt(<structs.CreateAmStmt*> data, offset_to_index)
    elif tag == structs.T_CreateTrigStmt:
        return create_CreateTrigStmt(<structs.CreateTrigStmt*> data, offset_to_index)
    elif tag == structs.T_CreateEventTrigStmt:
        return create_CreateEventTrigStmt(<structs.CreateEventTrigStmt*> data, offset_to_index)
    elif tag == structs.T_AlterEventTrigStmt:
        return create_AlterEventTrigStmt(<structs.AlterEventTrigStmt*> data, offset_to_index)
    elif tag == structs.T_CreatePLangStmt:
        return create_CreatePLangStmt(<structs.CreatePLangStmt*> data, offset_to_index)
    elif tag == structs.T_CreateRoleStmt:
        return create_CreateRoleStmt(<structs.CreateRoleStmt*> data, offset_to_index)
    elif tag == structs.T_AlterRoleStmt:
        return create_AlterRoleStmt(<structs.AlterRoleStmt*> data, offset_to_index)
    elif tag == structs.T_AlterRoleSetStmt:
        return create_AlterRoleSetStmt(<structs.AlterRoleSetStmt*> data, offset_to_index)
    elif tag == structs.T_DropRoleStmt:
        return create_DropRoleStmt(<structs.DropRoleStmt*> data, offset_to_index)
    elif tag == structs.T_CreateSeqStmt:
        return create_CreateSeqStmt(<structs.CreateSeqStmt*> data, offset_to_index)
    elif tag == structs.T_AlterSeqStmt:
        return create_AlterSeqStmt(<structs.AlterSeqStmt*> data, offset_to_index)
    elif tag == structs.T_DefineStmt:
        return create_DefineStmt(<structs.DefineStmt*> data, offset_to_index)
    elif tag == structs.T_CreateDomainStmt:
        return create_CreateDomainStmt(<structs.CreateDomainStmt*> data, offset_to_index)
    elif tag == structs.T_CreateOpClassStmt:
        return create_CreateOpClassStmt(<structs.CreateOpClassStmt*> data, offset_to_index)
    elif tag == structs.T_CreateOpClassItem:
        return create_CreateOpClassItem(<structs.CreateOpClassItem*> data, offset_to_index)
    elif tag == structs.T_CreateOpFamilyStmt:
        return create_CreateOpFamilyStmt(<structs.CreateOpFamilyStmt*> data, offset_to_index)
    elif tag == structs.T_AlterOpFamilyStmt:
        return create_AlterOpFamilyStmt(<structs.AlterOpFamilyStmt*> data, offset_to_index)
    elif tag == structs.T_DropStmt:
        return create_DropStmt(<structs.DropStmt*> data, offset_to_index)
    elif tag == structs.T_TruncateStmt:
        return create_TruncateStmt(<structs.TruncateStmt*> data, offset_to_index)
    elif tag == structs.T_CommentStmt:
        return create_CommentStmt(<structs.CommentStmt*> data, offset_to_index)
    elif tag == structs.T_SecLabelStmt:
        return create_SecLabelStmt(<structs.SecLabelStmt*> data, offset_to_index)
    elif tag == structs.T_DeclareCursorStmt:
        return create_DeclareCursorStmt(<structs.DeclareCursorStmt*> data, offset_to_index)
    elif tag == structs.T_ClosePortalStmt:
        return create_ClosePortalStmt(<structs.ClosePortalStmt*> data, offset_to_index)
    elif tag == structs.T_FetchStmt:
        return create_FetchStmt(<structs.FetchStmt*> data, offset_to_index)
    elif tag == structs.T_IndexStmt:
        return create_IndexStmt(<structs.IndexStmt*> data, offset_to_index)
    elif tag == structs.T_CreateStatsStmt:
        return create_CreateStatsStmt(<structs.CreateStatsStmt*> data, offset_to_index)
    elif tag == structs.T_StatsElem:
        return create_StatsElem(<structs.StatsElem*> data, offset_to_index)
    elif tag == structs.T_AlterStatsStmt:
        return create_AlterStatsStmt(<structs.AlterStatsStmt*> data, offset_to_index)
    elif tag == structs.T_CreateFunctionStmt:
        return create_CreateFunctionStmt(<structs.CreateFunctionStmt*> data, offset_to_index)
    elif tag == structs.T_FunctionParameter:
        return create_FunctionParameter(<structs.FunctionParameter*> data, offset_to_index)
    elif tag == structs.T_AlterFunctionStmt:
        return create_AlterFunctionStmt(<structs.AlterFunctionStmt*> data, offset_to_index)
    elif tag == structs.T_DoStmt:
        return create_DoStmt(<structs.DoStmt*> data, offset_to_index)
    elif tag == structs.T_InlineCodeBlock:
        return create_InlineCodeBlock(<structs.InlineCodeBlock*> data, offset_to_index)
    elif tag == structs.T_CallStmt:
        return create_CallStmt(<structs.CallStmt*> data, offset_to_index)
    elif tag == structs.T_CallContext:
        return create_CallContext(<structs.CallContext*> data, offset_to_index)
    elif tag == structs.T_RenameStmt:
        return create_RenameStmt(<structs.RenameStmt*> data, offset_to_index)
    elif tag == structs.T_AlterObjectDependsStmt:
        return create_AlterObjectDependsStmt(<structs.AlterObjectDependsStmt*> data, offset_to_index)
    elif tag == structs.T_AlterObjectSchemaStmt:
        return create_AlterObjectSchemaStmt(<structs.AlterObjectSchemaStmt*> data, offset_to_index)
    elif tag == structs.T_AlterOwnerStmt:
        return create_AlterOwnerStmt(<structs.AlterOwnerStmt*> data, offset_to_index)
    elif tag == structs.T_AlterOperatorStmt:
        return create_AlterOperatorStmt(<structs.AlterOperatorStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTypeStmt:
        return create_AlterTypeStmt(<structs.AlterTypeStmt*> data, offset_to_index)
    elif tag == structs.T_RuleStmt:
        return create_RuleStmt(<structs.RuleStmt*> data, offset_to_index)
    elif tag == structs.T_NotifyStmt:
        return create_NotifyStmt(<structs.NotifyStmt*> data, offset_to_index)
    elif tag == structs.T_ListenStmt:
        return create_ListenStmt(<structs.ListenStmt*> data, offset_to_index)
    elif tag == structs.T_UnlistenStmt:
        return create_UnlistenStmt(<structs.UnlistenStmt*> data, offset_to_index)
    elif tag == structs.T_TransactionStmt:
        return create_TransactionStmt(<structs.TransactionStmt*> data, offset_to_index)
    elif tag == structs.T_CompositeTypeStmt:
        return create_CompositeTypeStmt(<structs.CompositeTypeStmt*> data, offset_to_index)
    elif tag == structs.T_CreateEnumStmt:
        return create_CreateEnumStmt(<structs.CreateEnumStmt*> data, offset_to_index)
    elif tag == structs.T_CreateRangeStmt:
        return create_CreateRangeStmt(<structs.CreateRangeStmt*> data, offset_to_index)
    elif tag == structs.T_AlterEnumStmt:
        return create_AlterEnumStmt(<structs.AlterEnumStmt*> data, offset_to_index)
    elif tag == structs.T_ViewStmt:
        return create_ViewStmt(<structs.ViewStmt*> data, offset_to_index)
    elif tag == structs.T_LoadStmt:
        return create_LoadStmt(<structs.LoadStmt*> data, offset_to_index)
    elif tag == structs.T_CreatedbStmt:
        return create_CreatedbStmt(<structs.CreatedbStmt*> data, offset_to_index)
    elif tag == structs.T_AlterDatabaseStmt:
        return create_AlterDatabaseStmt(<structs.AlterDatabaseStmt*> data, offset_to_index)
    elif tag == structs.T_AlterDatabaseRefreshCollStmt:
        return create_AlterDatabaseRefreshCollStmt(<structs.AlterDatabaseRefreshCollStmt*> data, offset_to_index)
    elif tag == structs.T_AlterDatabaseSetStmt:
        return create_AlterDatabaseSetStmt(<structs.AlterDatabaseSetStmt*> data, offset_to_index)
    elif tag == structs.T_DropdbStmt:
        return create_DropdbStmt(<structs.DropdbStmt*> data, offset_to_index)
    elif tag == structs.T_AlterSystemStmt:
        return create_AlterSystemStmt(<structs.AlterSystemStmt*> data, offset_to_index)
    elif tag == structs.T_ClusterStmt:
        return create_ClusterStmt(<structs.ClusterStmt*> data, offset_to_index)
    elif tag == structs.T_VacuumStmt:
        return create_VacuumStmt(<structs.VacuumStmt*> data, offset_to_index)
    elif tag == structs.T_VacuumRelation:
        return create_VacuumRelation(<structs.VacuumRelation*> data, offset_to_index)
    elif tag == structs.T_ExplainStmt:
        return create_ExplainStmt(<structs.ExplainStmt*> data, offset_to_index)
    elif tag == structs.T_CreateTableAsStmt:
        return create_CreateTableAsStmt(<structs.CreateTableAsStmt*> data, offset_to_index)
    elif tag == structs.T_RefreshMatViewStmt:
        return create_RefreshMatViewStmt(<structs.RefreshMatViewStmt*> data, offset_to_index)
    elif tag == structs.T_CheckPointStmt:
        return create_CheckPointStmt(<structs.CheckPointStmt*> data, offset_to_index)
    elif tag == structs.T_DiscardStmt:
        return create_DiscardStmt(<structs.DiscardStmt*> data, offset_to_index)
    elif tag == structs.T_LockStmt:
        return create_LockStmt(<structs.LockStmt*> data, offset_to_index)
    elif tag == structs.T_ConstraintsSetStmt:
        return create_ConstraintsSetStmt(<structs.ConstraintsSetStmt*> data, offset_to_index)
    elif tag == structs.T_ReindexStmt:
        return create_ReindexStmt(<structs.ReindexStmt*> data, offset_to_index)
    elif tag == structs.T_CreateConversionStmt:
        return create_CreateConversionStmt(<structs.CreateConversionStmt*> data, offset_to_index)
    elif tag == structs.T_CreateCastStmt:
        return create_CreateCastStmt(<structs.CreateCastStmt*> data, offset_to_index)
    elif tag == structs.T_CreateTransformStmt:
        return create_CreateTransformStmt(<structs.CreateTransformStmt*> data, offset_to_index)
    elif tag == structs.T_PrepareStmt:
        return create_PrepareStmt(<structs.PrepareStmt*> data, offset_to_index)
    elif tag == structs.T_ExecuteStmt:
        return create_ExecuteStmt(<structs.ExecuteStmt*> data, offset_to_index)
    elif tag == structs.T_DeallocateStmt:
        return create_DeallocateStmt(<structs.DeallocateStmt*> data, offset_to_index)
    elif tag == structs.T_DropOwnedStmt:
        return create_DropOwnedStmt(<structs.DropOwnedStmt*> data, offset_to_index)
    elif tag == structs.T_ReassignOwnedStmt:
        return create_ReassignOwnedStmt(<structs.ReassignOwnedStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTSDictionaryStmt:
        return create_AlterTSDictionaryStmt(<structs.AlterTSDictionaryStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTSConfigurationStmt:
        return create_AlterTSConfigurationStmt(<structs.AlterTSConfigurationStmt*> data, offset_to_index)
    elif tag == structs.T_PublicationTable:
        return create_PublicationTable(<structs.PublicationTable*> data, offset_to_index)
    elif tag == structs.T_PublicationObjSpec:
        return create_PublicationObjSpec(<structs.PublicationObjSpec*> data, offset_to_index)
    elif tag == structs.T_CreatePublicationStmt:
        return create_CreatePublicationStmt(<structs.CreatePublicationStmt*> data, offset_to_index)
    elif tag == structs.T_AlterPublicationStmt:
        return create_AlterPublicationStmt(<structs.AlterPublicationStmt*> data, offset_to_index)
    elif tag == structs.T_CreateSubscriptionStmt:
        return create_CreateSubscriptionStmt(<structs.CreateSubscriptionStmt*> data, offset_to_index)
    elif tag == structs.T_AlterSubscriptionStmt:
        return create_AlterSubscriptionStmt(<structs.AlterSubscriptionStmt*> data, offset_to_index)
    elif tag == structs.T_DropSubscriptionStmt:
        return create_DropSubscriptionStmt(<structs.DropSubscriptionStmt*> data, offset_to_index)
    elif tag == structs.T_Integer:
        return create_Integer(<structs.Integer*> data, offset_to_index)
    elif tag == structs.T_Float:
        return create_Float(<structs.Float*> data, offset_to_index)
    elif tag == structs.T_Boolean:
        return create_Boolean(<structs.Boolean*> data, offset_to_index)
    elif tag == structs.T_String:
        return create_String(<structs.String*> data, offset_to_index)
    elif tag == structs.T_BitString:
        return create_BitString(<structs.BitString*> data, offset_to_index)
    raise ValueError("Unhandled tag: %s" % tag)
