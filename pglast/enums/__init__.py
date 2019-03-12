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
    GOUPING_SET_EMPTY = 0,
    GROUPING_SET_SIMPLE = auto()
    GROUPING_SET_ROLLUP = auto()
    GROUPING_SET_CUBE = auto()
    GROUPING_SET_SETS = auto()

