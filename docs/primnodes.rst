.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

==============================================================================
 :mod:`pg_query.enums.primnodes` --- Constants extracted from `primnodes.h`__
==============================================================================

__ https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h

.. module:: pg_query.enums.primnodes


.. class:: pg_query.enums.primnodes.BoolExprType

   Corresponds to the `BoolExprType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L554>`__.

   .. data:: AND_EXPR

   .. data:: OR_EXPR

   .. data:: NOT_EXPR


.. class:: pg_query.enums.primnodes.BoolTestType

   Corresponds to the `BoolTestType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1195>`__.

   .. data:: IS_TRUE

   .. data:: IS_NOT_TRUE

   .. data:: IS_FALSE

   .. data:: IS_NOT_FALSE

   .. data:: IS_UNKNOWN

   .. data:: IS_NOT_UNKNOWN


.. class:: pg_query.enums.primnodes.CoercionContext

   Corresponds to the `CoercionContext enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L420>`__.

   .. data:: COERCION_IMPLICIT

   .. data:: COERCION_ASSIGNMENT

   .. data:: COERCION_EXPLICIT


.. class:: pg_query.enums.primnodes.CoercionForm

   Corresponds to the `CoercionForm enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L436>`__.

   .. data:: COERCE_EXPLICIT_CALL

   .. data:: COERCE_EXPLICIT_CAST

   .. data:: COERCE_IMPLICIT_CAST


.. class:: pg_query.enums.primnodes.MinMaxOp

   Corresponds to the `MinMaxOp enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1054>`__.

   .. data:: IS_GREATEST

   .. data:: IS_LEAST


.. class:: pg_query.enums.primnodes.NullTestType

   Corresponds to the `NullTestType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1172>`__.

   .. data:: IS_NULL

   .. data:: IS_NOT_NULL


.. class:: pg_query.enums.primnodes.OnCommitAction

   Corresponds to the `OnCommitAction enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L47>`__.

   .. data:: ONCOMMIT_NOOP

   .. data:: ONCOMMIT_PRESERVE_ROWS

   .. data:: ONCOMMIT_DELETE_ROWS

   .. data:: ONCOMMIT_DROP


.. class:: pg_query.enums.primnodes.ParamKind

   Corresponds to the `ParamKind enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L233>`__.

   .. data:: PARAM_EXTERN

   .. data:: PARAM_EXEC

   .. data:: PARAM_SUBLINK

   .. data:: PARAM_MULTIEXPR


.. class:: pg_query.enums.primnodes.RowCompareType

   Corresponds to the `RowCompareType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1017>`__.

   .. data:: ROWCOMPARE_LT

   .. data:: ROWCOMPARE_LE

   .. data:: ROWCOMPARE_EQ

   .. data:: ROWCOMPARE_GE

   .. data:: ROWCOMPARE_GT

   .. data:: ROWCOMPARE_NE


.. class:: pg_query.enums.primnodes.SQLValueFunctionOp

   Corresponds to the `SQLValueFunctionOp enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1082>`__.

   .. data:: SVFOP_CURRENT_DATE

   .. data:: SVFOP_CURRENT_TIME

   .. data:: SVFOP_CURRENT_TIME_N

   .. data:: SVFOP_CURRENT_TIMESTAMP

   .. data:: SVFOP_CURRENT_TIMESTAMP_N

   .. data:: SVFOP_LOCALTIME

   .. data:: SVFOP_LOCALTIME_N

   .. data:: SVFOP_LOCALTIMESTAMP

   .. data:: SVFOP_LOCALTIMESTAMP_N

   .. data:: SVFOP_CURRENT_ROLE

   .. data:: SVFOP_CURRENT_USER

   .. data:: SVFOP_USER

   .. data:: SVFOP_SESSION_USER

   .. data:: SVFOP_CURRENT_CATALOG

   .. data:: SVFOP_CURRENT_SCHEMA


.. class:: pg_query.enums.primnodes.SubLinkType

   Corresponds to the `SubLinkType enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L618>`__.

   .. data:: EXISTS_SUBLINK

   .. data:: ALL_SUBLINK

   .. data:: ANY_SUBLINK

   .. data:: ROWCOMPARE_SUBLINK

   .. data:: EXPR_SUBLINK

   .. data:: MULTIEXPR_SUBLINK

   .. data:: ARRAY_SUBLINK

   .. data:: CTE_SUBLINK


.. class:: pg_query.enums.primnodes.XmlExprOp

   Corresponds to the `XmlExprOp enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/primnodes.h#L1121>`__.

   .. data:: IS_XMLCONCAT

   .. data:: IS_XMLELEMENT

   .. data:: IS_XMLFOREST

   .. data:: IS_XMLPARSE

   .. data:: IS_XMLPI

   .. data:: IS_XMLROOT

   .. data:: IS_XMLSERIALIZE

   .. data:: IS_DOCUMENT
