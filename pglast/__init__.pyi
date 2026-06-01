# -*- coding: utf-8 -*-
# :Project:   pglast — Type stubs for pglast package
# :License:   GNU General Public License version 3 or later
#

from typing import Any, NamedTuple

from . import enums as enums
from .error import Error as Error
from .parser import fingerprint as fingerprint
from .parser import get_postgresql_version as get_postgresql_version
from .parser import parse_sql as parse_sql
from .parser import scan as scan
from .parser import split as split

__version__: str
__author__: str
__all__: tuple[str, ...]

class Comment(NamedTuple):
    location: int
    text: str
    at_start_of_line: bool
    continue_previous: bool

def parse_plpgsql(statement: str) -> list[dict[str, Any]]: ...
def _extract_comments(statement: str) -> list[Comment]: ...
def prettify(
    statement: str,
    safety_belt: bool = False,
    preserve_comments: bool = False,
    **options: Any,
) -> str: ...
