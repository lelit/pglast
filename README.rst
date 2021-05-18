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
:Status: |build| |doc| |codecov|
:Version: `3`__

__ https://www.gnu.org/licenses/gpl.html
__ https://pglast.readthedocs.io/en/v3/development.html#history

.. |build| image:: https://github.com/lelit/pglast/actions/workflows/ci.yml/badge.svg?branch=v3
   :target: https://github.com/lelit/pglast/actions/workflows/ci.yml
   :alt: Build status
.. |doc| image:: https://readthedocs.org/projects/pglast/badge/?version=v3
   :target: https://readthedocs.org/projects/pglast/builds/
   :alt: Documentation status
.. |codecov| image:: https://codecov.io/gh/lelit/pglast/branch/v3/graph/badge.svg?token=A90D8tWnft
   :target: https://codecov.io/gh/lelit/pglast
   :alt: Test coverage status

This is a Python 3 module that exposes the *parse tree* of a PostgreSQL__ statement (extracted
by the almost standard PG parser repackaged as a standalone static library by `libpg_query`__)
as set of interconnected *nodes*, usually called an *abstract syntax tree*.

__ https://www.postgresql.org/
__ https://github.com/pganalyze/libpg_query

See a `more detailed introduction`__ in the documentation_.

__ https://pglast.readthedocs.io/en/v3/introduction.html


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
__ https://codecov.io/gh/lelit/pglast/branch/v3/


Documentation
-------------

Latest documentation is hosted by `Read the Docs`__ at http://pglast.readthedocs.io/

__ https://readthedocs.org/
