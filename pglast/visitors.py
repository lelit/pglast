# -*- coding: utf-8 -*-
# :Project:   pglast -- Visitors base machinery
# :Created:   dom 9 mag 2021, 16:15:05
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021, 2022 Lele Gaifax
#

from collections import deque
from inspect import getmembers, ismethod

from . import ast
from .stream import maybe_double_quote_name


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

    :param Ancestor parent: the parent of the new instance
    :param node: the tracked object
    :param member: either the name of the attribute or the index in the sequence
                   that points to the tracked object in the parent container

    An instance of this class represent a particular ancestor in the hierarchy chain: it
    carries a reference that points to the higher item in the chain, the associated
    :class:`.ast.Node` instance and a *member*, either the attribute name or sequential index
    in the parent node: the latter happens when the parent node is actually a tuple, not an
    ``Node`` instance.

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
        >>> columns_path = (select_stmt_path
        ...                 / (tree[0].stmt, 'targetList'))
        >>> first_col_path = (columns_path
        ...                   / (tree[0].stmt.targetList[0], 0))
        >>> first_col_path
        ROOT → 0 → stmt → targetList → 0
        >>> first_col_path[0]
        <ResTarget val=<A_Const val=<Integer val=1>>>
        >>> first_col_path[1] is columns_path[0]
        True

    As said, the `node` is not always a :class:`.ast.Node`, but may be a tuple, possibly
    containing *subtuples*, for example the ``functions`` slot of :class:`~.ast.RangeFunction`:

    .. doctest::

        >>> tree = parse_sql('SELECT * FROM ROWS'
        ...                  ' FROM(generate_series(10,11), get_users())')
        >>> root = Ancestor()
        >>> from_clause_path = (root / (root, 0) / (tree[0], 'stmt')
        ...                     / (tree[0].stmt, 'fromClause'))
        >>> from_clause = tree[0].stmt.fromClause
        >>> from_clause_path@tree is from_clause
        True
        >>> range_function_path = (from_clause_path
        ...                        / (from_clause, 0))
        >>> range_function = from_clause[0]
        >>> functions_path = (range_function_path
        ...                   / (range_function, 'functions'))
        >>> functions = from_clause[0].functions
        >>> functions_path@tree is functions
        True
        >>> generate_series_path = (functions_path
        ...                         / (functions, 0))
        >>> generate_series_path@tree is functions[0]
        True
        >>> type(generate_series_path.node)
        <class 'tuple'>
        >>> type(generate_series_path.member)
        <class 'int'>
        >>> type(generate_series_path.node[0])
        <class 'tuple'>
        >>> generate_series_path.node[0][0]
        <FuncCall funcname=(<String val='generate_series'>,)...
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

    def find_nearest(self, cls):
        "Find the nearest ancestor with a node of the given `cls`."

        path = self
        while True:
            if isinstance(path.node, cls):
                return path
            path = path.parent
            if path is None:
                break

    def __contains__(self, cls):
        "Tell whether there is a node of type `cls` in the anchestry."

        return self.find_nearest(cls) is not None

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


class Visitor:
    """Base class implementing the `visitor pattern`__.

    __ https://en.wikipedia.org/wiki/Visitor_pattern

    To use it, you shall write a subclass that implements a set of particular named methods,
    specifically ``visit_XYZ`` where ``XYZ`` is the name of a class name defined in the
    :mod:`pglast.ast` module.

    Instances of this class are *callables* and accept either a :class:`.ast.Node`
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

        :param node: either a :class:`.ast.Node` instance or a tuple of those

        This is a generator, that yields ``Node`` instances together with their *ancestors
        chain* as it finds them while traversing the tree.
        """

        todo = deque()

        if isinstance(node, (tuple, ast.Node)):
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
                sub_node = nodes.pop(0)
                if is_sequence:
                    sub_ancestors = ancestors / (node, index)
                else:
                    sub_ancestors = ancestors
                if isinstance(sub_node, ast.Node):
                    action = yield sub_ancestors, sub_node
                    if action is Continue:
                        if is_sequence:
                            new_nodes.append(sub_node)

                        for member in sub_node:
                            value = getattr(sub_node, member)
                            if isinstance(value, (tuple, ast.Node)):
                                todo.append((sub_ancestors / (sub_node, member), value))
                    elif action is Skip:
                        if is_sequence:
                            new_nodes.append(sub_node)
                    else:
                        if action is Delete:
                            if is_sequence:
                                sequence_changed = True
                            new_node = None
                        elif action is not sub_node:
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
                elif isinstance(sub_node, tuple):
                    for sub_index, value in enumerate(sub_node):
                        if isinstance(value, (tuple, ast.Node)):
                            todo.append((sub_ancestors / (sub_node, sub_index), value))

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


class ReferencedRelations(Visitor):
    """Concrete implementation of the :func:`.referenced_relations` function.

    :param set cte_names: the set of surrounding CTE names
    :param WithClause skip_with_clause: skip this clause, when specified

    Calling an instance of this class will return a set of the names of the
    relations referenced by the given :class:`node <pglast.ast.Node>`.
    """

    def __init__(self, cte_names=None, skip_with_clause=None):
        super().__init__()
        self.cte_names = set() if cte_names is None else cte_names.copy()
        self.skip_with_clause = skip_with_clause
        self.r_names = set()

    def __call__(self, node):
        super().__call__(node)
        return self.r_names

    def visit_DropStmt(self, ancestors, node):
        from .enums import ObjectType

        if node.removeType in (ObjectType.OBJECT_TABLE, ObjectType.OBJECT_VIEW):
            for obj in node.objects:
                self.r_names.add('.'.join(maybe_double_quote_name(n.val) for n in obj))

    def visit_SelectStmt(self, ancestors, node):
        if node.withClause and node.withClause is not self.skip_with_clause:
            # CTEs are tricky to get right, as issue #106 demonstrates!
            #
            # We must first collect the CTE names as well as the table referenced by their
            # queries, and then process the statement with that knowledge.
            #
            # In the normal case, each CTE must be processed in order, with the CTE names found
            # earlier; in the "WITH RECURSIVE" case all its CTEs must be considered valid at
            # the same time.
            with_clause = node.withClause
            if with_clause.recursive:
                self.cte_names.update(maybe_double_quote_name(cte.ctename)
                                      for cte in with_clause.ctes)
                self.r_names.update(ReferencedRelations(self.cte_names)(with_clause))
            else:
                for cte in with_clause.ctes:
                    cte_name = maybe_double_quote_name(cte.ctename)
                    self.r_names.update(ReferencedRelations(self.cte_names)(cte))
                    self.cte_names.add(cte_name)
            self.r_names.update(ReferencedRelations(self.cte_names, with_clause)(node))
            return Skip

    visit_UpdateStmt = visit_InsertStmt = visit_DeleteStmt = visit_SelectStmt

    def visit_WithClause(self, ancestors, node):
        if node is self.skip_with_clause:
            return Skip

    def visit_RangeVar(self, ancestors, node):
        "Collect relation names, taking into account defined CTE names"

        tname = maybe_double_quote_name(node.relname)

        if node.schemaname:
            tname = f'{maybe_double_quote_name(node.schemaname)}.{tname}'

        if node.catalogname:
            tname = f'{maybe_double_quote_name(node.catalogname)}.{tname}'

        if tname not in self.cte_names:
            self.r_names.add(tname)


def referenced_relations(stmt):
    """Return the set of relation names referenced in the given `stmt`.

    :param stmt: either a string containing the ``SQL`` statement or a :class:`.ast.Node`
                 instance
    :returns: a set of strings, the names of the relations

    Example:

    .. testsetup::

        from pglast.visitors import referenced_relations

    .. doctest::

        >>> referenced_relations('WITH q1(x,y) AS (SELECT 1,2)'
        ...                      ' SELECT * FROM q1, q2')
        {'q2'}
    """

    from .parser import parse_sql

    return ReferencedRelations()(parse_sql(stmt) if isinstance(stmt, str) else stmt)
