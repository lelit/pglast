# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from lockdefs.h @ 10-1.0.2-0-gd710cb0
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2019 Lele Gaifax
#

try:
    from enum import Enum, IntEnum, IntFlag, auto
except ImportError: #pragma: no cover
    # Python < 3.6
    from aenum import Enum, IntEnum, IntFlag, auto



# #define-ed constants

NoLock = 0

AccessShareLock = 1

RowShareLock = 2

RowExclusiveLock = 3

ShareUpdateExclusiveLock = 4

ShareLock = 5

ShareRowExclusiveLock = 6

ExclusiveLock = 7

AccessExclusiveLock = 8
