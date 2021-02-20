.. -*- coding: utf-8 -*-
.. :Project:   pglast -- PostgreSQL Languages AST
.. :Created:   mer 02 ago 2017 14:49:24 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2019, 2020, 2021 Lele Gaifax
..

========
 pglast
========

PostgreSQL Languages AST and statements prettifier
==================================================

:Author: Lele Gaifax
:Contact: lele@metapensiero.it
:License: `GNU General Public License version 3 or later`__
:Status: |build| |doc|
:Version: `2`__

__ https://www.gnu.org/licenses/gpl.html
.. |build| image:: https://github.com/lelit/pglast/actions/workflows/ci.yml/badge.svg?branch=v2
   :target: https://github.com/lelit/pglast/actions/workflows/ci.yml
   :alt: Build status
.. |doc| image:: https://readthedocs.org/projects/pglast/badge/?version=latest
   :target: https://readthedocs.org/projects/pglast/builds/
   :alt: Documentation status
__ `Version 2`_

This is a Python 3 module that exposes the *parse tree* of a PostgreSQL__ statement (extracted
by the almost standard PG parser repackaged as a standalone static library by `libpg_query`__)
as set of interconnected *nodes*, usually called an *abstract syntax tree*.

__ https://www.postgresql.org/
__ https://github.com/lfittl/libpg_query


Foreword
--------

I needed a better SQL reformatter than the one implemented by `sqlparse`__, and was annoyed by
a few glitches (subselects__ in particular) that ruins the otherwise excellent job it does,
considering that it is a generic library that tries to swallow many different SQL dialects.

__ https://pypi.org/project/sqlparse/
__ https://github.com/andialbrecht/sqlparse/issues/334

When I found `psqlparse`__ I decided to try implementing a PostgreSQL `focused tool`__: at the
beginning it's been easier than I feared, but I quickly hit some shortcomings in that
implementation, so I opted for writing my own solution restarting from scratch, with the
following goals:

__ https://github.com/alculquicondor/psqlparse
__ https://github.com/alculquicondor/psqlparse/pull/22

- target only Python 3.4+

- target PostgreSQL 10+

- use a more dynamic approach to represent the *parse tree*, with a twofold advantage:

  1. it is much less boring to code, because there's no need to write one Python class for each
     PostgreSQL node tag

  2. the representation is version agnostic, it can be adapted to newer/older Elephants in a
     snap

- allow exploration of parse tree in both directions, because I realized that some kinds of
  nodes require that knowledge to determine their textual representation

- avoid introducing arbitrary renames of tags and attributes, so what you read in PostgreSQL
  documentation/sources is available without the hassle of guessing how a symbol has been
  mapped

- use a `zero copy`__ approach, keeping the original parse tree returned from the underlying
  libpg_query functions and have each node just borrow a reference to its own subtree

__ https://en.wikipedia.org/wiki/Zero-copy


Version 2
~~~~~~~~~

In late 2019, Ronan Dunklau opened `PR #62`__ against ``libpg_query``, that reimplemented the
build machinery of the library to make it easier (read, semi-automatic) to support PostgreSQL
v12, and `PR #36`__ to bring ``pglast`` in line.

Since that version of PostgreSQL inevitably introduced some backward incompatibilities, I
bumped the major version of ``pglast`` to better reflect the fact.

As I'm writing this, the fate of ``PR #62`` is still unclear, so for the time being I switched
the ``libpg_query`` submodule to Ronan's fork.

I'm going to keep version 1 aligned to the original Lukas' `PG 10 branch`__. In all likelihood
version 3 will target PostgreSQL 13 once his work on `PG 13 branch`__ reaches stability.

.. important:: This version requires Python 3.6 or greater, due to usage of `f-strings`.

__ https://github.com/lfittl/libpg_query/pull/62
__ https://github.com/lelit/pglast/pull/36
__ https://github.com/lfittl/libpg_query/tree/10-latest
__ https://github.com/lfittl/libpg_query/tree/13-latest-develop


Introduction
------------

At the lower level the module exposes two libpg_query functions, ``parse_sql()`` and
``parse_plpgsql()``, that take respectively an ``SQL`` statement and a ``PLpgSQL`` statement
and return a *parse tree* as a hierarchy of Python dictionaries, lists and scalar values. In
some cases these scalars correspond to some C ``typedef enums``, that are automatically
extracted from the PostgreSQL headers mentioned above and are available as ``pglast.enums``.

At a higher level that tree is represented by three Python classes, a ``Node`` that represents
a single node, a ``List`` that wraps a sequence of nodes and a ``Scalar`` for plain values such
a *strings*, *integers*, *booleans* or *none*.

Every node is identified by a *tag*, a string label that characterizes its content that is
exposed as a set of *attributes* as well as with a dictionary-like interface (technically they
implements both a ``__getattr__`` method and a ``__getitem__`` method). When asked for an
attribute, the node returns an instance of the base classes, i.e. another ``Node``, or a
``List`` or a ``Scalar``, depending on the data type of that item. When the node does not
contain the requested attribute it returns a singleton ``Missing`` marker instance.

A ``List`` wraps a plain Python ``list`` and may contains a sequence of ``Node`` instances, or
in some cases other sub-lists, that can be accessed with the usual syntax, or iterated.

Finally, a ``Scalar`` carries a single value of some type, accessible through its ``value``
attribute.

On top of that, the module implements two serializations, one that transforms a ``Node`` into a
*raw* textual representation and another that returns a *prettified* representation. The latter
is exposed by the ``pgpp`` CLI tool, see below for an example.


Installation
------------

As usual, the easiest way is with pip::

  $ pip install pglast

Alternatively you can clone the repository::

  $ git clone https://github.com/lelit/pglast.git --recursive

and install from there::

  $ pip install ./pglast


Development
-----------

There is a set of *makefiles* implementing the most common operations, a ``make help`` will
show a brief table of contents. A comprehensive test suite, based on pytest__, covers 98% of
the source lines.

__ https://docs.pytest.org/en/latest/


Examples of usage
-----------------

* Parse an ``SQL`` statement and get its *AST* root node::

   >>> from pglast import Node, parse_sql
   >>> root = Node(parse_sql('SELECT foo FROM bar'))
   >>> print(root)
   None=[1*{RawStmt}]

* Recursively traverse the parse tree::

   >>> for node in root.traverse():
   ...   print(node)
   ...
   None[0]={RawStmt}
   stmt={SelectStmt}
   fromClause[0]={RangeVar}
   inh=<True>
   location=<16>
   relname=<'bar'>
   relpersistence=<'p'>
   op=<0>
   targetList[0]={ResTarget}
   location=<7>
   val={ColumnRef}
   fields[0]={String}
   str=<'foo'>
   location=<7>

  As you can see, the ``repr``\ esentation of each value is mnemonic: ``{some_tag}`` means a
  ``Node`` with tag ``some_tag``, ``[X*{some_tag}]`` is a ``List`` containing `X` nodes of that
  particular kind\ [*]_ and ``<value>`` is a ``Scalar``.

* Get a particular node::

   >>> from_clause = root[0].stmt.fromClause
   >>> print(from_clause)
   fromClause=[1*{RangeVar}]

* Obtain some information about a node::

   >>> range_var = from_clause[0]
   >>> print(range_var.node_tag)
   RangeVar
   >>> print(range_var.attribute_names)
   dict_keys(['relname', 'inh', 'relpersistence', 'location'])
   >>> print(range_var.parent_node)
   stmt={SelectStmt}

* Iterate over nodes::

   >>> for a in from_clause:
   ...     print(a)
   ...     for b in a:
   ...         print(b)
   ...
   fromClause[0]={RangeVar}
   inh=<True>
   location=<16>
   relname=<'bar'>
   relpersistence=<'p'>

* Reformat a SQL statement\ [*]_ from the command line::

   $ echo "select a,b,c from sometable" | pgpp
   SELECT a
        , b
        , c
   FROM sometable

   $ echo "select a,b,c from sometable" | pgpp -c
   SELECT a,
          b,
          c
   FROM sometable

   $ echo "select a, case when a=1 then 'singular' else 'plural' end from test" > /tmp/q.sql
   $ pgpp /tmp/q.sql
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

* Programmatically reformat a SQL statement::

   >>> from pglast import prettify
   >>> print(prettify('delete from sometable where value is null'))
   DELETE FROM sometable
   WHERE value IS NULL

.. [*] This is an approximation, because in principle a list could contain different kinds of
       nodes, or even sub-lists in some cases: the ``List`` representation arbitrarily shows
       the tag of the first object.

.. [*] Currently this covers most `DML` statements such as ``SELECT``\ s, ``INSERT``\ s,
       ``DELETE``\ s and ``UPDATE``\ s, fulfilling my needs, but I'd like to extend it to
       handle also `DDL` statements and, why not, `PLpgSQL` instructions too.


Documentation
-------------

Latest documentation is hosted by `Read the Docs`__ at http://pglast.readthedocs.io/en/latest/

__ https://readthedocs.org/
