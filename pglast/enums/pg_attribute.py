# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from pg_attribute.h @ 13-2.1.2-0-g4b30b03
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

ATTRIBUTE_IDENTITY_ALWAYS = 'a'

ATTRIBUTE_IDENTITY_BY_DEFAULT = 'd'

ATTRIBUTE_GENERATED_STORED = 's'
