# -*- coding: utf-8; mode: python -*-
# :Project:   pg_query -- Pythonic wrapper around libpg_query
# :Created:   mer 02 ago 2017 15:20:43 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

from pathlib import Path

from setuptools import setup, find_packages
from distutils.extension import Extension
try:
    from Cython.Build import cythonize
except ImportError:
    cythonize = lambda e: e
    extension_source = 'pg_query/parser.c'
else:
    extension_source = 'pg_query/parser.pyx'


here = Path(__file__).absolute().parent
with (here / 'README.rst').open(encoding='utf-8') as f:
    README = f.read()
with (here / 'CHANGES.rst').open(encoding='utf-8') as f:
    CHANGES = f.read()
with (here / 'version.txt').open(encoding='utf-8') as f:
    VERSION = f.read().strip()


setup(
    name="pg_query",
    version=VERSION,
    url="https://github.com/lelit/pg_query",

    description="Pythonic wrapper around libpg_query",
    long_description=README + '\n\n' + CHANGES,

    author="Lele Gaifax",
    author_email="lele@metapensiero.it",

    license="GPLv3+",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        ],
    keywords="",

    packages=find_packages('pg_query'),

    ext_modules = cythonize([
        Extension('pg_query.parser', [extension_source],
                  libraries=['pg_query'],
                  include_dirs=[str(here / 'libpg_query')],
                  library_dirs=[str(here / 'libpg_query')]),
    ]),

    install_requires=['setuptools'],
    extras_require={
        'dev': [
            'cython',
            'metapensiero.tool.bump_version',
            'pycparser',
            'readme_renderer',
        ]
    },
)
