# -*- coding: utf-8 -*-
# :Project:   pglast -- Printer functions for PG parse tree nodes
# :Created:   sab 05 ago 2017 16:33:14 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2020, 2021 Lele Gaifax
#

class IntEnumPrinter:
    "Helper class used to implement printers for specific enumerated values."

    enum = None
    "The enum class this is a printer for."

    def __init__(self):
        from enum import IntEnum

        assert issubclass(self.enum, IntEnum)
        assert len(set(m.value for m in self.enum)) == len(self.enum)
        self.value_to_symbol = {m.value: m.name for m in self.enum}

    def __call__(self, value, node, output):
        from ..node import Missing, Scalar

        if value is Missing:
            for symbol, member in self.enum.__members__.items():
                if member.value == 0:
                    break
            else:
                raise ValueError(f"Could not determine default value of class {self.enum!r}")
        elif isinstance(value, Scalar):
            if isinstance(value.value, str):
                # libpg_query 13+ emits enum names, not values
                symbol = value.value
                assert symbol in self.enum.__members__
            else:
                symbol = self.value_to_symbol.get(value.value)
        else:
            symbol = value
        if symbol is None:  # pragma: nocover
            raise ValueError(f"Invalid value {value!r}, not in class {self.enum!r}")
        method = getattr(self, symbol, None)
        if method is None:  # pragma: nocover
            raise NotImplementedError(f"Printer for {symbol!r} of {self.enum!r} not"
                                      f" implemented yet")
        method(node, output)


from . import ddl, dml, sfuncs
