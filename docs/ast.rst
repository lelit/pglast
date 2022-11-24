.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2021-2022 Lele Gaifax
..

.. _pglast.ast:

===================================================================
 :mod:`pglast.ast` --- Python classes representing PG parser nodes
===================================================================

The module implements a set of *data* classes, one for each ``C`` structure defined in several
PostgreSQL headers, primarily those in the `include/nodes/`__ directory.

__ https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes

The :class:`pglast.ast.Node` is an abstract class that implements the common behaviour of all
the concrete classes. In particular any node can be :meth:`compared <pglast.ast.Node.__eq__>`
with another instance, is able to :meth:`serialize <pglast.ast.Node.__call__>` itself and can
be :meth:`altered <pglast.ast.Node.__setattr__>`.

.. module:: pglast.ast

.. autoclass:: Node
   :special-members: __repr__, __eq__, __call__, __setattr__

.. autoclass:: Value
.. autoclass:: BitString
.. autoclass:: Float
.. autoclass:: Integer
.. autoclass:: Null
.. autoclass:: String


.. class:: A_ArrayExpr(elements=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L424>`__ parser node.

   .. attribute:: elements
      :type: tuple

      Array element expressions

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: A_Const(val=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L295>`__ parser node.

   .. attribute:: val
      :type: Value

      Value (includes type info, see value.h)

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: A_Expr(kind=None, name=None, lexpr=None, rexpr=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L282>`__ parser node.

   .. attribute:: kind
      :type: A_Expr_Kind

   .. attribute:: name
      :type: tuple

      Possibly-qualified name of operator

   .. attribute:: lexpr
      :type: Node

      Left argument, or NULL if none

   .. attribute:: rexpr
      :type: Node

      Right argument, or NULL if none

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: A_Indices(is_slice=None, lidx=None, uidx=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L391>`__ parser node.

   .. attribute:: is_slice
      :type: bool

      True if slice (i.e., colon present)

   .. attribute:: lidx
      :type: Node

      Slice lower bound, if any

   .. attribute:: uidx
      :type: Node

      Subscript, or slice upper bound if any


.. class:: A_Indirection(arg=None, indirection=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L414>`__ parser node.

   .. attribute:: arg
      :type: Node

      The thing being selected from

   .. attribute:: indirection
      :type: tuple

      Subscripts and/or field names and/or *


.. class:: A_Star()

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L380>`__ parser node.


.. class:: AccessPriv(priv_name=None, cols=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2060>`__ parser node.

   .. attribute:: priv_name
      :type: str

      String name of privilege

   .. attribute:: cols
      :type: tuple

      List of Value strings


.. class:: Aggref(aggargtypes=None, aggdirectargs=None, args=None, aggorder=None, aggdistinct=None, aggfilter=None, aggstar=None, aggvariadic=None, aggkind=None, agglevelsup=None, aggsplit=None, aggno=None, aggtransno=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L320>`__ parser node.

   .. attribute:: aggargtypes
      :type: tuple

      Type Oids of direct and aggregated args

   .. attribute:: aggdirectargs
      :type: tuple

      Direct arguments, if an ordered-set agg

   .. attribute:: args
      :type: tuple

      Aggregated arguments and sort expressions

   .. attribute:: aggorder
      :type: tuple

      ORDER BY (list of SortGroupClause)

   .. attribute:: aggdistinct
      :type: tuple

      DISTINCT (list of SortGroupClause)

   .. attribute:: aggfilter
      :type: Expr*

      FILTER expression, if any

   .. attribute:: aggstar
      :type: bool

      True if argument list was really '*'

   .. attribute:: aggvariadic
      :type: bool

      True if variadic arguments have been
      combined into an array last argument

   .. attribute:: aggkind
      :type: str

      Aggregate kind (see pg_aggregate.h)

   .. attribute:: agglevelsup
      :type: Index

      > 0 if agg belongs to outer query

   .. attribute:: aggsplit
      :type: AggSplit

      Expected agg-splitting mode of parent Agg

   .. attribute:: aggno
      :type: int

      Unique ID within the Agg node

   .. attribute:: aggtransno
      :type: int

      Unique ID of transition state in the Agg

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: Alias(aliasname=None, colnames=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L39>`__ parser node.

   .. attribute:: aliasname
      :type: str

      Aliased rel name (never qualified)

   .. attribute:: colnames
      :type: tuple

      Optional list of column aliases


.. class:: AlterCollationStmt(collname=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1967>`__ parser node.

   .. attribute:: collname
      :type: tuple


.. class:: AlterDatabaseSetStmt(dbname=None, setstmt=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3294>`__ parser node.

   .. attribute:: dbname
      :type: str

      Database name

   .. attribute:: setstmt
      :type: VariableSetStmt*

      SET or RESET subcommand


.. class:: AlterDatabaseStmt(dbname=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3287>`__ parser node.

   .. attribute:: dbname
      :type: str

      Name of database to alter

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterDefaultPrivilegesStmt(options=None, action=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2091>`__ parser node.

   .. attribute:: options
      :type: tuple

      List of DefElem

   .. attribute:: action
      :type: GrantStmt*

      GRANT/REVOKE action (with objects=NIL)


.. class:: AlterDomainStmt(subtype=None, typeName=None, name=None, def_=None, behavior=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1981>`__ parser node.

   .. attribute:: subtype
      :type: str

      * T = alter column default
      * N = alter column drop not null
      * O = alter column set not null
      * C = add constraint
      * X = drop constraint

   .. attribute:: typeName
      :type: tuple

      Domain to work on

   .. attribute:: name
      :type: str

      Column or constraint name to act on

   .. attribute:: def_
      :type: Node

      Definition of default or constraint

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE for DROP cases

   .. attribute:: missing_ok
      :type: bool

      Skip error if missing?


.. class:: AlterEnumStmt(typeName=None, oldVal=None, newVal=None, newValNeighbor=None, newValIsAfter=None, skipIfNewValExists=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3229>`__ parser node.

   .. attribute:: typeName
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: oldVal
      :type: str

      Old enum value's name, if renaming

   .. attribute:: newVal
      :type: str

      New enum value's name

   .. attribute:: newValNeighbor
      :type: str

      Neighboring enum value, if specified

   .. attribute:: newValIsAfter
      :type: bool

      Place new enum value after neighbor?

   .. attribute:: skipIfNewValExists
      :type: bool

      No error if new already exists?


.. class:: AlterEventTrigStmt(trigname=None, tgenabled=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2567>`__ parser node.

   .. attribute:: trigname
      :type: str

      TRIGGER's name

   .. attribute:: tgenabled
      :type: str

      Trigger's firing configuration WRT
      session_replication_role


.. class:: AlterExtensionContentsStmt(extname=None, action=None, objtype=None, object=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2360>`__ parser node.

   .. attribute:: extname
      :type: str

      Extension's name

   .. attribute:: action
      :type: int

      +1 = add object, -1 = drop object

   .. attribute:: objtype
      :type: ObjectType

      Object's type

   .. attribute:: object
      :type: Node

      Qualified name of the object


.. class:: AlterExtensionStmt(extname=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2353>`__ parser node.

   .. attribute:: extname
      :type: str

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterFdwStmt(fdwname=None, func_options=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2382>`__ parser node.

   .. attribute:: fdwname
      :type: str

      Foreign-data wrapper name

   .. attribute:: func_options
      :type: tuple

      HANDLER/VALIDATOR options

   .. attribute:: options
      :type: tuple

      Generic options to FDW


.. class:: AlterForeignServerStmt(servername=None, version=None, options=None, has_version=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2406>`__ parser node.

   .. attribute:: servername
      :type: str

      Server name

   .. attribute:: version
      :type: str

      Optional server version

   .. attribute:: options
      :type: tuple

      Generic options to server

   .. attribute:: has_version
      :type: bool

      Version specified


.. class:: AlterFunctionStmt(objtype=None, func=None, actions=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2984>`__ parser node.

   .. attribute:: objtype
      :type: ObjectType

   .. attribute:: func
      :type: ObjectWithArgs*

      Name and args of function

   .. attribute:: actions
      :type: tuple

      List of DefElem


.. class:: AlterObjectDependsStmt(objectType=None, relation=None, object=None, extname=None, remove=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3058>`__ parser node.

   .. attribute:: objectType
      :type: ObjectType

      OBJECT_FUNCTION, OBJECT_TRIGGER, etc

   .. attribute:: relation
      :type: RangeVar*

      In case a table is involved

   .. attribute:: object
      :type: Node

      Name of the object

   .. attribute:: extname
      :type: Value*

      Extension name

   .. attribute:: remove
      :type: bool

      Set true to remove dep rather than add


.. class:: AlterObjectSchemaStmt(objectType=None, relation=None, object=None, newschema=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3072>`__ parser node.

   .. attribute:: objectType
      :type: ObjectType

      OBJECT_TABLE, OBJECT_TYPE, etc

   .. attribute:: relation
      :type: RangeVar*

      In case it's a table

   .. attribute:: object
      :type: Node

      In case it's some other object

   .. attribute:: newschema
      :type: str

      The new schema

   .. attribute:: missing_ok
      :type: bool

      Skip error if missing?


.. class:: AlterOpFamilyStmt(opfamilyname=None, amname=None, isDrop=None, items=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2737>`__ parser node.

   .. attribute:: opfamilyname
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: amname
      :type: str

      Name of index AM opfamily is for

   .. attribute:: isDrop
      :type: bool

      ADD or DROP the items?

   .. attribute:: items
      :type: tuple

      List of CreateOpClassItem nodes


.. class:: AlterOperatorStmt(opername=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3099>`__ parser node.

   .. attribute:: opername
      :type: ObjectWithArgs*

      Operator name and argument types

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterOwnerStmt(objectType=None, relation=None, object=None, newowner=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3086>`__ parser node.

   .. attribute:: objectType
      :type: ObjectType

      OBJECT_TABLE, OBJECT_TYPE, etc

   .. attribute:: relation
      :type: RangeVar*

      In case it's a table

   .. attribute:: object
      :type: Node

      In case it's some other object

   .. attribute:: newowner
      :type: RoleSpec*

      The new owner


.. class:: AlterPolicyStmt(policy_name=None, table=None, roles=None, qual=None, with_check=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2500>`__ parser node.

   .. attribute:: policy_name
      :type: str

      Policy's name

   .. attribute:: table
      :type: RangeVar*

      The table name the policy applies to

   .. attribute:: roles
      :type: tuple

      The roles associated with the policy

   .. attribute:: qual
      :type: Node

      The policy's condition

   .. attribute:: with_check
      :type: Node

      The policy's WITH CHECK condition.


.. class:: AlterPublicationStmt(pubname=None, options=None, tables=None, for_all_tables=None, tableAction=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3637>`__ parser node.

   .. attribute:: pubname
      :type: str

      Name of the publication

   .. attribute:: options
      :type: tuple

      List of DefElem nodes

   .. attribute:: tables
      :type: tuple

      List of tables to add/drop

   .. attribute:: for_all_tables
      :type: bool

      Special publication for all tables in db

   .. attribute:: tableAction
      :type: DefElemAction

      What action to perform with the tables


.. class:: AlterRoleSetStmt(role=None, database=None, setstmt=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2622>`__ parser node.

   .. attribute:: role
      :type: RoleSpec*

      Role

   .. attribute:: database
      :type: str

      Database name, or NULL

   .. attribute:: setstmt
      :type: VariableSetStmt*

      SET or RESET subcommand


.. class:: AlterRoleStmt(role=None, options=None, action=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2614>`__ parser node.

   .. attribute:: role
      :type: RoleSpec*

      Role

   .. attribute:: options
      :type: tuple

      List of DefElem nodes

   .. attribute:: action
      :type: int

      +1 = add members, -1 = drop members


.. class:: AlterSeqStmt(sequence=None, options=None, for_identity=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2652>`__ parser node.

   .. attribute:: sequence
      :type: RangeVar*

      The sequence to alter

   .. attribute:: options
      :type: tuple

   .. attribute:: for_identity
      :type: bool

   .. attribute:: missing_ok
      :type: bool

      Skip error if a role is missing?


.. class:: AlterStatsStmt(defnames=None, stxstattarget=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2939>`__ parser node.

   .. attribute:: defnames
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: stxstattarget
      :type: int

      Statistics target

   .. attribute:: missing_ok
      :type: bool

      Skip error if statistics object is missing


.. class:: AlterSubscriptionStmt(kind=None, subname=None, conninfo=None, publication=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3671>`__ parser node.

   .. attribute:: kind
      :type: AlterSubscriptionType

      ALTER_SUBSCRIPTION_OPTIONS, etc

   .. attribute:: subname
      :type: str

      Name of the subscription

   .. attribute:: conninfo
      :type: str

      Connection string to publisher

   .. attribute:: publication
      :type: tuple

      One or more publication to subscribe to

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterSystemStmt(setstmt=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3317>`__ parser node.

   .. attribute:: setstmt
      :type: VariableSetStmt*

      SET subcommand


.. class:: AlterTSConfigurationStmt(kind=None, cfgname=None, tokentype=None, dicts=None, override=None, replace=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3610>`__ parser node.

   .. attribute:: kind
      :type: AlterTSConfigType

      ALTER_TSCONFIG_ADD_MAPPING, etc

   .. attribute:: cfgname
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: tokentype
      :type: tuple

      List of Value strings

   .. attribute:: dicts
      :type: tuple

      List of list of Value strings

   .. attribute:: override
      :type: bool

      If true - remove old variant

   .. attribute:: replace
      :type: bool

      If true - replace dictionary by another

   .. attribute:: missing_ok
      :type: bool

      For DROP - skip error if missing?


.. class:: AlterTSDictionaryStmt(dictname=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3591>`__ parser node.

   .. attribute:: dictname
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterTableCmd(subtype=None, name=None, num=None, newowner=None, def_=None, behavior=None, missing_ok=None, recurse=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1946>`__ parser node.

   .. attribute:: subtype
      :type: AlterTableType

      Type of table alteration to apply

   .. attribute:: name
      :type: str

      Column, constraint, or trigger to act on,
      or tablespace

   .. attribute:: num
      :type: int16

      Attribute number for columns referenced by
      number

   .. attribute:: newowner
      :type: RoleSpec*

   .. attribute:: def_
      :type: Node

      Definition of new column, index,
      constraint, or parent table

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE for DROP cases

   .. attribute:: missing_ok
      :type: bool

      Skip error if missing?

   .. attribute:: recurse
      :type: bool

      Exec-time recursion


.. class:: AlterTableMoveAllStmt(orig_tablespacename=None, objtype=None, roles=None, new_tablespacename=None, nowait=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2329>`__ parser node.

   .. attribute:: orig_tablespacename
      :type: str

   .. attribute:: objtype
      :type: ObjectType

      Object type to move

   .. attribute:: roles
      :type: tuple

      List of roles to move objects of

   .. attribute:: new_tablespacename
      :type: str

   .. attribute:: nowait
      :type: bool


.. class:: AlterTableSpaceOptionsStmt(tablespacename=None, options=None, isReset=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2321>`__ parser node.

   .. attribute:: tablespacename
      :type: str

   .. attribute:: options
      :type: tuple

   .. attribute:: isReset
      :type: bool


.. class:: AlterTableStmt(relation=None, cmds=None, objtype=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1856>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      Table to work on

   .. attribute:: cmds
      :type: tuple

      List of subcommands

   .. attribute:: objtype
      :type: ObjectType

      Type of object

   .. attribute:: missing_ok
      :type: bool

      Skip error if table missing


.. class:: AlterTypeStmt(typeName=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3110>`__ parser node.

   .. attribute:: typeName
      :type: tuple

      Type name (possibly qualified)

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterUserMappingStmt(user=None, servername=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2441>`__ parser node.

   .. attribute:: user
      :type: RoleSpec*

      User role

   .. attribute:: servername
      :type: str

      Server name

   .. attribute:: options
      :type: tuple

      Generic options to server


.. class:: AlternativeSubPlan(subplans=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L780>`__ parser node.

   .. attribute:: subplans
      :type: tuple

      SubPlan(s) with equivalent results


.. class:: ArrayCoerceExpr(arg=None, elemexpr=None, resulttypmod=None, coerceformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L891>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input expression (yields an array)

   .. attribute:: elemexpr
      :type: Expr*

      Expression representing per-element work

   .. attribute:: resulttypmod
      :type: int32

      Output typmod (also element typmod)

   .. attribute:: coerceformat
      :type: CoercionForm

      How to display this node

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: ArrayExpr(elements=None, multidims=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1021>`__ parser node.

   .. attribute:: elements
      :type: tuple

      The array elements or sub-arrays

   .. attribute:: multidims
      :type: bool

      True if elements are sub-arrays

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: BoolExpr(boolop=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L612>`__ parser node.

   .. attribute:: boolop
      :type: BoolExprType

   .. attribute:: args
      :type: tuple

      Arguments to this expression

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: BooleanTest(arg=None, booltesttype=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1275>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input expression

   .. attribute:: booltesttype
      :type: BoolTestType

      Test type

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CTECycleClause(cycle_col_list=None, cycle_mark_column=None, cycle_mark_value=None, cycle_mark_default=None, cycle_path_column=None, location=None, cycle_mark_typmod=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1481>`__ parser node.

   .. attribute:: cycle_col_list
      :type: tuple

   .. attribute:: cycle_mark_column
      :type: str

   .. attribute:: cycle_mark_value
      :type: Node

   .. attribute:: cycle_mark_default
      :type: Node

   .. attribute:: cycle_path_column
      :type: str

   .. attribute:: location
      :type: int

   .. attribute:: cycle_mark_typmod
      :type: int


.. class:: CTESearchClause(search_col_list=None, search_breadth_first=None, search_seq_column=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1472>`__ parser node.

   .. attribute:: search_col_list
      :type: tuple

   .. attribute:: search_breadth_first
      :type: bool

   .. attribute:: search_seq_column
      :type: str

   .. attribute:: location
      :type: int


.. class:: CallContext(atomic=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3030>`__ parser node.

   .. attribute:: atomic
      :type: bool


.. class:: CallStmt(funccall=None, funcexpr=None, outargs=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3022>`__ parser node.

   .. attribute:: funccall
      :type: FuncCall*

      From the parser

   .. attribute:: funcexpr
      :type: FuncExpr*

      Transformed call, with only input args

   .. attribute:: outargs
      :type: tuple

      Transformed output-argument expressions


.. class:: CaseExpr(arg=None, args=None, defresult=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L963>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Implicit equality comparison argument

   .. attribute:: args
      :type: tuple

      The arguments (list of WHEN clauses)

   .. attribute:: defresult
      :type: Expr*

      The default result (ELSE clause)

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CaseTestExpr(typeMod=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1005>`__ parser node.

   .. attribute:: typeMod
      :type: int32

      Typemod for substituted value


.. class:: CaseWhen(expr=None, result=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L977>`__ parser node.

   .. attribute:: expr
      :type: Expr*

      Condition expression

   .. attribute:: result
      :type: Expr*

      Substitution result

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CheckPointStmt()

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3419>`__ parser node.


.. class:: ClosePortalStmt(portalname=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2830>`__ parser node.

   .. attribute:: portalname
      :type: str

      Name of the portal (cursor)


.. class:: ClusterStmt(relation=None, indexname=None, params=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3327>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      Relation being indexed, or NULL if all

   .. attribute:: indexname
      :type: str

      Original index defined

   .. attribute:: params
      :type: tuple

      List of DefElem nodes


.. class:: CoalesceExpr(args=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1117>`__ parser node.

   .. attribute:: args
      :type: tuple

      The arguments

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CoerceToDomain(arg=None, resulttypmod=None, coercionformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1292>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input expression

   .. attribute:: resulttypmod
      :type: int32

      Output typmod (currently always -1)

   .. attribute:: coercionformat
      :type: CoercionForm

      How to display this node

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CoerceToDomainValue(typeMod=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1312>`__ parser node.

   .. attribute:: typeMod
      :type: int32

      Typemod for substituted value

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CoerceViaIO(arg=None, coerceformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L867>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input expression

   .. attribute:: coerceformat
      :type: CoercionForm

      How to display this node

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CollateClause(arg=None, collname=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L316>`__ parser node.

   .. attribute:: arg
      :type: Node

      Input expression

   .. attribute:: collname
      :type: tuple

      Possibly-qualified collation name

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CollateExpr(arg=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L933>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input expression

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: ColumnDef(colname=None, typeName=None, compression=None, inhcount=None, is_local=None, is_not_null=None, is_from_type=None, storage=None, raw_default=None, cooked_default=None, identity=None, identitySequence=None, generated=None, collClause=None, constraints=None, fdwoptions=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L655>`__ parser node.

   .. attribute:: colname
      :type: str

      Name of column

   .. attribute:: typeName
      :type: TypeName*

      Type of column

   .. attribute:: compression
      :type: str

      Compression method for column

   .. attribute:: inhcount
      :type: int

      Number of times column is inherited

   .. attribute:: is_local
      :type: bool

      Column has local (non-inherited) def'n

   .. attribute:: is_not_null
      :type: bool

      NOT NULL constraint specified?

   .. attribute:: is_from_type
      :type: bool

      Column definition came from table type

   .. attribute:: storage
      :type: str

      Attstorage setting, or 0 for default

   .. attribute:: raw_default
      :type: Node

      Default value (untransformed parse tree)

   .. attribute:: cooked_default
      :type: Node

      Default value (transformed expr tree)

   .. attribute:: identity
      :type: str

      Attidentity setting

   .. attribute:: identitySequence
      :type: RangeVar*

      To store identity sequence name for
      ALTER TABLE ... ADD COLUMN

   .. attribute:: generated
      :type: str

      Attgenerated setting

   .. attribute:: collClause
      :type: CollateClause*

      Untransformed COLLATE spec, if any

   .. attribute:: constraints
      :type: tuple

      Other constraints on column

   .. attribute:: fdwoptions
      :type: tuple

      Per-column FDW options

   .. attribute:: location
      :type: int

      Parse location, or -1 if none/unknown


.. class:: ColumnRef(fields=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L244>`__ parser node.

   .. attribute:: fields
      :type: tuple

      Field names (Value strings) or A_Star

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CommentStmt(objtype=None, object=None, comment=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2777>`__ parser node.

   .. attribute:: objtype
      :type: ObjectType

      Object's type

   .. attribute:: object
      :type: Node

      Qualified name of the object

   .. attribute:: comment
      :type: str

      Comment to insert, or NULL to remove


.. class:: CommonTableExpr(ctename=None, aliascolnames=None, ctematerialized=None, ctequery=None, search_clause=None, cycle_clause=None, location=None, cterecursive=None, cterefcount=None, ctecolnames=None, ctecoltypes=None, ctecoltypmods=None, ctecolcollations=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1497>`__ parser node.

   .. attribute:: ctename
      :type: str

      Query name (never qualified)

   .. attribute:: aliascolnames
      :type: tuple

      Optional list of column names

   .. attribute:: ctematerialized
      :type: CTEMaterialize

      Is this an optimization fence?

   .. attribute:: ctequery
      :type: Node

      The CTE's subquery

   .. attribute:: search_clause
      :type: CTESearchClause*

   .. attribute:: cycle_clause
      :type: CTECycleClause*

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown

   .. attribute:: cterecursive
      :type: bool

      Is this CTE actually recursive?

   .. attribute:: cterefcount
      :type: int

      Number of RTEs referencing this CTE
      (excluding internal self-references)

   .. attribute:: ctecolnames
      :type: tuple

      List of output column names

   .. attribute:: ctecoltypes
      :type: tuple

      OID list of output column type OIDs

   .. attribute:: ctecoltypmods
      :type: tuple

      Integer list of output column typmods

   .. attribute:: ctecolcollations
      :type: tuple

      OID list of column collation OIDs


.. class:: CompositeTypeStmt(typevar=None, coldeflist=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3196>`__ parser node.

   .. attribute:: typevar
      :type: RangeVar*

      The composite type to be created

   .. attribute:: coldeflist
      :type: tuple

      List of ColumnDef nodes


.. class:: Constraint(contype=None, conname=None, deferrable=None, initdeferred=None, location=None, is_no_inherit=None, raw_expr=None, cooked_expr=None, generated_when=None, keys=None, including=None, exclusions=None, options=None, indexname=None, indexspace=None, reset_default_tblspc=None, access_method=None, where_clause=None, pktable=None, fk_attrs=None, pk_attrs=None, fk_matchtype=None, fk_upd_action=None, fk_del_action=None, old_conpfeqop=None, skip_validation=None, initially_valid=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2248>`__ parser node.

   .. attribute:: contype
      :type: ConstrType

   .. attribute:: conname
      :type: str

      Constraint name, or NULL if unnamed

   .. attribute:: deferrable
      :type: bool

      DEFERRABLE?

   .. attribute:: initdeferred
      :type: bool

      INITIALLY DEFERRED?

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown

   .. attribute:: is_no_inherit
      :type: bool

      Is constraint non-inheritable?

   .. attribute:: raw_expr
      :type: Node

      Expr, as untransformed parse tree

   .. attribute:: cooked_expr
      :type: str

      Expr, as nodeToString representation

   .. attribute:: generated_when
      :type: str

      ALWAYS or BY DEFAULT

   .. attribute:: keys
      :type: tuple

      String nodes naming referenced key
      column(s)

   .. attribute:: including
      :type: tuple

      String nodes naming referenced nonkey
      column(s)

   .. attribute:: exclusions
      :type: tuple

      List of (IndexElem, operator name) pairs

   .. attribute:: options
      :type: tuple

      Options from WITH clause

   .. attribute:: indexname
      :type: str

      Existing index to use; otherwise NULL

   .. attribute:: indexspace
      :type: str

      Index tablespace; NULL for default

   .. attribute:: reset_default_tblspc
      :type: bool

      Reset default_tablespace prior to
      creating the index

   .. attribute:: access_method
      :type: str

      Index access method; NULL for default

   .. attribute:: where_clause
      :type: Node

      Partial index predicate

   .. attribute:: pktable
      :type: RangeVar*

      Primary key table

   .. attribute:: fk_attrs
      :type: tuple

      Attributes of foreign key

   .. attribute:: pk_attrs
      :type: tuple

      Corresponding attrs in PK table

   .. attribute:: fk_matchtype
      :type: str

      FULL, PARTIAL, SIMPLE

   .. attribute:: fk_upd_action
      :type: str

      ON UPDATE action

   .. attribute:: fk_del_action
      :type: str

      ON DELETE action

   .. attribute:: old_conpfeqop
      :type: tuple

      Pg_constraint.conpfeqop of my former self

   .. attribute:: skip_validation
      :type: bool

      Skip validation of existing rows?

   .. attribute:: initially_valid
      :type: bool

      Mark the new constraint as valid?


.. class:: ConstraintsSetStmt(constraints=None, deferred=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3459>`__ parser node.

   .. attribute:: constraints
      :type: tuple

      List of names as RangeVars

   .. attribute:: deferred
      :type: bool


.. class:: ConvertRowtypeExpr(arg=None, convertformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L916>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input expression

   .. attribute:: convertformat
      :type: CoercionForm

      How to display this node

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: CopyStmt(relation=None, query=None, attlist=None, is_from=None, is_program=None, filename=None, options=None, whereClause=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2106>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      The relation to copy

   .. attribute:: query
      :type: Node

      The query (SELECT or DML statement with
      RETURNING) to copy, as a raw parse tree

   .. attribute:: attlist
      :type: tuple

      List of column names (as Strings), or NIL
      for all columns

   .. attribute:: is_from
      :type: bool

      TO or FROM

   .. attribute:: is_program
      :type: bool

      Is 'filename' a program to popen?

   .. attribute:: filename
      :type: str

      Filename, or NULL for STDIN/STDOUT

   .. attribute:: options
      :type: tuple

      List of DefElem nodes

   .. attribute:: whereClause
      :type: Node

      WHERE condition (or NULL)


.. class:: CreateAmStmt(amname=None, handler_name=None, amtype=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2514>`__ parser node.

   .. attribute:: amname
      :type: str

      Access method name

   .. attribute:: handler_name
      :type: tuple

      Handler function name

   .. attribute:: amtype
      :type: str

      Type of access method


.. class:: CreateCastStmt(sourcetype=None, targettype=None, func=None, context=None, inout=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3507>`__ parser node.

   .. attribute:: sourcetype
      :type: TypeName*

   .. attribute:: targettype
      :type: TypeName*

   .. attribute:: func
      :type: ObjectWithArgs*

   .. attribute:: context
      :type: CoercionContext

   .. attribute:: inout
      :type: bool


.. class:: CreateConversionStmt(conversion_name=None, for_encoding_name=None, to_encoding_name=None, func_name=None, def_=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3493>`__ parser node.

   .. attribute:: conversion_name
      :type: tuple

      Name of the conversion

   .. attribute:: for_encoding_name
      :type: str

      Source encoding name

   .. attribute:: to_encoding_name
      :type: str

      Destination encoding name

   .. attribute:: func_name
      :type: tuple

      Qualified conversion function name

   .. attribute:: def_
      :type: bool

      Is this a default conversion?


.. class:: CreateDomainStmt(domainname=None, typeName=None, collClause=None, constraints=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2681>`__ parser node.

   .. attribute:: domainname
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: typeName
      :type: TypeName*

      The base type

   .. attribute:: collClause
      :type: CollateClause*

      Untransformed COLLATE spec, if any

   .. attribute:: constraints
      :type: tuple

      Constraints (list of Constraint nodes)


.. class:: CreateEnumStmt(typeName=None, vals=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3207>`__ parser node.

   .. attribute:: typeName
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: vals
      :type: tuple

      Enum values (list of Value strings)


.. class:: CreateEventTrigStmt(trigname=None, eventname=None, whenclause=None, funcname=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2554>`__ parser node.

   .. attribute:: trigname
      :type: str

      TRIGGER's name

   .. attribute:: eventname
      :type: str

      Event's identifier

   .. attribute:: whenclause
      :type: tuple

      List of DefElems indicating filtering

   .. attribute:: funcname
      :type: tuple

      Qual. name of function to call


.. class:: CreateExtensionStmt(extname=None, if_not_exists=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2344>`__ parser node.

   .. attribute:: extname
      :type: str

   .. attribute:: if_not_exists
      :type: bool

      Just do nothing if it already exists?

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: CreateFdwStmt(fdwname=None, func_options=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2374>`__ parser node.

   .. attribute:: fdwname
      :type: str

      Foreign-data wrapper name

   .. attribute:: func_options
      :type: tuple

      HANDLER/VALIDATOR options

   .. attribute:: options
      :type: tuple

      Generic options to FDW


.. class:: CreateForeignServerStmt(servername=None, servertype=None, version=None, fdwname=None, if_not_exists=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2395>`__ parser node.

   .. attribute:: servername
      :type: str

      Server name

   .. attribute:: servertype
      :type: str

      Optional server type

   .. attribute:: version
      :type: str

      Optional server version

   .. attribute:: fdwname
      :type: str

      FDW name

   .. attribute:: if_not_exists
      :type: bool

      Just do nothing if it already exists?

   .. attribute:: options
      :type: tuple

      Generic options to server


.. class:: CreateForeignTableStmt(base=None, servername=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2420>`__ parser node.

   .. attribute:: base
      :type: CreateStmt

   .. attribute:: servername
      :type: str

   .. attribute:: options
      :type: tuple


.. class:: CreateFunctionStmt(is_procedure=None, replace=None, funcname=None, parameters=None, returnType=None, options=None, sql_body=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2951>`__ parser node.

   .. attribute:: is_procedure
      :type: bool

      It's really CREATE PROCEDURE

   .. attribute:: replace
      :type: bool

      T => replace if already exists

   .. attribute:: funcname
      :type: tuple

      Qualified name of function to create

   .. attribute:: parameters
      :type: tuple

      A list of FunctionParameter

   .. attribute:: returnType
      :type: TypeName*

      The return type

   .. attribute:: options
      :type: tuple

      A list of DefElem

   .. attribute:: sql_body
      :type: Node


.. class:: CreateOpClassItem(itemtype=None, name=None, number=None, order_family=None, class_args=None, storedtype=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2709>`__ parser node.

   .. attribute:: itemtype
      :type: int

      See codes above

   .. attribute:: name
      :type: ObjectWithArgs*

      Operator or function name and args

   .. attribute:: number
      :type: int

      Strategy num or support proc num

   .. attribute:: order_family
      :type: tuple

      Only used for ordering operators

   .. attribute:: class_args
      :type: tuple

      Amproclefttype/amprocrighttype or
      amoplefttype/amoprighttype

   .. attribute:: storedtype
      :type: TypeName*

      Datatype stored in index


.. class:: CreateOpClassStmt(opclassname=None, opfamilyname=None, amname=None, datatype=None, items=None, isDefault=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2694>`__ parser node.

   .. attribute:: opclassname
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: opfamilyname
      :type: tuple

      Qualified name (ditto); NIL if omitted

   .. attribute:: amname
      :type: str

      Name of index AM opclass is for

   .. attribute:: datatype
      :type: TypeName*

      Datatype of indexed column

   .. attribute:: items
      :type: tuple

      List of CreateOpClassItem nodes

   .. attribute:: isDefault
      :type: bool

      Should be marked as default for type?


.. class:: CreateOpFamilyStmt(opfamilyname=None, amname=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2726>`__ parser node.

   .. attribute:: opfamilyname
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: amname
      :type: str

      Name of index AM opfamily is for


.. class:: CreatePLangStmt(replace=None, plname=None, plhandler=None, plinline=None, plvalidator=None, pltrusted=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2579>`__ parser node.

   .. attribute:: replace
      :type: bool

      T => replace if already exists

   .. attribute:: plname
      :type: str

      PL name

   .. attribute:: plhandler
      :type: tuple

      PL call handler function (qual. name)

   .. attribute:: plinline
      :type: tuple

      Optional inline function (qual. name)

   .. attribute:: plvalidator
      :type: tuple

      Optional validator function (qual. name)

   .. attribute:: pltrusted
      :type: bool

      PL is trusted


.. class:: CreatePolicyStmt(policy_name=None, table=None, cmd_name=None, permissive=None, roles=None, qual=None, with_check=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2484>`__ parser node.

   .. attribute:: policy_name
      :type: str

      Policy's name

   .. attribute:: table
      :type: RangeVar*

      The table name the policy applies to

   .. attribute:: cmd_name
      :type: str

      The command name the policy applies to

   .. attribute:: permissive
      :type: bool

      Restrictive or permissive policy

   .. attribute:: roles
      :type: tuple

      The roles associated with the policy

   .. attribute:: qual
      :type: Node

      The policy's condition

   .. attribute:: with_check
      :type: Node

      The policy's WITH CHECK condition.


.. class:: CreatePublicationStmt(pubname=None, options=None, tables=None, for_all_tables=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3628>`__ parser node.

   .. attribute:: pubname
      :type: str

      Name of the publication

   .. attribute:: options
      :type: tuple

      List of DefElem nodes

   .. attribute:: tables
      :type: tuple

      Optional list of tables to add

   .. attribute:: for_all_tables
      :type: bool

      Special publication for all tables in db


.. class:: CreateRangeStmt(typeName=None, params=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3218>`__ parser node.

   .. attribute:: typeName
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: params
      :type: tuple

      Range parameters (list of DefElem)


.. class:: CreateRoleStmt(stmt_type=None, role=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2606>`__ parser node.

   .. attribute:: stmt_type
      :type: RoleStmtType

      ROLE/USER/GROUP

   .. attribute:: role
      :type: str

      Role name

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: CreateSchemaStmt(schemaname=None, authrole=None, schemaElts=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1837>`__ parser node.

   .. attribute:: schemaname
      :type: str

      The name of the schema to create

   .. attribute:: authrole
      :type: RoleSpec*

      The owner of the created schema

   .. attribute:: schemaElts
      :type: tuple

      Schema components (list of parsenodes)

   .. attribute:: if_not_exists
      :type: bool

      Just do nothing if schema already exists?


.. class:: CreateSeqStmt(sequence=None, options=None, for_identity=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2642>`__ parser node.

   .. attribute:: sequence
      :type: RangeVar*

      The sequence to create

   .. attribute:: options
      :type: tuple

   .. attribute:: for_identity
      :type: bool

   .. attribute:: if_not_exists
      :type: bool

      Just do nothing if it already exists?


.. class:: CreateStatsStmt(defnames=None, stat_types=None, exprs=None, relations=None, stxcomment=None, transformed=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2908>`__ parser node.

   .. attribute:: defnames
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: stat_types
      :type: tuple

      Stat types (list of Value strings)

   .. attribute:: exprs
      :type: tuple

      Expressions to build statistics on

   .. attribute:: relations
      :type: tuple

      Rels to build stats on (list of RangeVar)

   .. attribute:: stxcomment
      :type: str

      Comment to apply to stats, or NULL

   .. attribute:: transformed
      :type: bool

      True when transformStatsStmt is finished

   .. attribute:: if_not_exists
      :type: bool

      Do nothing if stats name already exists


.. class:: CreateStmt(relation=None, tableElts=None, inhRelations=None, partbound=None, partspec=None, ofTypename=None, constraints=None, options=None, oncommit=None, tablespacename=None, accessMethod=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2168>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      Relation to create

   .. attribute:: tableElts
      :type: tuple

      Column definitions (list of ColumnDef)

   .. attribute:: inhRelations
      :type: tuple

      Relations to inherit from (list of
      RangeVar)

   .. attribute:: partbound
      :type: PartitionBoundSpec*

      FOR VALUES clause

   .. attribute:: partspec
      :type: PartitionSpec*

      PARTITION BY clause

   .. attribute:: ofTypename
      :type: TypeName*

      OF typename

   .. attribute:: constraints
      :type: tuple

      Constraints (list of Constraint nodes)

   .. attribute:: options
      :type: tuple

      Options from WITH clause

   .. attribute:: oncommit
      :type: OnCommitAction

      What do we do at COMMIT?

   .. attribute:: tablespacename
      :type: str

      Table space to use, or NULL

   .. attribute:: accessMethod
      :type: str

      Table access method

   .. attribute:: if_not_exists
      :type: bool

      Just do nothing if it already exists?


.. class:: CreateSubscriptionStmt(subname=None, conninfo=None, publication=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3651>`__ parser node.

   .. attribute:: subname
      :type: str

      Name of the subscription

   .. attribute:: conninfo
      :type: str

      Connection string to publisher

   .. attribute:: publication
      :type: tuple

      One or more publication to subscribe to

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: CreateTableAsStmt(query=None, into=None, objtype=None, is_select_into=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3393>`__ parser node.

   .. attribute:: query
      :type: Node

      The query (see comments above)

   .. attribute:: into
      :type: IntoClause*

      Destination table

   .. attribute:: objtype
      :type: ObjectType

      OBJECT_TABLE or OBJECT_MATVIEW

   .. attribute:: is_select_into
      :type: bool

      It was written as SELECT INTO

   .. attribute:: if_not_exists
      :type: bool

      Just do nothing if it already exists?


.. class:: CreateTableSpaceStmt(tablespacename=None, owner=None, location=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2305>`__ parser node.

   .. attribute:: tablespacename
      :type: str

   .. attribute:: owner
      :type: RoleSpec*

   .. attribute:: location
      :type: str

   .. attribute:: options
      :type: tuple


.. class:: CreateTransformStmt(replace=None, type_name=None, lang=None, fromsql=None, tosql=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3521>`__ parser node.

   .. attribute:: replace
      :type: bool

   .. attribute:: type_name
      :type: TypeName*

   .. attribute:: lang
      :type: str

   .. attribute:: fromsql
      :type: ObjectWithArgs*

   .. attribute:: tosql
      :type: ObjectWithArgs*


.. class:: CreateTrigStmt(replace=None, isconstraint=None, trigname=None, relation=None, funcname=None, args=None, row=None, timing=None, events=None, columns=None, whenClause=None, transitionRels=None, deferrable=None, initdeferred=None, constrrel=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2526>`__ parser node.

   .. attribute:: replace
      :type: bool

      Replace trigger if already exists

   .. attribute:: isconstraint
      :type: bool

      This is a constraint trigger

   .. attribute:: trigname
      :type: str

      TRIGGER's name

   .. attribute:: relation
      :type: RangeVar*

      Relation trigger is on

   .. attribute:: funcname
      :type: tuple

      Qual. name of function to call

   .. attribute:: args
      :type: tuple

      List of (T_String) Values or NIL

   .. attribute:: row
      :type: bool

      ROW/STATEMENT

   .. attribute:: timing
      :type: int16

      BEFORE, AFTER, or INSTEAD

   .. attribute:: events
      :type: int16

      "OR" of INSERT/UPDATE/DELETE/TRUNCATE

   .. attribute:: columns
      :type: tuple

      Column names, or NIL for all columns

   .. attribute:: whenClause
      :type: Node

      Qual expression, or NULL if none

   .. attribute:: transitionRels
      :type: tuple

      TriggerTransition nodes, or NIL if none

   .. attribute:: deferrable
      :type: bool

      [NOT] DEFERRABLE

   .. attribute:: initdeferred
      :type: bool

      INITIALLY {DEFERRED|IMMEDIATE}

   .. attribute:: constrrel
      :type: RangeVar*

      Opposite relation, if RI trigger


.. class:: CreateUserMappingStmt(user=None, servername=None, if_not_exists=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2432>`__ parser node.

   .. attribute:: user
      :type: RoleSpec*

      User role

   .. attribute:: servername
      :type: str

      Server name

   .. attribute:: if_not_exists
      :type: bool

      Just do nothing if it already exists?

   .. attribute:: options
      :type: tuple

      Generic options to server


.. class:: CreatedbStmt(dbname=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3276>`__ parser node.

   .. attribute:: dbname
      :type: str

      Name of database to create

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: CurrentOfExpr(cvarno=None, cursor_name=None, cursor_param=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1349>`__ parser node.

   .. attribute:: cvarno
      :type: Index

      RT index of target relation

   .. attribute:: cursor_name
      :type: str

      Name of referenced cursor, or NULL

   .. attribute:: cursor_param
      :type: int

      Refcursor parameter number, or 0


.. class:: DeallocateStmt(name=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3561>`__ parser node.

   .. attribute:: name
      :type: str

      The name of the plan to remove


.. class:: DeclareCursorStmt(portalname=None, options=None, query=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2818>`__ parser node.

   .. attribute:: portalname
      :type: str

      Name of the portal (cursor)

   .. attribute:: options
      :type: int

      Bitmask of options (see above)

   .. attribute:: query
      :type: Node

      The query (see comments above)


.. class:: DefElem(defnamespace=None, defname=None, arg=None, defaction=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L742>`__ parser node.

   .. attribute:: defnamespace
      :type: str

      NULL if unqualified name

   .. attribute:: defname
      :type: str

   .. attribute:: arg
      :type: Node

      A (Value \*) or a (TypeName \*)

   .. attribute:: defaction
      :type: DefElemAction

      Unspecified action, or SET/ADD/DROP

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: DefineStmt(kind=None, oldstyle=None, defnames=None, args=None, definition=None, if_not_exists=None, replace=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2665>`__ parser node.

   .. attribute:: kind
      :type: ObjectType

      Aggregate, operator, type

   .. attribute:: oldstyle
      :type: bool

      Hack to signal old CREATE AGG syntax

   .. attribute:: defnames
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: args
      :type: tuple

      A list of TypeName (if needed)

   .. attribute:: definition
      :type: tuple

      A list of DefElem

   .. attribute:: if_not_exists
      :type: bool

      Just do nothing if it already exists?

   .. attribute:: replace
      :type: bool

      Replace if already exists?


.. class:: DeleteStmt(relation=None, usingClause=None, whereClause=None, returningList=None, withClause=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1593>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      Relation to delete from

   .. attribute:: usingClause
      :type: tuple

      Optional using clause for more tables

   .. attribute:: whereClause
      :type: Node

      Qualifications

   .. attribute:: returningList
      :type: tuple

      List of expressions to return

   .. attribute:: withClause
      :type: WithClause*

      WITH clause


.. class:: DiscardStmt(target=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3437>`__ parser node.

   .. attribute:: target
      :type: DiscardMode


.. class:: DoStmt(args=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2998>`__ parser node.

   .. attribute:: args
      :type: tuple

      List of DefElem nodes


.. class:: DropOwnedStmt(roles=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3571>`__ parser node.

   .. attribute:: roles
      :type: tuple

   .. attribute:: behavior
      :type: DropBehavior


.. class:: DropRoleStmt(roles=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2630>`__ parser node.

   .. attribute:: roles
      :type: tuple

      List of roles to remove

   .. attribute:: missing_ok
      :type: bool

      Skip error if a role is missing?


.. class:: DropStmt(objects=None, removeType=None, behavior=None, missing_ok=None, concurrent=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2751>`__ parser node.

   .. attribute:: objects
      :type: tuple

      List of names

   .. attribute:: removeType
      :type: ObjectType

      Object type

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE behavior

   .. attribute:: missing_ok
      :type: bool

      Skip error if object is missing?

   .. attribute:: concurrent
      :type: bool

      Drop index concurrently?


.. class:: DropSubscriptionStmt(subname=None, missing_ok=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3681>`__ parser node.

   .. attribute:: subname
      :type: str

      Name of the subscription

   .. attribute:: missing_ok
      :type: bool

      Skip error if missing?

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE behavior


.. class:: DropTableSpaceStmt(tablespacename=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2314>`__ parser node.

   .. attribute:: tablespacename
      :type: str

   .. attribute:: missing_ok
      :type: bool

      Skip error if missing?


.. class:: DropUserMappingStmt(user=None, servername=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2449>`__ parser node.

   .. attribute:: user
      :type: RoleSpec*

      User role

   .. attribute:: servername
      :type: str

      Server name

   .. attribute:: missing_ok
      :type: bool

      Ignore missing mappings


.. class:: DropdbStmt(dbname=None, missing_ok=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3305>`__ parser node.

   .. attribute:: dbname
      :type: str

      Database to drop

   .. attribute:: missing_ok
      :type: bool

      Skip error if db is missing?

   .. attribute:: options
      :type: tuple

      Currently only FORCE is supported


.. class:: ExecuteStmt(name=None, params=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3549>`__ parser node.

   .. attribute:: name
      :type: str

      The name of the plan to execute

   .. attribute:: params
      :type: tuple

      Values to assign to parameters


.. class:: ExplainStmt(query=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3373>`__ parser node.

   .. attribute:: query
      :type: Node

      The query (see comments above)

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: FetchStmt(direction=None, howMany=None, portalname=None, ismove=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2853>`__ parser node.

   .. attribute:: direction
      :type: FetchDirection

   .. attribute:: howMany
      :type: long

      Number of rows, or position argument

   .. attribute:: portalname
      :type: str

      Name of portal (cursor)

   .. attribute:: ismove
      :type: bool

      True if MOVE


.. class:: FieldSelect(arg=None, fieldnum=None, resulttypmod=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L795>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input expression

   .. attribute:: fieldnum
      :type: AttrNumber

      Attribute number of field to extract

   .. attribute:: resulttypmod
      :type: int32

      Output typmod (usually -1)


.. class:: FieldStore(arg=None, newvals=None, fieldnums=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L824>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input tuple value

   .. attribute:: newvals
      :type: tuple

      New value(s) for field(s)

   .. attribute:: fieldnums
      :type: tuple

      Integer list of field attnums


.. class:: FromExpr(fromlist=None, quals=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1550>`__ parser node.

   .. attribute:: fromlist
      :type: tuple

      List of join subtrees

   .. attribute:: quals
      :type: Node

      Qualifiers on join, if any


.. class:: FuncCall(funcname=None, args=None, agg_order=None, agg_filter=None, over=None, agg_within_group=None, agg_star=None, agg_distinct=None, func_variadic=None, funcformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L358>`__ parser node.

   .. attribute:: funcname
      :type: tuple

      Qualified name of function

   .. attribute:: args
      :type: tuple

      The arguments (list of exprs)

   .. attribute:: agg_order
      :type: tuple

      ORDER BY (list of SortBy)

   .. attribute:: agg_filter
      :type: Node

      FILTER clause, if any

   .. attribute:: over
      :type: WindowDef*

      OVER clause, if any

   .. attribute:: agg_within_group
      :type: bool

      ORDER BY appeared in WITHIN GROUP

   .. attribute:: agg_star
      :type: bool

      Argument was really '*'

   .. attribute:: agg_distinct
      :type: bool

      Arguments were labeled DISTINCT

   .. attribute:: func_variadic
      :type: bool

      Last argument was labeled VARIADIC

   .. attribute:: funcformat
      :type: CoercionForm

      How to display this node

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: FuncExpr(funcretset=None, funcvariadic=None, funcformat=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L492>`__ parser node.

   .. attribute:: funcretset
      :type: bool

      True if function returns set

   .. attribute:: funcvariadic
      :type: bool

      True if variadic arguments have been
      combined into an array last argument

   .. attribute:: funcformat
      :type: CoercionForm

      How to display this function call

   .. attribute:: args
      :type: tuple

      Arguments to the function

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: FunctionParameter(name=None, argType=None, mode=None, defexpr=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2975>`__ parser node.

   .. attribute:: name
      :type: str

      Parameter name, or NULL if not given

   .. attribute:: argType
      :type: TypeName*

      TypeName for parameter type

   .. attribute:: mode
      :type: FunctionParameterMode

      IN/OUT/etc

   .. attribute:: defexpr
      :type: Node

      Raw default expr, or NULL if not given


.. class:: GrantRoleStmt(granted_roles=None, grantee_roles=None, is_grant=None, admin_opt=None, grantor=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2076>`__ parser node.

   .. attribute:: granted_roles
      :type: tuple

      List of roles to be granted/revoked

   .. attribute:: grantee_roles
      :type: tuple

      List of member roles to add/delete

   .. attribute:: is_grant
      :type: bool

      True = GRANT, false = REVOKE

   .. attribute:: admin_opt
      :type: bool

      With admin option

   .. attribute:: grantor
      :type: RoleSpec*

      Set grantor to other than current role

   .. attribute:: behavior
      :type: DropBehavior

      Drop behavior (for REVOKE)


.. class:: GrantStmt(is_grant=None, targtype=None, objtype=None, objects=None, privileges=None, grantees=None, grant_option=None, grantor=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2011>`__ parser node.

   .. attribute:: is_grant
      :type: bool

      True = GRANT, false = REVOKE

   .. attribute:: targtype
      :type: GrantTargetType

      Type of the grant target

   .. attribute:: objtype
      :type: ObjectType

      Kind of object being operated on

   .. attribute:: objects
      :type: tuple

      List of RangeVar nodes, ObjectWithArgs
      nodes, or plain names (as Value strings)

   .. attribute:: privileges
      :type: tuple

      List of AccessPriv nodes

   .. attribute:: grantees
      :type: tuple

      List of RoleSpec nodes

   .. attribute:: grant_option
      :type: bool

      Grant or revoke grant option

   .. attribute:: grantor
      :type: RoleSpec*

   .. attribute:: behavior
      :type: DropBehavior

      Drop behavior (for REVOKE)


.. class:: GroupingFunc(args=None, refs=None, cols=None, agglevelsup=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L369>`__ parser node.

   .. attribute:: args
      :type: tuple

      Arguments, not evaluated but kept for
      benefit of EXPLAIN etc.

   .. attribute:: refs
      :type: tuple

      Ressortgrouprefs of arguments

   .. attribute:: cols
      :type: tuple

      Actual column positions set by planner

   .. attribute:: agglevelsup
      :type: Index

      Same as Aggref.agglevelsup

   .. attribute:: location
      :type: int

      Token location


.. class:: GroupingSet(kind=None, content=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1349>`__ parser node.

   .. attribute:: kind
      :type: GroupingSetKind

   .. attribute:: content
      :type: tuple

   .. attribute:: location
      :type: int


.. class:: ImportForeignSchemaStmt(server_name=None, remote_schema=None, local_schema=None, list_type=None, table_list=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2469>`__ parser node.

   .. attribute:: server_name
      :type: str

      FDW server name

   .. attribute:: remote_schema
      :type: str

      Remote schema name to query

   .. attribute:: local_schema
      :type: str

      Local schema to create objects in

   .. attribute:: list_type
      :type: ImportForeignSchemaType

      Type of table list

   .. attribute:: table_list
      :type: tuple

      List of RangeVar

   .. attribute:: options
      :type: tuple

      List of options to pass to FDW


.. class:: IndexElem(name=None, expr=None, indexcolname=None, collation=None, opclass=None, opclassopts=None, ordering=None, nulls_ordering=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L711>`__ parser node.

   .. attribute:: name
      :type: str

      Name of attribute to index, or NULL

   .. attribute:: expr
      :type: Node

      Expression to index, or NULL

   .. attribute:: indexcolname
      :type: str

      Name for index column; NULL = default

   .. attribute:: collation
      :type: tuple

      Name of collation; NIL = default

   .. attribute:: opclass
      :type: tuple

      Name of desired opclass; NIL = default

   .. attribute:: opclassopts
      :type: tuple

      Opclass-specific options, or NIL

   .. attribute:: ordering
      :type: SortByDir

      ASC/DESC/default

   .. attribute:: nulls_ordering
      :type: SortByNulls

      FIRST/LAST/default


.. class:: IndexStmt(idxname=None, relation=None, accessMethod=None, tableSpace=None, indexParams=None, indexIncludingParams=None, options=None, whereClause=None, excludeOpNames=None, idxcomment=None, oldCreateSubid=None, oldFirstRelfilenodeSubid=None, unique=None, primary=None, isconstraint=None, deferrable=None, initdeferred=None, transformed=None, concurrent=None, if_not_exists=None, reset_default_tblspc=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2873>`__ parser node.

   .. attribute:: idxname
      :type: str

      Name of new index, or NULL for default

   .. attribute:: relation
      :type: RangeVar*

      Relation to build index on

   .. attribute:: accessMethod
      :type: str

      Name of access method (eg. btree)

   .. attribute:: tableSpace
      :type: str

      Tablespace, or NULL for default

   .. attribute:: indexParams
      :type: tuple

      Columns to index: a list of IndexElem

   .. attribute:: indexIncludingParams
      :type: tuple

      Additional columns to index: a list
      of IndexElem

   .. attribute:: options
      :type: tuple

      WITH clause options: a list of DefElem

   .. attribute:: whereClause
      :type: Node

      Qualification (partial-index predicate)

   .. attribute:: excludeOpNames
      :type: tuple

      Exclusion operator names, or NIL if none

   .. attribute:: idxcomment
      :type: str

      Comment to apply to index, or NULL

   .. attribute:: oldCreateSubid
      :type: SubTransactionId

      Rd_createSubid of oldNode

   .. attribute:: oldFirstRelfilenodeSubid
      :type: SubTransactionId

      Rd_firstRelfilenodeSubid of
      oldNode

   .. attribute:: unique
      :type: bool

      Is index unique?

   .. attribute:: primary
      :type: bool

      Is index a primary key?

   .. attribute:: isconstraint
      :type: bool

      Is it for a pkey/unique constraint?

   .. attribute:: deferrable
      :type: bool

      Is the constraint DEFERRABLE?

   .. attribute:: initdeferred
      :type: bool

      Is the constraint INITIALLY DEFERRED?

   .. attribute:: transformed
      :type: bool

      True when transformIndexStmt is finished

   .. attribute:: concurrent
      :type: bool

      Should this be a concurrent index build?

   .. attribute:: if_not_exists
      :type: bool

      Just do nothing if index already exists?

   .. attribute:: reset_default_tblspc
      :type: bool

      Reset default_tablespace prior to
      executing


.. class:: InferClause(indexElems=None, whereClause=None, conname=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1435>`__ parser node.

   .. attribute:: indexElems
      :type: tuple

      IndexElems to infer unique index

   .. attribute:: whereClause
      :type: Node

      Qualification (partial-index predicate)

   .. attribute:: conname
      :type: str

      Constraint name, or NULL if unnamed

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: InferenceElem(expr=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1378>`__ parser node.

   .. attribute:: expr
      :type: Node

      Expression to infer from, or NULL


.. class:: InlineCodeBlock(source_text=None, langIsTrusted=None, atomic=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3004>`__ parser node.

   .. attribute:: source_text
      :type: str

      Source text of anonymous code block

   .. attribute:: langIsTrusted
      :type: bool

      Trusted property of the language

   .. attribute:: atomic
      :type: bool

      Atomic execution context


.. class:: InsertStmt(relation=None, cols=None, selectStmt=None, onConflictClause=None, returningList=None, withClause=None, override=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1577>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      Relation to insert into

   .. attribute:: cols
      :type: tuple

      Optional: names of the target columns

   .. attribute:: selectStmt
      :type: Node

      The source SELECT/VALUES, or NULL

   .. attribute:: onConflictClause
      :type: OnConflictClause*

      ON CONFLICT clause

   .. attribute:: returningList
      :type: tuple

      List of expressions to return

   .. attribute:: withClause
      :type: WithClause*

      WITH clause

   .. attribute:: override
      :type: OverridingKind

      OVERRIDING clause


.. class:: IntoClause(rel=None, colNames=None, accessMethod=None, options=None, onCommit=None, tableSpaceName=None, viewQuery=None, skipData=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L108>`__ parser node.

   .. attribute:: rel
      :type: RangeVar*

      Target relation name

   .. attribute:: colNames
      :type: tuple

      Column names to assign, or NIL

   .. attribute:: accessMethod
      :type: str

      Table access method

   .. attribute:: options
      :type: tuple

      Options from WITH clause

   .. attribute:: onCommit
      :type: OnCommitAction

      What do we do at COMMIT?

   .. attribute:: tableSpaceName
      :type: str

      Table space to use, or NULL

   .. attribute:: viewQuery
      :type: Node

      Materialized view's SELECT query

   .. attribute:: skipData
      :type: bool

      True for WITH NO DATA


.. class:: JoinExpr(jointype=None, isNatural=None, larg=None, rarg=None, usingClause=None, join_using_alias=None, quals=None, alias=None, rtindex=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1527>`__ parser node.

   .. attribute:: jointype
      :type: JoinType

      Type of join

   .. attribute:: isNatural
      :type: bool

      Natural join? Will need to shape table

   .. attribute:: larg
      :type: Node

      Left subtree

   .. attribute:: rarg
      :type: Node

      Right subtree

   .. attribute:: usingClause
      :type: tuple

      USING clause, if any (list of String)

   .. attribute:: join_using_alias
      :type: Alias*

      Alias attached to USING clause, if any

   .. attribute:: quals
      :type: Node

      Qualifiers on join, if any

   .. attribute:: alias
      :type: Alias*

      User-written alias clause, if any

   .. attribute:: rtindex
      :type: int

      RT index assigned for join, or 0


.. class:: ListenStmt(conditionname=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3148>`__ parser node.

   .. attribute:: conditionname
      :type: str

      Condition name to listen on


.. class:: LoadStmt(filename=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3266>`__ parser node.

   .. attribute:: filename
      :type: str

      File to load


.. class:: LockStmt(relations=None, mode=None, nowait=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3447>`__ parser node.

   .. attribute:: relations
      :type: tuple

      Relations to lock

   .. attribute:: mode
      :type: int

      Lock mode

   .. attribute:: nowait
      :type: bool

      No wait mode


.. class:: LockingClause(lockedRels=None, strength=None, waitPolicy=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L761>`__ parser node.

   .. attribute:: lockedRels
      :type: tuple

      FOR [KEY] UPDATE/SHARE relations

   .. attribute:: strength
      :type: LockClauseStrength

   .. attribute:: waitPolicy
      :type: LockWaitPolicy

      NOWAIT and SKIP LOCKED


.. class:: MinMaxExpr(op=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1135>`__ parser node.

   .. attribute:: op
      :type: MinMaxOp

      Function to execute

   .. attribute:: args
      :type: tuple

      The arguments

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: MultiAssignRef(source=None, colno=None, ncolumns=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L467>`__ parser node.

   .. attribute:: source
      :type: Node

      The row-valued expression

   .. attribute:: colno
      :type: int

      Column number for this target (1..n)

   .. attribute:: ncolumns
      :type: int

      Number of targets in the construct


.. class:: NamedArgExpr(arg=None, name=None, argnumber=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L521>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      The argument expression

   .. attribute:: name
      :type: str

      The name

   .. attribute:: argnumber
      :type: int

      Argument's number in positional notation

   .. attribute:: location
      :type: int

      Argument name location, or -1 if unknown


.. class:: NotifyStmt(conditionname=None, payload=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3137>`__ parser node.

   .. attribute:: conditionname
      :type: str

      Condition name to notify

   .. attribute:: payload
      :type: str

      The payload string, or NULL if none


.. class:: NullTest(arg=None, nulltesttype=None, argisrow=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1252>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input expression

   .. attribute:: nulltesttype
      :type: NullTestType

      IS NULL, IS NOT NULL

   .. attribute:: argisrow
      :type: bool

      T to perform field-by-field null checks

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: ObjectWithArgs(objname=None, objargs=None, objfuncargs=None, args_unspecified=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2044>`__ parser node.

   .. attribute:: objname
      :type: tuple

      Qualified name of function/operator

   .. attribute:: objargs
      :type: tuple

      List of Typename nodes (input args only)

   .. attribute:: objfuncargs
      :type: tuple

      List of FunctionParameter nodes

   .. attribute:: args_unspecified
      :type: bool

      Argument list was omitted?


.. class:: OnConflictClause(action=None, infer=None, targetList=None, whereClause=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1450>`__ parser node.

   .. attribute:: action
      :type: OnConflictAction

      DO NOTHING or UPDATE?

   .. attribute:: infer
      :type: InferClause*

      Optional index inference clause

   .. attribute:: targetList
      :type: tuple

      The target list (of ResTarget)

   .. attribute:: whereClause
      :type: Node

      Qualifications

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: OnConflictExpr(action=None, arbiterElems=None, arbiterWhere=None, onConflictSet=None, onConflictWhere=None, exclRelIndex=None, exclRelTlist=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1566>`__ parser node.

   .. attribute:: action
      :type: OnConflictAction

      DO NOTHING or UPDATE?

   .. attribute:: arbiterElems
      :type: tuple

      Unique index arbiter list (of
      InferenceElem's)

   .. attribute:: arbiterWhere
      :type: Node

      Unique index arbiter WHERE clause

   .. attribute:: onConflictSet
      :type: tuple

      List of ON CONFLICT SET TargetEntrys

   .. attribute:: onConflictWhere
      :type: Node

      Qualifiers to restrict UPDATE to

   .. attribute:: exclRelIndex
      :type: int

      RT index of 'excluded' relation

   .. attribute:: exclRelTlist
      :type: tuple

      Tlist of the EXCLUDED pseudo relation


.. class:: OpExpr(opretset=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L539>`__ parser node.

   .. attribute:: opretset
      :type: bool

      True if operator returns set

   .. attribute:: args
      :type: tuple

      Arguments to the operator (1 or 2)

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: PLAssignStmt(name=None, indirection=None, nnames=None, val=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1743>`__ parser node.

   .. attribute:: name
      :type: str

      Initial column name

   .. attribute:: indirection
      :type: tuple

      Subscripts and field names, if any

   .. attribute:: nnames
      :type: int

      Number of names to use in ColumnRef

   .. attribute:: val
      :type: SelectStmt*

      The PL/pgSQL expression to assign

   .. attribute:: location
      :type: int

      Name's token location, or -1 if unknown


.. class:: Param(paramkind=None, paramid=None, paramtypmod=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L264>`__ parser node.

   .. attribute:: paramkind
      :type: ParamKind

      Kind of parameter. See above

   .. attribute:: paramid
      :type: int

      Numeric ID for parameter

   .. attribute:: paramtypmod
      :type: int32

      Typmod value, if known

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: ParamRef(number=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L254>`__ parser node.

   .. attribute:: number
      :type: int

      The number of the parameter

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: PartitionBoundSpec(strategy=None, is_default=None, modulus=None, remainder=None, listdatums=None, lowerdatums=None, upperdatums=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L824>`__ parser node.

   .. attribute:: strategy
      :type: str

      See PARTITION_STRATEGY codes above

   .. attribute:: is_default
      :type: bool

      Is it a default partition bound?

   .. attribute:: modulus
      :type: int

   .. attribute:: remainder
      :type: int

   .. attribute:: listdatums
      :type: tuple

      List of Consts (or A_Consts in raw tree)

   .. attribute:: lowerdatums
      :type: tuple

      List of PartitionRangeDatums

   .. attribute:: upperdatums
      :type: tuple

      List of PartitionRangeDatums

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: PartitionCmd(name=None, bound=None, concurrent=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L871>`__ parser node.

   .. attribute:: name
      :type: RangeVar*

      Name of partition to attach/detach

   .. attribute:: bound
      :type: PartitionBoundSpec*

      FOR VALUES, if attaching

   .. attribute:: concurrent
      :type: bool


.. class:: PartitionElem(name=None, expr=None, collation=None, opclass=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L789>`__ parser node.

   .. attribute:: name
      :type: str

      Name of column to partition on, or NULL

   .. attribute:: expr
      :type: Node

      Expression to partition on, or NULL

   .. attribute:: collation
      :type: tuple

      Name of collation; NIL = default

   .. attribute:: opclass
      :type: tuple

      Name of desired opclass; NIL = default

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: PartitionRangeDatum(kind=None, value=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L857>`__ parser node.

   .. attribute:: kind
      :type: PartitionRangeDatumKind

   .. attribute:: value
      :type: Node

      Const (or A_Const in raw tree), if kind is
      PARTITION_RANGE_DATUM_VALUE, else NULL

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: PartitionSpec(strategy=None, partParams=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L804>`__ parser node.

   .. attribute:: strategy
      :type: str

      Partitioning strategy ('hash', 'list' or
      'range')

   .. attribute:: partParams
      :type: tuple

      List of PartitionElems

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: PrepareStmt(name=None, argtypes=None, query=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3535>`__ parser node.

   .. attribute:: name
      :type: str

      Name of plan, arbitrary

   .. attribute:: argtypes
      :type: tuple

      Types of parameters (List of TypeName)

   .. attribute:: query
      :type: Node

      The query itself (as a raw parsetree)


.. class:: Query(commandType=None, querySource=None, queryId=None, canSetTag=None, utilityStmt=None, resultRelation=None, hasAggs=None, hasWindowFuncs=None, hasTargetSRFs=None, hasSubLinks=None, hasDistinctOn=None, hasRecursive=None, hasModifyingCTE=None, hasForUpdate=None, hasRowSecurity=None, isReturn=None, cteList=None, rtable=None, jointree=None, targetList=None, override=None, onConflict=None, returningList=None, groupClause=None, groupDistinct=None, groupingSets=None, havingQual=None, windowClause=None, distinctClause=None, sortClause=None, limitOffset=None, limitCount=None, limitOption=None, rowMarks=None, setOperations=None, constraintDeps=None, withCheckOptions=None, stmt_location=None, stmt_len=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L116>`__ parser node.

   .. attribute:: commandType
      :type: CmdType

      Select|insert|update|delete|utility

   .. attribute:: querySource
      :type: QuerySource

      Where did I come from?

   .. attribute:: queryId
      :type: uint64

      Query identifier (can be set by plugins)

   .. attribute:: canSetTag
      :type: bool

      Do I set the command result tag?

   .. attribute:: utilityStmt
      :type: Node

      Non-null if commandType == CMD_UTILITY

   .. attribute:: resultRelation
      :type: int

      Rtable index of target relation for
      INSERT/UPDATE/DELETE; 0 for SELECT

   .. attribute:: hasAggs
      :type: bool

      Has aggregates in tlist or havingQual

   .. attribute:: hasWindowFuncs
      :type: bool

      Has window functions in tlist

   .. attribute:: hasTargetSRFs
      :type: bool

      Has set-returning functions in tlist

   .. attribute:: hasSubLinks
      :type: bool

      Has subquery SubLink

   .. attribute:: hasDistinctOn
      :type: bool

      DistinctClause is from DISTINCT ON

   .. attribute:: hasRecursive
      :type: bool

      WITH RECURSIVE was specified

   .. attribute:: hasModifyingCTE
      :type: bool

      Has INSERT/UPDATE/DELETE in WITH

   .. attribute:: hasForUpdate
      :type: bool

      FOR [KEY] UPDATE/SHARE was specified

   .. attribute:: hasRowSecurity
      :type: bool

      Rewriter has applied some RLS policy

   .. attribute:: isReturn
      :type: bool

      Is a RETURN statement

   .. attribute:: cteList
      :type: tuple

      WITH list (of CommonTableExpr's)

   .. attribute:: rtable
      :type: tuple

      List of range table entries

   .. attribute:: jointree
      :type: FromExpr*

      Table join tree (FROM and WHERE clauses)

   .. attribute:: targetList
      :type: tuple

      Target list (of TargetEntry)

   .. attribute:: override
      :type: OverridingKind

      OVERRIDING clause

   .. attribute:: onConflict
      :type: OnConflictExpr*

      ON CONFLICT DO [NOTHING | UPDATE]

   .. attribute:: returningList
      :type: tuple

      Return-values list (of TargetEntry)

   .. attribute:: groupClause
      :type: tuple

      A list of SortGroupClause's

   .. attribute:: groupDistinct
      :type: bool

      Is the group by clause distinct?

   .. attribute:: groupingSets
      :type: tuple

      A list of GroupingSet's if present

   .. attribute:: havingQual
      :type: Node

      Qualifications applied to groups

   .. attribute:: windowClause
      :type: tuple

      A list of WindowClause's

   .. attribute:: distinctClause
      :type: tuple

      A list of SortGroupClause's

   .. attribute:: sortClause
      :type: tuple

      A list of SortGroupClause's

   .. attribute:: limitOffset
      :type: Node

      # of result tuples to skip (int8 expr)

   .. attribute:: limitCount
      :type: Node

      # of result tuples to return (int8 expr)

   .. attribute:: limitOption
      :type: LimitOption

      Limit type

   .. attribute:: rowMarks
      :type: tuple

      A list of RowMarkClause's

   .. attribute:: setOperations
      :type: Node

      Set-operation tree if this is top level of
      a UNION/INTERSECT/EXCEPT query

   .. attribute:: constraintDeps
      :type: tuple

      A list of pg_constraint OIDs that the query
      depends on to be semantically valid

   .. attribute:: withCheckOptions
      :type: tuple

      A list of WithCheckOption's (added
      during rewrite)

   .. attribute:: stmt_location
      :type: int

      Start location, or -1 if unknown

   .. attribute:: stmt_len
      :type: int

      Length in bytes; 0 means "rest of string"


.. class:: RangeFunction(lateral=None, ordinality=None, is_rowsfrom=None, functions=None, alias=None, coldeflist=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L572>`__ parser node.

   .. attribute:: lateral
      :type: bool

      Does it have LATERAL prefix?

   .. attribute:: ordinality
      :type: bool

      Does it have WITH ORDINALITY suffix?

   .. attribute:: is_rowsfrom
      :type: bool

      Is result of ROWS FROM() syntax?

   .. attribute:: functions
      :type: tuple

      Per-function information, see above

   .. attribute:: alias
      :type: Alias*

      Table alias & optional column aliases

   .. attribute:: coldeflist
      :type: tuple

      List of ColumnDef nodes to describe result
      of function returning RECORD


.. class:: RangeSubselect(lateral=None, subquery=None, alias=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L550>`__ parser node.

   .. attribute:: lateral
      :type: bool

      Does it have LATERAL prefix?

   .. attribute:: subquery
      :type: Node

      The untransformed sub-select clause

   .. attribute:: alias
      :type: Alias*

      Table alias & optional column aliases


.. class:: RangeTableFunc(lateral=None, docexpr=None, rowexpr=None, namespaces=None, columns=None, alias=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L587>`__ parser node.

   .. attribute:: lateral
      :type: bool

      Does it have LATERAL prefix?

   .. attribute:: docexpr
      :type: Node

      Document expression

   .. attribute:: rowexpr
      :type: Node

      Row generator expression

   .. attribute:: namespaces
      :type: tuple

      List of namespaces as ResTarget

   .. attribute:: columns
      :type: tuple

      List of RangeTableFuncCol

   .. attribute:: alias
      :type: Alias*

      Table alias & optional column aliases

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: RangeTableFuncCol(colname=None, typeName=None, for_ordinality=None, is_not_null=None, colexpr=None, coldefexpr=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L605>`__ parser node.

   .. attribute:: colname
      :type: str

      Name of generated column

   .. attribute:: typeName
      :type: TypeName*

      Type of generated column

   .. attribute:: for_ordinality
      :type: bool

      Does it have FOR ORDINALITY?

   .. attribute:: is_not_null
      :type: bool

      Does it have NOT NULL?

   .. attribute:: colexpr
      :type: Node

      Column filter expression

   .. attribute:: coldefexpr
      :type: Node

      Column default value expression

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: RangeTableSample(relation=None, method=None, args=None, repeatable=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L627>`__ parser node.

   .. attribute:: relation
      :type: Node

      Relation to be sampled

   .. attribute:: method
      :type: tuple

      Sampling method name (possibly qualified)

   .. attribute:: args
      :type: tuple

      Argument(s) for sampling method

   .. attribute:: repeatable
      :type: Node

      REPEATABLE expression, or NULL if none

   .. attribute:: location
      :type: int

      Method name location, or -1 if unknown


.. class:: RangeTblEntry(rtekind=None, relkind=None, rellockmode=None, tablesample=None, subquery=None, security_barrier=None, jointype=None, joinmergedcols=None, joinaliasvars=None, joinleftcols=None, joinrightcols=None, join_using_alias=None, functions=None, funcordinality=None, tablefunc=None, values_lists=None, ctename=None, ctelevelsup=None, self_reference=None, coltypes=None, coltypmods=None, colcollations=None, enrname=None, enrtuples=None, alias=None, eref=None, lateral=None, inh=None, inFromCl=None, requiredPerms=None, selectedCols=None, insertedCols=None, updatedCols=None, extraUpdatedCols=None, securityQuals=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L991>`__ parser node.

   .. attribute:: rtekind
      :type: RTEKind

   .. attribute:: relkind
      :type: str

      Relation kind (see pg_class.relkind)

   .. attribute:: rellockmode
      :type: int

      Lock level that query requires on the rel

   .. attribute:: tablesample
      :type: TableSampleClause*

      Sampling info, or NULL

   .. attribute:: subquery
      :type: Query*

      The sub-query

   .. attribute:: security_barrier
      :type: bool

      Is from security_barrier view?

   .. attribute:: jointype
      :type: JoinType

      Type of join

   .. attribute:: joinmergedcols
      :type: int

      Number of merged (JOIN USING) columns

   .. attribute:: joinaliasvars
      :type: tuple

      List of alias-var expansions

   .. attribute:: joinleftcols
      :type: tuple

      Left-side input column numbers

   .. attribute:: joinrightcols
      :type: tuple

      Right-side input column numbers

   .. attribute:: join_using_alias
      :type: Alias*

   .. attribute:: functions
      :type: tuple

      List of RangeTblFunction nodes

   .. attribute:: funcordinality
      :type: bool

      Is this called WITH ORDINALITY?

   .. attribute:: tablefunc
      :type: TableFunc*

   .. attribute:: values_lists
      :type: tuple

      List of expression lists

   .. attribute:: ctename
      :type: str

      Name of the WITH list item

   .. attribute:: ctelevelsup
      :type: Index

      Number of query levels up

   .. attribute:: self_reference
      :type: bool

      Is this a recursive self-reference?

   .. attribute:: coltypes
      :type: tuple

      OID list of column type OIDs

   .. attribute:: coltypmods
      :type: tuple

      Integer list of column typmods

   .. attribute:: colcollations
      :type: tuple

      OID list of column collation OIDs

   .. attribute:: enrname
      :type: str

      Name of ephemeral named relation

   .. attribute:: enrtuples
      :type: double

      Estimated or actual from caller

   .. attribute:: alias
      :type: Alias*

      User-written alias clause, if any

   .. attribute:: eref
      :type: Alias*

      Expanded reference names

   .. attribute:: lateral
      :type: bool

      Subquery, function, or values is LATERAL?

   .. attribute:: inh
      :type: bool

      Inheritance requested?

   .. attribute:: inFromCl
      :type: bool

      Present in FROM clause?

   .. attribute:: requiredPerms
      :type: AclMode

      Bitmask of required access permissions

   .. attribute:: selectedCols
      :type: Bitmapset*

      Columns needing SELECT permission

   .. attribute:: insertedCols
      :type: Bitmapset*

      Columns needing INSERT permission

   .. attribute:: updatedCols
      :type: Bitmapset*

      Columns needing UPDATE permission

   .. attribute:: extraUpdatedCols
      :type: Bitmapset*

      Generated columns being updated

   .. attribute:: securityQuals
      :type: tuple

      Security barrier quals to apply, if any


.. class:: RangeTblFunction(funcexpr=None, funccolcount=None, funccolnames=None, funccoltypes=None, funccoltypmods=None, funccolcollations=None, funcparams=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1170>`__ parser node.

   .. attribute:: funcexpr
      :type: Node

      Expression tree for func call

   .. attribute:: funccolcount
      :type: int

      Number of columns it contributes to RTE

   .. attribute:: funccolnames
      :type: tuple

      Column names (list of String)

   .. attribute:: funccoltypes
      :type: tuple

      OID list of column type OIDs

   .. attribute:: funccoltypmods
      :type: tuple

      Integer list of column typmods

   .. attribute:: funccolcollations
      :type: tuple

      OID list of column collation OIDs

   .. attribute:: funcparams
      :type: Bitmapset*

      PARAM_EXEC Param IDs affecting this func


.. class:: RangeTblRef(rtindex=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1493>`__ parser node.

   .. attribute:: rtindex
      :type: int


.. class:: RangeVar(catalogname=None, schemaname=None, relname=None, inh=None, relpersistence=None, alias=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L63>`__ parser node.

   .. attribute:: catalogname
      :type: str

      The catalog (database) name, or NULL

   .. attribute:: schemaname
      :type: str

      The schema name, or NULL

   .. attribute:: relname
      :type: str

      The relation/sequence name

   .. attribute:: inh
      :type: bool

      Expand rel by inheritance? recursively act
      on children?

   .. attribute:: relpersistence
      :type: str

      See RELPERSISTENCE_* in pg_class.h

   .. attribute:: alias
      :type: Alias*

      Table alias & optional column aliases

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: RawStmt(stmt=None, stmt_location=None, stmt_len=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1557>`__ parser node.

   .. attribute:: stmt
      :type: Node

      Raw parse tree

   .. attribute:: stmt_location
      :type: int

      Start location, or -1 if unknown

   .. attribute:: stmt_len
      :type: int

      Length in bytes; 0 means "rest of string"


.. class:: ReassignOwnedStmt(roles=None, newrole=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3581>`__ parser node.

   .. attribute:: roles
      :type: tuple

   .. attribute:: newrole
      :type: RoleSpec*


.. class:: RefreshMatViewStmt(concurrent=None, skipData=None, relation=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3407>`__ parser node.

   .. attribute:: concurrent
      :type: bool

      Allow concurrent access?

   .. attribute:: skipData
      :type: bool

      True for WITH NO DATA

   .. attribute:: relation
      :type: RangeVar*

      Relation to insert into


.. class:: ReindexStmt(kind=None, relation=None, name=None, params=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3479>`__ parser node.

   .. attribute:: kind
      :type: ReindexObjectType

      REINDEX_OBJECT_INDEX, REINDEX_OBJECT_TABLE,
      etc.

   .. attribute:: relation
      :type: RangeVar*

      Table or index to reindex

   .. attribute:: name
      :type: str

      Name of database to reindex

   .. attribute:: params
      :type: tuple

      List of DefElem nodes


.. class:: RelabelType(arg=None, resulttypmod=None, relabelformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L847>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      Input expression

   .. attribute:: resulttypmod
      :type: int32

      Output typmod (usually -1)

   .. attribute:: relabelformat
      :type: CoercionForm

      How to display this node

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: RenameStmt(renameType=None, relationType=None, relation=None, object=None, subname=None, newname=None, behavior=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3040>`__ parser node.

   .. attribute:: renameType
      :type: ObjectType

      OBJECT_TABLE, OBJECT_COLUMN, etc

   .. attribute:: relationType
      :type: ObjectType

      If column name, associated relation type

   .. attribute:: relation
      :type: RangeVar*

      In case it's a table

   .. attribute:: object
      :type: Node

      In case it's some other object

   .. attribute:: subname
      :type: str

      Name of contained object (column, rule,
      trigger, etc)

   .. attribute:: newname
      :type: str

      The new name

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE behavior

   .. attribute:: missing_ok
      :type: bool

      Skip error if missing?


.. class:: ReplicaIdentityStmt(identity_type=None, name=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1939>`__ parser node.

   .. attribute:: identity_type
      :type: str

   .. attribute:: name
      :type: str


.. class:: ResTarget(name=None, indirection=None, val=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L449>`__ parser node.

   .. attribute:: name
      :type: str

      Column name or NULL

   .. attribute:: indirection
      :type: tuple

      Subscripts, field names, and '*', or NIL

   .. attribute:: val
      :type: Node

      The value expression to compute or assign

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: ReturnStmt(returnval=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1729>`__ parser node.

   .. attribute:: returnval
      :type: Node


.. class:: RoleSpec(roletype=None, rolename=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L336>`__ parser node.

   .. attribute:: roletype
      :type: RoleSpecType

      Type of this rolespec

   .. attribute:: rolename
      :type: str

      Filled only for ROLESPEC_CSTRING

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: RowCompareExpr(rctype=None, opnos=None, opfamilies=None, inputcollids=None, largs=None, rargs=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1103>`__ parser node.

   .. attribute:: rctype
      :type: RowCompareType

      LT LE GE or GT, never EQ or NE

   .. attribute:: opnos
      :type: tuple

      OID list of pairwise comparison ops

   .. attribute:: opfamilies
      :type: tuple

      OID list of containing operator families

   .. attribute:: inputcollids
      :type: tuple

      OID list of collations for comparisons

   .. attribute:: largs
      :type: tuple

      The left-hand input arguments

   .. attribute:: rargs
      :type: tuple

      The right-hand input arguments


.. class:: RowExpr(args=None, row_format=None, colnames=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1055>`__ parser node.

   .. attribute:: args
      :type: tuple

      The fields

   .. attribute:: row_format
      :type: CoercionForm

      How to display this node

   .. attribute:: colnames
      :type: tuple

      List of String, or NIL

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: RowMarkClause(rti=None, strength=None, waitPolicy=None, pushedDown=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1405>`__ parser node.

   .. attribute:: rti
      :type: Index

      Range table index of target relation

   .. attribute:: strength
      :type: LockClauseStrength

   .. attribute:: waitPolicy
      :type: LockWaitPolicy

      NOWAIT and SKIP LOCKED

   .. attribute:: pushedDown
      :type: bool

      Pushed down from higher query level?


.. class:: RuleStmt(relation=None, rulename=None, whereClause=None, event=None, instead=None, actions=None, replace=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3121>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      Relation the rule is for

   .. attribute:: rulename
      :type: str

      Name of the rule

   .. attribute:: whereClause
      :type: Node

      Qualifications

   .. attribute:: event
      :type: CmdType

      SELECT, INSERT, etc

   .. attribute:: instead
      :type: bool

      Is a 'do instead'?

   .. attribute:: actions
      :type: tuple

      The action statements

   .. attribute:: replace
      :type: bool

      OR REPLACE


.. class:: SQLValueFunction(op=None, typmod=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1176>`__ parser node.

   .. attribute:: op
      :type: SQLValueFunctionOp

      Which function this is

   .. attribute:: typmod
      :type: int32

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: ScalarArrayOpExpr(useOr=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L588>`__ parser node.

   .. attribute:: useOr
      :type: bool

      True for ANY, false for ALL

   .. attribute:: args
      :type: tuple

      The scalar and array operands

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: SecLabelStmt(objtype=None, object=None, provider=None, label=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2789>`__ parser node.

   .. attribute:: objtype
      :type: ObjectType

      Object's type

   .. attribute:: object
      :type: Node

      Qualified name of the object

   .. attribute:: provider
      :type: str

      Label provider (or NULL)

   .. attribute:: label
      :type: str

      New security label to be assigned


.. class:: SelectStmt(distinctClause=None, intoClause=None, targetList=None, fromClause=None, whereClause=None, groupClause=None, groupDistinct=None, havingClause=None, windowClause=None, valuesLists=None, sortClause=None, limitOffset=None, limitCount=None, limitOption=None, lockingClause=None, withClause=None, op=None, all=None, larg=None, rarg=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1639>`__ parser node.

   .. attribute:: distinctClause
      :type: tuple

      NULL, list of DISTINCT ON exprs, or
      lcons(NIL,NIL) for all (SELECT DISTINCT)

   .. attribute:: intoClause
      :type: IntoClause*

      Target for SELECT INTO

   .. attribute:: targetList
      :type: tuple

      The target list (of ResTarget)

   .. attribute:: fromClause
      :type: tuple

      The FROM clause

   .. attribute:: whereClause
      :type: Node

      WHERE qualification

   .. attribute:: groupClause
      :type: tuple

      GROUP BY clauses

   .. attribute:: groupDistinct
      :type: bool

      Is this GROUP BY DISTINCT?

   .. attribute:: havingClause
      :type: Node

      HAVING conditional-expression

   .. attribute:: windowClause
      :type: tuple

      WINDOW window_name AS (...), ...

   .. attribute:: valuesLists
      :type: tuple

      Untransformed list of expression lists

   .. attribute:: sortClause
      :type: tuple

      Sort clause (a list of SortBy's)

   .. attribute:: limitOffset
      :type: Node

      # of result tuples to skip

   .. attribute:: limitCount
      :type: Node

      # of result tuples to return

   .. attribute:: limitOption
      :type: LimitOption

      Limit type

   .. attribute:: lockingClause
      :type: tuple

      FOR UPDATE (list of LockingClause's)

   .. attribute:: withClause
      :type: WithClause*

      WITH clause

   .. attribute:: op
      :type: SetOperation

      Type of set op

   .. attribute:: all
      :type: bool

      ALL specified?

   .. attribute:: larg
      :type: SelectStmt*

      Left child

   .. attribute:: rarg
      :type: SelectStmt*

      Right child


.. class:: SetOperationStmt(op=None, all=None, larg=None, rarg=None, colTypes=None, colTypmods=None, colCollations=None, groupClauses=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1708>`__ parser node.

   .. attribute:: op
      :type: SetOperation

      Type of set op

   .. attribute:: all
      :type: bool

      ALL specified?

   .. attribute:: larg
      :type: Node

      Left child

   .. attribute:: rarg
      :type: Node

      Right child

   .. attribute:: colTypes
      :type: tuple

      OID list of output column type OIDs

   .. attribute:: colTypmods
      :type: tuple

      Integer list of output column typmods

   .. attribute:: colCollations
      :type: tuple

      OID list of output column collation OIDs

   .. attribute:: groupClauses
      :type: tuple

      A list of SortGroupClause's


.. class:: SetToDefault(typeMod=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1328>`__ parser node.

   .. attribute:: typeMod
      :type: int32

      Typemod for substituted value

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: SortBy(node=None, sortby_dir=None, sortby_nulls=None, useOp=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L478>`__ parser node.

   .. attribute:: node
      :type: Node

      Expression to sort on

   .. attribute:: sortby_dir
      :type: SortByDir

      ASC/DESC/USING/default

   .. attribute:: sortby_nulls
      :type: SortByNulls

      NULLS FIRST/LAST

   .. attribute:: useOp
      :type: tuple

      Name of op to use, if SORTBY_USING

   .. attribute:: location
      :type: int

      Operator location, or -1 if none/unknown


.. class:: SortGroupClause(tleSortGroupRef=None, nulls_first=None, hashable=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1280>`__ parser node.

   .. attribute:: tleSortGroupRef
      :type: Index

      Reference into targetlist

   .. attribute:: nulls_first
      :type: bool

      Do NULLs come before normal values?

   .. attribute:: hashable
      :type: bool

      Can eqop be implemented by hashing?


.. class:: StatsElem(name=None, expr=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2927>`__ parser node.

   .. attribute:: name
      :type: str

      Name of attribute to index, or NULL

   .. attribute:: expr
      :type: Node

      Expression to index, or NULL


.. class:: SubLink(subLinkType=None, subLinkId=None, testexpr=None, operName=None, subselect=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L684>`__ parser node.

   .. attribute:: subLinkType
      :type: SubLinkType

   .. attribute:: subLinkId
      :type: int

      ID (1..n); 0 if not MULTIEXPR

   .. attribute:: testexpr
      :type: Node

      Outer-query test for ALL/ANY/ROWCOMPARE

   .. attribute:: operName
      :type: tuple

      Originally specified operator name

   .. attribute:: subselect
      :type: Node

      Subselect as Query* or raw parsetree

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: SubPlan(subLinkType=None, testexpr=None, paramIds=None, plan_id=None, plan_name=None, firstColTypmod=None, useHashTable=None, unknownEqFalse=None, parallel_safe=None, setParam=None, parParam=None, args=None, startup_cost=None, per_call_cost=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L733>`__ parser node.

   .. attribute:: subLinkType
      :type: SubLinkType

   .. attribute:: testexpr
      :type: Node

      OpExpr or RowCompareExpr expression tree

   .. attribute:: paramIds
      :type: tuple

      IDs of Params embedded in the above

   .. attribute:: plan_id
      :type: int

      Index (from 1) in PlannedStmt.subplans

   .. attribute:: plan_name
      :type: str

      A name assigned during planning

   .. attribute:: firstColTypmod
      :type: int32

      Typmod of first column of subplan result

   .. attribute:: useHashTable
      :type: bool

      True to store subselect output in a hash
      table (implies we are doing "IN")

   .. attribute:: unknownEqFalse
      :type: bool

      True if it's okay to return FALSE when the
      spec result is UNKNOWN; this allows much
      simpler handling of null values

   .. attribute:: parallel_safe
      :type: bool

      Is the subplan parallel-safe?

   .. attribute:: setParam
      :type: tuple

      Initplan subqueries have to set these
      Params for parent plan

   .. attribute:: parParam
      :type: tuple

      Indices of input Params from parent plan

   .. attribute:: args
      :type: tuple

      Exprs to pass as parParam values

   .. attribute:: startup_cost
      :type: Cost

      One-time setup cost

   .. attribute:: per_call_cost
      :type: Cost

      Cost for each subplan evaluation


.. class:: SubscriptingRef(reftypmod=None, refupperindexpr=None, reflowerindexpr=None, refexpr=None, refassgnexpr=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L436>`__ parser node.

   .. attribute:: reftypmod
      :type: int32

      Typmod of the result

   .. attribute:: refupperindexpr
      :type: tuple

      Expressions that evaluate to upper
      container indexes

   .. attribute:: reflowerindexpr
      :type: tuple

      Expressions that evaluate to lower
      container indexes, or NIL for single
      container element

   .. attribute:: refexpr
      :type: Expr*

      The expression that evaluates to a
      container value

   .. attribute:: refassgnexpr
      :type: Expr*

      Expression for the source value, or NULL if
      fetch


.. class:: TableFunc(ns_uris=None, ns_names=None, docexpr=None, rowexpr=None, colnames=None, coltypes=None, coltypmods=None, colcollations=None, colexprs=None, coldefexprs=None, notnulls=None, ordinalitycol=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L82>`__ parser node.

   .. attribute:: ns_uris
      :type: tuple

      List of namespace URI expressions

   .. attribute:: ns_names
      :type: tuple

      List of namespace names or NULL

   .. attribute:: docexpr
      :type: Node

      Input document expression

   .. attribute:: rowexpr
      :type: Node

      Row filter expression

   .. attribute:: colnames
      :type: tuple

      Column names (list of String)

   .. attribute:: coltypes
      :type: tuple

      OID list of column type OIDs

   .. attribute:: coltypmods
      :type: tuple

      Integer list of column typmods

   .. attribute:: colcollations
      :type: tuple

      OID list of column collation OIDs

   .. attribute:: colexprs
      :type: tuple

      List of column filter expressions

   .. attribute:: coldefexprs
      :type: tuple

      List of column default expressions

   .. attribute:: notnulls
      :type: Bitmapset*

      Nullability flag for each output column

   .. attribute:: ordinalitycol
      :type: int

      Counts from 0; -1 if none specified

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: TableLikeClause(relation=None, options=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L682>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

   .. attribute:: options
      :type: bits32

      OR of TableLikeOption flags


.. class:: TableSampleClause(args=None, repeatable=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1190>`__ parser node.

   .. attribute:: args
      :type: tuple

      Tablesample argument expression(s)

   .. attribute:: repeatable
      :type: Expr*

      REPEATABLE expression, or NULL if none


.. class:: TargetEntry(expr=None, resno=None, resname=None, ressortgroupref=None, resorigcol=None, resjunk=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1441>`__ parser node.

   .. attribute:: expr
      :type: Expr*

      Expression to evaluate

   .. attribute:: resno
      :type: AttrNumber

      Attribute number (see notes above)

   .. attribute:: resname
      :type: str

      Name of the column (could be NULL)

   .. attribute:: ressortgroupref
      :type: Index

      Nonzero if referenced by a sort/group
      clause

   .. attribute:: resorigcol
      :type: AttrNumber

      Column's number in source table

   .. attribute:: resjunk
      :type: bool

      Set to true to eliminate the attribute from
      final target list


.. class:: TransactionStmt(kind=None, options=None, savepoint_name=None, gid=None, chain=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3182>`__ parser node.

   .. attribute:: kind
      :type: TransactionStmtKind

   .. attribute:: options
      :type: tuple

      For BEGIN/START commands

   .. attribute:: savepoint_name
      :type: str

      For savepoint commands

   .. attribute:: gid
      :type: str

      For two-phase-commit related commands

   .. attribute:: chain
      :type: bool

      AND CHAIN option


.. class:: TriggerTransition(name=None, isNew=None, isTable=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1533>`__ parser node.

   .. attribute:: name
      :type: str

   .. attribute:: isNew
      :type: bool

   .. attribute:: isTable
      :type: bool


.. class:: TruncateStmt(relations=None, restart_seqs=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2765>`__ parser node.

   .. attribute:: relations
      :type: tuple

      Relations (RangeVars) to be truncated

   .. attribute:: restart_seqs
      :type: bool

      Restart owned sequences?

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE behavior


.. class:: TypeCast(arg=None, typeName=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L305>`__ parser node.

   .. attribute:: arg
      :type: Node

      The expression being casted

   .. attribute:: typeName
      :type: TypeName*

      The target type

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: TypeName(names=None, setof=None, pct_type=None, typmods=None, typemod=None, arrayBounds=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L218>`__ parser node.

   .. attribute:: names
      :type: tuple

      Qualified name (list of Value strings)

   .. attribute:: setof
      :type: bool

      Is a set?

   .. attribute:: pct_type
      :type: bool

      %TYPE specified?

   .. attribute:: typmods
      :type: tuple

      Type modifier expression(s)

   .. attribute:: typemod
      :type: int32

      Prespecified type modifier

   .. attribute:: arrayBounds
      :type: tuple

      Array bounds

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: UnlistenStmt(conditionname=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3158>`__ parser node.

   .. attribute:: conditionname
      :type: str

      Name to unlisten on, or NULL for all


.. class:: UpdateStmt(relation=None, targetList=None, whereClause=None, fromClause=None, returningList=None, withClause=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1607>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      Relation to update

   .. attribute:: targetList
      :type: tuple

      The target list (of ResTarget)

   .. attribute:: whereClause
      :type: Node

      Qualifications

   .. attribute:: fromClause
      :type: tuple

      Optional from clause for more tables

   .. attribute:: returningList
      :type: tuple

      List of expressions to return

   .. attribute:: withClause
      :type: WithClause*

      WITH clause


.. class:: VacuumRelation(relation=None, va_cols=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3357>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      Table name to process, or NULL

   .. attribute:: va_cols
      :type: tuple

      List of column names, or NIL for all


.. class:: VacuumStmt(options=None, rels=None, is_vacuumcmd=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3342>`__ parser node.

   .. attribute:: options
      :type: tuple

      List of DefElem nodes

   .. attribute:: rels
      :type: tuple

      List of VacuumRelation, or NIL for all

   .. attribute:: is_vacuumcmd
      :type: bool

      True for VACUUM, false for ANALYZE


.. class:: Var(varno=None, varattno=None, vartypmod=None, varlevelsup=None, varnosyn=None, varattnosyn=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L186>`__ parser node.

   .. attribute:: varno
      :type: Index

      Index of this var's relation in the range
      table, or INNER_VAR/OUTER_VAR/INDEX_VAR

   .. attribute:: varattno
      :type: AttrNumber

      Attribute number of this var, or zero for
      all attrs ("whole-row Var")

   .. attribute:: vartypmod
      :type: int32

      Pg_attribute typmod value

   .. attribute:: varlevelsup
      :type: Index

      For subquery variables referencing outer
      relations; 0 in a normal var, >0 means N
      levels up

   .. attribute:: varnosyn
      :type: Index

      Syntactic relation index (0 if unknown)

   .. attribute:: varattnosyn
      :type: AttrNumber

      Syntactic attribute number

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: VariableSetStmt(kind=None, name=None, args=None, is_local=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2138>`__ parser node.

   .. attribute:: kind
      :type: VariableSetKind

   .. attribute:: name
      :type: str

      Variable to be set

   .. attribute:: args
      :type: tuple

      List of A_Const nodes

   .. attribute:: is_local
      :type: bool

      SET LOCAL?


.. class:: VariableShowStmt(name=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L2151>`__ parser node.

   .. attribute:: name
      :type: str


.. class:: ViewStmt(view=None, aliases=None, query=None, replace=None, options=None, withCheckOption=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L3251>`__ parser node.

   .. attribute:: view
      :type: RangeVar*

      The view to be created

   .. attribute:: aliases
      :type: tuple

      Target column names

   .. attribute:: query
      :type: Node

      The SELECT query (as a raw parse tree)

   .. attribute:: replace
      :type: bool

      Replace an existing view?

   .. attribute:: options
      :type: tuple

      Options from WITH clause

   .. attribute:: withCheckOption
      :type: ViewCheckOption

      WITH CHECK OPTION


.. class:: WindowClause(name=None, refname=None, partitionClause=None, orderClause=None, frameOptions=None, startOffset=None, endOffset=None, inRangeAsc=None, inRangeNullsFirst=None, winref=None, copiedOrder=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1374>`__ parser node.

   .. attribute:: name
      :type: str

      Window name (NULL in an OVER clause)

   .. attribute:: refname
      :type: str

      Referenced window name, if any

   .. attribute:: partitionClause
      :type: tuple

      PARTITION BY list

   .. attribute:: orderClause
      :type: tuple

      ORDER BY list

   .. attribute:: frameOptions
      :type: int

      Frame_clause options, see WindowDef

   .. attribute:: startOffset
      :type: Node

      Expression for starting bound, if any

   .. attribute:: endOffset
      :type: Node

      Expression for ending bound, if any

   .. attribute:: inRangeAsc
      :type: bool

      Use ASC sort order for in_range tests?

   .. attribute:: inRangeNullsFirst
      :type: bool

      Nulls sort first for in_range tests?

   .. attribute:: winref
      :type: Index

      ID referenced by window functions

   .. attribute:: copiedOrder
      :type: bool

      Did we copy orderClause from refname?


.. class:: WindowDef(name=None, refname=None, partitionClause=None, orderClause=None, frameOptions=None, startOffset=None, endOffset=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L496>`__ parser node.

   .. attribute:: name
      :type: str

      Window's own name

   .. attribute:: refname
      :type: str

      Referenced window name, if any

   .. attribute:: partitionClause
      :type: tuple

      PARTITION BY expression list

   .. attribute:: orderClause
      :type: tuple

      ORDER BY (list of SortBy)

   .. attribute:: frameOptions
      :type: int

      Frame_clause options, see below

   .. attribute:: startOffset
      :type: Node

      Expression for starting bound, if any

   .. attribute:: endOffset
      :type: Node

      Expression for ending bound, if any

   .. attribute:: location
      :type: int

      Parse location, or -1 if none/unknown


.. class:: WindowFunc(args=None, aggfilter=None, winref=None, winstar=None, winagg=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L383>`__ parser node.

   .. attribute:: args
      :type: tuple

      Arguments to the window function

   .. attribute:: aggfilter
      :type: Expr*

      FILTER expression, if any

   .. attribute:: winref
      :type: Index

      Index of associated WindowClause

   .. attribute:: winstar
      :type: bool

      True if argument list was really '*'

   .. attribute:: winagg
      :type: bool

      Is function a simple aggregate?

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: WithCheckOption(kind=None, relname=None, polname=None, qual=None, cascaded=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1212>`__ parser node.

   .. attribute:: kind
      :type: WCOKind

      Kind of WCO

   .. attribute:: relname
      :type: str

      Name of relation that specified the WCO

   .. attribute:: polname
      :type: str

      Name of RLS policy being checked

   .. attribute:: qual
      :type: Node

      Constraint qual to check

   .. attribute:: cascaded
      :type: bool

      True for a cascaded WCO on a view


.. class:: WithClause(ctes=None, recursive=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L1421>`__ parser node.

   .. attribute:: ctes
      :type: tuple

      List of CommonTableExprs

   .. attribute:: recursive
      :type: bool

      True = WITH RECURSIVE

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: XmlExpr(op=None, name=None, named_args=None, arg_names=None, args=None, xmloption=None, typmod=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/primnodes.h#L1214>`__ parser node.

   .. attribute:: op
      :type: XmlExprOp

      Xml function ID

   .. attribute:: name
      :type: str

      Name in xml(NAME foo ...) syntaxes

   .. attribute:: named_args
      :type: tuple

      Non-XML expressions for xml_attributes

   .. attribute:: arg_names
      :type: tuple

      Parallel list of Value strings

   .. attribute:: args
      :type: tuple

      List of expressions

   .. attribute:: xmloption
      :type: XmlOptionType

      DOCUMENT or CONTENT

   .. attribute:: typmod
      :type: int32

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown


.. class:: XmlSerialize(xmloption=None, expr=None, typeName=None, location=None)

   Wrapper for the `homonymous <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/parsenodes.h#L772>`__ parser node.

   .. attribute:: xmloption
      :type: XmlOptionType

      DOCUMENT or CONTENT

   .. attribute:: expr
      :type: Node

   .. attribute:: typeName
      :type: TypeName*

   .. attribute:: location
      :type: int

      Token location, or -1 if unknown

