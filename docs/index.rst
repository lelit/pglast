.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Documentation
.. :Created:   gio 10 ago 2017 09:56:59 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2019 Lele Gaifax
..

========
 pglast
========

PostgreSQL Languages AST and statements prettifier
==================================================

:author: Lele Gaifax
:contact: lele@metapensiero.it
:license: GNU General Public License version 3 or later
:version: 2

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

Since latest version of PostgreSQL inevitably introduced some backward incompatibilities, I
bumped the major version of ``pglast`` to better reflect the fact.

As I'm writing this, the fate of ``PR #62`` is still unclear, so for the time being I switched
the ``libpg_query`` submodule to Ronan's fork.

__ https://github.com/lfittl/libpg_query/pull/62
__ https://github.com/lelit/pglast/pull/36


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   installation
   development
   usage
   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
