# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from pg_class.h @ 13-2.1.2-0-g4b30b03
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

RELKIND_RELATION = 'r'

RELKIND_INDEX = 'i'

RELKIND_SEQUENCE = 'S'

RELKIND_TOASTVALUE = 't'

RELKIND_VIEW = 'v'

RELKIND_MATVIEW = 'm'

RELKIND_COMPOSITE_TYPE = 'c'

RELKIND_FOREIGN_TABLE = 'f'

RELKIND_PARTITIONED_TABLE = 'p'

RELKIND_PARTITIONED_INDEX = 'I'

RELPERSISTENCE_PERMANENT = 'p'

RELPERSISTENCE_UNLOGGED = 'u'

RELPERSISTENCE_TEMP = 't'

REPLICA_IDENTITY_DEFAULT = 'd'

REPLICA_IDENTITY_NOTHING = 'n'

REPLICA_IDENTITY_FULL = 'f'

REPLICA_IDENTITY_INDEX = 'i'
