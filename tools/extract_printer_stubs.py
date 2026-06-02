# -*- coding: utf-8 -*-
# :Project:   pglast — Extract type stubs from printer modules
# :Created:   dom 24 mag 2026, 22:48
# :Author:    Alexander Macdonald <alex@alexmac.cc>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2026 Alexander Macdonald
#

import ast as pyast
from datetime import date
from io import StringIO
from pathlib import Path


CYEARS = f'2017-{date.today().year}'


HEADER = f"""\
# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: type stubs automatically extracted from %s
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © {CYEARS} Lele Gaifax
#

"""


def dotted_name(node):
    "Return the dotted name represented by an AST node, or ``None``."

    if isinstance(node, pyast.Name):
        return node.id
    if isinstance(node, pyast.Attribute):
        prefix = dotted_name(node.value)
        return None if prefix is None else f'{prefix}.{node.attr}'
    return None


def node_type_from_decorators(decorators):
    "Infer the printed node type from a ``node_printer`` or ``special_function`` decorator."

    for decorator in decorators:
        if not isinstance(decorator, pyast.Call):
            continue

        decorator_name = dotted_name(decorator.func)
        if decorator_name == 'special_function':
            return 'ast.FuncCall'

        if decorator_name != 'node_printer' or not decorator.args:
            continue

        node_arg = decorator.args[-1] if len(decorator.args) > 1 else decorator.args[0]
        node_arg_name = dotted_name(node_arg)
        if node_arg_name and node_arg_name.startswith('ast.'):
            return node_arg_name

    return None


def annotation_for_arg(arg, node_type, default=None):
    "Infer an annotation for a printer function argument."

    if arg.arg == 'node' and node_type is not None:
        return node_type
    if arg.arg == 'node':
        return 'ast.Node'
    if arg.arg == 'output':
        return 'RawStream'
    if isinstance(default, pyast.Constant):
        if isinstance(default.value, bool):
            return 'bool'
        if isinstance(default.value, int):
            return 'int'
        if isinstance(default.value, str):
            return 'str'
    return 'Any'


def return_annotation(function):
    "Infer a conservative return annotation for a function body."

    def is_bool_expression(node):
        if isinstance(node, pyast.Constant):
            return isinstance(node.value, bool)
        if isinstance(node, (pyast.BoolOp, pyast.Compare)):
            return True
        if isinstance(node, pyast.UnaryOp):
            return isinstance(node.op, pyast.Not)
        if isinstance(node, pyast.Call):
            return dotted_name(node.func) in ('bool', 'isinstance')
        return False

    def returns_from_body():
        pending = list(function.body)
        while pending:
            node = pending.pop()
            if isinstance(node, pyast.Return):
                if node.value is not None:
                    yield node.value
            elif not isinstance(
                node,
                (
                    pyast.FunctionDef,
                    pyast.AsyncFunctionDef,
                    pyast.ClassDef,
                    pyast.Lambda,
                ),
            ):
                pending.extend(pyast.iter_child_nodes(node))

    returns_with_value = [node for node in returns_from_body()]
    if not returns_with_value:
        return 'None'
    if all(is_bool_expression(value) for value in returns_with_value):
        return 'bool'
    return 'Any'


def emit_function(function, output, node_type=None, method=False):
    "Emit a function or method signature."

    args = []
    positional = list(function.args.posonlyargs) + list(function.args.args)
    defaults = [None] * (len(positional) - len(function.args.defaults))
    defaults += function.args.defaults
    for arg, default in zip(positional, defaults):
        if method and arg.arg == 'self':
            args.append('self')
            continue
        annotation = annotation_for_arg(arg, node_type, default)
        rendered = f'{arg.arg}: {annotation}'
        if default is not None:
            rendered += ' = ...'
        args.append(rendered)

    if function.args.vararg is not None:
        args.append(f'*{function.args.vararg.arg}: Any')
    elif function.args.kwonlyargs:
        args.append('*')

    for arg, default in zip(function.args.kwonlyargs, function.args.kw_defaults):
        rendered = f'{arg.arg}: Any'
        if default is not None:
            rendered += ' = ...'
        args.append(rendered)

    if function.args.kwarg is not None:
        args.append(f'**{function.args.kwarg.arg}: Any')

    indent = '    ' if method else ''
    output.write(
        f'{indent}def {function.name}({", ".join(args)})'
        f' -> {return_annotation(function)}: ...\n'
    )


def enum_assignment(class_def):
    "Return the enum class assigned to an ``IntEnumPrinter`` subclass, if any."

    for item in class_def.body:
        if isinstance(item, pyast.Assign):
            for target in item.targets:
                if isinstance(target, pyast.Name) and target.id == 'enum':
                    value = dotted_name(item.value)
                    if value and value.startswith('enums.'):
                        return value
    return None


def assignment_type(assign):
    "Infer a useful type for a module-level assignment."

    def is_int_expr(node):
        if isinstance(node, pyast.Constant):
            return type(node.value) is int
        if isinstance(node, pyast.BinOp):
            return is_int_expr(node.left) and is_int_expr(node.right)
        if isinstance(node, pyast.UnaryOp):
            return is_int_expr(node.operand)
        return False

    if is_int_expr(assign.value):
        return 'int'
    if isinstance(assign.value, pyast.Constant):
        return type(assign.value).__name__
    if isinstance(assign.value, pyast.Call):
        name = dotted_name(assign.value.func)
        if name and name.split('.')[-1].endswith('Printer'):
            return name.split('.')[-1]
    return 'Any'


def top_level_names(module):
    "Collect names needed to decide imports."

    has_classes = any(isinstance(item, pyast.ClassDef) for item in module.body)
    uses_enums = False
    for item in module.body:
        if isinstance(item, pyast.ClassDef) and enum_assignment(item):
            uses_enums = True
            break
    return has_classes, uses_enums


def write_stub(source, target):
    "Write a printer module stub for ``source``."

    tree = pyast.parse(source.read_text(encoding='utf-8'))
    has_classes, uses_enums = top_level_names(tree)
    body = StringIO()

    for item in tree.body:
        if isinstance(item, pyast.FunctionDef):
            if item.name.startswith('_'):
                continue
            node_type = node_type_from_decorators(item.decorator_list)
            emit_function(item, body, node_type)
            body.write('\n')
        elif isinstance(item, pyast.ClassDef):
            if item.name.startswith('_'):
                continue
            bases = [dotted_name(base) for base in item.bases]
            enum = enum_assignment(item)
            if 'IntEnumPrinter' in bases and enum is not None:
                base = f'IntEnumPrinter[{enum}]'
            elif 'IntEnumPrinter' in bases:
                base = 'IntEnumPrinter[Any]'
            else:
                base = 'object'
            body.write(f'class {item.name}({base}):\n')
            methods = [
                child
                for child in item.body
                if isinstance(child, pyast.FunctionDef)
                and not child.name.startswith('_')
            ]
            if enum is not None:
                body.write(f'    enum: ClassVar[type[{enum}]]\n')
            if methods:
                for method in methods:
                    emit_function(method, body, 'ast.Node', method=True)
            elif enum is None:
                body.write('    pass\n')
            body.write('\n\n')
        elif isinstance(item, pyast.Assign):
            for target_node in item.targets:
                if isinstance(
                    target_node, pyast.Name
                ) and not target_node.id.startswith('_'):
                    body.write(f'{target_node.id}: {assignment_type(item)}\n')
            body.write('\n')

    body_text = body.getvalue().rstrip() + '\n'
    with target.open('w', encoding='utf-8') as output:
        output.write(HEADER % source.name)
        typing_imports = []
        if 'Any' in body_text:
            typing_imports.append('Any')
        if 'ClassVar' in body_text:
            typing_imports.append('ClassVar')
        if typing_imports:
            output.write(f'from typing import {", ".join(typing_imports)}\n\n')
        output.write('from .. import ast')
        if uses_enums:
            output.write(', enums')
        output.write('\n')
        if 'RawStream' in body_text:
            output.write('from ..stream import RawStream\n')
        if has_classes:
            output.write('from . import IntEnumPrinter\n')
        output.write('\n')
        output.write(body_text)


def main():
    from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

    parser = ArgumentParser(
        description='Printer module type stub extractor',
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('source', type=Path, help="Python source to inspect")
    parser.add_argument('output', type=Path, help="Python type stub to create")

    args = parser.parse_args()
    write_stub(args.source, args.output)


if __name__ == '__main__':
    main()
