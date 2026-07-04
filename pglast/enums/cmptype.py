# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: automatically extracted from cmptype.h @ 18-latest-0-g6ced8d4
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2026 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:  # pragma: no cover
    # Python < 3.11
    class StrEnum(str, Enum):
        pass


class CompareType(IntEnum):
    COMPARE_INVALID = 0
    COMPARE_LT = 1
    COMPARE_LE = 2
    COMPARE_EQ = 3
    COMPARE_GE = 4
    COMPARE_GT = 5
    COMPARE_NE = 6
    COMPARE_OVERLAP = auto()
    COMPARE_CONTAINED_BY = auto()
