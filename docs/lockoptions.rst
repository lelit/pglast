.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2019 Lele Gaifax
..

================================================================================
 :mod:`pglast.enums.lockoptions` --- Constants extracted from `lockoptions.h`__
================================================================================

__ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/lockoptions.h

.. module:: pglast.enums.lockoptions
   :synopsis: Constants extracted from lockoptions.h


.. class:: pglast.enums.lockoptions.LockClauseStrength

   Corresponds to the `LockClauseStrength enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/lockoptions.h#l21>`__.

   .. data:: LCS_NONE

   .. data:: LCS_FORKEYSHARE

   .. data:: LCS_FORSHARE

   .. data:: LCS_FORNOKEYUPDATE

   .. data:: LCS_FORUPDATE


.. class:: pglast.enums.lockoptions.LockTupleMode

   Corresponds to the `LockTupleMode enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/lockoptions.h#l49>`__.

   .. data:: LockTupleKeyShare

   .. data:: LockTupleShare

   .. data:: LockTupleNoKeyExclusive

   .. data:: LockTupleExclusive


.. class:: pglast.enums.lockoptions.LockWaitPolicy

   Corresponds to the `LockWaitPolicy enum <https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;hb=refs/tags/REL_12_1;f=src/include/nodes/lockoptions.h#l36>`__.

   .. data:: LockWaitBlock

   .. data:: LockWaitSkip

   .. data:: LockWaitError
