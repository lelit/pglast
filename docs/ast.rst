.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2021 Lele Gaifax
..

.. _pglast.ast:

===================================================================
 :mod:`pglast.ast` --- Python classes representing PG parser nodes
===================================================================

The module implements a set of *data* classes, one for each ``C`` structure defined in the
PostgreSQL headers ``include/nodes/primnodes.h`` and ``include/nodes/parsenodes.h``.

.. module:: pglast.parser.ast

.. autoclass:: Node
   :special-members: __repr__, __eq__, __call__, __setattr__

.. autoclass:: Value
.. autoclass:: BitString
.. autoclass:: Float
.. autoclass:: Integer
.. autoclass:: Null
.. autoclass:: String



.. class:: A_ArrayExpr(elements=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L413>`__ parser node.

   .. attribute:: elements
      :type: tuple

      array element expressions

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: A_Const(val=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L286>`__ parser node.

   .. attribute:: val
      :type: Value

      value (includes type info, see value.h)

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: A_Expr(kind=None, name=None, lexpr=None, rexpr=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L273>`__ parser node.

   .. attribute:: kind
      :type: A_Expr_Kind

      see above

   .. attribute:: name
      :type: tuple

      possibly-qualified name of operator

   .. attribute:: lexpr
      :type: Node

      left argument, or NULL if none

   .. attribute:: rexpr
      :type: Node

      right argument, or NULL if none

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: A_Indices(is_slice=None, lidx=None, uidx=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L380>`__ parser node.

   .. attribute:: is_slice
      :type: bool

      true if slice (i.e., colon present)

   .. attribute:: lidx
      :type: Node

      slice lower bound, if any

   .. attribute:: uidx
      :type: Node

      subscript, or slice upper bound if any


.. class:: A_Indirection(arg=None, indirection=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L403>`__ parser node.

   .. attribute:: arg
      :type: Node

      the thing being selected from

   .. attribute:: indirection
      :type: tuple

      subscripts and/or field names and/or *


.. class:: A_Star()

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L369>`__ parser node.


.. class:: AccessPriv(priv_name=None, cols=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1967>`__ parser node.

   .. attribute:: priv_name
      :type: str

      string name of privilege

   .. attribute:: cols
      :type: tuple

      list of Value strings


.. class:: Aggref(aggargtypes=None, aggdirectargs=None, args=None, aggorder=None, aggdistinct=None, aggfilter=None, aggstar=None, aggvariadic=None, aggkind=None, agglevelsup=None, aggsplit=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L309>`__ parser node.

   .. attribute:: aggargtypes
      :type: tuple

      type Oids of direct and aggregated args

   .. attribute:: aggdirectargs
      :type: tuple

      direct arguments, if an ordered-set agg

   .. attribute:: args
      :type: tuple

      aggregated arguments and sort expressions

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

      true if argument list was really '*'

   .. attribute:: aggvariadic
      :type: bool

      true if variadic arguments have been
      * combined into an array last argument

   .. attribute:: aggkind
      :type: str

      aggregate kind (see pg_aggregate.h)

   .. attribute:: agglevelsup
      :type: Index

      > 0 if agg belongs to outer query

   .. attribute:: aggsplit
      :type: AggSplit

      expected agg-splitting mode of parent Agg

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: Alias(aliasname=None, colnames=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L39>`__ parser node.

   .. attribute:: aliasname
      :type: str

      aliased rel name (never qualified)

   .. attribute:: colnames
      :type: tuple

      optional list of column aliases


.. class:: AlterCollationStmt(collname=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1886>`__ parser node.

   .. attribute:: collname
      :type: tuple

      None


.. class:: AlterDatabaseSetStmt(dbname=None, setstmt=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3174>`__ parser node.

   .. attribute:: dbname
      :type: str

      database name

   .. attribute:: setstmt
      :type: VariableSetStmt*

      SET or RESET subcommand


.. class:: AlterDatabaseStmt(dbname=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3167>`__ parser node.

   .. attribute:: dbname
      :type: str

      name of database to alter

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterDefaultPrivilegesStmt(options=None, action=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1998>`__ parser node.

   .. attribute:: options
      :type: tuple

      list of DefElem

   .. attribute:: action
      :type: GrantStmt*

      GRANT/REVOKE action (with objects=NIL)


.. class:: AlterDomainStmt(subtype=None, typeName=None, name=None, def_=None, behavior=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1900>`__ parser node.

   .. attribute:: subtype
      :type: str

      * T = alter column default
      * N = alter column drop not null
      * O = alter column set not null
      * C = add constraint
      * X = drop constraint

   .. attribute:: typeName
      :type: tuple

      domain to work on

   .. attribute:: name
      :type: str

      column or constraint name to act on

   .. attribute:: def_
      :type: Node

      definition of default or constraint

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE for DROP cases

   .. attribute:: missing_ok
      :type: bool

      skip error if missing?


.. class:: AlterEnumStmt(typeName=None, oldVal=None, newVal=None, newValNeighbor=None, newValIsAfter=None, skipIfNewValExists=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3109>`__ parser node.

   .. attribute:: typeName
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: oldVal
      :type: str

      old enum value's name, if renaming

   .. attribute:: newVal
      :type: str

      new enum value's name

   .. attribute:: newValNeighbor
      :type: str

      neighboring enum value, if specified

   .. attribute:: newValIsAfter
      :type: bool

      place new enum value after neighbor?

   .. attribute:: skipIfNewValExists
      :type: bool

      no error if new already exists?


.. class:: AlterEventTrigStmt(trigname=None, tgenabled=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2473>`__ parser node.

   .. attribute:: trigname
      :type: str

      TRIGGER's name

   .. attribute:: tgenabled
      :type: str

      trigger's firing configuration WRT
      * session_replication_role


.. class:: AlterExtensionContentsStmt(extname=None, action=None, objtype=None, object=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2267>`__ parser node.

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

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2260>`__ parser node.

   .. attribute:: extname
      :type: str

      None

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterFdwStmt(fdwname=None, func_options=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2289>`__ parser node.

   .. attribute:: fdwname
      :type: str

      foreign-data wrapper name

   .. attribute:: func_options
      :type: tuple

      HANDLER/VALIDATOR options

   .. attribute:: options
      :type: tuple

      generic options to FDW


.. class:: AlterForeignServerStmt(servername=None, version=None, options=None, has_version=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2313>`__ parser node.

   .. attribute:: servername
      :type: str

      server name

   .. attribute:: version
      :type: str

      optional server version

   .. attribute:: options
      :type: tuple

      generic options to server

   .. attribute:: has_version
      :type: bool

      version specified


.. class:: AlterFunctionStmt(objtype=None, func=None, actions=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2870>`__ parser node.

   .. attribute:: objtype
      :type: ObjectType

      None

   .. attribute:: func
      :type: ObjectWithArgs*

      name and args of function

   .. attribute:: actions
      :type: tuple

      list of DefElem


.. class:: AlterObjectDependsStmt(objectType=None, relation=None, object=None, extname=None, remove=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2938>`__ parser node.

   .. attribute:: objectType
      :type: ObjectType

      OBJECT_FUNCTION, OBJECT_TRIGGER, etc

   .. attribute:: relation
      :type: RangeVar*

      in case a table is involved

   .. attribute:: object
      :type: Node

      name of the object

   .. attribute:: extname
      :type: Value*

      extension name

   .. attribute:: remove
      :type: bool

      set true to remove dep rather than add


.. class:: AlterObjectSchemaStmt(objectType=None, relation=None, object=None, newschema=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2952>`__ parser node.

   .. attribute:: objectType
      :type: ObjectType

      OBJECT_TABLE, OBJECT_TYPE, etc

   .. attribute:: relation
      :type: RangeVar*

      in case it's a table

   .. attribute:: object
      :type: Node

      in case it's some other object

   .. attribute:: newschema
      :type: str

      the new schema

   .. attribute:: missing_ok
      :type: bool

      skip error if missing?


.. class:: AlterOpFamilyStmt(opfamilyname=None, amname=None, isDrop=None, items=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2643>`__ parser node.

   .. attribute:: opfamilyname
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: amname
      :type: str

      name of index AM opfamily is for

   .. attribute:: isDrop
      :type: bool

      ADD or DROP the items?

   .. attribute:: items
      :type: tuple

      List of CreateOpClassItem nodes


.. class:: AlterOperatorStmt(opername=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2979>`__ parser node.

   .. attribute:: opername
      :type: ObjectWithArgs*

      operator name and argument types

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterOwnerStmt(objectType=None, relation=None, object=None, newowner=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2966>`__ parser node.

   .. attribute:: objectType
      :type: ObjectType

      OBJECT_TABLE, OBJECT_TYPE, etc

   .. attribute:: relation
      :type: RangeVar*

      in case it's a table

   .. attribute:: object
      :type: Node

      in case it's some other object

   .. attribute:: newowner
      :type: RoleSpec*

      the new owner


.. class:: AlterPolicyStmt(policy_name=None, table=None, roles=None, qual=None, with_check=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2407>`__ parser node.

   .. attribute:: policy_name
      :type: str

      Policy's name

   .. attribute:: table
      :type: RangeVar*

      the table name the policy applies to

   .. attribute:: roles
      :type: tuple

      the roles associated with the policy

   .. attribute:: qual
      :type: Node

      the policy's condition

   .. attribute:: with_check
      :type: Node

      the policy's WITH CHECK condition.


.. class:: AlterPublicationStmt(pubname=None, options=None, tables=None, for_all_tables=None, tableAction=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3529>`__ parser node.

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

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2528>`__ parser node.

   .. attribute:: role
      :type: RoleSpec*

      role

   .. attribute:: database
      :type: str

      database name, or NULL

   .. attribute:: setstmt
      :type: VariableSetStmt*

      SET or RESET subcommand


.. class:: AlterRoleStmt(role=None, options=None, action=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2520>`__ parser node.

   .. attribute:: role
      :type: RoleSpec*

      role

   .. attribute:: options
      :type: tuple

      List of DefElem nodes

   .. attribute:: action
      :type: int

      +1 = add members, -1 = drop members


.. class:: AlterSeqStmt(sequence=None, options=None, for_identity=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2558>`__ parser node.

   .. attribute:: sequence
      :type: RangeVar*

      the sequence to alter

   .. attribute:: options
      :type: tuple

      None

   .. attribute:: for_identity
      :type: bool

      None

   .. attribute:: missing_ok
      :type: bool

      skip error if a role is missing?


.. class:: AlterStatsStmt(defnames=None, stxstattarget=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2828>`__ parser node.

   .. attribute:: defnames
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: stxstattarget
      :type: int

      statistics target

   .. attribute:: missing_ok
      :type: bool

      skip error if statistics object is missing


.. class:: AlterSubscriptionStmt(kind=None, subname=None, conninfo=None, publication=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3561>`__ parser node.

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

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3197>`__ parser node.

   .. attribute:: setstmt
      :type: VariableSetStmt*

      SET subcommand


.. class:: AlterTSConfigurationStmt(kind=None, cfgname=None, tokentype=None, dicts=None, override=None, replace=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3502>`__ parser node.

   .. attribute:: kind
      :type: AlterTSConfigType

      ALTER_TSCONFIG_ADD_MAPPING, etc

   .. attribute:: cfgname
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: tokentype
      :type: tuple

      list of Value strings

   .. attribute:: dicts
      :type: tuple

      list of list of Value strings

   .. attribute:: override
      :type: bool

      if true - remove old variant

   .. attribute:: replace
      :type: bool

      if true - replace dictionary by another

   .. attribute:: missing_ok
      :type: bool

      for DROP - skip error if missing?


.. class:: AlterTSDictionaryStmt(dictname=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3483>`__ parser node.

   .. attribute:: dictname
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterTableCmd(subtype=None, name=None, num=None, newowner=None, def_=None, behavior=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1866>`__ parser node.

   .. attribute:: subtype
      :type: AlterTableType

      Type of table alteration to apply

   .. attribute:: name
      :type: str

      column, constraint, or trigger to act on,
      * or tablespace

   .. attribute:: num
      :type: int16

      attribute number for columns referenced by
      * number

   .. attribute:: newowner
      :type: RoleSpec*

      None

   .. attribute:: def_
      :type: Node

      definition of new column, index,
      * constraint, or parent table

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE for DROP cases

   .. attribute:: missing_ok
      :type: bool

      skip error if missing?


.. class:: AlterTableMoveAllStmt(orig_tablespacename=None, objtype=None, roles=None, new_tablespacename=None, nowait=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2236>`__ parser node.

   .. attribute:: orig_tablespacename
      :type: str

      None

   .. attribute:: objtype
      :type: ObjectType

      Object type to move

   .. attribute:: roles
      :type: tuple

      List of roles to move objects of

   .. attribute:: new_tablespacename
      :type: str

      None

   .. attribute:: nowait
      :type: bool

      None


.. class:: AlterTableSpaceOptionsStmt(tablespacename=None, options=None, isReset=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2228>`__ parser node.

   .. attribute:: tablespacename
      :type: str

      None

   .. attribute:: options
      :type: tuple

      None

   .. attribute:: isReset
      :type: bool

      None


.. class:: AlterTableStmt(relation=None, cmds=None, relkind=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1779>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      table to work on

   .. attribute:: cmds
      :type: tuple

      list of subcommands

   .. attribute:: relkind
      :type: ObjectType

      type of object

   .. attribute:: missing_ok
      :type: bool

      skip error if table missing


.. class:: AlterTypeStmt(typeName=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2990>`__ parser node.

   .. attribute:: typeName
      :type: tuple

      type name (possibly qualified)

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: AlterUserMappingStmt(user=None, servername=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2348>`__ parser node.

   .. attribute:: user
      :type: RoleSpec*

      user role

   .. attribute:: servername
      :type: str

      server name

   .. attribute:: options
      :type: tuple

      generic options to server


.. class:: AlternativeSubPlan(subplans=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L744>`__ parser node.

   .. attribute:: subplans
      :type: tuple

      SubPlan(s) with equivalent results


.. class:: ArrayCoerceExpr(arg=None, elemexpr=None, resulttypmod=None, coerceformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L855>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input expression (yields an array)

   .. attribute:: elemexpr
      :type: Expr*

      expression representing per-element work

   .. attribute:: resulttypmod
      :type: int32

      output typmod (also element typmod)

   .. attribute:: coerceformat
      :type: CoercionForm

      how to display this node

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: ArrayExpr(elements=None, multidims=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L985>`__ parser node.

   .. attribute:: elements
      :type: tuple

      the array elements or sub-arrays

   .. attribute:: multidims
      :type: bool

      true if elements are sub-arrays

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: BoolExpr(boolop=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L579>`__ parser node.

   .. attribute:: boolop
      :type: BoolExprType

      None

   .. attribute:: args
      :type: tuple

      arguments to this expression

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: BooleanTest(arg=None, booltesttype=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1239>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input expression

   .. attribute:: booltesttype
      :type: BoolTestType

      test type

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CallContext(atomic=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2910>`__ parser node.

   .. attribute:: atomic
      :type: bool

      None


.. class:: CallStmt(funccall=None, funcexpr=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2903>`__ parser node.

   .. attribute:: funccall
      :type: FuncCall*

      from the parser

   .. attribute:: funcexpr
      :type: FuncExpr*

      transformed


.. class:: CaseExpr(arg=None, args=None, defresult=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L927>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      implicit equality comparison argument

   .. attribute:: args
      :type: tuple

      the arguments (list of WHEN clauses)

   .. attribute:: defresult
      :type: Expr*

      the default result (ELSE clause)

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CaseTestExpr(typeMod=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L969>`__ parser node.

   .. attribute:: typeMod
      :type: int32

      typemod for substituted value


.. class:: CaseWhen(expr=None, result=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L941>`__ parser node.

   .. attribute:: expr
      :type: Expr*

      condition expression

   .. attribute:: result
      :type: Expr*

      substitution result

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CheckPointStmt()

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3305>`__ parser node.


.. class:: ClosePortalStmt(portalname=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2735>`__ parser node.

   .. attribute:: portalname
      :type: str

      name of the portal (cursor)


.. class:: ClusterStmt(relation=None, indexname=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3213>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      relation being indexed, or NULL if all

   .. attribute:: indexname
      :type: str

      original index defined

   .. attribute:: options
      :type: int

      OR of ClusterOption flags


.. class:: CoalesceExpr(args=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1081>`__ parser node.

   .. attribute:: args
      :type: tuple

      the arguments

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CoerceToDomain(arg=None, resulttypmod=None, coercionformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1256>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input expression

   .. attribute:: resulttypmod
      :type: int32

      output typmod (currently always -1)

   .. attribute:: coercionformat
      :type: CoercionForm

      how to display this node

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CoerceToDomainValue(typeMod=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1276>`__ parser node.

   .. attribute:: typeMod
      :type: int32

      typemod for substituted value

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CoerceViaIO(arg=None, coerceformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L831>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input expression

   .. attribute:: coerceformat
      :type: CoercionForm

      how to display this node

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CollateClause(arg=None, collname=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L307>`__ parser node.

   .. attribute:: arg
      :type: Node

      input expression

   .. attribute:: collname
      :type: tuple

      possibly-qualified collation name

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CollateExpr(arg=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L897>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input expression

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: ColumnDef(colname=None, typeName=None, inhcount=None, is_local=None, is_not_null=None, is_from_type=None, storage=None, raw_default=None, cooked_default=None, identity=None, identitySequence=None, generated=None, collClause=None, constraints=None, fdwoptions=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L644>`__ parser node.

   .. attribute:: colname
      :type: str

      name of column

   .. attribute:: typeName
      :type: TypeName*

      type of column

   .. attribute:: inhcount
      :type: int

      number of times column is inherited

   .. attribute:: is_local
      :type: bool

      column has local (non-inherited) def'n

   .. attribute:: is_not_null
      :type: bool

      NOT NULL constraint specified?

   .. attribute:: is_from_type
      :type: bool

      column definition came from table type

   .. attribute:: storage
      :type: str

      attstorage setting, or 0 for default

   .. attribute:: raw_default
      :type: Node

      default value (untransformed parse tree)

   .. attribute:: cooked_default
      :type: Node

      default value (transformed expr tree)

   .. attribute:: identity
      :type: str

      attidentity setting

   .. attribute:: identitySequence
      :type: RangeVar*

      to store identity sequence name for
      * ALTER TABLE ... ADD COLUMN

   .. attribute:: generated
      :type: str

      attgenerated setting

   .. attribute:: collClause
      :type: CollateClause*

      untransformed COLLATE spec, if any

   .. attribute:: constraints
      :type: tuple

      other constraints on column

   .. attribute:: fdwoptions
      :type: tuple

      per-column FDW options

   .. attribute:: location
      :type: int

      parse location, or -1 if none/unknown


.. class:: ColumnRef(fields=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L233>`__ parser node.

   .. attribute:: fields
      :type: tuple

      field names (Value strings) or A_Star

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CommentStmt(objtype=None, object=None, comment=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2683>`__ parser node.

   .. attribute:: objtype
      :type: ObjectType

      Object's type

   .. attribute:: object
      :type: Node

      Qualified name of the object

   .. attribute:: comment
      :type: str

      Comment to insert, or NULL to remove


.. class:: CommonTableExpr(ctename=None, aliascolnames=None, ctematerialized=None, ctequery=None, location=None, cterecursive=None, cterefcount=None, ctecolnames=None, ctecoltypes=None, ctecoltypmods=None, ctecolcollations=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1452>`__ parser node.

   .. attribute:: ctename
      :type: str

      query name (never qualified)

   .. attribute:: aliascolnames
      :type: tuple

      optional list of column names

   .. attribute:: ctematerialized
      :type: CTEMaterialize

      is this an optimization fence?

   .. attribute:: ctequery
      :type: Node

      the CTE's subquery

   .. attribute:: location
      :type: int

      token location, or -1 if unknown

   .. attribute:: cterecursive
      :type: bool

      is this CTE actually recursive?

   .. attribute:: cterefcount
      :type: int

      number of RTEs referencing this CTE
      * (excluding internal self-references)

   .. attribute:: ctecolnames
      :type: tuple

      list of output column names

   .. attribute:: ctecoltypes
      :type: tuple

      OID list of output column type OIDs

   .. attribute:: ctecoltypmods
      :type: tuple

      integer list of output column typmods

   .. attribute:: ctecolcollations
      :type: tuple

      OID list of column collation OIDs


.. class:: CompositeTypeStmt(typevar=None, coldeflist=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3076>`__ parser node.

   .. attribute:: typevar
      :type: RangeVar*

      the composite type to be created

   .. attribute:: coldeflist
      :type: tuple

      list of ColumnDef nodes


.. class:: Constraint(contype=None, conname=None, deferrable=None, initdeferred=None, location=None, is_no_inherit=None, raw_expr=None, cooked_expr=None, generated_when=None, keys=None, including=None, exclusions=None, options=None, indexname=None, indexspace=None, reset_default_tblspc=None, access_method=None, where_clause=None, pktable=None, fk_attrs=None, pk_attrs=None, fk_matchtype=None, fk_upd_action=None, fk_del_action=None, old_conpfeqop=None, skip_validation=None, initially_valid=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2155>`__ parser node.

   .. attribute:: contype
      :type: ConstrType

      see above

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

      token location, or -1 if unknown

   .. attribute:: is_no_inherit
      :type: bool

      is constraint non-inheritable?

   .. attribute:: raw_expr
      :type: Node

      expr, as untransformed parse tree

   .. attribute:: cooked_expr
      :type: str

      expr, as nodeToString representation

   .. attribute:: generated_when
      :type: str

      ALWAYS or BY DEFAULT

   .. attribute:: keys
      :type: tuple

      String nodes naming referenced key
      * column(s)

   .. attribute:: including
      :type: tuple

      String nodes naming referenced nonkey
      * column(s)

   .. attribute:: exclusions
      :type: tuple

      list of (IndexElem, operator name) pairs

   .. attribute:: options
      :type: tuple

      options from WITH clause

   .. attribute:: indexname
      :type: str

      existing index to use; otherwise NULL

   .. attribute:: indexspace
      :type: str

      index tablespace; NULL for default

   .. attribute:: reset_default_tblspc
      :type: bool

      reset default_tablespace prior to
      * creating the index

   .. attribute:: access_method
      :type: str

      index access method; NULL for default

   .. attribute:: where_clause
      :type: Node

      partial index predicate

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

      pg_constraint.conpfeqop of my former self

   .. attribute:: skip_validation
      :type: bool

      skip validation of existing rows?

   .. attribute:: initially_valid
      :type: bool

      mark the new constraint as valid?


.. class:: ConstraintsSetStmt(constraints=None, deferred=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3345>`__ parser node.

   .. attribute:: constraints
      :type: tuple

      List of names as RangeVars

   .. attribute:: deferred
      :type: bool

      None


.. class:: ConvertRowtypeExpr(arg=None, convertformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L880>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input expression

   .. attribute:: convertformat
      :type: CoercionForm

      how to display this node

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: CopyStmt(relation=None, query=None, attlist=None, is_from=None, is_program=None, filename=None, options=None, whereClause=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2013>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      the relation to copy

   .. attribute:: query
      :type: Node

      the query (SELECT or DML statement with
      * RETURNING) to copy, as a raw parse tree

   .. attribute:: attlist
      :type: tuple

      List of column names (as Strings), or NIL
      * for all columns

   .. attribute:: is_from
      :type: bool

      TO or FROM

   .. attribute:: is_program
      :type: bool

      is 'filename' a program to popen?

   .. attribute:: filename
      :type: str

      filename, or NULL for STDIN/STDOUT

   .. attribute:: options
      :type: tuple

      List of DefElem nodes

   .. attribute:: whereClause
      :type: Node

      WHERE condition (or NULL)


.. class:: CreateAmStmt(amname=None, handler_name=None, amtype=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2421>`__ parser node.

   .. attribute:: amname
      :type: str

      access method name

   .. attribute:: handler_name
      :type: tuple

      handler function name

   .. attribute:: amtype
      :type: str

      type of access method


.. class:: CreateCastStmt(sourcetype=None, targettype=None, func=None, context=None, inout=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3399>`__ parser node.

   .. attribute:: sourcetype
      :type: TypeName*

      None

   .. attribute:: targettype
      :type: TypeName*

      None

   .. attribute:: func
      :type: ObjectWithArgs*

      None

   .. attribute:: context
      :type: CoercionContext

      None

   .. attribute:: inout
      :type: bool

      None


.. class:: CreateConversionStmt(conversion_name=None, for_encoding_name=None, to_encoding_name=None, func_name=None, def_=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3385>`__ parser node.

   .. attribute:: conversion_name
      :type: tuple

      Name of the conversion

   .. attribute:: for_encoding_name
      :type: str

      source encoding name

   .. attribute:: to_encoding_name
      :type: str

      destination encoding name

   .. attribute:: func_name
      :type: tuple

      qualified conversion function name

   .. attribute:: def_
      :type: bool

      is this a default conversion?


.. class:: CreateDomainStmt(domainname=None, typeName=None, collClause=None, constraints=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2587>`__ parser node.

   .. attribute:: domainname
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: typeName
      :type: TypeName*

      the base type

   .. attribute:: collClause
      :type: CollateClause*

      untransformed COLLATE spec, if any

   .. attribute:: constraints
      :type: tuple

      constraints (list of Constraint nodes)


.. class:: CreateEnumStmt(typeName=None, vals=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3087>`__ parser node.

   .. attribute:: typeName
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: vals
      :type: tuple

      enum values (list of Value strings)


.. class:: CreateEventTrigStmt(trigname=None, eventname=None, whenclause=None, funcname=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2460>`__ parser node.

   .. attribute:: trigname
      :type: str

      TRIGGER's name

   .. attribute:: eventname
      :type: str

      event's identifier

   .. attribute:: whenclause
      :type: tuple

      list of DefElems indicating filtering

   .. attribute:: funcname
      :type: tuple

      qual. name of function to call


.. class:: CreateExtensionStmt(extname=None, if_not_exists=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2251>`__ parser node.

   .. attribute:: extname
      :type: str

      None

   .. attribute:: if_not_exists
      :type: bool

      just do nothing if it already exists?

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: CreateFdwStmt(fdwname=None, func_options=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2281>`__ parser node.

   .. attribute:: fdwname
      :type: str

      foreign-data wrapper name

   .. attribute:: func_options
      :type: tuple

      HANDLER/VALIDATOR options

   .. attribute:: options
      :type: tuple

      generic options to FDW


.. class:: CreateForeignServerStmt(servername=None, servertype=None, version=None, fdwname=None, if_not_exists=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2302>`__ parser node.

   .. attribute:: servername
      :type: str

      server name

   .. attribute:: servertype
      :type: str

      optional server type

   .. attribute:: version
      :type: str

      optional server version

   .. attribute:: fdwname
      :type: str

      FDW name

   .. attribute:: if_not_exists
      :type: bool

      just do nothing if it already exists?

   .. attribute:: options
      :type: tuple

      generic options to server


.. class:: CreateForeignTableStmt(base=None, servername=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2327>`__ parser node.

   .. attribute:: base
      :type: CreateStmt

      None

   .. attribute:: servername
      :type: str

      None

   .. attribute:: options
      :type: tuple

      None


.. class:: CreateFunctionStmt(is_procedure=None, replace=None, funcname=None, parameters=None, returnType=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2840>`__ parser node.

   .. attribute:: is_procedure
      :type: bool

      it's really CREATE PROCEDURE

   .. attribute:: replace
      :type: bool

      T => replace if already exists

   .. attribute:: funcname
      :type: tuple

      qualified name of function to create

   .. attribute:: parameters
      :type: tuple

      a list of FunctionParameter

   .. attribute:: returnType
      :type: TypeName*

      the return type

   .. attribute:: options
      :type: tuple

      a list of DefElem


.. class:: CreateOpClassItem(itemtype=None, name=None, number=None, order_family=None, class_args=None, storedtype=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2615>`__ parser node.

   .. attribute:: itemtype
      :type: int

      see codes above

   .. attribute:: name
      :type: ObjectWithArgs*

      operator or function name and args

   .. attribute:: number
      :type: int

      strategy num or support proc num

   .. attribute:: order_family
      :type: tuple

      only used for ordering operators

   .. attribute:: class_args
      :type: tuple

      amproclefttype/amprocrighttype or
      * amoplefttype/amoprighttype

   .. attribute:: storedtype
      :type: TypeName*

      datatype stored in index


.. class:: CreateOpClassStmt(opclassname=None, opfamilyname=None, amname=None, datatype=None, items=None, isDefault=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2600>`__ parser node.

   .. attribute:: opclassname
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: opfamilyname
      :type: tuple

      qualified name (ditto); NIL if omitted

   .. attribute:: amname
      :type: str

      name of index AM opclass is for

   .. attribute:: datatype
      :type: TypeName*

      datatype of indexed column

   .. attribute:: items
      :type: tuple

      List of CreateOpClassItem nodes

   .. attribute:: isDefault
      :type: bool

      Should be marked as default for type?


.. class:: CreateOpFamilyStmt(opfamilyname=None, amname=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2632>`__ parser node.

   .. attribute:: opfamilyname
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: amname
      :type: str

      name of index AM opfamily is for


.. class:: CreatePLangStmt(replace=None, plname=None, plhandler=None, plinline=None, plvalidator=None, pltrusted=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2485>`__ parser node.

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

      optional inline function (qual. name)

   .. attribute:: plvalidator
      :type: tuple

      optional validator function (qual. name)

   .. attribute:: pltrusted
      :type: bool

      PL is trusted


.. class:: CreatePolicyStmt(policy_name=None, table=None, cmd_name=None, permissive=None, roles=None, qual=None, with_check=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2391>`__ parser node.

   .. attribute:: policy_name
      :type: str

      Policy's name

   .. attribute:: table
      :type: RangeVar*

      the table name the policy applies to

   .. attribute:: cmd_name
      :type: str

      the command name the policy applies to

   .. attribute:: permissive
      :type: bool

      restrictive or permissive policy

   .. attribute:: roles
      :type: tuple

      the roles associated with the policy

   .. attribute:: qual
      :type: Node

      the policy's condition

   .. attribute:: with_check
      :type: Node

      the policy's WITH CHECK condition.


.. class:: CreatePublicationStmt(pubname=None, options=None, tables=None, for_all_tables=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3520>`__ parser node.

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

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3098>`__ parser node.

   .. attribute:: typeName
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: params
      :type: tuple

      range parameters (list of DefElem)


.. class:: CreateRoleStmt(stmt_type=None, role=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2512>`__ parser node.

   .. attribute:: stmt_type
      :type: RoleStmtType

      ROLE/USER/GROUP

   .. attribute:: role
      :type: str

      role name

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: CreateSchemaStmt(schemaname=None, authrole=None, schemaElts=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1760>`__ parser node.

   .. attribute:: schemaname
      :type: str

      the name of the schema to create

   .. attribute:: authrole
      :type: RoleSpec*

      the owner of the created schema

   .. attribute:: schemaElts
      :type: tuple

      schema components (list of parsenodes)

   .. attribute:: if_not_exists
      :type: bool

      just do nothing if schema already exists?


.. class:: CreateSeqStmt(sequence=None, options=None, for_identity=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2548>`__ parser node.

   .. attribute:: sequence
      :type: RangeVar*

      the sequence to create

   .. attribute:: options
      :type: tuple

      None

   .. attribute:: for_identity
      :type: bool

      None

   .. attribute:: if_not_exists
      :type: bool

      just do nothing if it already exists?


.. class:: CreateStatsStmt(defnames=None, stat_types=None, exprs=None, relations=None, stxcomment=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2813>`__ parser node.

   .. attribute:: defnames
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: stat_types
      :type: tuple

      stat types (list of Value strings)

   .. attribute:: exprs
      :type: tuple

      expressions to build statistics on

   .. attribute:: relations
      :type: tuple

      rels to build stats on (list of RangeVar)

   .. attribute:: stxcomment
      :type: str

      comment to apply to stats, or NULL

   .. attribute:: if_not_exists
      :type: bool

      do nothing if stats name already exists


.. class:: CreateStmt(relation=None, tableElts=None, inhRelations=None, partbound=None, partspec=None, ofTypename=None, constraints=None, options=None, oncommit=None, tablespacename=None, accessMethod=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2075>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      relation to create

   .. attribute:: tableElts
      :type: tuple

      column definitions (list of ColumnDef)

   .. attribute:: inhRelations
      :type: tuple

      relations to inherit from (list of
      * inhRelation)

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

      constraints (list of Constraint nodes)

   .. attribute:: options
      :type: tuple

      options from WITH clause

   .. attribute:: oncommit
      :type: OnCommitAction

      what do we do at COMMIT?

   .. attribute:: tablespacename
      :type: str

      table space to use, or NULL

   .. attribute:: accessMethod
      :type: str

      table access method

   .. attribute:: if_not_exists
      :type: bool

      just do nothing if it already exists?


.. class:: CreateSubscriptionStmt(subname=None, conninfo=None, publication=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3543>`__ parser node.

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


.. class:: CreateTableAsStmt(query=None, into=None, relkind=None, is_select_into=None, if_not_exists=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3279>`__ parser node.

   .. attribute:: query
      :type: Node

      the query (see comments above)

   .. attribute:: into
      :type: IntoClause*

      destination table

   .. attribute:: relkind
      :type: ObjectType

      OBJECT_TABLE or OBJECT_MATVIEW

   .. attribute:: is_select_into
      :type: bool

      it was written as SELECT INTO

   .. attribute:: if_not_exists
      :type: bool

      just do nothing if it already exists?


.. class:: CreateTableSpaceStmt(tablespacename=None, owner=None, location=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2212>`__ parser node.

   .. attribute:: tablespacename
      :type: str

      None

   .. attribute:: owner
      :type: RoleSpec*

      None

   .. attribute:: location
      :type: str

      None

   .. attribute:: options
      :type: tuple

      None


.. class:: CreateTransformStmt(replace=None, type_name=None, lang=None, fromsql=None, tosql=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3413>`__ parser node.

   .. attribute:: replace
      :type: bool

      None

   .. attribute:: type_name
      :type: TypeName*

      None

   .. attribute:: lang
      :type: str

      None

   .. attribute:: fromsql
      :type: ObjectWithArgs*

      None

   .. attribute:: tosql
      :type: ObjectWithArgs*

      None


.. class:: CreateTrigStmt(trigname=None, relation=None, funcname=None, args=None, row=None, timing=None, events=None, columns=None, whenClause=None, isconstraint=None, transitionRels=None, deferrable=None, initdeferred=None, constrrel=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2433>`__ parser node.

   .. attribute:: trigname
      :type: str

      TRIGGER's name

   .. attribute:: relation
      :type: RangeVar*

      relation trigger is on

   .. attribute:: funcname
      :type: tuple

      qual. name of function to call

   .. attribute:: args
      :type: tuple

      list of (T_String) Values or NIL

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

      column names, or NIL for all columns

   .. attribute:: whenClause
      :type: Node

      qual expression, or NULL if none

   .. attribute:: isconstraint
      :type: bool

      This is a constraint trigger

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

      opposite relation, if RI trigger


.. class:: CreateUserMappingStmt(user=None, servername=None, if_not_exists=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2339>`__ parser node.

   .. attribute:: user
      :type: RoleSpec*

      user role

   .. attribute:: servername
      :type: str

      server name

   .. attribute:: if_not_exists
      :type: bool

      just do nothing if it already exists?

   .. attribute:: options
      :type: tuple

      generic options to server


.. class:: CreatedbStmt(dbname=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3156>`__ parser node.

   .. attribute:: dbname
      :type: str

      name of database to create

   .. attribute:: options
      :type: tuple

      List of DefElem nodes


.. class:: CurrentOfExpr(cvarno=None, cursor_name=None, cursor_param=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1313>`__ parser node.

   .. attribute:: cvarno
      :type: Index

      RT index of target relation

   .. attribute:: cursor_name
      :type: str

      name of referenced cursor, or NULL

   .. attribute:: cursor_param
      :type: int

      refcursor parameter number, or 0


.. class:: DeallocateStmt(name=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3453>`__ parser node.

   .. attribute:: name
      :type: str

      The name of the plan to remove


.. class:: DeclareCursorStmt(portalname=None, options=None, query=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2723>`__ parser node.

   .. attribute:: portalname
      :type: str

      name of the portal (cursor)

   .. attribute:: options
      :type: int

      bitmask of options (see above)

   .. attribute:: query
      :type: Node

      the query (see comments above)


.. class:: DefElem(defnamespace=None, defname=None, arg=None, defaction=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L729>`__ parser node.

   .. attribute:: defnamespace
      :type: str

      NULL if unqualified name

   .. attribute:: defname
      :type: str

      None

   .. attribute:: arg
      :type: Node

      a (Value \*) or a (TypeName \*)

   .. attribute:: defaction
      :type: DefElemAction

      unspecified action, or SET/ADD/DROP

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: DefineStmt(kind=None, oldstyle=None, defnames=None, args=None, definition=None, if_not_exists=None, replace=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2571>`__ parser node.

   .. attribute:: kind
      :type: ObjectType

      aggregate, operator, type

   .. attribute:: oldstyle
      :type: bool

      hack to signal old CREATE AGG syntax

   .. attribute:: defnames
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: args
      :type: tuple

      a list of TypeName (if needed)

   .. attribute:: definition
      :type: tuple

      a list of DefElem

   .. attribute:: if_not_exists
      :type: bool

      just do nothing if it already exists?

   .. attribute:: replace
      :type: bool

      replace if already exists?


.. class:: DeleteStmt(relation=None, usingClause=None, whereClause=None, returningList=None, withClause=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1546>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      relation to delete from

   .. attribute:: usingClause
      :type: tuple

      optional using clause for more tables

   .. attribute:: whereClause
      :type: Node

      qualifications

   .. attribute:: returningList
      :type: tuple

      list of expressions to return

   .. attribute:: withClause
      :type: WithClause*

      WITH clause


.. class:: DiscardStmt(target=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3323>`__ parser node.

   .. attribute:: target
      :type: DiscardMode

      None


.. class:: DoStmt(args=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2884>`__ parser node.

   .. attribute:: args
      :type: tuple

      List of DefElem nodes


.. class:: DropOwnedStmt(roles=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3463>`__ parser node.

   .. attribute:: roles
      :type: tuple

      None

   .. attribute:: behavior
      :type: DropBehavior

      None


.. class:: DropRoleStmt(roles=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2536>`__ parser node.

   .. attribute:: roles
      :type: tuple

      List of roles to remove

   .. attribute:: missing_ok
      :type: bool

      skip error if a role is missing?


.. class:: DropStmt(objects=None, removeType=None, behavior=None, missing_ok=None, concurrent=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2657>`__ parser node.

   .. attribute:: objects
      :type: tuple

      list of names

   .. attribute:: removeType
      :type: ObjectType

      object type

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE behavior

   .. attribute:: missing_ok
      :type: bool

      skip error if object is missing?

   .. attribute:: concurrent
      :type: bool

      drop index concurrently?


.. class:: DropSubscriptionStmt(subname=None, missing_ok=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3571>`__ parser node.

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

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2221>`__ parser node.

   .. attribute:: tablespacename
      :type: str

      None

   .. attribute:: missing_ok
      :type: bool

      skip error if missing?


.. class:: DropUserMappingStmt(user=None, servername=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2356>`__ parser node.

   .. attribute:: user
      :type: RoleSpec*

      user role

   .. attribute:: servername
      :type: str

      server name

   .. attribute:: missing_ok
      :type: bool

      ignore missing mappings


.. class:: DropdbStmt(dbname=None, missing_ok=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3185>`__ parser node.

   .. attribute:: dbname
      :type: str

      database to drop

   .. attribute:: missing_ok
      :type: bool

      skip error if db is missing?

   .. attribute:: options
      :type: tuple

      currently only FORCE is supported


.. class:: ExecuteStmt(name=None, params=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3441>`__ parser node.

   .. attribute:: name
      :type: str

      The name of the plan to execute

   .. attribute:: params
      :type: tuple

      Values to assign to parameters


.. class:: ExplainStmt(query=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3259>`__ parser node.

   .. attribute:: query
      :type: Node

      the query (see comments above)

   .. attribute:: options
      :type: tuple

      list of DefElem nodes


.. class:: Expr()

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L136>`__ parser node.


.. class:: FetchStmt(direction=None, howMany=None, portalname=None, ismove=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2758>`__ parser node.

   .. attribute:: direction
      :type: FetchDirection

      see above

   .. attribute:: howMany
      :type: long

      number of rows, or position argument

   .. attribute:: portalname
      :type: str

      name of portal (cursor)

   .. attribute:: ismove
      :type: bool

      true if MOVE


.. class:: FieldSelect(arg=None, fieldnum=None, resulttypmod=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L759>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input expression

   .. attribute:: fieldnum
      :type: AttrNumber

      attribute number of field to extract

   .. attribute:: resulttypmod
      :type: int32

      output typmod (usually -1)


.. class:: FieldStore(arg=None, newvals=None, fieldnums=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L788>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input tuple value

   .. attribute:: newvals
      :type: tuple

      new value(s) for field(s)

   .. attribute:: fieldnums
      :type: tuple

      integer list of field attnums


.. class:: FromExpr(fromlist=None, quals=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1507>`__ parser node.

   .. attribute:: fromlist
      :type: tuple

      List of join subtrees

   .. attribute:: quals
      :type: Node

      qualifiers on join, if any


.. class:: FuncCall(funcname=None, args=None, agg_order=None, agg_filter=None, agg_within_group=None, agg_star=None, agg_distinct=None, func_variadic=None, over=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L348>`__ parser node.

   .. attribute:: funcname
      :type: tuple

      qualified name of function

   .. attribute:: args
      :type: tuple

      the arguments (list of exprs)

   .. attribute:: agg_order
      :type: tuple

      ORDER BY (list of SortBy)

   .. attribute:: agg_filter
      :type: Node

      FILTER clause, if any

   .. attribute:: agg_within_group
      :type: bool

      ORDER BY appeared in WITHIN GROUP

   .. attribute:: agg_star
      :type: bool

      argument was really '*'

   .. attribute:: agg_distinct
      :type: bool

      arguments were labeled DISTINCT

   .. attribute:: func_variadic
      :type: bool

      last argument was labeled VARIADIC

   .. attribute:: over
      :type: WindowDef*

      OVER clause, if any

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: FuncExpr(funcretset=None, funcvariadic=None, funcformat=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L466>`__ parser node.

   .. attribute:: funcretset
      :type: bool

      true if function returns set

   .. attribute:: funcvariadic
      :type: bool

      true if variadic arguments have been
      * combined into an array last argument

   .. attribute:: funcformat
      :type: CoercionForm

      how to display this function call

   .. attribute:: args
      :type: tuple

      arguments to the function

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: FunctionParameter(name=None, argType=None, mode=None, defexpr=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2861>`__ parser node.

   .. attribute:: name
      :type: str

      parameter name, or NULL if not given

   .. attribute:: argType
      :type: TypeName*

      TypeName for parameter type

   .. attribute:: mode
      :type: FunctionParameterMode

      IN/OUT/etc

   .. attribute:: defexpr
      :type: Node

      raw default expr, or NULL if not given


.. class:: GrantRoleStmt(granted_roles=None, grantee_roles=None, is_grant=None, admin_opt=None, grantor=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1983>`__ parser node.

   .. attribute:: granted_roles
      :type: tuple

      list of roles to be granted/revoked

   .. attribute:: grantee_roles
      :type: tuple

      list of member roles to add/delete

   .. attribute:: is_grant
      :type: bool

      true = GRANT, false = REVOKE

   .. attribute:: admin_opt
      :type: bool

      with admin option

   .. attribute:: grantor
      :type: RoleSpec*

      set grantor to other than current role

   .. attribute:: behavior
      :type: DropBehavior

      drop behavior (for REVOKE)


.. class:: GrantStmt(is_grant=None, targtype=None, objtype=None, objects=None, privileges=None, grantees=None, grant_option=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1930>`__ parser node.

   .. attribute:: is_grant
      :type: bool

      true = GRANT, false = REVOKE

   .. attribute:: targtype
      :type: GrantTargetType

      type of the grant target

   .. attribute:: objtype
      :type: ObjectType

      kind of object being operated on

   .. attribute:: objects
      :type: tuple

      list of RangeVar nodes, ObjectWithArgs
      * nodes, or plain names (as Value strings)

   .. attribute:: privileges
      :type: tuple

      list of AccessPriv nodes

   .. attribute:: grantees
      :type: tuple

      list of RoleSpec nodes

   .. attribute:: grant_option
      :type: bool

      grant or revoke grant option

   .. attribute:: behavior
      :type: DropBehavior

      drop behavior (for REVOKE)


.. class:: GroupingFunc(args=None, refs=None, cols=None, agglevelsup=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L356>`__ parser node.

   .. attribute:: args
      :type: tuple

      arguments, not evaluated but kept for
      * benefit of EXPLAIN etc.

   .. attribute:: refs
      :type: tuple

      ressortgrouprefs of arguments

   .. attribute:: cols
      :type: tuple

      actual column positions set by planner

   .. attribute:: agglevelsup
      :type: Index

      same as Aggref.agglevelsup

   .. attribute:: location
      :type: int

      token location


.. class:: GroupingSet(kind=None, content=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1328>`__ parser node.

   .. attribute:: kind
      :type: GroupingSetKind

      None

   .. attribute:: content
      :type: tuple

      None

   .. attribute:: location
      :type: int

      None


.. class:: ImportForeignSchemaStmt(server_name=None, remote_schema=None, local_schema=None, list_type=None, table_list=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2376>`__ parser node.

   .. attribute:: server_name
      :type: str

      FDW server name

   .. attribute:: remote_schema
      :type: str

      remote schema name to query

   .. attribute:: local_schema
      :type: str

      local schema to create objects in

   .. attribute:: list_type
      :type: ImportForeignSchemaType

      type of table list

   .. attribute:: table_list
      :type: tuple

      List of RangeVar

   .. attribute:: options
      :type: tuple

      list of options to pass to FDW


.. class:: IndexElem(name=None, expr=None, indexcolname=None, collation=None, opclass=None, opclassopts=None, ordering=None, nulls_ordering=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L698>`__ parser node.

   .. attribute:: name
      :type: str

      name of attribute to index, or NULL

   .. attribute:: expr
      :type: Node

      expression to index, or NULL

   .. attribute:: indexcolname
      :type: str

      name for index column; NULL = default

   .. attribute:: collation
      :type: tuple

      name of collation; NIL = default

   .. attribute:: opclass
      :type: tuple

      name of desired opclass; NIL = default

   .. attribute:: opclassopts
      :type: tuple

      opclass-specific options, or NIL

   .. attribute:: ordering
      :type: SortByDir

      ASC/DESC/default

   .. attribute:: nulls_ordering
      :type: SortByNulls

      FIRST/LAST/default


.. class:: IndexStmt(idxname=None, relation=None, accessMethod=None, tableSpace=None, indexParams=None, indexIncludingParams=None, options=None, whereClause=None, excludeOpNames=None, idxcomment=None, oldCreateSubid=None, oldFirstRelfilenodeSubid=None, unique=None, primary=None, isconstraint=None, deferrable=None, initdeferred=None, transformed=None, concurrent=None, if_not_exists=None, reset_default_tblspc=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2778>`__ parser node.

   .. attribute:: idxname
      :type: str

      name of new index, or NULL for default

   .. attribute:: relation
      :type: RangeVar*

      relation to build index on

   .. attribute:: accessMethod
      :type: str

      name of access method (eg. btree)

   .. attribute:: tableSpace
      :type: str

      tablespace, or NULL for default

   .. attribute:: indexParams
      :type: tuple

      columns to index: a list of IndexElem

   .. attribute:: indexIncludingParams
      :type: tuple

      additional columns to index: a list
      * of IndexElem

   .. attribute:: options
      :type: tuple

      WITH clause options: a list of DefElem

   .. attribute:: whereClause
      :type: Node

      qualification (partial-index predicate)

   .. attribute:: excludeOpNames
      :type: tuple

      exclusion operator names, or NIL if none

   .. attribute:: idxcomment
      :type: str

      comment to apply to index, or NULL

   .. attribute:: oldCreateSubid
      :type: SubTransactionId

      rd_createSubid of oldNode

   .. attribute:: oldFirstRelfilenodeSubid
      :type: SubTransactionId

      rd_firstRelfilenodeSubid of
      * oldNode

   .. attribute:: unique
      :type: bool

      is index unique?

   .. attribute:: primary
      :type: bool

      is index a primary key?

   .. attribute:: isconstraint
      :type: bool

      is it for a pkey/unique constraint?

   .. attribute:: deferrable
      :type: bool

      is the constraint DEFERRABLE?

   .. attribute:: initdeferred
      :type: bool

      is the constraint INITIALLY DEFERRED?

   .. attribute:: transformed
      :type: bool

      true when transformIndexStmt is finished

   .. attribute:: concurrent
      :type: bool

      should this be a concurrent index build?

   .. attribute:: if_not_exists
      :type: bool

      just do nothing if index already exists?

   .. attribute:: reset_default_tblspc
      :type: bool

      reset default_tablespace prior to
      * executing


.. class:: InferClause(indexElems=None, whereClause=None, conname=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1414>`__ parser node.

   .. attribute:: indexElems
      :type: tuple

      IndexElems to infer unique index

   .. attribute:: whereClause
      :type: Node

      qualification (partial-index predicate)

   .. attribute:: conname
      :type: str

      Constraint name, or NULL if unnamed

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: InferenceElem(expr=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1342>`__ parser node.

   .. attribute:: expr
      :type: Node

      expression to infer from, or NULL


.. class:: InlineCodeBlock(source_text=None, langIsTrusted=None, atomic=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2890>`__ parser node.

   .. attribute:: source_text
      :type: str

      source text of anonymous code block

   .. attribute:: langIsTrusted
      :type: bool

      trusted property of the language

   .. attribute:: atomic
      :type: bool

      atomic execution context


.. class:: InsertStmt(relation=None, cols=None, selectStmt=None, onConflictClause=None, returningList=None, withClause=None, override=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1530>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      relation to insert into

   .. attribute:: cols
      :type: tuple

      optional: names of the target columns

   .. attribute:: selectStmt
      :type: Node

      the source SELECT/VALUES, or NULL

   .. attribute:: onConflictClause
      :type: OnConflictClause*

      ON CONFLICT clause

   .. attribute:: returningList
      :type: tuple

      list of expressions to return

   .. attribute:: withClause
      :type: WithClause*

      WITH clause

   .. attribute:: override
      :type: OverridingKind

      OVERRIDING clause


.. class:: IntoClause(rel=None, colNames=None, accessMethod=None, options=None, onCommit=None, tableSpaceName=None, viewQuery=None, skipData=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L108>`__ parser node.

   .. attribute:: rel
      :type: RangeVar*

      target relation name

   .. attribute:: colNames
      :type: tuple

      column names to assign, or NIL

   .. attribute:: accessMethod
      :type: str

      table access method

   .. attribute:: options
      :type: tuple

      options from WITH clause

   .. attribute:: onCommit
      :type: OnCommitAction

      what do we do at COMMIT?

   .. attribute:: tableSpaceName
      :type: str

      table space to use, or NULL

   .. attribute:: viewQuery
      :type: Node

      materialized view's SELECT query

   .. attribute:: skipData
      :type: bool

      true for WITH NO DATA


.. class:: JoinExpr(jointype=None, isNatural=None, larg=None, rarg=None, usingClause=None, quals=None, alias=None, rtindex=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1485>`__ parser node.

   .. attribute:: jointype
      :type: JoinType

      type of join

   .. attribute:: isNatural
      :type: bool

      Natural join? Will need to shape table

   .. attribute:: larg
      :type: Node

      left subtree

   .. attribute:: rarg
      :type: Node

      right subtree

   .. attribute:: usingClause
      :type: tuple

      USING clause, if any (list of String)

   .. attribute:: quals
      :type: Node

      qualifiers on join, if any

   .. attribute:: alias
      :type: Alias*

      user-written alias clause, if any

   .. attribute:: rtindex
      :type: int

      RT index assigned for join, or 0


.. class:: ListenStmt(conditionname=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3028>`__ parser node.

   .. attribute:: conditionname
      :type: str

      condition name to listen on


.. class:: LoadStmt(filename=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3146>`__ parser node.

   .. attribute:: filename
      :type: str

      file to load


.. class:: LockStmt(relations=None, mode=None, nowait=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3333>`__ parser node.

   .. attribute:: relations
      :type: tuple

      relations to lock

   .. attribute:: mode
      :type: int

      lock mode

   .. attribute:: nowait
      :type: bool

      no wait mode


.. class:: LockingClause(lockedRels=None, strength=None, waitPolicy=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L748>`__ parser node.

   .. attribute:: lockedRels
      :type: tuple

      FOR [KEY] UPDATE/SHARE relations

   .. attribute:: strength
      :type: LockClauseStrength

      None

   .. attribute:: waitPolicy
      :type: LockWaitPolicy

      NOWAIT and SKIP LOCKED


.. class:: MinMaxExpr(op=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1099>`__ parser node.

   .. attribute:: op
      :type: MinMaxOp

      function to execute

   .. attribute:: args
      :type: tuple

      the arguments

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: MultiAssignRef(source=None, colno=None, ncolumns=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L456>`__ parser node.

   .. attribute:: source
      :type: Node

      the row-valued expression

   .. attribute:: colno
      :type: int

      column number for this target (1..n)

   .. attribute:: ncolumns
      :type: int

      number of targets in the construct


.. class:: NamedArgExpr(arg=None, name=None, argnumber=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L495>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      the argument expression

   .. attribute:: name
      :type: str

      the name

   .. attribute:: argnumber
      :type: int

      argument's number in positional notation

   .. attribute:: location
      :type: int

      argument name location, or -1 if unknown


.. class:: NotifyStmt(conditionname=None, payload=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3017>`__ parser node.

   .. attribute:: conditionname
      :type: str

      condition name to notify

   .. attribute:: payload
      :type: str

      the payload string, or NULL if none


.. class:: NullTest(arg=None, nulltesttype=None, argisrow=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1216>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input expression

   .. attribute:: nulltesttype
      :type: NullTestType

      IS NULL, IS NOT NULL

   .. attribute:: argisrow
      :type: bool

      T to perform field-by-field null checks

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: ObjectWithArgs(objname=None, objargs=None, args_unspecified=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1950>`__ parser node.

   .. attribute:: objname
      :type: tuple

      qualified name of function/operator

   .. attribute:: objargs
      :type: tuple

      list of Typename nodes

   .. attribute:: args_unspecified
      :type: bool

      argument list was omitted, so name must
      * be unique (note that objargs == NIL
      * means zero args)


.. class:: OnConflictClause(action=None, infer=None, targetList=None, whereClause=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1429>`__ parser node.

   .. attribute:: action
      :type: OnConflictAction

      DO NOTHING or UPDATE?

   .. attribute:: infer
      :type: InferClause*

      Optional index inference clause

   .. attribute:: targetList
      :type: tuple

      the target list (of ResTarget)

   .. attribute:: whereClause
      :type: Node

      qualifications

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: OnConflictExpr(action=None, arbiterElems=None, arbiterWhere=None, onConflictSet=None, onConflictWhere=None, exclRelIndex=None, exclRelTlist=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1523>`__ parser node.

   .. attribute:: action
      :type: OnConflictAction

      DO NOTHING or UPDATE?

   .. attribute:: arbiterElems
      :type: tuple

      unique index arbiter list (of
      * InferenceElem's)

   .. attribute:: arbiterWhere
      :type: Node

      unique index arbiter WHERE clause

   .. attribute:: onConflictSet
      :type: tuple

      List of ON CONFLICT SET TargetEntrys

   .. attribute:: onConflictWhere
      :type: Node

      qualifiers to restrict UPDATE to

   .. attribute:: exclRelIndex
      :type: int

      RT index of 'excluded' relation

   .. attribute:: exclRelTlist
      :type: tuple

      tlist of the EXCLUDED pseudo relation


.. class:: OpExpr(opretset=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L513>`__ parser node.

   .. attribute:: opretset
      :type: bool

      true if operator returns set

   .. attribute:: args
      :type: tuple

      arguments to the operator (1 or 2)

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: Param(paramkind=None, paramid=None, paramtypmod=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L259>`__ parser node.

   .. attribute:: paramkind
      :type: ParamKind

      kind of parameter. See above

   .. attribute:: paramid
      :type: int

      numeric ID for parameter

   .. attribute:: paramtypmod
      :type: int32

      typmod value, if known

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: ParamRef(number=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L243>`__ parser node.

   .. attribute:: number
      :type: int

      the number of the parameter

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: PartitionBoundSpec(strategy=None, is_default=None, modulus=None, remainder=None, listdatums=None, lowerdatums=None, upperdatums=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L811>`__ parser node.

   .. attribute:: strategy
      :type: str

      see PARTITION_STRATEGY codes above

   .. attribute:: is_default
      :type: bool

      is it a default partition bound?

   .. attribute:: modulus
      :type: int

      None

   .. attribute:: remainder
      :type: int

      None

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

      token location, or -1 if unknown


.. class:: PartitionCmd(name=None, bound=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L858>`__ parser node.

   .. attribute:: name
      :type: RangeVar*

      name of partition to attach/detach

   .. attribute:: bound
      :type: PartitionBoundSpec*

      FOR VALUES, if attaching


.. class:: PartitionElem(name=None, expr=None, collation=None, opclass=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L776>`__ parser node.

   .. attribute:: name
      :type: str

      name of column to partition on, or NULL

   .. attribute:: expr
      :type: Node

      expression to partition on, or NULL

   .. attribute:: collation
      :type: tuple

      name of collation; NIL = default

   .. attribute:: opclass
      :type: tuple

      name of desired opclass; NIL = default

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: PartitionRangeDatum(kind=None, value=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L844>`__ parser node.

   .. attribute:: kind
      :type: PartitionRangeDatumKind

      None

   .. attribute:: value
      :type: Node

      Const (or A_Const in raw tree), if kind is
      * PARTITION_RANGE_DATUM_VALUE, else NULL

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: PartitionSpec(strategy=None, partParams=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L791>`__ parser node.

   .. attribute:: strategy
      :type: str

      partitioning strategy ('hash', 'list' or
      * 'range')

   .. attribute:: partParams
      :type: tuple

      List of PartitionElems

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: PrepareStmt(name=None, argtypes=None, query=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3427>`__ parser node.

   .. attribute:: name
      :type: str

      Name of plan, arbitrary

   .. attribute:: argtypes
      :type: tuple

      Types of parameters (List of TypeName)

   .. attribute:: query
      :type: Node

      The query itself (as a raw parsetree)


.. class:: Query(commandType=None, querySource=None, queryId=None, canSetTag=None, utilityStmt=None, resultRelation=None, hasAggs=None, hasWindowFuncs=None, hasTargetSRFs=None, hasSubLinks=None, hasDistinctOn=None, hasRecursive=None, hasModifyingCTE=None, hasForUpdate=None, hasRowSecurity=None, cteList=None, rtable=None, jointree=None, targetList=None, override=None, onConflict=None, returningList=None, groupClause=None, groupingSets=None, havingQual=None, windowClause=None, distinctClause=None, sortClause=None, limitOffset=None, limitCount=None, limitOption=None, rowMarks=None, setOperations=None, constraintDeps=None, withCheckOptions=None, stmt_location=None, stmt_len=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L108>`__ parser node.

   .. attribute:: commandType
      :type: CmdType

      select|insert|update|delete|utility

   .. attribute:: querySource
      :type: QuerySource

      where did I come from?

   .. attribute:: queryId
      :type: uint64

      query identifier (can be set by plugins)

   .. attribute:: canSetTag
      :type: bool

      do I set the command result tag?

   .. attribute:: utilityStmt
      :type: Node

      non-null if commandType == CMD_UTILITY

   .. attribute:: resultRelation
      :type: int

      rtable index of target relation for
      * INSERT/UPDATE/DELETE; 0 for SELECT

   .. attribute:: hasAggs
      :type: bool

      has aggregates in tlist or havingQual

   .. attribute:: hasWindowFuncs
      :type: bool

      has window functions in tlist

   .. attribute:: hasTargetSRFs
      :type: bool

      has set-returning functions in tlist

   .. attribute:: hasSubLinks
      :type: bool

      has subquery SubLink

   .. attribute:: hasDistinctOn
      :type: bool

      distinctClause is from DISTINCT ON

   .. attribute:: hasRecursive
      :type: bool

      WITH RECURSIVE was specified

   .. attribute:: hasModifyingCTE
      :type: bool

      has INSERT/UPDATE/DELETE in WITH

   .. attribute:: hasForUpdate
      :type: bool

      FOR [KEY] UPDATE/SHARE was specified

   .. attribute:: hasRowSecurity
      :type: bool

      rewriter has applied some RLS policy

   .. attribute:: cteList
      :type: tuple

      WITH list (of CommonTableExpr's)

   .. attribute:: rtable
      :type: tuple

      list of range table entries

   .. attribute:: jointree
      :type: FromExpr*

      table join tree (FROM and WHERE clauses)

   .. attribute:: targetList
      :type: tuple

      target list (of TargetEntry)

   .. attribute:: override
      :type: OverridingKind

      OVERRIDING clause

   .. attribute:: onConflict
      :type: OnConflictExpr*

      ON CONFLICT DO [NOTHING | UPDATE]

   .. attribute:: returningList
      :type: tuple

      return-values list (of TargetEntry)

   .. attribute:: groupClause
      :type: tuple

      a list of SortGroupClause's

   .. attribute:: groupingSets
      :type: tuple

      a list of GroupingSet's if present

   .. attribute:: havingQual
      :type: Node

      qualifications applied to groups

   .. attribute:: windowClause
      :type: tuple

      a list of WindowClause's

   .. attribute:: distinctClause
      :type: tuple

      a list of SortGroupClause's

   .. attribute:: sortClause
      :type: tuple

      a list of SortGroupClause's

   .. attribute:: limitOffset
      :type: Node

      # of result tuples to skip (int8 expr)

   .. attribute:: limitCount
      :type: Node

      # of result tuples to return (int8 expr)

   .. attribute:: limitOption
      :type: LimitOption

      limit type

   .. attribute:: rowMarks
      :type: tuple

      a list of RowMarkClause's

   .. attribute:: setOperations
      :type: Node

      set-operation tree if this is top level of
      * a UNION/INTERSECT/EXCEPT query

   .. attribute:: constraintDeps
      :type: tuple

      a list of pg_constraint OIDs that the query
      * depends on to be semantically valid

   .. attribute:: withCheckOptions
      :type: tuple

      a list of WithCheckOption's (added
      * during rewrite)

   .. attribute:: stmt_location
      :type: int

      start location, or -1 if unknown

   .. attribute:: stmt_len
      :type: int

      length in bytes; 0 means "rest of string"


.. class:: RangeFunction(lateral=None, ordinality=None, is_rowsfrom=None, functions=None, alias=None, coldeflist=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L561>`__ parser node.

   .. attribute:: lateral
      :type: bool

      does it have LATERAL prefix?

   .. attribute:: ordinality
      :type: bool

      does it have WITH ORDINALITY suffix?

   .. attribute:: is_rowsfrom
      :type: bool

      is result of ROWS FROM() syntax?

   .. attribute:: functions
      :type: tuple

      per-function information, see above

   .. attribute:: alias
      :type: Alias*

      table alias & optional column aliases

   .. attribute:: coldeflist
      :type: tuple

      list of ColumnDef nodes to describe result
      * of function returning RECORD


.. class:: RangeSubselect(lateral=None, subquery=None, alias=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L539>`__ parser node.

   .. attribute:: lateral
      :type: bool

      does it have LATERAL prefix?

   .. attribute:: subquery
      :type: Node

      the untransformed sub-select clause

   .. attribute:: alias
      :type: Alias*

      table alias & optional column aliases


.. class:: RangeTableFunc(lateral=None, docexpr=None, rowexpr=None, namespaces=None, columns=None, alias=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L576>`__ parser node.

   .. attribute:: lateral
      :type: bool

      does it have LATERAL prefix?

   .. attribute:: docexpr
      :type: Node

      document expression

   .. attribute:: rowexpr
      :type: Node

      row generator expression

   .. attribute:: namespaces
      :type: tuple

      list of namespaces as ResTarget

   .. attribute:: columns
      :type: tuple

      list of RangeTableFuncCol

   .. attribute:: alias
      :type: Alias*

      table alias & optional column aliases

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: RangeTableFuncCol(colname=None, typeName=None, for_ordinality=None, is_not_null=None, colexpr=None, coldefexpr=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L594>`__ parser node.

   .. attribute:: colname
      :type: str

      name of generated column

   .. attribute:: typeName
      :type: TypeName*

      type of generated column

   .. attribute:: for_ordinality
      :type: bool

      does it have FOR ORDINALITY?

   .. attribute:: is_not_null
      :type: bool

      does it have NOT NULL?

   .. attribute:: colexpr
      :type: Node

      column filter expression

   .. attribute:: coldefexpr
      :type: Node

      column default value expression

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: RangeTableSample(relation=None, method=None, args=None, repeatable=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L616>`__ parser node.

   .. attribute:: relation
      :type: Node

      relation to be sampled

   .. attribute:: method
      :type: tuple

      sampling method name (possibly qualified)

   .. attribute:: args
      :type: tuple

      argument(s) for sampling method

   .. attribute:: repeatable
      :type: Node

      REPEATABLE expression, or NULL if none

   .. attribute:: location
      :type: int

      method name location, or -1 if unknown


.. class:: RangeTblEntry(rtekind=None, relkind=None, rellockmode=None, tablesample=None, subquery=None, security_barrier=None, jointype=None, joinmergedcols=None, joinaliasvars=None, joinleftcols=None, joinrightcols=None, functions=None, funcordinality=None, tablefunc=None, values_lists=None, ctename=None, ctelevelsup=None, self_reference=None, coltypes=None, coltypmods=None, colcollations=None, enrname=None, enrtuples=None, alias=None, eref=None, lateral=None, inh=None, inFromCl=None, requiredPerms=None, selectedCols=None, insertedCols=None, updatedCols=None, extraUpdatedCols=None, securityQuals=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L977>`__ parser node.

   .. attribute:: rtekind
      :type: RTEKind

      see above

   .. attribute:: relkind
      :type: str

      relation kind (see pg_class.relkind)

   .. attribute:: rellockmode
      :type: int

      lock level that query requires on the rel

   .. attribute:: tablesample
      :type: TableSampleClause*

      sampling info, or NULL

   .. attribute:: subquery
      :type: Query*

      the sub-query

   .. attribute:: security_barrier
      :type: bool

      is from security_barrier view?

   .. attribute:: jointype
      :type: JoinType

      type of join

   .. attribute:: joinmergedcols
      :type: int

      number of merged (JOIN USING) columns

   .. attribute:: joinaliasvars
      :type: tuple

      list of alias-var expansions

   .. attribute:: joinleftcols
      :type: tuple

      left-side input column numbers

   .. attribute:: joinrightcols
      :type: tuple

      right-side input column numbers

   .. attribute:: functions
      :type: tuple

      list of RangeTblFunction nodes

   .. attribute:: funcordinality
      :type: bool

      is this called WITH ORDINALITY?

   .. attribute:: tablefunc
      :type: TableFunc*

      None

   .. attribute:: values_lists
      :type: tuple

      list of expression lists

   .. attribute:: ctename
      :type: str

      name of the WITH list item

   .. attribute:: ctelevelsup
      :type: Index

      number of query levels up

   .. attribute:: self_reference
      :type: bool

      is this a recursive self-reference?

   .. attribute:: coltypes
      :type: tuple

      OID list of column type OIDs

   .. attribute:: coltypmods
      :type: tuple

      integer list of column typmods

   .. attribute:: colcollations
      :type: tuple

      OID list of column collation OIDs

   .. attribute:: enrname
      :type: str

      name of ephemeral named relation

   .. attribute:: enrtuples
      :type: double

      estimated or actual from caller

   .. attribute:: alias
      :type: Alias*

      user-written alias clause, if any

   .. attribute:: eref
      :type: Alias*

      expanded reference names

   .. attribute:: lateral
      :type: bool

      subquery, function, or values is LATERAL?

   .. attribute:: inh
      :type: bool

      inheritance requested?

   .. attribute:: inFromCl
      :type: bool

      present in FROM clause?

   .. attribute:: requiredPerms
      :type: AclMode

      bitmask of required access permissions

   .. attribute:: selectedCols
      :type: Bitmapset*

      columns needing SELECT permission

   .. attribute:: insertedCols
      :type: Bitmapset*

      columns needing INSERT permission

   .. attribute:: updatedCols
      :type: Bitmapset*

      columns needing UPDATE permission

   .. attribute:: extraUpdatedCols
      :type: Bitmapset*

      generated columns being updated

   .. attribute:: securityQuals
      :type: tuple

      security barrier quals to apply, if any


.. class:: RangeTblFunction(funcexpr=None, funccolcount=None, funccolnames=None, funccoltypes=None, funccoltypmods=None, funccolcollations=None, funcparams=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1149>`__ parser node.

   .. attribute:: funcexpr
      :type: Node

      expression tree for func call

   .. attribute:: funccolcount
      :type: int

      number of columns it contributes to RTE

   .. attribute:: funccolnames
      :type: tuple

      column names (list of String)

   .. attribute:: funccoltypes
      :type: tuple

      OID list of column type OIDs

   .. attribute:: funccoltypmods
      :type: tuple

      integer list of column typmods

   .. attribute:: funccolcollations
      :type: tuple

      OID list of column collation OIDs

   .. attribute:: funcparams
      :type: Bitmapset*

      PARAM_EXEC Param IDs affecting this func


.. class:: RangeTblRef(rtindex=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1456>`__ parser node.

   .. attribute:: rtindex
      :type: int

      None


.. class:: RangeVar(catalogname=None, schemaname=None, relname=None, inh=None, relpersistence=None, alias=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L63>`__ parser node.

   .. attribute:: catalogname
      :type: str

      the catalog (database) name, or NULL

   .. attribute:: schemaname
      :type: str

      the schema name, or NULL

   .. attribute:: relname
      :type: str

      the relation/sequence name

   .. attribute:: inh
      :type: bool

      expand rel by inheritance? recursively act
      * on children?

   .. attribute:: relpersistence
      :type: str

      see RELPERSISTENCE_* in pg_class.h

   .. attribute:: alias
      :type: Alias*

      table alias & optional column aliases

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: RawStmt(stmt=None, stmt_location=None, stmt_len=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1510>`__ parser node.

   .. attribute:: stmt
      :type: Node

      raw parse tree

   .. attribute:: stmt_location
      :type: int

      start location, or -1 if unknown

   .. attribute:: stmt_len
      :type: int

      length in bytes; 0 means "rest of string"


.. class:: ReassignOwnedStmt(roles=None, newrole=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3473>`__ parser node.

   .. attribute:: roles
      :type: tuple

      None

   .. attribute:: newrole
      :type: RoleSpec*

      None


.. class:: RefreshMatViewStmt(concurrent=None, skipData=None, relation=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3293>`__ parser node.

   .. attribute:: concurrent
      :type: bool

      allow concurrent access?

   .. attribute:: skipData
      :type: bool

      true for WITH NO DATA

   .. attribute:: relation
      :type: RangeVar*

      relation to insert into


.. class:: ReindexStmt(kind=None, relation=None, name=None, options=None, concurrent=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3370>`__ parser node.

   .. attribute:: kind
      :type: ReindexObjectType

      REINDEX_OBJECT_INDEX, REINDEX_OBJECT_TABLE,
      * etc.

   .. attribute:: relation
      :type: RangeVar*

      Table or index to reindex

   .. attribute:: name
      :type: str

      name of database to reindex

   .. attribute:: options
      :type: int

      Reindex options flags

   .. attribute:: concurrent
      :type: bool

      reindex concurrently?


.. class:: RelabelType(arg=None, resulttypmod=None, relabelformat=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L811>`__ parser node.

   .. attribute:: arg
      :type: Expr*

      input expression

   .. attribute:: resulttypmod
      :type: int32

      output typmod (usually -1)

   .. attribute:: relabelformat
      :type: CoercionForm

      how to display this node

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: RenameStmt(renameType=None, relationType=None, relation=None, object=None, subname=None, newname=None, behavior=None, missing_ok=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2920>`__ parser node.

   .. attribute:: renameType
      :type: ObjectType

      OBJECT_TABLE, OBJECT_COLUMN, etc

   .. attribute:: relationType
      :type: ObjectType

      if column name, associated relation type

   .. attribute:: relation
      :type: RangeVar*

      in case it's a table

   .. attribute:: object
      :type: Node

      in case it's some other object

   .. attribute:: subname
      :type: str

      name of contained object (column, rule,
      * trigger, etc)

   .. attribute:: newname
      :type: str

      the new name

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE behavior

   .. attribute:: missing_ok
      :type: bool

      skip error if missing?


.. class:: ReplicaIdentityStmt(identity_type=None, name=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1859>`__ parser node.

   .. attribute:: identity_type
      :type: str

      None

   .. attribute:: name
      :type: str

      None


.. class:: ResTarget(name=None, indirection=None, val=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L438>`__ parser node.

   .. attribute:: name
      :type: str

      column name or NULL

   .. attribute:: indirection
      :type: tuple

      subscripts, field names, and '*', or NIL

   .. attribute:: val
      :type: Node

      the value expression to compute or assign

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: RoleSpec(roletype=None, rolename=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L326>`__ parser node.

   .. attribute:: roletype
      :type: RoleSpecType

      Type of this rolespec

   .. attribute:: rolename
      :type: str

      filled only for ROLESPEC_CSTRING

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: RowCompareExpr(rctype=None, opnos=None, opfamilies=None, inputcollids=None, largs=None, rargs=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1067>`__ parser node.

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

      the left-hand input arguments

   .. attribute:: rargs
      :type: tuple

      the right-hand input arguments


.. class:: RowExpr(args=None, row_format=None, colnames=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1019>`__ parser node.

   .. attribute:: args
      :type: tuple

      the fields

   .. attribute:: row_format
      :type: CoercionForm

      how to display this node

   .. attribute:: colnames
      :type: tuple

      list of String, or NIL

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: RowMarkClause(rti=None, strength=None, waitPolicy=None, pushedDown=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1384>`__ parser node.

   .. attribute:: rti
      :type: Index

      range table index of target relation

   .. attribute:: strength
      :type: LockClauseStrength

      None

   .. attribute:: waitPolicy
      :type: LockWaitPolicy

      NOWAIT and SKIP LOCKED

   .. attribute:: pushedDown
      :type: bool

      pushed down from higher query level?


.. class:: RuleStmt(relation=None, rulename=None, whereClause=None, event=None, instead=None, actions=None, replace=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3001>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      relation the rule is for

   .. attribute:: rulename
      :type: str

      name of the rule

   .. attribute:: whereClause
      :type: Node

      qualifications

   .. attribute:: event
      :type: CmdType

      SELECT, INSERT, etc

   .. attribute:: instead
      :type: bool

      is a 'do instead'?

   .. attribute:: actions
      :type: tuple

      the action statements

   .. attribute:: replace
      :type: bool

      OR REPLACE


.. class:: SQLValueFunction(op=None, typmod=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1140>`__ parser node.

   .. attribute:: op
      :type: SQLValueFunctionOp

      which function this is

   .. attribute:: typmod
      :type: int32

      None

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: ScalarArrayOpExpr(useOr=None, args=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L556>`__ parser node.

   .. attribute:: useOr
      :type: bool

      true for ANY, false for ALL

   .. attribute:: args
      :type: tuple

      the scalar and array operands

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: SecLabelStmt(objtype=None, object=None, provider=None, label=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2695>`__ parser node.

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


.. class:: SelectStmt(distinctClause=None, intoClause=None, targetList=None, fromClause=None, whereClause=None, groupClause=None, havingClause=None, windowClause=None, valuesLists=None, sortClause=None, limitOffset=None, limitCount=None, limitOption=None, lockingClause=None, withClause=None, op=None, all=None, larg=None, rarg=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1592>`__ parser node.

   .. attribute:: distinctClause
      :type: tuple

      NULL, list of DISTINCT ON exprs, or
      * lcons(NIL,NIL) for all (SELECT DISTINCT)

   .. attribute:: intoClause
      :type: IntoClause*

      target for SELECT INTO

   .. attribute:: targetList
      :type: tuple

      the target list (of ResTarget)

   .. attribute:: fromClause
      :type: tuple

      the FROM clause

   .. attribute:: whereClause
      :type: Node

      WHERE qualification

   .. attribute:: groupClause
      :type: tuple

      GROUP BY clauses

   .. attribute:: havingClause
      :type: Node

      HAVING conditional-expression

   .. attribute:: windowClause
      :type: tuple

      WINDOW window_name AS (...), ...

   .. attribute:: valuesLists
      :type: tuple

      untransformed list of expression lists

   .. attribute:: sortClause
      :type: tuple

      sort clause (a list of SortBy's)

   .. attribute:: limitOffset
      :type: Node

      # of result tuples to skip

   .. attribute:: limitCount
      :type: Node

      # of result tuples to return

   .. attribute:: limitOption
      :type: LimitOption

      limit type

   .. attribute:: lockingClause
      :type: tuple

      FOR UPDATE (list of LockingClause's)

   .. attribute:: withClause
      :type: WithClause*

      WITH clause

   .. attribute:: op
      :type: SetOperation

      type of set op

   .. attribute:: all
      :type: bool

      ALL specified?

   .. attribute:: larg
      :type: SelectStmt*

      left child

   .. attribute:: rarg
      :type: SelectStmt*

      right child


.. class:: SetOperationStmt(op=None, all=None, larg=None, rarg=None, colTypes=None, colTypmods=None, colCollations=None, groupClauses=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1660>`__ parser node.

   .. attribute:: op
      :type: SetOperation

      type of set op

   .. attribute:: all
      :type: bool

      ALL specified?

   .. attribute:: larg
      :type: Node

      left child

   .. attribute:: rarg
      :type: Node

      right child

   .. attribute:: colTypes
      :type: tuple

      OID list of output column type OIDs

   .. attribute:: colTypmods
      :type: tuple

      integer list of output column typmods

   .. attribute:: colCollations
      :type: tuple

      OID list of output column collation OIDs

   .. attribute:: groupClauses
      :type: tuple

      a list of SortGroupClause's


.. class:: SetToDefault(typeMod=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1292>`__ parser node.

   .. attribute:: typeMod
      :type: int32

      typemod for substituted value

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: SortBy(node=None, sortby_dir=None, sortby_nulls=None, useOp=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L467>`__ parser node.

   .. attribute:: node
      :type: Node

      expression to sort on

   .. attribute:: sortby_dir
      :type: SortByDir

      ASC/DESC/USING/default

   .. attribute:: sortby_nulls
      :type: SortByNulls

      NULLS FIRST/LAST

   .. attribute:: useOp
      :type: tuple

      name of op to use, if SORTBY_USING

   .. attribute:: location
      :type: int

      operator location, or -1 if none/unknown


.. class:: SortGroupClause(tleSortGroupRef=None, nulls_first=None, hashable=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1259>`__ parser node.

   .. attribute:: tleSortGroupRef
      :type: Index

      reference into targetlist

   .. attribute:: nulls_first
      :type: bool

      do NULLs come before normal values?

   .. attribute:: hashable
      :type: bool

      can eqop be implemented by hashing?


.. class:: SubLink(subLinkType=None, subLinkId=None, testexpr=None, operName=None, subselect=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L651>`__ parser node.

   .. attribute:: subLinkType
      :type: SubLinkType

      see above

   .. attribute:: subLinkId
      :type: int

      ID (1..n); 0 if not MULTIEXPR

   .. attribute:: testexpr
      :type: Node

      outer-query test for ALL/ANY/ROWCOMPARE

   .. attribute:: operName
      :type: tuple

      originally specified operator name

   .. attribute:: subselect
      :type: Node

      subselect as Query* or raw parsetree

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: SubPlan(subLinkType=None, testexpr=None, paramIds=None, plan_id=None, plan_name=None, firstColTypmod=None, useHashTable=None, unknownEqFalse=None, parallel_safe=None, setParam=None, parParam=None, args=None, startup_cost=None, per_call_cost=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L700>`__ parser node.

   .. attribute:: subLinkType
      :type: SubLinkType

      see above

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

      true to store subselect output in a hash
      * table (implies we are doing "IN")

   .. attribute:: unknownEqFalse
      :type: bool

      true if it's okay to return FALSE when the
      * spec result is UNKNOWN; this allows much
      * simpler handling of null values

   .. attribute:: parallel_safe
      :type: bool

      is the subplan parallel-safe?

   .. attribute:: setParam
      :type: tuple

      initplan subqueries have to set these
      * Params for parent plan

   .. attribute:: parParam
      :type: tuple

      indices of input Params from parent plan

   .. attribute:: args
      :type: tuple

      exprs to pass as parParam values

   .. attribute:: startup_cost
      :type: Cost

      one-time setup cost

   .. attribute:: per_call_cost
      :type: Cost

      cost for each subplan evaluation


.. class:: SubscriptingRef(reftypmod=None, refupperindexpr=None, reflowerindexpr=None, refexpr=None, refassgnexpr=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L415>`__ parser node.

   .. attribute:: reftypmod
      :type: int32

      typmod of the container (and elements too)

   .. attribute:: refupperindexpr
      :type: tuple

      expressions that evaluate to upper
      * container indexes

   .. attribute:: reflowerindexpr
      :type: tuple

      expressions that evaluate to lower
      * container indexes, or NIL for single
      * container element

   .. attribute:: refexpr
      :type: Expr*

      the expression that evaluates to a
      * container value

   .. attribute:: refassgnexpr
      :type: Expr*

      expression for the source value, or NULL if
      * fetch


.. class:: TableFunc(ns_uris=None, ns_names=None, docexpr=None, rowexpr=None, colnames=None, coltypes=None, coltypmods=None, colcollations=None, colexprs=None, coldefexprs=None, notnulls=None, ordinalitycol=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L82>`__ parser node.

   .. attribute:: ns_uris
      :type: tuple

      list of namespace URI expressions

   .. attribute:: ns_names
      :type: tuple

      list of namespace names or NULL

   .. attribute:: docexpr
      :type: Node

      input document expression

   .. attribute:: rowexpr
      :type: Node

      row filter expression

   .. attribute:: colnames
      :type: tuple

      column names (list of String)

   .. attribute:: coltypes
      :type: tuple

      OID list of column type OIDs

   .. attribute:: coltypmods
      :type: tuple

      integer list of column typmods

   .. attribute:: colcollations
      :type: tuple

      OID list of column collation OIDs

   .. attribute:: colexprs
      :type: tuple

      list of column filter expressions

   .. attribute:: coldefexprs
      :type: tuple

      list of column default expressions

   .. attribute:: notnulls
      :type: Bitmapset*

      nullability flag for each output column

   .. attribute:: ordinalitycol
      :type: int

      counts from 0; -1 if none specified

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: TableLikeClause(relation=None, options=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L670>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      None

   .. attribute:: options
      :type: bits32

      OR of TableLikeOption flags


.. class:: TableSampleClause(args=None, repeatable=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1169>`__ parser node.

   .. attribute:: args
      :type: tuple

      tablesample argument expression(s)

   .. attribute:: repeatable
      :type: Expr*

      REPEATABLE expression, or NULL if none


.. class:: TargetEntry(expr=None, resno=None, resname=None, ressortgroupref=None, resorigcol=None, resjunk=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1404>`__ parser node.

   .. attribute:: expr
      :type: Expr*

      expression to evaluate

   .. attribute:: resno
      :type: AttrNumber

      attribute number (see notes above)

   .. attribute:: resname
      :type: str

      name of the column (could be NULL)

   .. attribute:: ressortgroupref
      :type: Index

      nonzero if referenced by a sort/group
      * clause

   .. attribute:: resorigcol
      :type: AttrNumber

      column's number in source table

   .. attribute:: resjunk
      :type: bool

      set to true to eliminate the attribute from
      * final target list


.. class:: TransactionStmt(kind=None, options=None, savepoint_name=None, gid=None, chain=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3062>`__ parser node.

   .. attribute:: kind
      :type: TransactionStmtKind

      see above

   .. attribute:: options
      :type: tuple

      for BEGIN/START commands

   .. attribute:: savepoint_name
      :type: str

      for savepoint commands

   .. attribute:: gid
      :type: str

      for two-phase-commit related commands

   .. attribute:: chain
      :type: bool

      AND CHAIN option


.. class:: TriggerTransition(name=None, isNew=None, isTable=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1486>`__ parser node.

   .. attribute:: name
      :type: str

      None

   .. attribute:: isNew
      :type: bool

      None

   .. attribute:: isTable
      :type: bool

      None


.. class:: TruncateStmt(relations=None, restart_seqs=None, behavior=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2671>`__ parser node.

   .. attribute:: relations
      :type: tuple

      relations (RangeVars) to be truncated

   .. attribute:: restart_seqs
      :type: bool

      restart owned sequences?

   .. attribute:: behavior
      :type: DropBehavior

      RESTRICT or CASCADE behavior


.. class:: TypeCast(arg=None, typeName=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L296>`__ parser node.

   .. attribute:: arg
      :type: Node

      the expression being casted

   .. attribute:: typeName
      :type: TypeName*

      the target type

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: TypeName(names=None, setof=None, pct_type=None, typmods=None, typemod=None, arrayBounds=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L207>`__ parser node.

   .. attribute:: names
      :type: tuple

      qualified name (list of Value strings)

   .. attribute:: setof
      :type: bool

      is a set?

   .. attribute:: pct_type
      :type: bool

      %TYPE specified?

   .. attribute:: typmods
      :type: tuple

      type modifier expression(s)

   .. attribute:: typemod
      :type: int32

      prespecified type modifier

   .. attribute:: arrayBounds
      :type: tuple

      array bounds

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: UnlistenStmt(conditionname=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3038>`__ parser node.

   .. attribute:: conditionname
      :type: str

      name to unlisten on, or NULL for all


.. class:: UpdateStmt(relation=None, targetList=None, whereClause=None, fromClause=None, returningList=None, withClause=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1560>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      relation to update

   .. attribute:: targetList
      :type: tuple

      the target list (of ResTarget)

   .. attribute:: whereClause
      :type: Node

      qualifications

   .. attribute:: fromClause
      :type: tuple

      optional from clause for more tables

   .. attribute:: returningList
      :type: tuple

      list of expressions to return

   .. attribute:: withClause
      :type: WithClause*

      WITH clause


.. class:: VacuumRelation(relation=None, va_cols=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3243>`__ parser node.

   .. attribute:: relation
      :type: RangeVar*

      table name to process, or NULL

   .. attribute:: va_cols
      :type: tuple

      list of column names, or NIL for all


.. class:: VacuumStmt(options=None, rels=None, is_vacuumcmd=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3228>`__ parser node.

   .. attribute:: options
      :type: tuple

      list of DefElem nodes

   .. attribute:: rels
      :type: tuple

      list of VacuumRelation, or NIL for all

   .. attribute:: is_vacuumcmd
      :type: bool

      true for VACUUM, false for ANALYZE


.. class:: Var(varno=None, varattno=None, vartypmod=None, varlevelsup=None, varnosyn=None, varattnosyn=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L181>`__ parser node.

   .. attribute:: varno
      :type: Index

      index of this var's relation in the range
      * table, or INNER_VAR/OUTER_VAR/INDEX_VAR

   .. attribute:: varattno
      :type: AttrNumber

      attribute number of this var, or zero for
      * all attrs ("whole-row Var")

   .. attribute:: vartypmod
      :type: int32

      pg_attribute typmod value

   .. attribute:: varlevelsup
      :type: Index

      for subquery variables referencing outer
      * relations; 0 in a normal var, >0 means N
      * levels up

   .. attribute:: varnosyn
      :type: Index

      syntactic relation index (0 if unknown)

   .. attribute:: varattnosyn
      :type: AttrNumber

      syntactic attribute number

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: VariableSetStmt(kind=None, name=None, args=None, is_local=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2045>`__ parser node.

   .. attribute:: kind
      :type: VariableSetKind

      None

   .. attribute:: name
      :type: str

      variable to be set

   .. attribute:: args
      :type: tuple

      List of A_Const nodes

   .. attribute:: is_local
      :type: bool

      SET LOCAL?


.. class:: VariableShowStmt(name=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L2058>`__ parser node.

   .. attribute:: name
      :type: str

      None


.. class:: ViewStmt(view=None, aliases=None, query=None, replace=None, options=None, withCheckOption=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L3131>`__ parser node.

   .. attribute:: view
      :type: RangeVar*

      the view to be created

   .. attribute:: aliases
      :type: tuple

      target column names

   .. attribute:: query
      :type: Node

      the SELECT query (as a raw parse tree)

   .. attribute:: replace
      :type: bool

      replace an existing view?

   .. attribute:: options
      :type: tuple

      options from WITH clause

   .. attribute:: withCheckOption
      :type: ViewCheckOption

      WITH CHECK OPTION


.. class:: WindowClause(name=None, refname=None, partitionClause=None, orderClause=None, frameOptions=None, startOffset=None, endOffset=None, inRangeAsc=None, inRangeNullsFirst=None, winref=None, copiedOrder=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1353>`__ parser node.

   .. attribute:: name
      :type: str

      window name (NULL in an OVER clause)

   .. attribute:: refname
      :type: str

      referenced window name, if any

   .. attribute:: partitionClause
      :type: tuple

      PARTITION BY list

   .. attribute:: orderClause
      :type: tuple

      ORDER BY list

   .. attribute:: frameOptions
      :type: int

      frame_clause options, see WindowDef

   .. attribute:: startOffset
      :type: Node

      expression for starting bound, if any

   .. attribute:: endOffset
      :type: Node

      expression for ending bound, if any

   .. attribute:: inRangeAsc
      :type: bool

      use ASC sort order for in_range tests?

   .. attribute:: inRangeNullsFirst
      :type: bool

      nulls sort first for in_range tests?

   .. attribute:: winref
      :type: Index

      ID referenced by window functions

   .. attribute:: copiedOrder
      :type: bool

      did we copy orderClause from refname?


.. class:: WindowDef(name=None, refname=None, partitionClause=None, orderClause=None, frameOptions=None, startOffset=None, endOffset=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L485>`__ parser node.

   .. attribute:: name
      :type: str

      window's own name

   .. attribute:: refname
      :type: str

      referenced window name, if any

   .. attribute:: partitionClause
      :type: tuple

      PARTITION BY expression list

   .. attribute:: orderClause
      :type: tuple

      ORDER BY (list of SortBy)

   .. attribute:: frameOptions
      :type: int

      frame_clause options, see below

   .. attribute:: startOffset
      :type: Node

      expression for starting bound, if any

   .. attribute:: endOffset
      :type: Node

      expression for ending bound, if any

   .. attribute:: location
      :type: int

      parse location, or -1 if none/unknown


.. class:: WindowFunc(args=None, aggfilter=None, winref=None, winstar=None, winagg=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L370>`__ parser node.

   .. attribute:: args
      :type: tuple

      arguments to the window function

   .. attribute:: aggfilter
      :type: Expr*

      FILTER expression, if any

   .. attribute:: winref
      :type: Index

      index of associated WindowClause

   .. attribute:: winstar
      :type: bool

      true if argument list was really '*'

   .. attribute:: winagg
      :type: bool

      is function a simple aggregate?

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: WithCheckOption(kind=None, relname=None, polname=None, qual=None, cascaded=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1191>`__ parser node.

   .. attribute:: kind
      :type: WCOKind

      kind of WCO

   .. attribute:: relname
      :type: str

      name of relation that specified the WCO

   .. attribute:: polname
      :type: str

      name of RLS policy being checked

   .. attribute:: qual
      :type: Node

      constraint qual to check

   .. attribute:: cascaded
      :type: bool

      true for a cascaded WCO on a view


.. class:: WithClause(ctes=None, recursive=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L1400>`__ parser node.

   .. attribute:: ctes
      :type: tuple

      list of CommonTableExprs

   .. attribute:: recursive
      :type: bool

      true = WITH RECURSIVE

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: XmlExpr(op=None, name=None, named_args=None, arg_names=None, args=None, xmloption=None, typmod=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/primnodes.h#L1178>`__ parser node.

   .. attribute:: op
      :type: XmlExprOp

      xml function ID

   .. attribute:: name
      :type: str

      name in xml(NAME foo ...) syntaxes

   .. attribute:: named_args
      :type: tuple

      non-XML expressions for xml_attributes

   .. attribute:: arg_names
      :type: tuple

      parallel list of Value strings

   .. attribute:: args
      :type: tuple

      list of expressions

   .. attribute:: xmloption
      :type: XmlOptionType

      DOCUMENT or CONTENT

   .. attribute:: typmod
      :type: int32

      None

   .. attribute:: location
      :type: int

      token location, or -1 if unknown


.. class:: XmlSerialize(xmloption=None, expr=None, typeName=None, location=None)

   Wrapper for the `homonymous <https://github.com/lfittl/libpg_query/blob/69e163b/src/postgres/include/nodes/parsenodes.h#L759>`__ parser node.

   .. attribute:: xmloption
      :type: XmlOptionType

      DOCUMENT or CONTENT

   .. attribute:: expr
      :type: Node

      None

   .. attribute:: typeName
      :type: TypeName*

      None

   .. attribute:: location
      :type: int

      token location, or -1 if unknown

