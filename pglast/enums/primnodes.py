# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: automatically extracted from primnodes.h @ 17-6.1.0-0-g1c1a32e
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2025 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:  # pragma: no cover
    # Python < 3.10
    class StrEnum(str, Enum):
        pass


class BoolExprType(IntEnum):
    AND_EXPR = 0
    OR_EXPR = auto()
    NOT_EXPR = auto()


class BoolTestType(IntEnum):
    IS_TRUE = 0
    IS_NOT_TRUE = auto()
    IS_FALSE = auto()
    IS_NOT_FALSE = auto()
    IS_UNKNOWN = auto()
    IS_NOT_UNKNOWN = auto()


class CoercionContext(IntEnum):
    COERCION_IMPLICIT = 0
    COERCION_ASSIGNMENT = auto()
    COERCION_PLPGSQL = auto()
    COERCION_EXPLICIT = auto()


class CoercionForm(IntEnum):
    COERCE_EXPLICIT_CALL = 0
    COERCE_EXPLICIT_CAST = auto()
    COERCE_IMPLICIT_CAST = auto()
    COERCE_SQL_SYNTAX = auto()


class JsonBehaviorType(IntEnum):
    JSON_BEHAVIOR_NULL = 0
    JSON_BEHAVIOR_ERROR = auto()
    JSON_BEHAVIOR_EMPTY = auto()
    JSON_BEHAVIOR_TRUE = auto()
    JSON_BEHAVIOR_FALSE = auto()
    JSON_BEHAVIOR_UNKNOWN = auto()
    JSON_BEHAVIOR_EMPTY_ARRAY = auto()
    JSON_BEHAVIOR_EMPTY_OBJECT = auto()
    JSON_BEHAVIOR_DEFAULT = auto()


class JsonConstructorType(IntEnum):
    JSCTOR_JSON_OBJECT = 1
    JSCTOR_JSON_ARRAY = 2
    JSCTOR_JSON_OBJECTAGG = 3
    JSCTOR_JSON_ARRAYAGG = 4
    JSCTOR_JSON_PARSE = 5
    JSCTOR_JSON_SCALAR = 6
    JSCTOR_JSON_SERIALIZE = 7


class JsonEncoding(IntEnum):
    JS_ENC_DEFAULT = 0
    JS_ENC_UTF8 = auto()
    JS_ENC_UTF16 = auto()
    JS_ENC_UTF32 = auto()


class JsonExprOp(IntEnum):
    JSON_EXISTS_OP = 0
    JSON_QUERY_OP = auto()
    JSON_VALUE_OP = auto()
    JSON_TABLE_OP = auto()


class JsonFormatType(IntEnum):
    JS_FORMAT_DEFAULT = 0
    JS_FORMAT_JSON = auto()
    JS_FORMAT_JSONB = auto()


class JsonValueType(IntEnum):
    JS_TYPE_ANY = 0
    JS_TYPE_OBJECT = auto()
    JS_TYPE_ARRAY = auto()
    JS_TYPE_SCALAR = auto()


class JsonWrapper(IntEnum):
    JSW_UNSPEC = 0
    JSW_NONE = auto()
    JSW_CONDITIONAL = auto()
    JSW_UNCONDITIONAL = auto()


class MergeMatchKind(IntEnum):
    MERGE_WHEN_MATCHED = 0
    MERGE_WHEN_NOT_MATCHED_BY_SOURCE = auto()
    MERGE_WHEN_NOT_MATCHED_BY_TARGET = auto()


class MinMaxOp(IntEnum):
    IS_GREATEST = 0
    IS_LEAST = auto()


class NullTestType(IntEnum):
    IS_NULL = 0
    IS_NOT_NULL = auto()


class OnCommitAction(IntEnum):
    ONCOMMIT_NOOP = 0
    ONCOMMIT_PRESERVE_ROWS = auto()
    ONCOMMIT_DELETE_ROWS = auto()
    ONCOMMIT_DROP = auto()


class OverridingKind(IntEnum):
    OVERRIDING_NOT_SET = 0
    OVERRIDING_USER_VALUE = auto()
    OVERRIDING_SYSTEM_VALUE = auto()


class ParamKind(IntEnum):
    PARAM_EXTERN = 0
    PARAM_EXEC = auto()
    PARAM_SUBLINK = auto()
    PARAM_MULTIEXPR = auto()


class RowCompareType(IntEnum):
    ROWCOMPARE_LT = 1
    ROWCOMPARE_LE = 2
    ROWCOMPARE_EQ = 3
    ROWCOMPARE_GE = 4
    ROWCOMPARE_GT = 5
    ROWCOMPARE_NE = 6


class SQLValueFunctionOp(IntEnum):
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
    EXISTS_SUBLINK = 0
    ALL_SUBLINK = auto()
    ANY_SUBLINK = auto()
    ROWCOMPARE_SUBLINK = auto()
    EXPR_SUBLINK = auto()
    MULTIEXPR_SUBLINK = auto()
    ARRAY_SUBLINK = auto()
    CTE_SUBLINK = auto()


class TableFuncType(IntEnum):
    TFT_XMLTABLE = 0
    TFT_JSON_TABLE = auto()


class XmlExprOp(IntEnum):
    IS_XMLCONCAT = 0
    IS_XMLELEMENT = auto()
    IS_XMLFOREST = auto()
    IS_XMLPARSE = auto()
    IS_XMLPI = auto()
    IS_XMLROOT = auto()
    IS_XMLSERIALIZE = auto()
    IS_DOCUMENT = auto()


class XmlOptionType(IntEnum):
    XMLOPTION_DOCUMENT = 0
    XMLOPTION_CONTENT = auto()
