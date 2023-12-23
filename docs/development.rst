.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Development
.. :Created:   gio 10 ago 2017 10:04:43 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2021, 2022, 2023 Lele Gaifax
..

=============
 Development
=============

There is a set of *makefiles* implementing the most common operations, a ``make help`` will
show a brief table of contents. A comprehensive test suite, based on pytest__, covers__ nearly
99% of the source lines.

__ https://docs.pytest.org/en/latest/
__ https://codecov.io/gh/lelit/pglast/branch/v3/


History
-------

For a more detailed evolution steps see :ref:`changes`.

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

In late 2019, Ronan__ opened `PR #62`__ against ``libpg_query``, that reimplemented the
build machinery of the library to make it easier (read, semi-automatic) to support PostgreSQL
12, and `PR #36`__ to bring ``pglast`` in line.

__ https://github.com/rdunklau
__ https://github.com/pganalyze/libpg_query/pull/62
__ https://github.com/lelit/pglast/pull/36

Since that version of PostgreSQL inevitably introduced some backward incompatibilities, I
bumped the major version of ``pglast`` to better reflect the fact.

This version only had some `development releases`__, since ``PR #62`` has been superseded__.

__ https://pypi.org/project/pglast/2.0.dev3/
__ https://github.com/pganalyze/libpg_query/pull/62#issuecomment-801659703

.. important:: This version requires Python 3.6 or greater, due to usage of `f-strings`.


Version 3
#########

In early 2021, Lukas__ put a considerable effort into evolving his library to target PostgreSQL
13. He introduced a richer `protobuf`__\-based AST serialization protocol, rewriting the
underlying machinery so that the same code is used to generate either a ``JSON`` or a
``protobuf`` stream.

__ https://github.com/lfittl
__ https://developers.google.com/protocol-buffers

The approach has obvious advantages, but unfortunately both formats come with different
shortcomings, and I was not able to adapt ``pglast``. The ``JSON`` serialization has changed in
a way that it is not sufficient anymore to rebuild the original ``AST`` because some attributes
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
wrapper layer on top of PG parser's nodes, :mod:`pglast.ast`.

Ronan and Hong__ helped a lot respectively with `PR #72`__ and `PR #77`__. Last but not least,
https://bit.io/ kindly sponsored the project.

__ https://github.com/hcheng2002cn
__ https://github.com/lelit/pglast/pull/72
__ https://github.com/lelit/pglast/pull/77


Version 4
#########

The ultimate goal of this version is targeting ``PostgreSQL 14``, exploiting the combined
effort of `Tessa Lisanti`__ and `Wolfgang Walther`__ who upgraded ``libpg_query`` to the latest
PG 14 parser that eventually has been finalized in the `14-latest`__ branch.

__ https://github.com/tlisanti/libpg_query/tree/14-latest
__ https://github.com/wolfgangwalther/libpg_query/tree/pg-14
__ https://github.com/pganalyze/libpg_query/tree/14-latest

While I was waiting for that to happen, I simplified the code getting rid of the `wrapper
classes`__. They were required in `version 1`_, when ``pglast`` consumed the
``JSON``-serialized parse tree emitted by ``libpg_query`` exposing those structures as generic
``Node``\ s distinguishable by their *tag*.

`Version 3`_ retained them, although rewritten on top of the new concrete AST parser nodes, to
make them aware of their ancestry, notion required by some printers to choose different
representations.

Now the lineage is injected directly into the AST nodes by the printer machinery (cheaper than
updating/computing it when setting/accessing each *property*) and all the printer functions
receive one concrete AST node.

__ https://github.com/lelit/pglast/issues/80


Version 5
#########

This version tracks the `15-latest`__ branch of ``libpg_query`` and thus targets ``PostgreSQL
15``: other than handling new statements (`MERGE`__ to mention just one) and revised
syntaxes, there are currently no other significant differences from `Version 4`_.

__ https://github.com/pganalyze/libpg_query/tree/15-latest
__ https://www.postgresql.org/docs/15/sql-merge.html


Version 6
#########

This version tracks the `16-latest`__ branch of ``libpg_query`` and thus targets ``PostgreSQL
16``: other than handling new statements (most notably, ``SQL/JSON`` constructor functions like
``json_array()`` or aggregators such as ``json_objectagg()``) and revised syntaxes, there are
currently no other significant differences from `Version 5`_.

__ https://github.com/pganalyze/libpg_query/tree/16-latest

.. toctree::
   :maxdepth: 2

   changes
