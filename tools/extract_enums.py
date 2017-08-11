# -*- coding: utf-8 -*-
# :Project:   pg_query -- Extract enums from PostgreSQL headers
# :Created:   gio 03 ago 2017 14:54:39 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

from os.path import basename
from re import match
import subprocess

from pycparser import c_ast, c_parser


HEADER = """\
# -*- coding: utf-8 -*-
# :Project:   pg_query -- DO NOT EDIT: automatically extracted from %s @ %s
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

try:
    from enum import Enum, IntEnum, IntFlag, auto
except ImportError:
    # Python < 3.6
    from aenum import Enum, IntEnum, IntFlag, auto

"""


def get_libpg_query_info():
    "Return a tuple with (version, baseurl) of the libpg_query library."

    version = subprocess.check_output(['git', 'describe', '--all', '--long'],
                                      cwd='libpg_query')
    version = version.decode('utf-8').strip().split('/')[1]
    remote = subprocess.check_output(['git', 'remote', 'get-url', 'origin'],
                                      cwd='libpg_query')
    remote = remote.decode('utf-8')
    baseurl = '%s/blob/%s/' % (remote[:-5], version[-7:])
    return version, baseurl


def preprocess(fname, cpp_args=[]):
    "Preprocess the given header and return the result."

    result = subprocess.check_output(['cpp', '-E', *cpp_args, fname])

    return result.decode('utf-8')


def extract_toc(header):
    "Extract the enums and defines with their position in the header."

    toc = {}

    with open(header, encoding='utf-8') as f:
        content = f.read()

    for lineno, line in enumerate(content.splitlines(), 1):
        if line.startswith('typedef enum '):
            m = match(r'typedef enum\s+([\w_]+)', line)
            if m is not None:
                toc[m.group(1)] = lineno
        elif line.startswith('#define '):
            m = match(r'#define\s+([A-Z_]+)', line)
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
            elif line.startswith('typedef enum '):
                in_typedef = True
                typedef.append(line)

    parser = c_parser.CParser()
    for typedef in typedefs:
        td = parser.parse(''.join(typedef))
        if td.ext[0].name in toc:
            yield td


def extract_defines(source):
    "Yield all #defined constants in the given header."

    for line in source.splitlines():
        if line and line.startswith('#define '):
            m = match(r'#define\s+([A-Z_]+)\s+\(?(\d+<<\d+|0x\d+)\)?', line)
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


def int_enum_value_factory(index, enumerator):
    if enumerator.value is None:
        return '0' if index==0 else 'auto()'

    if isinstance(enumerator.value, c_ast.BinaryOp):
        return emit_binary_op(enumerator.value)
    elif isinstance(enumerator.value, c_ast.Constant):
        return emit_constant(enumerator.value)
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
                type = 'str, Enum'
                value = char_enum_value_factory
                break
            elif isinstance(item.value, c_ast.BinaryOp) and item.value.op == '<<':
                type = 'IntFlag'
                break

    return type, value


def write_enum(enum, output, toc, url):
    enum_type, value_factory = determine_enum_type_and_value(enum)
    output.write('\n')
    output.write('class %s(%s):\n' % (enum.name, enum_type))
    if enum.name in toc:
        output.write('    "See `here for details <%s#L%d>`__."\n\n' % (url, toc[enum.name]))
    for index, item in enumerate(enum.values.enumerators):
        output.write('    %s = %s\n' % (item.name, value_factory(index, item)))


def workhorse(args):
    libpg_query_version, libpg_query_baseurl = get_libpg_query_info()
    header_url = libpg_query_baseurl + args.header[12:]
    toc = extract_toc(args.header)
    preprocessed = preprocess(args.header, ['-I%s' % idir for idir in args.include_directory])
    with open(args.output, 'w', encoding='utf-8') as output:
        output.write(HEADER % (basename(args.header), libpg_query_version))
        for node in sorted(extract_enums(toc, preprocessed),
                           key=lambda x: x.ext[0].name):
            write_enum(node.ext[0].type.type, output, toc, header_url)

        separator_emitted = False
        with open(args.header, encoding='utf-8') as header:
            for constant, value in extract_defines(header.read()):
                if not separator_emitted:
                    output.write('\n\n')
                    output.write('# #define-ed constants\n')
                    separator_emitted = True
                output.write('\n%s = %s\n' % (constant, value))
                if constant in toc:
                    output.write('"See `here for details <%s#L%d>`__."\n'
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

    args = parser.parse_args()

    workhorse(args)


if __name__ == '__main__':
    main()
