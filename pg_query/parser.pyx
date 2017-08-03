# -*- coding: utf-8 -*-
# :Project:   pg_query -- Cython interface with libpg_query
# :Created:   mer 02 ago 2017 15:12:49 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

#cython: language_level=3


import json

from . import Error


class ParseError(Error):
    "Exception representing the error state returned by the PG parser."

    def __init__(self, message, location):
        super().__init__(message)
        self.location = location

    def __str__(self):
        message = self.args[0]
        return f"{message}, at location {self.location}"


cdef extern from "pg_query.h":

    ctypedef struct PgQueryError:
        char *message
        int lineno
        int cursorpos

    ctypedef struct PgQueryParseResult:
        char *parse_tree
        PgQueryError *error

    ctypedef struct PgQueryPlpgsqlParseResult:
        char *plpgsql_funcs
        PgQueryError *error

    PgQueryParseResult pg_query_parse(const char* input)
    void pg_query_free_parse_result(PgQueryParseResult result)

    PgQueryPlpgsqlParseResult pg_query_parse_plpgsql(const char* input)
    void pg_query_free_plpgsql_parse_result(PgQueryPlpgsqlParseResult result)


def parse_sql(str query):
    cdef PgQueryParseResult parsed

    parsed = pg_query_parse(query.encode('utf-8'))
    try:
        if parsed.error:
            message = parsed.error.message.decode('utf8')
            cursorpos = parsed.error.cursorpos
            raise ParseError(message, cursorpos)

        result = json.loads(parsed.parse_tree.decode('utf8'))
        return result
    finally:
        pg_query_free_parse_result(parsed)


def parse_plpgsql(str query):
    cdef PgQueryPlpgsqlParseResult parsed

    parsed = pg_query_parse_plpgsql(query.encode('utf-8'))
    try:
        if parsed.error:
            message = parsed.error.message.decode('utf8')
            cursorpos = parsed.error.cursorpos
            raise ParseError(message, cursorpos)

        result = json.loads(parsed.plpgsql_funcs.decode('utf8'))
        return result
    finally:
        pg_query_free_plpgsql_parse_result(parsed)
