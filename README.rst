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
:Version: `3`__

__ https://www.gnu.org/licenses/gpl.html
.. |build| image:: https://github.com/lelit/pglast/actions/workflows/ci.yml/badge.svg?branch=v2
   :target: https://github.com/lelit/pglast/actions/workflows/ci.yml
   :alt: Build status
.. |doc| image:: https://readthedocs.org/projects/pglast/badge/?version=latest
   :target: https://readthedocs.org/projects/pglast/builds/
   :alt: Documentation status
__ `Version 3`_

This is a Python 3 module that exposes the *parse tree* of a PostgreSQL__ statement (extracted
by the almost standard PG parser repackaged as a standalone static library by `libpg_query`__)
as set of interconnected *nodes*, usually called an *abstract syntax tree*.

__ https://www.postgresql.org/
__ https://github.com/pganalyze/libpg_query


Introduction
------------

At the lower level the module exposes several ``libpg_query`` functions, ``parse_sql_json()``,
``parse_sql_protobuf()``, ``parse_plpgsql_json()``, ``fingerprint()``, ``scan``, ``split()``
and ``deparse_protobuf()``; the first two take an ``SQL`` statement and return the
correspondent *parse tree* respectively as a ``JSON`` encoded value and a ``Protobuf`` encoded
value; the third function takes a ``PLpgSQL`` statement and returns the *parse tree* as
``JSON``, the fourth returns a sequence of *tokens* that compose a ``SQL`` statement, the fifth
returns a *signature* of the given statement, the sixth returns a sequence of the single
statements and the last one accepts a ``Protobuf``\ -serialized statement and reproduce the
original ``SQL`` statement.

One more function, ``parse_sql()``, returns the syntax tree represented by a hierarchy of
instances of the classes implemented in the ``pglast.ast`` module.

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
is exposed by the ``pgpp`` CLI tool, see the `Usage` section in the documentation for an
example.


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


Documentation
-------------

Latest documentation is hosted by `Read the Docs`__ at http://pglast.readthedocs.io/en/latest/

__ https://readthedocs.org/


History
-------

Version 1
#########

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
#########

In late 2019, Ronan Dunklau opened `PR #62`__ against ``libpg_query``, that reimplemented the
build machinery of the library to make it easier (read, semi-automatic) to support PostgreSQL
12, and `PR #36`__ to bring ``pglast`` in line.

Since that version of PostgreSQL inevitably introduced some backward incompatibilities, I
bumped the major version of ``pglast`` to better reflect the fact.

As I'm writing this, the fate of ``PR #62`` is still unclear, so for the time being I switched
the ``libpg_query`` submodule to Ronan's fork.

I'm going to keep version 1 aligned to the original Lukas' `PG 10 branch`__.

.. important:: This version requires Python 3.6 or greater, due to usage of `f-strings`.

__ https://github.com/pganalyze/libpg_query/pull/62
__ https://github.com/lelit/pglast/pull/36
__ https://github.com/pganalyze/libpg_query/tree/10-latest


Version 3
#########

In early 2021, Lukas put a considerable effort into evolving his library to target PostgreSQL
13. He introduced a richer `protobuf`__\-based AST serialization protocol, rewriting the
underlying machinery so that the same code is used to generate either a ``JSON`` or a
``protobuf`` stream.

__ https://developers.google.com/protocol-buffers

The approach has obvious advantages, but unfortunately both formats come with different
shortcomings, and I was not able to adapt ``pglast``. The ``JSON`` serialization has changed in
a way that it not anymore sufficient to rebuild the original ``AST`` because some attributes
now carry an *implicit* structure, that requires additional information to understand the
content (see issue `#82`__). OTOH, the ``Protobuf`` format is clumsy, at least on the Python
side: the Google's compiler creates a huge and unreadable module, while other implementations
(see `pyrobuf`__, `cprotobuf`__ and `betterproto`__) suffer of different issues (see issue
`#210`__).

__ https://github.com/pganalyze/libpg_query/issues/82#issuecomment-782616284
__ https://github.com/appnexus/pyrobuf
__ https://github.com/yihuang/cprotobuf
__ https://github.com/danielgtaylor/python-betterproto
__ https://github.com/danielgtaylor/python-betterproto/issues/210

After several attempts, I decided to follow a more rewarding way and implement a native Python
wrapper layer on top of PG parser's nodes.
