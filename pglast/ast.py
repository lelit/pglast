# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from struct_defs.json @ 14-latest-0-g6ebd8d8
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021-2022 Lele Gaifax
#

from collections import namedtuple
from decimal import Decimal
from enum import Enum


SlotTypeInfo = namedtuple('SlotTypeInfo', ['c_type', 'py_type', 'adaptor'])


def _serialize_node(n, depth, ellipsis, skip_none):
    d = {'@': n.__class__.__name__}
    for a in n:
        v = _serialize_value(getattr(n, a), depth, ellipsis, skip_none)
        if not skip_none or v is not None:
            d[a] = v
    return d


def _serialize_value(v, depth, ellipsis, skip_none):
    if isinstance(v, Node):
        if depth is None or depth > 0:
            v = _serialize_node(v, None if depth is None else depth - 1,
                                ellipsis, skip_none)
        else:
            v = ellipsis
    elif isinstance(v, tuple):
        if depth is None or depth > 0:
            v = tuple(_serialize_value(i, None if depth is None else depth - 1,
                                       ellipsis, skip_none)
                      for i in v)
        else:
            v = ellipsis
    elif isinstance(v, Enum):
        v = {'#': v.__class__.__name__, 'name': v.name, 'value': v.value}
    return v


class Omissis:
    def __eq__(self, other):
        if other is ... or other is self:
            return True
        return False

    def __repr__(self):
        return '…'


Omissis = Omissis()
"Marker value used as default for the ellipsis argument"


class Node:
    "Base class for all AST nodes."

    __slots__ = ('ancestors',)

    def __init__(self, data):
        if not isinstance(data, dict):  # pragma: no cover
            raise ValueError(f'Bad argument, expected a dictionary, got {type(data)!r}')
        if '@' not in data:  # pragma: no cover
            raise ValueError('Bad argument, expected a dictionary with a "@" key')
        if data['@'] != self.__class__.__name__:
            raise ValueError(f'Bad argument, wrong "@" value, expected'
                             f' {self.__class__.__name__!r}, got {data["@"]!r}')

        G = globals()
        for a in self:
            v = data.get(a)
            if v is not None:
                if isinstance(v, dict) and '@' in v:
                    v = G[v['@']](v)
                elif isinstance(v, (tuple, list)):
                    v = tuple(G[i['@']](i) if isinstance(i, dict) and '@' in i else i
                              for i in v)
            setattr(self, a, v)

    def __iter__(self):
        "Iterate over all attribute names of this node."

        return iter(self.__slots__)

    def __repr__(self):
        "Build a representation of the whole node and its subtree, for debug."

        attrs = []
        for a in self:
            if a != 'location':
                v = getattr(self, a)
                if v is not None:
                    attrs.append(f'{a}={v!r}')
        if attrs:
            attrs = ' ' + ' '.join(attrs)
        else:
            attrs = ''
        return '<' + self.__class__.__name__ + attrs + '>'

    _ATTRS_TO_IGNORE_IN_COMPARISON = {'location', 'stmt_len', 'stmt_location'}

    def __eq__(self, other):
        '''
        Compare two nodes, returning ``True`` if they are considered equivalent.

        This is mainly an helper method used by tests: for this reason, two nodes are
        considered equal when all their attributes match, ignoring *positional* ones such as
        ``location``, ``stmt_len`` and ``stmt_location``.
        '''

        if not isinstance(other, type(self)):
            return False
        for a in self:
            if ((a not in self._ATTRS_TO_IGNORE_IN_COMPARISON
                 and getattr(self, a) != getattr(other, a))):
                return False
        return True

    def __call__(self, depth=None, ellipsis=Omissis, skip_none=False):
        '''Serialize the node as a structure made of simple Python data-types.

        :type depth: ``None`` or ``int``
        :param depth: if not ``None``, the maximum depth to reach
        :param ellipsis: the marker value that will be used to replace cut-off branch
        :param bool skip_none: whether ``None``-valued attributes should be elided
        :param bool enum_name: whether Enums will be rendered as their name only
        :return: a :class:`dict` instance

        This performs a top-down recursive visit to the whole AST tree: each :class:`Node`
        instance becomes a dictionary with a special ``@`` key carrying the node type, lists
        becomes tuples and ``Enum`` instances become dictionaries with a special ``#`` key
        carrying the enum name.'''

        return _serialize_node(self, depth, ellipsis, skip_none)

    def __setattr__(self, name, value):
        '''Validate the given `value` and if acceptable assign it to the `name` attribute.

        This tries to coerce the given `value` accordingly with the *ctype* of the
        attribute, raising opportune exception when that is not possible.
        '''

        if value is not None and name in self.__slots__:
            ctype, ptype, adaptor = self.__slots__[name]
            if not isinstance(ptype, tuple):
                ptype = (ptype,)
            if not isinstance(value, ptype):
                raise ValueError(f'Bad value for attribute {self.__class__.__name__}'
                                 f'.{name}, expected {ptype}, got {type(value)}:'
                                 f' {value!r}')

            if adaptor is not None:
                value = adaptor(value)
            elif ctype != 'char*':
                from pglast import enums

                if hasattr(enums, ctype):
                    enum = getattr(enums, ctype)
                    if not isinstance(value, enum):
                        if isinstance(value, dict) and '#' in value:
                            if value['#'] != ctype:
                                raise ValueError(f'Bad value for attribute'
                                                 f' {self.__class__.__name__}.{name},'
                                                 f' expected a {ptype}, got'
                                                 f' {value!r}') from None
                            if 'name' in value:
                                value = value['name']
                            elif 'value' in value:
                                value = value['value']
                            else:
                                raise ValueError(f'Bad value for attribute'
                                                 f' {self.__class__.__name__}.{name},'
                                                 f' expected a {ptype}, got'
                                                 f' {value!r}') from None
                        try:
                            if isinstance(value, str) and len(value) > 1:
                                value = enum[value]
                            else:
                                value = enum(value)
                        except (KeyError, ValueError):
                            raise ValueError(f'Bad value for attribute'
                                             f' {self.__class__.__name__}.{name},'
                                             f' expected a {ptype}, got'
                                             f' {value!r}') from None
                else:
                    if ctype.endswith('*'):
                        cls = globals().get(ctype[:-1])
                        if cls is None:
                            raise NotImplementedError(f'Unhandled {ctype!r} for attribute'
                                                      f' {self.__class__.__name__}.{name}')
                        if isinstance(value, dict) and '@' in value:
                            value = cls(value)

        super().__setattr__(name, value)


class Expr(Node):
    '''Abstract super class of several *expression* classes.'''

    __slots__ = ()


class Value(Node):
    '''Abstract super class, representing PG's `Value`__ union type.

    __ https://git.postgresql.org/gitweb/?p=postgresql.git;a=blob;f=src/include/nodes/value.h
    '''

    __slots__ = ()

    def __init__(self, value=None):
        if ((value is not None
             and isinstance(value, dict)
             and '@' in value)):
            super().__init__(value)
        else:
            self.val = value


class BitString(Value):
    '''Implement the ``T_BitString`` variant of the :class:`Value` union.'''

    __slots__ = {'val': SlotTypeInfo('char*', str, None)}


class Float(Value):
    '''Implement the ``T_Float`` variant of the :class:`Value` union.'''

    __slots__ = {'val': SlotTypeInfo('char*', (str, Decimal), Decimal)}


class Integer(Value):
    '''Implement the ``T_Integer`` variant of the :class:`Value` union.'''

    __slots__ = {'val': SlotTypeInfo('char*', int, None)}


class Null(Value):
    '''Implement the ``T_Null`` variant of the :class:`Value` union.'''

    __slots__ = {'val': SlotTypeInfo('char*', type(None), None)}


class String(Value):
    '''Implement the ``T_String`` variant of the :class:`Value` union.'''

    __slots__ = {'val': SlotTypeInfo('char*', str, None)}


class A_ArrayExpr(Node):
    __slots__ = {'elements': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, elements=None, location=None):  # pragma: no cover  # noqa: E501
        if ((elements is not None
             and location is None  # noqa: E501
             and isinstance(elements, dict)
             and '@' in elements)):
            super().__init__(elements)
        else:
            self.elements = elements
            self.location = location


class A_Const(Node):
    __slots__ = {'val': 'Value', 'location': 'int'}  # noqa: E501

    def __init__(self, val=None, location=None):  # pragma: no cover  # noqa: E501
        if ((val is not None
             and location is None  # noqa: E501
             and isinstance(val, dict)
             and '@' in val)):
            super().__init__(val)
        else:
            self.val = val
            self.location = location


class A_Expr(Node):
    __slots__ = {'kind': 'A_Expr_Kind', 'name': 'List*', 'lexpr': 'Node*', 'rexpr': 'Node*', 'location': 'int'}  # noqa: E501

    def __init__(self, kind=None, name=None, lexpr=None, rexpr=None, location=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and name is lexpr is rexpr is location is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.name = name
            self.lexpr = lexpr
            self.rexpr = rexpr
            self.location = location


class A_Indices(Node):
    __slots__ = {'is_slice': 'bool', 'lidx': 'Node*', 'uidx': 'Node*'}  # noqa: E501

    def __init__(self, is_slice=None, lidx=None, uidx=None):  # pragma: no cover  # noqa: E501
        if ((is_slice is not None
             and lidx is uidx is None  # noqa: E501
             and isinstance(is_slice, dict)
             and '@' in is_slice)):
            super().__init__(is_slice)
        else:
            self.is_slice = is_slice
            self.lidx = lidx
            self.uidx = uidx


class A_Indirection(Node):
    __slots__ = {'arg': 'Node*', 'indirection': 'List*'}  # noqa: E501

    def __init__(self, arg=None, indirection=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and indirection is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.indirection = indirection


class A_Star(Node):
    __slots__ = {}  # noqa: E501

    def __init__(self):  # pragma: no cover
        pass


class AccessPriv(Node):
    __slots__ = {'priv_name': 'char*', 'cols': 'List*'}  # noqa: E501

    def __init__(self, priv_name=None, cols=None):  # pragma: no cover  # noqa: E501
        if ((priv_name is not None
             and cols is None  # noqa: E501
             and isinstance(priv_name, dict)
             and '@' in priv_name)):
            super().__init__(priv_name)
        else:
            self.priv_name = priv_name
            self.cols = cols


class Aggref(Expr):
    __slots__ = {'aggargtypes': 'List*', 'aggdirectargs': 'List*', 'args': 'List*', 'aggorder': 'List*', 'aggdistinct': 'List*', 'aggfilter': 'Expr*', 'aggstar': 'bool', 'aggvariadic': 'bool', 'aggkind': 'char', 'agglevelsup': 'Index', 'aggsplit': 'AggSplit', 'aggno': 'int', 'aggtransno': 'int', 'location': 'int'}  # noqa: E501

    def __init__(self, aggargtypes=None, aggdirectargs=None, args=None, aggorder=None, aggdistinct=None, aggfilter=None, aggstar=None, aggvariadic=None, aggkind=None, agglevelsup=None, aggsplit=None, aggno=None, aggtransno=None, location=None):  # pragma: no cover  # noqa: E501
        if ((aggargtypes is not None
             and aggdirectargs is args is aggorder is aggdistinct is aggfilter is aggstar is aggvariadic is aggkind is agglevelsup is aggsplit is aggno is aggtransno is location is None  # noqa: E501
             and isinstance(aggargtypes, dict)
             and '@' in aggargtypes)):
            super().__init__(aggargtypes)
        else:
            self.aggargtypes = aggargtypes
            self.aggdirectargs = aggdirectargs
            self.args = args
            self.aggorder = aggorder
            self.aggdistinct = aggdistinct
            self.aggfilter = aggfilter
            self.aggstar = aggstar
            self.aggvariadic = aggvariadic
            self.aggkind = aggkind
            self.agglevelsup = agglevelsup
            self.aggsplit = aggsplit
            self.aggno = aggno
            self.aggtransno = aggtransno
            self.location = location


class Alias(Node):
    __slots__ = {'aliasname': 'char*', 'colnames': 'List*'}  # noqa: E501

    def __init__(self, aliasname=None, colnames=None):  # pragma: no cover  # noqa: E501
        if ((aliasname is not None
             and colnames is None  # noqa: E501
             and isinstance(aliasname, dict)
             and '@' in aliasname)):
            super().__init__(aliasname)
        else:
            self.aliasname = aliasname
            self.colnames = colnames


class AlterCollationStmt(Node):
    __slots__ = {'collname': 'List*'}  # noqa: E501

    def __init__(self, collname=None):  # pragma: no cover  # noqa: E501

        if ((collname is not None
             and isinstance(collname, dict)
             and '@' in collname)):
            super().__init__(collname)
        else:
            self.collname = collname


class AlterDatabaseSetStmt(Node):
    __slots__ = {'dbname': 'char*', 'setstmt': 'VariableSetStmt*'}  # noqa: E501

    def __init__(self, dbname=None, setstmt=None):  # pragma: no cover  # noqa: E501
        if ((dbname is not None
             and setstmt is None  # noqa: E501
             and isinstance(dbname, dict)
             and '@' in dbname)):
            super().__init__(dbname)
        else:
            self.dbname = dbname
            self.setstmt = setstmt


class AlterDatabaseStmt(Node):
    __slots__ = {'dbname': 'char*', 'options': 'List*'}  # noqa: E501

    def __init__(self, dbname=None, options=None):  # pragma: no cover  # noqa: E501
        if ((dbname is not None
             and options is None  # noqa: E501
             and isinstance(dbname, dict)
             and '@' in dbname)):
            super().__init__(dbname)
        else:
            self.dbname = dbname
            self.options = options


class AlterDefaultPrivilegesStmt(Node):
    __slots__ = {'options': 'List*', 'action': 'GrantStmt*'}  # noqa: E501

    def __init__(self, options=None, action=None):  # pragma: no cover  # noqa: E501
        if ((options is not None
             and action is None  # noqa: E501
             and isinstance(options, dict)
             and '@' in options)):
            super().__init__(options)
        else:
            self.options = options
            self.action = action


class AlterDomainStmt(Node):
    __slots__ = {'subtype': 'char', 'typeName': 'List*', 'name': 'char*', 'def_': 'Node*', 'behavior': 'DropBehavior', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, subtype=None, typeName=None, name=None, def_=None, behavior=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((subtype is not None
             and typeName is name is def_ is behavior is missing_ok is None  # noqa: E501
             and isinstance(subtype, dict)
             and '@' in subtype)):
            super().__init__(subtype)
        else:
            self.subtype = subtype
            self.typeName = typeName
            self.name = name
            self.def_ = def_
            self.behavior = behavior
            self.missing_ok = missing_ok


class AlterEnumStmt(Node):
    __slots__ = {'typeName': 'List*', 'oldVal': 'char*', 'newVal': 'char*', 'newValNeighbor': 'char*', 'newValIsAfter': 'bool', 'skipIfNewValExists': 'bool'}  # noqa: E501

    def __init__(self, typeName=None, oldVal=None, newVal=None, newValNeighbor=None, newValIsAfter=None, skipIfNewValExists=None):  # pragma: no cover  # noqa: E501
        if ((typeName is not None
             and oldVal is newVal is newValNeighbor is newValIsAfter is skipIfNewValExists is None  # noqa: E501
             and isinstance(typeName, dict)
             and '@' in typeName)):
            super().__init__(typeName)
        else:
            self.typeName = typeName
            self.oldVal = oldVal
            self.newVal = newVal
            self.newValNeighbor = newValNeighbor
            self.newValIsAfter = newValIsAfter
            self.skipIfNewValExists = skipIfNewValExists


class AlterEventTrigStmt(Node):
    __slots__ = {'trigname': 'char*', 'tgenabled': 'char'}  # noqa: E501

    def __init__(self, trigname=None, tgenabled=None):  # pragma: no cover  # noqa: E501
        if ((trigname is not None
             and tgenabled is None  # noqa: E501
             and isinstance(trigname, dict)
             and '@' in trigname)):
            super().__init__(trigname)
        else:
            self.trigname = trigname
            self.tgenabled = tgenabled


class AlterExtensionContentsStmt(Node):
    __slots__ = {'extname': 'char*', 'action': 'int', 'objtype': 'ObjectType', 'object': 'Node*'}  # noqa: E501

    def __init__(self, extname=None, action=None, objtype=None, object=None):  # pragma: no cover  # noqa: E501
        if ((extname is not None
             and action is objtype is object is None  # noqa: E501
             and isinstance(extname, dict)
             and '@' in extname)):
            super().__init__(extname)
        else:
            self.extname = extname
            self.action = action
            self.objtype = objtype
            self.object = object


class AlterExtensionStmt(Node):
    __slots__ = {'extname': 'char*', 'options': 'List*'}  # noqa: E501

    def __init__(self, extname=None, options=None):  # pragma: no cover  # noqa: E501
        if ((extname is not None
             and options is None  # noqa: E501
             and isinstance(extname, dict)
             and '@' in extname)):
            super().__init__(extname)
        else:
            self.extname = extname
            self.options = options


class AlterFdwStmt(Node):
    __slots__ = {'fdwname': 'char*', 'func_options': 'List*', 'options': 'List*'}  # noqa: E501

    def __init__(self, fdwname=None, func_options=None, options=None):  # pragma: no cover  # noqa: E501
        if ((fdwname is not None
             and func_options is options is None  # noqa: E501
             and isinstance(fdwname, dict)
             and '@' in fdwname)):
            super().__init__(fdwname)
        else:
            self.fdwname = fdwname
            self.func_options = func_options
            self.options = options


class AlterForeignServerStmt(Node):
    __slots__ = {'servername': 'char*', 'version': 'char*', 'options': 'List*', 'has_version': 'bool'}  # noqa: E501

    def __init__(self, servername=None, version=None, options=None, has_version=None):  # pragma: no cover  # noqa: E501
        if ((servername is not None
             and version is options is has_version is None  # noqa: E501
             and isinstance(servername, dict)
             and '@' in servername)):
            super().__init__(servername)
        else:
            self.servername = servername
            self.version = version
            self.options = options
            self.has_version = has_version


class AlterFunctionStmt(Node):
    __slots__ = {'objtype': 'ObjectType', 'func': 'ObjectWithArgs*', 'actions': 'List*'}  # noqa: E501

    def __init__(self, objtype=None, func=None, actions=None):  # pragma: no cover  # noqa: E501
        if ((objtype is not None
             and func is actions is None  # noqa: E501
             and isinstance(objtype, dict)
             and '@' in objtype)):
            super().__init__(objtype)
        else:
            self.objtype = objtype
            self.func = func
            self.actions = actions


class AlterObjectDependsStmt(Node):
    __slots__ = {'objectType': 'ObjectType', 'relation': 'RangeVar*', 'object': 'Node*', 'extname': 'Value*', 'remove': 'bool'}  # noqa: E501

    def __init__(self, objectType=None, relation=None, object=None, extname=None, remove=None):  # pragma: no cover  # noqa: E501
        if ((objectType is not None
             and relation is object is extname is remove is None  # noqa: E501
             and isinstance(objectType, dict)
             and '@' in objectType)):
            super().__init__(objectType)
        else:
            self.objectType = objectType
            self.relation = relation
            self.object = object
            self.extname = extname
            self.remove = remove


class AlterObjectSchemaStmt(Node):
    __slots__ = {'objectType': 'ObjectType', 'relation': 'RangeVar*', 'object': 'Node*', 'newschema': 'char*', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, objectType=None, relation=None, object=None, newschema=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((objectType is not None
             and relation is object is newschema is missing_ok is None  # noqa: E501
             and isinstance(objectType, dict)
             and '@' in objectType)):
            super().__init__(objectType)
        else:
            self.objectType = objectType
            self.relation = relation
            self.object = object
            self.newschema = newschema
            self.missing_ok = missing_ok


class AlterOpFamilyStmt(Node):
    __slots__ = {'opfamilyname': 'List*', 'amname': 'char*', 'isDrop': 'bool', 'items': 'List*'}  # noqa: E501

    def __init__(self, opfamilyname=None, amname=None, isDrop=None, items=None):  # pragma: no cover  # noqa: E501
        if ((opfamilyname is not None
             and amname is isDrop is items is None  # noqa: E501
             and isinstance(opfamilyname, dict)
             and '@' in opfamilyname)):
            super().__init__(opfamilyname)
        else:
            self.opfamilyname = opfamilyname
            self.amname = amname
            self.isDrop = isDrop
            self.items = items


class AlterOperatorStmt(Node):
    __slots__ = {'opername': 'ObjectWithArgs*', 'options': 'List*'}  # noqa: E501

    def __init__(self, opername=None, options=None):  # pragma: no cover  # noqa: E501
        if ((opername is not None
             and options is None  # noqa: E501
             and isinstance(opername, dict)
             and '@' in opername)):
            super().__init__(opername)
        else:
            self.opername = opername
            self.options = options


class AlterOwnerStmt(Node):
    __slots__ = {'objectType': 'ObjectType', 'relation': 'RangeVar*', 'object': 'Node*', 'newowner': 'RoleSpec*'}  # noqa: E501

    def __init__(self, objectType=None, relation=None, object=None, newowner=None):  # pragma: no cover  # noqa: E501
        if ((objectType is not None
             and relation is object is newowner is None  # noqa: E501
             and isinstance(objectType, dict)
             and '@' in objectType)):
            super().__init__(objectType)
        else:
            self.objectType = objectType
            self.relation = relation
            self.object = object
            self.newowner = newowner


class AlterPolicyStmt(Node):
    __slots__ = {'policy_name': 'char*', 'table': 'RangeVar*', 'roles': 'List*', 'qual': 'Node*', 'with_check': 'Node*'}  # noqa: E501

    def __init__(self, policy_name=None, table=None, roles=None, qual=None, with_check=None):  # pragma: no cover  # noqa: E501
        if ((policy_name is not None
             and table is roles is qual is with_check is None  # noqa: E501
             and isinstance(policy_name, dict)
             and '@' in policy_name)):
            super().__init__(policy_name)
        else:
            self.policy_name = policy_name
            self.table = table
            self.roles = roles
            self.qual = qual
            self.with_check = with_check


class AlterPublicationStmt(Node):
    __slots__ = {'pubname': 'char*', 'options': 'List*', 'tables': 'List*', 'for_all_tables': 'bool', 'tableAction': 'DefElemAction'}  # noqa: E501

    def __init__(self, pubname=None, options=None, tables=None, for_all_tables=None, tableAction=None):  # pragma: no cover  # noqa: E501
        if ((pubname is not None
             and options is tables is for_all_tables is tableAction is None  # noqa: E501
             and isinstance(pubname, dict)
             and '@' in pubname)):
            super().__init__(pubname)
        else:
            self.pubname = pubname
            self.options = options
            self.tables = tables
            self.for_all_tables = for_all_tables
            self.tableAction = tableAction


class AlterRoleSetStmt(Node):
    __slots__ = {'role': 'RoleSpec*', 'database': 'char*', 'setstmt': 'VariableSetStmt*'}  # noqa: E501

    def __init__(self, role=None, database=None, setstmt=None):  # pragma: no cover  # noqa: E501
        if ((role is not None
             and database is setstmt is None  # noqa: E501
             and isinstance(role, dict)
             and '@' in role)):
            super().__init__(role)
        else:
            self.role = role
            self.database = database
            self.setstmt = setstmt


class AlterRoleStmt(Node):
    __slots__ = {'role': 'RoleSpec*', 'options': 'List*', 'action': 'int'}  # noqa: E501

    def __init__(self, role=None, options=None, action=None):  # pragma: no cover  # noqa: E501
        if ((role is not None
             and options is action is None  # noqa: E501
             and isinstance(role, dict)
             and '@' in role)):
            super().__init__(role)
        else:
            self.role = role
            self.options = options
            self.action = action


class AlterSeqStmt(Node):
    __slots__ = {'sequence': 'RangeVar*', 'options': 'List*', 'for_identity': 'bool', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, sequence=None, options=None, for_identity=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((sequence is not None
             and options is for_identity is missing_ok is None  # noqa: E501
             and isinstance(sequence, dict)
             and '@' in sequence)):
            super().__init__(sequence)
        else:
            self.sequence = sequence
            self.options = options
            self.for_identity = for_identity
            self.missing_ok = missing_ok


class AlterStatsStmt(Node):
    __slots__ = {'defnames': 'List*', 'stxstattarget': 'int', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, defnames=None, stxstattarget=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((defnames is not None
             and stxstattarget is missing_ok is None  # noqa: E501
             and isinstance(defnames, dict)
             and '@' in defnames)):
            super().__init__(defnames)
        else:
            self.defnames = defnames
            self.stxstattarget = stxstattarget
            self.missing_ok = missing_ok


class AlterSubscriptionStmt(Node):
    __slots__ = {'kind': 'AlterSubscriptionType', 'subname': 'char*', 'conninfo': 'char*', 'publication': 'List*', 'options': 'List*'}  # noqa: E501

    def __init__(self, kind=None, subname=None, conninfo=None, publication=None, options=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and subname is conninfo is publication is options is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.subname = subname
            self.conninfo = conninfo
            self.publication = publication
            self.options = options


class AlterSystemStmt(Node):
    __slots__ = {'setstmt': 'VariableSetStmt*'}  # noqa: E501

    def __init__(self, setstmt=None):  # pragma: no cover  # noqa: E501

        if ((setstmt is not None
             and isinstance(setstmt, dict)
             and '@' in setstmt)):
            super().__init__(setstmt)
        else:
            self.setstmt = setstmt


class AlterTSConfigurationStmt(Node):
    __slots__ = {'kind': 'AlterTSConfigType', 'cfgname': 'List*', 'tokentype': 'List*', 'dicts': 'List*', 'override': 'bool', 'replace': 'bool', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, kind=None, cfgname=None, tokentype=None, dicts=None, override=None, replace=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and cfgname is tokentype is dicts is override is replace is missing_ok is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.cfgname = cfgname
            self.tokentype = tokentype
            self.dicts = dicts
            self.override = override
            self.replace = replace
            self.missing_ok = missing_ok


class AlterTSDictionaryStmt(Node):
    __slots__ = {'dictname': 'List*', 'options': 'List*'}  # noqa: E501

    def __init__(self, dictname=None, options=None):  # pragma: no cover  # noqa: E501
        if ((dictname is not None
             and options is None  # noqa: E501
             and isinstance(dictname, dict)
             and '@' in dictname)):
            super().__init__(dictname)
        else:
            self.dictname = dictname
            self.options = options


class AlterTableCmd(Node):
    __slots__ = {'subtype': 'AlterTableType', 'name': 'char*', 'num': 'int16', 'newowner': 'RoleSpec*', 'def_': 'Node*', 'behavior': 'DropBehavior', 'missing_ok': 'bool', 'recurse': 'bool'}  # noqa: E501

    def __init__(self, subtype=None, name=None, num=None, newowner=None, def_=None, behavior=None, missing_ok=None, recurse=None):  # pragma: no cover  # noqa: E501
        if ((subtype is not None
             and name is num is newowner is def_ is behavior is missing_ok is recurse is None  # noqa: E501
             and isinstance(subtype, dict)
             and '@' in subtype)):
            super().__init__(subtype)
        else:
            self.subtype = subtype
            self.name = name
            self.num = num
            self.newowner = newowner
            self.def_ = def_
            self.behavior = behavior
            self.missing_ok = missing_ok
            self.recurse = recurse


class AlterTableMoveAllStmt(Node):
    __slots__ = {'orig_tablespacename': 'char*', 'objtype': 'ObjectType', 'roles': 'List*', 'new_tablespacename': 'char*', 'nowait': 'bool'}  # noqa: E501

    def __init__(self, orig_tablespacename=None, objtype=None, roles=None, new_tablespacename=None, nowait=None):  # pragma: no cover  # noqa: E501
        if ((orig_tablespacename is not None
             and objtype is roles is new_tablespacename is nowait is None  # noqa: E501
             and isinstance(orig_tablespacename, dict)
             and '@' in orig_tablespacename)):
            super().__init__(orig_tablespacename)
        else:
            self.orig_tablespacename = orig_tablespacename
            self.objtype = objtype
            self.roles = roles
            self.new_tablespacename = new_tablespacename
            self.nowait = nowait


class AlterTableSpaceOptionsStmt(Node):
    __slots__ = {'tablespacename': 'char*', 'options': 'List*', 'isReset': 'bool'}  # noqa: E501

    def __init__(self, tablespacename=None, options=None, isReset=None):  # pragma: no cover  # noqa: E501
        if ((tablespacename is not None
             and options is isReset is None  # noqa: E501
             and isinstance(tablespacename, dict)
             and '@' in tablespacename)):
            super().__init__(tablespacename)
        else:
            self.tablespacename = tablespacename
            self.options = options
            self.isReset = isReset


class AlterTableStmt(Node):
    __slots__ = {'relation': 'RangeVar*', 'cmds': 'List*', 'objtype': 'ObjectType', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, relation=None, cmds=None, objtype=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and cmds is objtype is missing_ok is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.cmds = cmds
            self.objtype = objtype
            self.missing_ok = missing_ok


class AlterTypeStmt(Node):
    __slots__ = {'typeName': 'List*', 'options': 'List*'}  # noqa: E501

    def __init__(self, typeName=None, options=None):  # pragma: no cover  # noqa: E501
        if ((typeName is not None
             and options is None  # noqa: E501
             and isinstance(typeName, dict)
             and '@' in typeName)):
            super().__init__(typeName)
        else:
            self.typeName = typeName
            self.options = options


class AlterUserMappingStmt(Node):
    __slots__ = {'user': 'RoleSpec*', 'servername': 'char*', 'options': 'List*'}  # noqa: E501

    def __init__(self, user=None, servername=None, options=None):  # pragma: no cover  # noqa: E501
        if ((user is not None
             and servername is options is None  # noqa: E501
             and isinstance(user, dict)
             and '@' in user)):
            super().__init__(user)
        else:
            self.user = user
            self.servername = servername
            self.options = options


class AlternativeSubPlan(Expr):
    __slots__ = {'subplans': 'List*'}  # noqa: E501

    def __init__(self, subplans=None):  # pragma: no cover  # noqa: E501

        if ((subplans is not None
             and isinstance(subplans, dict)
             and '@' in subplans)):
            super().__init__(subplans)
        else:
            self.subplans = subplans


class ArrayCoerceExpr(Expr):
    __slots__ = {'arg': 'Expr*', 'elemexpr': 'Expr*', 'resulttypmod': 'int32', 'coerceformat': 'CoercionForm', 'location': 'int'}  # noqa: E501

    _ATTRS_TO_IGNORE_IN_COMPARISON = Expr._ATTRS_TO_IGNORE_IN_COMPARISON | {'coerceformat'}

    def __init__(self, arg=None, elemexpr=None, resulttypmod=None, coerceformat=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and elemexpr is resulttypmod is coerceformat is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.elemexpr = elemexpr
            self.resulttypmod = resulttypmod
            self.coerceformat = coerceformat
            self.location = location


class ArrayExpr(Expr):
    __slots__ = {'elements': 'List*', 'multidims': 'bool', 'location': 'int'}  # noqa: E501

    def __init__(self, elements=None, multidims=None, location=None):  # pragma: no cover  # noqa: E501
        if ((elements is not None
             and multidims is location is None  # noqa: E501
             and isinstance(elements, dict)
             and '@' in elements)):
            super().__init__(elements)
        else:
            self.elements = elements
            self.multidims = multidims
            self.location = location


class BoolExpr(Expr):
    __slots__ = {'boolop': 'BoolExprType', 'args': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, boolop=None, args=None, location=None):  # pragma: no cover  # noqa: E501
        if ((boolop is not None
             and args is location is None  # noqa: E501
             and isinstance(boolop, dict)
             and '@' in boolop)):
            super().__init__(boolop)
        else:
            self.boolop = boolop
            self.args = args
            self.location = location


class BooleanTest(Expr):
    __slots__ = {'arg': 'Expr*', 'booltesttype': 'BoolTestType', 'location': 'int'}  # noqa: E501

    def __init__(self, arg=None, booltesttype=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and booltesttype is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.booltesttype = booltesttype
            self.location = location


class CTECycleClause(Node):
    __slots__ = {'cycle_col_list': 'List*', 'cycle_mark_column': 'char*', 'cycle_mark_value': 'Node*', 'cycle_mark_default': 'Node*', 'cycle_path_column': 'char*', 'location': 'int', 'cycle_mark_typmod': 'int'}  # noqa: E501

    def __init__(self, cycle_col_list=None, cycle_mark_column=None, cycle_mark_value=None, cycle_mark_default=None, cycle_path_column=None, location=None, cycle_mark_typmod=None):  # pragma: no cover  # noqa: E501
        if ((cycle_col_list is not None
             and cycle_mark_column is cycle_mark_value is cycle_mark_default is cycle_path_column is location is cycle_mark_typmod is None  # noqa: E501
             and isinstance(cycle_col_list, dict)
             and '@' in cycle_col_list)):
            super().__init__(cycle_col_list)
        else:
            self.cycle_col_list = cycle_col_list
            self.cycle_mark_column = cycle_mark_column
            self.cycle_mark_value = cycle_mark_value
            self.cycle_mark_default = cycle_mark_default
            self.cycle_path_column = cycle_path_column
            self.location = location
            self.cycle_mark_typmod = cycle_mark_typmod


class CTESearchClause(Node):
    __slots__ = {'search_col_list': 'List*', 'search_breadth_first': 'bool', 'search_seq_column': 'char*', 'location': 'int'}  # noqa: E501

    def __init__(self, search_col_list=None, search_breadth_first=None, search_seq_column=None, location=None):  # pragma: no cover  # noqa: E501
        if ((search_col_list is not None
             and search_breadth_first is search_seq_column is location is None  # noqa: E501
             and isinstance(search_col_list, dict)
             and '@' in search_col_list)):
            super().__init__(search_col_list)
        else:
            self.search_col_list = search_col_list
            self.search_breadth_first = search_breadth_first
            self.search_seq_column = search_seq_column
            self.location = location


class CallContext(Node):
    __slots__ = {'atomic': 'bool'}  # noqa: E501

    def __init__(self, atomic=None):  # pragma: no cover  # noqa: E501

        if ((atomic is not None
             and isinstance(atomic, dict)
             and '@' in atomic)):
            super().__init__(atomic)
        else:
            self.atomic = atomic


class CallStmt(Node):
    __slots__ = {'funccall': 'FuncCall*', 'funcexpr': 'FuncExpr*', 'outargs': 'List*'}  # noqa: E501

    def __init__(self, funccall=None, funcexpr=None, outargs=None):  # pragma: no cover  # noqa: E501
        if ((funccall is not None
             and funcexpr is outargs is None  # noqa: E501
             and isinstance(funccall, dict)
             and '@' in funccall)):
            super().__init__(funccall)
        else:
            self.funccall = funccall
            self.funcexpr = funcexpr
            self.outargs = outargs


class CaseExpr(Expr):
    __slots__ = {'arg': 'Expr*', 'args': 'List*', 'defresult': 'Expr*', 'location': 'int'}  # noqa: E501

    def __init__(self, arg=None, args=None, defresult=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and args is defresult is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.args = args
            self.defresult = defresult
            self.location = location


class CaseTestExpr(Expr):
    __slots__ = {'typeMod': 'int32'}  # noqa: E501

    def __init__(self, typeMod=None):  # pragma: no cover  # noqa: E501

        if ((typeMod is not None
             and isinstance(typeMod, dict)
             and '@' in typeMod)):
            super().__init__(typeMod)
        else:
            self.typeMod = typeMod


class CaseWhen(Expr):
    __slots__ = {'expr': 'Expr*', 'result': 'Expr*', 'location': 'int'}  # noqa: E501

    def __init__(self, expr=None, result=None, location=None):  # pragma: no cover  # noqa: E501
        if ((expr is not None
             and result is location is None  # noqa: E501
             and isinstance(expr, dict)
             and '@' in expr)):
            super().__init__(expr)
        else:
            self.expr = expr
            self.result = result
            self.location = location


class CheckPointStmt(Node):
    __slots__ = {}  # noqa: E501

    def __init__(self):  # pragma: no cover
        pass


class ClosePortalStmt(Node):
    __slots__ = {'portalname': 'char*'}  # noqa: E501

    def __init__(self, portalname=None):  # pragma: no cover  # noqa: E501

        if ((portalname is not None
             and isinstance(portalname, dict)
             and '@' in portalname)):
            super().__init__(portalname)
        else:
            self.portalname = portalname


class ClusterStmt(Node):
    __slots__ = {'relation': 'RangeVar*', 'indexname': 'char*', 'params': 'List*'}  # noqa: E501

    def __init__(self, relation=None, indexname=None, params=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and indexname is params is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.indexname = indexname
            self.params = params


class CoalesceExpr(Expr):
    __slots__ = {'args': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, args=None, location=None):  # pragma: no cover  # noqa: E501
        if ((args is not None
             and location is None  # noqa: E501
             and isinstance(args, dict)
             and '@' in args)):
            super().__init__(args)
        else:
            self.args = args
            self.location = location


class CoerceToDomain(Expr):
    __slots__ = {'arg': 'Expr*', 'resulttypmod': 'int32', 'coercionformat': 'CoercionForm', 'location': 'int'}  # noqa: E501

    _ATTRS_TO_IGNORE_IN_COMPARISON = Expr._ATTRS_TO_IGNORE_IN_COMPARISON | {'coercionformat'}

    def __init__(self, arg=None, resulttypmod=None, coercionformat=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and resulttypmod is coercionformat is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.resulttypmod = resulttypmod
            self.coercionformat = coercionformat
            self.location = location


class CoerceToDomainValue(Expr):
    __slots__ = {'typeMod': 'int32', 'location': 'int'}  # noqa: E501

    def __init__(self, typeMod=None, location=None):  # pragma: no cover  # noqa: E501
        if ((typeMod is not None
             and location is None  # noqa: E501
             and isinstance(typeMod, dict)
             and '@' in typeMod)):
            super().__init__(typeMod)
        else:
            self.typeMod = typeMod
            self.location = location


class CoerceViaIO(Expr):
    __slots__ = {'arg': 'Expr*', 'coerceformat': 'CoercionForm', 'location': 'int'}  # noqa: E501

    _ATTRS_TO_IGNORE_IN_COMPARISON = Expr._ATTRS_TO_IGNORE_IN_COMPARISON | {'coerceformat'}

    def __init__(self, arg=None, coerceformat=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and coerceformat is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.coerceformat = coerceformat
            self.location = location


class CollateClause(Node):
    __slots__ = {'arg': 'Node*', 'collname': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, arg=None, collname=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and collname is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.collname = collname
            self.location = location


class CollateExpr(Expr):
    __slots__ = {'arg': 'Expr*', 'location': 'int'}  # noqa: E501

    def __init__(self, arg=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.location = location


class ColumnDef(Node):
    __slots__ = {'colname': 'char*', 'typeName': 'TypeName*', 'compression': 'char*', 'inhcount': 'int', 'is_local': 'bool', 'is_not_null': 'bool', 'is_from_type': 'bool', 'storage': 'char', 'raw_default': 'Node*', 'cooked_default': 'Node*', 'identity': 'char', 'identitySequence': 'RangeVar*', 'generated': 'char', 'collClause': 'CollateClause*', 'constraints': 'List*', 'fdwoptions': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, colname=None, typeName=None, compression=None, inhcount=None, is_local=None, is_not_null=None, is_from_type=None, storage=None, raw_default=None, cooked_default=None, identity=None, identitySequence=None, generated=None, collClause=None, constraints=None, fdwoptions=None, location=None):  # pragma: no cover  # noqa: E501
        if ((colname is not None
             and typeName is compression is inhcount is is_local is is_not_null is is_from_type is storage is raw_default is cooked_default is identity is identitySequence is generated is collClause is constraints is fdwoptions is location is None  # noqa: E501
             and isinstance(colname, dict)
             and '@' in colname)):
            super().__init__(colname)
        else:
            self.colname = colname
            self.typeName = typeName
            self.compression = compression
            self.inhcount = inhcount
            self.is_local = is_local
            self.is_not_null = is_not_null
            self.is_from_type = is_from_type
            self.storage = storage
            self.raw_default = raw_default
            self.cooked_default = cooked_default
            self.identity = identity
            self.identitySequence = identitySequence
            self.generated = generated
            self.collClause = collClause
            self.constraints = constraints
            self.fdwoptions = fdwoptions
            self.location = location


class ColumnRef(Node):
    __slots__ = {'fields': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, fields=None, location=None):  # pragma: no cover  # noqa: E501
        if ((fields is not None
             and location is None  # noqa: E501
             and isinstance(fields, dict)
             and '@' in fields)):
            super().__init__(fields)
        else:
            self.fields = fields
            self.location = location


class CommentStmt(Node):
    __slots__ = {'objtype': 'ObjectType', 'object': 'Node*', 'comment': 'char*'}  # noqa: E501

    def __init__(self, objtype=None, object=None, comment=None):  # pragma: no cover  # noqa: E501
        if ((objtype is not None
             and object is comment is None  # noqa: E501
             and isinstance(objtype, dict)
             and '@' in objtype)):
            super().__init__(objtype)
        else:
            self.objtype = objtype
            self.object = object
            self.comment = comment


class CommonTableExpr(Node):
    __slots__ = {'ctename': 'char*', 'aliascolnames': 'List*', 'ctematerialized': 'CTEMaterialize', 'ctequery': 'Node*', 'search_clause': 'CTESearchClause*', 'cycle_clause': 'CTECycleClause*', 'location': 'int', 'cterecursive': 'bool', 'cterefcount': 'int', 'ctecolnames': 'List*', 'ctecoltypes': 'List*', 'ctecoltypmods': 'List*', 'ctecolcollations': 'List*'}  # noqa: E501

    def __init__(self, ctename=None, aliascolnames=None, ctematerialized=None, ctequery=None, search_clause=None, cycle_clause=None, location=None, cterecursive=None, cterefcount=None, ctecolnames=None, ctecoltypes=None, ctecoltypmods=None, ctecolcollations=None):  # pragma: no cover  # noqa: E501
        if ((ctename is not None
             and aliascolnames is ctematerialized is ctequery is search_clause is cycle_clause is location is cterecursive is cterefcount is ctecolnames is ctecoltypes is ctecoltypmods is ctecolcollations is None  # noqa: E501
             and isinstance(ctename, dict)
             and '@' in ctename)):
            super().__init__(ctename)
        else:
            self.ctename = ctename
            self.aliascolnames = aliascolnames
            self.ctematerialized = ctematerialized
            self.ctequery = ctequery
            self.search_clause = search_clause
            self.cycle_clause = cycle_clause
            self.location = location
            self.cterecursive = cterecursive
            self.cterefcount = cterefcount
            self.ctecolnames = ctecolnames
            self.ctecoltypes = ctecoltypes
            self.ctecoltypmods = ctecoltypmods
            self.ctecolcollations = ctecolcollations


class CompositeTypeStmt(Node):
    __slots__ = {'typevar': 'RangeVar*', 'coldeflist': 'List*'}  # noqa: E501

    def __init__(self, typevar=None, coldeflist=None):  # pragma: no cover  # noqa: E501
        if ((typevar is not None
             and coldeflist is None  # noqa: E501
             and isinstance(typevar, dict)
             and '@' in typevar)):
            super().__init__(typevar)
        else:
            self.typevar = typevar
            self.coldeflist = coldeflist


class Constraint(Node):
    __slots__ = {'contype': 'ConstrType', 'conname': 'char*', 'deferrable': 'bool', 'initdeferred': 'bool', 'location': 'int', 'is_no_inherit': 'bool', 'raw_expr': 'Node*', 'cooked_expr': 'char*', 'generated_when': 'char', 'keys': 'List*', 'including': 'List*', 'exclusions': 'List*', 'options': 'List*', 'indexname': 'char*', 'indexspace': 'char*', 'reset_default_tblspc': 'bool', 'access_method': 'char*', 'where_clause': 'Node*', 'pktable': 'RangeVar*', 'fk_attrs': 'List*', 'pk_attrs': 'List*', 'fk_matchtype': 'char', 'fk_upd_action': 'char', 'fk_del_action': 'char', 'old_conpfeqop': 'List*', 'skip_validation': 'bool', 'initially_valid': 'bool'}  # noqa: E501

    def __init__(self, contype=None, conname=None, deferrable=None, initdeferred=None, location=None, is_no_inherit=None, raw_expr=None, cooked_expr=None, generated_when=None, keys=None, including=None, exclusions=None, options=None, indexname=None, indexspace=None, reset_default_tblspc=None, access_method=None, where_clause=None, pktable=None, fk_attrs=None, pk_attrs=None, fk_matchtype=None, fk_upd_action=None, fk_del_action=None, old_conpfeqop=None, skip_validation=None, initially_valid=None):  # pragma: no cover  # noqa: E501
        if ((contype is not None
             and conname is deferrable is initdeferred is location is is_no_inherit is raw_expr is cooked_expr is generated_when is keys is including is exclusions is options is indexname is indexspace is reset_default_tblspc is access_method is where_clause is pktable is fk_attrs is pk_attrs is fk_matchtype is fk_upd_action is fk_del_action is old_conpfeqop is skip_validation is initially_valid is None  # noqa: E501
             and isinstance(contype, dict)
             and '@' in contype)):
            super().__init__(contype)
        else:
            self.contype = contype
            self.conname = conname
            self.deferrable = deferrable
            self.initdeferred = initdeferred
            self.location = location
            self.is_no_inherit = is_no_inherit
            self.raw_expr = raw_expr
            self.cooked_expr = cooked_expr
            self.generated_when = generated_when
            self.keys = keys
            self.including = including
            self.exclusions = exclusions
            self.options = options
            self.indexname = indexname
            self.indexspace = indexspace
            self.reset_default_tblspc = reset_default_tblspc
            self.access_method = access_method
            self.where_clause = where_clause
            self.pktable = pktable
            self.fk_attrs = fk_attrs
            self.pk_attrs = pk_attrs
            self.fk_matchtype = fk_matchtype
            self.fk_upd_action = fk_upd_action
            self.fk_del_action = fk_del_action
            self.old_conpfeqop = old_conpfeqop
            self.skip_validation = skip_validation
            self.initially_valid = initially_valid


class ConstraintsSetStmt(Node):
    __slots__ = {'constraints': 'List*', 'deferred': 'bool'}  # noqa: E501

    def __init__(self, constraints=None, deferred=None):  # pragma: no cover  # noqa: E501
        if ((constraints is not None
             and deferred is None  # noqa: E501
             and isinstance(constraints, dict)
             and '@' in constraints)):
            super().__init__(constraints)
        else:
            self.constraints = constraints
            self.deferred = deferred


class ConvertRowtypeExpr(Expr):
    __slots__ = {'arg': 'Expr*', 'convertformat': 'CoercionForm', 'location': 'int'}  # noqa: E501

    _ATTRS_TO_IGNORE_IN_COMPARISON = Expr._ATTRS_TO_IGNORE_IN_COMPARISON | {'convertformat'}

    def __init__(self, arg=None, convertformat=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and convertformat is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.convertformat = convertformat
            self.location = location


class CopyStmt(Node):
    __slots__ = {'relation': 'RangeVar*', 'query': 'Node*', 'attlist': 'List*', 'is_from': 'bool', 'is_program': 'bool', 'filename': 'char*', 'options': 'List*', 'whereClause': 'Node*'}  # noqa: E501

    def __init__(self, relation=None, query=None, attlist=None, is_from=None, is_program=None, filename=None, options=None, whereClause=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and query is attlist is is_from is is_program is filename is options is whereClause is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.query = query
            self.attlist = attlist
            self.is_from = is_from
            self.is_program = is_program
            self.filename = filename
            self.options = options
            self.whereClause = whereClause


class CreateAmStmt(Node):
    __slots__ = {'amname': 'char*', 'handler_name': 'List*', 'amtype': 'char'}  # noqa: E501

    def __init__(self, amname=None, handler_name=None, amtype=None):  # pragma: no cover  # noqa: E501
        if ((amname is not None
             and handler_name is amtype is None  # noqa: E501
             and isinstance(amname, dict)
             and '@' in amname)):
            super().__init__(amname)
        else:
            self.amname = amname
            self.handler_name = handler_name
            self.amtype = amtype


class CreateCastStmt(Node):
    __slots__ = {'sourcetype': 'TypeName*', 'targettype': 'TypeName*', 'func': 'ObjectWithArgs*', 'context': 'CoercionContext', 'inout': 'bool'}  # noqa: E501

    def __init__(self, sourcetype=None, targettype=None, func=None, context=None, inout=None):  # pragma: no cover  # noqa: E501
        if ((sourcetype is not None
             and targettype is func is context is inout is None  # noqa: E501
             and isinstance(sourcetype, dict)
             and '@' in sourcetype)):
            super().__init__(sourcetype)
        else:
            self.sourcetype = sourcetype
            self.targettype = targettype
            self.func = func
            self.context = context
            self.inout = inout


class CreateConversionStmt(Node):
    __slots__ = {'conversion_name': 'List*', 'for_encoding_name': 'char*', 'to_encoding_name': 'char*', 'func_name': 'List*', 'def_': 'bool'}  # noqa: E501

    def __init__(self, conversion_name=None, for_encoding_name=None, to_encoding_name=None, func_name=None, def_=None):  # pragma: no cover  # noqa: E501
        if ((conversion_name is not None
             and for_encoding_name is to_encoding_name is func_name is def_ is None  # noqa: E501
             and isinstance(conversion_name, dict)
             and '@' in conversion_name)):
            super().__init__(conversion_name)
        else:
            self.conversion_name = conversion_name
            self.for_encoding_name = for_encoding_name
            self.to_encoding_name = to_encoding_name
            self.func_name = func_name
            self.def_ = def_


class CreateDomainStmt(Node):
    __slots__ = {'domainname': 'List*', 'typeName': 'TypeName*', 'collClause': 'CollateClause*', 'constraints': 'List*'}  # noqa: E501

    def __init__(self, domainname=None, typeName=None, collClause=None, constraints=None):  # pragma: no cover  # noqa: E501
        if ((domainname is not None
             and typeName is collClause is constraints is None  # noqa: E501
             and isinstance(domainname, dict)
             and '@' in domainname)):
            super().__init__(domainname)
        else:
            self.domainname = domainname
            self.typeName = typeName
            self.collClause = collClause
            self.constraints = constraints


class CreateEnumStmt(Node):
    __slots__ = {'typeName': 'List*', 'vals': 'List*'}  # noqa: E501

    def __init__(self, typeName=None, vals=None):  # pragma: no cover  # noqa: E501
        if ((typeName is not None
             and vals is None  # noqa: E501
             and isinstance(typeName, dict)
             and '@' in typeName)):
            super().__init__(typeName)
        else:
            self.typeName = typeName
            self.vals = vals


class CreateEventTrigStmt(Node):
    __slots__ = {'trigname': 'char*', 'eventname': 'char*', 'whenclause': 'List*', 'funcname': 'List*'}  # noqa: E501

    def __init__(self, trigname=None, eventname=None, whenclause=None, funcname=None):  # pragma: no cover  # noqa: E501
        if ((trigname is not None
             and eventname is whenclause is funcname is None  # noqa: E501
             and isinstance(trigname, dict)
             and '@' in trigname)):
            super().__init__(trigname)
        else:
            self.trigname = trigname
            self.eventname = eventname
            self.whenclause = whenclause
            self.funcname = funcname


class CreateExtensionStmt(Node):
    __slots__ = {'extname': 'char*', 'if_not_exists': 'bool', 'options': 'List*'}  # noqa: E501

    def __init__(self, extname=None, if_not_exists=None, options=None):  # pragma: no cover  # noqa: E501
        if ((extname is not None
             and if_not_exists is options is None  # noqa: E501
             and isinstance(extname, dict)
             and '@' in extname)):
            super().__init__(extname)
        else:
            self.extname = extname
            self.if_not_exists = if_not_exists
            self.options = options


class CreateFdwStmt(Node):
    __slots__ = {'fdwname': 'char*', 'func_options': 'List*', 'options': 'List*'}  # noqa: E501

    def __init__(self, fdwname=None, func_options=None, options=None):  # pragma: no cover  # noqa: E501
        if ((fdwname is not None
             and func_options is options is None  # noqa: E501
             and isinstance(fdwname, dict)
             and '@' in fdwname)):
            super().__init__(fdwname)
        else:
            self.fdwname = fdwname
            self.func_options = func_options
            self.options = options


class CreateForeignServerStmt(Node):
    __slots__ = {'servername': 'char*', 'servertype': 'char*', 'version': 'char*', 'fdwname': 'char*', 'if_not_exists': 'bool', 'options': 'List*'}  # noqa: E501

    def __init__(self, servername=None, servertype=None, version=None, fdwname=None, if_not_exists=None, options=None):  # pragma: no cover  # noqa: E501
        if ((servername is not None
             and servertype is version is fdwname is if_not_exists is options is None  # noqa: E501
             and isinstance(servername, dict)
             and '@' in servername)):
            super().__init__(servername)
        else:
            self.servername = servername
            self.servertype = servertype
            self.version = version
            self.fdwname = fdwname
            self.if_not_exists = if_not_exists
            self.options = options


class CreateForeignTableStmt(Node):
    __slots__ = {'base': 'CreateStmt', 'servername': 'char*', 'options': 'List*'}  # noqa: E501

    def __init__(self, base=None, servername=None, options=None):  # pragma: no cover  # noqa: E501
        if ((base is not None
             and servername is options is None  # noqa: E501
             and isinstance(base, dict)
             and '@' in base)):
            super().__init__(base)
        else:
            self.base = base
            self.servername = servername
            self.options = options


class CreateFunctionStmt(Node):
    __slots__ = {'is_procedure': 'bool', 'replace': 'bool', 'funcname': 'List*', 'parameters': 'List*', 'returnType': 'TypeName*', 'options': 'List*', 'sql_body': 'Node*'}  # noqa: E501

    def __init__(self, is_procedure=None, replace=None, funcname=None, parameters=None, returnType=None, options=None, sql_body=None):  # pragma: no cover  # noqa: E501
        if ((is_procedure is not None
             and replace is funcname is parameters is returnType is options is sql_body is None  # noqa: E501
             and isinstance(is_procedure, dict)
             and '@' in is_procedure)):
            super().__init__(is_procedure)
        else:
            self.is_procedure = is_procedure
            self.replace = replace
            self.funcname = funcname
            self.parameters = parameters
            self.returnType = returnType
            self.options = options
            self.sql_body = sql_body


class CreateOpClassItem(Node):
    __slots__ = {'itemtype': 'int', 'name': 'ObjectWithArgs*', 'number': 'int', 'order_family': 'List*', 'class_args': 'List*', 'storedtype': 'TypeName*'}  # noqa: E501

    def __init__(self, itemtype=None, name=None, number=None, order_family=None, class_args=None, storedtype=None):  # pragma: no cover  # noqa: E501
        if ((itemtype is not None
             and name is number is order_family is class_args is storedtype is None  # noqa: E501
             and isinstance(itemtype, dict)
             and '@' in itemtype)):
            super().__init__(itemtype)
        else:
            self.itemtype = itemtype
            self.name = name
            self.number = number
            self.order_family = order_family
            self.class_args = class_args
            self.storedtype = storedtype


class CreateOpClassStmt(Node):
    __slots__ = {'opclassname': 'List*', 'opfamilyname': 'List*', 'amname': 'char*', 'datatype': 'TypeName*', 'items': 'List*', 'isDefault': 'bool'}  # noqa: E501

    def __init__(self, opclassname=None, opfamilyname=None, amname=None, datatype=None, items=None, isDefault=None):  # pragma: no cover  # noqa: E501
        if ((opclassname is not None
             and opfamilyname is amname is datatype is items is isDefault is None  # noqa: E501
             and isinstance(opclassname, dict)
             and '@' in opclassname)):
            super().__init__(opclassname)
        else:
            self.opclassname = opclassname
            self.opfamilyname = opfamilyname
            self.amname = amname
            self.datatype = datatype
            self.items = items
            self.isDefault = isDefault


class CreateOpFamilyStmt(Node):
    __slots__ = {'opfamilyname': 'List*', 'amname': 'char*'}  # noqa: E501

    def __init__(self, opfamilyname=None, amname=None):  # pragma: no cover  # noqa: E501
        if ((opfamilyname is not None
             and amname is None  # noqa: E501
             and isinstance(opfamilyname, dict)
             and '@' in opfamilyname)):
            super().__init__(opfamilyname)
        else:
            self.opfamilyname = opfamilyname
            self.amname = amname


class CreatePLangStmt(Node):
    __slots__ = {'replace': 'bool', 'plname': 'char*', 'plhandler': 'List*', 'plinline': 'List*', 'plvalidator': 'List*', 'pltrusted': 'bool'}  # noqa: E501

    def __init__(self, replace=None, plname=None, plhandler=None, plinline=None, plvalidator=None, pltrusted=None):  # pragma: no cover  # noqa: E501
        if ((replace is not None
             and plname is plhandler is plinline is plvalidator is pltrusted is None  # noqa: E501
             and isinstance(replace, dict)
             and '@' in replace)):
            super().__init__(replace)
        else:
            self.replace = replace
            self.plname = plname
            self.plhandler = plhandler
            self.plinline = plinline
            self.plvalidator = plvalidator
            self.pltrusted = pltrusted


class CreatePolicyStmt(Node):
    __slots__ = {'policy_name': 'char*', 'table': 'RangeVar*', 'cmd_name': 'char*', 'permissive': 'bool', 'roles': 'List*', 'qual': 'Node*', 'with_check': 'Node*'}  # noqa: E501

    def __init__(self, policy_name=None, table=None, cmd_name=None, permissive=None, roles=None, qual=None, with_check=None):  # pragma: no cover  # noqa: E501
        if ((policy_name is not None
             and table is cmd_name is permissive is roles is qual is with_check is None  # noqa: E501
             and isinstance(policy_name, dict)
             and '@' in policy_name)):
            super().__init__(policy_name)
        else:
            self.policy_name = policy_name
            self.table = table
            self.cmd_name = cmd_name
            self.permissive = permissive
            self.roles = roles
            self.qual = qual
            self.with_check = with_check


class CreatePublicationStmt(Node):
    __slots__ = {'pubname': 'char*', 'options': 'List*', 'tables': 'List*', 'for_all_tables': 'bool'}  # noqa: E501

    def __init__(self, pubname=None, options=None, tables=None, for_all_tables=None):  # pragma: no cover  # noqa: E501
        if ((pubname is not None
             and options is tables is for_all_tables is None  # noqa: E501
             and isinstance(pubname, dict)
             and '@' in pubname)):
            super().__init__(pubname)
        else:
            self.pubname = pubname
            self.options = options
            self.tables = tables
            self.for_all_tables = for_all_tables


class CreateRangeStmt(Node):
    __slots__ = {'typeName': 'List*', 'params': 'List*'}  # noqa: E501

    def __init__(self, typeName=None, params=None):  # pragma: no cover  # noqa: E501
        if ((typeName is not None
             and params is None  # noqa: E501
             and isinstance(typeName, dict)
             and '@' in typeName)):
            super().__init__(typeName)
        else:
            self.typeName = typeName
            self.params = params


class CreateRoleStmt(Node):
    __slots__ = {'stmt_type': 'RoleStmtType', 'role': 'char*', 'options': 'List*'}  # noqa: E501

    def __init__(self, stmt_type=None, role=None, options=None):  # pragma: no cover  # noqa: E501
        if ((stmt_type is not None
             and role is options is None  # noqa: E501
             and isinstance(stmt_type, dict)
             and '@' in stmt_type)):
            super().__init__(stmt_type)
        else:
            self.stmt_type = stmt_type
            self.role = role
            self.options = options


class CreateSchemaStmt(Node):
    __slots__ = {'schemaname': 'char*', 'authrole': 'RoleSpec*', 'schemaElts': 'List*', 'if_not_exists': 'bool'}  # noqa: E501

    def __init__(self, schemaname=None, authrole=None, schemaElts=None, if_not_exists=None):  # pragma: no cover  # noqa: E501
        if ((schemaname is not None
             and authrole is schemaElts is if_not_exists is None  # noqa: E501
             and isinstance(schemaname, dict)
             and '@' in schemaname)):
            super().__init__(schemaname)
        else:
            self.schemaname = schemaname
            self.authrole = authrole
            self.schemaElts = schemaElts
            self.if_not_exists = if_not_exists


class CreateSeqStmt(Node):
    __slots__ = {'sequence': 'RangeVar*', 'options': 'List*', 'for_identity': 'bool', 'if_not_exists': 'bool'}  # noqa: E501

    def __init__(self, sequence=None, options=None, for_identity=None, if_not_exists=None):  # pragma: no cover  # noqa: E501
        if ((sequence is not None
             and options is for_identity is if_not_exists is None  # noqa: E501
             and isinstance(sequence, dict)
             and '@' in sequence)):
            super().__init__(sequence)
        else:
            self.sequence = sequence
            self.options = options
            self.for_identity = for_identity
            self.if_not_exists = if_not_exists


class CreateStatsStmt(Node):
    __slots__ = {'defnames': 'List*', 'stat_types': 'List*', 'exprs': 'List*', 'relations': 'List*', 'stxcomment': 'char*', 'transformed': 'bool', 'if_not_exists': 'bool'}  # noqa: E501

    def __init__(self, defnames=None, stat_types=None, exprs=None, relations=None, stxcomment=None, transformed=None, if_not_exists=None):  # pragma: no cover  # noqa: E501
        if ((defnames is not None
             and stat_types is exprs is relations is stxcomment is transformed is if_not_exists is None  # noqa: E501
             and isinstance(defnames, dict)
             and '@' in defnames)):
            super().__init__(defnames)
        else:
            self.defnames = defnames
            self.stat_types = stat_types
            self.exprs = exprs
            self.relations = relations
            self.stxcomment = stxcomment
            self.transformed = transformed
            self.if_not_exists = if_not_exists


class CreateStmt(Node):
    __slots__ = {'relation': 'RangeVar*', 'tableElts': 'List*', 'inhRelations': 'List*', 'partbound': 'PartitionBoundSpec*', 'partspec': 'PartitionSpec*', 'ofTypename': 'TypeName*', 'constraints': 'List*', 'options': 'List*', 'oncommit': 'OnCommitAction', 'tablespacename': 'char*', 'accessMethod': 'char*', 'if_not_exists': 'bool'}  # noqa: E501

    def __init__(self, relation=None, tableElts=None, inhRelations=None, partbound=None, partspec=None, ofTypename=None, constraints=None, options=None, oncommit=None, tablespacename=None, accessMethod=None, if_not_exists=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and tableElts is inhRelations is partbound is partspec is ofTypename is constraints is options is oncommit is tablespacename is accessMethod is if_not_exists is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.tableElts = tableElts
            self.inhRelations = inhRelations
            self.partbound = partbound
            self.partspec = partspec
            self.ofTypename = ofTypename
            self.constraints = constraints
            self.options = options
            self.oncommit = oncommit
            self.tablespacename = tablespacename
            self.accessMethod = accessMethod
            self.if_not_exists = if_not_exists


class CreateSubscriptionStmt(Node):
    __slots__ = {'subname': 'char*', 'conninfo': 'char*', 'publication': 'List*', 'options': 'List*'}  # noqa: E501

    def __init__(self, subname=None, conninfo=None, publication=None, options=None):  # pragma: no cover  # noqa: E501
        if ((subname is not None
             and conninfo is publication is options is None  # noqa: E501
             and isinstance(subname, dict)
             and '@' in subname)):
            super().__init__(subname)
        else:
            self.subname = subname
            self.conninfo = conninfo
            self.publication = publication
            self.options = options


class CreateTableAsStmt(Node):
    __slots__ = {'query': 'Node*', 'into': 'IntoClause*', 'objtype': 'ObjectType', 'is_select_into': 'bool', 'if_not_exists': 'bool'}  # noqa: E501

    def __init__(self, query=None, into=None, objtype=None, is_select_into=None, if_not_exists=None):  # pragma: no cover  # noqa: E501
        if ((query is not None
             and into is objtype is is_select_into is if_not_exists is None  # noqa: E501
             and isinstance(query, dict)
             and '@' in query)):
            super().__init__(query)
        else:
            self.query = query
            self.into = into
            self.objtype = objtype
            self.is_select_into = is_select_into
            self.if_not_exists = if_not_exists


class CreateTableSpaceStmt(Node):
    __slots__ = {'tablespacename': 'char*', 'owner': 'RoleSpec*', 'location': 'char*', 'options': 'List*'}  # noqa: E501

    def __init__(self, tablespacename=None, owner=None, location=None, options=None):  # pragma: no cover  # noqa: E501
        if ((tablespacename is not None
             and owner is location is options is None  # noqa: E501
             and isinstance(tablespacename, dict)
             and '@' in tablespacename)):
            super().__init__(tablespacename)
        else:
            self.tablespacename = tablespacename
            self.owner = owner
            self.location = location
            self.options = options


class CreateTransformStmt(Node):
    __slots__ = {'replace': 'bool', 'type_name': 'TypeName*', 'lang': 'char*', 'fromsql': 'ObjectWithArgs*', 'tosql': 'ObjectWithArgs*'}  # noqa: E501

    def __init__(self, replace=None, type_name=None, lang=None, fromsql=None, tosql=None):  # pragma: no cover  # noqa: E501
        if ((replace is not None
             and type_name is lang is fromsql is tosql is None  # noqa: E501
             and isinstance(replace, dict)
             and '@' in replace)):
            super().__init__(replace)
        else:
            self.replace = replace
            self.type_name = type_name
            self.lang = lang
            self.fromsql = fromsql
            self.tosql = tosql


class CreateTrigStmt(Node):
    __slots__ = {'replace': 'bool', 'isconstraint': 'bool', 'trigname': 'char*', 'relation': 'RangeVar*', 'funcname': 'List*', 'args': 'List*', 'row': 'bool', 'timing': 'int16', 'events': 'int16', 'columns': 'List*', 'whenClause': 'Node*', 'transitionRels': 'List*', 'deferrable': 'bool', 'initdeferred': 'bool', 'constrrel': 'RangeVar*'}  # noqa: E501

    def __init__(self, replace=None, isconstraint=None, trigname=None, relation=None, funcname=None, args=None, row=None, timing=None, events=None, columns=None, whenClause=None, transitionRels=None, deferrable=None, initdeferred=None, constrrel=None):  # pragma: no cover  # noqa: E501
        if ((replace is not None
             and isconstraint is trigname is relation is funcname is args is row is timing is events is columns is whenClause is transitionRels is deferrable is initdeferred is constrrel is None  # noqa: E501
             and isinstance(replace, dict)
             and '@' in replace)):
            super().__init__(replace)
        else:
            self.replace = replace
            self.isconstraint = isconstraint
            self.trigname = trigname
            self.relation = relation
            self.funcname = funcname
            self.args = args
            self.row = row
            self.timing = timing
            self.events = events
            self.columns = columns
            self.whenClause = whenClause
            self.transitionRels = transitionRels
            self.deferrable = deferrable
            self.initdeferred = initdeferred
            self.constrrel = constrrel


class CreateUserMappingStmt(Node):
    __slots__ = {'user': 'RoleSpec*', 'servername': 'char*', 'if_not_exists': 'bool', 'options': 'List*'}  # noqa: E501

    def __init__(self, user=None, servername=None, if_not_exists=None, options=None):  # pragma: no cover  # noqa: E501
        if ((user is not None
             and servername is if_not_exists is options is None  # noqa: E501
             and isinstance(user, dict)
             and '@' in user)):
            super().__init__(user)
        else:
            self.user = user
            self.servername = servername
            self.if_not_exists = if_not_exists
            self.options = options


class CreatedbStmt(Node):
    __slots__ = {'dbname': 'char*', 'options': 'List*'}  # noqa: E501

    def __init__(self, dbname=None, options=None):  # pragma: no cover  # noqa: E501
        if ((dbname is not None
             and options is None  # noqa: E501
             and isinstance(dbname, dict)
             and '@' in dbname)):
            super().__init__(dbname)
        else:
            self.dbname = dbname
            self.options = options


class CurrentOfExpr(Expr):
    __slots__ = {'cvarno': 'Index', 'cursor_name': 'char*', 'cursor_param': 'int'}  # noqa: E501

    def __init__(self, cvarno=None, cursor_name=None, cursor_param=None):  # pragma: no cover  # noqa: E501
        if ((cvarno is not None
             and cursor_name is cursor_param is None  # noqa: E501
             and isinstance(cvarno, dict)
             and '@' in cvarno)):
            super().__init__(cvarno)
        else:
            self.cvarno = cvarno
            self.cursor_name = cursor_name
            self.cursor_param = cursor_param


class DeallocateStmt(Node):
    __slots__ = {'name': 'char*'}  # noqa: E501

    def __init__(self, name=None):  # pragma: no cover  # noqa: E501

        if ((name is not None
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name


class DeclareCursorStmt(Node):
    __slots__ = {'portalname': 'char*', 'options': 'int', 'query': 'Node*'}  # noqa: E501

    def __init__(self, portalname=None, options=None, query=None):  # pragma: no cover  # noqa: E501
        if ((portalname is not None
             and options is query is None  # noqa: E501
             and isinstance(portalname, dict)
             and '@' in portalname)):
            super().__init__(portalname)
        else:
            self.portalname = portalname
            self.options = options
            self.query = query


class DefElem(Node):
    __slots__ = {'defnamespace': 'char*', 'defname': 'char*', 'arg': 'Node*', 'defaction': 'DefElemAction', 'location': 'int'}  # noqa: E501

    def __init__(self, defnamespace=None, defname=None, arg=None, defaction=None, location=None):  # pragma: no cover  # noqa: E501
        if ((defnamespace is not None
             and defname is arg is defaction is location is None  # noqa: E501
             and isinstance(defnamespace, dict)
             and '@' in defnamespace)):
            super().__init__(defnamespace)
        else:
            self.defnamespace = defnamespace
            self.defname = defname
            self.arg = arg
            self.defaction = defaction
            self.location = location


class DefineStmt(Node):
    __slots__ = {'kind': 'ObjectType', 'oldstyle': 'bool', 'defnames': 'List*', 'args': 'List*', 'definition': 'List*', 'if_not_exists': 'bool', 'replace': 'bool'}  # noqa: E501

    def __init__(self, kind=None, oldstyle=None, defnames=None, args=None, definition=None, if_not_exists=None, replace=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and oldstyle is defnames is args is definition is if_not_exists is replace is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.oldstyle = oldstyle
            self.defnames = defnames
            self.args = args
            self.definition = definition
            self.if_not_exists = if_not_exists
            self.replace = replace


class DeleteStmt(Node):
    __slots__ = {'relation': 'RangeVar*', 'usingClause': 'List*', 'whereClause': 'Node*', 'returningList': 'List*', 'withClause': 'WithClause*'}  # noqa: E501

    def __init__(self, relation=None, usingClause=None, whereClause=None, returningList=None, withClause=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and usingClause is whereClause is returningList is withClause is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.usingClause = usingClause
            self.whereClause = whereClause
            self.returningList = returningList
            self.withClause = withClause


class DiscardStmt(Node):
    __slots__ = {'target': 'DiscardMode'}  # noqa: E501

    def __init__(self, target=None):  # pragma: no cover  # noqa: E501

        if ((target is not None
             and isinstance(target, dict)
             and '@' in target)):
            super().__init__(target)
        else:
            self.target = target


class DoStmt(Node):
    __slots__ = {'args': 'List*'}  # noqa: E501

    def __init__(self, args=None):  # pragma: no cover  # noqa: E501

        if ((args is not None
             and isinstance(args, dict)
             and '@' in args)):
            super().__init__(args)
        else:
            self.args = args


class DropOwnedStmt(Node):
    __slots__ = {'roles': 'List*', 'behavior': 'DropBehavior'}  # noqa: E501

    def __init__(self, roles=None, behavior=None):  # pragma: no cover  # noqa: E501
        if ((roles is not None
             and behavior is None  # noqa: E501
             and isinstance(roles, dict)
             and '@' in roles)):
            super().__init__(roles)
        else:
            self.roles = roles
            self.behavior = behavior


class DropRoleStmt(Node):
    __slots__ = {'roles': 'List*', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, roles=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((roles is not None
             and missing_ok is None  # noqa: E501
             and isinstance(roles, dict)
             and '@' in roles)):
            super().__init__(roles)
        else:
            self.roles = roles
            self.missing_ok = missing_ok


class DropStmt(Node):
    __slots__ = {'objects': 'List*', 'removeType': 'ObjectType', 'behavior': 'DropBehavior', 'missing_ok': 'bool', 'concurrent': 'bool'}  # noqa: E501

    def __init__(self, objects=None, removeType=None, behavior=None, missing_ok=None, concurrent=None):  # pragma: no cover  # noqa: E501
        if ((objects is not None
             and removeType is behavior is missing_ok is concurrent is None  # noqa: E501
             and isinstance(objects, dict)
             and '@' in objects)):
            super().__init__(objects)
        else:
            self.objects = objects
            self.removeType = removeType
            self.behavior = behavior
            self.missing_ok = missing_ok
            self.concurrent = concurrent


class DropSubscriptionStmt(Node):
    __slots__ = {'subname': 'char*', 'missing_ok': 'bool', 'behavior': 'DropBehavior'}  # noqa: E501

    def __init__(self, subname=None, missing_ok=None, behavior=None):  # pragma: no cover  # noqa: E501
        if ((subname is not None
             and missing_ok is behavior is None  # noqa: E501
             and isinstance(subname, dict)
             and '@' in subname)):
            super().__init__(subname)
        else:
            self.subname = subname
            self.missing_ok = missing_ok
            self.behavior = behavior


class DropTableSpaceStmt(Node):
    __slots__ = {'tablespacename': 'char*', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, tablespacename=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((tablespacename is not None
             and missing_ok is None  # noqa: E501
             and isinstance(tablespacename, dict)
             and '@' in tablespacename)):
            super().__init__(tablespacename)
        else:
            self.tablespacename = tablespacename
            self.missing_ok = missing_ok


class DropUserMappingStmt(Node):
    __slots__ = {'user': 'RoleSpec*', 'servername': 'char*', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, user=None, servername=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((user is not None
             and servername is missing_ok is None  # noqa: E501
             and isinstance(user, dict)
             and '@' in user)):
            super().__init__(user)
        else:
            self.user = user
            self.servername = servername
            self.missing_ok = missing_ok


class DropdbStmt(Node):
    __slots__ = {'dbname': 'char*', 'missing_ok': 'bool', 'options': 'List*'}  # noqa: E501

    def __init__(self, dbname=None, missing_ok=None, options=None):  # pragma: no cover  # noqa: E501
        if ((dbname is not None
             and missing_ok is options is None  # noqa: E501
             and isinstance(dbname, dict)
             and '@' in dbname)):
            super().__init__(dbname)
        else:
            self.dbname = dbname
            self.missing_ok = missing_ok
            self.options = options


class ExecuteStmt(Node):
    __slots__ = {'name': 'char*', 'params': 'List*'}  # noqa: E501

    def __init__(self, name=None, params=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and params is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.params = params


class ExplainStmt(Node):
    __slots__ = {'query': 'Node*', 'options': 'List*'}  # noqa: E501

    def __init__(self, query=None, options=None):  # pragma: no cover  # noqa: E501
        if ((query is not None
             and options is None  # noqa: E501
             and isinstance(query, dict)
             and '@' in query)):
            super().__init__(query)
        else:
            self.query = query
            self.options = options


class FetchStmt(Node):
    __slots__ = {'direction': 'FetchDirection', 'howMany': 'long', 'portalname': 'char*', 'ismove': 'bool'}  # noqa: E501

    def __init__(self, direction=None, howMany=None, portalname=None, ismove=None):  # pragma: no cover  # noqa: E501
        if ((direction is not None
             and howMany is portalname is ismove is None  # noqa: E501
             and isinstance(direction, dict)
             and '@' in direction)):
            super().__init__(direction)
        else:
            self.direction = direction
            self.howMany = howMany
            self.portalname = portalname
            self.ismove = ismove


class FieldSelect(Expr):
    __slots__ = {'arg': 'Expr*', 'fieldnum': 'AttrNumber', 'resulttypmod': 'int32'}  # noqa: E501

    def __init__(self, arg=None, fieldnum=None, resulttypmod=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and fieldnum is resulttypmod is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.fieldnum = fieldnum
            self.resulttypmod = resulttypmod


class FieldStore(Expr):
    __slots__ = {'arg': 'Expr*', 'newvals': 'List*', 'fieldnums': 'List*'}  # noqa: E501

    def __init__(self, arg=None, newvals=None, fieldnums=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and newvals is fieldnums is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.newvals = newvals
            self.fieldnums = fieldnums


class FromExpr(Node):
    __slots__ = {'fromlist': 'List*', 'quals': 'Node*'}  # noqa: E501

    def __init__(self, fromlist=None, quals=None):  # pragma: no cover  # noqa: E501
        if ((fromlist is not None
             and quals is None  # noqa: E501
             and isinstance(fromlist, dict)
             and '@' in fromlist)):
            super().__init__(fromlist)
        else:
            self.fromlist = fromlist
            self.quals = quals


class FuncCall(Node):
    __slots__ = {'funcname': 'List*', 'args': 'List*', 'agg_order': 'List*', 'agg_filter': 'Node*', 'over': 'WindowDef*', 'agg_within_group': 'bool', 'agg_star': 'bool', 'agg_distinct': 'bool', 'func_variadic': 'bool', 'funcformat': 'CoercionForm', 'location': 'int'}  # noqa: E501

    _ATTRS_TO_IGNORE_IN_COMPARISON = Node._ATTRS_TO_IGNORE_IN_COMPARISON | {'funcformat'}

    def __init__(self, funcname=None, args=None, agg_order=None, agg_filter=None, over=None, agg_within_group=None, agg_star=None, agg_distinct=None, func_variadic=None, funcformat=None, location=None):  # pragma: no cover  # noqa: E501
        if ((funcname is not None
             and args is agg_order is agg_filter is over is agg_within_group is agg_star is agg_distinct is func_variadic is funcformat is location is None  # noqa: E501
             and isinstance(funcname, dict)
             and '@' in funcname)):
            super().__init__(funcname)
        else:
            self.funcname = funcname
            self.args = args
            self.agg_order = agg_order
            self.agg_filter = agg_filter
            self.over = over
            self.agg_within_group = agg_within_group
            self.agg_star = agg_star
            self.agg_distinct = agg_distinct
            self.func_variadic = func_variadic
            self.funcformat = funcformat
            self.location = location


class FuncExpr(Expr):
    __slots__ = {'funcretset': 'bool', 'funcvariadic': 'bool', 'funcformat': 'CoercionForm', 'args': 'List*', 'location': 'int'}  # noqa: E501

    _ATTRS_TO_IGNORE_IN_COMPARISON = Expr._ATTRS_TO_IGNORE_IN_COMPARISON | {'funcformat'}

    def __init__(self, funcretset=None, funcvariadic=None, funcformat=None, args=None, location=None):  # pragma: no cover  # noqa: E501
        if ((funcretset is not None
             and funcvariadic is funcformat is args is location is None  # noqa: E501
             and isinstance(funcretset, dict)
             and '@' in funcretset)):
            super().__init__(funcretset)
        else:
            self.funcretset = funcretset
            self.funcvariadic = funcvariadic
            self.funcformat = funcformat
            self.args = args
            self.location = location


class FunctionParameter(Node):
    __slots__ = {'name': 'char*', 'argType': 'TypeName*', 'mode': 'FunctionParameterMode', 'defexpr': 'Node*'}  # noqa: E501

    def __init__(self, name=None, argType=None, mode=None, defexpr=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and argType is mode is defexpr is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.argType = argType
            self.mode = mode
            self.defexpr = defexpr


class GrantRoleStmt(Node):
    __slots__ = {'granted_roles': 'List*', 'grantee_roles': 'List*', 'is_grant': 'bool', 'admin_opt': 'bool', 'grantor': 'RoleSpec*', 'behavior': 'DropBehavior'}  # noqa: E501

    def __init__(self, granted_roles=None, grantee_roles=None, is_grant=None, admin_opt=None, grantor=None, behavior=None):  # pragma: no cover  # noqa: E501
        if ((granted_roles is not None
             and grantee_roles is is_grant is admin_opt is grantor is behavior is None  # noqa: E501
             and isinstance(granted_roles, dict)
             and '@' in granted_roles)):
            super().__init__(granted_roles)
        else:
            self.granted_roles = granted_roles
            self.grantee_roles = grantee_roles
            self.is_grant = is_grant
            self.admin_opt = admin_opt
            self.grantor = grantor
            self.behavior = behavior


class GrantStmt(Node):
    __slots__ = {'is_grant': 'bool', 'targtype': 'GrantTargetType', 'objtype': 'ObjectType', 'objects': 'List*', 'privileges': 'List*', 'grantees': 'List*', 'grant_option': 'bool', 'grantor': 'RoleSpec*', 'behavior': 'DropBehavior'}  # noqa: E501

    def __init__(self, is_grant=None, targtype=None, objtype=None, objects=None, privileges=None, grantees=None, grant_option=None, grantor=None, behavior=None):  # pragma: no cover  # noqa: E501
        if ((is_grant is not None
             and targtype is objtype is objects is privileges is grantees is grant_option is grantor is behavior is None  # noqa: E501
             and isinstance(is_grant, dict)
             and '@' in is_grant)):
            super().__init__(is_grant)
        else:
            self.is_grant = is_grant
            self.targtype = targtype
            self.objtype = objtype
            self.objects = objects
            self.privileges = privileges
            self.grantees = grantees
            self.grant_option = grant_option
            self.grantor = grantor
            self.behavior = behavior


class GroupingFunc(Expr):
    __slots__ = {'args': 'List*', 'refs': 'List*', 'cols': 'List*', 'agglevelsup': 'Index', 'location': 'int'}  # noqa: E501

    def __init__(self, args=None, refs=None, cols=None, agglevelsup=None, location=None):  # pragma: no cover  # noqa: E501
        if ((args is not None
             and refs is cols is agglevelsup is location is None  # noqa: E501
             and isinstance(args, dict)
             and '@' in args)):
            super().__init__(args)
        else:
            self.args = args
            self.refs = refs
            self.cols = cols
            self.agglevelsup = agglevelsup
            self.location = location


class GroupingSet(Node):
    __slots__ = {'kind': 'GroupingSetKind', 'content': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, kind=None, content=None, location=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and content is location is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.content = content
            self.location = location


class ImportForeignSchemaStmt(Node):
    __slots__ = {'server_name': 'char*', 'remote_schema': 'char*', 'local_schema': 'char*', 'list_type': 'ImportForeignSchemaType', 'table_list': 'List*', 'options': 'List*'}  # noqa: E501

    def __init__(self, server_name=None, remote_schema=None, local_schema=None, list_type=None, table_list=None, options=None):  # pragma: no cover  # noqa: E501
        if ((server_name is not None
             and remote_schema is local_schema is list_type is table_list is options is None  # noqa: E501
             and isinstance(server_name, dict)
             and '@' in server_name)):
            super().__init__(server_name)
        else:
            self.server_name = server_name
            self.remote_schema = remote_schema
            self.local_schema = local_schema
            self.list_type = list_type
            self.table_list = table_list
            self.options = options


class IndexElem(Node):
    __slots__ = {'name': 'char*', 'expr': 'Node*', 'indexcolname': 'char*', 'collation': 'List*', 'opclass': 'List*', 'opclassopts': 'List*', 'ordering': 'SortByDir', 'nulls_ordering': 'SortByNulls'}  # noqa: E501

    def __init__(self, name=None, expr=None, indexcolname=None, collation=None, opclass=None, opclassopts=None, ordering=None, nulls_ordering=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and expr is indexcolname is collation is opclass is opclassopts is ordering is nulls_ordering is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.expr = expr
            self.indexcolname = indexcolname
            self.collation = collation
            self.opclass = opclass
            self.opclassopts = opclassopts
            self.ordering = ordering
            self.nulls_ordering = nulls_ordering


class IndexStmt(Node):
    __slots__ = {'idxname': 'char*', 'relation': 'RangeVar*', 'accessMethod': 'char*', 'tableSpace': 'char*', 'indexParams': 'List*', 'indexIncludingParams': 'List*', 'options': 'List*', 'whereClause': 'Node*', 'excludeOpNames': 'List*', 'idxcomment': 'char*', 'oldCreateSubid': 'SubTransactionId', 'oldFirstRelfilenodeSubid': 'SubTransactionId', 'unique': 'bool', 'primary': 'bool', 'isconstraint': 'bool', 'deferrable': 'bool', 'initdeferred': 'bool', 'transformed': 'bool', 'concurrent': 'bool', 'if_not_exists': 'bool', 'reset_default_tblspc': 'bool'}  # noqa: E501

    def __init__(self, idxname=None, relation=None, accessMethod=None, tableSpace=None, indexParams=None, indexIncludingParams=None, options=None, whereClause=None, excludeOpNames=None, idxcomment=None, oldCreateSubid=None, oldFirstRelfilenodeSubid=None, unique=None, primary=None, isconstraint=None, deferrable=None, initdeferred=None, transformed=None, concurrent=None, if_not_exists=None, reset_default_tblspc=None):  # pragma: no cover  # noqa: E501
        if ((idxname is not None
             and relation is accessMethod is tableSpace is indexParams is indexIncludingParams is options is whereClause is excludeOpNames is idxcomment is oldCreateSubid is oldFirstRelfilenodeSubid is unique is primary is isconstraint is deferrable is initdeferred is transformed is concurrent is if_not_exists is reset_default_tblspc is None  # noqa: E501
             and isinstance(idxname, dict)
             and '@' in idxname)):
            super().__init__(idxname)
        else:
            self.idxname = idxname
            self.relation = relation
            self.accessMethod = accessMethod
            self.tableSpace = tableSpace
            self.indexParams = indexParams
            self.indexIncludingParams = indexIncludingParams
            self.options = options
            self.whereClause = whereClause
            self.excludeOpNames = excludeOpNames
            self.idxcomment = idxcomment
            self.oldCreateSubid = oldCreateSubid
            self.oldFirstRelfilenodeSubid = oldFirstRelfilenodeSubid
            self.unique = unique
            self.primary = primary
            self.isconstraint = isconstraint
            self.deferrable = deferrable
            self.initdeferred = initdeferred
            self.transformed = transformed
            self.concurrent = concurrent
            self.if_not_exists = if_not_exists
            self.reset_default_tblspc = reset_default_tblspc


class InferClause(Node):
    __slots__ = {'indexElems': 'List*', 'whereClause': 'Node*', 'conname': 'char*', 'location': 'int'}  # noqa: E501

    def __init__(self, indexElems=None, whereClause=None, conname=None, location=None):  # pragma: no cover  # noqa: E501
        if ((indexElems is not None
             and whereClause is conname is location is None  # noqa: E501
             and isinstance(indexElems, dict)
             and '@' in indexElems)):
            super().__init__(indexElems)
        else:
            self.indexElems = indexElems
            self.whereClause = whereClause
            self.conname = conname
            self.location = location


class InferenceElem(Expr):
    __slots__ = {'expr': 'Node*'}  # noqa: E501

    def __init__(self, expr=None):  # pragma: no cover  # noqa: E501

        if ((expr is not None
             and isinstance(expr, dict)
             and '@' in expr)):
            super().__init__(expr)
        else:
            self.expr = expr


class InlineCodeBlock(Node):
    __slots__ = {'source_text': 'char*', 'langIsTrusted': 'bool', 'atomic': 'bool'}  # noqa: E501

    def __init__(self, source_text=None, langIsTrusted=None, atomic=None):  # pragma: no cover  # noqa: E501
        if ((source_text is not None
             and langIsTrusted is atomic is None  # noqa: E501
             and isinstance(source_text, dict)
             and '@' in source_text)):
            super().__init__(source_text)
        else:
            self.source_text = source_text
            self.langIsTrusted = langIsTrusted
            self.atomic = atomic


class InsertStmt(Node):
    __slots__ = {'relation': 'RangeVar*', 'cols': 'List*', 'selectStmt': 'Node*', 'onConflictClause': 'OnConflictClause*', 'returningList': 'List*', 'withClause': 'WithClause*', 'override': 'OverridingKind'}  # noqa: E501

    def __init__(self, relation=None, cols=None, selectStmt=None, onConflictClause=None, returningList=None, withClause=None, override=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and cols is selectStmt is onConflictClause is returningList is withClause is override is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.cols = cols
            self.selectStmt = selectStmt
            self.onConflictClause = onConflictClause
            self.returningList = returningList
            self.withClause = withClause
            self.override = override


class IntoClause(Node):
    __slots__ = {'rel': 'RangeVar*', 'colNames': 'List*', 'accessMethod': 'char*', 'options': 'List*', 'onCommit': 'OnCommitAction', 'tableSpaceName': 'char*', 'viewQuery': 'Node*', 'skipData': 'bool'}  # noqa: E501

    def __init__(self, rel=None, colNames=None, accessMethod=None, options=None, onCommit=None, tableSpaceName=None, viewQuery=None, skipData=None):  # pragma: no cover  # noqa: E501
        if ((rel is not None
             and colNames is accessMethod is options is onCommit is tableSpaceName is viewQuery is skipData is None  # noqa: E501
             and isinstance(rel, dict)
             and '@' in rel)):
            super().__init__(rel)
        else:
            self.rel = rel
            self.colNames = colNames
            self.accessMethod = accessMethod
            self.options = options
            self.onCommit = onCommit
            self.tableSpaceName = tableSpaceName
            self.viewQuery = viewQuery
            self.skipData = skipData


class JoinExpr(Node):
    __slots__ = {'jointype': 'JoinType', 'isNatural': 'bool', 'larg': 'Node*', 'rarg': 'Node*', 'usingClause': 'List*', 'join_using_alias': 'Alias*', 'quals': 'Node*', 'alias': 'Alias*', 'rtindex': 'int'}  # noqa: E501

    def __init__(self, jointype=None, isNatural=None, larg=None, rarg=None, usingClause=None, join_using_alias=None, quals=None, alias=None, rtindex=None):  # pragma: no cover  # noqa: E501
        if ((jointype is not None
             and isNatural is larg is rarg is usingClause is join_using_alias is quals is alias is rtindex is None  # noqa: E501
             and isinstance(jointype, dict)
             and '@' in jointype)):
            super().__init__(jointype)
        else:
            self.jointype = jointype
            self.isNatural = isNatural
            self.larg = larg
            self.rarg = rarg
            self.usingClause = usingClause
            self.join_using_alias = join_using_alias
            self.quals = quals
            self.alias = alias
            self.rtindex = rtindex


class ListenStmt(Node):
    __slots__ = {'conditionname': 'char*'}  # noqa: E501

    def __init__(self, conditionname=None):  # pragma: no cover  # noqa: E501

        if ((conditionname is not None
             and isinstance(conditionname, dict)
             and '@' in conditionname)):
            super().__init__(conditionname)
        else:
            self.conditionname = conditionname


class LoadStmt(Node):
    __slots__ = {'filename': 'char*'}  # noqa: E501

    def __init__(self, filename=None):  # pragma: no cover  # noqa: E501

        if ((filename is not None
             and isinstance(filename, dict)
             and '@' in filename)):
            super().__init__(filename)
        else:
            self.filename = filename


class LockStmt(Node):
    __slots__ = {'relations': 'List*', 'mode': 'int', 'nowait': 'bool'}  # noqa: E501

    def __init__(self, relations=None, mode=None, nowait=None):  # pragma: no cover  # noqa: E501
        if ((relations is not None
             and mode is nowait is None  # noqa: E501
             and isinstance(relations, dict)
             and '@' in relations)):
            super().__init__(relations)
        else:
            self.relations = relations
            self.mode = mode
            self.nowait = nowait


class LockingClause(Node):
    __slots__ = {'lockedRels': 'List*', 'strength': 'LockClauseStrength', 'waitPolicy': 'LockWaitPolicy'}  # noqa: E501

    def __init__(self, lockedRels=None, strength=None, waitPolicy=None):  # pragma: no cover  # noqa: E501
        if ((lockedRels is not None
             and strength is waitPolicy is None  # noqa: E501
             and isinstance(lockedRels, dict)
             and '@' in lockedRels)):
            super().__init__(lockedRels)
        else:
            self.lockedRels = lockedRels
            self.strength = strength
            self.waitPolicy = waitPolicy


class MinMaxExpr(Expr):
    __slots__ = {'op': 'MinMaxOp', 'args': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, op=None, args=None, location=None):  # pragma: no cover  # noqa: E501
        if ((op is not None
             and args is location is None  # noqa: E501
             and isinstance(op, dict)
             and '@' in op)):
            super().__init__(op)
        else:
            self.op = op
            self.args = args
            self.location = location


class MultiAssignRef(Node):
    __slots__ = {'source': 'Node*', 'colno': 'int', 'ncolumns': 'int'}  # noqa: E501

    def __init__(self, source=None, colno=None, ncolumns=None):  # pragma: no cover  # noqa: E501
        if ((source is not None
             and colno is ncolumns is None  # noqa: E501
             and isinstance(source, dict)
             and '@' in source)):
            super().__init__(source)
        else:
            self.source = source
            self.colno = colno
            self.ncolumns = ncolumns


class NamedArgExpr(Expr):
    __slots__ = {'arg': 'Expr*', 'name': 'char*', 'argnumber': 'int', 'location': 'int'}  # noqa: E501

    def __init__(self, arg=None, name=None, argnumber=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and name is argnumber is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.name = name
            self.argnumber = argnumber
            self.location = location


class NotifyStmt(Node):
    __slots__ = {'conditionname': 'char*', 'payload': 'char*'}  # noqa: E501

    def __init__(self, conditionname=None, payload=None):  # pragma: no cover  # noqa: E501
        if ((conditionname is not None
             and payload is None  # noqa: E501
             and isinstance(conditionname, dict)
             and '@' in conditionname)):
            super().__init__(conditionname)
        else:
            self.conditionname = conditionname
            self.payload = payload


class NullTest(Expr):
    __slots__ = {'arg': 'Expr*', 'nulltesttype': 'NullTestType', 'argisrow': 'bool', 'location': 'int'}  # noqa: E501

    def __init__(self, arg=None, nulltesttype=None, argisrow=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and nulltesttype is argisrow is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.nulltesttype = nulltesttype
            self.argisrow = argisrow
            self.location = location


class ObjectWithArgs(Node):
    __slots__ = {'objname': 'List*', 'objargs': 'List*', 'objfuncargs': 'List*', 'args_unspecified': 'bool'}  # noqa: E501

    def __init__(self, objname=None, objargs=None, objfuncargs=None, args_unspecified=None):  # pragma: no cover  # noqa: E501
        if ((objname is not None
             and objargs is objfuncargs is args_unspecified is None  # noqa: E501
             and isinstance(objname, dict)
             and '@' in objname)):
            super().__init__(objname)
        else:
            self.objname = objname
            self.objargs = objargs
            self.objfuncargs = objfuncargs
            self.args_unspecified = args_unspecified


class OnConflictClause(Node):
    __slots__ = {'action': 'OnConflictAction', 'infer': 'InferClause*', 'targetList': 'List*', 'whereClause': 'Node*', 'location': 'int'}  # noqa: E501

    def __init__(self, action=None, infer=None, targetList=None, whereClause=None, location=None):  # pragma: no cover  # noqa: E501
        if ((action is not None
             and infer is targetList is whereClause is location is None  # noqa: E501
             and isinstance(action, dict)
             and '@' in action)):
            super().__init__(action)
        else:
            self.action = action
            self.infer = infer
            self.targetList = targetList
            self.whereClause = whereClause
            self.location = location


class OnConflictExpr(Node):
    __slots__ = {'action': 'OnConflictAction', 'arbiterElems': 'List*', 'arbiterWhere': 'Node*', 'onConflictSet': 'List*', 'onConflictWhere': 'Node*', 'exclRelIndex': 'int', 'exclRelTlist': 'List*'}  # noqa: E501

    def __init__(self, action=None, arbiterElems=None, arbiterWhere=None, onConflictSet=None, onConflictWhere=None, exclRelIndex=None, exclRelTlist=None):  # pragma: no cover  # noqa: E501
        if ((action is not None
             and arbiterElems is arbiterWhere is onConflictSet is onConflictWhere is exclRelIndex is exclRelTlist is None  # noqa: E501
             and isinstance(action, dict)
             and '@' in action)):
            super().__init__(action)
        else:
            self.action = action
            self.arbiterElems = arbiterElems
            self.arbiterWhere = arbiterWhere
            self.onConflictSet = onConflictSet
            self.onConflictWhere = onConflictWhere
            self.exclRelIndex = exclRelIndex
            self.exclRelTlist = exclRelTlist


class OpExpr(Expr):
    __slots__ = {'opretset': 'bool', 'args': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, opretset=None, args=None, location=None):  # pragma: no cover  # noqa: E501
        if ((opretset is not None
             and args is location is None  # noqa: E501
             and isinstance(opretset, dict)
             and '@' in opretset)):
            super().__init__(opretset)
        else:
            self.opretset = opretset
            self.args = args
            self.location = location


class PLAssignStmt(Node):
    __slots__ = {'name': 'char*', 'indirection': 'List*', 'nnames': 'int', 'val': 'SelectStmt*', 'location': 'int'}  # noqa: E501

    def __init__(self, name=None, indirection=None, nnames=None, val=None, location=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and indirection is nnames is val is location is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.indirection = indirection
            self.nnames = nnames
            self.val = val
            self.location = location


class Param(Expr):
    __slots__ = {'paramkind': 'ParamKind', 'paramid': 'int', 'paramtypmod': 'int32', 'location': 'int'}  # noqa: E501

    def __init__(self, paramkind=None, paramid=None, paramtypmod=None, location=None):  # pragma: no cover  # noqa: E501
        if ((paramkind is not None
             and paramid is paramtypmod is location is None  # noqa: E501
             and isinstance(paramkind, dict)
             and '@' in paramkind)):
            super().__init__(paramkind)
        else:
            self.paramkind = paramkind
            self.paramid = paramid
            self.paramtypmod = paramtypmod
            self.location = location


class ParamRef(Node):
    __slots__ = {'number': 'int', 'location': 'int'}  # noqa: E501

    def __init__(self, number=None, location=None):  # pragma: no cover  # noqa: E501
        if ((number is not None
             and location is None  # noqa: E501
             and isinstance(number, dict)
             and '@' in number)):
            super().__init__(number)
        else:
            self.number = number
            self.location = location


class PartitionBoundSpec(Node):
    __slots__ = {'strategy': 'char', 'is_default': 'bool', 'modulus': 'int', 'remainder': 'int', 'listdatums': 'List*', 'lowerdatums': 'List*', 'upperdatums': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, strategy=None, is_default=None, modulus=None, remainder=None, listdatums=None, lowerdatums=None, upperdatums=None, location=None):  # pragma: no cover  # noqa: E501
        if ((strategy is not None
             and is_default is modulus is remainder is listdatums is lowerdatums is upperdatums is location is None  # noqa: E501
             and isinstance(strategy, dict)
             and '@' in strategy)):
            super().__init__(strategy)
        else:
            self.strategy = strategy
            self.is_default = is_default
            self.modulus = modulus
            self.remainder = remainder
            self.listdatums = listdatums
            self.lowerdatums = lowerdatums
            self.upperdatums = upperdatums
            self.location = location


class PartitionCmd(Node):
    __slots__ = {'name': 'RangeVar*', 'bound': 'PartitionBoundSpec*', 'concurrent': 'bool'}  # noqa: E501

    def __init__(self, name=None, bound=None, concurrent=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and bound is concurrent is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.bound = bound
            self.concurrent = concurrent


class PartitionElem(Node):
    __slots__ = {'name': 'char*', 'expr': 'Node*', 'collation': 'List*', 'opclass': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, name=None, expr=None, collation=None, opclass=None, location=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and expr is collation is opclass is location is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.expr = expr
            self.collation = collation
            self.opclass = opclass
            self.location = location


class PartitionRangeDatum(Node):
    __slots__ = {'kind': 'PartitionRangeDatumKind', 'value': 'Node*', 'location': 'int'}  # noqa: E501

    def __init__(self, kind=None, value=None, location=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and value is location is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.value = value
            self.location = location


class PartitionSpec(Node):
    __slots__ = {'strategy': 'char*', 'partParams': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, strategy=None, partParams=None, location=None):  # pragma: no cover  # noqa: E501
        if ((strategy is not None
             and partParams is location is None  # noqa: E501
             and isinstance(strategy, dict)
             and '@' in strategy)):
            super().__init__(strategy)
        else:
            self.strategy = strategy
            self.partParams = partParams
            self.location = location


class PrepareStmt(Node):
    __slots__ = {'name': 'char*', 'argtypes': 'List*', 'query': 'Node*'}  # noqa: E501

    def __init__(self, name=None, argtypes=None, query=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and argtypes is query is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.argtypes = argtypes
            self.query = query


class Query(Node):
    __slots__ = {'commandType': 'CmdType', 'querySource': 'QuerySource', 'queryId': 'uint64', 'canSetTag': 'bool', 'utilityStmt': 'Node*', 'resultRelation': 'int', 'hasAggs': 'bool', 'hasWindowFuncs': 'bool', 'hasTargetSRFs': 'bool', 'hasSubLinks': 'bool', 'hasDistinctOn': 'bool', 'hasRecursive': 'bool', 'hasModifyingCTE': 'bool', 'hasForUpdate': 'bool', 'hasRowSecurity': 'bool', 'isReturn': 'bool', 'cteList': 'List*', 'rtable': 'List*', 'jointree': 'FromExpr*', 'targetList': 'List*', 'override': 'OverridingKind', 'onConflict': 'OnConflictExpr*', 'returningList': 'List*', 'groupClause': 'List*', 'groupDistinct': 'bool', 'groupingSets': 'List*', 'havingQual': 'Node*', 'windowClause': 'List*', 'distinctClause': 'List*', 'sortClause': 'List*', 'limitOffset': 'Node*', 'limitCount': 'Node*', 'limitOption': 'LimitOption', 'rowMarks': 'List*', 'setOperations': 'Node*', 'constraintDeps': 'List*', 'withCheckOptions': 'List*', 'stmt_location': 'int', 'stmt_len': 'int'}  # noqa: E501

    def __init__(self, commandType=None, querySource=None, queryId=None, canSetTag=None, utilityStmt=None, resultRelation=None, hasAggs=None, hasWindowFuncs=None, hasTargetSRFs=None, hasSubLinks=None, hasDistinctOn=None, hasRecursive=None, hasModifyingCTE=None, hasForUpdate=None, hasRowSecurity=None, isReturn=None, cteList=None, rtable=None, jointree=None, targetList=None, override=None, onConflict=None, returningList=None, groupClause=None, groupDistinct=None, groupingSets=None, havingQual=None, windowClause=None, distinctClause=None, sortClause=None, limitOffset=None, limitCount=None, limitOption=None, rowMarks=None, setOperations=None, constraintDeps=None, withCheckOptions=None, stmt_location=None, stmt_len=None):  # pragma: no cover  # noqa: E501
        if ((commandType is not None
             and querySource is queryId is canSetTag is utilityStmt is resultRelation is hasAggs is hasWindowFuncs is hasTargetSRFs is hasSubLinks is hasDistinctOn is hasRecursive is hasModifyingCTE is hasForUpdate is hasRowSecurity is isReturn is cteList is rtable is jointree is targetList is override is onConflict is returningList is groupClause is groupDistinct is groupingSets is havingQual is windowClause is distinctClause is sortClause is limitOffset is limitCount is limitOption is rowMarks is setOperations is constraintDeps is withCheckOptions is stmt_location is stmt_len is None  # noqa: E501
             and isinstance(commandType, dict)
             and '@' in commandType)):
            super().__init__(commandType)
        else:
            self.commandType = commandType
            self.querySource = querySource
            self.queryId = queryId
            self.canSetTag = canSetTag
            self.utilityStmt = utilityStmt
            self.resultRelation = resultRelation
            self.hasAggs = hasAggs
            self.hasWindowFuncs = hasWindowFuncs
            self.hasTargetSRFs = hasTargetSRFs
            self.hasSubLinks = hasSubLinks
            self.hasDistinctOn = hasDistinctOn
            self.hasRecursive = hasRecursive
            self.hasModifyingCTE = hasModifyingCTE
            self.hasForUpdate = hasForUpdate
            self.hasRowSecurity = hasRowSecurity
            self.isReturn = isReturn
            self.cteList = cteList
            self.rtable = rtable
            self.jointree = jointree
            self.targetList = targetList
            self.override = override
            self.onConflict = onConflict
            self.returningList = returningList
            self.groupClause = groupClause
            self.groupDistinct = groupDistinct
            self.groupingSets = groupingSets
            self.havingQual = havingQual
            self.windowClause = windowClause
            self.distinctClause = distinctClause
            self.sortClause = sortClause
            self.limitOffset = limitOffset
            self.limitCount = limitCount
            self.limitOption = limitOption
            self.rowMarks = rowMarks
            self.setOperations = setOperations
            self.constraintDeps = constraintDeps
            self.withCheckOptions = withCheckOptions
            self.stmt_location = stmt_location
            self.stmt_len = stmt_len


class RangeFunction(Node):
    __slots__ = {'lateral': 'bool', 'ordinality': 'bool', 'is_rowsfrom': 'bool', 'functions': 'List*', 'alias': 'Alias*', 'coldeflist': 'List*'}  # noqa: E501

    def __init__(self, lateral=None, ordinality=None, is_rowsfrom=None, functions=None, alias=None, coldeflist=None):  # pragma: no cover  # noqa: E501
        if ((lateral is not None
             and ordinality is is_rowsfrom is functions is alias is coldeflist is None  # noqa: E501
             and isinstance(lateral, dict)
             and '@' in lateral)):
            super().__init__(lateral)
        else:
            self.lateral = lateral
            self.ordinality = ordinality
            self.is_rowsfrom = is_rowsfrom
            self.functions = functions
            self.alias = alias
            self.coldeflist = coldeflist


class RangeSubselect(Node):
    __slots__ = {'lateral': 'bool', 'subquery': 'Node*', 'alias': 'Alias*'}  # noqa: E501

    def __init__(self, lateral=None, subquery=None, alias=None):  # pragma: no cover  # noqa: E501
        if ((lateral is not None
             and subquery is alias is None  # noqa: E501
             and isinstance(lateral, dict)
             and '@' in lateral)):
            super().__init__(lateral)
        else:
            self.lateral = lateral
            self.subquery = subquery
            self.alias = alias


class RangeTableFunc(Node):
    __slots__ = {'lateral': 'bool', 'docexpr': 'Node*', 'rowexpr': 'Node*', 'namespaces': 'List*', 'columns': 'List*', 'alias': 'Alias*', 'location': 'int'}  # noqa: E501

    def __init__(self, lateral=None, docexpr=None, rowexpr=None, namespaces=None, columns=None, alias=None, location=None):  # pragma: no cover  # noqa: E501
        if ((lateral is not None
             and docexpr is rowexpr is namespaces is columns is alias is location is None  # noqa: E501
             and isinstance(lateral, dict)
             and '@' in lateral)):
            super().__init__(lateral)
        else:
            self.lateral = lateral
            self.docexpr = docexpr
            self.rowexpr = rowexpr
            self.namespaces = namespaces
            self.columns = columns
            self.alias = alias
            self.location = location


class RangeTableFuncCol(Node):
    __slots__ = {'colname': 'char*', 'typeName': 'TypeName*', 'for_ordinality': 'bool', 'is_not_null': 'bool', 'colexpr': 'Node*', 'coldefexpr': 'Node*', 'location': 'int'}  # noqa: E501

    def __init__(self, colname=None, typeName=None, for_ordinality=None, is_not_null=None, colexpr=None, coldefexpr=None, location=None):  # pragma: no cover  # noqa: E501
        if ((colname is not None
             and typeName is for_ordinality is is_not_null is colexpr is coldefexpr is location is None  # noqa: E501
             and isinstance(colname, dict)
             and '@' in colname)):
            super().__init__(colname)
        else:
            self.colname = colname
            self.typeName = typeName
            self.for_ordinality = for_ordinality
            self.is_not_null = is_not_null
            self.colexpr = colexpr
            self.coldefexpr = coldefexpr
            self.location = location


class RangeTableSample(Node):
    __slots__ = {'relation': 'Node*', 'method': 'List*', 'args': 'List*', 'repeatable': 'Node*', 'location': 'int'}  # noqa: E501

    def __init__(self, relation=None, method=None, args=None, repeatable=None, location=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and method is args is repeatable is location is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.method = method
            self.args = args
            self.repeatable = repeatable
            self.location = location


class RangeTblEntry(Node):
    __slots__ = {'rtekind': 'RTEKind', 'relkind': 'char', 'rellockmode': 'int', 'tablesample': 'TableSampleClause*', 'subquery': 'Query*', 'security_barrier': 'bool', 'jointype': 'JoinType', 'joinmergedcols': 'int', 'joinaliasvars': 'List*', 'joinleftcols': 'List*', 'joinrightcols': 'List*', 'join_using_alias': 'Alias*', 'functions': 'List*', 'funcordinality': 'bool', 'tablefunc': 'TableFunc*', 'values_lists': 'List*', 'ctename': 'char*', 'ctelevelsup': 'Index', 'self_reference': 'bool', 'coltypes': 'List*', 'coltypmods': 'List*', 'colcollations': 'List*', 'enrname': 'char*', 'enrtuples': 'double', 'alias': 'Alias*', 'eref': 'Alias*', 'lateral': 'bool', 'inh': 'bool', 'inFromCl': 'bool', 'requiredPerms': 'AclMode', 'selectedCols': 'Bitmapset*', 'insertedCols': 'Bitmapset*', 'updatedCols': 'Bitmapset*', 'extraUpdatedCols': 'Bitmapset*', 'securityQuals': 'List*'}  # noqa: E501

    def __init__(self, rtekind=None, relkind=None, rellockmode=None, tablesample=None, subquery=None, security_barrier=None, jointype=None, joinmergedcols=None, joinaliasvars=None, joinleftcols=None, joinrightcols=None, join_using_alias=None, functions=None, funcordinality=None, tablefunc=None, values_lists=None, ctename=None, ctelevelsup=None, self_reference=None, coltypes=None, coltypmods=None, colcollations=None, enrname=None, enrtuples=None, alias=None, eref=None, lateral=None, inh=None, inFromCl=None, requiredPerms=None, selectedCols=None, insertedCols=None, updatedCols=None, extraUpdatedCols=None, securityQuals=None):  # pragma: no cover  # noqa: E501
        if ((rtekind is not None
             and relkind is rellockmode is tablesample is subquery is security_barrier is jointype is joinmergedcols is joinaliasvars is joinleftcols is joinrightcols is join_using_alias is functions is funcordinality is tablefunc is values_lists is ctename is ctelevelsup is self_reference is coltypes is coltypmods is colcollations is enrname is enrtuples is alias is eref is lateral is inh is inFromCl is requiredPerms is selectedCols is insertedCols is updatedCols is extraUpdatedCols is securityQuals is None  # noqa: E501
             and isinstance(rtekind, dict)
             and '@' in rtekind)):
            super().__init__(rtekind)
        else:
            self.rtekind = rtekind
            self.relkind = relkind
            self.rellockmode = rellockmode
            self.tablesample = tablesample
            self.subquery = subquery
            self.security_barrier = security_barrier
            self.jointype = jointype
            self.joinmergedcols = joinmergedcols
            self.joinaliasvars = joinaliasvars
            self.joinleftcols = joinleftcols
            self.joinrightcols = joinrightcols
            self.join_using_alias = join_using_alias
            self.functions = functions
            self.funcordinality = funcordinality
            self.tablefunc = tablefunc
            self.values_lists = values_lists
            self.ctename = ctename
            self.ctelevelsup = ctelevelsup
            self.self_reference = self_reference
            self.coltypes = coltypes
            self.coltypmods = coltypmods
            self.colcollations = colcollations
            self.enrname = enrname
            self.enrtuples = enrtuples
            self.alias = alias
            self.eref = eref
            self.lateral = lateral
            self.inh = inh
            self.inFromCl = inFromCl
            self.requiredPerms = requiredPerms
            self.selectedCols = selectedCols
            self.insertedCols = insertedCols
            self.updatedCols = updatedCols
            self.extraUpdatedCols = extraUpdatedCols
            self.securityQuals = securityQuals


class RangeTblFunction(Node):
    __slots__ = {'funcexpr': 'Node*', 'funccolcount': 'int', 'funccolnames': 'List*', 'funccoltypes': 'List*', 'funccoltypmods': 'List*', 'funccolcollations': 'List*', 'funcparams': 'Bitmapset*'}  # noqa: E501

    def __init__(self, funcexpr=None, funccolcount=None, funccolnames=None, funccoltypes=None, funccoltypmods=None, funccolcollations=None, funcparams=None):  # pragma: no cover  # noqa: E501
        if ((funcexpr is not None
             and funccolcount is funccolnames is funccoltypes is funccoltypmods is funccolcollations is funcparams is None  # noqa: E501
             and isinstance(funcexpr, dict)
             and '@' in funcexpr)):
            super().__init__(funcexpr)
        else:
            self.funcexpr = funcexpr
            self.funccolcount = funccolcount
            self.funccolnames = funccolnames
            self.funccoltypes = funccoltypes
            self.funccoltypmods = funccoltypmods
            self.funccolcollations = funccolcollations
            self.funcparams = funcparams


class RangeTblRef(Node):
    __slots__ = {'rtindex': 'int'}  # noqa: E501

    def __init__(self, rtindex=None):  # pragma: no cover  # noqa: E501

        if ((rtindex is not None
             and isinstance(rtindex, dict)
             and '@' in rtindex)):
            super().__init__(rtindex)
        else:
            self.rtindex = rtindex


class RangeVar(Node):
    __slots__ = {'catalogname': 'char*', 'schemaname': 'char*', 'relname': 'char*', 'inh': 'bool', 'relpersistence': 'char', 'alias': 'Alias*', 'location': 'int'}  # noqa: E501

    def __init__(self, catalogname=None, schemaname=None, relname=None, inh=None, relpersistence=None, alias=None, location=None):  # pragma: no cover  # noqa: E501
        if ((catalogname is not None
             and schemaname is relname is inh is relpersistence is alias is location is None  # noqa: E501
             and isinstance(catalogname, dict)
             and '@' in catalogname)):
            super().__init__(catalogname)
        else:
            self.catalogname = catalogname
            self.schemaname = schemaname
            self.relname = relname
            self.inh = inh
            self.relpersistence = relpersistence
            self.alias = alias
            self.location = location


class RawStmt(Node):
    __slots__ = {'stmt': 'Node*', 'stmt_location': 'int', 'stmt_len': 'int'}  # noqa: E501

    def __init__(self, stmt=None, stmt_location=None, stmt_len=None):  # pragma: no cover  # noqa: E501
        if ((stmt is not None
             and stmt_location is stmt_len is None  # noqa: E501
             and isinstance(stmt, dict)
             and '@' in stmt)):
            super().__init__(stmt)
        else:
            self.stmt = stmt
            self.stmt_location = stmt_location
            self.stmt_len = stmt_len


class ReassignOwnedStmt(Node):
    __slots__ = {'roles': 'List*', 'newrole': 'RoleSpec*'}  # noqa: E501

    def __init__(self, roles=None, newrole=None):  # pragma: no cover  # noqa: E501
        if ((roles is not None
             and newrole is None  # noqa: E501
             and isinstance(roles, dict)
             and '@' in roles)):
            super().__init__(roles)
        else:
            self.roles = roles
            self.newrole = newrole


class RefreshMatViewStmt(Node):
    __slots__ = {'concurrent': 'bool', 'skipData': 'bool', 'relation': 'RangeVar*'}  # noqa: E501

    def __init__(self, concurrent=None, skipData=None, relation=None):  # pragma: no cover  # noqa: E501
        if ((concurrent is not None
             and skipData is relation is None  # noqa: E501
             and isinstance(concurrent, dict)
             and '@' in concurrent)):
            super().__init__(concurrent)
        else:
            self.concurrent = concurrent
            self.skipData = skipData
            self.relation = relation


class ReindexStmt(Node):
    __slots__ = {'kind': 'ReindexObjectType', 'relation': 'RangeVar*', 'name': 'char*', 'params': 'List*'}  # noqa: E501

    def __init__(self, kind=None, relation=None, name=None, params=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and relation is name is params is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.relation = relation
            self.name = name
            self.params = params


class RelabelType(Expr):
    __slots__ = {'arg': 'Expr*', 'resulttypmod': 'int32', 'relabelformat': 'CoercionForm', 'location': 'int'}  # noqa: E501

    _ATTRS_TO_IGNORE_IN_COMPARISON = Expr._ATTRS_TO_IGNORE_IN_COMPARISON | {'relabelformat'}

    def __init__(self, arg=None, resulttypmod=None, relabelformat=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and resulttypmod is relabelformat is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.resulttypmod = resulttypmod
            self.relabelformat = relabelformat
            self.location = location


class RenameStmt(Node):
    __slots__ = {'renameType': 'ObjectType', 'relationType': 'ObjectType', 'relation': 'RangeVar*', 'object': 'Node*', 'subname': 'char*', 'newname': 'char*', 'behavior': 'DropBehavior', 'missing_ok': 'bool'}  # noqa: E501

    def __init__(self, renameType=None, relationType=None, relation=None, object=None, subname=None, newname=None, behavior=None, missing_ok=None):  # pragma: no cover  # noqa: E501
        if ((renameType is not None
             and relationType is relation is object is subname is newname is behavior is missing_ok is None  # noqa: E501
             and isinstance(renameType, dict)
             and '@' in renameType)):
            super().__init__(renameType)
        else:
            self.renameType = renameType
            self.relationType = relationType
            self.relation = relation
            self.object = object
            self.subname = subname
            self.newname = newname
            self.behavior = behavior
            self.missing_ok = missing_ok


class ReplicaIdentityStmt(Node):
    __slots__ = {'identity_type': 'char', 'name': 'char*'}  # noqa: E501

    def __init__(self, identity_type=None, name=None):  # pragma: no cover  # noqa: E501
        if ((identity_type is not None
             and name is None  # noqa: E501
             and isinstance(identity_type, dict)
             and '@' in identity_type)):
            super().__init__(identity_type)
        else:
            self.identity_type = identity_type
            self.name = name


class ResTarget(Node):
    __slots__ = {'name': 'char*', 'indirection': 'List*', 'val': 'Node*', 'location': 'int'}  # noqa: E501

    def __init__(self, name=None, indirection=None, val=None, location=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and indirection is val is location is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.indirection = indirection
            self.val = val
            self.location = location


class ReturnStmt(Node):
    __slots__ = {'returnval': 'Node*'}  # noqa: E501

    def __init__(self, returnval=None):  # pragma: no cover  # noqa: E501

        if ((returnval is not None
             and isinstance(returnval, dict)
             and '@' in returnval)):
            super().__init__(returnval)
        else:
            self.returnval = returnval


class RoleSpec(Node):
    __slots__ = {'roletype': 'RoleSpecType', 'rolename': 'char*', 'location': 'int'}  # noqa: E501

    def __init__(self, roletype=None, rolename=None, location=None):  # pragma: no cover  # noqa: E501
        if ((roletype is not None
             and rolename is location is None  # noqa: E501
             and isinstance(roletype, dict)
             and '@' in roletype)):
            super().__init__(roletype)
        else:
            self.roletype = roletype
            self.rolename = rolename
            self.location = location


class RowCompareExpr(Expr):
    __slots__ = {'rctype': 'RowCompareType', 'opnos': 'List*', 'opfamilies': 'List*', 'inputcollids': 'List*', 'largs': 'List*', 'rargs': 'List*'}  # noqa: E501

    def __init__(self, rctype=None, opnos=None, opfamilies=None, inputcollids=None, largs=None, rargs=None):  # pragma: no cover  # noqa: E501
        if ((rctype is not None
             and opnos is opfamilies is inputcollids is largs is rargs is None  # noqa: E501
             and isinstance(rctype, dict)
             and '@' in rctype)):
            super().__init__(rctype)
        else:
            self.rctype = rctype
            self.opnos = opnos
            self.opfamilies = opfamilies
            self.inputcollids = inputcollids
            self.largs = largs
            self.rargs = rargs


class RowExpr(Expr):
    __slots__ = {'args': 'List*', 'row_format': 'CoercionForm', 'colnames': 'List*', 'location': 'int'}  # noqa: E501

    _ATTRS_TO_IGNORE_IN_COMPARISON = Expr._ATTRS_TO_IGNORE_IN_COMPARISON | {'row_format'}

    def __init__(self, args=None, row_format=None, colnames=None, location=None):  # pragma: no cover  # noqa: E501
        if ((args is not None
             and row_format is colnames is location is None  # noqa: E501
             and isinstance(args, dict)
             and '@' in args)):
            super().__init__(args)
        else:
            self.args = args
            self.row_format = row_format
            self.colnames = colnames
            self.location = location


class RowMarkClause(Node):
    __slots__ = {'rti': 'Index', 'strength': 'LockClauseStrength', 'waitPolicy': 'LockWaitPolicy', 'pushedDown': 'bool'}  # noqa: E501

    def __init__(self, rti=None, strength=None, waitPolicy=None, pushedDown=None):  # pragma: no cover  # noqa: E501
        if ((rti is not None
             and strength is waitPolicy is pushedDown is None  # noqa: E501
             and isinstance(rti, dict)
             and '@' in rti)):
            super().__init__(rti)
        else:
            self.rti = rti
            self.strength = strength
            self.waitPolicy = waitPolicy
            self.pushedDown = pushedDown


class RuleStmt(Node):
    __slots__ = {'relation': 'RangeVar*', 'rulename': 'char*', 'whereClause': 'Node*', 'event': 'CmdType', 'instead': 'bool', 'actions': 'List*', 'replace': 'bool'}  # noqa: E501

    def __init__(self, relation=None, rulename=None, whereClause=None, event=None, instead=None, actions=None, replace=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and rulename is whereClause is event is instead is actions is replace is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.rulename = rulename
            self.whereClause = whereClause
            self.event = event
            self.instead = instead
            self.actions = actions
            self.replace = replace


class SQLValueFunction(Expr):
    __slots__ = {'op': 'SQLValueFunctionOp', 'typmod': 'int32', 'location': 'int'}  # noqa: E501

    def __init__(self, op=None, typmod=None, location=None):  # pragma: no cover  # noqa: E501
        if ((op is not None
             and typmod is location is None  # noqa: E501
             and isinstance(op, dict)
             and '@' in op)):
            super().__init__(op)
        else:
            self.op = op
            self.typmod = typmod
            self.location = location


class ScalarArrayOpExpr(Expr):
    __slots__ = {'useOr': 'bool', 'args': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, useOr=None, args=None, location=None):  # pragma: no cover  # noqa: E501
        if ((useOr is not None
             and args is location is None  # noqa: E501
             and isinstance(useOr, dict)
             and '@' in useOr)):
            super().__init__(useOr)
        else:
            self.useOr = useOr
            self.args = args
            self.location = location


class SecLabelStmt(Node):
    __slots__ = {'objtype': 'ObjectType', 'object': 'Node*', 'provider': 'char*', 'label': 'char*'}  # noqa: E501

    def __init__(self, objtype=None, object=None, provider=None, label=None):  # pragma: no cover  # noqa: E501
        if ((objtype is not None
             and object is provider is label is None  # noqa: E501
             and isinstance(objtype, dict)
             and '@' in objtype)):
            super().__init__(objtype)
        else:
            self.objtype = objtype
            self.object = object
            self.provider = provider
            self.label = label


class SelectStmt(Node):
    __slots__ = {'distinctClause': 'List*', 'intoClause': 'IntoClause*', 'targetList': 'List*', 'fromClause': 'List*', 'whereClause': 'Node*', 'groupClause': 'List*', 'groupDistinct': 'bool', 'havingClause': 'Node*', 'windowClause': 'List*', 'valuesLists': 'List*', 'sortClause': 'List*', 'limitOffset': 'Node*', 'limitCount': 'Node*', 'limitOption': 'LimitOption', 'lockingClause': 'List*', 'withClause': 'WithClause*', 'op': 'SetOperation', 'all': 'bool', 'larg': 'SelectStmt*', 'rarg': 'SelectStmt*'}  # noqa: E501

    def __init__(self, distinctClause=None, intoClause=None, targetList=None, fromClause=None, whereClause=None, groupClause=None, groupDistinct=None, havingClause=None, windowClause=None, valuesLists=None, sortClause=None, limitOffset=None, limitCount=None, limitOption=None, lockingClause=None, withClause=None, op=None, all=None, larg=None, rarg=None):  # pragma: no cover  # noqa: E501
        if ((distinctClause is not None
             and intoClause is targetList is fromClause is whereClause is groupClause is groupDistinct is havingClause is windowClause is valuesLists is sortClause is limitOffset is limitCount is limitOption is lockingClause is withClause is op is all is larg is rarg is None  # noqa: E501
             and isinstance(distinctClause, dict)
             and '@' in distinctClause)):
            super().__init__(distinctClause)
        else:
            self.distinctClause = distinctClause
            self.intoClause = intoClause
            self.targetList = targetList
            self.fromClause = fromClause
            self.whereClause = whereClause
            self.groupClause = groupClause
            self.groupDistinct = groupDistinct
            self.havingClause = havingClause
            self.windowClause = windowClause
            self.valuesLists = valuesLists
            self.sortClause = sortClause
            self.limitOffset = limitOffset
            self.limitCount = limitCount
            self.limitOption = limitOption
            self.lockingClause = lockingClause
            self.withClause = withClause
            self.op = op
            self.all = all
            self.larg = larg
            self.rarg = rarg


class SetOperationStmt(Node):
    __slots__ = {'op': 'SetOperation', 'all': 'bool', 'larg': 'Node*', 'rarg': 'Node*', 'colTypes': 'List*', 'colTypmods': 'List*', 'colCollations': 'List*', 'groupClauses': 'List*'}  # noqa: E501

    def __init__(self, op=None, all=None, larg=None, rarg=None, colTypes=None, colTypmods=None, colCollations=None, groupClauses=None):  # pragma: no cover  # noqa: E501
        if ((op is not None
             and all is larg is rarg is colTypes is colTypmods is colCollations is groupClauses is None  # noqa: E501
             and isinstance(op, dict)
             and '@' in op)):
            super().__init__(op)
        else:
            self.op = op
            self.all = all
            self.larg = larg
            self.rarg = rarg
            self.colTypes = colTypes
            self.colTypmods = colTypmods
            self.colCollations = colCollations
            self.groupClauses = groupClauses


class SetToDefault(Expr):
    __slots__ = {'typeMod': 'int32', 'location': 'int'}  # noqa: E501

    def __init__(self, typeMod=None, location=None):  # pragma: no cover  # noqa: E501
        if ((typeMod is not None
             and location is None  # noqa: E501
             and isinstance(typeMod, dict)
             and '@' in typeMod)):
            super().__init__(typeMod)
        else:
            self.typeMod = typeMod
            self.location = location


class SortBy(Node):
    __slots__ = {'node': 'Node*', 'sortby_dir': 'SortByDir', 'sortby_nulls': 'SortByNulls', 'useOp': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, node=None, sortby_dir=None, sortby_nulls=None, useOp=None, location=None):  # pragma: no cover  # noqa: E501
        if ((node is not None
             and sortby_dir is sortby_nulls is useOp is location is None  # noqa: E501
             and isinstance(node, dict)
             and '@' in node)):
            super().__init__(node)
        else:
            self.node = node
            self.sortby_dir = sortby_dir
            self.sortby_nulls = sortby_nulls
            self.useOp = useOp
            self.location = location


class SortGroupClause(Node):
    __slots__ = {'tleSortGroupRef': 'Index', 'nulls_first': 'bool', 'hashable': 'bool'}  # noqa: E501

    def __init__(self, tleSortGroupRef=None, nulls_first=None, hashable=None):  # pragma: no cover  # noqa: E501
        if ((tleSortGroupRef is not None
             and nulls_first is hashable is None  # noqa: E501
             and isinstance(tleSortGroupRef, dict)
             and '@' in tleSortGroupRef)):
            super().__init__(tleSortGroupRef)
        else:
            self.tleSortGroupRef = tleSortGroupRef
            self.nulls_first = nulls_first
            self.hashable = hashable


class StatsElem(Node):
    __slots__ = {'name': 'char*', 'expr': 'Node*'}  # noqa: E501

    def __init__(self, name=None, expr=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and expr is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.expr = expr


class SubLink(Expr):
    __slots__ = {'subLinkType': 'SubLinkType', 'subLinkId': 'int', 'testexpr': 'Node*', 'operName': 'List*', 'subselect': 'Node*', 'location': 'int'}  # noqa: E501

    def __init__(self, subLinkType=None, subLinkId=None, testexpr=None, operName=None, subselect=None, location=None):  # pragma: no cover  # noqa: E501
        if ((subLinkType is not None
             and subLinkId is testexpr is operName is subselect is location is None  # noqa: E501
             and isinstance(subLinkType, dict)
             and '@' in subLinkType)):
            super().__init__(subLinkType)
        else:
            self.subLinkType = subLinkType
            self.subLinkId = subLinkId
            self.testexpr = testexpr
            self.operName = operName
            self.subselect = subselect
            self.location = location


class SubPlan(Expr):
    __slots__ = {'subLinkType': 'SubLinkType', 'testexpr': 'Node*', 'paramIds': 'List*', 'plan_id': 'int', 'plan_name': 'char*', 'firstColTypmod': 'int32', 'useHashTable': 'bool', 'unknownEqFalse': 'bool', 'parallel_safe': 'bool', 'setParam': 'List*', 'parParam': 'List*', 'args': 'List*', 'startup_cost': 'Cost', 'per_call_cost': 'Cost'}  # noqa: E501

    def __init__(self, subLinkType=None, testexpr=None, paramIds=None, plan_id=None, plan_name=None, firstColTypmod=None, useHashTable=None, unknownEqFalse=None, parallel_safe=None, setParam=None, parParam=None, args=None, startup_cost=None, per_call_cost=None):  # pragma: no cover  # noqa: E501
        if ((subLinkType is not None
             and testexpr is paramIds is plan_id is plan_name is firstColTypmod is useHashTable is unknownEqFalse is parallel_safe is setParam is parParam is args is startup_cost is per_call_cost is None  # noqa: E501
             and isinstance(subLinkType, dict)
             and '@' in subLinkType)):
            super().__init__(subLinkType)
        else:
            self.subLinkType = subLinkType
            self.testexpr = testexpr
            self.paramIds = paramIds
            self.plan_id = plan_id
            self.plan_name = plan_name
            self.firstColTypmod = firstColTypmod
            self.useHashTable = useHashTable
            self.unknownEqFalse = unknownEqFalse
            self.parallel_safe = parallel_safe
            self.setParam = setParam
            self.parParam = parParam
            self.args = args
            self.startup_cost = startup_cost
            self.per_call_cost = per_call_cost


class SubscriptingRef(Expr):
    __slots__ = {'reftypmod': 'int32', 'refupperindexpr': 'List*', 'reflowerindexpr': 'List*', 'refexpr': 'Expr*', 'refassgnexpr': 'Expr*'}  # noqa: E501

    def __init__(self, reftypmod=None, refupperindexpr=None, reflowerindexpr=None, refexpr=None, refassgnexpr=None):  # pragma: no cover  # noqa: E501
        if ((reftypmod is not None
             and refupperindexpr is reflowerindexpr is refexpr is refassgnexpr is None  # noqa: E501
             and isinstance(reftypmod, dict)
             and '@' in reftypmod)):
            super().__init__(reftypmod)
        else:
            self.reftypmod = reftypmod
            self.refupperindexpr = refupperindexpr
            self.reflowerindexpr = reflowerindexpr
            self.refexpr = refexpr
            self.refassgnexpr = refassgnexpr


class TableFunc(Node):
    __slots__ = {'ns_uris': 'List*', 'ns_names': 'List*', 'docexpr': 'Node*', 'rowexpr': 'Node*', 'colnames': 'List*', 'coltypes': 'List*', 'coltypmods': 'List*', 'colcollations': 'List*', 'colexprs': 'List*', 'coldefexprs': 'List*', 'notnulls': 'Bitmapset*', 'ordinalitycol': 'int', 'location': 'int'}  # noqa: E501

    def __init__(self, ns_uris=None, ns_names=None, docexpr=None, rowexpr=None, colnames=None, coltypes=None, coltypmods=None, colcollations=None, colexprs=None, coldefexprs=None, notnulls=None, ordinalitycol=None, location=None):  # pragma: no cover  # noqa: E501
        if ((ns_uris is not None
             and ns_names is docexpr is rowexpr is colnames is coltypes is coltypmods is colcollations is colexprs is coldefexprs is notnulls is ordinalitycol is location is None  # noqa: E501
             and isinstance(ns_uris, dict)
             and '@' in ns_uris)):
            super().__init__(ns_uris)
        else:
            self.ns_uris = ns_uris
            self.ns_names = ns_names
            self.docexpr = docexpr
            self.rowexpr = rowexpr
            self.colnames = colnames
            self.coltypes = coltypes
            self.coltypmods = coltypmods
            self.colcollations = colcollations
            self.colexprs = colexprs
            self.coldefexprs = coldefexprs
            self.notnulls = notnulls
            self.ordinalitycol = ordinalitycol
            self.location = location


class TableLikeClause(Node):
    __slots__ = {'relation': 'RangeVar*', 'options': 'bits32'}  # noqa: E501

    def __init__(self, relation=None, options=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and options is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.options = options


class TableSampleClause(Node):
    __slots__ = {'args': 'List*', 'repeatable': 'Expr*'}  # noqa: E501

    def __init__(self, args=None, repeatable=None):  # pragma: no cover  # noqa: E501
        if ((args is not None
             and repeatable is None  # noqa: E501
             and isinstance(args, dict)
             and '@' in args)):
            super().__init__(args)
        else:
            self.args = args
            self.repeatable = repeatable


class TargetEntry(Expr):
    __slots__ = {'expr': 'Expr*', 'resno': 'AttrNumber', 'resname': 'char*', 'ressortgroupref': 'Index', 'resorigcol': 'AttrNumber', 'resjunk': 'bool'}  # noqa: E501

    def __init__(self, expr=None, resno=None, resname=None, ressortgroupref=None, resorigcol=None, resjunk=None):  # pragma: no cover  # noqa: E501
        if ((expr is not None
             and resno is resname is ressortgroupref is resorigcol is resjunk is None  # noqa: E501
             and isinstance(expr, dict)
             and '@' in expr)):
            super().__init__(expr)
        else:
            self.expr = expr
            self.resno = resno
            self.resname = resname
            self.ressortgroupref = ressortgroupref
            self.resorigcol = resorigcol
            self.resjunk = resjunk


class TransactionStmt(Node):
    __slots__ = {'kind': 'TransactionStmtKind', 'options': 'List*', 'savepoint_name': 'char*', 'gid': 'char*', 'chain': 'bool'}  # noqa: E501

    def __init__(self, kind=None, options=None, savepoint_name=None, gid=None, chain=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and options is savepoint_name is gid is chain is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.options = options
            self.savepoint_name = savepoint_name
            self.gid = gid
            self.chain = chain


class TriggerTransition(Node):
    __slots__ = {'name': 'char*', 'isNew': 'bool', 'isTable': 'bool'}  # noqa: E501

    def __init__(self, name=None, isNew=None, isTable=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and isNew is isTable is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.isNew = isNew
            self.isTable = isTable


class TruncateStmt(Node):
    __slots__ = {'relations': 'List*', 'restart_seqs': 'bool', 'behavior': 'DropBehavior'}  # noqa: E501

    def __init__(self, relations=None, restart_seqs=None, behavior=None):  # pragma: no cover  # noqa: E501
        if ((relations is not None
             and restart_seqs is behavior is None  # noqa: E501
             and isinstance(relations, dict)
             and '@' in relations)):
            super().__init__(relations)
        else:
            self.relations = relations
            self.restart_seqs = restart_seqs
            self.behavior = behavior


class TypeCast(Node):
    __slots__ = {'arg': 'Node*', 'typeName': 'TypeName*', 'location': 'int'}  # noqa: E501

    def __init__(self, arg=None, typeName=None, location=None):  # pragma: no cover  # noqa: E501
        if ((arg is not None
             and typeName is location is None  # noqa: E501
             and isinstance(arg, dict)
             and '@' in arg)):
            super().__init__(arg)
        else:
            self.arg = arg
            self.typeName = typeName
            self.location = location


class TypeName(Node):
    __slots__ = {'names': 'List*', 'setof': 'bool', 'pct_type': 'bool', 'typmods': 'List*', 'typemod': 'int32', 'arrayBounds': 'List*', 'location': 'int'}  # noqa: E501

    def __init__(self, names=None, setof=None, pct_type=None, typmods=None, typemod=None, arrayBounds=None, location=None):  # pragma: no cover  # noqa: E501
        if ((names is not None
             and setof is pct_type is typmods is typemod is arrayBounds is location is None  # noqa: E501
             and isinstance(names, dict)
             and '@' in names)):
            super().__init__(names)
        else:
            self.names = names
            self.setof = setof
            self.pct_type = pct_type
            self.typmods = typmods
            self.typemod = typemod
            self.arrayBounds = arrayBounds
            self.location = location


class UnlistenStmt(Node):
    __slots__ = {'conditionname': 'char*'}  # noqa: E501

    def __init__(self, conditionname=None):  # pragma: no cover  # noqa: E501

        if ((conditionname is not None
             and isinstance(conditionname, dict)
             and '@' in conditionname)):
            super().__init__(conditionname)
        else:
            self.conditionname = conditionname


class UpdateStmt(Node):
    __slots__ = {'relation': 'RangeVar*', 'targetList': 'List*', 'whereClause': 'Node*', 'fromClause': 'List*', 'returningList': 'List*', 'withClause': 'WithClause*'}  # noqa: E501

    def __init__(self, relation=None, targetList=None, whereClause=None, fromClause=None, returningList=None, withClause=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and targetList is whereClause is fromClause is returningList is withClause is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.targetList = targetList
            self.whereClause = whereClause
            self.fromClause = fromClause
            self.returningList = returningList
            self.withClause = withClause


class VacuumRelation(Node):
    __slots__ = {'relation': 'RangeVar*', 'va_cols': 'List*'}  # noqa: E501

    def __init__(self, relation=None, va_cols=None):  # pragma: no cover  # noqa: E501
        if ((relation is not None
             and va_cols is None  # noqa: E501
             and isinstance(relation, dict)
             and '@' in relation)):
            super().__init__(relation)
        else:
            self.relation = relation
            self.va_cols = va_cols


class VacuumStmt(Node):
    __slots__ = {'options': 'List*', 'rels': 'List*', 'is_vacuumcmd': 'bool'}  # noqa: E501

    def __init__(self, options=None, rels=None, is_vacuumcmd=None):  # pragma: no cover  # noqa: E501
        if ((options is not None
             and rels is is_vacuumcmd is None  # noqa: E501
             and isinstance(options, dict)
             and '@' in options)):
            super().__init__(options)
        else:
            self.options = options
            self.rels = rels
            self.is_vacuumcmd = is_vacuumcmd


class Var(Expr):
    __slots__ = {'varno': 'Index', 'varattno': 'AttrNumber', 'vartypmod': 'int32', 'varlevelsup': 'Index', 'varnosyn': 'Index', 'varattnosyn': 'AttrNumber', 'location': 'int'}  # noqa: E501

    def __init__(self, varno=None, varattno=None, vartypmod=None, varlevelsup=None, varnosyn=None, varattnosyn=None, location=None):  # pragma: no cover  # noqa: E501
        if ((varno is not None
             and varattno is vartypmod is varlevelsup is varnosyn is varattnosyn is location is None  # noqa: E501
             and isinstance(varno, dict)
             and '@' in varno)):
            super().__init__(varno)
        else:
            self.varno = varno
            self.varattno = varattno
            self.vartypmod = vartypmod
            self.varlevelsup = varlevelsup
            self.varnosyn = varnosyn
            self.varattnosyn = varattnosyn
            self.location = location


class VariableSetStmt(Node):
    __slots__ = {'kind': 'VariableSetKind', 'name': 'char*', 'args': 'List*', 'is_local': 'bool'}  # noqa: E501

    def __init__(self, kind=None, name=None, args=None, is_local=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and name is args is is_local is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.name = name
            self.args = args
            self.is_local = is_local


class VariableShowStmt(Node):
    __slots__ = {'name': 'char*'}  # noqa: E501

    def __init__(self, name=None):  # pragma: no cover  # noqa: E501

        if ((name is not None
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name


class ViewStmt(Node):
    __slots__ = {'view': 'RangeVar*', 'aliases': 'List*', 'query': 'Node*', 'replace': 'bool', 'options': 'List*', 'withCheckOption': 'ViewCheckOption'}  # noqa: E501

    def __init__(self, view=None, aliases=None, query=None, replace=None, options=None, withCheckOption=None):  # pragma: no cover  # noqa: E501
        if ((view is not None
             and aliases is query is replace is options is withCheckOption is None  # noqa: E501
             and isinstance(view, dict)
             and '@' in view)):
            super().__init__(view)
        else:
            self.view = view
            self.aliases = aliases
            self.query = query
            self.replace = replace
            self.options = options
            self.withCheckOption = withCheckOption


class WindowClause(Node):
    __slots__ = {'name': 'char*', 'refname': 'char*', 'partitionClause': 'List*', 'orderClause': 'List*', 'frameOptions': 'int', 'startOffset': 'Node*', 'endOffset': 'Node*', 'inRangeAsc': 'bool', 'inRangeNullsFirst': 'bool', 'winref': 'Index', 'copiedOrder': 'bool'}  # noqa: E501

    def __init__(self, name=None, refname=None, partitionClause=None, orderClause=None, frameOptions=None, startOffset=None, endOffset=None, inRangeAsc=None, inRangeNullsFirst=None, winref=None, copiedOrder=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and refname is partitionClause is orderClause is frameOptions is startOffset is endOffset is inRangeAsc is inRangeNullsFirst is winref is copiedOrder is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.refname = refname
            self.partitionClause = partitionClause
            self.orderClause = orderClause
            self.frameOptions = frameOptions
            self.startOffset = startOffset
            self.endOffset = endOffset
            self.inRangeAsc = inRangeAsc
            self.inRangeNullsFirst = inRangeNullsFirst
            self.winref = winref
            self.copiedOrder = copiedOrder


class WindowDef(Node):
    __slots__ = {'name': 'char*', 'refname': 'char*', 'partitionClause': 'List*', 'orderClause': 'List*', 'frameOptions': 'int', 'startOffset': 'Node*', 'endOffset': 'Node*', 'location': 'int'}  # noqa: E501

    def __init__(self, name=None, refname=None, partitionClause=None, orderClause=None, frameOptions=None, startOffset=None, endOffset=None, location=None):  # pragma: no cover  # noqa: E501
        if ((name is not None
             and refname is partitionClause is orderClause is frameOptions is startOffset is endOffset is location is None  # noqa: E501
             and isinstance(name, dict)
             and '@' in name)):
            super().__init__(name)
        else:
            self.name = name
            self.refname = refname
            self.partitionClause = partitionClause
            self.orderClause = orderClause
            self.frameOptions = frameOptions
            self.startOffset = startOffset
            self.endOffset = endOffset
            self.location = location


class WindowFunc(Expr):
    __slots__ = {'args': 'List*', 'aggfilter': 'Expr*', 'winref': 'Index', 'winstar': 'bool', 'winagg': 'bool', 'location': 'int'}  # noqa: E501

    def __init__(self, args=None, aggfilter=None, winref=None, winstar=None, winagg=None, location=None):  # pragma: no cover  # noqa: E501
        if ((args is not None
             and aggfilter is winref is winstar is winagg is location is None  # noqa: E501
             and isinstance(args, dict)
             and '@' in args)):
            super().__init__(args)
        else:
            self.args = args
            self.aggfilter = aggfilter
            self.winref = winref
            self.winstar = winstar
            self.winagg = winagg
            self.location = location


class WithCheckOption(Node):
    __slots__ = {'kind': 'WCOKind', 'relname': 'char*', 'polname': 'char*', 'qual': 'Node*', 'cascaded': 'bool'}  # noqa: E501

    def __init__(self, kind=None, relname=None, polname=None, qual=None, cascaded=None):  # pragma: no cover  # noqa: E501
        if ((kind is not None
             and relname is polname is qual is cascaded is None  # noqa: E501
             and isinstance(kind, dict)
             and '@' in kind)):
            super().__init__(kind)
        else:
            self.kind = kind
            self.relname = relname
            self.polname = polname
            self.qual = qual
            self.cascaded = cascaded


class WithClause(Node):
    __slots__ = {'ctes': 'List*', 'recursive': 'bool', 'location': 'int'}  # noqa: E501

    def __init__(self, ctes=None, recursive=None, location=None):  # pragma: no cover  # noqa: E501
        if ((ctes is not None
             and recursive is location is None  # noqa: E501
             and isinstance(ctes, dict)
             and '@' in ctes)):
            super().__init__(ctes)
        else:
            self.ctes = ctes
            self.recursive = recursive
            self.location = location


class XmlExpr(Expr):
    __slots__ = {'op': 'XmlExprOp', 'name': 'char*', 'named_args': 'List*', 'arg_names': 'List*', 'args': 'List*', 'xmloption': 'XmlOptionType', 'typmod': 'int32', 'location': 'int'}  # noqa: E501

    def __init__(self, op=None, name=None, named_args=None, arg_names=None, args=None, xmloption=None, typmod=None, location=None):  # pragma: no cover  # noqa: E501
        if ((op is not None
             and name is named_args is arg_names is args is xmloption is typmod is location is None  # noqa: E501
             and isinstance(op, dict)
             and '@' in op)):
            super().__init__(op)
        else:
            self.op = op
            self.name = name
            self.named_args = named_args
            self.arg_names = arg_names
            self.args = args
            self.xmloption = xmloption
            self.typmod = typmod
            self.location = location


class XmlSerialize(Node):
    __slots__ = {'xmloption': 'XmlOptionType', 'expr': 'Node*', 'typeName': 'TypeName*', 'location': 'int'}  # noqa: E501

    def __init__(self, xmloption=None, expr=None, typeName=None, location=None):  # pragma: no cover  # noqa: E501
        if ((xmloption is not None
             and expr is typeName is location is None  # noqa: E501
             and isinstance(xmloption, dict)
             and '@' in xmloption)):
            super().__init__(xmloption)
        else:
            self.xmloption = xmloption
            self.expr = expr
            self.typeName = typeName
            self.location = location


def _fixup_attribute_types_in_slots():
    G = globals()

    def traverse_sub_classes(cls):
        for subc in cls.__subclasses__():
            yield subc
            yield from traverse_sub_classes(subc)

    for cls in traverse_sub_classes(Node):
        slots = cls.__slots__
        if not (slots
                and isinstance(slots, dict)
                and isinstance(next(iter(slots.values())), str)):
            continue
        for attr in slots:
            adaptor = None
            ctype = slots[attr]
            if ctype == 'List*':
                ptype = (list, tuple)

                def adaptor(value):
                    return tuple(G[i['@']](i)
                                 if isinstance(i, dict) and '@' in i
                                 else i
                                 for i in value)
            elif ctype == 'bool':
                ptype = (bool, int)
                adaptor = bool
            elif ctype == 'char':
                ptype = (str, int)

                def adaptor(value):
                    if isinstance(value, int):
                        value = chr(value)
                    elif len(value) != 1:
                        raise ValueError(f'Bad value for attribute {cls.__name__}.{attr},'
                                         f' expected a single char, got {value!r}')
                    return value
            elif ctype == 'char*':
                ptype = str
            elif ctype in ('Expr*', 'Node*'):
                ptype = (dict, list, tuple, Node)

                def adaptor(value):
                    if isinstance(value, dict):
                        if '@' in value:
                            value = G[value['@']](value)
                    elif isinstance(value, (list, tuple)):
                        value = tuple(G[i['@']](i)
                                      if isinstance(i, dict) and '@' in i
                                      else i
                                      for i in value)
                    return value
            elif ctype in ('Value', 'Value*'):
                ptype = (int, str, float, Decimal, Value)
            elif ctype in ('int', 'int16', 'bits32', 'int32', 'uint32', 'uint64',
                           'AttrNumber', 'AclMode', 'Index', 'SubTransactionId'):
                ptype = int
            elif ctype == 'Cost':
                ptype = float
            elif ctype == 'CreateStmt':
                ptype = (dict, CreateStmt)

                def adaptor(value):
                    if isinstance(value, dict):
                        if '@' in value:
                            value = G[value['@']](value)
                    return value
            elif ctype == 'Bitmapset*':
                ptype = (list, set, tuple)

                def adaptor(value):
                    if isinstance(value, (list, tuple)):
                        return set(value)
                    else:
                        return value
            else:
                from pglast import enums

                if hasattr(enums, ctype):
                    ptype = (int, str, dict, getattr(enums, ctype))
                else:
                    if ctype.endswith('*'):
                        ptype = G.get(ctype[:-1])
                        if ptype is None:
                            raise NotImplementedError(f'unknown {ctype!r}') from None
                        else:
                            ptype = (dict, ptype)
            slots[attr] = SlotTypeInfo(ctype, ptype, adaptor)


_fixup_attribute_types_in_slots()
del _fixup_attribute_types_in_slots
