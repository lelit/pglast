.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Usage
.. :Created:   gio 10 ago 2017 10:06:38 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2019, 2021, 2022 Lele Gaifax
..

.. _usage:

===================
 Examples of usage
===================

Here are some example of how the module can be used.

---------
AST level
---------

The lowest level is a Python wrapper around each *parse node* returned by the ``PostgreSQL``
parser. Each node is represented by a corresponding Python class in the module
:ref:`pglast.ast`.

Parse an ``SQL`` statement and get its *AST* root node
======================================================

The function :func:`~pglast.parser.parse_sql` returns a tuple containing one or more
:class:`~pglast.ast.RawStmt` instances:

.. doctest::

   >>> from pglast import parse_sql
   >>> root = parse_sql('select 1')
   >>> print(root)
   (<RawStmt stmt=<SelectStmt targetList=(<ResTarget val=<A_Const val=<Integer val=1>>>,) ...,)

The textual ``repr``\ esentation of a parse node carries all its *not* ``None`` attributes,
recursively.

You can obtain the accepted attributes of any node by iterating it:

.. doctest::

   >>> rawstmt = root[0]
   >>> print(tuple(rawstmt))
   ('stmt', 'stmt_location', 'stmt_len')

.. doctest::

   >>> from pglast import ast
   >>> stmt = rawstmt.stmt
   >>> assert isinstance(stmt, ast.SelectStmt)

Each node is also a *callable*, to serialize it into a hierarchy of elementary Python values
such as dictionaries and tuples:

.. doctest::

   >>> from pprint import pprint
   >>> pprint(stmt(depth=2, skip_none=True))
   {'@': 'SelectStmt',
    'all': False,
    'groupDistinct': False,
    'limitOption': {'#': 'LimitOption',
                    'name': 'LIMIT_OPTION_DEFAULT',
                    'value': 0},
    'op': {'#': 'SetOperation', 'name': 'SETOP_NONE', 'value': 0},
    'targetList': ({'@': 'ResTarget', 'location': 7, 'val': …},)}

As you can see, each node is serialized to a dictionary containing at least on *special* key,
``@``, with the *tag name* of the node; lists of nodes are converted to tuples, and ``Enum``
instances to a dictionary with a special ``#`` key carrying the name of data type, and two
other keys ``name`` and ``value`` respectively with the name and value of the enum value.

Nodes can be compared to each other, and are considered equal when all their attributes match,
ignoring those semantically irrelevant:

.. doctest::

   >>> other_stmt = parse_sql('select /* something here */ 1')[0].stmt
   >>> print(other_stmt(depth=2, skip_none=True))
   {'@': 'SelectStmt', 'targetList': ({'@': 'ResTarget', 'val': …, 'location': 28},), ...}
   >>> stmt == other_stmt
   True

Altering a node
===============

Any attribute of a node is alterable, and some check is done on the assigned value:

.. doctest::

   >>> print(stmt.all)
   False
   >>> stmt.all = True
   >>> print(stmt.all)
   True

.. doctest::

   >>> stmt.all = "foo"
   Traceback (most recent call last):
     ...
   ValueError: Bad value for attribute SelectStmt.all, expected (<class 'bool'>, <class 'int'>), got <class 'str'>: 'foo'

Enum attributes can be set to either a plain string, which is looked up in the related class,
or to a dictionary:

.. doctest::

   >>> stmt.limitOption = 'LIMIT_OPTION_COUNT'
   >>> pprint(stmt(depth=1, skip_none=True))
   {'@': 'SelectStmt',
    'all': True,
    'groupDistinct': False,
    'limitOption': {'#': 'LimitOption', 'name': 'LIMIT_OPTION_COUNT', 'value': 1},
    'op': {'#': 'SetOperation', 'name': 'SETOP_NONE', 'value': 0},
    'targetList': (…,)}

.. doctest::

   >>> stmt.limitOption = {'#': 'LimitOption', 'name': 'LIMIT_OPTION_WITH_TIES'}
   >>> pprint(stmt(depth=1, skip_none=True))
   {'@': 'SelectStmt',
    'all': True,
    'groupDistinct': False,
    'limitOption': {'#': 'LimitOption',
                    'name': 'LIMIT_OPTION_WITH_TIES',
                    'value': 2},
    'op': {'#': 'SetOperation', 'name': 'SETOP_NONE', 'value': 0},
    'targetList': (…,)}

Either way, assigning the wrong value raises an exception:

.. doctest::

   >>> stmt.limitOption = 'foo'
   Traceback (most recent call last):
     ...
   ValueError: Bad value for attribute SelectStmt.limitOption, (<class 'int'>, <class 'str'>, <class 'dict'>, <enum 'LimitOption'>), got 'foo'
   >>> stmt.limitOption = {'#': 'JoinType', 'name': 'JOIN_INNER'}
   Traceback (most recent call last):
     ...
   ValueError: Bad value for attribute SelectStmt.limitOption, expected a (<class 'int'>, <class 'str'>, <class 'dict'>, <enum 'LimitOption'>), got {'#': 'JoinType', 'name': 'JOIN_INNER'}


Creating a node
===============

You can easily create a new node in the usual way, possibly passing any recognized attribute as
a parameter to the constructor:

.. doctest::

   >>> print(ast.SelectStmt())
   <SelectStmt>
   >>> print(ast.SelectStmt(all=1))
   <SelectStmt all=True>
   >>> ast.SelectStmt(non_existing_attribute=None)
   Traceback (most recent call last):
     ...
   TypeError: __init__() got an unexpected keyword argument 'non_existing_attribute'
   >>> ast.SelectStmt(all="foo")
   Traceback (most recent call last):
     ...
   ValueError: Bad value for attribute SelectStmt.all, expected (<class 'bool'>, <class 'int'>), got <class 'str'>: 'foo'

Alternatively, you can pass a single dictionary as argument, with the special ``@`` key valued
with the correct node name:

   >>> print(ast.SelectStmt({'@': 'SelectStmt', 'all': True}))
   <SelectStmt all=True>
   >>> print(ast.SelectStmt({'@': 'RawStmt', 'all': True}))
   Traceback (most recent call last):
     ...
   ValueError: Bad argument, wrong "@" value, expected 'SelectStmt', got 'RawStmt'

This basically means that you can reconstruct a syntax tree from the result of calling a node:

   >>> clone = ast.SelectStmt(stmt())
   >>> clone is stmt
   False
   >>> clone == stmt
   True

Programmatically :func:`reformat <pglast.prettify>` a ``SQL`` statement
=======================================================================

The easy way
------------

The :func:`~pglast.prettify()` takes a textual ``SQL`` statement and returns its equivalent
once *reprinted* with a focus on readability.

.. doctest::

   >>> from pglast import prettify
   >>> print(prettify('delete from sometable where value is null'))
   DELETE FROM sometable
   WHERE value IS NULL

.. doctest::

   >>> print(prettify('select a,b,c from sometable where value is null'))
   SELECT a
        , b
        , c
   FROM sometable
   WHERE value IS NULL

.. doctest::

   >>> print(prettify('select a,b,c from sometable'
   ...                ' where value is null or value = 1',
   ...                comma_at_eoln=True))
   SELECT a,
          b,
          c
   FROM sometable
   WHERE value IS NULL
      OR value = 1

Under the cover
---------------

The function above is a simple wrapper to the :class:`~pglast.stream.IndentedStream` class,
that extends :class:`pglast.stream.RawStream` adding a bit a aesthetic sense.

.. doctest::

   >>> from pglast.stream import IndentedStream, RawStream
   >>> print(IndentedStream(comma_at_eoln=True)('select a,b,c from sometable'))
   SELECT a,
          b,
          c
   FROM sometable

.. doctest::

   >>> print(IndentedStream()('select foo from bar'))
   SELECT foo
   FROM bar

.. doctest::

   >>> sql = 'select a.x, b.y from a join b on a.bid = b.id'
   >>> astnode = parse_sql(sql)[0].stmt
   >>> astnode
   <SelectStmt targetList=(<ResTarget val=<ColumnRef fields=(<String val='a'>, <String val='x'>)>>...
   >>> print(RawStream()(astnode.fromClause))
   a INNER JOIN b ON a.bid = b.id

:class:`Visit <pglast.visitors.Visitor>` or modify the AST tree
===============================================================

.. doctest::

   >>> from collections import Counter
   >>> from pglast.visitors import Visitor
   >>>
   >>> class Stats(Visitor):
   ...     def __call__(self, node):
   ...         self.counters = Counter()
   ...         super().__call__(node)
   ...         return self.counters
   ...
   ...     def visit(self, ancestors, node):
   ...         self.counters.update((node.__class__.__name__,))
   ...
   >>> stats = Stats()
   >>> print(stats(parse_sql('select 1')))
   Counter({'RawStmt': 1, 'SelectStmt': 1, 'ResTarget': 1, 'A_Const': 1, 'Integer': 1})

.. doctest::

   >>> class NoisyVisitor(Visitor):
   ...     def visit(self, ancestors, node):
   ...         print(ancestors, ':', node(depth=0, skip_none=True))
   ...
   >>> visitor = NoisyVisitor()
   >>> visitor(parse_sql('select a, b from c'))
   ROOT → 0 : {'@': 'RawStmt', 'stmt': …, 'stmt_location': 0, 'stmt_len': 0}
   ROOT → 0 → stmt : {'@': 'SelectStmt', 'targetList': …, 'fromClause': …, ...
   ROOT → 0 → stmt → targetList → 0 : {'@': 'ResTarget', 'val': …, 'location': 7}
   ROOT → 0 → stmt → targetList → 1 : {'@': 'ResTarget', 'val': …, 'location': 10}
   ROOT → 0 → stmt → fromClause → 0 : {'@': 'RangeVar', 'relname': 'c', 'inh': True, ...
   ROOT → 0 → stmt → targetList → 0 → val : {'@': 'ColumnRef', 'fields': …, 'location': 7}
   ROOT → 0 → stmt → targetList → 1 → val : {'@': 'ColumnRef', 'fields': …, 'location': 10}
   ROOT → 0 → stmt → targetList → 0 → val → fields → 0 : {'@': 'String', 'val': 'a'}
   ROOT → 0 → stmt → targetList → 1 → val → fields → 0 : {'@': 'String', 'val': 'b'}
   (<RawStmt stmt=<SelectStmt ...

.. doctest::

   >>> from pglast import enums
   >>> from pglast.visitors import Delete
   >>>
   >>> class DropNullConstraint(Visitor):
   ...     def visit_Constraint(self, ancestors, node):
   ...         if node.contype == enums.ConstrType.CONSTR_NULL:
   ...             return Delete
   ...
   >>> raw = parse_sql('create table foo (a integer null, b integer not null)')
   >>> DropNullConstraint()(raw)
   (<RawStmt stmt=<CreateStmt ...
   >>> print(RawStream()(raw))
   CREATE TABLE foo (a integer, b integer NOT NULL)

Customize a :func:`node printer <pglast.printers.node_printer>`
===============================================================

.. doctest::

   >>> sql = 'update translations set italian=$2 where word=$1'
   >>> print(prettify(sql))
   UPDATE translations
   SET italian = $2
   WHERE word = $1
   >>> from pglast.printers import node_printer
   >>> @node_printer(ast.ParamRef, override=True)
   ... def replace_param_ref(node, output):
   ...     output.write(repr(args[node.number - 1]))
   ...
   >>> args = ['Hello', 'Ciao']
   >>> print(prettify(sql, safety_belt=False))
   UPDATE translations
   SET italian = 'Ciao'
   WHERE word = 'Hello'

:func:`Iterate <pglast.split>` over each statement
==================================================

By default, the :func:`split` function uses the parser to do its job:

.. doctest::

   >>> from pglast import split
   >>> for statement in split('select 1; select 2'):
   ...     print(statement)
   ...
   select 1
   select 2

and thus it raises an error if the statement contains errors:

.. doctest::

   >>> split('select 1 from; select 2')
   Traceback (most recent call last):
     ...
   pglast.parser.ParseError: syntax error at or near ";", at location 14

In this case, you can use a variant that uses the lexical *scanner* instead:

.. doctest::

   >>> for statement in split('select 1 from; select 2', with_parser=False):
   ...     print(statement)
   ...
   select 1 from
   select 2

.. _cli:

------------
Command line
------------

Reformat a ``SQL`` statement
============================

.. code-block:: shell

   $ echo "select a,b,c from sometable" | pgpp
   SELECT a
        , b
        , c
   FROM sometable

   $ pgpp -S "select a, case when a=1 then 'singular' else 'plural' end from test"
   SELECT a
        , CASE
            WHEN (a = 1)
              THEN 'singular'
            ELSE 'plural'
          END
   FROM test

   $ echo 'update "table" set value=123 where value is null' | pgpp
   UPDATE "table"
   SET value = 123
   WHERE value IS NULL

   $ echo "
   insert into t (id, description)
   values (1, 'this is short enough'),
          (2, 'this is too long, and will be splitted')" | pgpp -s 20
   INSERT INTO t (id, description)
   VALUES (1, 'this is short enough')
        , (2, 'this is too long, an'
              'd will be splitted')

Get a more compact representation
=================================

.. code-block:: shell

   $ pgpp --compact 30 -S "select a,b,c from st where a='longvalue1' and b='longvalue2'"
   SELECT a, b, c
   FROM st
   WHERE (a = 'longvalue1')
     AND (b = 'longvalue2')

   $ pgpp --compact 60 -S "select a,b,c from st where a='longvalue1' and b='longvalue2'"
   SELECT a, b, c
   FROM st
   WHERE (a = 'longvalue1') AND (b = 'longvalue2')

Obtain the *parse tree* of a ``SQL`` statement
==============================================

.. code-block:: shell

   $ pgpp --parse-tree --statement "select 1"
   [{'@': 'RawStmt',
     'stmt': {'@': 'SelectStmt',
              'all': False,
              'limitOption': <LimitOption.LIMIT_OPTION_DEFAULT: 0>,
              'op': <SetOperation.SETOP_NONE: 0>,
              'targetList': ({'@': 'ResTarget',
                              'location': 7,
                              'val': {'@': 'A_Const',
                                      'location': 7,
                                      'val': {'@': 'Integer', 'val': 1}}},)},
     'stmt_len': 0,
     'stmt_location': 0}]

Preserve comments
=================

.. code-block:: shell

   $ pgpp --preserve-comments -S "/* Header */ select 1"
   /* Header */ SELECT 1

   $ echo -e "--what?\nselect foo\n--where?\nfrom bar" | pgpp -C
   --what?
   SELECT foo
   FROM
      --where?
   bar

   $ echo -e "--what?\nselect foo\n/*where?*/from bar\n--end" | pgpp -C
   --what?
   SELECT foo
   FROM
      /*where?*/ bar
   --end

.. note:: Preserving comments is always hard and far from a perfect science: not all AST nodes
          carry their exact location, so it is not possible to differentiate between
          ``SELECT * /*comment*/ FROM foo`` and ``SELECT * FROM /*comment*/ foo``.


Functions vs SQL syntax
=======================

.. code-block:: shell

   $ pgpp -S "select extract(hour from t1.modtime) from t1"
   SELECT pg_catalog.date_part('hour', t1.modtime)
   FROM t1

   $ pgpp --special-functions -S "select extract(hour from t1.modtime) from t1"
   SELECT EXTRACT(HOUR FROM t1.modtime)
   FROM t1

   $ echo "
   select substring('123',2,3),
          regexp_split_to_array('x,x,x', ','),
          btrim('xxx'), trim('xxx'),
          POSITION('hour' in trim(substring('xyz hour ',1,6)))
   " | pgpp
   SELECT pg_catalog.substring('123', 2, 3)
        , regexp_split_to_array('x,x,x', ',')
        , btrim('xxx')
        , pg_catalog.btrim('xxx')
        , pg_catalog.position(pg_catalog.btrim(pg_catalog.substring('xyz hour ', 1, 6))
                            , 'hour')

   $ echo "
   select substring('123',2,3),
          regexp_split_to_array('x,x,x', ','),
          btrim('xxx'), trim('xxx'),
          POSITION('hour' in trim(substring('xyz hour ',1,6)))
   " | pgpp -f --remove-pg_catalog-from-functions
   SELECT substring('123', 2, 3)
        , regexp_split_to_array('x,x,x', ',')
        , btrim('xxx')
        , btrim('xxx')
        , pg_catalog.position(btrim(substring('xyz hour ', 1, 6))
                            , 'hour')
