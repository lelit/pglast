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

.. data:: NODE_PRINTERS

   Registry of specialized printers, keyed by their `tag`.

.. exception:: PrinterAlreadyPresentError

   Exception raised trying to register another function for a tag already present.

.. function:: get_printer_for_node_tag(node_tag)

   Get specific printer implementation for given `node_tag`.

.. function:: node_printer(node_tag, override=False)

   Decorator to register a specific printer implementation for given `node_tag`.

   :param str node_tag: the node tag
   :param bool override: when ``True`` the function will be registered even if already
                         present

.. autoclass:: OutputStream
   :members:

.. autoclass:: RawStream
   :members:
   :special-members: __call__

.. autoclass:: IndentedStream
   :members:
