.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- Introduction
.. :Created:   gio 10 ago 2017 10:03:30 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

==============
 Introduction
==============

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
