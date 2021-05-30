# -*- coding: utf-8 -*-
# :Project:   pglast -- Printer functions for PG parse tree nodes
# :Created:   sab 05 ago 2017 16:33:14 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2020, 2021 Lele Gaifax
#

from .. import ast
from ..error import Error


NODE_PRINTERS = {}
"Registry of specialized printers, keyed by their `tag`."


SPECIAL_FUNCTIONS = {}
"Registry of specialized function printers, keyed by their qualified name."


class PrinterAlreadyPresentError(Error):
    "Exception raised trying to register another function for a tag already present."


def get_printer_for_node_tag(parent_node_tag, node_tag):
    """Get specific printer implementation for given `node_tag`.

    If there is a more specific printer for it, when it's inside a particular
    `parent_node_tag`, return that instead.
    """

    printer = NODE_PRINTERS.get((parent_node_tag, node_tag))
    if printer is None:
        printer = NODE_PRINTERS.get(node_tag)
        if printer is None:
            raise NotImplementedError("Printer for node %r is not implemented yet"
                                      % node_tag)
    return printer


def node_printer(*node_tags, override=False, check_tags=True):
    r"""Decorator to register a specific printer implementation for given `node_tag`.

    :param \*node_tags: one or two node tags
    :param bool override:
           when ``True`` the function will be registered even if already present in the
           :data:`NODE_PRINTERS` registry
    :param bool check_tags:
           by default each `node_tags` is checked for validity, that is must be a valid class
           implemented by :mod:`pglast.ast`; pass ``False`` to disable the check

    When `node_tags` contains a single item then the decorated function is the *generic* one,
    and it will be registered in :data:`NODE_PRINTERS` with that key alone. Otherwise it must
    contain two elements: the first may be either a scalar value or a sequence of parent tags,
    and the function will be registered under the key ``(parent_tag, tag)``.
    """

    if check_tags:
        for tag in node_tags:
            if not isinstance(tag, (list, tuple)):
                tag = (tag,)
            for t in tag:
                if not isinstance(t, str):
                    raise ValueError(f'Invalid tag {t!r}, expected a string')
                if not hasattr(ast, t):
                    raise ValueError(f'Unknown tag name {t}')

    def decorator(impl):
        if len(node_tags) == 1:
            parent_tags = (None,)
            tag = node_tags[0]
        elif len(node_tags) == 2:
            parent_tags, tag = node_tags
            if not isinstance(parent_tags, (list, tuple)):
                parent_tags = (parent_tags,)
        else:
            raise ValueError(f'Must specify one or two tags, got {len(node_tags)} instead')

        for parent_tag in parent_tags:
            t = tag if parent_tag is None else (parent_tag, tag)
            if not override and t in NODE_PRINTERS:
                raise PrinterAlreadyPresentError("A printer is already registered for tag %r"
                                                 % t)
            NODE_PRINTERS[t] = impl
        return impl
    return decorator


def special_function(name, override=False):
    """Decorator to declare a particular PostgreSQL function `name` as *special*, with a
    specific printer.

    :param str name: the qualified name of the PG function
    :param bool override: when ``True`` the function will be registered even if already
                          present in the :data:`SPECIAL_FUNCTIONS` registry
    """

    def decorator(impl):
        if not override and name in SPECIAL_FUNCTIONS:
            raise PrinterAlreadyPresentError("A printer is already registered for function %r"
                                             % name)
        SPECIAL_FUNCTIONS[name] = impl
        return impl
    return decorator


get_special_function = SPECIAL_FUNCTIONS.get


class IntEnumPrinter:
    "Helper class used to implement printers for specific enumerated values."

    enum = None
    "The enum class this is a printer for."

    def __init__(self):
        from enum import IntEnum

        if not issubclass(self.enum, IntEnum):
            raise ValueError(f'Given enum {self.enum!r} is not an IntEnum subclass')
        if len(set(m.value for m in self.enum)) != len(self.enum):  # pragma: no cover
            raise ValueError(f'Given enum {self.enum!r} contains aliased symbols')
        self.value_to_symbol = {m.value: m.name for m in self.enum}

    def __call__(self, value, node, output):
        from ..node import Missing, Scalar

        if value is Missing:
            # Should never happen, but better safe than sorry
            for symbol, member in self.enum.__members__.items():
                if member.value == 0:
                    break
            else:  # pragma: no cover
                raise ValueError(f"Could not determine default value of class {self.enum!r}")
        elif isinstance(value, Scalar):
            if isinstance(value.value, str):
                # libpg_query 13+ emits enum names, not values
                symbol = value.value
                if symbol not in self.enum.__members__:
                    raise ValueError('Unexpected symbol {symbol!r}, not in {self.enum!r}')
            else:
                symbol = self.value_to_symbol.get(value.value)
        else:
            symbol = value
        if symbol is None:
            raise ValueError(f"Invalid value {value!r}, not in class {self.enum!r}")
        method = getattr(self, symbol, None)
        if method is None:
            if symbol in self.enum.__members__:
                raise NotImplementedError(f"Printer for {symbol!r} of {self.enum!r} not"
                                          f" implemented yet")
            else:
                raise ValueError(f"Invalid symbol {symbol!r}, not in class {self.enum!r}")

        method(node, output)


from . import ddl, dml, sfuncs  # noqa: F401,E402
