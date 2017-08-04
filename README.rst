.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- Pythonic wrapper around libpg_query
.. :Created:   mer 02 ago 2017 14:49:24 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

==========
 pg_query
==========

Pythonic wrapper around libpg_query
===================================

 :author: Lele Gaifax
 :contact: lele@metapensiero.it
 :license: GNU General Public License version 3 or later

This is a Python 3.6+ implementation of a wrapper to `libpg_query`__, a C library that
repackages the PostgreSQL__ language parser as a standalone static library.

It is similar to the more mature `psqlparse`__, but has different goals:

- it targets only Python 3 (more precisely, only 3.6 or higher, mainly because I'm lazy and the
  enums extraction code uses the `auto()`__ helper of the standard library ``enum`` module)

- it aims to target PostgreSQL 10 (in `beta 2`__ as I'm writing this), taking advantage of a
  work-in-progress `branch`__ of the libpg_query library

- it uses a more dynamic approach to represent the *parse tree*; this has a twofold advantage:

  1. it is much less boring to code, because there's no need to write one Python class for each
     PostgreSQL node tag

  2. the representation is version agnostic, it can be adapted to newer/older Elephants in a
     snap

- it allows to explore the parse tree in both directions, as each node carries a reference to
  the node from which it stems: this is the main reason I started this project, because while
  implementing the `pretty printing feature`__ for psqlparse I realized that some kinds of
  nodes require that knowledge to determine their textual representation

- it does not introduce arbitrary renames of tags and attributes, so what you read in
  PostgreSQL documentation/sources is available without the hassle of guessing how a symbol has
  been mapped

- not very important, but I guess it is much more performant, as basically it does not
  duplicates the original parse tree into every instance

__ https://github.com/lfittl/libpg_query
__ https://www.postgresql.org/
__ https://pypi.python.org/pypi/psqlparse
__ https://docs.python.org/3/library/enum.html#enum.auto
__ https://www.postgresql.org/about/news/1763/
__ https://github.com/lfittl/libpg_query/tree/10-latest
__ https://github.com/alculquicondor/psqlparse/issues/20


Installation
------------

Once this is released to PyPI, the following command will do::

  $ pip install pg_query

Until then, you have to clone the repository::

  $ git clone https://github.com/lelit/pg_query.git --recursive

and install from there::

  $ pip install ./pg_query


Examples of usage
-----------------

* Parse an ``SQL`` statement and get its *AST* root node::

   >>> from pg_query import Node, parse_sql
   >>> root = Node(parse_sql('SELECT foo FROM bar'))

* Recursively traverse the parse tree::

   >>> for node in root.traverse():
   ...   print(node)
   ...
   None[0]=<RawStmt>
   stmt=<SelectStmt>
   fromClause[0]=<RangeVar>
   inh=True
   location=16
   relname='bar'
   relpersistence='p'
   op=0
   targetList[0]=<ResTarget>
   location=7
   val=<ColumnRef>
   fields[0]=<String>
   str='foo'
   location=7

* Get a particular node::

   >>> from_clause = root[0].stmt.fromClause
   >>> print(from_clause)
   fromClause=[<RangeVar>]

* Obtain some information about a node::

   >>> range_var = from_clause[0]
   >>> print(range_var.node_tag)
   RangeVar
   >>> print(range_var.attribute_names)
   dict_keys(['relname', 'inh', 'relpersistence', 'location'])
   >>> print(range_var.parent_node)
   stmt=<SelectStmt>
