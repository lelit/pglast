.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Node documentation
.. :Created:   gio 10 ago 2017 10:28:36 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2021 Lele Gaifax
..

=====================================================================
 :mod:`pglast.node` --- The higher level interface to the parse tree
=====================================================================

This module implements a set of classes that make it easier to deal with the :mod:`pglast.ast`
nodes.

The :class:`pglast.node.Node` wraps a single :class:`pglast.ast.Node` adding a reference to the
parent node; the class:`pglast.node.List` wraps a sequence of them and
:class:`pglast.node.Scalar` represents plain values such a *strings*, *integers*, *booleans* or
*none*.

Every node is identified by a *tag*, a string label that characterizes its content, exposed as
a set of *attributes* as well as with a dictionary-like interface (technically
:class:`pglast.node.Node` implements both a ``__getattr__`` method and a ``__getitem__``
method, while underlying :class:`pglast.ast.Node` only the former). When asked for an
attribute, the node returns an instance of the base classes, i.e. another ``Node``, or a
``List`` or a ``Scalar``, depending on the data type of that item. When the node does not
contain the requested attribute it returns a singleton :data:`pglast.node.Missing` marker
instance.

A ``List`` wraps a plain Python ``list`` and may contains a sequence of ``Node`` instances, or
in some cases other sub-lists, that can be accessed with the usual syntax, or iterated.

Finally, a ``Scalar`` carries a single value of some scalar type, accessible through its
``value`` attribute.

.. automodule:: pglast.node
   :synopsis: The higher level interface to the parse tree
   :members:
