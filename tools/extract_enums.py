# -*- coding: utf-8 -*-
# :Project:   pglast — Extract enums from PostgreSQL headers
# :Created:   gio 03 ago 2017 14:54:39 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 Lele Gaifax
#

from datetime import date
from os import environ
from os.path import basename, splitext
from re import match
from shutil import which
import subprocess

from pycparser import c_ast, c_parser


CYEARS = f'2017-{date.today().year}'


PY_HEADER = f"""\
# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: automatically extracted from %s @ %s
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © {CYEARS} Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:  # pragma: no cover
    # Python < 3.11
    class StrEnum(str, Enum):
        pass
"""


PYI_HEADER = f"""\
# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: type stubs automatically extracted from %s @ %s
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © {CYEARS} Lele Gaifax
#
"""


RST_HEADER = f"""\
.. -*- coding: utf-8 -*-
.. :Project:   pglast — DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © {CYEARS} Lele Gaifax
..

========================================================%(extra_decoration)s
 :mod:`pglast.enums.%(mod_name)s` --- Constants extracted from `%(header_fname)s`__
========================================================%(extra_decoration)s

__ %(header_url)s

.. module:: pglast.enums.%(mod_name)s
   :synopsis: Constants extracted from %(header_fname)s
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


def preprocess(fname, cpp_args=()):
    "Preprocess the given header and return the result."

    # macOS /usr/bin/cpp may expose SDK typedef enums that pycparser cannot
    # parse. Prefer clang unless the caller selected a preprocessor explicitly.
    cpp = environ.get('CPP') or which('clang') or 'cpp'
    result = subprocess.check_output([cpp, '-E', '-include', 'c.h', *cpp_args, fname])

    return result.decode('utf-8')


def extract_toc(header):
    "Extract the enums and defines with their position in the header."

    toc = {}

    with open(header, encoding='utf-8') as f:
        content = f.read()

    in_typedef_enum = 0

    for lineno, line in enumerate(content.splitlines(), 1):
        if line.startswith('typedef enum '):
            m = match(r'typedef enum\s+([\w_]+)', line)
            if m is not None:
                toc[m.group(1)] = lineno
        elif line.startswith('typedef enum'):
            in_typedef_enum = lineno
        elif in_typedef_enum and line.startswith('}'):
            m = match(r'}\s+([\w_]+)\s*;', line)
            if m is not None:
                toc[m.group(1)] = in_typedef_enum
                in_typedef_enum = 0
        elif line.startswith('#define'):
            m = match(r'#define\s+([a-zA-Z_]+)', line)
            if m is not None:
                toc[m.group(1)] = lineno

    return toc


def extract_enums(toc, source):
    "Yield all enum definitions belonging to the given header."

    typedefs = []
    in_typedef = False
    typedef = []

    for line in source.splitlines():
        if line and not line.startswith('#'):
            if in_typedef:
                typedef.append(line)
                if line.startswith('}'):
                    in_typedef = False
                    typedefs.append(typedef)
                    typedef = []
            elif line.startswith('typedef enum'):
                in_typedef = True
                typedef.append(line)

    parser = c_parser.CParser()
    for typedef in typedefs:
        source = ''.join(typedef)
        m = match(r'typedef enum\s+([\w_]+)', source)
        if m is None:
            m = match(r'.*}\s+([\w_]+)\s*;', source)
        if m is None or m.group(1) not in toc:
            continue
        yield parser.parse(source)


def extract_defines(source):
    "Yield all #defined constants in the given header."

    for line in source.splitlines():
        if line and line.startswith('#define'):
            m = match(r"#define\s+([a-zA-Z_]+)\s+\(?(\d+\s*<<\s*\d+|(0x)?\d+|'[a-zA-Z]')\)?",
                      line)
            if m is not None:
                yield m.group(1), m.group(2)


def emit_constant(value):
    return value.value


def emit_binary_op(value):
    assert isinstance(value.left, c_ast.Constant)
    assert isinstance(value.right, c_ast.Constant)
    return '%s %s %s' % (emit_constant(value.left),
                         value.op,
                         emit_constant(value.right))


def emit_unary_op(value):
    return '%s%s' % (value.op, emit_constant(value.expr))


def int_enum_value_factory(index, enumerator):
    if enumerator.value is None:
        return '0' if index == 0 else 'auto()'

    if isinstance(enumerator.value, c_ast.BinaryOp):
        return emit_binary_op(enumerator.value)
    elif isinstance(enumerator.value, c_ast.Constant):
        return emit_constant(enumerator.value)
    elif isinstance(enumerator.value, c_ast.UnaryOp):
        return emit_unary_op(enumerator.value)
    elif enumerator.value.name == 'PG_INT32_MAX':
        return '0x7FFFFFFF'

    assert enumerator.value.type == 'int'
    return enumerator.value.value


def char_enum_value_factory(index, enumerator):
    assert enumerator.value.type == 'char'
    return enumerator.value.value


def determine_enum_type_and_value(enum):
    type = 'IntEnum'
    value = int_enum_value_factory

    for item in enum.values.enumerators:
        if item.value:
            if isinstance(item.value, c_ast.Constant) and item.value.type == 'char':
                type = 'StrEnum'
                value = char_enum_value_factory
                break
            elif isinstance(item.value, c_ast.BinaryOp) and item.value.op == '<<':
                type = 'IntFlag'
                break

    return type, value


def write_enum(name, enum, output):
    enum_type, value_factory = determine_enum_type_and_value(enum)
    output.write('\n\n')
    output.write('class %s(%s):\n' % (name, enum_type))
    for index, item in enumerate(enum.values.enumerators):
        output.write('    %s = %s\n' % (item.name, value_factory(index, item)))


def write_enum_stub(name, enum, output):
    enum_type, __ = determine_enum_type_and_value(enum)
    if enum_type == 'StrEnum':
        enum_type = 'str, Enum'
    output.write('\n\n')
    output.write('class %s(%s):\n' % (name, enum_type))
    for item in enum.values.enumerators:
        output.write('    %s = ...\n' % item.name)


def write_enum_doc(name, enum, output, toc, url, mod_name):
    output.write('\n\n.. class:: pglast.enums.%s.%s\n' % (mod_name, name))
    if name in toc:
        output.write('\n   Corresponds to the `%s enum <%s#L%d>`__.\n' %
                     (name, url, toc[name]))
    for item in enum.values.enumerators:
        output.write('\n   .. data:: %s\n' % item.name)


def define_stub_type(value):
    return 'str' if value.startswith("'") else 'int'


def workhorse(args):
    libpg_query_version, libpg_query_baseurl = get_libpg_query_info()
    header_url = libpg_query_baseurl + args.header[12:]
    toc = extract_toc(args.header)
    preprocessed = preprocess(args.header, ['-I%s' % idir for idir in args.include_directory])
    enum_nodes = sorted(extract_enums(toc, preprocessed), key=lambda x: x.ext[0].name)
    with open(args.output, 'w', encoding='utf-8') as output, \
         open(args.output + 'i', 'w', encoding='utf-8') as stub_output, \
         open(args.rstdoc, 'w', encoding='utf-8') as rstdoc:
        header_fname = basename(args.header)
        mod_name = splitext(header_fname)[0]
        output.write(PY_HEADER % (header_fname, libpg_query_version))
        stub_output.write(PYI_HEADER % (header_fname, libpg_query_version))
        stub_enum_types = set()
        for node in enum_nodes:
            enum_type, __ = determine_enum_type_and_value(node.ext[0].type.type)
            stub_enum_types.add('Enum' if enum_type == 'StrEnum' else enum_type)
        if stub_enum_types:
            stub_output.write('\nfrom enum import %s\n' %
                              ', '.join(sorted(stub_enum_types)))
        rstdoc.write(RST_HEADER % dict(
            mod_name=mod_name, header_fname=header_fname,
            extra_decoration='='*(len(mod_name) + len(header_fname)),
            header_url=header_url))

        for node in enum_nodes:
            enum = node.ext[0].type.type
            write_enum(enum.name or node.ext[0].name, enum, output)
            write_enum_stub(enum.name or node.ext[0].name, enum, stub_output)
            write_enum_doc(enum.name or node.ext[0].name, enum, rstdoc, toc, header_url,
                           mod_name)

        separator_emitted = False
        with open(args.header, encoding='utf-8') as header:
            for constant, value in extract_defines(header.read()):
                if not separator_emitted:
                    output.write('\n\n')
                    output.write('# #define-ed constants\n')
                    rstdoc.write('\n')
                    separator_emitted = True
                output.write('\n%s = %s\n' % (constant, value))
                stub_output.write('\n%s: %s\n' % (constant, define_stub_type(value)))
                rstdoc.write('\n.. data:: %s\n' % constant)
                if constant in toc:
                    rstdoc.write('\n   See `here for details <%s#L%d>`__.\n'
                                 % (header_url, toc[constant]))


def main():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(description="PG enum extractor",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('-I', '--include-directory', action='append', metavar='DIR',
                        help="add DIR to the list of include directories")
    parser.add_argument('header',
                        help="source header to be processed")
    parser.add_argument('output',
                        help="Python source to be created")
    parser.add_argument('rstdoc',
                        help="reST documentation to be created")

    args = parser.parse_args()

    workhorse(args)


if __name__ == '__main__':
    main()
