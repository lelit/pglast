# -*- coding: utf-8 -*-
# :Project:   pglast -- Extract printer functions doc
# :Created:   gio 09 nov 2017 12:56:35 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019 Lele Gaifax
#

from datetime import date
from ast import literal_eval
from os.path import basename, splitext
from re import match
import subprocess


RST_HEADER = """\
.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-%d Lele Gaifax
..

================================================%%(extra_decoration)s
 :mod:`pglast.printers.%%(mod_name)s` --- %%(mod_nick_name)s printer functions
================================================%%(extra_decoration)s

.. module:: pglast.printers.%%(mod_name)s
   :synopsis: %%(mod_nick_name)s printer functions
""" % date.today().year


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


def extract_toc(headers):
    "Extract the nodes position in the headers."

    toc = {}

    for header in headers:
        with open(header, encoding='utf-8') as f:
            content = f.read()

        for lineno, line in enumerate(content.splitlines(), 1):
            if line.startswith('typedef struct '):
                m = match(r'typedef struct\s+([\w_]+)', line)
                if m is not None:
                    toc[m.group(1)] = (header, lineno)

    # Add implicit "aliases"
    toc['Integer'] = toc['Float'] = toc['String'] = toc['BitString'] = toc['Null'] = \
        toc['Value']

    return toc


def extract_printers(source):
    "Extract printer functions implemented in `source`."

    printers = []

    with open(source, encoding='utf-8') as f:
        content = f.read()

    nps = []
    for line in content.splitlines():
        if line.startswith('@node_printer('):
            m = match(r'''@node_printer\((.*,\s)?['"]([\w_]+)['"]\)''', line)
            scope = m.group(1)
            if scope:
                scope = literal_eval(scope.rstrip(', '))
                if isinstance(scope, str):
                    scope = (scope,)
            node = m.group(2)
            nps.append((scope, node))
        elif line.startswith('def '):
            if nps:
                funcname = line[4:].split('(', 1)[0]
                for scope, node in nps:
                    printers.append((scope, node, funcname))
                nps = []

    return printers


def workhorse(args):
    libpg_query_version, libpg_query_baseurl = get_libpg_query_info()
    toc = extract_toc(args.headers)
    printers = extract_printers(args.source)
    with open(args.rstdoc, 'w', encoding='utf-8') as rstdoc:
        source_fname = basename(args.source)
        mod_name = splitext(source_fname)[0]
        rstdoc.write(RST_HEADER % dict(
            mod_name=mod_name, mod_nick_name=mod_name.upper(),
            extra_decoration='='*(len(mod_name) * 2)))
        for scope, node, funcname in printers:
            if scope:
                scoped = ", when it is inside "
                snode = scope[0]
                header, lineno = toc[snode]
                header_url = libpg_query_baseurl + header[12:]
                scoped += "a `%s <%s#L%d>`__" % (snode, header_url, lineno)
                for snode in scope[1:]:
                    header, lineno = toc[snode]
                    header_url = libpg_query_baseurl + header[12:]
                    scoped += " or a `%s <%s#L%d>`__" % (snode, header_url, lineno)
                scoped += ','
            else:
                scoped = ''
            header, lineno = toc[node]
            header_url = libpg_query_baseurl + header[12:]
            if scope:
                for snode in scope:
                    rstdoc.write('\n.. index::\n   pair: %s;%s\n' % (snode, node))
            else:
                rstdoc.write('\n.. index:: %s\n' % node)
            rstdoc.write('\n.. function:: %s(node, output)\n' % funcname)
            rstdoc.write('\n   Pretty print a `node` of type `%s <%s#L%d>`__%s to the `output`'
                         ' stream.\n' % (node, header_url, lineno, scoped))


def main():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(description="Printer functions doc extractor",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('source',
                        help="Python source module to be documented")
    parser.add_argument('rstdoc',
                        help="reST documentation to be created")
    parser.add_argument('headers', nargs='+',
                        help="The PG headers containing nodes definitions")
    args = parser.parse_args()

    workhorse(args)


if __name__ == '__main__':
    main()
