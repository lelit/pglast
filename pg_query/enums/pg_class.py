# -*- coding: utf-8 -*-
# :Project:   pg_query -- DO NOT EDIT: automatically extracted from pg_class.h @ 10-latest-0-g43ce2e8
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

try:
    from enum import Enum, IntEnum, IntFlag, auto
except ImportError: #pragma: no cover
    # Python < 3.6
    from aenum import Enum, IntEnum, IntFlag, auto



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

RELPERSISTENCE_PERMANENT = 'p'

RELPERSISTENCE_UNLOGGED = 'u'

RELPERSISTENCE_TEMP = 't'

REPLICA_IDENTITY_DEFAULT = 'd'

REPLICA_IDENTITY_NOTHING = 'n'

REPLICA_IDENTITY_FULL = 'f'

REPLICA_IDENTITY_INDEX = 'i'
