# -*- coding: utf-8 -*-
# :Project:   pglast -- Extract keywords from PostgreSQL header
# :Created:   dom 06 ago 2017 23:34:53 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018 Lele Gaifax
#

from collections import defaultdict
from os.path import basename
from pprint import pformat
from re import match
import subprocess


HEADER = """\
# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from %s @ %s
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#
"""


def get_libpg_query_version():
    result = subprocess.check_output(['git', 'describe', '--all', '--long'],
                                     cwd='libpg_query')
    return result.decode('utf-8').strip().split('/')[-1]


def extract_keywords(source):
    for line in source.splitlines():
        if line.startswith('PG_KEYWORD'):
            m = match(r'PG_KEYWORD\("([^"]+)",[^,]+,\s*([\w_]+)\)', line.strip())
            if m:
                yield m.group(1), m.group(2)


def workhorse(args):
    with open(args.header, encoding='utf-8') as f:
        source = f.read()

    bytype = defaultdict(set)
    for keyword, type in extract_keywords(source):
        bytype[type].add(keyword)

    with open(args.output, 'w', encoding='utf-8') as output:
        output.write(HEADER % (basename(args.header), get_libpg_query_version()))
        for type in sorted(bytype):
            output.write('\n')
            output.write(type + 'S')
            output.write(' = {')
            keywords = pformat(bytype[type], compact=True, indent=len(type)+5, width=95)
            output.write(keywords[1:].lstrip())
            output.write('\n')


def main():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(description="PG keyword extractor",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('header',
                        help="source header to be processed")
    parser.add_argument('output',
                        help="Python source to be created")

    args = parser.parse_args()

    workhorse(args)


if __name__ == '__main__':
    main()
