.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Introduction
.. :Created:   gio 10 ago 2017 10:03:30 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2021 Lele Gaifax
..

==============
 Introduction
==============

At the lower level the module exposes several `libpg_query`__ functions:

__ https://github.com/pganalyze/libpg_query

1. :func:`pglast.parser.parse_sql_json()`
2. :func:`pglast.parser.parse_sql_protobuf()`
3. :func:`pglast.parser.parse_plpgsql_json()`
4. :func:`pglast.parser.fingerprint()`
5. :func:`pglast.parser.scan()`
6. :func:`pglast.parser.split()`
7. :func:`pglast.parser.deparse_protobuf()`

The first two take an ``SQL`` statement and return the correspondent *parse tree* respectively
as a ``JSON`` encoded value and a ``Protobuf`` encoded value; the third function takes a
``PLpgSQL`` statement and returns the *parse tree* as ``JSON``, the fourth returns an *hash* of
the given statement that can be used to compare different ``SQL``\ s, the fifth returns a
sequence of *tokens* that compose a ``SQL`` statement, the sixth returns a sequence of the
single statements and the last one accepts a ``Protobuf``\ -serialized statement and reproduce
the original ``SQL`` statement.

One more function, :func:`pglast.parser.parse_sql()`, is similar to ``parse_sql_json()`` but
instead of ``JSON`` returns the syntax tree represented by a hierarchy of instances of the
classes implemented in the :mod:`pglast.ast` module.

On top of that, the module implements two serializations, one that transforms a ``Node`` into a
:class:`raw <pglast.stream.RawStream>` textual representation and another that returns a
:class:`prettified <pglast.stream.IndentedStream` representation. The latter is exposed by the
``pgpp`` CLI tool, see the :ref:`Command line <cli>` section of the :ref:`examples of usage
<usage>`.
