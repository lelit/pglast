# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from pg_am.h @ 14-3.0.0-0-g397cbb9
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2023 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:  # pragma: no cover
    # Python < 3.10
    class StrEnum(str, Enum):
        pass



# #define-ed constants

AmNameIndexId = 2651

AmOidIndexId = 2652

AMTYPE_INDEX = 'i'

AMTYPE_TABLE = 't'
