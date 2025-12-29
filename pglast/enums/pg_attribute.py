# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: automatically extracted from pg_attribute.h @ 18-latest-dev-0-gb3b9523
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2025 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:  # pragma: no cover
    # Python < 3.11
    class StrEnum(str, Enum):


# #define-ed constants

ATTRIBUTE_IDENTITY_ALWAYS = 'a'

ATTRIBUTE_IDENTITY_BY_DEFAULT = 'd'

ATTRIBUTE_GENERATED_STORED = 's'

ATTRIBUTE_GENERATED_VIRTUAL = 'v'
