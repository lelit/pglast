.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Printer documentation
.. :Created:   gio 10 ago 2017 10:58:06 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018 Lele Gaifax
..

=========================================================
 :mod:`pglast.printer` --- The serialization machinery
=========================================================

.. module:: pglast.printer
   :synopsis: The serialization machinery

.. autodata:: NODE_PRINTERS

.. autodata:: SPECIAL_FUNCTIONS

.. autoexception:: PrinterAlreadyPresentError

.. autofunction:: get_printer_for_node_tag

.. autofunction:: node_printer

.. autofunction:: special_function

.. autoclass:: OutputStream
   :members:

.. autoclass:: RawStream
   :members:
   :special-members: __call__

.. autoclass:: IndentedStream
   :members:
