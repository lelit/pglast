# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from pg_trigger.h @ 10-1.0.2-0-gd710cb0
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

TriggerRelationId = 2620

Natts_pg_trigger = 17

Anum_pg_trigger_tgrelid = 1

Anum_pg_trigger_tgname = 2

Anum_pg_trigger_tgfoid = 3

Anum_pg_trigger_tgtype = 4

Anum_pg_trigger_tgenabled = 5

Anum_pg_trigger_tgisinternal = 6

Anum_pg_trigger_tgconstrrelid = 7

Anum_pg_trigger_tgconstrindid = 8

Anum_pg_trigger_tgconstraint = 9

Anum_pg_trigger_tgdeferrable = 10

Anum_pg_trigger_tginitdeferred = 11

Anum_pg_trigger_tgnargs = 12

Anum_pg_trigger_tgattr = 13

Anum_pg_trigger_tgargs = 14

Anum_pg_trigger_tgqual = 15

Anum_pg_trigger_tgoldtable = 16

Anum_pg_trigger_tgnewtable = 17

TRIGGER_TYPE_ROW = 1 << 0

TRIGGER_TYPE_BEFORE = 1 << 1

TRIGGER_TYPE_INSERT = 1 << 2

TRIGGER_TYPE_DELETE = 1 << 3

TRIGGER_TYPE_UPDATE = 1 << 4

TRIGGER_TYPE_TRUNCATE = 1 << 5

TRIGGER_TYPE_INSTEAD = 1 << 6

TRIGGER_TYPE_STATEMENT = 0

TRIGGER_TYPE_AFTER = 0
