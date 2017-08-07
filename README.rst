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
repackages the PostgreSQL__ languages parser as a standalone static library.

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
  PostgreSQL documentation/sources\ [*]_ is available without the hassle of guessing how a
  symbol has been mapped

- not very important, but I guess it is much more performant, as basically it does not
  duplicates the original parse tree into every instance

.. [*] Currently what you can find in the following headers:

       - `nodes.h`__
       - `primnodes.h`__
       - `parsenodes.h`__
       - `lockoptions.h`__

__ https://github.com/lfittl/libpg_query
__ https://www.postgresql.org/
__ https://pypi.python.org/pypi/psqlparse
__ https://docs.python.org/3/library/enum.html#enum.auto
__ https://www.postgresql.org/about/news/1763/
__ https://github.com/lfittl/libpg_query/tree/10-latest
__ https://github.com/alculquicondor/psqlparse/issues/20
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/nodes.h;hb=HEAD
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/primnodes.h;hb=HEAD
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/parsenodes.h;hb=HEAD
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/lockoptions.h;hb=HEAD

Introduction
------------

At the lower level the module exposes two libpg_query functions, ``parse_sql()`` and
``parse_plpgsql()``, that take respectively an ``SQL`` statement and a ``PLpgSQL`` statement
and return a *parse tree* as a hierarchy of Python dictionaries, lists and scalar values. In
some cases these scalars correspond to some C ``typedef enums``, that are automatically
extracted from the PostgreSQL headers and are available as ``pg_query.enums``.

At a higher level that tree is represented by three Python classes, a ``Node`` that represents
a single node, a ``List`` that wraps a sequence of nodes and a ``Scalar`` for plain values such
a *strings*, *integers*, *booleans* or *none*.

Every node is identified by a *tag*, a string label that characterize its content that is
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
is exposed by the ``__main__`` entry point of the package, see below for an example.

Installation
------------

Once this is released to PyPI, the following command will do::

  $ pip install pg_query

Until then, you have to clone the repository::

  $ git clone https://github.com/lelit/pg_query.git --recursive

and install from there::

  $ pip install ./pg_query

Development
-----------

There is a set of *makefiles* implementing the most common operations, a ``make help`` will
show a brief table of contents. A comprehensive test suite, based on pytest__, covers 98% of
the source lines.

__ https://docs.pytest.org/en/latest/

Examples of usage
-----------------

* Parse an ``SQL`` statement and get its *AST* root node::

   >>> from pg_query import Node, parse_sql
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

   $ echo "select a,b,c from sometable" | python -m pg_query
   SELECT a
        , b
        , c
   FROM sometable

   $ echo 'update "table" set value=123 where value is null' | python -m pg_query
   UPDATE "table"
   SET value = 123
   WHERE value IS NULL

.. [*] This is an approximation, because in principle a list could contain different kinds of
       nodes, or even sub-lists in some cases: the ``List`` representation arbitrarily shows
       the tag of the first object.

.. [*] Currently this covers most `DML` statements such as ``SELECT``\ s, ``INSERT``\ s,
       ``DELETE``\ s and ``UPDATE``\ s, fulfilling my needs, but I'd like to extend it to
       handle also `DDL` statements and, why not, `PLpgSQL` instructions too.
