.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- Printer documentation
.. :Created:   gio 10 ago 2017 10:58:06 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

=========================================================
 :mod:`pg_query.printer` --- The serialization machinery
=========================================================

.. module:: pg_query.printer
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
