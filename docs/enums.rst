.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- Enums documentation
.. :Created:   gio 10 ago 2017 12:44:33 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

================================================
 :mod:`pg_query.enums` --- Enumerated constants
================================================

.. module:: pg_query.enums
   :synopsis: The constants extracted automatically from PG headers

This module contains all the constants that are used to give a meaning to some *scalar* values
of the various kinds of nodes. Most of these constants are grouped in :class:`enum.Enum`
subclasses.

Currently they are collected by parsing the following headers:

- `lockoptions.h`__
- `nodes.h`__
- `parsenodes.h`__
- `primnodes.h`__

__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/lockoptions.h;hb=HEAD
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/nodes.h;hb=HEAD
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/parsenodes.h;hb=HEAD
__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/primnodes.h;hb=HEAD


.. automodule:: pg_query.enums.lockoptions
   :members:

.. automodule:: pg_query.enums.nodes
   :members:

.. automodule:: pg_query.enums.primnodes
   :members:

.. automodule:: pg_query.enums.parsenodes
   :members:
