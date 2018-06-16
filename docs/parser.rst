.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Parser module
.. :Created:   gio 10 ago 2017 10:19:26 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018 Lele Gaifax
..

===========================================================
 :mod:`pglast.parser` --- The interface with libpg_query
===========================================================

.. module:: pglast.parser
   :synopsis: The interface with libpg_query

This module is a C extension written in Cython__ that exposes a few functions from the
underlying ``libpg_query`` library it links against.

.. function:: get_postgresql_version()

   :returns: a tuple

   Return the PostgreSQL version as a tuple (`major`, `minor`, `patch`).

.. function:: parse_sql(query)

   :param str query: The SQL statement
   :returns: a dictionary

   Parse the given `query`, a string with the ``SQL`` statement(s), and return the
   corresponding *parse tree*.

.. function:: parse_plpgsql(query)

   :param str query: The PLpgSQL statement
   :returns: a dictionary

   Parse the given `query`, a string with the ``plpgsql`` statement(s), and return the
   corresponding *parse tree*.


__ http://cython.org/
