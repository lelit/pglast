# -*- coding: utf-8 -*-
# :Project:   pg_query -- DO NOT EDIT: automatically extracted from lockoptions.h @ 10-latest-0-g1ec5c22
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

try:
    from enum import Enum, IntEnum, IntFlag, auto
except ImportError:
    # Python < 3.6
    from aenum import Enum, IntEnum, IntFlag, auto


class LockClauseStrength(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/lockoptions.h#L21>`__."

    LCS_NONE = 0
    LCS_FORKEYSHARE = auto()
    LCS_FORSHARE = auto()
    LCS_FORNOKEYUPDATE = auto()
    LCS_FORUPDATE = auto()

class LockWaitPolicy(IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/lockoptions.h#L36>`__."

    LockWaitBlock = 0
    LockWaitSkip = auto()
    LockWaitError = auto()
