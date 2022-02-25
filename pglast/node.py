# -*- coding: utf-8 -*-
# :Project:   pglast -- Generic Node implementation
# :Created:   mer 02 ago 2017 15:44:14 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2022 Lele Gaifax
#

from collections import namedtuple
from decimal import Decimal
from enum import Enum

from . import ast


class Missing:
    def __bool__(self):
        return False

    def __repr__(self):  # pragma: no cover
        return "MISSING"

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration()


Missing = Missing()
"Singleton returned when trying to get a non-existing attribute out of a :class:`Node`."


Comment = namedtuple('Comment', ('location', 'text', 'at_start_of_line', 'continue_previous'))
"A structure to carry information about a single SQL comment."


class Base:
    """Common base class.

    :param details: the *parse tree*
    :type parent: ``None`` or :class:`Node` instance
    :param parent: ``None`` to indicate that the node is the *root* of the parse tree,
                   otherwise it is the immediate parent of the new node
    :type name: str or tuple
    :param name: the name of the attribute in the `parent` node that *points* to this one;
                 it may be a tuple (name, position) when ``parent[name]`` is actually a list of
                 nodes

    Its main purpose is to create the right kind of instance, depending on the type of the
    `details` argument passed to the constructor: a :class:`ast.Node <pglast.ast.Node>`
    produces a :class:`Node` instance, a ``list`` or ``tuple`` produces a :class:`List`
    instance, everything else a :class:`Scalar` instance.

    """

    __slots__ = ('_parent_node', '_parent_attribute')

    def __new__(cls, details, parent=None, name=None):
        if parent is not None and not isinstance(parent, Node):
            raise ValueError("Unexpected value for 'parent', must be either None"
                             " or a Node instance, got %r" % type(parent))
        if name is not None and not isinstance(name, (str, tuple)):
            raise ValueError("Unexpected value for 'name', must be either None,"
                             " a string or a tuple, got %r" % type(name))
        if isinstance(details, (list, tuple)):
            self = super().__new__(List)
        elif isinstance(details, ast.Node):
            self = super().__new__(Node)
        else:
            self = super().__new__(Scalar)
        self._init(details, parent, name)
        return self

    def _init(self, parent, name):
        self._parent_node = parent
        self._parent_attribute = name

    def __str__(self):  # pragma: no cover
        aname = self._parent_attribute
        if isinstance(aname, tuple):
            aname = '%s[%d]' % aname
        return '%s=%r' % (aname, self)

    @property
    def parent_node(self):
        "The parent :class:`Node` of this element."

        return self._parent_node

    @property
    def parent_attribute(self):
        "The *attribute* in the parent :class:`Node` referencing this element."

        return self._parent_attribute


class List(Base):
    """Represent a sequence of :class:`Node` instances.

    :type items: list
    :param items: a list of items, usually :class:`Node` instances
    :type parent: ``None`` or :class:`Node` instance
    :param parent: ``None`` to indicate that the node is the *root* of the parse tree,
                   otherwise it is the immediate parent of the new node
    :type name: str or tuple
    :param name: the name of the attribute in the `parent` node that *points* to this one;
                 it may be a tuple (name, position) when ``parent[name]`` is actually a list of
                 nodes
    """

    __slots__ = ('_items',)

    def _init(self, items, parent, name):
        if not isinstance(items, (list, tuple)) or not items:  # pragma: no cover
            raise ValueError("Unexpected value for 'items', must be a non empty tuple or list,"
                             " got %r" % type(items))
        super()._init(parent, name)
        self._items = items

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return len(self) > 0

    def __repr__(self):
        if not self:  # pragma: no cover
            return '[]'
        # There's no guarantee that a list contains the same kind of objects,
        # so picking the first is rather arbitrary but serves the purpose, as
        # this is primarily an helper for investigating the internals of a tree.
        count = len(self)
        pivot = self[0]
        return '[%d*%r]' % (count, pivot)

    def __iter__(self):
        pnode = self.parent_node
        aname = self.parent_attribute
        for idx, item in enumerate(self._items):
            yield Base(item, pnode, (aname, idx))

    def __getitem__(self, index):
        return Base(self._items[index], self.parent_node, (self.parent_attribute, index))

    def __eq__(self, other):
        cls = type(self)
        if cls is type(other):
            return self._items == other._items
        return False

    @property
    def string_value(self):
        if len(self) != 1:  # pragma: no cover
            raise TypeError('%r does not contain a single String node' % self)
        node = self[0]
        if node.node_tag != 'String':  # pragma: no cover
            raise TypeError('%r does not contain a single String node' % self)
        return node.val.value

    def traverse(self):
        "A generator that recursively traverse all the items in the list."

        for item in self:
            yield from item.traverse()


class Node(Base):
    """Represent a single entry in a *parse tree*.

    :type details: :class:`.ast.Node`
    :param details: the *parse tree* of the node
    :type parent: ``None`` or :class:`Node` instance
    :param parent: ``None`` to indicate that the node is the *root* of the parse tree,
                   otherwise it is the immediate parent of the new node
    :type name: str or tuple
    :param name: the name of the attribute in the `parent` node that *points* to this one;
                 it may be a tuple (name, position) when ``parent[name]`` is actually a list of
                 nodes
    """

    __slots__ = ('node_tag', 'ast_node')

    def _init(self, details, parent=None, name=None):
        if not isinstance(details, ast.Node):  # pragma: no cover
            raise ValueError("Unexpected value for 'details', must be a ast.Node")
        super()._init(parent, name)
        self.node_tag = details.__class__.__name__
        self.ast_node = details

    def __getattr__(self, attr):
        value = getattr(self.ast_node, attr)
        if value is None:
            return Missing
        else:
            return Base(value, self, attr)

    def __repr__(self):
        return '{%s}' % self.node_tag

    def __getitem__(self, attr):
        if isinstance(attr, tuple):  # pragma: no cover
            attr, index = attr
            return self[attr][index]
        elif isinstance(attr, str):
            return getattr(self, attr)
        else:
            raise ValueError('Wrong key type %r, must be str or tuple'
                             % type(attr).__name__)

    def __iter__(self):
        node = self.ast_node
        for attr in sorted(node.__slots__):
            value = getattr(node, attr)
            if value is not None:
                yield Base(value, self, attr)

    def __eq__(self, other):
        cls = type(self)
        if cls is type(other):
            return self.ast_node == other.ast_node
        return False

    @property
    def attribute_names(self):
        "The names of the attributes present in the parse tree of the node."

        return tuple(self.ast_node)

    def traverse(self):
        "A generator that recursively traverse all attributes of the node."

        yield self
        for item in self:
            yield from item.traverse()


class Scalar(Base):
    "Represent a single scalar value."

    __slots__ = ('_value',)

    def _init(self, value, parent, name):
        if value is not None and not isinstance(value, (bool, float, int, str, Decimal,
                                                        ast.Value)):
            raise ValueError("Unexpected value for 'value', must be either None or a"
                             " bool|float|int|str|Decimal instance, got %r" % type(value))
        super()._init(parent, name)
        self._value = value

    def __and__(self, other):
        value = self._value
        if isinstance(value, int) and isinstance(other, int):
            return value & other
        else:  # pragma: no cover
            raise ValueError("Wrong operands for __and__: %r & %r"
                             % (type(value), type(other)))

    def __bool__(self):
        value = self._value
        if value is None:
            return False
        if isinstance(value, str):
            if len(value) == 0:
                return False
            elif len(value) == 1:
                return value[0] != '\x00'
            else:
                return True
        elif isinstance(value, bool):
            return value
        return True

    def __hash__(self):
        return hash(self._value)

    def __eq__(self, other):
        value = self._value
        if isinstance(other, Enum):
            return value == other
        elif isinstance(other, type(value)):
            return value == other
        else:
            cls = type(self)
            if cls is type(other):
                return value == other._value
        return False

    def __repr__(self):  # pragma: no cover
        if isinstance(self._value, Enum):
            return repr(self._value)
        else:
            return '<%r>' % self._value

    def traverse(self):
        yield self

    @property
    def value(self):
        return self._value
