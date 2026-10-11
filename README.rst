.. -*- coding: utf-8 -*-
.. :Project:   pglast — PostgreSQL Languages AST
.. :Created:   mer 02 ago 2017 14:49:24 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2026 Lele Gaifax
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
:Version: `8`__

__ https://www.gnu.org/licenses/gpl.html
__ https://pglast.readthedocs.io/en/v8/development.html#history

.. |build| image:: https://github.com/lelit/pglast/actions/workflows/ci.yml/badge.svg?branch=v8
   :target: https://github.com/lelit/pglast/actions/workflows/ci.yml
   :alt: Build status
.. |doc| image:: https://readthedocs.org/projects/pglast/badge/?version=v8
   :target: https://readthedocs.org/projects/pglast/builds/
   :alt: Documentation status

This is a Python 3 module that exposes the *parse tree* of a PostgreSQL__ statement (extracted
by the almost standard PG parser repackaged as a standalone static library by `libpg_query`__)
as set of interconnected *nodes*, usually called an *abstract syntax tree*.

__ https://www.postgresql.org/
__ https://github.com/pganalyze/libpg_query

See a `more detailed introduction`__ in the documentation_.

__ https://pglast.readthedocs.io/en/v8/introduction.html


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
show a brief table of contents. A comprehensive test suite, based on pytest__, covers__ nearly
99% of the source lines.

__ https://docs.pytest.org/en/latest/
__ https://codecov.io/gh/lelit/pglast/branch/v8/


Contributing
~~~~~~~~~~~~

Many of the sources in this repository are *mechanically derived* from others: the enums, the
keyword sets, the ``pglast.ast`` module and its type stubs, the printer documentation and the
``parser.c`` translation are all produced by one of the tools in ``tools/``, driven by the
``Makefile``. Each of those files carries a ``DO NOT EDIT`` notice in its header, and none of
them should ever be modified by hand: change the generating tool, its input data or the recipe,
then rebuild with ``make build``.

Because a tiny change in a generator can produce an avalanche of changes in its output, two
developers working on unrelated areas of the same generator will rarely conflict on the
generator itself, but are bound to conflict on the generated sources when their branches are
merged. A handful of lines edited in one of the tools is enough to rewrite every file it
produces: skipping a few node definitions in ``tools/extract_ast.py``, for instance, was
followed by a regeneration touching more than twenty thousand lines, spread over the
``pglast.ast`` module, the enums, the keyword sets and ``parser.c``. The trigger can also come
from outside the tools: bumping ``libpg_query`` affects nearly all of the generated files,
since its revision is embedded in a comment of most of them, and a new release of ``Cython``
retranslates ``parser.c`` from scratch. In all those cases use "Update generated sources" as
the subject of the regeneration commit, or "Regenerate with Cython X.Y.Z" when that is what
triggered it, and do not let it carry any other modification.

.. important:: Please keep the *automatic regeneration* in a commit of its own, with nothing
               else in it: the ordinary changes of a branch then merge without trouble, and the
               regeneration commit can be easily resolved by simply re-running the generator on
               the merged tree.


Documentation
-------------

Latest documentation is hosted by `Read the Docs`__ at https://pglast.readthedocs.io/en/v8

__ https://readthedocs.org/
