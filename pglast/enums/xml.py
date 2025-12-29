# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: automatically extracted from xml.h @ 18-latest-dev-0-gb3b9523
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


class PgXmlStrictness(IntEnum):
    PG_XML_STRICTNESS_LEGACY = 0
    PG_XML_STRICTNESS_WELLFORMED = auto()
    PG_XML_STRICTNESS_ALL = auto()


class XmlBinaryType(IntEnum):
    XMLBINARY_BASE64 = 0
    XMLBINARY_HEX = auto()


class XmlStandaloneType(IntEnum):
    XML_STANDALONE_YES = 0
    XML_STANDALONE_NO = auto()
    XML_STANDALONE_NO_VALUE = auto()
    XML_STANDALONE_OMITTED = auto()
