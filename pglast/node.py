# -*- coding: utf-8 -*-
# :Project:   pglast -- Generic Node implementation
# :Created:   mer 02 ago 2017 15:44:14 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018 Lele Gaifax
#

from enum import Enum


class Missing:
    def __bool__(self):
        return False

    def __repr__(self):
        return "MISSING"


NoneType = type(None)


Missing = Missing()
"Singleton returned when trying to get a non-existing attribute out of a :class:`Node`."


class Base:
    """Common base class.

    :type details: dict
    :param details: the *parse tree*
    :type parent: ``None`` or :class:`Node` instance
    :param parent: ``None`` to indicate that the node is the *root* of the parse tree,
                   otherwise it is the immediate parent of the new node
    :type name: str or tuple
    :param name: the name of the attribute in the `parent` node that *points* to this one;
                 it may be a tuple (name, position) when ``parent[name]`` is actually a list of
                 nodes

    Its main purpose is to create the right kind of instance, depending on the type of the
    `details` argument passed to the constructor: a ``dict`` produces a :class:`Node` instance,
    a ``list`` produces a :class:`List` instance, everything else a :class:`Scalar` instance.
    """

    __slots__ = ('_parent_node', '_parent_attribute')

    def __new__(cls, details, parent=None, name=None):
        if not isinstance(parent, (Node, NoneType)):
            raise ValueError("Unexpected value for 'parent', must be either None"
                             " or a Node instance, got %r" % type(parent))
        if not isinstance(name, (NoneType, str, tuple)):
            raise ValueError("Unexpected value for 'name', must be either None,"
                             " a string or a tuple, got %r" % type(name))
        if isinstance(details, list):
            self = super().__new__(List)
        elif isinstance(details, dict):
            self = super().__new__(Node)
        else:
            self = super().__new__(Scalar)
        self._init(details, parent, name)
        return self

    def _init(self, parent, name):
        self._parent_node = parent
        self._parent_attribute = name

    def __eq__(self, other):
        if type(self) is type(other):
            return all(getattr(self, slot) == getattr(other, slot) for slot in self.__slots__)
        return False

    def __str__(self):
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

    __slots__ = Base.__slots__ + ('_items',)

    def _init(self, items, parent, name):
        if not isinstance(items, list) or not items:
            raise ValueError("Unexpected value for 'items', must be a non empty"
                             " list, got %r" % type(items))
        super()._init(parent, name)
        self._items = items

    def __len__(self):
        return len(self._items)

    def __repr__(self):
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

    @property
    def string_value(self):
        if len(self) != 1:
            raise TypeError('%r does not contain a single String node' % self)
        node = self[0]
        if node.node_tag != 'String':
            raise TypeError('%r does not contain a single String node' % self)
        return node.str.value

    def traverse(self):
        "A generator that recursively traverse all the items in the list."

        for item in self:
            yield from item.traverse()


class Node(Base):
    """Represent a single entry in a *parse tree* returned by :func:`~.parser.parse_sql()`
    (or :func:`~.parser.parse_plpgsql()`).

    :type details: dict
    :param details: the *parse tree* of the node
    :type parent: ``None`` or :class:`Node` instance
    :param parent: ``None`` to indicate that the node is the *root* of the parse tree,
                   otherwise it is the immediate parent of the new node
    :type name: str or tuple
    :param name: the name of the attribute in the `parent` node that *points* to this one;
                 it may be a tuple (name, position) when ``parent[name]`` is actually a list of
                 nodes
    """

    __slots__ = Base.__slots__ + ('_node_tag', '_parse_tree')

    def _init(self, details, parent=None, name=None):
        if not isinstance(details, dict) or len(details) != 1:
            raise ValueError("Unexpected value for 'details', must be a dict with"
                             " exactly one key, got %r" % type(details))
        super()._init(parent, name)
        (self._node_tag, self._parse_tree), *_ = details.items()

    def __repr__(self):
        return '{%s}' % self._node_tag

    def __getattr__(self, attr):
        try:
            value = self._parse_tree[attr]
        except KeyError:
            return Missing
        else:
            return Base(value, self, attr)

    def __getitem__(self, attr):
        if isinstance(attr, tuple):
            attr, index = attr
            return self[attr][index]
        elif isinstance(attr, str):
            return getattr(self, attr)
        else:
            raise ValueError('Wrong key type %r, must be str or tuple'
                             % type(attr).__name__)

    def __iter__(self):
        value = self._parse_tree
        for attr in sorted(value.keys()):
            yield Base(value[attr], self, attr)

    @property
    def attribute_names(self):
        "The names of the attributes present in the parse tree of the node."

        value = self._parse_tree
        return value.keys()

    @property
    def node_tag(self):
        "The *tag* of the node."

        return self._node_tag

    @property
    def parse_tree(self):
        "The *parse tree* of the node."

        return self._parse_tree

    @property
    def string_value(self):
        if self.node_tag != 'String':
            raise TypeError('%r is not a String node' % self)
        return self.str.value

    def traverse(self):
        "A generator that recursively traverse all attributes of the node."

        yield self
        for item in self:
            yield from item.traverse()


class Scalar(Base):
    "Represent a single scalar value."

    __slots__ = Base.__slots__ + ('_value',)

    def _init(self, value, parent, name):
        if not isinstance(value, (NoneType, bool, float, int, str)):
            raise ValueError("Unexpected value for 'value', must be either None or a"
                             " bool|float|int|str instance, got %r" % type(value))
        super()._init(parent, name)
        self._value = value

    def __and__(self, other):
        if isinstance(self._value, int) and isinstance(other, int):
            return self._value & other
        else:
            raise ValueError("Wrong operands for __and__: %r & %r"
                             % (type(self._value), type(other)))

    def __bool__(self):
        if self.value is None:
            return False
        if isinstance(self.value, str):
            return bool(self.value)
        elif isinstance(self.value, bool):
            return self.value
        return True

    def __eq__(self, other):
        if isinstance(other, Enum):
            # Handle the FunctionParameterMode case, when the value is an integer while the
            # enum is actually a character
            if isinstance(self.value, int) and isinstance(other.value, str):
                assert len(other.value) == 1
                return self.value == ord(other.value)
            return self.value == other
        elif isinstance(other, type(self.value)):
            return self.value == other
        else:
            return super().__eq__(other)

    def __repr__(self):
        return '<%r>' % self._value

    def traverse(self):
        yield self

    @property
    def value(self):
        return self._value
