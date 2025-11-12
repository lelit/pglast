# -*- coding: utf-8; mode: python -*-
# :Project:   pglast — PostgreSQL Languages AST
# :Created:   mer 02 ago 2017 15:20:43 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2020, 2021, 2022, 2024, 2025 Lele Gaifax
#

from os import fspath
from pathlib import Path
import subprocess
import sys

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


here = Path(__file__).absolute().parent

libpg_query_dir = here / 'libpg_query'
include_dir = libpg_query_dir / 'src' / 'postgres' / 'include'
vendor_dir = libpg_query_dir / 'vendor'

include_dirs = [libpg_query_dir, vendor_dir, include_dir]

if sys.platform == 'win32':
    include_dirs.append(include_dir / 'port' / 'win32')
    include_dirs.append(include_dir / 'port' / 'win32_msvc')
    make_cmd = make = ['nmake', '/F', 'Makefile.msvc', 'build']
else:
    make_cmd = ['make', '-s', 'build']


class BuildLibPgQueryFirst(build_ext):
    def run(self):
        subprocess.check_call(make_cmd, cwd=libpg_query_dir)
        super().run()


setup(
    cmdclass={'build_ext': BuildLibPgQueryFirst},
    ext_modules=[
        Extension(
            'pglast.parser',
            sources=['pglast/parser.c'],
            libraries=['pg_query'],
            include_dirs=[fspath(p) for p in include_dirs],
            library_dirs=[fspath(libpg_query_dir)]
        ),
    ],
)
