# -*- coding: utf-8 -*-
# :Project:   pglast -- Wrap PG nodes into a Python AST
# :Created:   sab 27 feb 2021, 19:47:11
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021, 2022 Lele Gaifax
#

from datetime import date
import json
from keyword import iskeyword
from pathlib import Path
import subprocess
from re import match, sub


CYEARS = f'2021-{date.today().year}'


AST_PY_HEADER = f"""\
# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from struct_defs.json @ %s
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © {CYEARS} Lele Gaifax
#

from collections import namedtuple
from decimal import Decimal
from enum import Enum


SlotTypeInfo = namedtuple('SlotTypeInfo', ['c_type', 'py_type', 'adaptor'])


def _serialize_node(n, depth, ellipsis, skip_none):
    d = {{'@': n.__class__.__name__}}
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
        v = {{'#': v.__class__.__name__, 'name': v.name, 'value': v.value}}
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
            raise ValueError(f'Bad argument, expected a dictionary, got {{type(data)!r}}')
        if '@' not in data:  # pragma: no cover
            raise ValueError('Bad argument, expected a dictionary with a "@" key')
        if data['@'] != self.__class__.__name__:
            raise ValueError(f'Bad argument, wrong "@" value, expected'
                             f' {{self.__class__.__name__!r}}, got {{data["@"]!r}}')

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
                    attrs.append(f'{{a}}={{v!r}}')
        if attrs:
            attrs = ' ' + ' '.join(attrs)
        else:
            attrs = ''
        return '<' + self.__class__.__name__ + attrs + '>'

    _ATTRS_TO_IGNORE_IN_COMPARISON = {{'location', 'stmt_len', 'stmt_location'}}

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
                raise ValueError(f'Bad value for attribute {{self.__class__.__name__}}'
                                 f'.{{name}}, expected {{ptype}}, got {{type(value)}}:'
                                 f' {{value!r}}')

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
                                                 f' {{self.__class__.__name__}}.{{name}},'
                                                 f' expected a {{ptype}}, got'
                                                 f' {{value!r}}') from None
                            if 'name' in value:
                                value = value['name']
                            elif 'value' in value:
                                value = value['value']
                            else:
                                raise ValueError(f'Bad value for attribute'
                                                 f' {{self.__class__.__name__}}.{{name}},'
                                                 f' expected a {{ptype}}, got'
                                                 f' {{value!r}}') from None
                        try:
                            if isinstance(value, str) and len(value) > 1:
                                value = enum[value]
                            else:
                                value = enum(value)
                        except (KeyError, ValueError):
                            raise ValueError(f'Bad value for attribute'
                                             f' {{self.__class__.__name__}}.{{name}},'
                                             f' expected a {{ptype}}, got'
                                             f' {{value!r}}') from None
                else:
                    if ctype.endswith('*'):
                        cls = globals().get(ctype[:-1])
                        if cls is None:
                            raise NotImplementedError(f'Unhandled {{ctype!r}} for attribute'
                                                      f' {{self.__class__.__name__}}.{{name}}')
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

    __slots__ = {{'val': SlotTypeInfo('char*', str, None)}}


class Float(Value):
    '''Implement the ``T_Float`` variant of the :class:`Value` union.'''

    __slots__ = {{'val': SlotTypeInfo('char*', (str, Decimal), Decimal)}}


class Integer(Value):
    '''Implement the ``T_Integer`` variant of the :class:`Value` union.'''

    __slots__ = {{'val': SlotTypeInfo('char*', int, None)}}


class Null(Value):
    '''Implement the ``T_Null`` variant of the :class:`Value` union.'''

    __slots__ = {{'val': SlotTypeInfo('char*', type(None), None)}}


class String(Value):
    '''Implement the ``T_String`` variant of the :class:`Value` union.'''

    __slots__ = {{'val': SlotTypeInfo('char*', str, None)}}
"""


AST_PYX_HEADER = f"""\
# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from struct_defs.json @ %s
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © {CYEARS} Lele Gaifax
#

#cython: language_level=3

from cpython.ref cimport Py_INCREF
from cpython.tuple cimport PyTuple_New, PyTuple_SET_ITEM

from decimal import Decimal

from pglast import ast, enums
from pglast cimport structs


cdef _pg_bitmapset_to_set(const structs.Bitmapset* bms):
    cdef set result
    cdef int m
    if bms is not NULL:
        result = set()
        m = structs.bms_next_member(bms, -1)
        while m >= 0:
            result.add(m)
            m = structs.bms_next_member(bms, m)
    else:
        result = None
    return result


cdef _pg_str_to_decimal(const char* cstr):
    # Add a trailing zero to truncated floats like "2.", see issues #91 and #100
    cdef s = cstr.decode("utf-8")
    if s.endswith('.'):
        s += '0'
    return ast.Float(Decimal(s))


cdef _pg_list_to_tuple(const structs.List* lst, offset_to_index):
    cdef tuple result
    cdef int i
    if lst is not NULL:
        result = PyTuple_New(lst.length)
        for i in range(lst.length):
            item = create(structs.list_nth(lst, i), offset_to_index)
            Py_INCREF(item)
            PyTuple_SET_ITEM(result, i, item)
    else:
        result = None
    return result


cdef _pg_value_to_py(structs.Value val):
    cdef object result
    if val.type == structs.T_Null:
        result = ast.Null(None)
    elif val.type == structs.T_Integer:
        result = ast.Integer(val.val.ival)
    elif val.type == structs.T_Float:
        result = _pg_str_to_decimal(val.val.str)
    elif val.type == structs.T_BitString:
        result = ast.BitString(val.val.str.decode("utf-8"))
    else:
        result = ast.String(val.val.str.decode("utf-8"))
    return result
"""


STRUCTS_PXD_HEADER = f"""\
# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from struct_defs.json @ %s
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © {CYEARS} Lele Gaifax
#

#cython: language_level=3

from libc.stdint cimport int16_t, int32_t, uint32_t, uint64_t


cdef extern from "postgres.h":
    ctypedef unsigned char bool

    ctypedef struct Node:
        int type

    ctypedef union ValueUnion:
        int ival
        char *str

    ctypedef struct Value:
        int type
        ValueUnion val

    ctypedef struct Bitmapset:
        int nwords
        unsigned long *words


cdef extern from "nodes/bitmapset.h":
    ctypedef struct Bitmapset:
        pass

    int bms_next_member(const Bitmapset *a, int prevbit)


cdef extern from "nodes/pg_list.h":
    ctypedef struct List:
        int length

    void* list_nth(List* list, int n)


cdef extern from "nodes/value.h":
    ctypedef struct ValUnion:
        int ival
        char *str

    ctypedef struct Value:
        NodeTag type
        ValUnion val

    int intVal(Value* v)
    char* strVal(Value* v)
"""


AST_RST_HEADER = f"""\
.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © {CYEARS} Lele Gaifax
..

.. _pglast.ast:

===================================================================
 :mod:`pglast.ast` --- Python classes representing PG parser nodes
===================================================================

The module implements a set of *data* classes, one for each ``C`` structure defined in several
PostgreSQL headers, primarily those in the `include/nodes/`__ directory.

__ %ssrc/postgres/include/nodes

The :class:`pglast.ast.Node` is an abstract class that implements the common behaviour of all
the concrete classes. In particular any node can be :meth:`compared <pglast.ast.Node.__eq__>`
with another instance, is able to :meth:`serialize <pglast.ast.Node.__call__>` itself and can
be :meth:`altered <pglast.ast.Node.__setattr__>`.

.. module:: pglast.ast

.. autoclass:: Node
   :special-members: __repr__, __eq__, __call__, __setattr__

.. autoclass:: Value
.. autoclass:: BitString
.. autoclass:: Float
.. autoclass:: Integer
.. autoclass:: Null
.. autoclass:: String

"""


def get_libpg_query_info():
    "Return a tuple with (version, baseurl) of the libpg_query library."

    version = subprocess.check_output(['git', 'describe', '--all', '--long'],
                                      cwd='libpg_query')
    version = version.decode('utf-8').strip().split('/')[-1]
    remote = subprocess.check_output(['git', 'remote', 'get-url', 'origin'],
                                     cwd='libpg_query')
    remote = remote.decode('utf-8')
    baseurl = '%s/blob/%s/' % (remote[:-5], version[-7:])
    return version, baseurl


def extract_toc(header):
    "Extract the enums and defines with their position in the header."

    toc = {}

    content = header.read_text(encoding='utf-8')

    for lineno, line in enumerate(content.splitlines(), 1):
        if line.startswith(('struct ', 'typedef struct ')):
            m = match(r'(typedef )?struct\s+([\w_]+)', line)
            if m is not None:
                toc[m.group(2)] = lineno

    return toc


def emit_struct_def(name, fields, output):
    output.write(f'    ctypedef struct {name}:\n')

    empty = True
    for field in fields:
        if 'name' not in field or 'c_type' not in field:
            continue

        ctype = field['c_type']
        if ctype in ('Expr', 'Oid'):
            continue
        if ctype == 'int16':
            ctype = 'int16_t'
        elif ctype in ('bits32', 'int32'):
            ctype = 'int32_t'
        elif ctype == 'uint32':
            ctype = 'uint32_t'
        elif ctype == 'uint64':
            ctype = 'uint64_t'
        if ctype == 'AttrNumber':
            ctype = 'int'
        elif ctype in ('AclMode', 'Index', 'SubTransactionId'):
            ctype = 'unsigned int'
        elif ctype == 'Cost':
            ctype = 'float'
        elif ctype.endswith('*'):
            ctype = f'const {ctype}'

        fname = field['name']
        if iskeyword(fname):
            fname = f'{fname}_ "{fname}"'

        output.write(f'        {ctype} {fname}\n')
        empty = False

    if empty:
        output.write('        pass\n')


def emit_generic_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = data.{name}
''')


def emit_bool_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = bool(data.{name})
''')


def emit_value_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = _pg_value_to_py(data.{name})
''')


def emit_str_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = data.{name}.decode("utf-8") if data.{name} is not NULL else None
''')


def emit_char_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = chr(data.{name})
''')


def emit_list_attr(name, ctype, output):
    output.write(f'''\
    cdef tuple v_{name} = _pg_list_to_tuple(data.{name}, offset_to_index)
''')


def emit_node_attr(name, ctype, output):
    output.write(f'''\
    cdef v_{name} = create(&data.{name}, offset_to_index)
''')


def emit_create_stmt_attr(name, ctype, output):
    output.write(f'''
    cdef object v_{name} = create_CreateStmt(<structs.CreateStmt*> data, offset_to_index)
''')


def emit_nodeptr_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = create(data.{name}, offset_to_index) if data.{name} is not NULL else None
''')


def emit_no_attr(name, ctype, output):
    # output.write(f'#        cdef object v_{name} = data.{name}\n')
    pass


def emit_int_enum_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = getattr(enums, {ctype!r})(data.{name})
''')


def emit_str_enum_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = getattr(enums, {ctype!r})(chr(data.{name}))
''')


def emit_bitmapset_attr(name, ctype, output):
    output.write(f'''\
    cdef set v_{name} = _pg_bitmapset_to_set(data.{name})
''')


def emit_location_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = offset_to_index(data.{name})
''')


def emit_stmt_len_attr(name, ctype, output):
    output.write(f'''\
    cdef object v_{name} = offset_to_index(data.stmt_location + data.{name}) - offset_to_index(data.stmt_location)
''')


def emitter_for(fname, ctype, enums):
    from pglast import enums as eimpl

    if fname == 'location' and ctype == 'int' or fname == 'stmt_location':
        emitter = emit_location_attr
    elif fname == 'stmt_len':
        emitter = emit_stmt_len_attr
    elif ctype == 'List*':
        emitter = emit_list_attr
    elif ctype == 'CreateStmt':
        emitter = emit_create_stmt_attr
    elif ctype == 'Expr':
        emitter = emit_no_attr
    elif ctype == 'NodeTag':
        emitter = emit_no_attr
    elif ctype == 'Value':
        emitter = emit_value_attr
    elif ctype == 'char*':
        emitter = emit_str_attr
    elif ctype == 'char':
        emitter = emit_char_attr
    elif ctype == 'bool':
        emitter = emit_bool_attr
    elif ctype == 'Bitmapset*':
        emitter = emit_bitmapset_attr
    elif ctype.endswith('*'):
        emitter = emit_nodeptr_attr
    elif ctype in enums:
        if issubclass(getattr(eimpl, ctype), eimpl.IntEnum):
            emitter = emit_int_enum_attr
        else:
            emitter = emit_str_enum_attr
    else:
        emitter = emit_generic_attr

    return emitter


def emit_node_def(name, fields, enums, url, output, doc):
    attrs = []
    attrs_to_ignore_in_comparison = set()

    superclass = 'Node'

    for field in fields:
        if 'name' not in field or 'c_type' not in field:
            continue

        ctype = field['c_type']

        if ctype == 'Oid':
            continue

        fname = field['name']
        if iskeyword(fname):
            fname = f'{fname}_'

        if ctype == 'CoercionForm':
            attrs_to_ignore_in_comparison.add(fname)

        emitter = emitter_for(fname, ctype, enums)
        if ctype == 'Expr':
            superclass = 'Expr'

        comment = field['comment']
        if comment:
            comment = comment.strip()
            if comment.startswith('/*'):
                comment = comment[2:-2].strip()
            comment = sub(r'\t+( \* (?![A-Z] = ))?', ' ', comment)
            comment = sub(r'\*-+\s*', '', comment)
            comment = sub(r'-+\n', '', comment)
            comment = sub(r'\n +', '\n      ', comment)
            comment = sub(r'\*\)', '\\*)', comment)
            comment = comment.strip()
            comment = comment[0].upper() + comment[1:]
            if comment.lower() == 'see above':
                comment = ''

        attrs.append((fname, ctype, comment, emitter))

    real_attrs = []
    if attrs:
        for attr, ctype, comment, emitter in attrs:
            if emitter is emit_no_attr:
                continue
            real_attrs.append((attr, ctype))

    output.write(f'''\


class {name}({superclass}):
    __slots__ = {{{', '.join(repr(a)+': '+repr(t) for a, t in real_attrs)}}}  # noqa: E501

''')

    if attrs_to_ignore_in_comparison:
        output.write(f'''\
    _ATTRS_TO_IGNORE_IN_COMPARISON = {superclass}._ATTRS_TO_IGNORE_IN_COMPARISON | {repr(attrs_to_ignore_in_comparison)}

''')
    if real_attrs:
        output.write(f'''\
    def __init__(self, {', '.join(f'{attr}=None' for attr, __ in real_attrs)}):  # pragma: no cover  # noqa: E501
''')

        if len(real_attrs) > 1:
            output.write(f'''\
        if (({real_attrs[0][0]} is not None
             and {' is '.join(attr for attr, __ in real_attrs[1:])} is None  # noqa: E501
             and isinstance({real_attrs[0][0]}, dict)
             and '@' in {real_attrs[0][0]})):
            super().__init__({real_attrs[0][0]})
        else:
''')
            for a, v in real_attrs:
                output.write(f'            self.{a} = {a}\n')
        else:
            output.write(f'''
        if (({real_attrs[0][0]} is not None
             and isinstance({real_attrs[0][0]}, dict)
             and '@' in {real_attrs[0][0]})):
            super().__init__({real_attrs[0][0]})
        else:
''')
            for a, v in real_attrs:
                output.write(f'            self.{a} = {a}\n')
    else:
        output.write('''\
    def __init__(self):  # pragma: no cover
        pass
''')

    doc.write(f'''
.. class:: {name}({', '.join(f'{attr}=None' for attr, __ in real_attrs)})

   Wrapper for the `homonymous <{url}>`__ parser node.

''')
    for attr, ctype, comment, emitter in attrs:
        if emitter is emit_no_attr:
            continue
        if ctype == 'List*':
            type = 'tuple'
        elif ctype in ('char', 'char*'):
            type = 'str'
        elif ctype == 'Node*':
            type = 'Node'
        elif ctype in enums:
            type = f'{ctype}'
        else:
            type = ctype
        doc.write(f'   .. attribute:: {attr}\n')
        doc.write(f'      :type: {type}\n\n')
        if comment:
            doc.write(f'      {comment}\n\n')


def emit_node_create_function(nodes, enums, output):
    from pglast import enums as eimpl

    nnames = set(n[0] for n in nodes)

    for name, fields in nodes:
        attrs = []
        real_attrs = []
        for field in fields:
            if 'name' not in field or 'c_type' not in field:
                continue

            ctype = field['c_type']
            if ctype in ('Expr', 'Oid'):
                continue

            fname = field['name']
            if iskeyword(fname):
                fname = f'{fname}_'

            emitter = emitter_for(fname, ctype, enums)

            attrs.append((fname, ctype, emitter))
            if emitter is not emit_no_attr:
                real_attrs.append((fname, ctype))

        output.write(f'''\


cdef create_{name}(structs.{name}* data, offset_to_index):
''')
        for attr, ctype, emitter in attrs:
            emitter(attr, ctype, output)
        output.write(f'''\
    return ast.{name}({', '.join(f'v_{attr}' for attr, __ in real_attrs)})
''')

    output.write('''\


cdef create(void* data, offset_to_index):
    if data is NULL:
        return None

    cdef tuple t
    cdef int i
    cdef str s
    cdef int tag = structs.nodeTag(data)

''')

    first = True
    for tag in eimpl.NodeTag:
        name = tag.name[2:]
        if name in nnames:
            output.write('    ')
            output.write('if' if first else 'elif')
            output.write(f' tag == structs.{tag.name}:\n')
            output.write(f'        return create_{name}(<structs.{name}*> data, offset_to_index)\n')
            first = False

        elif name == 'Null':
            output.write('''\
    elif tag == structs.T_Null:
        return ast.Null(None)
''')

        elif name == 'Integer':
            output.write('''\
    elif tag == structs.T_Integer:
        return ast.Integer(structs.intVal(<structs.Value *> data))
''')

        elif name == 'Float':
            output.write('''\
    elif tag == structs.T_Float:
        return _pg_str_to_decimal(structs.strVal(<structs.Value *> data))
''')

        elif name == 'BitString':
            output.write('''\
    elif tag == structs.T_BitString:
        return ast.BitString(structs.strVal(<structs.Value *> data).decode("utf-8"))
''')

        elif name == 'String':
            output.write('''\
    elif tag == structs.T_String:
        return ast.String(structs.strVal(<structs.Value *> data).decode("utf-8"))
''')

        elif name == 'List':
            output.write('''\
    elif tag == structs.T_List:
        return _pg_list_to_tuple(<structs.List *> data, offset_to_index)
''')

    output.write('''\
    raise ValueError("Unhandled tag: %s" % tag)
''')


def workhorse(args):
    libpg_query_version, libpg_query_baseurl = get_libpg_query_info()

    pgq_dir = Path('libpg_query')
    pg_inc_dir = pgq_dir / 'src' / 'postgres' / 'include'

    with (pgq_dir / 'srcdata' / 'struct_defs.json').open(encoding='utf-8') as f:
        structs = json.load(f)

    ctypes = set()
    for header in ('nodes/parsenodes', 'nodes/primnodes'):
        for name in structs[header]:
            fields = structs[header][name]['fields']
            for field in fields:
                if 'c_type' in field:
                    ctypes.add(field['c_type'])

    with (pgq_dir / 'srcdata' / 'all_known_enums.json').open(encoding='utf-8') as f:
        enums = sorted(json.load(f))

    with (pgq_dir / 'srcdata' / 'enum_defs.json').open(encoding='utf-8') as f:
        node_tags = [e['name']
                     for e in json.load(f)['nodes/nodes']['NodeTag']['values']
                     if 'name' in e]

    linenos = {}

    structs_pxd = args.output_dir / 'structs.pxd'
    with structs_pxd.open('w', encoding='utf-8') as output:
        output.write(STRUCTS_PXD_HEADER % libpg_query_version)

        output.write('\n\ncdef extern from *:')
        for name in enums:
            output.write(f'\n    ctypedef enum {name}:\n')
            if name == 'NodeTag':
                for tag in node_tags:
                    output.write(f'        {tag}\n')
            else:
                output.write('        pass\n')
        output.write('\n    int nodeTag(void* data)\n')

        nodes = []
        for header in ('nodes/parsenodes', 'nodes/primnodes'):
            output.write(f'\n\ncdef extern from "{header}.h":\n')
            toc = extract_toc(pg_inc_dir / (header + '.h'))
            for name in toc:
                linenos[name] = (header, toc[name])
            defs = structs[header]
            first = True
            for name in defs:
                fields = defs[name]['fields']
                if name not in ('Const', 'NextValueExpr', 'Value'):
                    if name != 'Expr':
                        # Omit the Expr node, because it is hand written in the
                        # ast.py header above: also, it is an abstract class,
                        # never instantiated directly
                        nodes.append((name, fields))
                    if first:
                        first = False
                    else:
                        output.write('\n')
                    emit_struct_def(name, fields, output)

    ast_py = args.output_dir / 'ast.py'
    with ast_py.open('w', encoding='utf-8') as output, \
         args.rstdoc.open('w', encoding='utf-8') as doc:
        output.write(AST_PY_HEADER % libpg_query_version)

        doc.write(AST_RST_HEADER % libpg_query_baseurl)

        for name, fields in sorted(nodes):
            header, lineno = linenos[name]
            url = f'{libpg_query_baseurl}src/postgres/include/{header}.h#L{lineno}'
            emit_node_def(name, fields, enums, url, output, doc)

        output.write('''

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
''')

    ast_pyx = args.output_dir / 'ast.pyx'
    with ast_pyx.open('w', encoding='utf-8') as output:
        output.write(AST_PYX_HEADER % libpg_query_version)
        emit_node_create_function(nodes, enums, output)


def main():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(description="PG structs extractor",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('output_dir', type=Path,
                        help="where Cython sources will be created")
    parser.add_argument('rstdoc', type=Path,
                        help="reST documentation to be created")

    args = parser.parse_args()

    workhorse(args)


if __name__ == '__main__':
    main()
