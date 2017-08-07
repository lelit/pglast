# -*- coding: utf-8 -*-
# :Project:   pg_query -- Simple frontend to the pretty reformatter
# :Created:   dom 06 ago 2017 23:09:23 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

import argparse
import sys

from pg_query import Error, prettify


def workhorse(args):
    input = args.infile or sys.stdin
    with input:
        statement = input.read()

    try:
        prettified = prettify(statement)
    except Error as e:
        print()
        raise SystemExit(e)

    output = args.outfile or sys.stdout
    with output:
        output.write(prettified)
        output.write('\n')


def main(options):
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(description="PostgreSQL language prettifier",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('infile', nargs='?', type=argparse.FileType(),
                        help='a file containing the SQL statement to be pretty-printed,'
                       ' by default stdin')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        help='where the result will be written, by default stdout')

    args = parser.parse_args(options)

    workhorse(args)


if __name__ == '__main__': #pragma: no cover
    main(sys.argv[1:])
