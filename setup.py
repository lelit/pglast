# -*- coding: utf-8; mode: python -*-
# :Project:   pglast -- PostgreSQL Languages AST
# :Created:   mer 02 ago 2017 15:20:43 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2020, 2021, 2022, 2024 Lele Gaifax
#

from pathlib import Path
import subprocess
import sys

from setuptools import Extension, setup, find_packages
from setuptools.command.build_ext import build_ext


here = Path(__file__).absolute().parent
with (here / 'README.rst').open(encoding='utf-8') as f:
    README = f.read()
with (here / 'CHANGES.rst').open(encoding='utf-8') as f:
    CHANGES = f.read()
with (here / 'version.txt').open(encoding='utf-8') as f:
    VERSION = f.read().strip()


LIBPG_QUERY_DIR = here / 'libpg_query'
SRC_DIR = LIBPG_QUERY_DIR / 'src'
INCLUDE_DIR = SRC_DIR / 'include'
PG_SRC_DIR = SRC_DIR / 'postgres'
PG_INCLUDE_DIR = PG_SRC_DIR / 'include'
VENDOR_DIR = LIBPG_QUERY_DIR / 'vendor'

SOURCES = ['pglast/parser.c']
SOURCES.extend(SRC_DIR.glob('*.c'))
SOURCES.extend(PG_SRC_DIR.glob('*.c'))
SOURCES.append(VENDOR_DIR / 'protobuf-c' / 'protobuf-c.c')
SOURCES.append(VENDOR_DIR / 'xxhash' / 'xxhash.c')
SOURCES.append(LIBPG_QUERY_DIR / 'protobuf' / 'pg_query.pb-c.c')


class BuildLibPgQueryFirst(build_ext):
    def run(self):
        if sys.platform == 'win32':
            make = ['nmake', '/F', 'Makefile.msvc', 'build']
        else:
            make = ['make', '-s', 'build']
        subprocess.check_call(make, cwd=LIBPG_QUERY_DIR)
        super().run()


setup(
    name="pglast",
    version=VERSION,
    url="https://github.com/lelit/pglast",

    description="PostgreSQL Languages AST and statements prettifier",
    long_description=README + '\n\n' + CHANGES,
    long_description_content_type='text/x-rst',

    author="Lele Gaifax",
    author_email="lele@metapensiero.it",

    license="GPLv3+",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: SQL",
        # "Programming Language :: PL/SQL",
        "Topic :: Database",
        "Topic :: Utilities",
        ],
    keywords="postgresql parser sql prettifier",

    packages=find_packages('.'),

    #cmdclass={'build_ext': BuildLibPgQueryFirst},
    ext_modules=[
        Extension(
            'pglast.parser',
            sources=list(map(str, SOURCES)),
            extra_compile_args=(['-Wno-unused-function',
                                 '-Wno-unused-value',
                                 '-Wno-unused-variable',
                                 '-Wno-unused-but-set-variable',
                                 '-Wno-sign-compare']
                                if sys.platform == 'linux'
                                else []),
            include_dirs=list(
                map(str, (LIBPG_QUERY_DIR, VENDOR_DIR, INCLUDE_DIR, PG_INCLUDE_DIR)
                    +
                    ((PG_INCLUDE_DIR / 'port' / 'win32',
                      PG_INCLUDE_DIR / 'port' / 'win32_msvc')
                     if sys.platform == 'win32'
                     else ()))),
        ),
    ],

    install_requires=[
        'setuptools',
    ],
    extras_require={
        'dev': [
            'cython',
            'metapensiero.tool.bump_version',
            'pycparser',
            'readme_renderer',
        ]
    },
    entry_points="""\
    [console_scripts]
    pgpp = pglast.__main__:main
    """,
)
