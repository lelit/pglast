# -*- coding: utf-8 -*-
# :Project:   pglast -- Printer functions for PG parse tree nodes
# :Created:   sab 05 ago 2017 16:33:14 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2020 Lele Gaifax
#

class IntEnumPrinter:
    "Helper class used to implement printers for specific enumerated values."

    def __init__(self, enum=None):
        assert len(set(m.value for m in enum)) == len(enum)
        self.enum = enum
        self.value_to_symbol = {m.value: m.name for m in enum}

    def __getitem__(self, value):
        from ..node import Scalar

        symbol = self.value_to_symbol.get(value.value if isinstance(value, Scalar) else value)
        if symbol is None:  # pragma: nocover
            raise ValueError(f"Invalid value {value!r}, not in class {self.enum!r}")
        method = getattr(self, symbol, None)
        if method is None:  # pragma: nocover
            raise NotImplementedError(f"Printer for {symbol!r} of {self.enum!r} not"
                                      f" implemented yet")
        return method


from . import ddl, dml, sfuncs
