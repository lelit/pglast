.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Documentation
.. :Created:   gio 10 ago 2017 09:56:59 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2019, 2021, 2022 Lele Gaifax
..

========
 pglast
========

PostgreSQL Languages AST and statements prettifier
==================================================

:author: Lele Gaifax
:contact: lele@metapensiero.it
:license: `GNU General Public License version 3 or later`__
:version: `4`__

__ https://www.gnu.org/licenses/gpl.html
__ https://pglast.readthedocs.io/en/v4/introduction.html

This is a Python 3 module that exposes the *parse tree* of a PostgreSQL__ statement (extracted
by the almost standard PG parser repackaged as a standalone static library by `libpg_query`__)
as set of interconnected *nodes*, usually called an *abstract syntax tree*.

__ https://www.postgresql.org/
__ https://github.com/pganalyze/libpg_query


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
