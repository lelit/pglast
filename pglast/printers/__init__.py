# -*- coding: utf-8 -*-
# :Project:   pglast -- Printer functions for PG parse tree nodes
# :Created:   sab 05 ago 2017 16:33:14 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2020, 2021, 2022 Lele Gaifax
#

from .. import ast
from ..error import Error


NODE_PRINTERS = {}
"Registry of specialized node printers, keyed by their class."


SPECIAL_FUNCTIONS = {}
"Registry of specialized function printers, keyed by their qualified name."


class PrinterAlreadyPresentError(Error):
    "Exception raised trying to register another function for a tag already present."


def get_printer_for_node(node):
    """Get specific printer implementation for given `node`.

    If there is a more specific printer for it, when it's inside a particular
    ancestor, return that instead.
    """

    node_class = type(node)
    if not issubclass(node_class, ast.Node):
        raise ValueError('Expected an ast.Node, not a %r' % node_class.__name__)
    parent = abs(node.ancestors)
    parent_node_class = None if parent is None else type(parent.node)
    printer = NODE_PRINTERS.get((parent_node_class, node_class))
    if printer is None:
        printer = NODE_PRINTERS.get(node_class)
        if printer is None:
            raise NotImplementedError("Printer for node %r is not implemented yet"
                                      % node_class.__name__)
    return printer


def node_printer(*nodes, override=False):
    r"""Decorator to register a specific printer implementation for a (set of) `nodes`.

    :param \*nodes: a list of one or two items
    :param bool override:
           when ``True`` the function will be registered even if already present in the
           :data:`NODE_PRINTERS` registry

    When `nodes` contains a single item then the decorated function is the *generic*
    one, and it will be registered in :data:`NODE_PRINTERS` with that key alone. Otherwise it
    must contain two elements: the first may be either a scalar value or a sequence of parent
    nodes, and the function will be registered under the key ``(parent, node)``.
    """

    n = len(nodes)
    if n == 1:
        parent_classes = (None,)
        node_class = nodes[0]
    elif n == 2:
        parent_classes, node_class = nodes
        if not isinstance(parent_classes, (list, tuple)):
            parent_classes = (parent_classes,)
        if not all(isinstance(c, type) and issubclass(c, ast.Node) for c in parent_classes):
            raise ValueError('Invalid nodes: expected a sequence of ast.Node classes as'
                             '  parents, got %r' % (parent_classes,))
    else:
        raise ValueError('Invalid nodes: must contain one or two items!')

    if not isinstance(node_class, type) or not issubclass(node_class, ast.Node):
        raise ValueError('Invalid nodes: expected an ast.Node class,'
                         ' got %r' % node_class)

    def decorator(impl):
        for parent_class in parent_classes:
            key = node_class if parent_class is None else (parent_class, node_class)
            if not override and key in NODE_PRINTERS:  # pragma: no cover
                raise PrinterAlreadyPresentError("A printer is already registered for tag %r"
                                                 % key)
            NODE_PRINTERS[key] = impl
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
        if value is None:
            # Should never happen, but better safe than sorry
            for symbol, member in self.enum.__members__.items():
                if member.value == 0:
                    break
            else:  # pragma: no cover
                raise ValueError(f"Could not determine default value of class {self.enum!r}")
        elif isinstance(value, self.enum):
            symbol = self.value_to_symbol.get(value)
        elif isinstance(value, ast.Integer):
            symbol = self.value_to_symbol.get(value.ival)
        else:
            symbol = value
        if symbol is None:  # pragma: no cover
            raise ValueError(f"Invalid value {value!r}, not in class {self.enum!r}")
        method = getattr(self, symbol, None)
        if method is None:
            if symbol in self.enum.__members__:
                raise NotImplementedError(f"Printer for {symbol!r} of {self.enum!r} not"
                                          f" implemented yet")
            else:
                raise ValueError(f"Invalid symbol {symbol!r}, not in class {self.enum!r}")

        method(node, output)


def get_string_value(lst):
    "Helper function to get a literal string value, wrapped in a one-sized list."

    if len(lst) != 1 or not isinstance(lst[0], ast.String):  # pragma: no cover
        raise TypeError('%r does not contain a single String node' % lst)
    return lst[0].sval


from . import ddl, dml, sfuncs  # noqa: F401,E402
