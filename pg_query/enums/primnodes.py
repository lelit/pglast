# -*- coding: utf-8 -*-
# :Project:   pg_query -- DO NOT EDIT: automatically extracted from primnodes.h @ 10-latest-0-g1ec5c22
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

try:
    from enum import Enum, IntEnum, IntFlag, auto
except ImportError:
    # Python < 3.6
    from aenum import Enum, IntEnum, IntFlag, auto


class BoolExprType(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L554>`__."

    AND_EXPR = 0
    OR_EXPR = auto()
    NOT_EXPR = auto()

class BoolTestType(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1195>`__."

    IS_TRUE = 0
    IS_NOT_TRUE = auto()
    IS_FALSE = auto()
    IS_NOT_FALSE = auto()
    IS_UNKNOWN = auto()
    IS_NOT_UNKNOWN = auto()

class CoercionContext(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L420>`__."

    COERCION_IMPLICIT = 0
    COERCION_ASSIGNMENT = auto()
    COERCION_EXPLICIT = auto()

class CoercionForm(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L436>`__."

    COERCE_EXPLICIT_CALL = 0
    COERCE_EXPLICIT_CAST = auto()
    COERCE_IMPLICIT_CAST = auto()

class MinMaxOp(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1054>`__."

    IS_GREATEST = 0
    IS_LEAST = auto()

class NullTestType(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1172>`__."

    IS_NULL = 0
    IS_NOT_NULL = auto()

class OnCommitAction(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L47>`__."

    ONCOMMIT_NOOP = 0
    ONCOMMIT_PRESERVE_ROWS = auto()
    ONCOMMIT_DELETE_ROWS = auto()
    ONCOMMIT_DROP = auto()

class ParamKind(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L233>`__."

    PARAM_EXTERN = 0
    PARAM_EXEC = auto()
    PARAM_SUBLINK = auto()
    PARAM_MULTIEXPR = auto()

class RowCompareType(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1017>`__."

    ROWCOMPARE_LT = 1
    ROWCOMPARE_LE = 2
    ROWCOMPARE_EQ = 3
    ROWCOMPARE_GE = 4
    ROWCOMPARE_GT = 5
    ROWCOMPARE_NE = 6

class SQLValueFunctionOp(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1082>`__."

    SVFOP_CURRENT_DATE = 0
    SVFOP_CURRENT_TIME = auto()
    SVFOP_CURRENT_TIME_N = auto()
    SVFOP_CURRENT_TIMESTAMP = auto()
    SVFOP_CURRENT_TIMESTAMP_N = auto()
    SVFOP_LOCALTIME = auto()
    SVFOP_LOCALTIME_N = auto()
    SVFOP_LOCALTIMESTAMP = auto()
    SVFOP_LOCALTIMESTAMP_N = auto()
    SVFOP_CURRENT_ROLE = auto()
    SVFOP_CURRENT_USER = auto()
    SVFOP_USER = auto()
    SVFOP_SESSION_USER = auto()
    SVFOP_CURRENT_CATALOG = auto()
    SVFOP_CURRENT_SCHEMA = auto()

class SubLinkType(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L618>`__."

    EXISTS_SUBLINK = 0
    ALL_SUBLINK = auto()
    ANY_SUBLINK = auto()
    ROWCOMPARE_SUBLINK = auto()
    EXPR_SUBLINK = auto()
    MULTIEXPR_SUBLINK = auto()
    ARRAY_SUBLINK = auto()
    CTE_SUBLINK = auto()

class XmlExprOp(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/primnodes.h#L1121>`__."

    IS_XMLCONCAT = 0
    IS_XMLELEMENT = auto()
    IS_XMLFOREST = auto()
    IS_XMLPARSE = auto()
    IS_XMLPI = auto()
    IS_XMLROOT = auto()
    IS_XMLSERIALIZE = auto()
    IS_DOCUMENT = auto()
