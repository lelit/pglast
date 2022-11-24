# -*- coding: utf-8 -*-
# :Project:   pglast -- PostgreSQL Languages AST
# :Created:   mer 02 ago 2017 15:11:02 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2022 Lele Gaifax
#

from collections import namedtuple

from . import enums
from .error import Error
try:
    from .parser import fingerprint, get_postgresql_version, parse_sql, scan, split
except ModuleNotFoundError:  # pragma: no cover
    # bootstrap
    pass


# This is injected automatically at release time
__version__ = 'v4.0.dev0'
"Package's version."

__author__ = 'Lele Gaifax <lele@metapensiero.it>'
"Package's author."


def parse_plpgsql(statement):
    from json import loads
    from .parser import parse_plpgsql_json

    return loads(parse_plpgsql_json(statement))


Comment = namedtuple('Comment', ('location', 'text', 'at_start_of_line', 'continue_previous'))
"A structure to carry information about a single SQL comment."


def _extract_comments(statement):
    lines = []
    lofs = 0
    for line in statement.splitlines(True):
        llen = len(line)
        lines.append((lofs, lofs+llen, line))
        lofs += llen
    comments = []
    continue_previous = False
    for token in scan(statement):
        if token.name in ('C_COMMENT', 'SQL_COMMENT'):
            for bol_ofs, eol_ofs, line in lines:
                if bol_ofs <= token.start < eol_ofs:
                    break
            else:  # pragma: no cover
                raise RuntimeError('Uhm, logic error!')
            at_start_of_line = not line[:token.start - bol_ofs].strip()
            text = statement[token.start:token.end+1]
            comments.append(Comment(token.start, text, at_start_of_line, continue_previous))
            continue_previous = True
        else:
            continue_previous = False
    return comments


def prettify(statement, safety_belt=False, preserve_comments=False, **options):
    r"""Render given `statement` into a prettified format.

    :param str statement: the SQL statement(s)
    :param bool safety_belt: whether to perform a safe check against bugs in pglast's
                             serialization
    :param bool preserve_comments: whether comments shall be preserved, defaults to not
    :param \*\*options: any keyword option accepted by :class:`~.stream.IndentedStream`
                        constructor
    :returns: a string with the equivalent prettified statement(s)

    When `safety_belt` is ``True``, the resulting statement is parsed again and its *AST*
    compared with the original statement: if they don't match, a warning is emitted and the
    original statement is returned. By default it is ``False``, so no double check is done.
    """

    # Intentional lazy imports, so the modules are loaded on demand

    from .stream import IndentedStream
    from . import printers  # noqa

    if preserve_comments:
        options['comments'] = _extract_comments(statement)

    orig_pt = parse_sql(statement)
    prettified = IndentedStream(**options)(orig_pt)
    if safety_belt:
        from logging import getLogger
        import warnings

        try:
            pretty_pt = parse_sql(prettified)
        except Error as e:
            logger = getLogger(__file__)
            logger.warning("Detected a bug in pglast serialization, original statement:\n\n"
                           "%s\n\nhas been serialized to the following invalid one:\n\n%s",
                           statement, prettified)
            warnings.warn(f"Detected a bug in pglast serialization, please report: {e}",
                          RuntimeWarning)
            return statement

        if pretty_pt != orig_pt:
            logger = getLogger(__file__)
            logger.warning("Detected a non-cosmetic difference between this original"
                           " statement:\n\n%s\n\nand the prettified one:\n\n%s",
                           statement, prettified)
            warnings.warn("Detected a non-cosmetic difference between original and"
                          " prettified statements, please report",  RuntimeWarning)
            return statement

    return prettified


__all__ = ('Error', 'enums', 'fingerprint', 'get_postgresql_version',
           'parse_plpgsql', 'parse_sql', 'prettify', 'split')
