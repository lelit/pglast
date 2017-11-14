.. -*- coding: utf-8 -*-

Changes
-------

0.18 (2017-11-14)
~~~~~~~~~~~~~~~~~

- Fix endless loop due to sloppy conversion of command line option

- Install the command line tool as ``pgpp``


0.17 (2017-11-12)
~~~~~~~~~~~~~~~~~

- Rename printers.sql to printers.dml (**backward incompatibility**)

- List printer functions in the documentation, referencing the definition of related node type

- Fix inconsistent spacing in JOIN condition inside a nested expression

- Fix representation of unbound arrays

- Fix representation of ``interval`` data type

- Initial support for DDL statements

- Fix representation of string literals containing single quotes


0.16 (2017-10-31)
~~~~~~~~~~~~~~~~~

- Update libpg_query to 10-1.0.0


0.15 (2017-10-12)
~~~~~~~~~~~~~~~~~

- Fix indentation of boolean expressions in SELECT's targets (`issue #3`__)

__ https://github.com/lelit/pg_query/issues/3


0.14 (2017-10-09)
~~~~~~~~~~~~~~~~~

- Update to latest libpg_query's 10-latest branch, targeting PostgreSQL 10.0 final


0.13 (2017-09-17)
~~~~~~~~~~~~~~~~~

- Fix representation of subselects requiring surrounding parens


0.12 (2017-08-22)
~~~~~~~~~~~~~~~~~

- New option ``--version`` on the command line tool

- Better enums documentation

- Release the GIL while calling libpg_query functions


0.11 (2017-08-11)
~~~~~~~~~~~~~~~~~

- Nicer indentation for JOINs, making OUTER JOINs stand out

- Minor tweaks to lists rendering, with less spurious whitespaces

- New option ``--no-location`` on the command line tool


0.10 (2017-08-11)
~~~~~~~~~~~~~~~~~

- Support Python 3.4 and Python 3.5 as well as Python 3.6


0.9 (2017-08-10)
~~~~~~~~~~~~~~~~

- Fix spacing before the $ character

- Handle type modifiers

- New option ``--plpgsql`` on the command line tool, just for fun


0.8 (2017-08-10)
~~~~~~~~~~~~~~~~

- Add enums subpackages to the documentation with references to their related headers

- New ``compact_lists_margin`` option to produce a more compact representation when possible
  (see `issue #1`__)

__ https://github.com/lelit/pg_query/issues/1


0.7 (2017-08-10)
~~~~~~~~~~~~~~~~

- Fix sdist including the Sphinx documentation


0.6 (2017-08-10)
~~~~~~~~~~~~~~~~

- New option ``--parse-tree`` on the command line tool to show just the parse tree

- Sphinx documentation, available online


0.5 (2017-08-09)
~~~~~~~~~~~~~~~~

- Handle some more cases when a name must be double-quoted

- Complete the serialization of the WindowDef node, handling its frame options


0.4 (2017-08-09)
~~~~~~~~~~~~~~~~

- Expose the actual PostgreSQL version the underlying libpg_query libray is built on thru a new
  ``get_postgresql_version()`` function

- New option `safety_belt` for the ``prettify()`` function, to protect the innocents

- Handle serialization of ``CoalesceExpr`` and ``MinMaxExpr``


0.3 (2017-08-07)
~~~~~~~~~~~~~~~~

- Handle serialization of ``ParamRef`` nodes

- Expose a ``prettify()`` helper function


0.2 (2017-08-07)
~~~~~~~~~~~~~~~~

- Test coverage at 99%

- First attempt at automatic wheel upload to PyPI, let's see...


0.1 (2017-08-07)
~~~~~~~~~~~~~~~~

- First release ("Hi daddy!", as my soul would tag it)
