.. -*- coding: utf-8 -*-
.. :Project:   pg_query -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017 Lele Gaifax
..

==================================================================================
 :mod:`pg_query.enums.lockoptions` --- Constants extracted from `lockoptions.h`__
==================================================================================

__ https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/lockoptions.h

.. module:: pg_query.enums.lockoptions


.. class:: pg_query.enums.lockoptions.LockClauseStrength

   Corresponds to the `LockClauseStrength enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/lockoptions.h#L21>`__.

   .. data:: LCS_NONE

   .. data:: LCS_FORKEYSHARE

   .. data:: LCS_FORSHARE

   .. data:: LCS_FORNOKEYUPDATE

   .. data:: LCS_FORUPDATE


.. class:: pg_query.enums.lockoptions.LockWaitPolicy

   Corresponds to the `LockWaitPolicy enum <https://github.com/lfittl/libpg_query/blob/43ce2e8/src/postgres/include/nodes/lockoptions.h#L36>`__.

   .. data:: LockWaitBlock

   .. data:: LockWaitSkip

   .. data:: LockWaitError
