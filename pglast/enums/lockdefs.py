# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: automatically extracted from lockdefs.h @ 18-latest-dev-0-g8e5b04b
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2025 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, StrEnum, auto


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

MaxLockMode = 8
