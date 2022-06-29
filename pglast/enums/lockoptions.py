# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from lockoptions.h @ 13-2.1.2-0-g4b30b03
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2022 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:
    # Python < 3.10
    class StrEnum(str, Enum):
        pass


class LockClauseStrength(IntEnum):
    LCS_NONE = 0
    LCS_FORKEYSHARE = auto()
    LCS_FORSHARE = auto()
    LCS_FORNOKEYUPDATE = auto()
    LCS_FORUPDATE = auto()

class LockTupleMode(IntEnum):
    LockTupleKeyShare = 0
    LockTupleShare = auto()
    LockTupleNoKeyExclusive = auto()
    LockTupleExclusive = auto()

class LockWaitPolicy(IntEnum):
    LockWaitBlock = 0
    LockWaitSkip = auto()
    LockWaitError = auto()
