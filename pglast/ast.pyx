# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from struct_defs.json @ 13-2.0.5-0-gdee15dd
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021 Lele Gaifax
#

#cython: language_level=3

from cpython.ref cimport Py_INCREF
from cpython.tuple cimport PyTuple_New, PyTuple_SET_ITEM

from decimal import Decimal

from pglast import ast, enums
from pglast cimport structs


cdef create_Query(structs.Query* data, offset_to_index):
    cdef object v_commandType = getattr(enums, 'CmdType')(data.commandType)
    cdef object v_querySource = getattr(enums, 'QuerySource')(data.querySource)
    cdef object v_queryId = data.queryId
    cdef object v_canSetTag = bool(data.canSetTag)
    cdef object v_utilityStmt
    if data.utilityStmt is not NULL:
        v_utilityStmt = create(data.utilityStmt, offset_to_index)
    else:
        v_utilityStmt = None
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
    cdef tuple v_cteList
    cdef int cteList_i
    if data.cteList is not NULL:
        v_cteList = PyTuple_New(data.cteList.length)
        for i in range(data.cteList.length):
            item = create(structs.list_nth(data.cteList, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_cteList, i, item)
    else:
        v_cteList = None
    cdef tuple v_rtable
    cdef int rtable_i
    if data.rtable is not NULL:
        v_rtable = PyTuple_New(data.rtable.length)
        for i in range(data.rtable.length):
            item = create(structs.list_nth(data.rtable, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_rtable, i, item)
    else:
        v_rtable = None
    cdef object v_jointree
    if data.jointree is not NULL:
        v_jointree = create(data.jointree, offset_to_index)
    else:
        v_jointree = None
    cdef tuple v_targetList
    cdef int targetList_i
    if data.targetList is not NULL:
        v_targetList = PyTuple_New(data.targetList.length)
        for i in range(data.targetList.length):
            item = create(structs.list_nth(data.targetList, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_targetList, i, item)
    else:
        v_targetList = None
    cdef object v_override = getattr(enums, 'OverridingKind')(data.override)
    cdef object v_onConflict
    if data.onConflict is not NULL:
        v_onConflict = create(data.onConflict, offset_to_index)
    else:
        v_onConflict = None
    cdef tuple v_returningList
    cdef int returningList_i
    if data.returningList is not NULL:
        v_returningList = PyTuple_New(data.returningList.length)
        for i in range(data.returningList.length):
            item = create(structs.list_nth(data.returningList, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_returningList, i, item)
    else:
        v_returningList = None
    cdef tuple v_groupClause
    cdef int groupClause_i
    if data.groupClause is not NULL:
        v_groupClause = PyTuple_New(data.groupClause.length)
        for i in range(data.groupClause.length):
            item = create(structs.list_nth(data.groupClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_groupClause, i, item)
    else:
        v_groupClause = None
    cdef tuple v_groupingSets
    cdef int groupingSets_i
    if data.groupingSets is not NULL:
        v_groupingSets = PyTuple_New(data.groupingSets.length)
        for i in range(data.groupingSets.length):
            item = create(structs.list_nth(data.groupingSets, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_groupingSets, i, item)
    else:
        v_groupingSets = None
    cdef object v_havingQual
    if data.havingQual is not NULL:
        v_havingQual = create(data.havingQual, offset_to_index)
    else:
        v_havingQual = None
    cdef tuple v_windowClause
    cdef int windowClause_i
    if data.windowClause is not NULL:
        v_windowClause = PyTuple_New(data.windowClause.length)
        for i in range(data.windowClause.length):
            item = create(structs.list_nth(data.windowClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_windowClause, i, item)
    else:
        v_windowClause = None
    cdef tuple v_distinctClause
    cdef int distinctClause_i
    if data.distinctClause is not NULL:
        v_distinctClause = PyTuple_New(data.distinctClause.length)
        for i in range(data.distinctClause.length):
            item = create(structs.list_nth(data.distinctClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_distinctClause, i, item)
    else:
        v_distinctClause = None
    cdef tuple v_sortClause
    cdef int sortClause_i
    if data.sortClause is not NULL:
        v_sortClause = PyTuple_New(data.sortClause.length)
        for i in range(data.sortClause.length):
            item = create(structs.list_nth(data.sortClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_sortClause, i, item)
    else:
        v_sortClause = None
    cdef object v_limitOffset
    if data.limitOffset is not NULL:
        v_limitOffset = create(data.limitOffset, offset_to_index)
    else:
        v_limitOffset = None
    cdef object v_limitCount
    if data.limitCount is not NULL:
        v_limitCount = create(data.limitCount, offset_to_index)
    else:
        v_limitCount = None
    cdef object v_limitOption = getattr(enums, 'LimitOption')(data.limitOption)
    cdef tuple v_rowMarks
    cdef int rowMarks_i
    if data.rowMarks is not NULL:
        v_rowMarks = PyTuple_New(data.rowMarks.length)
        for i in range(data.rowMarks.length):
            item = create(structs.list_nth(data.rowMarks, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_rowMarks, i, item)
    else:
        v_rowMarks = None
    cdef object v_setOperations
    if data.setOperations is not NULL:
        v_setOperations = create(data.setOperations, offset_to_index)
    else:
        v_setOperations = None
    cdef tuple v_constraintDeps
    cdef int constraintDeps_i
    if data.constraintDeps is not NULL:
        v_constraintDeps = PyTuple_New(data.constraintDeps.length)
        for i in range(data.constraintDeps.length):
            item = create(structs.list_nth(data.constraintDeps, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_constraintDeps, i, item)
    else:
        v_constraintDeps = None
    cdef tuple v_withCheckOptions
    cdef int withCheckOptions_i
    if data.withCheckOptions is not NULL:
        v_withCheckOptions = PyTuple_New(data.withCheckOptions.length)
        for i in range(data.withCheckOptions.length):
            item = create(structs.list_nth(data.withCheckOptions, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_withCheckOptions, i, item)
    else:
        v_withCheckOptions = None
    cdef object v_stmt_location = offset_to_index(data.stmt_location)
    cdef object v_stmt_len = offset_to_index(data.stmt_location + data.stmt_len) - offset_to_index(data.stmt_location)
    return ast.Query(v_commandType, v_querySource, v_queryId, v_canSetTag, v_utilityStmt, v_resultRelation, v_hasAggs, v_hasWindowFuncs, v_hasTargetSRFs, v_hasSubLinks, v_hasDistinctOn, v_hasRecursive, v_hasModifyingCTE, v_hasForUpdate, v_hasRowSecurity, v_cteList, v_rtable, v_jointree, v_targetList, v_override, v_onConflict, v_returningList, v_groupClause, v_groupingSets, v_havingQual, v_windowClause, v_distinctClause, v_sortClause, v_limitOffset, v_limitCount, v_limitOption, v_rowMarks, v_setOperations, v_constraintDeps, v_withCheckOptions, v_stmt_location, v_stmt_len)


cdef create_TypeName(structs.TypeName* data, offset_to_index):
    cdef tuple v_names
    cdef int names_i
    if data.names is not NULL:
        v_names = PyTuple_New(data.names.length)
        for i in range(data.names.length):
            item = create(structs.list_nth(data.names, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_names, i, item)
    else:
        v_names = None
    cdef object v_setof = bool(data.setof)
    cdef object v_pct_type = bool(data.pct_type)
    cdef tuple v_typmods
    cdef int typmods_i
    if data.typmods is not NULL:
        v_typmods = PyTuple_New(data.typmods.length)
        for i in range(data.typmods.length):
            item = create(structs.list_nth(data.typmods, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_typmods, i, item)
    else:
        v_typmods = None
    cdef object v_typemod = data.typemod
    cdef tuple v_arrayBounds
    cdef int arrayBounds_i
    if data.arrayBounds is not NULL:
        v_arrayBounds = PyTuple_New(data.arrayBounds.length)
        for i in range(data.arrayBounds.length):
            item = create(structs.list_nth(data.arrayBounds, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_arrayBounds, i, item)
    else:
        v_arrayBounds = None
    cdef object v_location = offset_to_index(data.location)
    return ast.TypeName(v_names, v_setof, v_pct_type, v_typmods, v_typemod, v_arrayBounds, v_location)


cdef create_ColumnRef(structs.ColumnRef* data, offset_to_index):
    cdef tuple v_fields
    cdef int fields_i
    if data.fields is not NULL:
        v_fields = PyTuple_New(data.fields.length)
        for i in range(data.fields.length):
            item = create(structs.list_nth(data.fields, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_fields, i, item)
    else:
        v_fields = None
    cdef object v_location = offset_to_index(data.location)
    return ast.ColumnRef(v_fields, v_location)


cdef create_ParamRef(structs.ParamRef* data, offset_to_index):
    cdef object v_number = data.number
    cdef object v_location = offset_to_index(data.location)
    return ast.ParamRef(v_number, v_location)


cdef create_A_Expr(structs.A_Expr* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'A_Expr_Kind')(data.kind)
    cdef tuple v_name
    cdef int name_i
    if data.name is not NULL:
        v_name = PyTuple_New(data.name.length)
        for i in range(data.name.length):
            item = create(structs.list_nth(data.name, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_name, i, item)
    else:
        v_name = None
    cdef object v_lexpr
    if data.lexpr is not NULL:
        v_lexpr = create(data.lexpr, offset_to_index)
    else:
        v_lexpr = None
    cdef object v_rexpr
    if data.rexpr is not NULL:
        v_rexpr = create(data.rexpr, offset_to_index)
    else:
        v_rexpr = None
    cdef object v_location = offset_to_index(data.location)
    return ast.A_Expr(v_kind, v_name, v_lexpr, v_rexpr, v_location)


cdef create_A_Const(structs.A_Const* data, offset_to_index):
    cdef object v_val
    if data.val.type == structs.T_Null:
        v_val = ast.Null(None)
    elif data.val.type == structs.T_Integer:
        v_val = ast.Integer(data.val.val.ival)
    elif data.val.type == structs.T_Float:
        v_val = ast.Float(Decimal(data.val.val.str.decode("utf-8")))
    elif data.val.type == structs.T_BitString:
        v_val = ast.BitString(data.val.val.str.decode("utf-8"))
    else:
        v_val = ast.String(data.val.val.str.decode("utf-8"))
    cdef object v_location = offset_to_index(data.location)
    return ast.A_Const(v_val, v_location)


cdef create_TypeCast(structs.TypeCast* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_typeName
    if data.typeName is not NULL:
        v_typeName = create(data.typeName, offset_to_index)
    else:
        v_typeName = None
    cdef object v_location = offset_to_index(data.location)
    return ast.TypeCast(v_arg, v_typeName, v_location)


cdef create_CollateClause(structs.CollateClause* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef tuple v_collname
    cdef int collname_i
    if data.collname is not NULL:
        v_collname = PyTuple_New(data.collname.length)
        for i in range(data.collname.length):
            item = create(structs.list_nth(data.collname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_collname, i, item)
    else:
        v_collname = None
    cdef object v_location = offset_to_index(data.location)
    return ast.CollateClause(v_arg, v_collname, v_location)


cdef create_RoleSpec(structs.RoleSpec* data, offset_to_index):
    cdef object v_roletype = getattr(enums, 'RoleSpecType')(data.roletype)
    cdef object v_rolename
    if data.rolename is not NULL:
        v_rolename = data.rolename.decode("utf-8")
    else:
        v_rolename = None
    cdef object v_location = offset_to_index(data.location)
    return ast.RoleSpec(v_roletype, v_rolename, v_location)


cdef create_FuncCall(structs.FuncCall* data, offset_to_index):
    cdef tuple v_funcname
    cdef int funcname_i
    if data.funcname is not NULL:
        v_funcname = PyTuple_New(data.funcname.length)
        for i in range(data.funcname.length):
            item = create(structs.list_nth(data.funcname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_funcname, i, item)
    else:
        v_funcname = None
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef tuple v_agg_order
    cdef int agg_order_i
    if data.agg_order is not NULL:
        v_agg_order = PyTuple_New(data.agg_order.length)
        for i in range(data.agg_order.length):
            item = create(structs.list_nth(data.agg_order, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_agg_order, i, item)
    else:
        v_agg_order = None
    cdef object v_agg_filter
    if data.agg_filter is not NULL:
        v_agg_filter = create(data.agg_filter, offset_to_index)
    else:
        v_agg_filter = None
    cdef object v_agg_within_group = bool(data.agg_within_group)
    cdef object v_agg_star = bool(data.agg_star)
    cdef object v_agg_distinct = bool(data.agg_distinct)
    cdef object v_func_variadic = bool(data.func_variadic)
    cdef object v_over
    if data.over is not NULL:
        v_over = create(data.over, offset_to_index)
    else:
        v_over = None
    cdef object v_location = offset_to_index(data.location)
    return ast.FuncCall(v_funcname, v_args, v_agg_order, v_agg_filter, v_agg_within_group, v_agg_star, v_agg_distinct, v_func_variadic, v_over, v_location)


cdef create_A_Star(structs.A_Star* data, offset_to_index):
    return ast.A_Star()


cdef create_A_Indices(structs.A_Indices* data, offset_to_index):
    cdef object v_is_slice = bool(data.is_slice)
    cdef object v_lidx
    if data.lidx is not NULL:
        v_lidx = create(data.lidx, offset_to_index)
    else:
        v_lidx = None
    cdef object v_uidx
    if data.uidx is not NULL:
        v_uidx = create(data.uidx, offset_to_index)
    else:
        v_uidx = None
    return ast.A_Indices(v_is_slice, v_lidx, v_uidx)


cdef create_A_Indirection(structs.A_Indirection* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef tuple v_indirection
    cdef int indirection_i
    if data.indirection is not NULL:
        v_indirection = PyTuple_New(data.indirection.length)
        for i in range(data.indirection.length):
            item = create(structs.list_nth(data.indirection, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_indirection, i, item)
    else:
        v_indirection = None
    return ast.A_Indirection(v_arg, v_indirection)


cdef create_A_ArrayExpr(structs.A_ArrayExpr* data, offset_to_index):
    cdef tuple v_elements
    cdef int elements_i
    if data.elements is not NULL:
        v_elements = PyTuple_New(data.elements.length)
        for i in range(data.elements.length):
            item = create(structs.list_nth(data.elements, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_elements, i, item)
    else:
        v_elements = None
    cdef object v_location = offset_to_index(data.location)
    return ast.A_ArrayExpr(v_elements, v_location)


cdef create_ResTarget(structs.ResTarget* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef tuple v_indirection
    cdef int indirection_i
    if data.indirection is not NULL:
        v_indirection = PyTuple_New(data.indirection.length)
        for i in range(data.indirection.length):
            item = create(structs.list_nth(data.indirection, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_indirection, i, item)
    else:
        v_indirection = None
    cdef object v_val
    if data.val is not NULL:
        v_val = create(data.val, offset_to_index)
    else:
        v_val = None
    cdef object v_location = offset_to_index(data.location)
    return ast.ResTarget(v_name, v_indirection, v_val, v_location)


cdef create_MultiAssignRef(structs.MultiAssignRef* data, offset_to_index):
    cdef object v_source
    if data.source is not NULL:
        v_source = create(data.source, offset_to_index)
    else:
        v_source = None
    cdef object v_colno = data.colno
    cdef object v_ncolumns = data.ncolumns
    return ast.MultiAssignRef(v_source, v_colno, v_ncolumns)


cdef create_SortBy(structs.SortBy* data, offset_to_index):
    cdef object v_node
    if data.node is not NULL:
        v_node = create(data.node, offset_to_index)
    else:
        v_node = None
    cdef object v_sortby_dir = getattr(enums, 'SortByDir')(data.sortby_dir)
    cdef object v_sortby_nulls = getattr(enums, 'SortByNulls')(data.sortby_nulls)
    cdef tuple v_useOp
    cdef int useOp_i
    if data.useOp is not NULL:
        v_useOp = PyTuple_New(data.useOp.length)
        for i in range(data.useOp.length):
            item = create(structs.list_nth(data.useOp, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_useOp, i, item)
    else:
        v_useOp = None
    cdef object v_location = offset_to_index(data.location)
    return ast.SortBy(v_node, v_sortby_dir, v_sortby_nulls, v_useOp, v_location)


cdef create_WindowDef(structs.WindowDef* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_refname
    if data.refname is not NULL:
        v_refname = data.refname.decode("utf-8")
    else:
        v_refname = None
    cdef tuple v_partitionClause
    cdef int partitionClause_i
    if data.partitionClause is not NULL:
        v_partitionClause = PyTuple_New(data.partitionClause.length)
        for i in range(data.partitionClause.length):
            item = create(structs.list_nth(data.partitionClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_partitionClause, i, item)
    else:
        v_partitionClause = None
    cdef tuple v_orderClause
    cdef int orderClause_i
    if data.orderClause is not NULL:
        v_orderClause = PyTuple_New(data.orderClause.length)
        for i in range(data.orderClause.length):
            item = create(structs.list_nth(data.orderClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_orderClause, i, item)
    else:
        v_orderClause = None
    cdef object v_frameOptions = data.frameOptions
    cdef object v_startOffset
    if data.startOffset is not NULL:
        v_startOffset = create(data.startOffset, offset_to_index)
    else:
        v_startOffset = None
    cdef object v_endOffset
    if data.endOffset is not NULL:
        v_endOffset = create(data.endOffset, offset_to_index)
    else:
        v_endOffset = None
    cdef object v_location = offset_to_index(data.location)
    return ast.WindowDef(v_name, v_refname, v_partitionClause, v_orderClause, v_frameOptions, v_startOffset, v_endOffset, v_location)


cdef create_RangeSubselect(structs.RangeSubselect* data, offset_to_index):
    cdef object v_lateral = bool(data.lateral)
    cdef object v_subquery
    if data.subquery is not NULL:
        v_subquery = create(data.subquery, offset_to_index)
    else:
        v_subquery = None
    cdef object v_alias
    if data.alias is not NULL:
        v_alias = create(data.alias, offset_to_index)
    else:
        v_alias = None
    return ast.RangeSubselect(v_lateral, v_subquery, v_alias)


cdef create_RangeFunction(structs.RangeFunction* data, offset_to_index):
    cdef object v_lateral = bool(data.lateral)
    cdef object v_ordinality = bool(data.ordinality)
    cdef object v_is_rowsfrom = bool(data.is_rowsfrom)
    cdef tuple v_functions
    cdef int functions_i
    if data.functions is not NULL:
        v_functions = PyTuple_New(data.functions.length)
        for i in range(data.functions.length):
            item = create(structs.list_nth(data.functions, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_functions, i, item)
    else:
        v_functions = None
    cdef object v_alias
    if data.alias is not NULL:
        v_alias = create(data.alias, offset_to_index)
    else:
        v_alias = None
    cdef tuple v_coldeflist
    cdef int coldeflist_i
    if data.coldeflist is not NULL:
        v_coldeflist = PyTuple_New(data.coldeflist.length)
        for i in range(data.coldeflist.length):
            item = create(structs.list_nth(data.coldeflist, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_coldeflist, i, item)
    else:
        v_coldeflist = None
    return ast.RangeFunction(v_lateral, v_ordinality, v_is_rowsfrom, v_functions, v_alias, v_coldeflist)


cdef create_RangeTableFunc(structs.RangeTableFunc* data, offset_to_index):
    cdef object v_lateral = bool(data.lateral)
    cdef object v_docexpr
    if data.docexpr is not NULL:
        v_docexpr = create(data.docexpr, offset_to_index)
    else:
        v_docexpr = None
    cdef object v_rowexpr
    if data.rowexpr is not NULL:
        v_rowexpr = create(data.rowexpr, offset_to_index)
    else:
        v_rowexpr = None
    cdef tuple v_namespaces
    cdef int namespaces_i
    if data.namespaces is not NULL:
        v_namespaces = PyTuple_New(data.namespaces.length)
        for i in range(data.namespaces.length):
            item = create(structs.list_nth(data.namespaces, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_namespaces, i, item)
    else:
        v_namespaces = None
    cdef tuple v_columns
    cdef int columns_i
    if data.columns is not NULL:
        v_columns = PyTuple_New(data.columns.length)
        for i in range(data.columns.length):
            item = create(structs.list_nth(data.columns, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_columns, i, item)
    else:
        v_columns = None
    cdef object v_alias
    if data.alias is not NULL:
        v_alias = create(data.alias, offset_to_index)
    else:
        v_alias = None
    cdef object v_location = offset_to_index(data.location)
    return ast.RangeTableFunc(v_lateral, v_docexpr, v_rowexpr, v_namespaces, v_columns, v_alias, v_location)


cdef create_RangeTableFuncCol(structs.RangeTableFuncCol* data, offset_to_index):
    cdef object v_colname
    if data.colname is not NULL:
        v_colname = data.colname.decode("utf-8")
    else:
        v_colname = None
    cdef object v_typeName
    if data.typeName is not NULL:
        v_typeName = create(data.typeName, offset_to_index)
    else:
        v_typeName = None
    cdef object v_for_ordinality = bool(data.for_ordinality)
    cdef object v_is_not_null = bool(data.is_not_null)
    cdef object v_colexpr
    if data.colexpr is not NULL:
        v_colexpr = create(data.colexpr, offset_to_index)
    else:
        v_colexpr = None
    cdef object v_coldefexpr
    if data.coldefexpr is not NULL:
        v_coldefexpr = create(data.coldefexpr, offset_to_index)
    else:
        v_coldefexpr = None
    cdef object v_location = offset_to_index(data.location)
    return ast.RangeTableFuncCol(v_colname, v_typeName, v_for_ordinality, v_is_not_null, v_colexpr, v_coldefexpr, v_location)


cdef create_RangeTableSample(structs.RangeTableSample* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef tuple v_method
    cdef int method_i
    if data.method is not NULL:
        v_method = PyTuple_New(data.method.length)
        for i in range(data.method.length):
            item = create(structs.list_nth(data.method, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_method, i, item)
    else:
        v_method = None
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_repeatable
    if data.repeatable is not NULL:
        v_repeatable = create(data.repeatable, offset_to_index)
    else:
        v_repeatable = None
    cdef object v_location = offset_to_index(data.location)
    return ast.RangeTableSample(v_relation, v_method, v_args, v_repeatable, v_location)


cdef create_ColumnDef(structs.ColumnDef* data, offset_to_index):
    cdef object v_colname
    if data.colname is not NULL:
        v_colname = data.colname.decode("utf-8")
    else:
        v_colname = None
    cdef object v_typeName
    if data.typeName is not NULL:
        v_typeName = create(data.typeName, offset_to_index)
    else:
        v_typeName = None
    cdef object v_inhcount = data.inhcount
    cdef object v_is_local = bool(data.is_local)
    cdef object v_is_not_null = bool(data.is_not_null)
    cdef object v_is_from_type = bool(data.is_from_type)
    cdef object v_storage = chr(data.storage)
    cdef object v_raw_default
    if data.raw_default is not NULL:
        v_raw_default = create(data.raw_default, offset_to_index)
    else:
        v_raw_default = None
    cdef object v_cooked_default
    if data.cooked_default is not NULL:
        v_cooked_default = create(data.cooked_default, offset_to_index)
    else:
        v_cooked_default = None
    cdef object v_identity = chr(data.identity)
    cdef object v_identitySequence
    if data.identitySequence is not NULL:
        v_identitySequence = create(data.identitySequence, offset_to_index)
    else:
        v_identitySequence = None
    cdef object v_generated = chr(data.generated)
    cdef object v_collClause
    if data.collClause is not NULL:
        v_collClause = create(data.collClause, offset_to_index)
    else:
        v_collClause = None
    cdef tuple v_constraints
    cdef int constraints_i
    if data.constraints is not NULL:
        v_constraints = PyTuple_New(data.constraints.length)
        for i in range(data.constraints.length):
            item = create(structs.list_nth(data.constraints, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_constraints, i, item)
    else:
        v_constraints = None
    cdef tuple v_fdwoptions
    cdef int fdwoptions_i
    if data.fdwoptions is not NULL:
        v_fdwoptions = PyTuple_New(data.fdwoptions.length)
        for i in range(data.fdwoptions.length):
            item = create(structs.list_nth(data.fdwoptions, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_fdwoptions, i, item)
    else:
        v_fdwoptions = None
    cdef object v_location = offset_to_index(data.location)
    return ast.ColumnDef(v_colname, v_typeName, v_inhcount, v_is_local, v_is_not_null, v_is_from_type, v_storage, v_raw_default, v_cooked_default, v_identity, v_identitySequence, v_generated, v_collClause, v_constraints, v_fdwoptions, v_location)


cdef create_TableLikeClause(structs.TableLikeClause* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_options = data.options
    return ast.TableLikeClause(v_relation, v_options)


cdef create_IndexElem(structs.IndexElem* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_expr
    if data.expr is not NULL:
        v_expr = create(data.expr, offset_to_index)
    else:
        v_expr = None
    cdef object v_indexcolname
    if data.indexcolname is not NULL:
        v_indexcolname = data.indexcolname.decode("utf-8")
    else:
        v_indexcolname = None
    cdef tuple v_collation
    cdef int collation_i
    if data.collation is not NULL:
        v_collation = PyTuple_New(data.collation.length)
        for i in range(data.collation.length):
            item = create(structs.list_nth(data.collation, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_collation, i, item)
    else:
        v_collation = None
    cdef tuple v_opclass
    cdef int opclass_i
    if data.opclass is not NULL:
        v_opclass = PyTuple_New(data.opclass.length)
        for i in range(data.opclass.length):
            item = create(structs.list_nth(data.opclass, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_opclass, i, item)
    else:
        v_opclass = None
    cdef tuple v_opclassopts
    cdef int opclassopts_i
    if data.opclassopts is not NULL:
        v_opclassopts = PyTuple_New(data.opclassopts.length)
        for i in range(data.opclassopts.length):
            item = create(structs.list_nth(data.opclassopts, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_opclassopts, i, item)
    else:
        v_opclassopts = None
    cdef object v_ordering = getattr(enums, 'SortByDir')(data.ordering)
    cdef object v_nulls_ordering = getattr(enums, 'SortByNulls')(data.nulls_ordering)
    return ast.IndexElem(v_name, v_expr, v_indexcolname, v_collation, v_opclass, v_opclassopts, v_ordering, v_nulls_ordering)


cdef create_DefElem(structs.DefElem* data, offset_to_index):
    cdef object v_defnamespace
    if data.defnamespace is not NULL:
        v_defnamespace = data.defnamespace.decode("utf-8")
    else:
        v_defnamespace = None
    cdef object v_defname
    if data.defname is not NULL:
        v_defname = data.defname.decode("utf-8")
    else:
        v_defname = None
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_defaction = getattr(enums, 'DefElemAction')(data.defaction)
    cdef object v_location = offset_to_index(data.location)
    return ast.DefElem(v_defnamespace, v_defname, v_arg, v_defaction, v_location)


cdef create_LockingClause(structs.LockingClause* data, offset_to_index):
    cdef tuple v_lockedRels
    cdef int lockedRels_i
    if data.lockedRels is not NULL:
        v_lockedRels = PyTuple_New(data.lockedRels.length)
        for i in range(data.lockedRels.length):
            item = create(structs.list_nth(data.lockedRels, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_lockedRels, i, item)
    else:
        v_lockedRels = None
    cdef object v_strength = getattr(enums, 'LockClauseStrength')(data.strength)
    cdef object v_waitPolicy = getattr(enums, 'LockWaitPolicy')(data.waitPolicy)
    return ast.LockingClause(v_lockedRels, v_strength, v_waitPolicy)


cdef create_XmlSerialize(structs.XmlSerialize* data, offset_to_index):
    cdef object v_xmloption = getattr(enums, 'XmlOptionType')(data.xmloption)
    cdef object v_expr
    if data.expr is not NULL:
        v_expr = create(data.expr, offset_to_index)
    else:
        v_expr = None
    cdef object v_typeName
    if data.typeName is not NULL:
        v_typeName = create(data.typeName, offset_to_index)
    else:
        v_typeName = None
    cdef object v_location = offset_to_index(data.location)
    return ast.XmlSerialize(v_xmloption, v_expr, v_typeName, v_location)


cdef create_PartitionElem(structs.PartitionElem* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_expr
    if data.expr is not NULL:
        v_expr = create(data.expr, offset_to_index)
    else:
        v_expr = None
    cdef tuple v_collation
    cdef int collation_i
    if data.collation is not NULL:
        v_collation = PyTuple_New(data.collation.length)
        for i in range(data.collation.length):
            item = create(structs.list_nth(data.collation, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_collation, i, item)
    else:
        v_collation = None
    cdef tuple v_opclass
    cdef int opclass_i
    if data.opclass is not NULL:
        v_opclass = PyTuple_New(data.opclass.length)
        for i in range(data.opclass.length):
            item = create(structs.list_nth(data.opclass, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_opclass, i, item)
    else:
        v_opclass = None
    cdef object v_location = offset_to_index(data.location)
    return ast.PartitionElem(v_name, v_expr, v_collation, v_opclass, v_location)


cdef create_PartitionSpec(structs.PartitionSpec* data, offset_to_index):
    cdef object v_strategy
    if data.strategy is not NULL:
        v_strategy = data.strategy.decode("utf-8")
    else:
        v_strategy = None
    cdef tuple v_partParams
    cdef int partParams_i
    if data.partParams is not NULL:
        v_partParams = PyTuple_New(data.partParams.length)
        for i in range(data.partParams.length):
            item = create(structs.list_nth(data.partParams, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_partParams, i, item)
    else:
        v_partParams = None
    cdef object v_location = offset_to_index(data.location)
    return ast.PartitionSpec(v_strategy, v_partParams, v_location)


cdef create_PartitionBoundSpec(structs.PartitionBoundSpec* data, offset_to_index):
    cdef object v_strategy = chr(data.strategy)
    cdef object v_is_default = bool(data.is_default)
    cdef object v_modulus = data.modulus
    cdef object v_remainder = data.remainder
    cdef tuple v_listdatums
    cdef int listdatums_i
    if data.listdatums is not NULL:
        v_listdatums = PyTuple_New(data.listdatums.length)
        for i in range(data.listdatums.length):
            item = create(structs.list_nth(data.listdatums, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_listdatums, i, item)
    else:
        v_listdatums = None
    cdef tuple v_lowerdatums
    cdef int lowerdatums_i
    if data.lowerdatums is not NULL:
        v_lowerdatums = PyTuple_New(data.lowerdatums.length)
        for i in range(data.lowerdatums.length):
            item = create(structs.list_nth(data.lowerdatums, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_lowerdatums, i, item)
    else:
        v_lowerdatums = None
    cdef tuple v_upperdatums
    cdef int upperdatums_i
    if data.upperdatums is not NULL:
        v_upperdatums = PyTuple_New(data.upperdatums.length)
        for i in range(data.upperdatums.length):
            item = create(structs.list_nth(data.upperdatums, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_upperdatums, i, item)
    else:
        v_upperdatums = None
    cdef object v_location = offset_to_index(data.location)
    return ast.PartitionBoundSpec(v_strategy, v_is_default, v_modulus, v_remainder, v_listdatums, v_lowerdatums, v_upperdatums, v_location)


cdef create_PartitionRangeDatum(structs.PartitionRangeDatum* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'PartitionRangeDatumKind')(data.kind)
    cdef object v_value
    if data.value is not NULL:
        v_value = create(data.value, offset_to_index)
    else:
        v_value = None
    cdef object v_location = offset_to_index(data.location)
    return ast.PartitionRangeDatum(v_kind, v_value, v_location)


cdef create_PartitionCmd(structs.PartitionCmd* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = create(data.name, offset_to_index)
    else:
        v_name = None
    cdef object v_bound
    if data.bound is not NULL:
        v_bound = create(data.bound, offset_to_index)
    else:
        v_bound = None
    return ast.PartitionCmd(v_name, v_bound)


cdef create_RangeTblEntry(structs.RangeTblEntry* data, offset_to_index):
    cdef object v_rtekind = getattr(enums, 'RTEKind')(data.rtekind)
    cdef object v_relkind = chr(data.relkind)
    cdef object v_rellockmode = data.rellockmode
    cdef object v_tablesample
    if data.tablesample is not NULL:
        v_tablesample = create(data.tablesample, offset_to_index)
    else:
        v_tablesample = None
    cdef object v_subquery
    if data.subquery is not NULL:
        v_subquery = create(data.subquery, offset_to_index)
    else:
        v_subquery = None
    cdef object v_security_barrier = bool(data.security_barrier)
    cdef object v_jointype = getattr(enums, 'JoinType')(data.jointype)
    cdef object v_joinmergedcols = data.joinmergedcols
    cdef tuple v_joinaliasvars
    cdef int joinaliasvars_i
    if data.joinaliasvars is not NULL:
        v_joinaliasvars = PyTuple_New(data.joinaliasvars.length)
        for i in range(data.joinaliasvars.length):
            item = create(structs.list_nth(data.joinaliasvars, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_joinaliasvars, i, item)
    else:
        v_joinaliasvars = None
    cdef tuple v_joinleftcols
    cdef int joinleftcols_i
    if data.joinleftcols is not NULL:
        v_joinleftcols = PyTuple_New(data.joinleftcols.length)
        for i in range(data.joinleftcols.length):
            item = create(structs.list_nth(data.joinleftcols, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_joinleftcols, i, item)
    else:
        v_joinleftcols = None
    cdef tuple v_joinrightcols
    cdef int joinrightcols_i
    if data.joinrightcols is not NULL:
        v_joinrightcols = PyTuple_New(data.joinrightcols.length)
        for i in range(data.joinrightcols.length):
            item = create(structs.list_nth(data.joinrightcols, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_joinrightcols, i, item)
    else:
        v_joinrightcols = None
    cdef tuple v_functions
    cdef int functions_i
    if data.functions is not NULL:
        v_functions = PyTuple_New(data.functions.length)
        for i in range(data.functions.length):
            item = create(structs.list_nth(data.functions, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_functions, i, item)
    else:
        v_functions = None
    cdef object v_funcordinality = bool(data.funcordinality)
    cdef object v_tablefunc
    if data.tablefunc is not NULL:
        v_tablefunc = create(data.tablefunc, offset_to_index)
    else:
        v_tablefunc = None
    cdef tuple v_values_lists
    cdef int values_lists_i
    if data.values_lists is not NULL:
        v_values_lists = PyTuple_New(data.values_lists.length)
        for i in range(data.values_lists.length):
            item = create(structs.list_nth(data.values_lists, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_values_lists, i, item)
    else:
        v_values_lists = None
    cdef object v_ctename
    if data.ctename is not NULL:
        v_ctename = data.ctename.decode("utf-8")
    else:
        v_ctename = None
    cdef object v_ctelevelsup = data.ctelevelsup
    cdef object v_self_reference = bool(data.self_reference)
    cdef tuple v_coltypes
    cdef int coltypes_i
    if data.coltypes is not NULL:
        v_coltypes = PyTuple_New(data.coltypes.length)
        for i in range(data.coltypes.length):
            item = create(structs.list_nth(data.coltypes, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_coltypes, i, item)
    else:
        v_coltypes = None
    cdef tuple v_coltypmods
    cdef int coltypmods_i
    if data.coltypmods is not NULL:
        v_coltypmods = PyTuple_New(data.coltypmods.length)
        for i in range(data.coltypmods.length):
            item = create(structs.list_nth(data.coltypmods, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_coltypmods, i, item)
    else:
        v_coltypmods = None
    cdef tuple v_colcollations
    cdef int colcollations_i
    if data.colcollations is not NULL:
        v_colcollations = PyTuple_New(data.colcollations.length)
        for i in range(data.colcollations.length):
            item = create(structs.list_nth(data.colcollations, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colcollations, i, item)
    else:
        v_colcollations = None
    cdef object v_enrname
    if data.enrname is not NULL:
        v_enrname = data.enrname.decode("utf-8")
    else:
        v_enrname = None
    cdef object v_enrtuples = data.enrtuples
    cdef object v_alias
    if data.alias is not NULL:
        v_alias = create(data.alias, offset_to_index)
    else:
        v_alias = None
    cdef object v_eref
    if data.eref is not NULL:
        v_eref = create(data.eref, offset_to_index)
    else:
        v_eref = None
    cdef object v_lateral = bool(data.lateral)
    cdef object v_inh = bool(data.inh)
    cdef object v_inFromCl = bool(data.inFromCl)
    cdef object v_requiredPerms = data.requiredPerms
    cdef set v_selectedCols
    cdef int selectedCols_member
    if data.selectedCols is not NULL:
        v_selectedCols = set()
        selectedCols_member = structs.bms_next_member(data.selectedCols, -1)
        while selectedCols_member >= 0:
            v_selectedCols.add(selectedCols_member)
            selectedCols_member = structs.bms_next_member(data.selectedCols, selectedCols_member)
    else:
        v_selectedCols = None
    cdef set v_insertedCols
    cdef int insertedCols_member
    if data.insertedCols is not NULL:
        v_insertedCols = set()
        insertedCols_member = structs.bms_next_member(data.insertedCols, -1)
        while insertedCols_member >= 0:
            v_insertedCols.add(insertedCols_member)
            insertedCols_member = structs.bms_next_member(data.insertedCols, insertedCols_member)
    else:
        v_insertedCols = None
    cdef set v_updatedCols
    cdef int updatedCols_member
    if data.updatedCols is not NULL:
        v_updatedCols = set()
        updatedCols_member = structs.bms_next_member(data.updatedCols, -1)
        while updatedCols_member >= 0:
            v_updatedCols.add(updatedCols_member)
            updatedCols_member = structs.bms_next_member(data.updatedCols, updatedCols_member)
    else:
        v_updatedCols = None
    cdef set v_extraUpdatedCols
    cdef int extraUpdatedCols_member
    if data.extraUpdatedCols is not NULL:
        v_extraUpdatedCols = set()
        extraUpdatedCols_member = structs.bms_next_member(data.extraUpdatedCols, -1)
        while extraUpdatedCols_member >= 0:
            v_extraUpdatedCols.add(extraUpdatedCols_member)
            extraUpdatedCols_member = structs.bms_next_member(data.extraUpdatedCols, extraUpdatedCols_member)
    else:
        v_extraUpdatedCols = None
    cdef tuple v_securityQuals
    cdef int securityQuals_i
    if data.securityQuals is not NULL:
        v_securityQuals = PyTuple_New(data.securityQuals.length)
        for i in range(data.securityQuals.length):
            item = create(structs.list_nth(data.securityQuals, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_securityQuals, i, item)
    else:
        v_securityQuals = None
    return ast.RangeTblEntry(v_rtekind, v_relkind, v_rellockmode, v_tablesample, v_subquery, v_security_barrier, v_jointype, v_joinmergedcols, v_joinaliasvars, v_joinleftcols, v_joinrightcols, v_functions, v_funcordinality, v_tablefunc, v_values_lists, v_ctename, v_ctelevelsup, v_self_reference, v_coltypes, v_coltypmods, v_colcollations, v_enrname, v_enrtuples, v_alias, v_eref, v_lateral, v_inh, v_inFromCl, v_requiredPerms, v_selectedCols, v_insertedCols, v_updatedCols, v_extraUpdatedCols, v_securityQuals)


cdef create_RangeTblFunction(structs.RangeTblFunction* data, offset_to_index):
    cdef object v_funcexpr
    if data.funcexpr is not NULL:
        v_funcexpr = create(data.funcexpr, offset_to_index)
    else:
        v_funcexpr = None
    cdef object v_funccolcount = data.funccolcount
    cdef tuple v_funccolnames
    cdef int funccolnames_i
    if data.funccolnames is not NULL:
        v_funccolnames = PyTuple_New(data.funccolnames.length)
        for i in range(data.funccolnames.length):
            item = create(structs.list_nth(data.funccolnames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_funccolnames, i, item)
    else:
        v_funccolnames = None
    cdef tuple v_funccoltypes
    cdef int funccoltypes_i
    if data.funccoltypes is not NULL:
        v_funccoltypes = PyTuple_New(data.funccoltypes.length)
        for i in range(data.funccoltypes.length):
            item = create(structs.list_nth(data.funccoltypes, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_funccoltypes, i, item)
    else:
        v_funccoltypes = None
    cdef tuple v_funccoltypmods
    cdef int funccoltypmods_i
    if data.funccoltypmods is not NULL:
        v_funccoltypmods = PyTuple_New(data.funccoltypmods.length)
        for i in range(data.funccoltypmods.length):
            item = create(structs.list_nth(data.funccoltypmods, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_funccoltypmods, i, item)
    else:
        v_funccoltypmods = None
    cdef tuple v_funccolcollations
    cdef int funccolcollations_i
    if data.funccolcollations is not NULL:
        v_funccolcollations = PyTuple_New(data.funccolcollations.length)
        for i in range(data.funccolcollations.length):
            item = create(structs.list_nth(data.funccolcollations, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_funccolcollations, i, item)
    else:
        v_funccolcollations = None
    cdef set v_funcparams
    cdef int funcparams_member
    if data.funcparams is not NULL:
        v_funcparams = set()
        funcparams_member = structs.bms_next_member(data.funcparams, -1)
        while funcparams_member >= 0:
            v_funcparams.add(funcparams_member)
            funcparams_member = structs.bms_next_member(data.funcparams, funcparams_member)
    else:
        v_funcparams = None
    return ast.RangeTblFunction(v_funcexpr, v_funccolcount, v_funccolnames, v_funccoltypes, v_funccoltypmods, v_funccolcollations, v_funcparams)


cdef create_TableSampleClause(structs.TableSampleClause* data, offset_to_index):
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_repeatable
    if data.repeatable is not NULL:
        v_repeatable = create(data.repeatable, offset_to_index)
    else:
        v_repeatable = None
    return ast.TableSampleClause(v_args, v_repeatable)


cdef create_WithCheckOption(structs.WithCheckOption* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'WCOKind')(data.kind)
    cdef object v_relname
    if data.relname is not NULL:
        v_relname = data.relname.decode("utf-8")
    else:
        v_relname = None
    cdef object v_polname
    if data.polname is not NULL:
        v_polname = data.polname.decode("utf-8")
    else:
        v_polname = None
    cdef object v_qual
    if data.qual is not NULL:
        v_qual = create(data.qual, offset_to_index)
    else:
        v_qual = None
    cdef object v_cascaded = bool(data.cascaded)
    return ast.WithCheckOption(v_kind, v_relname, v_polname, v_qual, v_cascaded)


cdef create_SortGroupClause(structs.SortGroupClause* data, offset_to_index):
    cdef object v_tleSortGroupRef = data.tleSortGroupRef
    cdef object v_nulls_first = bool(data.nulls_first)
    cdef object v_hashable = bool(data.hashable)
    return ast.SortGroupClause(v_tleSortGroupRef, v_nulls_first, v_hashable)


cdef create_GroupingSet(structs.GroupingSet* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'GroupingSetKind')(data.kind)
    cdef tuple v_content
    cdef int content_i
    if data.content is not NULL:
        v_content = PyTuple_New(data.content.length)
        for i in range(data.content.length):
            item = create(structs.list_nth(data.content, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_content, i, item)
    else:
        v_content = None
    cdef object v_location = offset_to_index(data.location)
    return ast.GroupingSet(v_kind, v_content, v_location)


cdef create_WindowClause(structs.WindowClause* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_refname
    if data.refname is not NULL:
        v_refname = data.refname.decode("utf-8")
    else:
        v_refname = None
    cdef tuple v_partitionClause
    cdef int partitionClause_i
    if data.partitionClause is not NULL:
        v_partitionClause = PyTuple_New(data.partitionClause.length)
        for i in range(data.partitionClause.length):
            item = create(structs.list_nth(data.partitionClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_partitionClause, i, item)
    else:
        v_partitionClause = None
    cdef tuple v_orderClause
    cdef int orderClause_i
    if data.orderClause is not NULL:
        v_orderClause = PyTuple_New(data.orderClause.length)
        for i in range(data.orderClause.length):
            item = create(structs.list_nth(data.orderClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_orderClause, i, item)
    else:
        v_orderClause = None
    cdef object v_frameOptions = data.frameOptions
    cdef object v_startOffset
    if data.startOffset is not NULL:
        v_startOffset = create(data.startOffset, offset_to_index)
    else:
        v_startOffset = None
    cdef object v_endOffset
    if data.endOffset is not NULL:
        v_endOffset = create(data.endOffset, offset_to_index)
    else:
        v_endOffset = None
    cdef object v_inRangeAsc = bool(data.inRangeAsc)
    cdef object v_inRangeNullsFirst = bool(data.inRangeNullsFirst)
    cdef object v_winref = data.winref
    cdef object v_copiedOrder = bool(data.copiedOrder)
    return ast.WindowClause(v_name, v_refname, v_partitionClause, v_orderClause, v_frameOptions, v_startOffset, v_endOffset, v_inRangeAsc, v_inRangeNullsFirst, v_winref, v_copiedOrder)


cdef create_RowMarkClause(structs.RowMarkClause* data, offset_to_index):
    cdef object v_rti = data.rti
    cdef object v_strength = getattr(enums, 'LockClauseStrength')(data.strength)
    cdef object v_waitPolicy = getattr(enums, 'LockWaitPolicy')(data.waitPolicy)
    cdef object v_pushedDown = bool(data.pushedDown)
    return ast.RowMarkClause(v_rti, v_strength, v_waitPolicy, v_pushedDown)


cdef create_WithClause(structs.WithClause* data, offset_to_index):
    cdef tuple v_ctes
    cdef int ctes_i
    if data.ctes is not NULL:
        v_ctes = PyTuple_New(data.ctes.length)
        for i in range(data.ctes.length):
            item = create(structs.list_nth(data.ctes, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_ctes, i, item)
    else:
        v_ctes = None
    cdef object v_recursive = bool(data.recursive)
    cdef object v_location = offset_to_index(data.location)
    return ast.WithClause(v_ctes, v_recursive, v_location)


cdef create_InferClause(structs.InferClause* data, offset_to_index):
    cdef tuple v_indexElems
    cdef int indexElems_i
    if data.indexElems is not NULL:
        v_indexElems = PyTuple_New(data.indexElems.length)
        for i in range(data.indexElems.length):
            item = create(structs.list_nth(data.indexElems, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_indexElems, i, item)
    else:
        v_indexElems = None
    cdef object v_whereClause
    if data.whereClause is not NULL:
        v_whereClause = create(data.whereClause, offset_to_index)
    else:
        v_whereClause = None
    cdef object v_conname
    if data.conname is not NULL:
        v_conname = data.conname.decode("utf-8")
    else:
        v_conname = None
    cdef object v_location = offset_to_index(data.location)
    return ast.InferClause(v_indexElems, v_whereClause, v_conname, v_location)


cdef create_OnConflictClause(structs.OnConflictClause* data, offset_to_index):
    cdef object v_action = getattr(enums, 'OnConflictAction')(data.action)
    cdef object v_infer
    if data.infer is not NULL:
        v_infer = create(data.infer, offset_to_index)
    else:
        v_infer = None
    cdef tuple v_targetList
    cdef int targetList_i
    if data.targetList is not NULL:
        v_targetList = PyTuple_New(data.targetList.length)
        for i in range(data.targetList.length):
            item = create(structs.list_nth(data.targetList, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_targetList, i, item)
    else:
        v_targetList = None
    cdef object v_whereClause
    if data.whereClause is not NULL:
        v_whereClause = create(data.whereClause, offset_to_index)
    else:
        v_whereClause = None
    cdef object v_location = offset_to_index(data.location)
    return ast.OnConflictClause(v_action, v_infer, v_targetList, v_whereClause, v_location)


cdef create_CommonTableExpr(structs.CommonTableExpr* data, offset_to_index):
    cdef object v_ctename
    if data.ctename is not NULL:
        v_ctename = data.ctename.decode("utf-8")
    else:
        v_ctename = None
    cdef tuple v_aliascolnames
    cdef int aliascolnames_i
    if data.aliascolnames is not NULL:
        v_aliascolnames = PyTuple_New(data.aliascolnames.length)
        for i in range(data.aliascolnames.length):
            item = create(structs.list_nth(data.aliascolnames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_aliascolnames, i, item)
    else:
        v_aliascolnames = None
    cdef object v_ctematerialized = getattr(enums, 'CTEMaterialize')(data.ctematerialized)
    cdef object v_ctequery
    if data.ctequery is not NULL:
        v_ctequery = create(data.ctequery, offset_to_index)
    else:
        v_ctequery = None
    cdef object v_location = offset_to_index(data.location)
    cdef object v_cterecursive = bool(data.cterecursive)
    cdef object v_cterefcount = data.cterefcount
    cdef tuple v_ctecolnames
    cdef int ctecolnames_i
    if data.ctecolnames is not NULL:
        v_ctecolnames = PyTuple_New(data.ctecolnames.length)
        for i in range(data.ctecolnames.length):
            item = create(structs.list_nth(data.ctecolnames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_ctecolnames, i, item)
    else:
        v_ctecolnames = None
    cdef tuple v_ctecoltypes
    cdef int ctecoltypes_i
    if data.ctecoltypes is not NULL:
        v_ctecoltypes = PyTuple_New(data.ctecoltypes.length)
        for i in range(data.ctecoltypes.length):
            item = create(structs.list_nth(data.ctecoltypes, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_ctecoltypes, i, item)
    else:
        v_ctecoltypes = None
    cdef tuple v_ctecoltypmods
    cdef int ctecoltypmods_i
    if data.ctecoltypmods is not NULL:
        v_ctecoltypmods = PyTuple_New(data.ctecoltypmods.length)
        for i in range(data.ctecoltypmods.length):
            item = create(structs.list_nth(data.ctecoltypmods, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_ctecoltypmods, i, item)
    else:
        v_ctecoltypmods = None
    cdef tuple v_ctecolcollations
    cdef int ctecolcollations_i
    if data.ctecolcollations is not NULL:
        v_ctecolcollations = PyTuple_New(data.ctecolcollations.length)
        for i in range(data.ctecolcollations.length):
            item = create(structs.list_nth(data.ctecolcollations, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_ctecolcollations, i, item)
    else:
        v_ctecolcollations = None
    return ast.CommonTableExpr(v_ctename, v_aliascolnames, v_ctematerialized, v_ctequery, v_location, v_cterecursive, v_cterefcount, v_ctecolnames, v_ctecoltypes, v_ctecoltypmods, v_ctecolcollations)


cdef create_TriggerTransition(structs.TriggerTransition* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_isNew = bool(data.isNew)
    cdef object v_isTable = bool(data.isTable)
    return ast.TriggerTransition(v_name, v_isNew, v_isTable)


cdef create_RawStmt(structs.RawStmt* data, offset_to_index):
    cdef object v_stmt
    if data.stmt is not NULL:
        v_stmt = create(data.stmt, offset_to_index)
    else:
        v_stmt = None
    cdef object v_stmt_location = offset_to_index(data.stmt_location)
    cdef object v_stmt_len = offset_to_index(data.stmt_location + data.stmt_len) - offset_to_index(data.stmt_location)
    return ast.RawStmt(v_stmt, v_stmt_location, v_stmt_len)


cdef create_InsertStmt(structs.InsertStmt* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef tuple v_cols
    cdef int cols_i
    if data.cols is not NULL:
        v_cols = PyTuple_New(data.cols.length)
        for i in range(data.cols.length):
            item = create(structs.list_nth(data.cols, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_cols, i, item)
    else:
        v_cols = None
    cdef object v_selectStmt
    if data.selectStmt is not NULL:
        v_selectStmt = create(data.selectStmt, offset_to_index)
    else:
        v_selectStmt = None
    cdef object v_onConflictClause
    if data.onConflictClause is not NULL:
        v_onConflictClause = create(data.onConflictClause, offset_to_index)
    else:
        v_onConflictClause = None
    cdef tuple v_returningList
    cdef int returningList_i
    if data.returningList is not NULL:
        v_returningList = PyTuple_New(data.returningList.length)
        for i in range(data.returningList.length):
            item = create(structs.list_nth(data.returningList, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_returningList, i, item)
    else:
        v_returningList = None
    cdef object v_withClause
    if data.withClause is not NULL:
        v_withClause = create(data.withClause, offset_to_index)
    else:
        v_withClause = None
    cdef object v_override = getattr(enums, 'OverridingKind')(data.override)
    return ast.InsertStmt(v_relation, v_cols, v_selectStmt, v_onConflictClause, v_returningList, v_withClause, v_override)


cdef create_DeleteStmt(structs.DeleteStmt* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef tuple v_usingClause
    cdef int usingClause_i
    if data.usingClause is not NULL:
        v_usingClause = PyTuple_New(data.usingClause.length)
        for i in range(data.usingClause.length):
            item = create(structs.list_nth(data.usingClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_usingClause, i, item)
    else:
        v_usingClause = None
    cdef object v_whereClause
    if data.whereClause is not NULL:
        v_whereClause = create(data.whereClause, offset_to_index)
    else:
        v_whereClause = None
    cdef tuple v_returningList
    cdef int returningList_i
    if data.returningList is not NULL:
        v_returningList = PyTuple_New(data.returningList.length)
        for i in range(data.returningList.length):
            item = create(structs.list_nth(data.returningList, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_returningList, i, item)
    else:
        v_returningList = None
    cdef object v_withClause
    if data.withClause is not NULL:
        v_withClause = create(data.withClause, offset_to_index)
    else:
        v_withClause = None
    return ast.DeleteStmt(v_relation, v_usingClause, v_whereClause, v_returningList, v_withClause)


cdef create_UpdateStmt(structs.UpdateStmt* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef tuple v_targetList
    cdef int targetList_i
    if data.targetList is not NULL:
        v_targetList = PyTuple_New(data.targetList.length)
        for i in range(data.targetList.length):
            item = create(structs.list_nth(data.targetList, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_targetList, i, item)
    else:
        v_targetList = None
    cdef object v_whereClause
    if data.whereClause is not NULL:
        v_whereClause = create(data.whereClause, offset_to_index)
    else:
        v_whereClause = None
    cdef tuple v_fromClause
    cdef int fromClause_i
    if data.fromClause is not NULL:
        v_fromClause = PyTuple_New(data.fromClause.length)
        for i in range(data.fromClause.length):
            item = create(structs.list_nth(data.fromClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_fromClause, i, item)
    else:
        v_fromClause = None
    cdef tuple v_returningList
    cdef int returningList_i
    if data.returningList is not NULL:
        v_returningList = PyTuple_New(data.returningList.length)
        for i in range(data.returningList.length):
            item = create(structs.list_nth(data.returningList, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_returningList, i, item)
    else:
        v_returningList = None
    cdef object v_withClause
    if data.withClause is not NULL:
        v_withClause = create(data.withClause, offset_to_index)
    else:
        v_withClause = None
    return ast.UpdateStmt(v_relation, v_targetList, v_whereClause, v_fromClause, v_returningList, v_withClause)


cdef create_SelectStmt(structs.SelectStmt* data, offset_to_index):
    cdef tuple v_distinctClause
    cdef int distinctClause_i
    if data.distinctClause is not NULL:
        v_distinctClause = PyTuple_New(data.distinctClause.length)
        for i in range(data.distinctClause.length):
            item = create(structs.list_nth(data.distinctClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_distinctClause, i, item)
    else:
        v_distinctClause = None
    cdef object v_intoClause
    if data.intoClause is not NULL:
        v_intoClause = create(data.intoClause, offset_to_index)
    else:
        v_intoClause = None
    cdef tuple v_targetList
    cdef int targetList_i
    if data.targetList is not NULL:
        v_targetList = PyTuple_New(data.targetList.length)
        for i in range(data.targetList.length):
            item = create(structs.list_nth(data.targetList, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_targetList, i, item)
    else:
        v_targetList = None
    cdef tuple v_fromClause
    cdef int fromClause_i
    if data.fromClause is not NULL:
        v_fromClause = PyTuple_New(data.fromClause.length)
        for i in range(data.fromClause.length):
            item = create(structs.list_nth(data.fromClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_fromClause, i, item)
    else:
        v_fromClause = None
    cdef object v_whereClause
    if data.whereClause is not NULL:
        v_whereClause = create(data.whereClause, offset_to_index)
    else:
        v_whereClause = None
    cdef tuple v_groupClause
    cdef int groupClause_i
    if data.groupClause is not NULL:
        v_groupClause = PyTuple_New(data.groupClause.length)
        for i in range(data.groupClause.length):
            item = create(structs.list_nth(data.groupClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_groupClause, i, item)
    else:
        v_groupClause = None
    cdef object v_havingClause
    if data.havingClause is not NULL:
        v_havingClause = create(data.havingClause, offset_to_index)
    else:
        v_havingClause = None
    cdef tuple v_windowClause
    cdef int windowClause_i
    if data.windowClause is not NULL:
        v_windowClause = PyTuple_New(data.windowClause.length)
        for i in range(data.windowClause.length):
            item = create(structs.list_nth(data.windowClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_windowClause, i, item)
    else:
        v_windowClause = None
    cdef tuple v_valuesLists
    cdef int valuesLists_i
    if data.valuesLists is not NULL:
        v_valuesLists = PyTuple_New(data.valuesLists.length)
        for i in range(data.valuesLists.length):
            item = create(structs.list_nth(data.valuesLists, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_valuesLists, i, item)
    else:
        v_valuesLists = None
    cdef tuple v_sortClause
    cdef int sortClause_i
    if data.sortClause is not NULL:
        v_sortClause = PyTuple_New(data.sortClause.length)
        for i in range(data.sortClause.length):
            item = create(structs.list_nth(data.sortClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_sortClause, i, item)
    else:
        v_sortClause = None
    cdef object v_limitOffset
    if data.limitOffset is not NULL:
        v_limitOffset = create(data.limitOffset, offset_to_index)
    else:
        v_limitOffset = None
    cdef object v_limitCount
    if data.limitCount is not NULL:
        v_limitCount = create(data.limitCount, offset_to_index)
    else:
        v_limitCount = None
    cdef object v_limitOption = getattr(enums, 'LimitOption')(data.limitOption)
    cdef tuple v_lockingClause
    cdef int lockingClause_i
    if data.lockingClause is not NULL:
        v_lockingClause = PyTuple_New(data.lockingClause.length)
        for i in range(data.lockingClause.length):
            item = create(structs.list_nth(data.lockingClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_lockingClause, i, item)
    else:
        v_lockingClause = None
    cdef object v_withClause
    if data.withClause is not NULL:
        v_withClause = create(data.withClause, offset_to_index)
    else:
        v_withClause = None
    cdef object v_op = getattr(enums, 'SetOperation')(data.op)
    cdef object v_all = bool(data.all)
    cdef object v_larg
    if data.larg is not NULL:
        v_larg = create(data.larg, offset_to_index)
    else:
        v_larg = None
    cdef object v_rarg
    if data.rarg is not NULL:
        v_rarg = create(data.rarg, offset_to_index)
    else:
        v_rarg = None
    return ast.SelectStmt(v_distinctClause, v_intoClause, v_targetList, v_fromClause, v_whereClause, v_groupClause, v_havingClause, v_windowClause, v_valuesLists, v_sortClause, v_limitOffset, v_limitCount, v_limitOption, v_lockingClause, v_withClause, v_op, v_all, v_larg, v_rarg)


cdef create_SetOperationStmt(structs.SetOperationStmt* data, offset_to_index):
    cdef object v_op = getattr(enums, 'SetOperation')(data.op)
    cdef object v_all = bool(data.all)
    cdef object v_larg
    if data.larg is not NULL:
        v_larg = create(data.larg, offset_to_index)
    else:
        v_larg = None
    cdef object v_rarg
    if data.rarg is not NULL:
        v_rarg = create(data.rarg, offset_to_index)
    else:
        v_rarg = None
    cdef tuple v_colTypes
    cdef int colTypes_i
    if data.colTypes is not NULL:
        v_colTypes = PyTuple_New(data.colTypes.length)
        for i in range(data.colTypes.length):
            item = create(structs.list_nth(data.colTypes, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colTypes, i, item)
    else:
        v_colTypes = None
    cdef tuple v_colTypmods
    cdef int colTypmods_i
    if data.colTypmods is not NULL:
        v_colTypmods = PyTuple_New(data.colTypmods.length)
        for i in range(data.colTypmods.length):
            item = create(structs.list_nth(data.colTypmods, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colTypmods, i, item)
    else:
        v_colTypmods = None
    cdef tuple v_colCollations
    cdef int colCollations_i
    if data.colCollations is not NULL:
        v_colCollations = PyTuple_New(data.colCollations.length)
        for i in range(data.colCollations.length):
            item = create(structs.list_nth(data.colCollations, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colCollations, i, item)
    else:
        v_colCollations = None
    cdef tuple v_groupClauses
    cdef int groupClauses_i
    if data.groupClauses is not NULL:
        v_groupClauses = PyTuple_New(data.groupClauses.length)
        for i in range(data.groupClauses.length):
            item = create(structs.list_nth(data.groupClauses, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_groupClauses, i, item)
    else:
        v_groupClauses = None
    return ast.SetOperationStmt(v_op, v_all, v_larg, v_rarg, v_colTypes, v_colTypmods, v_colCollations, v_groupClauses)


cdef create_CreateSchemaStmt(structs.CreateSchemaStmt* data, offset_to_index):
    cdef object v_schemaname
    if data.schemaname is not NULL:
        v_schemaname = data.schemaname.decode("utf-8")
    else:
        v_schemaname = None
    cdef object v_authrole
    if data.authrole is not NULL:
        v_authrole = create(data.authrole, offset_to_index)
    else:
        v_authrole = None
    cdef tuple v_schemaElts
    cdef int schemaElts_i
    if data.schemaElts is not NULL:
        v_schemaElts = PyTuple_New(data.schemaElts.length)
        for i in range(data.schemaElts.length):
            item = create(structs.list_nth(data.schemaElts, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_schemaElts, i, item)
    else:
        v_schemaElts = None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateSchemaStmt(v_schemaname, v_authrole, v_schemaElts, v_if_not_exists)


cdef create_AlterTableStmt(structs.AlterTableStmt* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef tuple v_cmds
    cdef int cmds_i
    if data.cmds is not NULL:
        v_cmds = PyTuple_New(data.cmds.length)
        for i in range(data.cmds.length):
            item = create(structs.list_nth(data.cmds, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_cmds, i, item)
    else:
        v_cmds = None
    cdef object v_relkind = getattr(enums, 'ObjectType')(data.relkind)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterTableStmt(v_relation, v_cmds, v_relkind, v_missing_ok)


cdef create_ReplicaIdentityStmt(structs.ReplicaIdentityStmt* data, offset_to_index):
    cdef object v_identity_type = chr(data.identity_type)
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    return ast.ReplicaIdentityStmt(v_identity_type, v_name)


cdef create_AlterTableCmd(structs.AlterTableCmd* data, offset_to_index):
    cdef object v_subtype = getattr(enums, 'AlterTableType')(data.subtype)
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_num = data.num
    cdef object v_newowner
    if data.newowner is not NULL:
        v_newowner = create(data.newowner, offset_to_index)
    else:
        v_newowner = None
    cdef object v_def_
    if data.def_ is not NULL:
        v_def_ = create(data.def_, offset_to_index)
    else:
        v_def_ = None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterTableCmd(v_subtype, v_name, v_num, v_newowner, v_def_, v_behavior, v_missing_ok)


cdef create_AlterCollationStmt(structs.AlterCollationStmt* data, offset_to_index):
    cdef tuple v_collname
    cdef int collname_i
    if data.collname is not NULL:
        v_collname = PyTuple_New(data.collname.length)
        for i in range(data.collname.length):
            item = create(structs.list_nth(data.collname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_collname, i, item)
    else:
        v_collname = None
    return ast.AlterCollationStmt(v_collname)


cdef create_AlterDomainStmt(structs.AlterDomainStmt* data, offset_to_index):
    cdef object v_subtype = chr(data.subtype)
    cdef tuple v_typeName
    cdef int typeName_i
    if data.typeName is not NULL:
        v_typeName = PyTuple_New(data.typeName.length)
        for i in range(data.typeName.length):
            item = create(structs.list_nth(data.typeName, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_typeName, i, item)
    else:
        v_typeName = None
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_def_
    if data.def_ is not NULL:
        v_def_ = create(data.def_, offset_to_index)
    else:
        v_def_ = None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterDomainStmt(v_subtype, v_typeName, v_name, v_def_, v_behavior, v_missing_ok)


cdef create_GrantStmt(structs.GrantStmt* data, offset_to_index):
    cdef object v_is_grant = bool(data.is_grant)
    cdef object v_targtype = getattr(enums, 'GrantTargetType')(data.targtype)
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef tuple v_objects
    cdef int objects_i
    if data.objects is not NULL:
        v_objects = PyTuple_New(data.objects.length)
        for i in range(data.objects.length):
            item = create(structs.list_nth(data.objects, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_objects, i, item)
    else:
        v_objects = None
    cdef tuple v_privileges
    cdef int privileges_i
    if data.privileges is not NULL:
        v_privileges = PyTuple_New(data.privileges.length)
        for i in range(data.privileges.length):
            item = create(structs.list_nth(data.privileges, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_privileges, i, item)
    else:
        v_privileges = None
    cdef tuple v_grantees
    cdef int grantees_i
    if data.grantees is not NULL:
        v_grantees = PyTuple_New(data.grantees.length)
        for i in range(data.grantees.length):
            item = create(structs.list_nth(data.grantees, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_grantees, i, item)
    else:
        v_grantees = None
    cdef object v_grant_option = bool(data.grant_option)
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.GrantStmt(v_is_grant, v_targtype, v_objtype, v_objects, v_privileges, v_grantees, v_grant_option, v_behavior)


cdef create_ObjectWithArgs(structs.ObjectWithArgs* data, offset_to_index):
    cdef tuple v_objname
    cdef int objname_i
    if data.objname is not NULL:
        v_objname = PyTuple_New(data.objname.length)
        for i in range(data.objname.length):
            item = create(structs.list_nth(data.objname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_objname, i, item)
    else:
        v_objname = None
    cdef tuple v_objargs
    cdef int objargs_i
    if data.objargs is not NULL:
        v_objargs = PyTuple_New(data.objargs.length)
        for i in range(data.objargs.length):
            item = create(structs.list_nth(data.objargs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_objargs, i, item)
    else:
        v_objargs = None
    cdef object v_args_unspecified = bool(data.args_unspecified)
    return ast.ObjectWithArgs(v_objname, v_objargs, v_args_unspecified)


cdef create_AccessPriv(structs.AccessPriv* data, offset_to_index):
    cdef object v_priv_name
    if data.priv_name is not NULL:
        v_priv_name = data.priv_name.decode("utf-8")
    else:
        v_priv_name = None
    cdef tuple v_cols
    cdef int cols_i
    if data.cols is not NULL:
        v_cols = PyTuple_New(data.cols.length)
        for i in range(data.cols.length):
            item = create(structs.list_nth(data.cols, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_cols, i, item)
    else:
        v_cols = None
    return ast.AccessPriv(v_priv_name, v_cols)


cdef create_GrantRoleStmt(structs.GrantRoleStmt* data, offset_to_index):
    cdef tuple v_granted_roles
    cdef int granted_roles_i
    if data.granted_roles is not NULL:
        v_granted_roles = PyTuple_New(data.granted_roles.length)
        for i in range(data.granted_roles.length):
            item = create(structs.list_nth(data.granted_roles, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_granted_roles, i, item)
    else:
        v_granted_roles = None
    cdef tuple v_grantee_roles
    cdef int grantee_roles_i
    if data.grantee_roles is not NULL:
        v_grantee_roles = PyTuple_New(data.grantee_roles.length)
        for i in range(data.grantee_roles.length):
            item = create(structs.list_nth(data.grantee_roles, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_grantee_roles, i, item)
    else:
        v_grantee_roles = None
    cdef object v_is_grant = bool(data.is_grant)
    cdef object v_admin_opt = bool(data.admin_opt)
    cdef object v_grantor
    if data.grantor is not NULL:
        v_grantor = create(data.grantor, offset_to_index)
    else:
        v_grantor = None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.GrantRoleStmt(v_granted_roles, v_grantee_roles, v_is_grant, v_admin_opt, v_grantor, v_behavior)


cdef create_AlterDefaultPrivilegesStmt(structs.AlterDefaultPrivilegesStmt* data, offset_to_index):
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_action
    if data.action is not NULL:
        v_action = create(data.action, offset_to_index)
    else:
        v_action = None
    return ast.AlterDefaultPrivilegesStmt(v_options, v_action)


cdef create_CopyStmt(structs.CopyStmt* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_query
    if data.query is not NULL:
        v_query = create(data.query, offset_to_index)
    else:
        v_query = None
    cdef tuple v_attlist
    cdef int attlist_i
    if data.attlist is not NULL:
        v_attlist = PyTuple_New(data.attlist.length)
        for i in range(data.attlist.length):
            item = create(structs.list_nth(data.attlist, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_attlist, i, item)
    else:
        v_attlist = None
    cdef object v_is_from = bool(data.is_from)
    cdef object v_is_program = bool(data.is_program)
    cdef object v_filename
    if data.filename is not NULL:
        v_filename = data.filename.decode("utf-8")
    else:
        v_filename = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_whereClause
    if data.whereClause is not NULL:
        v_whereClause = create(data.whereClause, offset_to_index)
    else:
        v_whereClause = None
    return ast.CopyStmt(v_relation, v_query, v_attlist, v_is_from, v_is_program, v_filename, v_options, v_whereClause)


cdef create_VariableSetStmt(structs.VariableSetStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'VariableSetKind')(data.kind)
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_is_local = bool(data.is_local)
    return ast.VariableSetStmt(v_kind, v_name, v_args, v_is_local)


cdef create_VariableShowStmt(structs.VariableShowStmt* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    return ast.VariableShowStmt(v_name)


cdef create_CreateStmt(structs.CreateStmt* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef tuple v_tableElts
    cdef int tableElts_i
    if data.tableElts is not NULL:
        v_tableElts = PyTuple_New(data.tableElts.length)
        for i in range(data.tableElts.length):
            item = create(structs.list_nth(data.tableElts, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_tableElts, i, item)
    else:
        v_tableElts = None
    cdef tuple v_inhRelations
    cdef int inhRelations_i
    if data.inhRelations is not NULL:
        v_inhRelations = PyTuple_New(data.inhRelations.length)
        for i in range(data.inhRelations.length):
            item = create(structs.list_nth(data.inhRelations, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_inhRelations, i, item)
    else:
        v_inhRelations = None
    cdef object v_partbound
    if data.partbound is not NULL:
        v_partbound = create(data.partbound, offset_to_index)
    else:
        v_partbound = None
    cdef object v_partspec
    if data.partspec is not NULL:
        v_partspec = create(data.partspec, offset_to_index)
    else:
        v_partspec = None
    cdef object v_ofTypename
    if data.ofTypename is not NULL:
        v_ofTypename = create(data.ofTypename, offset_to_index)
    else:
        v_ofTypename = None
    cdef tuple v_constraints
    cdef int constraints_i
    if data.constraints is not NULL:
        v_constraints = PyTuple_New(data.constraints.length)
        for i in range(data.constraints.length):
            item = create(structs.list_nth(data.constraints, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_constraints, i, item)
    else:
        v_constraints = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_oncommit = getattr(enums, 'OnCommitAction')(data.oncommit)
    cdef object v_tablespacename
    if data.tablespacename is not NULL:
        v_tablespacename = data.tablespacename.decode("utf-8")
    else:
        v_tablespacename = None
    cdef object v_accessMethod
    if data.accessMethod is not NULL:
        v_accessMethod = data.accessMethod.decode("utf-8")
    else:
        v_accessMethod = None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateStmt(v_relation, v_tableElts, v_inhRelations, v_partbound, v_partspec, v_ofTypename, v_constraints, v_options, v_oncommit, v_tablespacename, v_accessMethod, v_if_not_exists)


cdef create_Constraint(structs.Constraint* data, offset_to_index):
    cdef object v_contype = getattr(enums, 'ConstrType')(data.contype)
    cdef object v_conname
    if data.conname is not NULL:
        v_conname = data.conname.decode("utf-8")
    else:
        v_conname = None
    cdef object v_deferrable = bool(data.deferrable)
    cdef object v_initdeferred = bool(data.initdeferred)
    cdef object v_location = offset_to_index(data.location)
    cdef object v_is_no_inherit = bool(data.is_no_inherit)
    cdef object v_raw_expr
    if data.raw_expr is not NULL:
        v_raw_expr = create(data.raw_expr, offset_to_index)
    else:
        v_raw_expr = None
    cdef object v_cooked_expr
    if data.cooked_expr is not NULL:
        v_cooked_expr = data.cooked_expr.decode("utf-8")
    else:
        v_cooked_expr = None
    cdef object v_generated_when = chr(data.generated_when)
    cdef tuple v_keys
    cdef int keys_i
    if data.keys is not NULL:
        v_keys = PyTuple_New(data.keys.length)
        for i in range(data.keys.length):
            item = create(structs.list_nth(data.keys, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_keys, i, item)
    else:
        v_keys = None
    cdef tuple v_including
    cdef int including_i
    if data.including is not NULL:
        v_including = PyTuple_New(data.including.length)
        for i in range(data.including.length):
            item = create(structs.list_nth(data.including, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_including, i, item)
    else:
        v_including = None
    cdef tuple v_exclusions
    cdef int exclusions_i
    if data.exclusions is not NULL:
        v_exclusions = PyTuple_New(data.exclusions.length)
        for i in range(data.exclusions.length):
            item = create(structs.list_nth(data.exclusions, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_exclusions, i, item)
    else:
        v_exclusions = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_indexname
    if data.indexname is not NULL:
        v_indexname = data.indexname.decode("utf-8")
    else:
        v_indexname = None
    cdef object v_indexspace
    if data.indexspace is not NULL:
        v_indexspace = data.indexspace.decode("utf-8")
    else:
        v_indexspace = None
    cdef object v_reset_default_tblspc = bool(data.reset_default_tblspc)
    cdef object v_access_method
    if data.access_method is not NULL:
        v_access_method = data.access_method.decode("utf-8")
    else:
        v_access_method = None
    cdef object v_where_clause
    if data.where_clause is not NULL:
        v_where_clause = create(data.where_clause, offset_to_index)
    else:
        v_where_clause = None
    cdef object v_pktable
    if data.pktable is not NULL:
        v_pktable = create(data.pktable, offset_to_index)
    else:
        v_pktable = None
    cdef tuple v_fk_attrs
    cdef int fk_attrs_i
    if data.fk_attrs is not NULL:
        v_fk_attrs = PyTuple_New(data.fk_attrs.length)
        for i in range(data.fk_attrs.length):
            item = create(structs.list_nth(data.fk_attrs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_fk_attrs, i, item)
    else:
        v_fk_attrs = None
    cdef tuple v_pk_attrs
    cdef int pk_attrs_i
    if data.pk_attrs is not NULL:
        v_pk_attrs = PyTuple_New(data.pk_attrs.length)
        for i in range(data.pk_attrs.length):
            item = create(structs.list_nth(data.pk_attrs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_pk_attrs, i, item)
    else:
        v_pk_attrs = None
    cdef object v_fk_matchtype = chr(data.fk_matchtype)
    cdef object v_fk_upd_action = chr(data.fk_upd_action)
    cdef object v_fk_del_action = chr(data.fk_del_action)
    cdef tuple v_old_conpfeqop
    cdef int old_conpfeqop_i
    if data.old_conpfeqop is not NULL:
        v_old_conpfeqop = PyTuple_New(data.old_conpfeqop.length)
        for i in range(data.old_conpfeqop.length):
            item = create(structs.list_nth(data.old_conpfeqop, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_old_conpfeqop, i, item)
    else:
        v_old_conpfeqop = None
    cdef object v_skip_validation = bool(data.skip_validation)
    cdef object v_initially_valid = bool(data.initially_valid)
    return ast.Constraint(v_contype, v_conname, v_deferrable, v_initdeferred, v_location, v_is_no_inherit, v_raw_expr, v_cooked_expr, v_generated_when, v_keys, v_including, v_exclusions, v_options, v_indexname, v_indexspace, v_reset_default_tblspc, v_access_method, v_where_clause, v_pktable, v_fk_attrs, v_pk_attrs, v_fk_matchtype, v_fk_upd_action, v_fk_del_action, v_old_conpfeqop, v_skip_validation, v_initially_valid)


cdef create_CreateTableSpaceStmt(structs.CreateTableSpaceStmt* data, offset_to_index):
    cdef object v_tablespacename
    if data.tablespacename is not NULL:
        v_tablespacename = data.tablespacename.decode("utf-8")
    else:
        v_tablespacename = None
    cdef object v_owner
    if data.owner is not NULL:
        v_owner = create(data.owner, offset_to_index)
    else:
        v_owner = None
    cdef object v_location = offset_to_index(data.location)
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreateTableSpaceStmt(v_tablespacename, v_owner, v_location, v_options)


cdef create_DropTableSpaceStmt(structs.DropTableSpaceStmt* data, offset_to_index):
    cdef object v_tablespacename
    if data.tablespacename is not NULL:
        v_tablespacename = data.tablespacename.decode("utf-8")
    else:
        v_tablespacename = None
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.DropTableSpaceStmt(v_tablespacename, v_missing_ok)


cdef create_AlterTableSpaceOptionsStmt(structs.AlterTableSpaceOptionsStmt* data, offset_to_index):
    cdef object v_tablespacename
    if data.tablespacename is not NULL:
        v_tablespacename = data.tablespacename.decode("utf-8")
    else:
        v_tablespacename = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_isReset = bool(data.isReset)
    return ast.AlterTableSpaceOptionsStmt(v_tablespacename, v_options, v_isReset)


cdef create_AlterTableMoveAllStmt(structs.AlterTableMoveAllStmt* data, offset_to_index):
    cdef object v_orig_tablespacename
    if data.orig_tablespacename is not NULL:
        v_orig_tablespacename = data.orig_tablespacename.decode("utf-8")
    else:
        v_orig_tablespacename = None
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef tuple v_roles
    cdef int roles_i
    if data.roles is not NULL:
        v_roles = PyTuple_New(data.roles.length)
        for i in range(data.roles.length):
            item = create(structs.list_nth(data.roles, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_roles, i, item)
    else:
        v_roles = None
    cdef object v_new_tablespacename
    if data.new_tablespacename is not NULL:
        v_new_tablespacename = data.new_tablespacename.decode("utf-8")
    else:
        v_new_tablespacename = None
    cdef object v_nowait = bool(data.nowait)
    return ast.AlterTableMoveAllStmt(v_orig_tablespacename, v_objtype, v_roles, v_new_tablespacename, v_nowait)


cdef create_CreateExtensionStmt(structs.CreateExtensionStmt* data, offset_to_index):
    cdef object v_extname
    if data.extname is not NULL:
        v_extname = data.extname.decode("utf-8")
    else:
        v_extname = None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreateExtensionStmt(v_extname, v_if_not_exists, v_options)


cdef create_AlterExtensionStmt(structs.AlterExtensionStmt* data, offset_to_index):
    cdef object v_extname
    if data.extname is not NULL:
        v_extname = data.extname.decode("utf-8")
    else:
        v_extname = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.AlterExtensionStmt(v_extname, v_options)


cdef create_AlterExtensionContentsStmt(structs.AlterExtensionContentsStmt* data, offset_to_index):
    cdef object v_extname
    if data.extname is not NULL:
        v_extname = data.extname.decode("utf-8")
    else:
        v_extname = None
    cdef object v_action = data.action
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_object
    if data.object is not NULL:
        v_object = create(data.object, offset_to_index)
    else:
        v_object = None
    return ast.AlterExtensionContentsStmt(v_extname, v_action, v_objtype, v_object)


cdef create_CreateFdwStmt(structs.CreateFdwStmt* data, offset_to_index):
    cdef object v_fdwname
    if data.fdwname is not NULL:
        v_fdwname = data.fdwname.decode("utf-8")
    else:
        v_fdwname = None
    cdef tuple v_func_options
    cdef int func_options_i
    if data.func_options is not NULL:
        v_func_options = PyTuple_New(data.func_options.length)
        for i in range(data.func_options.length):
            item = create(structs.list_nth(data.func_options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_func_options, i, item)
    else:
        v_func_options = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreateFdwStmt(v_fdwname, v_func_options, v_options)


cdef create_AlterFdwStmt(structs.AlterFdwStmt* data, offset_to_index):
    cdef object v_fdwname
    if data.fdwname is not NULL:
        v_fdwname = data.fdwname.decode("utf-8")
    else:
        v_fdwname = None
    cdef tuple v_func_options
    cdef int func_options_i
    if data.func_options is not NULL:
        v_func_options = PyTuple_New(data.func_options.length)
        for i in range(data.func_options.length):
            item = create(structs.list_nth(data.func_options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_func_options, i, item)
    else:
        v_func_options = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.AlterFdwStmt(v_fdwname, v_func_options, v_options)


cdef create_CreateForeignServerStmt(structs.CreateForeignServerStmt* data, offset_to_index):
    cdef object v_servername
    if data.servername is not NULL:
        v_servername = data.servername.decode("utf-8")
    else:
        v_servername = None
    cdef object v_servertype
    if data.servertype is not NULL:
        v_servertype = data.servertype.decode("utf-8")
    else:
        v_servertype = None
    cdef object v_version
    if data.version is not NULL:
        v_version = data.version.decode("utf-8")
    else:
        v_version = None
    cdef object v_fdwname
    if data.fdwname is not NULL:
        v_fdwname = data.fdwname.decode("utf-8")
    else:
        v_fdwname = None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreateForeignServerStmt(v_servername, v_servertype, v_version, v_fdwname, v_if_not_exists, v_options)


cdef create_AlterForeignServerStmt(structs.AlterForeignServerStmt* data, offset_to_index):
    cdef object v_servername
    if data.servername is not NULL:
        v_servername = data.servername.decode("utf-8")
    else:
        v_servername = None
    cdef object v_version
    if data.version is not NULL:
        v_version = data.version.decode("utf-8")
    else:
        v_version = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_has_version = bool(data.has_version)
    return ast.AlterForeignServerStmt(v_servername, v_version, v_options, v_has_version)


cdef create_CreateForeignTableStmt(structs.CreateForeignTableStmt* data, offset_to_index):

    cdef object v_base = create_CreateStmt(<structs.CreateStmt*> data, offset_to_index)
    cdef object v_servername
    if data.servername is not NULL:
        v_servername = data.servername.decode("utf-8")
    else:
        v_servername = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreateForeignTableStmt(v_base, v_servername, v_options)


cdef create_CreateUserMappingStmt(structs.CreateUserMappingStmt* data, offset_to_index):
    cdef object v_user
    if data.user is not NULL:
        v_user = create(data.user, offset_to_index)
    else:
        v_user = None
    cdef object v_servername
    if data.servername is not NULL:
        v_servername = data.servername.decode("utf-8")
    else:
        v_servername = None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreateUserMappingStmt(v_user, v_servername, v_if_not_exists, v_options)


cdef create_AlterUserMappingStmt(structs.AlterUserMappingStmt* data, offset_to_index):
    cdef object v_user
    if data.user is not NULL:
        v_user = create(data.user, offset_to_index)
    else:
        v_user = None
    cdef object v_servername
    if data.servername is not NULL:
        v_servername = data.servername.decode("utf-8")
    else:
        v_servername = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.AlterUserMappingStmt(v_user, v_servername, v_options)


cdef create_DropUserMappingStmt(structs.DropUserMappingStmt* data, offset_to_index):
    cdef object v_user
    if data.user is not NULL:
        v_user = create(data.user, offset_to_index)
    else:
        v_user = None
    cdef object v_servername
    if data.servername is not NULL:
        v_servername = data.servername.decode("utf-8")
    else:
        v_servername = None
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.DropUserMappingStmt(v_user, v_servername, v_missing_ok)


cdef create_ImportForeignSchemaStmt(structs.ImportForeignSchemaStmt* data, offset_to_index):
    cdef object v_server_name
    if data.server_name is not NULL:
        v_server_name = data.server_name.decode("utf-8")
    else:
        v_server_name = None
    cdef object v_remote_schema
    if data.remote_schema is not NULL:
        v_remote_schema = data.remote_schema.decode("utf-8")
    else:
        v_remote_schema = None
    cdef object v_local_schema
    if data.local_schema is not NULL:
        v_local_schema = data.local_schema.decode("utf-8")
    else:
        v_local_schema = None
    cdef object v_list_type = getattr(enums, 'ImportForeignSchemaType')(data.list_type)
    cdef tuple v_table_list
    cdef int table_list_i
    if data.table_list is not NULL:
        v_table_list = PyTuple_New(data.table_list.length)
        for i in range(data.table_list.length):
            item = create(structs.list_nth(data.table_list, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_table_list, i, item)
    else:
        v_table_list = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.ImportForeignSchemaStmt(v_server_name, v_remote_schema, v_local_schema, v_list_type, v_table_list, v_options)


cdef create_CreatePolicyStmt(structs.CreatePolicyStmt* data, offset_to_index):
    cdef object v_policy_name
    if data.policy_name is not NULL:
        v_policy_name = data.policy_name.decode("utf-8")
    else:
        v_policy_name = None
    cdef object v_table
    if data.table is not NULL:
        v_table = create(data.table, offset_to_index)
    else:
        v_table = None
    cdef object v_cmd_name
    if data.cmd_name is not NULL:
        v_cmd_name = data.cmd_name.decode("utf-8")
    else:
        v_cmd_name = None
    cdef object v_permissive = bool(data.permissive)
    cdef tuple v_roles
    cdef int roles_i
    if data.roles is not NULL:
        v_roles = PyTuple_New(data.roles.length)
        for i in range(data.roles.length):
            item = create(structs.list_nth(data.roles, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_roles, i, item)
    else:
        v_roles = None
    cdef object v_qual
    if data.qual is not NULL:
        v_qual = create(data.qual, offset_to_index)
    else:
        v_qual = None
    cdef object v_with_check
    if data.with_check is not NULL:
        v_with_check = create(data.with_check, offset_to_index)
    else:
        v_with_check = None
    return ast.CreatePolicyStmt(v_policy_name, v_table, v_cmd_name, v_permissive, v_roles, v_qual, v_with_check)


cdef create_AlterPolicyStmt(structs.AlterPolicyStmt* data, offset_to_index):
    cdef object v_policy_name
    if data.policy_name is not NULL:
        v_policy_name = data.policy_name.decode("utf-8")
    else:
        v_policy_name = None
    cdef object v_table
    if data.table is not NULL:
        v_table = create(data.table, offset_to_index)
    else:
        v_table = None
    cdef tuple v_roles
    cdef int roles_i
    if data.roles is not NULL:
        v_roles = PyTuple_New(data.roles.length)
        for i in range(data.roles.length):
            item = create(structs.list_nth(data.roles, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_roles, i, item)
    else:
        v_roles = None
    cdef object v_qual
    if data.qual is not NULL:
        v_qual = create(data.qual, offset_to_index)
    else:
        v_qual = None
    cdef object v_with_check
    if data.with_check is not NULL:
        v_with_check = create(data.with_check, offset_to_index)
    else:
        v_with_check = None
    return ast.AlterPolicyStmt(v_policy_name, v_table, v_roles, v_qual, v_with_check)


cdef create_CreateAmStmt(structs.CreateAmStmt* data, offset_to_index):
    cdef object v_amname
    if data.amname is not NULL:
        v_amname = data.amname.decode("utf-8")
    else:
        v_amname = None
    cdef tuple v_handler_name
    cdef int handler_name_i
    if data.handler_name is not NULL:
        v_handler_name = PyTuple_New(data.handler_name.length)
        for i in range(data.handler_name.length):
            item = create(structs.list_nth(data.handler_name, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_handler_name, i, item)
    else:
        v_handler_name = None
    cdef object v_amtype = chr(data.amtype)
    return ast.CreateAmStmt(v_amname, v_handler_name, v_amtype)


cdef create_CreateTrigStmt(structs.CreateTrigStmt* data, offset_to_index):
    cdef object v_trigname
    if data.trigname is not NULL:
        v_trigname = data.trigname.decode("utf-8")
    else:
        v_trigname = None
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef tuple v_funcname
    cdef int funcname_i
    if data.funcname is not NULL:
        v_funcname = PyTuple_New(data.funcname.length)
        for i in range(data.funcname.length):
            item = create(structs.list_nth(data.funcname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_funcname, i, item)
    else:
        v_funcname = None
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_row = bool(data.row)
    cdef object v_timing = data.timing
    cdef object v_events = data.events
    cdef tuple v_columns
    cdef int columns_i
    if data.columns is not NULL:
        v_columns = PyTuple_New(data.columns.length)
        for i in range(data.columns.length):
            item = create(structs.list_nth(data.columns, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_columns, i, item)
    else:
        v_columns = None
    cdef object v_whenClause
    if data.whenClause is not NULL:
        v_whenClause = create(data.whenClause, offset_to_index)
    else:
        v_whenClause = None
    cdef object v_isconstraint = bool(data.isconstraint)
    cdef tuple v_transitionRels
    cdef int transitionRels_i
    if data.transitionRels is not NULL:
        v_transitionRels = PyTuple_New(data.transitionRels.length)
        for i in range(data.transitionRels.length):
            item = create(structs.list_nth(data.transitionRels, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_transitionRels, i, item)
    else:
        v_transitionRels = None
    cdef object v_deferrable = bool(data.deferrable)
    cdef object v_initdeferred = bool(data.initdeferred)
    cdef object v_constrrel
    if data.constrrel is not NULL:
        v_constrrel = create(data.constrrel, offset_to_index)
    else:
        v_constrrel = None
    return ast.CreateTrigStmt(v_trigname, v_relation, v_funcname, v_args, v_row, v_timing, v_events, v_columns, v_whenClause, v_isconstraint, v_transitionRels, v_deferrable, v_initdeferred, v_constrrel)


cdef create_CreateEventTrigStmt(structs.CreateEventTrigStmt* data, offset_to_index):
    cdef object v_trigname
    if data.trigname is not NULL:
        v_trigname = data.trigname.decode("utf-8")
    else:
        v_trigname = None
    cdef object v_eventname
    if data.eventname is not NULL:
        v_eventname = data.eventname.decode("utf-8")
    else:
        v_eventname = None
    cdef tuple v_whenclause
    cdef int whenclause_i
    if data.whenclause is not NULL:
        v_whenclause = PyTuple_New(data.whenclause.length)
        for i in range(data.whenclause.length):
            item = create(structs.list_nth(data.whenclause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_whenclause, i, item)
    else:
        v_whenclause = None
    cdef tuple v_funcname
    cdef int funcname_i
    if data.funcname is not NULL:
        v_funcname = PyTuple_New(data.funcname.length)
        for i in range(data.funcname.length):
            item = create(structs.list_nth(data.funcname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_funcname, i, item)
    else:
        v_funcname = None
    return ast.CreateEventTrigStmt(v_trigname, v_eventname, v_whenclause, v_funcname)


cdef create_AlterEventTrigStmt(structs.AlterEventTrigStmt* data, offset_to_index):
    cdef object v_trigname
    if data.trigname is not NULL:
        v_trigname = data.trigname.decode("utf-8")
    else:
        v_trigname = None
    cdef object v_tgenabled = chr(data.tgenabled)
    return ast.AlterEventTrigStmt(v_trigname, v_tgenabled)


cdef create_CreatePLangStmt(structs.CreatePLangStmt* data, offset_to_index):
    cdef object v_replace = bool(data.replace)
    cdef object v_plname
    if data.plname is not NULL:
        v_plname = data.plname.decode("utf-8")
    else:
        v_plname = None
    cdef tuple v_plhandler
    cdef int plhandler_i
    if data.plhandler is not NULL:
        v_plhandler = PyTuple_New(data.plhandler.length)
        for i in range(data.plhandler.length):
            item = create(structs.list_nth(data.plhandler, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_plhandler, i, item)
    else:
        v_plhandler = None
    cdef tuple v_plinline
    cdef int plinline_i
    if data.plinline is not NULL:
        v_plinline = PyTuple_New(data.plinline.length)
        for i in range(data.plinline.length):
            item = create(structs.list_nth(data.plinline, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_plinline, i, item)
    else:
        v_plinline = None
    cdef tuple v_plvalidator
    cdef int plvalidator_i
    if data.plvalidator is not NULL:
        v_plvalidator = PyTuple_New(data.plvalidator.length)
        for i in range(data.plvalidator.length):
            item = create(structs.list_nth(data.plvalidator, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_plvalidator, i, item)
    else:
        v_plvalidator = None
    cdef object v_pltrusted = bool(data.pltrusted)
    return ast.CreatePLangStmt(v_replace, v_plname, v_plhandler, v_plinline, v_plvalidator, v_pltrusted)


cdef create_CreateRoleStmt(structs.CreateRoleStmt* data, offset_to_index):
    cdef object v_stmt_type = getattr(enums, 'RoleStmtType')(data.stmt_type)
    cdef object v_role
    if data.role is not NULL:
        v_role = data.role.decode("utf-8")
    else:
        v_role = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreateRoleStmt(v_stmt_type, v_role, v_options)


cdef create_AlterRoleStmt(structs.AlterRoleStmt* data, offset_to_index):
    cdef object v_role
    if data.role is not NULL:
        v_role = create(data.role, offset_to_index)
    else:
        v_role = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_action = data.action
    return ast.AlterRoleStmt(v_role, v_options, v_action)


cdef create_AlterRoleSetStmt(structs.AlterRoleSetStmt* data, offset_to_index):
    cdef object v_role
    if data.role is not NULL:
        v_role = create(data.role, offset_to_index)
    else:
        v_role = None
    cdef object v_database
    if data.database is not NULL:
        v_database = data.database.decode("utf-8")
    else:
        v_database = None
    cdef object v_setstmt
    if data.setstmt is not NULL:
        v_setstmt = create(data.setstmt, offset_to_index)
    else:
        v_setstmt = None
    return ast.AlterRoleSetStmt(v_role, v_database, v_setstmt)


cdef create_DropRoleStmt(structs.DropRoleStmt* data, offset_to_index):
    cdef tuple v_roles
    cdef int roles_i
    if data.roles is not NULL:
        v_roles = PyTuple_New(data.roles.length)
        for i in range(data.roles.length):
            item = create(structs.list_nth(data.roles, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_roles, i, item)
    else:
        v_roles = None
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.DropRoleStmt(v_roles, v_missing_ok)


cdef create_CreateSeqStmt(structs.CreateSeqStmt* data, offset_to_index):
    cdef object v_sequence
    if data.sequence is not NULL:
        v_sequence = create(data.sequence, offset_to_index)
    else:
        v_sequence = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_for_identity = bool(data.for_identity)
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateSeqStmt(v_sequence, v_options, v_for_identity, v_if_not_exists)


cdef create_AlterSeqStmt(structs.AlterSeqStmt* data, offset_to_index):
    cdef object v_sequence
    if data.sequence is not NULL:
        v_sequence = create(data.sequence, offset_to_index)
    else:
        v_sequence = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_for_identity = bool(data.for_identity)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterSeqStmt(v_sequence, v_options, v_for_identity, v_missing_ok)


cdef create_DefineStmt(structs.DefineStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'ObjectType')(data.kind)
    cdef object v_oldstyle = bool(data.oldstyle)
    cdef tuple v_defnames
    cdef int defnames_i
    if data.defnames is not NULL:
        v_defnames = PyTuple_New(data.defnames.length)
        for i in range(data.defnames.length):
            item = create(structs.list_nth(data.defnames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_defnames, i, item)
    else:
        v_defnames = None
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef tuple v_definition
    cdef int definition_i
    if data.definition is not NULL:
        v_definition = PyTuple_New(data.definition.length)
        for i in range(data.definition.length):
            item = create(structs.list_nth(data.definition, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_definition, i, item)
    else:
        v_definition = None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef object v_replace = bool(data.replace)
    return ast.DefineStmt(v_kind, v_oldstyle, v_defnames, v_args, v_definition, v_if_not_exists, v_replace)


cdef create_CreateDomainStmt(structs.CreateDomainStmt* data, offset_to_index):
    cdef tuple v_domainname
    cdef int domainname_i
    if data.domainname is not NULL:
        v_domainname = PyTuple_New(data.domainname.length)
        for i in range(data.domainname.length):
            item = create(structs.list_nth(data.domainname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_domainname, i, item)
    else:
        v_domainname = None
    cdef object v_typeName
    if data.typeName is not NULL:
        v_typeName = create(data.typeName, offset_to_index)
    else:
        v_typeName = None
    cdef object v_collClause
    if data.collClause is not NULL:
        v_collClause = create(data.collClause, offset_to_index)
    else:
        v_collClause = None
    cdef tuple v_constraints
    cdef int constraints_i
    if data.constraints is not NULL:
        v_constraints = PyTuple_New(data.constraints.length)
        for i in range(data.constraints.length):
            item = create(structs.list_nth(data.constraints, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_constraints, i, item)
    else:
        v_constraints = None
    return ast.CreateDomainStmt(v_domainname, v_typeName, v_collClause, v_constraints)


cdef create_CreateOpClassStmt(structs.CreateOpClassStmt* data, offset_to_index):
    cdef tuple v_opclassname
    cdef int opclassname_i
    if data.opclassname is not NULL:
        v_opclassname = PyTuple_New(data.opclassname.length)
        for i in range(data.opclassname.length):
            item = create(structs.list_nth(data.opclassname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_opclassname, i, item)
    else:
        v_opclassname = None
    cdef tuple v_opfamilyname
    cdef int opfamilyname_i
    if data.opfamilyname is not NULL:
        v_opfamilyname = PyTuple_New(data.opfamilyname.length)
        for i in range(data.opfamilyname.length):
            item = create(structs.list_nth(data.opfamilyname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_opfamilyname, i, item)
    else:
        v_opfamilyname = None
    cdef object v_amname
    if data.amname is not NULL:
        v_amname = data.amname.decode("utf-8")
    else:
        v_amname = None
    cdef object v_datatype
    if data.datatype is not NULL:
        v_datatype = create(data.datatype, offset_to_index)
    else:
        v_datatype = None
    cdef tuple v_items
    cdef int items_i
    if data.items is not NULL:
        v_items = PyTuple_New(data.items.length)
        for i in range(data.items.length):
            item = create(structs.list_nth(data.items, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_items, i, item)
    else:
        v_items = None
    cdef object v_isDefault = bool(data.isDefault)
    return ast.CreateOpClassStmt(v_opclassname, v_opfamilyname, v_amname, v_datatype, v_items, v_isDefault)


cdef create_CreateOpClassItem(structs.CreateOpClassItem* data, offset_to_index):
    cdef object v_itemtype = data.itemtype
    cdef object v_name
    if data.name is not NULL:
        v_name = create(data.name, offset_to_index)
    else:
        v_name = None
    cdef object v_number = data.number
    cdef tuple v_order_family
    cdef int order_family_i
    if data.order_family is not NULL:
        v_order_family = PyTuple_New(data.order_family.length)
        for i in range(data.order_family.length):
            item = create(structs.list_nth(data.order_family, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_order_family, i, item)
    else:
        v_order_family = None
    cdef tuple v_class_args
    cdef int class_args_i
    if data.class_args is not NULL:
        v_class_args = PyTuple_New(data.class_args.length)
        for i in range(data.class_args.length):
            item = create(structs.list_nth(data.class_args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_class_args, i, item)
    else:
        v_class_args = None
    cdef object v_storedtype
    if data.storedtype is not NULL:
        v_storedtype = create(data.storedtype, offset_to_index)
    else:
        v_storedtype = None
    return ast.CreateOpClassItem(v_itemtype, v_name, v_number, v_order_family, v_class_args, v_storedtype)


cdef create_CreateOpFamilyStmt(structs.CreateOpFamilyStmt* data, offset_to_index):
    cdef tuple v_opfamilyname
    cdef int opfamilyname_i
    if data.opfamilyname is not NULL:
        v_opfamilyname = PyTuple_New(data.opfamilyname.length)
        for i in range(data.opfamilyname.length):
            item = create(structs.list_nth(data.opfamilyname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_opfamilyname, i, item)
    else:
        v_opfamilyname = None
    cdef object v_amname
    if data.amname is not NULL:
        v_amname = data.amname.decode("utf-8")
    else:
        v_amname = None
    return ast.CreateOpFamilyStmt(v_opfamilyname, v_amname)


cdef create_AlterOpFamilyStmt(structs.AlterOpFamilyStmt* data, offset_to_index):
    cdef tuple v_opfamilyname
    cdef int opfamilyname_i
    if data.opfamilyname is not NULL:
        v_opfamilyname = PyTuple_New(data.opfamilyname.length)
        for i in range(data.opfamilyname.length):
            item = create(structs.list_nth(data.opfamilyname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_opfamilyname, i, item)
    else:
        v_opfamilyname = None
    cdef object v_amname
    if data.amname is not NULL:
        v_amname = data.amname.decode("utf-8")
    else:
        v_amname = None
    cdef object v_isDrop = bool(data.isDrop)
    cdef tuple v_items
    cdef int items_i
    if data.items is not NULL:
        v_items = PyTuple_New(data.items.length)
        for i in range(data.items.length):
            item = create(structs.list_nth(data.items, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_items, i, item)
    else:
        v_items = None
    return ast.AlterOpFamilyStmt(v_opfamilyname, v_amname, v_isDrop, v_items)


cdef create_DropStmt(structs.DropStmt* data, offset_to_index):
    cdef tuple v_objects
    cdef int objects_i
    if data.objects is not NULL:
        v_objects = PyTuple_New(data.objects.length)
        for i in range(data.objects.length):
            item = create(structs.list_nth(data.objects, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_objects, i, item)
    else:
        v_objects = None
    cdef object v_removeType = getattr(enums, 'ObjectType')(data.removeType)
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    cdef object v_missing_ok = bool(data.missing_ok)
    cdef object v_concurrent = bool(data.concurrent)
    return ast.DropStmt(v_objects, v_removeType, v_behavior, v_missing_ok, v_concurrent)


cdef create_TruncateStmt(structs.TruncateStmt* data, offset_to_index):
    cdef tuple v_relations
    cdef int relations_i
    if data.relations is not NULL:
        v_relations = PyTuple_New(data.relations.length)
        for i in range(data.relations.length):
            item = create(structs.list_nth(data.relations, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_relations, i, item)
    else:
        v_relations = None
    cdef object v_restart_seqs = bool(data.restart_seqs)
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.TruncateStmt(v_relations, v_restart_seqs, v_behavior)


cdef create_CommentStmt(structs.CommentStmt* data, offset_to_index):
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_object
    if data.object is not NULL:
        v_object = create(data.object, offset_to_index)
    else:
        v_object = None
    cdef object v_comment
    if data.comment is not NULL:
        v_comment = data.comment.decode("utf-8")
    else:
        v_comment = None
    return ast.CommentStmt(v_objtype, v_object, v_comment)


cdef create_SecLabelStmt(structs.SecLabelStmt* data, offset_to_index):
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_object
    if data.object is not NULL:
        v_object = create(data.object, offset_to_index)
    else:
        v_object = None
    cdef object v_provider
    if data.provider is not NULL:
        v_provider = data.provider.decode("utf-8")
    else:
        v_provider = None
    cdef object v_label
    if data.label is not NULL:
        v_label = data.label.decode("utf-8")
    else:
        v_label = None
    return ast.SecLabelStmt(v_objtype, v_object, v_provider, v_label)


cdef create_DeclareCursorStmt(structs.DeclareCursorStmt* data, offset_to_index):
    cdef object v_portalname
    if data.portalname is not NULL:
        v_portalname = data.portalname.decode("utf-8")
    else:
        v_portalname = None
    cdef object v_options = data.options
    cdef object v_query
    if data.query is not NULL:
        v_query = create(data.query, offset_to_index)
    else:
        v_query = None
    return ast.DeclareCursorStmt(v_portalname, v_options, v_query)


cdef create_ClosePortalStmt(structs.ClosePortalStmt* data, offset_to_index):
    cdef object v_portalname
    if data.portalname is not NULL:
        v_portalname = data.portalname.decode("utf-8")
    else:
        v_portalname = None
    return ast.ClosePortalStmt(v_portalname)


cdef create_FetchStmt(structs.FetchStmt* data, offset_to_index):
    cdef object v_direction = getattr(enums, 'FetchDirection')(data.direction)
    cdef object v_howMany = data.howMany
    cdef object v_portalname
    if data.portalname is not NULL:
        v_portalname = data.portalname.decode("utf-8")
    else:
        v_portalname = None
    cdef object v_ismove = bool(data.ismove)
    return ast.FetchStmt(v_direction, v_howMany, v_portalname, v_ismove)


cdef create_IndexStmt(structs.IndexStmt* data, offset_to_index):
    cdef object v_idxname
    if data.idxname is not NULL:
        v_idxname = data.idxname.decode("utf-8")
    else:
        v_idxname = None
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_accessMethod
    if data.accessMethod is not NULL:
        v_accessMethod = data.accessMethod.decode("utf-8")
    else:
        v_accessMethod = None
    cdef object v_tableSpace
    if data.tableSpace is not NULL:
        v_tableSpace = data.tableSpace.decode("utf-8")
    else:
        v_tableSpace = None
    cdef tuple v_indexParams
    cdef int indexParams_i
    if data.indexParams is not NULL:
        v_indexParams = PyTuple_New(data.indexParams.length)
        for i in range(data.indexParams.length):
            item = create(structs.list_nth(data.indexParams, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_indexParams, i, item)
    else:
        v_indexParams = None
    cdef tuple v_indexIncludingParams
    cdef int indexIncludingParams_i
    if data.indexIncludingParams is not NULL:
        v_indexIncludingParams = PyTuple_New(data.indexIncludingParams.length)
        for i in range(data.indexIncludingParams.length):
            item = create(structs.list_nth(data.indexIncludingParams, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_indexIncludingParams, i, item)
    else:
        v_indexIncludingParams = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_whereClause
    if data.whereClause is not NULL:
        v_whereClause = create(data.whereClause, offset_to_index)
    else:
        v_whereClause = None
    cdef tuple v_excludeOpNames
    cdef int excludeOpNames_i
    if data.excludeOpNames is not NULL:
        v_excludeOpNames = PyTuple_New(data.excludeOpNames.length)
        for i in range(data.excludeOpNames.length):
            item = create(structs.list_nth(data.excludeOpNames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_excludeOpNames, i, item)
    else:
        v_excludeOpNames = None
    cdef object v_idxcomment
    if data.idxcomment is not NULL:
        v_idxcomment = data.idxcomment.decode("utf-8")
    else:
        v_idxcomment = None
    cdef object v_oldCreateSubid = data.oldCreateSubid
    cdef object v_oldFirstRelfilenodeSubid = data.oldFirstRelfilenodeSubid
    cdef object v_unique = bool(data.unique)
    cdef object v_primary = bool(data.primary)
    cdef object v_isconstraint = bool(data.isconstraint)
    cdef object v_deferrable = bool(data.deferrable)
    cdef object v_initdeferred = bool(data.initdeferred)
    cdef object v_transformed = bool(data.transformed)
    cdef object v_concurrent = bool(data.concurrent)
    cdef object v_if_not_exists = bool(data.if_not_exists)
    cdef object v_reset_default_tblspc = bool(data.reset_default_tblspc)
    return ast.IndexStmt(v_idxname, v_relation, v_accessMethod, v_tableSpace, v_indexParams, v_indexIncludingParams, v_options, v_whereClause, v_excludeOpNames, v_idxcomment, v_oldCreateSubid, v_oldFirstRelfilenodeSubid, v_unique, v_primary, v_isconstraint, v_deferrable, v_initdeferred, v_transformed, v_concurrent, v_if_not_exists, v_reset_default_tblspc)


cdef create_CreateStatsStmt(structs.CreateStatsStmt* data, offset_to_index):
    cdef tuple v_defnames
    cdef int defnames_i
    if data.defnames is not NULL:
        v_defnames = PyTuple_New(data.defnames.length)
        for i in range(data.defnames.length):
            item = create(structs.list_nth(data.defnames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_defnames, i, item)
    else:
        v_defnames = None
    cdef tuple v_stat_types
    cdef int stat_types_i
    if data.stat_types is not NULL:
        v_stat_types = PyTuple_New(data.stat_types.length)
        for i in range(data.stat_types.length):
            item = create(structs.list_nth(data.stat_types, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_stat_types, i, item)
    else:
        v_stat_types = None
    cdef tuple v_exprs
    cdef int exprs_i
    if data.exprs is not NULL:
        v_exprs = PyTuple_New(data.exprs.length)
        for i in range(data.exprs.length):
            item = create(structs.list_nth(data.exprs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_exprs, i, item)
    else:
        v_exprs = None
    cdef tuple v_relations
    cdef int relations_i
    if data.relations is not NULL:
        v_relations = PyTuple_New(data.relations.length)
        for i in range(data.relations.length):
            item = create(structs.list_nth(data.relations, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_relations, i, item)
    else:
        v_relations = None
    cdef object v_stxcomment
    if data.stxcomment is not NULL:
        v_stxcomment = data.stxcomment.decode("utf-8")
    else:
        v_stxcomment = None
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateStatsStmt(v_defnames, v_stat_types, v_exprs, v_relations, v_stxcomment, v_if_not_exists)


cdef create_AlterStatsStmt(structs.AlterStatsStmt* data, offset_to_index):
    cdef tuple v_defnames
    cdef int defnames_i
    if data.defnames is not NULL:
        v_defnames = PyTuple_New(data.defnames.length)
        for i in range(data.defnames.length):
            item = create(structs.list_nth(data.defnames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_defnames, i, item)
    else:
        v_defnames = None
    cdef object v_stxstattarget = data.stxstattarget
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterStatsStmt(v_defnames, v_stxstattarget, v_missing_ok)


cdef create_CreateFunctionStmt(structs.CreateFunctionStmt* data, offset_to_index):
    cdef object v_is_procedure = bool(data.is_procedure)
    cdef object v_replace = bool(data.replace)
    cdef tuple v_funcname
    cdef int funcname_i
    if data.funcname is not NULL:
        v_funcname = PyTuple_New(data.funcname.length)
        for i in range(data.funcname.length):
            item = create(structs.list_nth(data.funcname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_funcname, i, item)
    else:
        v_funcname = None
    cdef tuple v_parameters
    cdef int parameters_i
    if data.parameters is not NULL:
        v_parameters = PyTuple_New(data.parameters.length)
        for i in range(data.parameters.length):
            item = create(structs.list_nth(data.parameters, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_parameters, i, item)
    else:
        v_parameters = None
    cdef object v_returnType
    if data.returnType is not NULL:
        v_returnType = create(data.returnType, offset_to_index)
    else:
        v_returnType = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreateFunctionStmt(v_is_procedure, v_replace, v_funcname, v_parameters, v_returnType, v_options)


cdef create_FunctionParameter(structs.FunctionParameter* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_argType
    if data.argType is not NULL:
        v_argType = create(data.argType, offset_to_index)
    else:
        v_argType = None
    cdef object v_mode = getattr(enums, 'FunctionParameterMode')(chr(data.mode))
    cdef object v_defexpr
    if data.defexpr is not NULL:
        v_defexpr = create(data.defexpr, offset_to_index)
    else:
        v_defexpr = None
    return ast.FunctionParameter(v_name, v_argType, v_mode, v_defexpr)


cdef create_AlterFunctionStmt(structs.AlterFunctionStmt* data, offset_to_index):
    cdef object v_objtype = getattr(enums, 'ObjectType')(data.objtype)
    cdef object v_func
    if data.func is not NULL:
        v_func = create(data.func, offset_to_index)
    else:
        v_func = None
    cdef tuple v_actions
    cdef int actions_i
    if data.actions is not NULL:
        v_actions = PyTuple_New(data.actions.length)
        for i in range(data.actions.length):
            item = create(structs.list_nth(data.actions, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_actions, i, item)
    else:
        v_actions = None
    return ast.AlterFunctionStmt(v_objtype, v_func, v_actions)


cdef create_DoStmt(structs.DoStmt* data, offset_to_index):
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    return ast.DoStmt(v_args)


cdef create_InlineCodeBlock(structs.InlineCodeBlock* data, offset_to_index):
    cdef object v_source_text
    if data.source_text is not NULL:
        v_source_text = data.source_text.decode("utf-8")
    else:
        v_source_text = None
    cdef object v_langIsTrusted = bool(data.langIsTrusted)
    cdef object v_atomic = bool(data.atomic)
    return ast.InlineCodeBlock(v_source_text, v_langIsTrusted, v_atomic)


cdef create_CallStmt(structs.CallStmt* data, offset_to_index):
    cdef object v_funccall
    if data.funccall is not NULL:
        v_funccall = create(data.funccall, offset_to_index)
    else:
        v_funccall = None
    cdef object v_funcexpr
    if data.funcexpr is not NULL:
        v_funcexpr = create(data.funcexpr, offset_to_index)
    else:
        v_funcexpr = None
    return ast.CallStmt(v_funccall, v_funcexpr)


cdef create_CallContext(structs.CallContext* data, offset_to_index):
    cdef object v_atomic = bool(data.atomic)
    return ast.CallContext(v_atomic)


cdef create_RenameStmt(structs.RenameStmt* data, offset_to_index):
    cdef object v_renameType = getattr(enums, 'ObjectType')(data.renameType)
    cdef object v_relationType = getattr(enums, 'ObjectType')(data.relationType)
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_object
    if data.object is not NULL:
        v_object = create(data.object, offset_to_index)
    else:
        v_object = None
    cdef object v_subname
    if data.subname is not NULL:
        v_subname = data.subname.decode("utf-8")
    else:
        v_subname = None
    cdef object v_newname
    if data.newname is not NULL:
        v_newname = data.newname.decode("utf-8")
    else:
        v_newname = None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.RenameStmt(v_renameType, v_relationType, v_relation, v_object, v_subname, v_newname, v_behavior, v_missing_ok)


cdef create_AlterObjectDependsStmt(structs.AlterObjectDependsStmt* data, offset_to_index):
    cdef object v_objectType = getattr(enums, 'ObjectType')(data.objectType)
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_object
    if data.object is not NULL:
        v_object = create(data.object, offset_to_index)
    else:
        v_object = None
    cdef object v_extname
    if data.extname is not NULL:
        v_extname = create(data.extname, offset_to_index)
    else:
        v_extname = None
    cdef object v_remove = bool(data.remove)
    return ast.AlterObjectDependsStmt(v_objectType, v_relation, v_object, v_extname, v_remove)


cdef create_AlterObjectSchemaStmt(structs.AlterObjectSchemaStmt* data, offset_to_index):
    cdef object v_objectType = getattr(enums, 'ObjectType')(data.objectType)
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_object
    if data.object is not NULL:
        v_object = create(data.object, offset_to_index)
    else:
        v_object = None
    cdef object v_newschema
    if data.newschema is not NULL:
        v_newschema = data.newschema.decode("utf-8")
    else:
        v_newschema = None
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterObjectSchemaStmt(v_objectType, v_relation, v_object, v_newschema, v_missing_ok)


cdef create_AlterOwnerStmt(structs.AlterOwnerStmt* data, offset_to_index):
    cdef object v_objectType = getattr(enums, 'ObjectType')(data.objectType)
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_object
    if data.object is not NULL:
        v_object = create(data.object, offset_to_index)
    else:
        v_object = None
    cdef object v_newowner
    if data.newowner is not NULL:
        v_newowner = create(data.newowner, offset_to_index)
    else:
        v_newowner = None
    return ast.AlterOwnerStmt(v_objectType, v_relation, v_object, v_newowner)


cdef create_AlterOperatorStmt(structs.AlterOperatorStmt* data, offset_to_index):
    cdef object v_opername
    if data.opername is not NULL:
        v_opername = create(data.opername, offset_to_index)
    else:
        v_opername = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.AlterOperatorStmt(v_opername, v_options)


cdef create_AlterTypeStmt(structs.AlterTypeStmt* data, offset_to_index):
    cdef tuple v_typeName
    cdef int typeName_i
    if data.typeName is not NULL:
        v_typeName = PyTuple_New(data.typeName.length)
        for i in range(data.typeName.length):
            item = create(structs.list_nth(data.typeName, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_typeName, i, item)
    else:
        v_typeName = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.AlterTypeStmt(v_typeName, v_options)


cdef create_RuleStmt(structs.RuleStmt* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_rulename
    if data.rulename is not NULL:
        v_rulename = data.rulename.decode("utf-8")
    else:
        v_rulename = None
    cdef object v_whereClause
    if data.whereClause is not NULL:
        v_whereClause = create(data.whereClause, offset_to_index)
    else:
        v_whereClause = None
    cdef object v_event = getattr(enums, 'CmdType')(data.event)
    cdef object v_instead = bool(data.instead)
    cdef tuple v_actions
    cdef int actions_i
    if data.actions is not NULL:
        v_actions = PyTuple_New(data.actions.length)
        for i in range(data.actions.length):
            item = create(structs.list_nth(data.actions, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_actions, i, item)
    else:
        v_actions = None
    cdef object v_replace = bool(data.replace)
    return ast.RuleStmt(v_relation, v_rulename, v_whereClause, v_event, v_instead, v_actions, v_replace)


cdef create_NotifyStmt(structs.NotifyStmt* data, offset_to_index):
    cdef object v_conditionname
    if data.conditionname is not NULL:
        v_conditionname = data.conditionname.decode("utf-8")
    else:
        v_conditionname = None
    cdef object v_payload
    if data.payload is not NULL:
        v_payload = data.payload.decode("utf-8")
    else:
        v_payload = None
    return ast.NotifyStmt(v_conditionname, v_payload)


cdef create_ListenStmt(structs.ListenStmt* data, offset_to_index):
    cdef object v_conditionname
    if data.conditionname is not NULL:
        v_conditionname = data.conditionname.decode("utf-8")
    else:
        v_conditionname = None
    return ast.ListenStmt(v_conditionname)


cdef create_UnlistenStmt(structs.UnlistenStmt* data, offset_to_index):
    cdef object v_conditionname
    if data.conditionname is not NULL:
        v_conditionname = data.conditionname.decode("utf-8")
    else:
        v_conditionname = None
    return ast.UnlistenStmt(v_conditionname)


cdef create_TransactionStmt(structs.TransactionStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'TransactionStmtKind')(data.kind)
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_savepoint_name
    if data.savepoint_name is not NULL:
        v_savepoint_name = data.savepoint_name.decode("utf-8")
    else:
        v_savepoint_name = None
    cdef object v_gid
    if data.gid is not NULL:
        v_gid = data.gid.decode("utf-8")
    else:
        v_gid = None
    cdef object v_chain = bool(data.chain)
    return ast.TransactionStmt(v_kind, v_options, v_savepoint_name, v_gid, v_chain)


cdef create_CompositeTypeStmt(structs.CompositeTypeStmt* data, offset_to_index):
    cdef object v_typevar
    if data.typevar is not NULL:
        v_typevar = create(data.typevar, offset_to_index)
    else:
        v_typevar = None
    cdef tuple v_coldeflist
    cdef int coldeflist_i
    if data.coldeflist is not NULL:
        v_coldeflist = PyTuple_New(data.coldeflist.length)
        for i in range(data.coldeflist.length):
            item = create(structs.list_nth(data.coldeflist, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_coldeflist, i, item)
    else:
        v_coldeflist = None
    return ast.CompositeTypeStmt(v_typevar, v_coldeflist)


cdef create_CreateEnumStmt(structs.CreateEnumStmt* data, offset_to_index):
    cdef tuple v_typeName
    cdef int typeName_i
    if data.typeName is not NULL:
        v_typeName = PyTuple_New(data.typeName.length)
        for i in range(data.typeName.length):
            item = create(structs.list_nth(data.typeName, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_typeName, i, item)
    else:
        v_typeName = None
    cdef tuple v_vals
    cdef int vals_i
    if data.vals is not NULL:
        v_vals = PyTuple_New(data.vals.length)
        for i in range(data.vals.length):
            item = create(structs.list_nth(data.vals, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_vals, i, item)
    else:
        v_vals = None
    return ast.CreateEnumStmt(v_typeName, v_vals)


cdef create_CreateRangeStmt(structs.CreateRangeStmt* data, offset_to_index):
    cdef tuple v_typeName
    cdef int typeName_i
    if data.typeName is not NULL:
        v_typeName = PyTuple_New(data.typeName.length)
        for i in range(data.typeName.length):
            item = create(structs.list_nth(data.typeName, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_typeName, i, item)
    else:
        v_typeName = None
    cdef tuple v_params
    cdef int params_i
    if data.params is not NULL:
        v_params = PyTuple_New(data.params.length)
        for i in range(data.params.length):
            item = create(structs.list_nth(data.params, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_params, i, item)
    else:
        v_params = None
    return ast.CreateRangeStmt(v_typeName, v_params)


cdef create_AlterEnumStmt(structs.AlterEnumStmt* data, offset_to_index):
    cdef tuple v_typeName
    cdef int typeName_i
    if data.typeName is not NULL:
        v_typeName = PyTuple_New(data.typeName.length)
        for i in range(data.typeName.length):
            item = create(structs.list_nth(data.typeName, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_typeName, i, item)
    else:
        v_typeName = None
    cdef object v_oldVal
    if data.oldVal is not NULL:
        v_oldVal = data.oldVal.decode("utf-8")
    else:
        v_oldVal = None
    cdef object v_newVal
    if data.newVal is not NULL:
        v_newVal = data.newVal.decode("utf-8")
    else:
        v_newVal = None
    cdef object v_newValNeighbor
    if data.newValNeighbor is not NULL:
        v_newValNeighbor = data.newValNeighbor.decode("utf-8")
    else:
        v_newValNeighbor = None
    cdef object v_newValIsAfter = bool(data.newValIsAfter)
    cdef object v_skipIfNewValExists = bool(data.skipIfNewValExists)
    return ast.AlterEnumStmt(v_typeName, v_oldVal, v_newVal, v_newValNeighbor, v_newValIsAfter, v_skipIfNewValExists)


cdef create_ViewStmt(structs.ViewStmt* data, offset_to_index):
    cdef object v_view
    if data.view is not NULL:
        v_view = create(data.view, offset_to_index)
    else:
        v_view = None
    cdef tuple v_aliases
    cdef int aliases_i
    if data.aliases is not NULL:
        v_aliases = PyTuple_New(data.aliases.length)
        for i in range(data.aliases.length):
            item = create(structs.list_nth(data.aliases, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_aliases, i, item)
    else:
        v_aliases = None
    cdef object v_query
    if data.query is not NULL:
        v_query = create(data.query, offset_to_index)
    else:
        v_query = None
    cdef object v_replace = bool(data.replace)
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_withCheckOption = getattr(enums, 'ViewCheckOption')(data.withCheckOption)
    return ast.ViewStmt(v_view, v_aliases, v_query, v_replace, v_options, v_withCheckOption)


cdef create_LoadStmt(structs.LoadStmt* data, offset_to_index):
    cdef object v_filename
    if data.filename is not NULL:
        v_filename = data.filename.decode("utf-8")
    else:
        v_filename = None
    return ast.LoadStmt(v_filename)


cdef create_CreatedbStmt(structs.CreatedbStmt* data, offset_to_index):
    cdef object v_dbname
    if data.dbname is not NULL:
        v_dbname = data.dbname.decode("utf-8")
    else:
        v_dbname = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreatedbStmt(v_dbname, v_options)


cdef create_AlterDatabaseStmt(structs.AlterDatabaseStmt* data, offset_to_index):
    cdef object v_dbname
    if data.dbname is not NULL:
        v_dbname = data.dbname.decode("utf-8")
    else:
        v_dbname = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.AlterDatabaseStmt(v_dbname, v_options)


cdef create_AlterDatabaseSetStmt(structs.AlterDatabaseSetStmt* data, offset_to_index):
    cdef object v_dbname
    if data.dbname is not NULL:
        v_dbname = data.dbname.decode("utf-8")
    else:
        v_dbname = None
    cdef object v_setstmt
    if data.setstmt is not NULL:
        v_setstmt = create(data.setstmt, offset_to_index)
    else:
        v_setstmt = None
    return ast.AlterDatabaseSetStmt(v_dbname, v_setstmt)


cdef create_DropdbStmt(structs.DropdbStmt* data, offset_to_index):
    cdef object v_dbname
    if data.dbname is not NULL:
        v_dbname = data.dbname.decode("utf-8")
    else:
        v_dbname = None
    cdef object v_missing_ok = bool(data.missing_ok)
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.DropdbStmt(v_dbname, v_missing_ok, v_options)


cdef create_AlterSystemStmt(structs.AlterSystemStmt* data, offset_to_index):
    cdef object v_setstmt
    if data.setstmt is not NULL:
        v_setstmt = create(data.setstmt, offset_to_index)
    else:
        v_setstmt = None
    return ast.AlterSystemStmt(v_setstmt)


cdef create_ClusterStmt(structs.ClusterStmt* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_indexname
    if data.indexname is not NULL:
        v_indexname = data.indexname.decode("utf-8")
    else:
        v_indexname = None
    cdef object v_options = data.options
    return ast.ClusterStmt(v_relation, v_indexname, v_options)


cdef create_VacuumStmt(structs.VacuumStmt* data, offset_to_index):
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef tuple v_rels
    cdef int rels_i
    if data.rels is not NULL:
        v_rels = PyTuple_New(data.rels.length)
        for i in range(data.rels.length):
            item = create(structs.list_nth(data.rels, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_rels, i, item)
    else:
        v_rels = None
    cdef object v_is_vacuumcmd = bool(data.is_vacuumcmd)
    return ast.VacuumStmt(v_options, v_rels, v_is_vacuumcmd)


cdef create_VacuumRelation(structs.VacuumRelation* data, offset_to_index):
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef tuple v_va_cols
    cdef int va_cols_i
    if data.va_cols is not NULL:
        v_va_cols = PyTuple_New(data.va_cols.length)
        for i in range(data.va_cols.length):
            item = create(structs.list_nth(data.va_cols, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_va_cols, i, item)
    else:
        v_va_cols = None
    return ast.VacuumRelation(v_relation, v_va_cols)


cdef create_ExplainStmt(structs.ExplainStmt* data, offset_to_index):
    cdef object v_query
    if data.query is not NULL:
        v_query = create(data.query, offset_to_index)
    else:
        v_query = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.ExplainStmt(v_query, v_options)


cdef create_CreateTableAsStmt(structs.CreateTableAsStmt* data, offset_to_index):
    cdef object v_query
    if data.query is not NULL:
        v_query = create(data.query, offset_to_index)
    else:
        v_query = None
    cdef object v_into
    if data.into is not NULL:
        v_into = create(data.into, offset_to_index)
    else:
        v_into = None
    cdef object v_relkind = getattr(enums, 'ObjectType')(data.relkind)
    cdef object v_is_select_into = bool(data.is_select_into)
    cdef object v_if_not_exists = bool(data.if_not_exists)
    return ast.CreateTableAsStmt(v_query, v_into, v_relkind, v_is_select_into, v_if_not_exists)


cdef create_RefreshMatViewStmt(structs.RefreshMatViewStmt* data, offset_to_index):
    cdef object v_concurrent = bool(data.concurrent)
    cdef object v_skipData = bool(data.skipData)
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    return ast.RefreshMatViewStmt(v_concurrent, v_skipData, v_relation)


cdef create_CheckPointStmt(structs.CheckPointStmt* data, offset_to_index):
    return ast.CheckPointStmt()


cdef create_DiscardStmt(structs.DiscardStmt* data, offset_to_index):
    cdef object v_target = getattr(enums, 'DiscardMode')(data.target)
    return ast.DiscardStmt(v_target)


cdef create_LockStmt(structs.LockStmt* data, offset_to_index):
    cdef tuple v_relations
    cdef int relations_i
    if data.relations is not NULL:
        v_relations = PyTuple_New(data.relations.length)
        for i in range(data.relations.length):
            item = create(structs.list_nth(data.relations, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_relations, i, item)
    else:
        v_relations = None
    cdef object v_mode = data.mode
    cdef object v_nowait = bool(data.nowait)
    return ast.LockStmt(v_relations, v_mode, v_nowait)


cdef create_ConstraintsSetStmt(structs.ConstraintsSetStmt* data, offset_to_index):
    cdef tuple v_constraints
    cdef int constraints_i
    if data.constraints is not NULL:
        v_constraints = PyTuple_New(data.constraints.length)
        for i in range(data.constraints.length):
            item = create(structs.list_nth(data.constraints, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_constraints, i, item)
    else:
        v_constraints = None
    cdef object v_deferred = bool(data.deferred)
    return ast.ConstraintsSetStmt(v_constraints, v_deferred)


cdef create_ReindexStmt(structs.ReindexStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'ReindexObjectType')(data.kind)
    cdef object v_relation
    if data.relation is not NULL:
        v_relation = create(data.relation, offset_to_index)
    else:
        v_relation = None
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_options = data.options
    cdef object v_concurrent = bool(data.concurrent)
    return ast.ReindexStmt(v_kind, v_relation, v_name, v_options, v_concurrent)


cdef create_CreateConversionStmt(structs.CreateConversionStmt* data, offset_to_index):
    cdef tuple v_conversion_name
    cdef int conversion_name_i
    if data.conversion_name is not NULL:
        v_conversion_name = PyTuple_New(data.conversion_name.length)
        for i in range(data.conversion_name.length):
            item = create(structs.list_nth(data.conversion_name, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_conversion_name, i, item)
    else:
        v_conversion_name = None
    cdef object v_for_encoding_name
    if data.for_encoding_name is not NULL:
        v_for_encoding_name = data.for_encoding_name.decode("utf-8")
    else:
        v_for_encoding_name = None
    cdef object v_to_encoding_name
    if data.to_encoding_name is not NULL:
        v_to_encoding_name = data.to_encoding_name.decode("utf-8")
    else:
        v_to_encoding_name = None
    cdef tuple v_func_name
    cdef int func_name_i
    if data.func_name is not NULL:
        v_func_name = PyTuple_New(data.func_name.length)
        for i in range(data.func_name.length):
            item = create(structs.list_nth(data.func_name, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_func_name, i, item)
    else:
        v_func_name = None
    cdef object v_def_ = bool(data.def_)
    return ast.CreateConversionStmt(v_conversion_name, v_for_encoding_name, v_to_encoding_name, v_func_name, v_def_)


cdef create_CreateCastStmt(structs.CreateCastStmt* data, offset_to_index):
    cdef object v_sourcetype
    if data.sourcetype is not NULL:
        v_sourcetype = create(data.sourcetype, offset_to_index)
    else:
        v_sourcetype = None
    cdef object v_targettype
    if data.targettype is not NULL:
        v_targettype = create(data.targettype, offset_to_index)
    else:
        v_targettype = None
    cdef object v_func
    if data.func is not NULL:
        v_func = create(data.func, offset_to_index)
    else:
        v_func = None
    cdef object v_context = getattr(enums, 'CoercionContext')(data.context)
    cdef object v_inout = bool(data.inout)
    return ast.CreateCastStmt(v_sourcetype, v_targettype, v_func, v_context, v_inout)


cdef create_CreateTransformStmt(structs.CreateTransformStmt* data, offset_to_index):
    cdef object v_replace = bool(data.replace)
    cdef object v_type_name
    if data.type_name is not NULL:
        v_type_name = create(data.type_name, offset_to_index)
    else:
        v_type_name = None
    cdef object v_lang
    if data.lang is not NULL:
        v_lang = data.lang.decode("utf-8")
    else:
        v_lang = None
    cdef object v_fromsql
    if data.fromsql is not NULL:
        v_fromsql = create(data.fromsql, offset_to_index)
    else:
        v_fromsql = None
    cdef object v_tosql
    if data.tosql is not NULL:
        v_tosql = create(data.tosql, offset_to_index)
    else:
        v_tosql = None
    return ast.CreateTransformStmt(v_replace, v_type_name, v_lang, v_fromsql, v_tosql)


cdef create_PrepareStmt(structs.PrepareStmt* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef tuple v_argtypes
    cdef int argtypes_i
    if data.argtypes is not NULL:
        v_argtypes = PyTuple_New(data.argtypes.length)
        for i in range(data.argtypes.length):
            item = create(structs.list_nth(data.argtypes, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_argtypes, i, item)
    else:
        v_argtypes = None
    cdef object v_query
    if data.query is not NULL:
        v_query = create(data.query, offset_to_index)
    else:
        v_query = None
    return ast.PrepareStmt(v_name, v_argtypes, v_query)


cdef create_ExecuteStmt(structs.ExecuteStmt* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef tuple v_params
    cdef int params_i
    if data.params is not NULL:
        v_params = PyTuple_New(data.params.length)
        for i in range(data.params.length):
            item = create(structs.list_nth(data.params, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_params, i, item)
    else:
        v_params = None
    return ast.ExecuteStmt(v_name, v_params)


cdef create_DeallocateStmt(structs.DeallocateStmt* data, offset_to_index):
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    return ast.DeallocateStmt(v_name)


cdef create_DropOwnedStmt(structs.DropOwnedStmt* data, offset_to_index):
    cdef tuple v_roles
    cdef int roles_i
    if data.roles is not NULL:
        v_roles = PyTuple_New(data.roles.length)
        for i in range(data.roles.length):
            item = create(structs.list_nth(data.roles, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_roles, i, item)
    else:
        v_roles = None
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.DropOwnedStmt(v_roles, v_behavior)


cdef create_ReassignOwnedStmt(structs.ReassignOwnedStmt* data, offset_to_index):
    cdef tuple v_roles
    cdef int roles_i
    if data.roles is not NULL:
        v_roles = PyTuple_New(data.roles.length)
        for i in range(data.roles.length):
            item = create(structs.list_nth(data.roles, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_roles, i, item)
    else:
        v_roles = None
    cdef object v_newrole
    if data.newrole is not NULL:
        v_newrole = create(data.newrole, offset_to_index)
    else:
        v_newrole = None
    return ast.ReassignOwnedStmt(v_roles, v_newrole)


cdef create_AlterTSDictionaryStmt(structs.AlterTSDictionaryStmt* data, offset_to_index):
    cdef tuple v_dictname
    cdef int dictname_i
    if data.dictname is not NULL:
        v_dictname = PyTuple_New(data.dictname.length)
        for i in range(data.dictname.length):
            item = create(structs.list_nth(data.dictname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_dictname, i, item)
    else:
        v_dictname = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.AlterTSDictionaryStmt(v_dictname, v_options)


cdef create_AlterTSConfigurationStmt(structs.AlterTSConfigurationStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'AlterTSConfigType')(data.kind)
    cdef tuple v_cfgname
    cdef int cfgname_i
    if data.cfgname is not NULL:
        v_cfgname = PyTuple_New(data.cfgname.length)
        for i in range(data.cfgname.length):
            item = create(structs.list_nth(data.cfgname, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_cfgname, i, item)
    else:
        v_cfgname = None
    cdef tuple v_tokentype
    cdef int tokentype_i
    if data.tokentype is not NULL:
        v_tokentype = PyTuple_New(data.tokentype.length)
        for i in range(data.tokentype.length):
            item = create(structs.list_nth(data.tokentype, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_tokentype, i, item)
    else:
        v_tokentype = None
    cdef tuple v_dicts
    cdef int dicts_i
    if data.dicts is not NULL:
        v_dicts = PyTuple_New(data.dicts.length)
        for i in range(data.dicts.length):
            item = create(structs.list_nth(data.dicts, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_dicts, i, item)
    else:
        v_dicts = None
    cdef object v_override = bool(data.override)
    cdef object v_replace = bool(data.replace)
    cdef object v_missing_ok = bool(data.missing_ok)
    return ast.AlterTSConfigurationStmt(v_kind, v_cfgname, v_tokentype, v_dicts, v_override, v_replace, v_missing_ok)


cdef create_CreatePublicationStmt(structs.CreatePublicationStmt* data, offset_to_index):
    cdef object v_pubname
    if data.pubname is not NULL:
        v_pubname = data.pubname.decode("utf-8")
    else:
        v_pubname = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef tuple v_tables
    cdef int tables_i
    if data.tables is not NULL:
        v_tables = PyTuple_New(data.tables.length)
        for i in range(data.tables.length):
            item = create(structs.list_nth(data.tables, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_tables, i, item)
    else:
        v_tables = None
    cdef object v_for_all_tables = bool(data.for_all_tables)
    return ast.CreatePublicationStmt(v_pubname, v_options, v_tables, v_for_all_tables)


cdef create_AlterPublicationStmt(structs.AlterPublicationStmt* data, offset_to_index):
    cdef object v_pubname
    if data.pubname is not NULL:
        v_pubname = data.pubname.decode("utf-8")
    else:
        v_pubname = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef tuple v_tables
    cdef int tables_i
    if data.tables is not NULL:
        v_tables = PyTuple_New(data.tables.length)
        for i in range(data.tables.length):
            item = create(structs.list_nth(data.tables, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_tables, i, item)
    else:
        v_tables = None
    cdef object v_for_all_tables = bool(data.for_all_tables)
    cdef object v_tableAction = getattr(enums, 'DefElemAction')(data.tableAction)
    return ast.AlterPublicationStmt(v_pubname, v_options, v_tables, v_for_all_tables, v_tableAction)


cdef create_CreateSubscriptionStmt(structs.CreateSubscriptionStmt* data, offset_to_index):
    cdef object v_subname
    if data.subname is not NULL:
        v_subname = data.subname.decode("utf-8")
    else:
        v_subname = None
    cdef object v_conninfo
    if data.conninfo is not NULL:
        v_conninfo = data.conninfo.decode("utf-8")
    else:
        v_conninfo = None
    cdef tuple v_publication
    cdef int publication_i
    if data.publication is not NULL:
        v_publication = PyTuple_New(data.publication.length)
        for i in range(data.publication.length):
            item = create(structs.list_nth(data.publication, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_publication, i, item)
    else:
        v_publication = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.CreateSubscriptionStmt(v_subname, v_conninfo, v_publication, v_options)


cdef create_AlterSubscriptionStmt(structs.AlterSubscriptionStmt* data, offset_to_index):
    cdef object v_kind = getattr(enums, 'AlterSubscriptionType')(data.kind)
    cdef object v_subname
    if data.subname is not NULL:
        v_subname = data.subname.decode("utf-8")
    else:
        v_subname = None
    cdef object v_conninfo
    if data.conninfo is not NULL:
        v_conninfo = data.conninfo.decode("utf-8")
    else:
        v_conninfo = None
    cdef tuple v_publication
    cdef int publication_i
    if data.publication is not NULL:
        v_publication = PyTuple_New(data.publication.length)
        for i in range(data.publication.length):
            item = create(structs.list_nth(data.publication, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_publication, i, item)
    else:
        v_publication = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    return ast.AlterSubscriptionStmt(v_kind, v_subname, v_conninfo, v_publication, v_options)


cdef create_DropSubscriptionStmt(structs.DropSubscriptionStmt* data, offset_to_index):
    cdef object v_subname
    if data.subname is not NULL:
        v_subname = data.subname.decode("utf-8")
    else:
        v_subname = None
    cdef object v_missing_ok = bool(data.missing_ok)
    cdef object v_behavior = getattr(enums, 'DropBehavior')(data.behavior)
    return ast.DropSubscriptionStmt(v_subname, v_missing_ok, v_behavior)


cdef create_Alias(structs.Alias* data, offset_to_index):
    cdef object v_aliasname
    if data.aliasname is not NULL:
        v_aliasname = data.aliasname.decode("utf-8")
    else:
        v_aliasname = None
    cdef tuple v_colnames
    cdef int colnames_i
    if data.colnames is not NULL:
        v_colnames = PyTuple_New(data.colnames.length)
        for i in range(data.colnames.length):
            item = create(structs.list_nth(data.colnames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colnames, i, item)
    else:
        v_colnames = None
    return ast.Alias(v_aliasname, v_colnames)


cdef create_RangeVar(structs.RangeVar* data, offset_to_index):
    cdef object v_catalogname
    if data.catalogname is not NULL:
        v_catalogname = data.catalogname.decode("utf-8")
    else:
        v_catalogname = None
    cdef object v_schemaname
    if data.schemaname is not NULL:
        v_schemaname = data.schemaname.decode("utf-8")
    else:
        v_schemaname = None
    cdef object v_relname
    if data.relname is not NULL:
        v_relname = data.relname.decode("utf-8")
    else:
        v_relname = None
    cdef object v_inh = bool(data.inh)
    cdef object v_relpersistence = chr(data.relpersistence)
    cdef object v_alias
    if data.alias is not NULL:
        v_alias = create(data.alias, offset_to_index)
    else:
        v_alias = None
    cdef object v_location = offset_to_index(data.location)
    return ast.RangeVar(v_catalogname, v_schemaname, v_relname, v_inh, v_relpersistence, v_alias, v_location)


cdef create_TableFunc(structs.TableFunc* data, offset_to_index):
    cdef tuple v_ns_uris
    cdef int ns_uris_i
    if data.ns_uris is not NULL:
        v_ns_uris = PyTuple_New(data.ns_uris.length)
        for i in range(data.ns_uris.length):
            item = create(structs.list_nth(data.ns_uris, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_ns_uris, i, item)
    else:
        v_ns_uris = None
    cdef tuple v_ns_names
    cdef int ns_names_i
    if data.ns_names is not NULL:
        v_ns_names = PyTuple_New(data.ns_names.length)
        for i in range(data.ns_names.length):
            item = create(structs.list_nth(data.ns_names, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_ns_names, i, item)
    else:
        v_ns_names = None
    cdef object v_docexpr
    if data.docexpr is not NULL:
        v_docexpr = create(data.docexpr, offset_to_index)
    else:
        v_docexpr = None
    cdef object v_rowexpr
    if data.rowexpr is not NULL:
        v_rowexpr = create(data.rowexpr, offset_to_index)
    else:
        v_rowexpr = None
    cdef tuple v_colnames
    cdef int colnames_i
    if data.colnames is not NULL:
        v_colnames = PyTuple_New(data.colnames.length)
        for i in range(data.colnames.length):
            item = create(structs.list_nth(data.colnames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colnames, i, item)
    else:
        v_colnames = None
    cdef tuple v_coltypes
    cdef int coltypes_i
    if data.coltypes is not NULL:
        v_coltypes = PyTuple_New(data.coltypes.length)
        for i in range(data.coltypes.length):
            item = create(structs.list_nth(data.coltypes, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_coltypes, i, item)
    else:
        v_coltypes = None
    cdef tuple v_coltypmods
    cdef int coltypmods_i
    if data.coltypmods is not NULL:
        v_coltypmods = PyTuple_New(data.coltypmods.length)
        for i in range(data.coltypmods.length):
            item = create(structs.list_nth(data.coltypmods, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_coltypmods, i, item)
    else:
        v_coltypmods = None
    cdef tuple v_colcollations
    cdef int colcollations_i
    if data.colcollations is not NULL:
        v_colcollations = PyTuple_New(data.colcollations.length)
        for i in range(data.colcollations.length):
            item = create(structs.list_nth(data.colcollations, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colcollations, i, item)
    else:
        v_colcollations = None
    cdef tuple v_colexprs
    cdef int colexprs_i
    if data.colexprs is not NULL:
        v_colexprs = PyTuple_New(data.colexprs.length)
        for i in range(data.colexprs.length):
            item = create(structs.list_nth(data.colexprs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colexprs, i, item)
    else:
        v_colexprs = None
    cdef tuple v_coldefexprs
    cdef int coldefexprs_i
    if data.coldefexprs is not NULL:
        v_coldefexprs = PyTuple_New(data.coldefexprs.length)
        for i in range(data.coldefexprs.length):
            item = create(structs.list_nth(data.coldefexprs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_coldefexprs, i, item)
    else:
        v_coldefexprs = None
    cdef set v_notnulls
    cdef int notnulls_member
    if data.notnulls is not NULL:
        v_notnulls = set()
        notnulls_member = structs.bms_next_member(data.notnulls, -1)
        while notnulls_member >= 0:
            v_notnulls.add(notnulls_member)
            notnulls_member = structs.bms_next_member(data.notnulls, notnulls_member)
    else:
        v_notnulls = None
    cdef object v_ordinalitycol = data.ordinalitycol
    cdef object v_location = offset_to_index(data.location)
    return ast.TableFunc(v_ns_uris, v_ns_names, v_docexpr, v_rowexpr, v_colnames, v_coltypes, v_coltypmods, v_colcollations, v_colexprs, v_coldefexprs, v_notnulls, v_ordinalitycol, v_location)


cdef create_IntoClause(structs.IntoClause* data, offset_to_index):
    cdef object v_rel
    if data.rel is not NULL:
        v_rel = create(data.rel, offset_to_index)
    else:
        v_rel = None
    cdef tuple v_colNames
    cdef int colNames_i
    if data.colNames is not NULL:
        v_colNames = PyTuple_New(data.colNames.length)
        for i in range(data.colNames.length):
            item = create(structs.list_nth(data.colNames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colNames, i, item)
    else:
        v_colNames = None
    cdef object v_accessMethod
    if data.accessMethod is not NULL:
        v_accessMethod = data.accessMethod.decode("utf-8")
    else:
        v_accessMethod = None
    cdef tuple v_options
    cdef int options_i
    if data.options is not NULL:
        v_options = PyTuple_New(data.options.length)
        for i in range(data.options.length):
            item = create(structs.list_nth(data.options, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_options, i, item)
    else:
        v_options = None
    cdef object v_onCommit = getattr(enums, 'OnCommitAction')(data.onCommit)
    cdef object v_tableSpaceName
    if data.tableSpaceName is not NULL:
        v_tableSpaceName = data.tableSpaceName.decode("utf-8")
    else:
        v_tableSpaceName = None
    cdef object v_viewQuery
    if data.viewQuery is not NULL:
        v_viewQuery = create(data.viewQuery, offset_to_index)
    else:
        v_viewQuery = None
    cdef object v_skipData = bool(data.skipData)
    return ast.IntoClause(v_rel, v_colNames, v_accessMethod, v_options, v_onCommit, v_tableSpaceName, v_viewQuery, v_skipData)


cdef create_Expr(structs.Expr* data, offset_to_index):
    return ast.Expr()


cdef create_Var(structs.Var* data, offset_to_index):
    cdef object v_varno = data.varno
    cdef object v_varattno = data.varattno
    cdef object v_vartypmod = data.vartypmod
    cdef object v_varlevelsup = data.varlevelsup
    cdef object v_varnosyn = data.varnosyn
    cdef object v_varattnosyn = data.varattnosyn
    cdef object v_location = offset_to_index(data.location)
    return ast.Var(v_varno, v_varattno, v_vartypmod, v_varlevelsup, v_varnosyn, v_varattnosyn, v_location)


cdef create_Param(structs.Param* data, offset_to_index):
    cdef object v_paramkind = getattr(enums, 'ParamKind')(data.paramkind)
    cdef object v_paramid = data.paramid
    cdef object v_paramtypmod = data.paramtypmod
    cdef object v_location = offset_to_index(data.location)
    return ast.Param(v_paramkind, v_paramid, v_paramtypmod, v_location)


cdef create_Aggref(structs.Aggref* data, offset_to_index):
    cdef tuple v_aggargtypes
    cdef int aggargtypes_i
    if data.aggargtypes is not NULL:
        v_aggargtypes = PyTuple_New(data.aggargtypes.length)
        for i in range(data.aggargtypes.length):
            item = create(structs.list_nth(data.aggargtypes, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_aggargtypes, i, item)
    else:
        v_aggargtypes = None
    cdef tuple v_aggdirectargs
    cdef int aggdirectargs_i
    if data.aggdirectargs is not NULL:
        v_aggdirectargs = PyTuple_New(data.aggdirectargs.length)
        for i in range(data.aggdirectargs.length):
            item = create(structs.list_nth(data.aggdirectargs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_aggdirectargs, i, item)
    else:
        v_aggdirectargs = None
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef tuple v_aggorder
    cdef int aggorder_i
    if data.aggorder is not NULL:
        v_aggorder = PyTuple_New(data.aggorder.length)
        for i in range(data.aggorder.length):
            item = create(structs.list_nth(data.aggorder, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_aggorder, i, item)
    else:
        v_aggorder = None
    cdef tuple v_aggdistinct
    cdef int aggdistinct_i
    if data.aggdistinct is not NULL:
        v_aggdistinct = PyTuple_New(data.aggdistinct.length)
        for i in range(data.aggdistinct.length):
            item = create(structs.list_nth(data.aggdistinct, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_aggdistinct, i, item)
    else:
        v_aggdistinct = None
    cdef object v_aggfilter
    if data.aggfilter is not NULL:
        v_aggfilter = create(data.aggfilter, offset_to_index)
    else:
        v_aggfilter = None
    cdef object v_aggstar = bool(data.aggstar)
    cdef object v_aggvariadic = bool(data.aggvariadic)
    cdef object v_aggkind = chr(data.aggkind)
    cdef object v_agglevelsup = data.agglevelsup
    cdef object v_aggsplit = getattr(enums, 'AggSplit')(data.aggsplit)
    cdef object v_location = offset_to_index(data.location)
    return ast.Aggref(v_aggargtypes, v_aggdirectargs, v_args, v_aggorder, v_aggdistinct, v_aggfilter, v_aggstar, v_aggvariadic, v_aggkind, v_agglevelsup, v_aggsplit, v_location)


cdef create_GroupingFunc(structs.GroupingFunc* data, offset_to_index):
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef tuple v_refs
    cdef int refs_i
    if data.refs is not NULL:
        v_refs = PyTuple_New(data.refs.length)
        for i in range(data.refs.length):
            item = create(structs.list_nth(data.refs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_refs, i, item)
    else:
        v_refs = None
    cdef tuple v_cols
    cdef int cols_i
    if data.cols is not NULL:
        v_cols = PyTuple_New(data.cols.length)
        for i in range(data.cols.length):
            item = create(structs.list_nth(data.cols, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_cols, i, item)
    else:
        v_cols = None
    cdef object v_agglevelsup = data.agglevelsup
    cdef object v_location = offset_to_index(data.location)
    return ast.GroupingFunc(v_args, v_refs, v_cols, v_agglevelsup, v_location)


cdef create_WindowFunc(structs.WindowFunc* data, offset_to_index):
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_aggfilter
    if data.aggfilter is not NULL:
        v_aggfilter = create(data.aggfilter, offset_to_index)
    else:
        v_aggfilter = None
    cdef object v_winref = data.winref
    cdef object v_winstar = bool(data.winstar)
    cdef object v_winagg = bool(data.winagg)
    cdef object v_location = offset_to_index(data.location)
    return ast.WindowFunc(v_args, v_aggfilter, v_winref, v_winstar, v_winagg, v_location)


cdef create_SubscriptingRef(structs.SubscriptingRef* data, offset_to_index):
    cdef object v_reftypmod = data.reftypmod
    cdef tuple v_refupperindexpr
    cdef int refupperindexpr_i
    if data.refupperindexpr is not NULL:
        v_refupperindexpr = PyTuple_New(data.refupperindexpr.length)
        for i in range(data.refupperindexpr.length):
            item = create(structs.list_nth(data.refupperindexpr, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_refupperindexpr, i, item)
    else:
        v_refupperindexpr = None
    cdef tuple v_reflowerindexpr
    cdef int reflowerindexpr_i
    if data.reflowerindexpr is not NULL:
        v_reflowerindexpr = PyTuple_New(data.reflowerindexpr.length)
        for i in range(data.reflowerindexpr.length):
            item = create(structs.list_nth(data.reflowerindexpr, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_reflowerindexpr, i, item)
    else:
        v_reflowerindexpr = None
    cdef object v_refexpr
    if data.refexpr is not NULL:
        v_refexpr = create(data.refexpr, offset_to_index)
    else:
        v_refexpr = None
    cdef object v_refassgnexpr
    if data.refassgnexpr is not NULL:
        v_refassgnexpr = create(data.refassgnexpr, offset_to_index)
    else:
        v_refassgnexpr = None
    return ast.SubscriptingRef(v_reftypmod, v_refupperindexpr, v_reflowerindexpr, v_refexpr, v_refassgnexpr)


cdef create_FuncExpr(structs.FuncExpr* data, offset_to_index):
    cdef object v_funcretset = bool(data.funcretset)
    cdef object v_funcvariadic = bool(data.funcvariadic)
    cdef object v_funcformat = getattr(enums, 'CoercionForm')(data.funcformat)
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_location = offset_to_index(data.location)
    return ast.FuncExpr(v_funcretset, v_funcvariadic, v_funcformat, v_args, v_location)


cdef create_NamedArgExpr(structs.NamedArgExpr* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef object v_argnumber = data.argnumber
    cdef object v_location = offset_to_index(data.location)
    return ast.NamedArgExpr(v_arg, v_name, v_argnumber, v_location)


cdef create_OpExpr(structs.OpExpr* data, offset_to_index):
    cdef object v_opretset = bool(data.opretset)
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_location = offset_to_index(data.location)
    return ast.OpExpr(v_opretset, v_args, v_location)


cdef create_ScalarArrayOpExpr(structs.ScalarArrayOpExpr* data, offset_to_index):
    cdef object v_useOr = bool(data.useOr)
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_location = offset_to_index(data.location)
    return ast.ScalarArrayOpExpr(v_useOr, v_args, v_location)


cdef create_BoolExpr(structs.BoolExpr* data, offset_to_index):
    cdef object v_boolop = getattr(enums, 'BoolExprType')(data.boolop)
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_location = offset_to_index(data.location)
    return ast.BoolExpr(v_boolop, v_args, v_location)


cdef create_SubLink(structs.SubLink* data, offset_to_index):
    cdef object v_subLinkType = getattr(enums, 'SubLinkType')(data.subLinkType)
    cdef object v_subLinkId = data.subLinkId
    cdef object v_testexpr
    if data.testexpr is not NULL:
        v_testexpr = create(data.testexpr, offset_to_index)
    else:
        v_testexpr = None
    cdef tuple v_operName
    cdef int operName_i
    if data.operName is not NULL:
        v_operName = PyTuple_New(data.operName.length)
        for i in range(data.operName.length):
            item = create(structs.list_nth(data.operName, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_operName, i, item)
    else:
        v_operName = None
    cdef object v_subselect
    if data.subselect is not NULL:
        v_subselect = create(data.subselect, offset_to_index)
    else:
        v_subselect = None
    cdef object v_location = offset_to_index(data.location)
    return ast.SubLink(v_subLinkType, v_subLinkId, v_testexpr, v_operName, v_subselect, v_location)


cdef create_SubPlan(structs.SubPlan* data, offset_to_index):
    cdef object v_subLinkType = getattr(enums, 'SubLinkType')(data.subLinkType)
    cdef object v_testexpr
    if data.testexpr is not NULL:
        v_testexpr = create(data.testexpr, offset_to_index)
    else:
        v_testexpr = None
    cdef tuple v_paramIds
    cdef int paramIds_i
    if data.paramIds is not NULL:
        v_paramIds = PyTuple_New(data.paramIds.length)
        for i in range(data.paramIds.length):
            item = create(structs.list_nth(data.paramIds, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_paramIds, i, item)
    else:
        v_paramIds = None
    cdef object v_plan_id = data.plan_id
    cdef object v_plan_name
    if data.plan_name is not NULL:
        v_plan_name = data.plan_name.decode("utf-8")
    else:
        v_plan_name = None
    cdef object v_firstColTypmod = data.firstColTypmod
    cdef object v_useHashTable = bool(data.useHashTable)
    cdef object v_unknownEqFalse = bool(data.unknownEqFalse)
    cdef object v_parallel_safe = bool(data.parallel_safe)
    cdef tuple v_setParam
    cdef int setParam_i
    if data.setParam is not NULL:
        v_setParam = PyTuple_New(data.setParam.length)
        for i in range(data.setParam.length):
            item = create(structs.list_nth(data.setParam, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_setParam, i, item)
    else:
        v_setParam = None
    cdef tuple v_parParam
    cdef int parParam_i
    if data.parParam is not NULL:
        v_parParam = PyTuple_New(data.parParam.length)
        for i in range(data.parParam.length):
            item = create(structs.list_nth(data.parParam, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_parParam, i, item)
    else:
        v_parParam = None
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_startup_cost = data.startup_cost
    cdef object v_per_call_cost = data.per_call_cost
    return ast.SubPlan(v_subLinkType, v_testexpr, v_paramIds, v_plan_id, v_plan_name, v_firstColTypmod, v_useHashTable, v_unknownEqFalse, v_parallel_safe, v_setParam, v_parParam, v_args, v_startup_cost, v_per_call_cost)


cdef create_AlternativeSubPlan(structs.AlternativeSubPlan* data, offset_to_index):
    cdef tuple v_subplans
    cdef int subplans_i
    if data.subplans is not NULL:
        v_subplans = PyTuple_New(data.subplans.length)
        for i in range(data.subplans.length):
            item = create(structs.list_nth(data.subplans, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_subplans, i, item)
    else:
        v_subplans = None
    return ast.AlternativeSubPlan(v_subplans)


cdef create_FieldSelect(structs.FieldSelect* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_fieldnum = data.fieldnum
    cdef object v_resulttypmod = data.resulttypmod
    return ast.FieldSelect(v_arg, v_fieldnum, v_resulttypmod)


cdef create_FieldStore(structs.FieldStore* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef tuple v_newvals
    cdef int newvals_i
    if data.newvals is not NULL:
        v_newvals = PyTuple_New(data.newvals.length)
        for i in range(data.newvals.length):
            item = create(structs.list_nth(data.newvals, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_newvals, i, item)
    else:
        v_newvals = None
    cdef tuple v_fieldnums
    cdef int fieldnums_i
    if data.fieldnums is not NULL:
        v_fieldnums = PyTuple_New(data.fieldnums.length)
        for i in range(data.fieldnums.length):
            item = create(structs.list_nth(data.fieldnums, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_fieldnums, i, item)
    else:
        v_fieldnums = None
    return ast.FieldStore(v_arg, v_newvals, v_fieldnums)


cdef create_RelabelType(structs.RelabelType* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_resulttypmod = data.resulttypmod
    cdef object v_relabelformat = getattr(enums, 'CoercionForm')(data.relabelformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.RelabelType(v_arg, v_resulttypmod, v_relabelformat, v_location)


cdef create_CoerceViaIO(structs.CoerceViaIO* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_coerceformat = getattr(enums, 'CoercionForm')(data.coerceformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.CoerceViaIO(v_arg, v_coerceformat, v_location)


cdef create_ArrayCoerceExpr(structs.ArrayCoerceExpr* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_elemexpr
    if data.elemexpr is not NULL:
        v_elemexpr = create(data.elemexpr, offset_to_index)
    else:
        v_elemexpr = None
    cdef object v_resulttypmod = data.resulttypmod
    cdef object v_coerceformat = getattr(enums, 'CoercionForm')(data.coerceformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.ArrayCoerceExpr(v_arg, v_elemexpr, v_resulttypmod, v_coerceformat, v_location)


cdef create_ConvertRowtypeExpr(structs.ConvertRowtypeExpr* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_convertformat = getattr(enums, 'CoercionForm')(data.convertformat)
    cdef object v_location = offset_to_index(data.location)
    return ast.ConvertRowtypeExpr(v_arg, v_convertformat, v_location)


cdef create_CollateExpr(structs.CollateExpr* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_location = offset_to_index(data.location)
    return ast.CollateExpr(v_arg, v_location)


cdef create_CaseExpr(structs.CaseExpr* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_defresult
    if data.defresult is not NULL:
        v_defresult = create(data.defresult, offset_to_index)
    else:
        v_defresult = None
    cdef object v_location = offset_to_index(data.location)
    return ast.CaseExpr(v_arg, v_args, v_defresult, v_location)


cdef create_CaseWhen(structs.CaseWhen* data, offset_to_index):
    cdef object v_expr
    if data.expr is not NULL:
        v_expr = create(data.expr, offset_to_index)
    else:
        v_expr = None
    cdef object v_result
    if data.result is not NULL:
        v_result = create(data.result, offset_to_index)
    else:
        v_result = None
    cdef object v_location = offset_to_index(data.location)
    return ast.CaseWhen(v_expr, v_result, v_location)


cdef create_CaseTestExpr(structs.CaseTestExpr* data, offset_to_index):
    cdef object v_typeMod = data.typeMod
    return ast.CaseTestExpr(v_typeMod)


cdef create_ArrayExpr(structs.ArrayExpr* data, offset_to_index):
    cdef tuple v_elements
    cdef int elements_i
    if data.elements is not NULL:
        v_elements = PyTuple_New(data.elements.length)
        for i in range(data.elements.length):
            item = create(structs.list_nth(data.elements, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_elements, i, item)
    else:
        v_elements = None
    cdef object v_multidims = bool(data.multidims)
    cdef object v_location = offset_to_index(data.location)
    return ast.ArrayExpr(v_elements, v_multidims, v_location)


cdef create_RowExpr(structs.RowExpr* data, offset_to_index):
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_row_format = getattr(enums, 'CoercionForm')(data.row_format)
    cdef tuple v_colnames
    cdef int colnames_i
    if data.colnames is not NULL:
        v_colnames = PyTuple_New(data.colnames.length)
        for i in range(data.colnames.length):
            item = create(structs.list_nth(data.colnames, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_colnames, i, item)
    else:
        v_colnames = None
    cdef object v_location = offset_to_index(data.location)
    return ast.RowExpr(v_args, v_row_format, v_colnames, v_location)


cdef create_RowCompareExpr(structs.RowCompareExpr* data, offset_to_index):
    cdef object v_rctype = getattr(enums, 'RowCompareType')(data.rctype)
    cdef tuple v_opnos
    cdef int opnos_i
    if data.opnos is not NULL:
        v_opnos = PyTuple_New(data.opnos.length)
        for i in range(data.opnos.length):
            item = create(structs.list_nth(data.opnos, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_opnos, i, item)
    else:
        v_opnos = None
    cdef tuple v_opfamilies
    cdef int opfamilies_i
    if data.opfamilies is not NULL:
        v_opfamilies = PyTuple_New(data.opfamilies.length)
        for i in range(data.opfamilies.length):
            item = create(structs.list_nth(data.opfamilies, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_opfamilies, i, item)
    else:
        v_opfamilies = None
    cdef tuple v_inputcollids
    cdef int inputcollids_i
    if data.inputcollids is not NULL:
        v_inputcollids = PyTuple_New(data.inputcollids.length)
        for i in range(data.inputcollids.length):
            item = create(structs.list_nth(data.inputcollids, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_inputcollids, i, item)
    else:
        v_inputcollids = None
    cdef tuple v_largs
    cdef int largs_i
    if data.largs is not NULL:
        v_largs = PyTuple_New(data.largs.length)
        for i in range(data.largs.length):
            item = create(structs.list_nth(data.largs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_largs, i, item)
    else:
        v_largs = None
    cdef tuple v_rargs
    cdef int rargs_i
    if data.rargs is not NULL:
        v_rargs = PyTuple_New(data.rargs.length)
        for i in range(data.rargs.length):
            item = create(structs.list_nth(data.rargs, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_rargs, i, item)
    else:
        v_rargs = None
    return ast.RowCompareExpr(v_rctype, v_opnos, v_opfamilies, v_inputcollids, v_largs, v_rargs)


cdef create_CoalesceExpr(structs.CoalesceExpr* data, offset_to_index):
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_location = offset_to_index(data.location)
    return ast.CoalesceExpr(v_args, v_location)


cdef create_MinMaxExpr(structs.MinMaxExpr* data, offset_to_index):
    cdef object v_op = getattr(enums, 'MinMaxOp')(data.op)
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_location = offset_to_index(data.location)
    return ast.MinMaxExpr(v_op, v_args, v_location)


cdef create_SQLValueFunction(structs.SQLValueFunction* data, offset_to_index):
    cdef object v_op = getattr(enums, 'SQLValueFunctionOp')(data.op)
    cdef object v_typmod = data.typmod
    cdef object v_location = offset_to_index(data.location)
    return ast.SQLValueFunction(v_op, v_typmod, v_location)


cdef create_XmlExpr(structs.XmlExpr* data, offset_to_index):
    cdef object v_op = getattr(enums, 'XmlExprOp')(data.op)
    cdef object v_name
    if data.name is not NULL:
        v_name = data.name.decode("utf-8")
    else:
        v_name = None
    cdef tuple v_named_args
    cdef int named_args_i
    if data.named_args is not NULL:
        v_named_args = PyTuple_New(data.named_args.length)
        for i in range(data.named_args.length):
            item = create(structs.list_nth(data.named_args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_named_args, i, item)
    else:
        v_named_args = None
    cdef tuple v_arg_names
    cdef int arg_names_i
    if data.arg_names is not NULL:
        v_arg_names = PyTuple_New(data.arg_names.length)
        for i in range(data.arg_names.length):
            item = create(structs.list_nth(data.arg_names, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_arg_names, i, item)
    else:
        v_arg_names = None
    cdef tuple v_args
    cdef int args_i
    if data.args is not NULL:
        v_args = PyTuple_New(data.args.length)
        for i in range(data.args.length):
            item = create(structs.list_nth(data.args, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_args, i, item)
    else:
        v_args = None
    cdef object v_xmloption = getattr(enums, 'XmlOptionType')(data.xmloption)
    cdef object v_typmod = data.typmod
    cdef object v_location = offset_to_index(data.location)
    return ast.XmlExpr(v_op, v_name, v_named_args, v_arg_names, v_args, v_xmloption, v_typmod, v_location)


cdef create_NullTest(structs.NullTest* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_nulltesttype = getattr(enums, 'NullTestType')(data.nulltesttype)
    cdef object v_argisrow = bool(data.argisrow)
    cdef object v_location = offset_to_index(data.location)
    return ast.NullTest(v_arg, v_nulltesttype, v_argisrow, v_location)


cdef create_BooleanTest(structs.BooleanTest* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
    cdef object v_booltesttype = getattr(enums, 'BoolTestType')(data.booltesttype)
    cdef object v_location = offset_to_index(data.location)
    return ast.BooleanTest(v_arg, v_booltesttype, v_location)


cdef create_CoerceToDomain(structs.CoerceToDomain* data, offset_to_index):
    cdef object v_arg
    if data.arg is not NULL:
        v_arg = create(data.arg, offset_to_index)
    else:
        v_arg = None
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
    cdef object v_cursor_name
    if data.cursor_name is not NULL:
        v_cursor_name = data.cursor_name.decode("utf-8")
    else:
        v_cursor_name = None
    cdef object v_cursor_param = data.cursor_param
    return ast.CurrentOfExpr(v_cvarno, v_cursor_name, v_cursor_param)


cdef create_InferenceElem(structs.InferenceElem* data, offset_to_index):
    cdef object v_expr
    if data.expr is not NULL:
        v_expr = create(data.expr, offset_to_index)
    else:
        v_expr = None
    return ast.InferenceElem(v_expr)


cdef create_TargetEntry(structs.TargetEntry* data, offset_to_index):
    cdef object v_expr
    if data.expr is not NULL:
        v_expr = create(data.expr, offset_to_index)
    else:
        v_expr = None
    cdef object v_resno = data.resno
    cdef object v_resname
    if data.resname is not NULL:
        v_resname = data.resname.decode("utf-8")
    else:
        v_resname = None
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
    cdef object v_larg
    if data.larg is not NULL:
        v_larg = create(data.larg, offset_to_index)
    else:
        v_larg = None
    cdef object v_rarg
    if data.rarg is not NULL:
        v_rarg = create(data.rarg, offset_to_index)
    else:
        v_rarg = None
    cdef tuple v_usingClause
    cdef int usingClause_i
    if data.usingClause is not NULL:
        v_usingClause = PyTuple_New(data.usingClause.length)
        for i in range(data.usingClause.length):
            item = create(structs.list_nth(data.usingClause, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_usingClause, i, item)
    else:
        v_usingClause = None
    cdef object v_quals
    if data.quals is not NULL:
        v_quals = create(data.quals, offset_to_index)
    else:
        v_quals = None
    cdef object v_alias
    if data.alias is not NULL:
        v_alias = create(data.alias, offset_to_index)
    else:
        v_alias = None
    cdef object v_rtindex = data.rtindex
    return ast.JoinExpr(v_jointype, v_isNatural, v_larg, v_rarg, v_usingClause, v_quals, v_alias, v_rtindex)


cdef create_FromExpr(structs.FromExpr* data, offset_to_index):
    cdef tuple v_fromlist
    cdef int fromlist_i
    if data.fromlist is not NULL:
        v_fromlist = PyTuple_New(data.fromlist.length)
        for i in range(data.fromlist.length):
            item = create(structs.list_nth(data.fromlist, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_fromlist, i, item)
    else:
        v_fromlist = None
    cdef object v_quals
    if data.quals is not NULL:
        v_quals = create(data.quals, offset_to_index)
    else:
        v_quals = None
    return ast.FromExpr(v_fromlist, v_quals)


cdef create_OnConflictExpr(structs.OnConflictExpr* data, offset_to_index):
    cdef object v_action = getattr(enums, 'OnConflictAction')(data.action)
    cdef tuple v_arbiterElems
    cdef int arbiterElems_i
    if data.arbiterElems is not NULL:
        v_arbiterElems = PyTuple_New(data.arbiterElems.length)
        for i in range(data.arbiterElems.length):
            item = create(structs.list_nth(data.arbiterElems, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_arbiterElems, i, item)
    else:
        v_arbiterElems = None
    cdef object v_arbiterWhere
    if data.arbiterWhere is not NULL:
        v_arbiterWhere = create(data.arbiterWhere, offset_to_index)
    else:
        v_arbiterWhere = None
    cdef tuple v_onConflictSet
    cdef int onConflictSet_i
    if data.onConflictSet is not NULL:
        v_onConflictSet = PyTuple_New(data.onConflictSet.length)
        for i in range(data.onConflictSet.length):
            item = create(structs.list_nth(data.onConflictSet, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_onConflictSet, i, item)
    else:
        v_onConflictSet = None
    cdef object v_onConflictWhere
    if data.onConflictWhere is not NULL:
        v_onConflictWhere = create(data.onConflictWhere, offset_to_index)
    else:
        v_onConflictWhere = None
    cdef object v_exclRelIndex = data.exclRelIndex
    cdef tuple v_exclRelTlist
    cdef int exclRelTlist_i
    if data.exclRelTlist is not NULL:
        v_exclRelTlist = PyTuple_New(data.exclRelTlist.length)
        for i in range(data.exclRelTlist.length):
            item = create(structs.list_nth(data.exclRelTlist, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(v_exclRelTlist, i, item)
    else:
        v_exclRelTlist = None
    return ast.OnConflictExpr(v_action, v_arbiterElems, v_arbiterWhere, v_onConflictSet, v_onConflictWhere, v_exclRelIndex, v_exclRelTlist)


cdef create(void* data, offset_to_index):
    if data is NULL:
        return None

    cdef tuple t
    cdef int i
    cdef int tag = structs.nodeTag(data)

    if tag == structs.T_Alias:
        return create_Alias(<structs.Alias*> data, offset_to_index)
    elif tag == structs.T_RangeVar:
        return create_RangeVar(<structs.RangeVar*> data, offset_to_index)
    elif tag == structs.T_TableFunc:
        return create_TableFunc(<structs.TableFunc*> data, offset_to_index)
    elif tag == structs.T_Expr:
        return create_Expr(<structs.Expr*> data, offset_to_index)
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
    elif tag == structs.T_IntoClause:
        return create_IntoClause(<structs.IntoClause*> data, offset_to_index)
    elif tag == structs.T_Integer:
        return ast.Integer(structs.intVal(<structs.Value *> data))
    elif tag == structs.T_Float:
        return ast.Float(Decimal(structs.strVal(<structs.Value *> data).decode("utf-8")))
    elif tag == structs.T_String:
        return ast.String(structs.strVal(<structs.Value *> data).decode("utf-8"))
    elif tag == structs.T_BitString:
        return ast.BitString(structs.strVal(<structs.Value *> data).decode("utf-8"))
    elif tag == structs.T_Null:
        return ast.Null(None)
    elif tag == structs.T_List:
        t = PyTuple_New((<structs.List *> data).length)
        for i in range((<structs.List *> data).length):
            item = create(structs.list_nth(<structs.List *> data, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(t, i, item)
        return t
    elif tag == structs.T_RawStmt:
        return create_RawStmt(<structs.RawStmt*> data, offset_to_index)
    elif tag == structs.T_Query:
        return create_Query(<structs.Query*> data, offset_to_index)
    elif tag == structs.T_InsertStmt:
        return create_InsertStmt(<structs.InsertStmt*> data, offset_to_index)
    elif tag == structs.T_DeleteStmt:
        return create_DeleteStmt(<structs.DeleteStmt*> data, offset_to_index)
    elif tag == structs.T_UpdateStmt:
        return create_UpdateStmt(<structs.UpdateStmt*> data, offset_to_index)
    elif tag == structs.T_SelectStmt:
        return create_SelectStmt(<structs.SelectStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTableStmt:
        return create_AlterTableStmt(<structs.AlterTableStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTableCmd:
        return create_AlterTableCmd(<structs.AlterTableCmd*> data, offset_to_index)
    elif tag == structs.T_AlterDomainStmt:
        return create_AlterDomainStmt(<structs.AlterDomainStmt*> data, offset_to_index)
    elif tag == structs.T_SetOperationStmt:
        return create_SetOperationStmt(<structs.SetOperationStmt*> data, offset_to_index)
    elif tag == structs.T_GrantStmt:
        return create_GrantStmt(<structs.GrantStmt*> data, offset_to_index)
    elif tag == structs.T_GrantRoleStmt:
        return create_GrantRoleStmt(<structs.GrantRoleStmt*> data, offset_to_index)
    elif tag == structs.T_AlterDefaultPrivilegesStmt:
        return create_AlterDefaultPrivilegesStmt(<structs.AlterDefaultPrivilegesStmt*> data, offset_to_index)
    elif tag == structs.T_ClosePortalStmt:
        return create_ClosePortalStmt(<structs.ClosePortalStmt*> data, offset_to_index)
    elif tag == structs.T_ClusterStmt:
        return create_ClusterStmt(<structs.ClusterStmt*> data, offset_to_index)
    elif tag == structs.T_CopyStmt:
        return create_CopyStmt(<structs.CopyStmt*> data, offset_to_index)
    elif tag == structs.T_CreateStmt:
        return create_CreateStmt(<structs.CreateStmt*> data, offset_to_index)
    elif tag == structs.T_DefineStmt:
        return create_DefineStmt(<structs.DefineStmt*> data, offset_to_index)
    elif tag == structs.T_DropStmt:
        return create_DropStmt(<structs.DropStmt*> data, offset_to_index)
    elif tag == structs.T_TruncateStmt:
        return create_TruncateStmt(<structs.TruncateStmt*> data, offset_to_index)
    elif tag == structs.T_CommentStmt:
        return create_CommentStmt(<structs.CommentStmt*> data, offset_to_index)
    elif tag == structs.T_FetchStmt:
        return create_FetchStmt(<structs.FetchStmt*> data, offset_to_index)
    elif tag == structs.T_IndexStmt:
        return create_IndexStmt(<structs.IndexStmt*> data, offset_to_index)
    elif tag == structs.T_CreateFunctionStmt:
        return create_CreateFunctionStmt(<structs.CreateFunctionStmt*> data, offset_to_index)
    elif tag == structs.T_AlterFunctionStmt:
        return create_AlterFunctionStmt(<structs.AlterFunctionStmt*> data, offset_to_index)
    elif tag == structs.T_DoStmt:
        return create_DoStmt(<structs.DoStmt*> data, offset_to_index)
    elif tag == structs.T_RenameStmt:
        return create_RenameStmt(<structs.RenameStmt*> data, offset_to_index)
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
    elif tag == structs.T_ViewStmt:
        return create_ViewStmt(<structs.ViewStmt*> data, offset_to_index)
    elif tag == structs.T_LoadStmt:
        return create_LoadStmt(<structs.LoadStmt*> data, offset_to_index)
    elif tag == structs.T_CreateDomainStmt:
        return create_CreateDomainStmt(<structs.CreateDomainStmt*> data, offset_to_index)
    elif tag == structs.T_CreatedbStmt:
        return create_CreatedbStmt(<structs.CreatedbStmt*> data, offset_to_index)
    elif tag == structs.T_DropdbStmt:
        return create_DropdbStmt(<structs.DropdbStmt*> data, offset_to_index)
    elif tag == structs.T_VacuumStmt:
        return create_VacuumStmt(<structs.VacuumStmt*> data, offset_to_index)
    elif tag == structs.T_ExplainStmt:
        return create_ExplainStmt(<structs.ExplainStmt*> data, offset_to_index)
    elif tag == structs.T_CreateTableAsStmt:
        return create_CreateTableAsStmt(<structs.CreateTableAsStmt*> data, offset_to_index)
    elif tag == structs.T_CreateSeqStmt:
        return create_CreateSeqStmt(<structs.CreateSeqStmt*> data, offset_to_index)
    elif tag == structs.T_AlterSeqStmt:
        return create_AlterSeqStmt(<structs.AlterSeqStmt*> data, offset_to_index)
    elif tag == structs.T_VariableSetStmt:
        return create_VariableSetStmt(<structs.VariableSetStmt*> data, offset_to_index)
    elif tag == structs.T_VariableShowStmt:
        return create_VariableShowStmt(<structs.VariableShowStmt*> data, offset_to_index)
    elif tag == structs.T_DiscardStmt:
        return create_DiscardStmt(<structs.DiscardStmt*> data, offset_to_index)
    elif tag == structs.T_CreateTrigStmt:
        return create_CreateTrigStmt(<structs.CreateTrigStmt*> data, offset_to_index)
    elif tag == structs.T_CreatePLangStmt:
        return create_CreatePLangStmt(<structs.CreatePLangStmt*> data, offset_to_index)
    elif tag == structs.T_CreateRoleStmt:
        return create_CreateRoleStmt(<structs.CreateRoleStmt*> data, offset_to_index)
    elif tag == structs.T_AlterRoleStmt:
        return create_AlterRoleStmt(<structs.AlterRoleStmt*> data, offset_to_index)
    elif tag == structs.T_DropRoleStmt:
        return create_DropRoleStmt(<structs.DropRoleStmt*> data, offset_to_index)
    elif tag == structs.T_LockStmt:
        return create_LockStmt(<structs.LockStmt*> data, offset_to_index)
    elif tag == structs.T_ConstraintsSetStmt:
        return create_ConstraintsSetStmt(<structs.ConstraintsSetStmt*> data, offset_to_index)
    elif tag == structs.T_ReindexStmt:
        return create_ReindexStmt(<structs.ReindexStmt*> data, offset_to_index)
    elif tag == structs.T_CheckPointStmt:
        return create_CheckPointStmt(<structs.CheckPointStmt*> data, offset_to_index)
    elif tag == structs.T_CreateSchemaStmt:
        return create_CreateSchemaStmt(<structs.CreateSchemaStmt*> data, offset_to_index)
    elif tag == structs.T_AlterDatabaseStmt:
        return create_AlterDatabaseStmt(<structs.AlterDatabaseStmt*> data, offset_to_index)
    elif tag == structs.T_AlterDatabaseSetStmt:
        return create_AlterDatabaseSetStmt(<structs.AlterDatabaseSetStmt*> data, offset_to_index)
    elif tag == structs.T_AlterRoleSetStmt:
        return create_AlterRoleSetStmt(<structs.AlterRoleSetStmt*> data, offset_to_index)
    elif tag == structs.T_CreateConversionStmt:
        return create_CreateConversionStmt(<structs.CreateConversionStmt*> data, offset_to_index)
    elif tag == structs.T_CreateCastStmt:
        return create_CreateCastStmt(<structs.CreateCastStmt*> data, offset_to_index)
    elif tag == structs.T_CreateOpClassStmt:
        return create_CreateOpClassStmt(<structs.CreateOpClassStmt*> data, offset_to_index)
    elif tag == structs.T_CreateOpFamilyStmt:
        return create_CreateOpFamilyStmt(<structs.CreateOpFamilyStmt*> data, offset_to_index)
    elif tag == structs.T_AlterOpFamilyStmt:
        return create_AlterOpFamilyStmt(<structs.AlterOpFamilyStmt*> data, offset_to_index)
    elif tag == structs.T_PrepareStmt:
        return create_PrepareStmt(<structs.PrepareStmt*> data, offset_to_index)
    elif tag == structs.T_ExecuteStmt:
        return create_ExecuteStmt(<structs.ExecuteStmt*> data, offset_to_index)
    elif tag == structs.T_DeallocateStmt:
        return create_DeallocateStmt(<structs.DeallocateStmt*> data, offset_to_index)
    elif tag == structs.T_DeclareCursorStmt:
        return create_DeclareCursorStmt(<structs.DeclareCursorStmt*> data, offset_to_index)
    elif tag == structs.T_CreateTableSpaceStmt:
        return create_CreateTableSpaceStmt(<structs.CreateTableSpaceStmt*> data, offset_to_index)
    elif tag == structs.T_DropTableSpaceStmt:
        return create_DropTableSpaceStmt(<structs.DropTableSpaceStmt*> data, offset_to_index)
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
    elif tag == structs.T_DropOwnedStmt:
        return create_DropOwnedStmt(<structs.DropOwnedStmt*> data, offset_to_index)
    elif tag == structs.T_ReassignOwnedStmt:
        return create_ReassignOwnedStmt(<structs.ReassignOwnedStmt*> data, offset_to_index)
    elif tag == structs.T_CompositeTypeStmt:
        return create_CompositeTypeStmt(<structs.CompositeTypeStmt*> data, offset_to_index)
    elif tag == structs.T_CreateEnumStmt:
        return create_CreateEnumStmt(<structs.CreateEnumStmt*> data, offset_to_index)
    elif tag == structs.T_CreateRangeStmt:
        return create_CreateRangeStmt(<structs.CreateRangeStmt*> data, offset_to_index)
    elif tag == structs.T_AlterEnumStmt:
        return create_AlterEnumStmt(<structs.AlterEnumStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTSDictionaryStmt:
        return create_AlterTSDictionaryStmt(<structs.AlterTSDictionaryStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTSConfigurationStmt:
        return create_AlterTSConfigurationStmt(<structs.AlterTSConfigurationStmt*> data, offset_to_index)
    elif tag == structs.T_CreateFdwStmt:
        return create_CreateFdwStmt(<structs.CreateFdwStmt*> data, offset_to_index)
    elif tag == structs.T_AlterFdwStmt:
        return create_AlterFdwStmt(<structs.AlterFdwStmt*> data, offset_to_index)
    elif tag == structs.T_CreateForeignServerStmt:
        return create_CreateForeignServerStmt(<structs.CreateForeignServerStmt*> data, offset_to_index)
    elif tag == structs.T_AlterForeignServerStmt:
        return create_AlterForeignServerStmt(<structs.AlterForeignServerStmt*> data, offset_to_index)
    elif tag == structs.T_CreateUserMappingStmt:
        return create_CreateUserMappingStmt(<structs.CreateUserMappingStmt*> data, offset_to_index)
    elif tag == structs.T_AlterUserMappingStmt:
        return create_AlterUserMappingStmt(<structs.AlterUserMappingStmt*> data, offset_to_index)
    elif tag == structs.T_DropUserMappingStmt:
        return create_DropUserMappingStmt(<structs.DropUserMappingStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTableSpaceOptionsStmt:
        return create_AlterTableSpaceOptionsStmt(<structs.AlterTableSpaceOptionsStmt*> data, offset_to_index)
    elif tag == structs.T_AlterTableMoveAllStmt:
        return create_AlterTableMoveAllStmt(<structs.AlterTableMoveAllStmt*> data, offset_to_index)
    elif tag == structs.T_SecLabelStmt:
        return create_SecLabelStmt(<structs.SecLabelStmt*> data, offset_to_index)
    elif tag == structs.T_CreateForeignTableStmt:
        return create_CreateForeignTableStmt(<structs.CreateForeignTableStmt*> data, offset_to_index)
    elif tag == structs.T_ImportForeignSchemaStmt:
        return create_ImportForeignSchemaStmt(<structs.ImportForeignSchemaStmt*> data, offset_to_index)
    elif tag == structs.T_CreateExtensionStmt:
        return create_CreateExtensionStmt(<structs.CreateExtensionStmt*> data, offset_to_index)
    elif tag == structs.T_AlterExtensionStmt:
        return create_AlterExtensionStmt(<structs.AlterExtensionStmt*> data, offset_to_index)
    elif tag == structs.T_AlterExtensionContentsStmt:
        return create_AlterExtensionContentsStmt(<structs.AlterExtensionContentsStmt*> data, offset_to_index)
    elif tag == structs.T_CreateEventTrigStmt:
        return create_CreateEventTrigStmt(<structs.CreateEventTrigStmt*> data, offset_to_index)
    elif tag == structs.T_AlterEventTrigStmt:
        return create_AlterEventTrigStmt(<structs.AlterEventTrigStmt*> data, offset_to_index)
    elif tag == structs.T_RefreshMatViewStmt:
        return create_RefreshMatViewStmt(<structs.RefreshMatViewStmt*> data, offset_to_index)
    elif tag == structs.T_ReplicaIdentityStmt:
        return create_ReplicaIdentityStmt(<structs.ReplicaIdentityStmt*> data, offset_to_index)
    elif tag == structs.T_AlterSystemStmt:
        return create_AlterSystemStmt(<structs.AlterSystemStmt*> data, offset_to_index)
    elif tag == structs.T_CreatePolicyStmt:
        return create_CreatePolicyStmt(<structs.CreatePolicyStmt*> data, offset_to_index)
    elif tag == structs.T_AlterPolicyStmt:
        return create_AlterPolicyStmt(<structs.AlterPolicyStmt*> data, offset_to_index)
    elif tag == structs.T_CreateTransformStmt:
        return create_CreateTransformStmt(<structs.CreateTransformStmt*> data, offset_to_index)
    elif tag == structs.T_CreateAmStmt:
        return create_CreateAmStmt(<structs.CreateAmStmt*> data, offset_to_index)
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
    elif tag == structs.T_CreateStatsStmt:
        return create_CreateStatsStmt(<structs.CreateStatsStmt*> data, offset_to_index)
    elif tag == structs.T_AlterCollationStmt:
        return create_AlterCollationStmt(<structs.AlterCollationStmt*> data, offset_to_index)
    elif tag == structs.T_CallStmt:
        return create_CallStmt(<structs.CallStmt*> data, offset_to_index)
    elif tag == structs.T_AlterStatsStmt:
        return create_AlterStatsStmt(<structs.AlterStatsStmt*> data, offset_to_index)
    elif tag == structs.T_A_Expr:
        return create_A_Expr(<structs.A_Expr*> data, offset_to_index)
    elif tag == structs.T_ColumnRef:
        return create_ColumnRef(<structs.ColumnRef*> data, offset_to_index)
    elif tag == structs.T_ParamRef:
        return create_ParamRef(<structs.ParamRef*> data, offset_to_index)
    elif tag == structs.T_A_Const:
        return create_A_Const(<structs.A_Const*> data, offset_to_index)
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
    elif tag == structs.T_TypeCast:
        return create_TypeCast(<structs.TypeCast*> data, offset_to_index)
    elif tag == structs.T_CollateClause:
        return create_CollateClause(<structs.CollateClause*> data, offset_to_index)
    elif tag == structs.T_SortBy:
        return create_SortBy(<structs.SortBy*> data, offset_to_index)
    elif tag == structs.T_WindowDef:
        return create_WindowDef(<structs.WindowDef*> data, offset_to_index)
    elif tag == structs.T_RangeSubselect:
        return create_RangeSubselect(<structs.RangeSubselect*> data, offset_to_index)
    elif tag == structs.T_RangeFunction:
        return create_RangeFunction(<structs.RangeFunction*> data, offset_to_index)
    elif tag == structs.T_RangeTableSample:
        return create_RangeTableSample(<structs.RangeTableSample*> data, offset_to_index)
    elif tag == structs.T_RangeTableFunc:
        return create_RangeTableFunc(<structs.RangeTableFunc*> data, offset_to_index)
    elif tag == structs.T_RangeTableFuncCol:
        return create_RangeTableFuncCol(<structs.RangeTableFuncCol*> data, offset_to_index)
    elif tag == structs.T_TypeName:
        return create_TypeName(<structs.TypeName*> data, offset_to_index)
    elif tag == structs.T_ColumnDef:
        return create_ColumnDef(<structs.ColumnDef*> data, offset_to_index)
    elif tag == structs.T_IndexElem:
        return create_IndexElem(<structs.IndexElem*> data, offset_to_index)
    elif tag == structs.T_Constraint:
        return create_Constraint(<structs.Constraint*> data, offset_to_index)
    elif tag == structs.T_DefElem:
        return create_DefElem(<structs.DefElem*> data, offset_to_index)
    elif tag == structs.T_RangeTblEntry:
        return create_RangeTblEntry(<structs.RangeTblEntry*> data, offset_to_index)
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
    elif tag == structs.T_ObjectWithArgs:
        return create_ObjectWithArgs(<structs.ObjectWithArgs*> data, offset_to_index)
    elif tag == structs.T_AccessPriv:
        return create_AccessPriv(<structs.AccessPriv*> data, offset_to_index)
    elif tag == structs.T_CreateOpClassItem:
        return create_CreateOpClassItem(<structs.CreateOpClassItem*> data, offset_to_index)
    elif tag == structs.T_TableLikeClause:
        return create_TableLikeClause(<structs.TableLikeClause*> data, offset_to_index)
    elif tag == structs.T_FunctionParameter:
        return create_FunctionParameter(<structs.FunctionParameter*> data, offset_to_index)
    elif tag == structs.T_LockingClause:
        return create_LockingClause(<structs.LockingClause*> data, offset_to_index)
    elif tag == structs.T_RowMarkClause:
        return create_RowMarkClause(<structs.RowMarkClause*> data, offset_to_index)
    elif tag == structs.T_XmlSerialize:
        return create_XmlSerialize(<structs.XmlSerialize*> data, offset_to_index)
    elif tag == structs.T_WithClause:
        return create_WithClause(<structs.WithClause*> data, offset_to_index)
    elif tag == structs.T_InferClause:
        return create_InferClause(<structs.InferClause*> data, offset_to_index)
    elif tag == structs.T_OnConflictClause:
        return create_OnConflictClause(<structs.OnConflictClause*> data, offset_to_index)
    elif tag == structs.T_CommonTableExpr:
        return create_CommonTableExpr(<structs.CommonTableExpr*> data, offset_to_index)
    elif tag == structs.T_RoleSpec:
        return create_RoleSpec(<structs.RoleSpec*> data, offset_to_index)
    elif tag == structs.T_TriggerTransition:
        return create_TriggerTransition(<structs.TriggerTransition*> data, offset_to_index)
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
    elif tag == structs.T_VacuumRelation:
        return create_VacuumRelation(<structs.VacuumRelation*> data, offset_to_index)
    elif tag == structs.T_InlineCodeBlock:
        return create_InlineCodeBlock(<structs.InlineCodeBlock*> data, offset_to_index)
    elif tag == structs.T_CallContext:
        return create_CallContext(<structs.CallContext*> data, offset_to_index)
    raise ValueError("Unhandled tag: %s" % tag)
