# -*- coding: utf-8 -*-
# :Project:   pglast -- Visitors base machinery
# :Created:   dom 9 mag 2021, 16:15:05
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021 Lele Gaifax
#

from collections import deque
from inspect import getmembers, ismethod

from . import ast


class ActionMeta(type):
    "Metaclass used to implement action singleton."

    def __repr__(cls):
        return cls.__name__


class Action(metaclass=ActionMeta):
    "Abstract action singleton."

    def __new__(cls):  # pragma: no cover
        return cls


class Add(Action):
    "Marker used to tell the iterator to insert nodes in the current sequence."


class Continue(Action):
    "Marker used to tell the iterator to keep going."


class Delete(Action):
    "Marker used to tell the iterator to delete current node."


class Skip(Action):
    "Marker used to tell the iterator to not descend into the current node."


class Ancestor:
    """Simple object to keep track of the node's ancestors while it's being visited.

    An instance of this class represent a particular ancestor in the hierarchy chain: it
    carries a reference that points to the higher item in the chain, the associated
    :class:`.ast.Node` instance and a *member*, either the attribute name or sequential index
    in the parent node.

    Iteration yields the sequence of involved *members*, that is the path starting from the
    root of the AST tree that leads to leaf node.

    Accessing an instance with a positive index returns the nth node up in the hierarchy.

    When applied (using the ``@`` operator) to an :class:`.ast.Node` instance will traverse
    that node returning the leaf one corresponding to the whole chain.

    Example:

    .. testsetup:: *

        from pglast import parse_sql
        from pglast.visitors import Ancestor

    .. doctest::

        >>> tree = parse_sql('select 1')
        >>> root = Ancestor()
        >>> root
        ROOT
        >>> root@tree is tree
        True
        >>> root[0] is None
        True
        >>> select_stmt_path = root / (root, 0) / (tree[0], 'stmt')
        >>> select_stmt_path
        ROOT → 0 → stmt
        >>> select_stmt_path@tree is tree[0].stmt
        True
        >>> select_stmt_path[0] is tree[0]
        True
        >>> columns_path = select_stmt_path / (tree[0].stmt, 'targetList')
        >>> first_col_path = columns_path / (tree[0].stmt.targetList[0], 0)
        >>> first_col_path
        ROOT → 0 → stmt → targetList → 0
        >>> first_col_path[0]
        <ResTarget val=<A_Const val=<Integer val=1>>>
        >>> first_col_path[1] is columns_path[0]
        True
    """

    def __init__(self, parent=None, node=None, member=None):
        self.parent = parent
        self.node = node
        self.member = member

    def __iter__(self):
        "Iterate over each step, yielding either an attribute name or a sequence index."

        ancestors = []

        path = self
        while True:
            ancestors.append(path.member)
            if path.parent is None:
                return reversed(ancestors)
            path = path.parent

    def __repr__(self):
        return ' → '.join('ROOT' if m is None else str(m) for m in self)

    def __getitem__(self, n):
        path = self
        while n > 0:
            path = path.parent
            n -= 1
        return path.node

    def __truediv__(self, node_and_member):
        "Create a new instance pointing to the given child node."

        return Ancestor(self, *node_and_member)

    def __matmul__(self, root):
        "Resolve the ancestry chain against the given `root` node, returning the leaf node."

        node = root
        for member in self:
            if member is not None:
                if isinstance(member, int):
                    node = node[member]
                else:
                    node = getattr(node, member)
        return node


def visitable(node):
    "Determine whether the given `node` is visitable or not."

    return (isinstance(node, ast.Node)
            or (isinstance(node, tuple) and all(isinstance(item, ast.Node) for item in node)))


class Visitor:
    """Base class implementing the `visitor pattern`__.

    __ https://en.wikipedia.org/wiki/Visitor_pattern

    To use it, you shall write a subclass that implements a set of particular named methods,
    specifically ``visit_XYZ`` where ``XYZ`` is the name of a class name defined in the
    :mod:`pglast.ast` module.

    Instances of this class are *callables* and accept either a :class:`pglast.ast.Node`
    instance or a sequence of instances, typically the result of :func:`parse_sql
    <pglast.parser.parse_sql>`. The argument will be *traversed* in a `breadth first`__ order
    and each :class:`Node <.ast.Node>` instance will be passed to the corresponding
    ``visit_XYZ`` method if it is implemented, falling back to the default ``visit`` method. If
    none of them are defined, the node will be ignored.

    The ``visit_XYZ`` methods receive two arguments: the *ancestry chain* of the node, an
    instance of :class:`Ancestor` and the :class:`Node <.ast.Node>` instance itself. The
    methods may return either ``None``, an *action* or a new node that will replace the
    original one.

    __ https://en.wikipedia.org/wiki/Breadth-first_search
    """

    def __call__(self, root):
        "Iteratively visit the `root` node calling related ``visit_XYZ`` methods."

        self.root = root

        by_ast_class = {}
        for name, method in getmembers(self, ismethod):
            if not name.startswith('visit_'):
                continue

            clsname = name[6:]
            cls = getattr(ast, clsname, None)
            if cls is not None:
                by_ast_class[cls] = method

        default_method = self.visit

        generator = self.iterate(root)
        try:
            ancestors, node = generator.send(None)
        except StopIteration:
            return

        while True:
            method = by_ast_class.get(node.__class__, default_method)
            if method is not None:
                result = method(ancestors, node)
            else:
                result = None
            try:
                ancestors, node = generator.send(Continue if result is None else result)
            except StopIteration:
                break

        return self.root

    def iterate(self, node):
        """Iterate thru `node`'s AST using a breadth-first traversing.

        :param node: either a :class:`Node <pglast.ast.Node>` instance or a tuple of those

        This is a generator, that yields ``Node`` instances together with their *ancestors
        chain* as it finds them while traversing the tree.
        """

        todo = deque()

        if visitable(node):
            todo.append((Ancestor(), node))
        else:
            raise ValueError('Bad argument, expected a ast.Node instance or a tuple')

        while todo:
            ancestors, node = todo.popleft()

            is_sequence = isinstance(node, tuple)
            if is_sequence:
                nodes = list(node)
                new_nodes = []
            else:
                nodes = [node]
                new_nodes = None
            sequence_changed = False

            index = 0
            while nodes:
                snode = nodes.pop(0)
                if is_sequence:
                    sancestors = ancestors / (node, index)
                else:
                    sancestors = ancestors
                action = yield sancestors, snode
                if action is Continue:
                    if is_sequence:
                        new_nodes.append(snode)

                    for attr in snode:
                        value = getattr(snode, attr)
                        if visitable(value):
                            todo.append((sancestors / (snode, attr), value))
                elif action is Skip:
                    if is_sequence:
                        new_nodes.append(snode)
                else:
                    if action is Delete:
                        if is_sequence:
                            sequence_changed = True
                        new_node = None
                    elif action is not snode:
                        if is_sequence:
                            sequence_changed = True
                            new_nodes.append(action)
                        else:
                            new_node = action

                    if not is_sequence:
                        parent = ancestors[0]
                        if parent is not None:
                            setattr(parent, ancestors.member, new_node)
                        else:
                            self.root = new_node
                index += 1

            if is_sequence and sequence_changed:
                parent = ancestors[0]
                if parent is not None:
                    setattr(parent, ancestors.member, tuple(new_nodes) if new_nodes else None)
                else:
                    self.root = tuple(new_nodes) if new_nodes else None

    visit = None
    """
    The default *visit* method for any node without a specific one.
    When ``None``, nothing happens.
    """


class RelationNames(Visitor):
    """Concrete implementation of the :func:`.referenced_relations` function.

    Calling an instance of this class will return a set of the names of the
    relations referenced by the given :class:`node <pglast.ast.Node>`.
    """

    def __call__(self, node):
        self.ctenames = set()
        self.rnames = set()
        super().__call__(node)
        return self.rnames - self.ctenames

    def visit_CommonTableExpr(self, ancestors, node):
        "Collect CTE names."

        self.ctenames.add(node.ctename)

    def visit_DropStmt(self, ancestors, node):
        from .enums import ObjectType
        if node.removeType in (ObjectType.OBJECT_TABLE, ObjectType.OBJECT_VIEW):
            for obj in node.objects:
                self.rnames.add('.'.join(n.val for n in obj))

    def visit_RangeVar(self, ancestors, node):
        "Collect relation names."

        tname = node.relname

        if node.schemaname:
            tname = f'{node.schemaname}.{tname}'

        if node.catalogname:
            tname = f'{node.catalogname}.{tname}'

        self.rnames.add(tname)


def referenced_relations(stmt):
    """Return the set of relation names referenced in the given `stmt`.

    :param stmt: either a string containing the ``SQL`` statement or a :class:`.ast.Node`
                 instance
    :returns: a set of strings, the names of the relations

    Example:

    .. code-block:: Python

       assert referenced_relations('WITH q1(x,y) AS (SELECT 1,2)'
                                   ' SELECT * FROM q1, q2') == {'q2'}
    """

    from .parser import parse_sql

    return RelationNames()(parse_sql(stmt) if isinstance(stmt, str) else stmt)
