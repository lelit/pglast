# -*- coding: utf-8 -*-
# :Project:   pg_query -- DO NOT EDIT: automatically extracted from lockoptions.h @ 10-latest-0-g60de51e
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

import enum


class LockClauseStrength(enum.IntEnum):
    LCS_NONE = 0
    LCS_FORKEYSHARE = enum.auto()
    LCS_FORSHARE = enum.auto()
    LCS_FORNOKEYUPDATE = enum.auto()
    LCS_FORUPDATE = enum.auto()

class LockWaitPolicy(enum.IntEnum):
    LockWaitBlock = 0
    LockWaitSkip = enum.auto()
    LockWaitError = enum.auto()
