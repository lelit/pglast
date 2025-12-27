# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: automatically extracted from cmptype.h @ 18-latest-dev-0-g8e5b04b
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2025 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, StrEnum, auto


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
