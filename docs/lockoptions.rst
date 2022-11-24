.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2022 Lele Gaifax
..

================================================================================
 :mod:`pglast.enums.lockoptions` --- Constants extracted from `lockoptions.h`__
================================================================================

__ https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/lockoptions.h

.. module:: pglast.enums.lockoptions
   :synopsis: Constants extracted from lockoptions.h


.. class:: pglast.enums.lockoptions.LockClauseStrength

   Corresponds to the `LockClauseStrength enum <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/lockoptions.h#L21>`__.

   .. data:: LCS_NONE

   .. data:: LCS_FORKEYSHARE

   .. data:: LCS_FORSHARE

   .. data:: LCS_FORNOKEYUPDATE

   .. data:: LCS_FORUPDATE


.. class:: pglast.enums.lockoptions.LockTupleMode

   Corresponds to the `LockTupleMode enum <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/lockoptions.h#L49>`__.

   .. data:: LockTupleKeyShare

   .. data:: LockTupleShare

   .. data:: LockTupleNoKeyExclusive

   .. data:: LockTupleExclusive


.. class:: pglast.enums.lockoptions.LockWaitPolicy

   Corresponds to the `LockWaitPolicy enum <https://github.com/pganalyze/libpg_query/blob/6ebd8d8/src/postgres/include/nodes/lockoptions.h#L36>`__.

   .. data:: LockWaitBlock

   .. data:: LockWaitSkip

   .. data:: LockWaitError
