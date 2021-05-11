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

    The ``visit_XYZ`` methods receive two arguments: the *hierarchy path* of the node and the
    :class:`Node <.ast.Node>` instance itself. The `path` is a sequence of tuples, each
    containing either one or two slots: in the former case it is an integer index within a list
    of nodes, in the other case it indicates the *parent* node and the corresponding
    *attribute*.

    __ https://en.wikipedia.org/wiki/Breadth-first_search
    """

    def __call__(self, root):
        "Iteratively visit the `root` node calling related ``visit_XYZ`` methods."

        by_ast_class = {}
        for name, method in getmembers(self, ismethod):
            if not name.startswith('visit_'):
                continue

            clsname = name[6:]
            cls = getattr(ast, clsname, None)
            if cls is not None:
                by_ast_class[cls] = method

        default_method = self.visit

        for path, node in self.iterate(root):
            method = by_ast_class.get(node.__class__, default_method)
            if method is not None:
                method(path, node)

    def iterate(self, node):
        """Iterate thru `node`'s AST using a breadth-first traversing.

        :param node: either a :class:`Node <pglast.ast.Node>` instance or a tuple of those

        This is a generator, that yields ``Node`` instances together with their *hierarchy
        path* as it finds them while traversing the tree.
        """

        todo = deque()

        if isinstance(node, ast.Node):
            todo.append(((), node))
        elif isinstance(node, tuple):
            for index, item in enumerate(node):
                if isinstance(item, ast.Node):
                    todo.append(((index,), item))
        else:
            raise ValueError('Bad argument, expected a ast.Node instance or a tuple')

        while todo:
            path, node = todo.popleft()

            yield path, node

            for attr in node:
                value = getattr(node, attr)
                if isinstance(value, ast.Node):
                    todo.append((path + ((node, attr),), value))
                elif isinstance(value, tuple):
                    spath = path + ((node, attr),)
                    for index, item in enumerate(value):
                        if isinstance(item, ast.Node):
                            todo.append((spath + (index,), item))

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

    def visit_CommonTableExpr(self, path, node):
        "Collect CTE names."

        self.ctenames.add(node.ctename)

    def visit_DropStmt(self, path, node):
        from .enums import ObjectType
        if node.removeType in (ObjectType.OBJECT_TABLE, ObjectType.OBJECT_VIEW):
            for obj in node.objects:
                self.rnames.add('.'.join(n.val for n in obj))

    def visit_RangeVar(self, path, node):
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
