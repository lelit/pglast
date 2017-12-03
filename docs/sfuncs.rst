.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- Special functions documentation
.. :Created:   mer 22 nov 2017 09:04:18 CET
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

===============================================================
 :mod:`pg_query.printers.sfuncs` --- Special function printers
===============================================================

The PostgreSQL parser *translates* some ``SQL`` constructs into function calls, for example the
expression ``EXTRACT(YEAR FROM date_column)`` is represented the same as
``pg_catalog.date_part('year', date_column)``.

This module declares some of those equivalences, implementing alternative printers that will be
used when the option `special_functions` of the :class:`output stream <.printer.RawStream>` is
set to ``True``.

.. automodule:: pg_query.printers.sfuncs
   :synopsis: Special function printers
   :members:
