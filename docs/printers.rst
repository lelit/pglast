.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Per-node specialized printer functions
.. :Created:   gio 10 ago 2017 13:23:18 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2021, 2022 Lele Gaifax
..

==========================================================
 :mod:`pglast.printers` --- Specialized printer functions
==========================================================

.. module:: pglast.printers
   :synopsis: Specialized printer functions

This module implements the specialized functions that define how a particular
:class:`~.ast.Node` will be serialized.

.. autodata:: NODE_PRINTERS

.. autodata:: SPECIAL_FUNCTIONS

.. autoexception:: PrinterAlreadyPresentError

.. autofunction:: get_printer_for_node

.. autofunction:: node_printer

.. autofunction:: special_function

.. toctree::
   :maxdepth: 2
   :caption: Printer functions

   ddl
   dml
