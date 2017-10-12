.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- Documentation
.. :Created:   gio 10 ago 2017 09:56:59 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

==========
 pg_query
==========

Pythonic wrapper around libpg_query and SQL prettifier
======================================================

 :author: Lele Gaifax
 :contact: lele@metapensiero.it
 :license: GNU General Public License version 3 or later

This is a Python 3 implementation of a wrapper to `libpg_query`__, a C library that repackages
the PostgreSQL__ languages parser as a standalone static library.

__ https://github.com/lfittl/libpg_query
__ https://www.postgresql.org/

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

- target PostgreSQL 10 taking advantage of a work-in-progress `branch`__ of the libpg_query
  library

__ https://github.com/lfittl/libpg_query/tree/10-latest

- use a more dynamic approach to represent the *parse tree*, with a twofold advantage:

  1. it is much less boring to code, because there's no need to write one Python class for each
     PostgreSQL node tag

  2. the representation is version agnostic, it can be adapted to newer/older Elephants in a
     snap

- allow exploration of parse tree in both directions, because I realized that some kinds of
  nodes require that knowledge to determine their textual representation

- avoid introducing arbitrary renames of tags and attributes, so what you read in PostgreSQL
  documentation/sources\ [*]_ is available without the hassle of guessing how a symbol has been
  mapped

- use a `zero copy`__ approach, keeping the original parse tree returned from the underlying
  libpg_query functions and have each node just borrow a reference to its own subtree

__ https://en.wikipedia.org/wiki/Zero-copy

.. [*] Currently what you can find in the following headers:

       - `nodes.h`__
       - `primnodes.h`__
       - `parsenodes.h`__
       - `lockoptions.h`__

__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/nodes.h;hb=HEAD
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/primnodes.h;hb=HEAD
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/parsenodes.h;hb=HEAD
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/lockoptions.h;hb=HEAD


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
