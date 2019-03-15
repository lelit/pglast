# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from lockoptions.h @ 10-1.0.2-0-gd710cb0
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2019 Lele Gaifax
#

try:
    from enum import Enum, IntEnum, IntFlag, auto
except ImportError: #pragma: no cover
    # Python < 3.6
    from aenum import Enum, IntEnum, IntFlag, auto


class LockClauseStrength(IntEnum):
    LCS_NONE = 0
    LCS_FORKEYSHARE = auto()
    LCS_FORSHARE = auto()
    LCS_FORNOKEYUPDATE = auto()
    LCS_FORUPDATE = auto()

class LockWaitPolicy(IntEnum):
    LockWaitBlock = 0
    LockWaitSkip = auto()
    LockWaitError = auto()
