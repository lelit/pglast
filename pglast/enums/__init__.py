# -*- coding: utf-8 -*-
# :Project:   pglast -- Enums used by the nodes
# :Created:   gio 03 ago 2017 17:08:26 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018 Lele Gaifax
#

from .lockoptions import *  # noqa
from .pg_class import *     # noqa

from .primnodes import *    # noqa
from .nodes import *        # noqa
from .parsenodes import *   # noqa


class GroupingSetKind(IntEnum):
    GOUPING_SET_EMPTY = 0
    GROUPING_SET_SIMPLE = auto()
    GROUPING_SET_ROLLUP = auto()
    GROUPING_SET_CUBE = auto()
    GROUPING_SET_SETS = auto()


class LockMode(IntEnum):
    LM_NoLock = 0
    LM_AccessShareLock = auto()
    LM_RowShareLock = auto()
    LM_RowExclusiveLock = auto()
    LM_ShareUpdateExclusiveLock = auto()
    LM_ShareLock = auto()
    LM_ShareRowExclusiveLock = auto()
    LM_ExclusiveLock = auto()
    LM_AccessExclusiveLock = auto()


class TriggerConstants(IntFlag):
    TRIGGER_TYPE_ROW = (1 << 0)
    TRIGGER_TYPE_BEFORE = (1 << 1)
    TRIGGER_TYPE_INSERT = (1 << 2)
    TRIGGER_TYPE_DELETE = (1 << 3)
    TRIGGER_TYPE_UPDATE = (1 << 4)
    TRIGGER_TYPE_TRUNCATE = (1 << 5)
    TRIGGER_TYPE_INSTEAD = (1 << 6)
