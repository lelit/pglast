# -*- coding: utf-8 -*-
# :Project:   pg_query -- DO NOT EDIT: automatically extracted from primnodes.h @ 10-latest-0-g1ec5c22
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

import enum


class BoolExprType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L554>`__."

    AND_EXPR = 0
    OR_EXPR = enum.auto()
    NOT_EXPR = enum.auto()

class BoolTestType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1195>`__."

    IS_TRUE = 0
    IS_NOT_TRUE = enum.auto()
    IS_FALSE = enum.auto()
    IS_NOT_FALSE = enum.auto()
    IS_UNKNOWN = enum.auto()
    IS_NOT_UNKNOWN = enum.auto()

class CoercionContext(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L420>`__."

    COERCION_IMPLICIT = 0
    COERCION_ASSIGNMENT = enum.auto()
    COERCION_EXPLICIT = enum.auto()

class CoercionForm(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L436>`__."

    COERCE_EXPLICIT_CALL = 0
    COERCE_EXPLICIT_CAST = enum.auto()
    COERCE_IMPLICIT_CAST = enum.auto()

class MinMaxOp(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1054>`__."

    IS_GREATEST = 0
    IS_LEAST = enum.auto()

class NullTestType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1172>`__."

    IS_NULL = 0
    IS_NOT_NULL = enum.auto()

class OnCommitAction(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L47>`__."

    ONCOMMIT_NOOP = 0
    ONCOMMIT_PRESERVE_ROWS = enum.auto()
    ONCOMMIT_DELETE_ROWS = enum.auto()
    ONCOMMIT_DROP = enum.auto()

class ParamKind(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L233>`__."

    PARAM_EXTERN = 0
    PARAM_EXEC = enum.auto()
    PARAM_SUBLINK = enum.auto()
    PARAM_MULTIEXPR = enum.auto()

class RowCompareType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1017>`__."

    ROWCOMPARE_LT = 1
    ROWCOMPARE_LE = 2
    ROWCOMPARE_EQ = 3
    ROWCOMPARE_GE = 4
    ROWCOMPARE_GT = 5
    ROWCOMPARE_NE = 6

class SQLValueFunctionOp(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1082>`__."

    SVFOP_CURRENT_DATE = 0
    SVFOP_CURRENT_TIME = enum.auto()
    SVFOP_CURRENT_TIME_N = enum.auto()
    SVFOP_CURRENT_TIMESTAMP = enum.auto()
    SVFOP_CURRENT_TIMESTAMP_N = enum.auto()
    SVFOP_LOCALTIME = enum.auto()
    SVFOP_LOCALTIME_N = enum.auto()
    SVFOP_LOCALTIMESTAMP = enum.auto()
    SVFOP_LOCALTIMESTAMP_N = enum.auto()
    SVFOP_CURRENT_ROLE = enum.auto()
    SVFOP_CURRENT_USER = enum.auto()
    SVFOP_USER = enum.auto()
    SVFOP_SESSION_USER = enum.auto()
    SVFOP_CURRENT_CATALOG = enum.auto()
    SVFOP_CURRENT_SCHEMA = enum.auto()

class SubLinkType(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L618>`__."

    EXISTS_SUBLINK = 0
    ALL_SUBLINK = enum.auto()
    ANY_SUBLINK = enum.auto()
    ROWCOMPARE_SUBLINK = enum.auto()
    EXPR_SUBLINK = enum.auto()
    MULTIEXPR_SUBLINK = enum.auto()
    ARRAY_SUBLINK = enum.auto()
    CTE_SUBLINK = enum.auto()

class XmlExprOp(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1121>`__."

    IS_XMLCONCAT = 0
    IS_XMLELEMENT = enum.auto()
    IS_XMLFOREST = enum.auto()
    IS_XMLPARSE = enum.auto()
    IS_XMLPI = enum.auto()
    IS_XMLROOT = enum.auto()
    IS_XMLSERIALIZE = enum.auto()
    IS_DOCUMENT = enum.auto()
