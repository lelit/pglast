# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from pg_trigger.h @ 13-2.1.2-0-g4b30b03
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



# #define-ed constants

TRIGGER_TYPE_ROW = 1 << 0

TRIGGER_TYPE_BEFORE = 1 << 1

TRIGGER_TYPE_INSERT = 1 << 2

TRIGGER_TYPE_DELETE = 1 << 3

TRIGGER_TYPE_UPDATE = 1 << 4

TRIGGER_TYPE_TRUNCATE = 1 << 5

TRIGGER_TYPE_INSTEAD = 1 << 6

TRIGGER_TYPE_STATEMENT = 0

TRIGGER_TYPE_AFTER = 0
