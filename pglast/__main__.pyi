# -*- coding: utf-8 -*-
# :Project:   pglast — Type stubs for pglast.__main__ module
# :License:   GNU General Public License version 3 or later
#

from argparse import Namespace
from collections.abc import Sequence

def workhorse(args: Namespace) -> None: ...
def main(options: Sequence[str] | None = None) -> None: ...
