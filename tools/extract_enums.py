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

import enum

"""


def get_libpg_query_version():
    result = subprocess.check_output(['git', 'describe', '--all', '--long'],
                                     cwd='libpg_query')
    return result.decode('utf-8').strip().split('/')[1]


def preprocess(fname, cpp_args=[]):
    result = subprocess.check_output(['cpp', '-E', *cpp_args, fname])

    return result.decode('utf-8')


def extract_enums(source):
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
        yield parser.parse(''.join(typedef))


def extract_defines(source):
    for line in source.splitlines():
        if line and line.startswith('#define '):
            m = match(r'#define\s+([A-Z_]+)\s+\(?(\d+<<\d+|0x\d+)\)?', line)
            if m:
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
        return '0' if index==0 else 'enum.auto()'

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
    type = 'enum.IntEnum'
    value = int_enum_value_factory

    for item in enum.values.enumerators:
        if item.value:
            if isinstance(item.value, c_ast.Constant) and item.value.type == 'char':
                type = 'str, enum.Enum'
                value = char_enum_value_factory
                break
            elif isinstance(item.value, c_ast.BinaryOp) and item.value.op == '<<':
                type = 'enum.IntFlag'
                break

    return type, value


def write_enum(enum, output):
    enum_type, value_factory = determine_enum_type_and_value(enum)
    output.write('\n')
    output.write('class %s(%s):\n' % (enum.name, enum_type))
    for index, item in enumerate(enum.values.enumerators):
        output.write('    %s = %s\n' % (item.name, value_factory(index, item)))


def workhorse(args):
    preprocessed = preprocess(args.header, ['-I%s' % idir for idir in args.include_directory])
    with open(args.output, 'w', encoding='utf-8') as output:
        output.write(HEADER % (basename(args.header), get_libpg_query_version()))
        for node in sorted(extract_enums(preprocessed), key=lambda x: x.ext[0].name):
            write_enum(node.ext[0].type.type, output)

        separator_emitted = False
        with open(args.header, encoding='utf-8') as header:
            for constant, value in extract_defines(header.read()):
                if not separator_emitted:
                    output.write('\n\n')
                    output.write('# #define-ed constants\n\n')
                    separator_emitted = True
                output.write('%s = %s\n' % (constant, value))


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
