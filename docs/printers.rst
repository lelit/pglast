.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- Per-node specialized printer functions
.. :Created:   gio 10 ago 2017 13:23:18 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

============================================================
 :mod:`pg_query.printers` --- Specialized printer functions
============================================================

.. module:: pg_query.printers
   :synopsis: Specialized printer functions

This module implements the specialized functions that for any given *tag* define how the
associated :class:`~.node.Node` will be serialized.

.. toctree::
   :maxdepth: 2
   :caption: Printer functions

   ddl
   dml
