# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from pg_class.h @ 10-1.0.2-0-gd710cb0
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

RelationRelationId = 1259

RelationRelation_Rowtype_Id = 83

Natts_pg_class = 33

Anum_pg_class_relname = 1

Anum_pg_class_relnamespace = 2

Anum_pg_class_reltype = 3

Anum_pg_class_reloftype = 4

Anum_pg_class_relowner = 5

Anum_pg_class_relam = 6

Anum_pg_class_relfilenode = 7

Anum_pg_class_reltablespace = 8

Anum_pg_class_relpages = 9

Anum_pg_class_reltuples = 10

Anum_pg_class_relallvisible = 11

Anum_pg_class_reltoastrelid = 12

Anum_pg_class_relhasindex = 13

Anum_pg_class_relisshared = 14

Anum_pg_class_relpersistence = 15

Anum_pg_class_relkind = 16

Anum_pg_class_relnatts = 17

Anum_pg_class_relchecks = 18

Anum_pg_class_relhasoids = 19

Anum_pg_class_relhaspkey = 20

Anum_pg_class_relhasrules = 21

Anum_pg_class_relhastriggers = 22

Anum_pg_class_relhassubclass = 23

Anum_pg_class_relrowsecurity = 24

Anum_pg_class_relforcerowsecurity = 25

Anum_pg_class_relispopulated = 26

Anum_pg_class_relreplident = 27

Anum_pg_class_relispartition = 28

Anum_pg_class_relfrozenxid = 29

Anum_pg_class_relminmxid = 30

Anum_pg_class_relacl = 31

Anum_pg_class_reloptions = 32

Anum_pg_class_relpartbound = 33

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
