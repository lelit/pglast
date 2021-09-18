# -*- coding: utf-8 -*-
# :Project:   pglast -- Simple frontend to the pretty reformatter
# :Created:   dom 06 ago 2017 23:09:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021 Lele Gaifax
#

import argparse
import json
import pprint
import sys

from pglast import Error, parse_plpgsql, parse_sql, prettify


def workhorse(args):
    if args.statement:
        statement = args.statement
    else:
        input = args.infile or sys.stdin
        with input:
            statement = input.read()

    if args.parse_tree or args.plpgsql:
        tree = parse_plpgsql(statement) if args.plpgsql else parse_sql(statement)
        output = args.outfile or sys.stdout
        with output:
            if args.plpgsql:
                json.dump(tree, output, sort_keys=True, indent=2)
            else:
                pprint.pprint([stmt(skip_none=True) for stmt in tree], output)
            output.write('\n')
    else:
        try:
            prettified = prettify(
                statement,
                preserve_comments=args.preserve_comments,
                compact_lists_margin=args.compact_lists_margin,
                split_string_literals_threshold=args.split_string_literals,
                special_functions=args.special_functions,
                comma_at_eoln=args.comma_at_eoln,
                remove_pg_catalog_from_functions=args.remove_pg_catalog_from_functions,
                semicolon_after_last_statement=args.semicolon_after_last_statement)
        except Error as e:
            print()
            raise SystemExit(e)

        output = args.outfile or sys.stdout
        with output:
            output.write(prettified)
            output.write('\n')


def main(options=None):
    from argparse import ArgumentParser
    from pkg_resources import get_distribution
    from .parser import get_postgresql_version

    version = '%s, with PostgreSQL %s parser' % (
        get_distribution('pglast').version,
        '.'.join(str(p) for p in get_postgresql_version()))

    parser = ArgumentParser(description="PostgreSQL language prettifier")

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version,)
    parser.add_argument('-p', '--plpgsql', action='store_true', default=False,
                        help='use the plpgsql parser (and print just the resulting tree)')
    parser.add_argument('-t', '--parse-tree', action='store_true', default=False,
                        help='show just the parse tree of the statement')
    parser.add_argument('-m', '--compact-lists-margin', type=int, default=0,
                        help='use compact form for lists not exceeding the given margin')
    parser.add_argument('-s', '--split-string-literals', type=int, default=0,
                        help='split string literals longer than given value')
    parser.add_argument('-f', '--special-functions', action='store_true', default=False,
                        help='activate special functions handling')
    parser.add_argument('-F', '--remove-pg_catalog-from-functions', action='store_true',
                        default=False,
                        help='omit explicit "pg_catalog" schema from function names,'
                        ' when possible')
    parser.add_argument('-c', '--comma-at-eoln', action='store_true', default=False,
                        help='use alternative style to print lists, putting the comma right'
                        ' after each item')
    parser.add_argument('-e', '--semicolon-after-last-statement', action='store_true',
                        default=False, help='end the last statement with a semicolon')
    parser.add_argument('-C', '--preserve-comments', action='store_true',
                        default=False, help="preserve comments in the statement")
    parser.add_argument('-S', '--statement',
                        help='the SQL statement')
    parser.add_argument('infile', nargs='?', type=argparse.FileType(),
                        help='a file containing the SQL statement to be pretty-printed,'
                        ' by default stdin, when not specified with --statement option')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        help='where the result will be written, by default stdout')

    args = parser.parse_args(options if options is not None else sys.argv[1:])

    workhorse(args)


if __name__ == '__main__':  # pragma: no cover
    main()
