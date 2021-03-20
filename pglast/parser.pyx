# -*- coding: utf-8 -*-
# :Project:   pglast -- Cython interface with libpg_query
# :Created:   mer 02 ago 2017 15:12:49 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021 Lele Gaifax
#

#cython: language_level=3

from cpython.bytes cimport PyBytes_AsStringAndSize, PyBytes_FromStringAndSize
from libc.stdint cimport uint64_t
from libc cimport limits

from . import Error
from . cimport structs


include "ast.pyx"


class ParseError(Error):
    "Exception representing the error state returned by the PG parser."

    def __init__(self, message, location):
        super().__init__(message)
        self.location = location

    def __str__(self):
        message = self.args[0]
        return f"{message}, at location {self.location}"


class DeparseError(Error):
    "Exception representing the error state returned by the PG deparser."

    def __init__(self, message, location):
        super().__init__(message)
        self.location = location

    def __str__(self):
        message = self.args[0]
        return f"{message}, at location {self.location}"


cdef extern from "pg_query.h" nogil:

    int PG_VERSION_NUM

    ctypedef struct PgQueryError:
        char* message
        int lineno
        int cursorpos

    ctypedef struct PgQueryParseResult:
        char* parse_tree
        PgQueryError *error

    ctypedef struct PgQueryProtobuf:
        unsigned int len
        char* data

    ctypedef struct PgQueryProtobufParseResult:
        PgQueryProtobuf parse_tree
        PgQueryError* error;

    ctypedef struct PgQueryPlpgsqlParseResult:
        char* plpgsql_funcs
        PgQueryError* error

    ctypedef struct PgQueryFingerprintResult:
        char* fingerprint_str
        char* stderr_buffer
        PgQueryError* error

    ctypedef struct PgQuerySplitStmt:
        int stmt_location
        int stmt_len

    ctypedef struct PgQuerySplitResult:
        PgQuerySplitStmt** stmts
        int n_stmts
        char* stderr_buffer
        PgQueryError* error

    ctypedef struct PgQueryDeparseResult:
        char* query
        PgQueryError* error

    PgQueryParseResult pg_query_parse(const char* input)
    void pg_query_free_parse_result(PgQueryParseResult result)

    PgQueryProtobufParseResult pg_query_parse_protobuf(const char* input)
    void pg_query_free_protobuf_parse_result(PgQueryProtobufParseResult result)

    PgQueryPlpgsqlParseResult pg_query_parse_plpgsql(const char* input)
    void pg_query_free_plpgsql_parse_result(PgQueryPlpgsqlParseResult result)

    PgQueryFingerprintResult pg_query_fingerprint(const char* input)
    void pg_query_free_fingerprint_result(PgQueryFingerprintResult result)

    PgQueryDeparseResult pg_query_deparse_protobuf(PgQueryProtobuf parse_tree)
    void pg_query_free_deparse_result(PgQueryDeparseResult result)

    PgQuerySplitResult pg_query_split_with_scanner(const char* input)
    PgQuerySplitResult pg_query_split_with_parser(const char* input)
    void pg_query_free_split_result(PgQuerySplitResult result)


cdef extern from "src/pg_query_internal.h" nogil:
    ctypedef struct PgQueryInternalParsetreeAndError:
        structs.List* tree
        char* stderr_buffer
        PgQueryError* error

    ctypedef void* MemoryContext

    MemoryContext pg_query_enter_memory_context()
    void pg_query_exit_memory_context(MemoryContext ctx)

    PgQueryInternalParsetreeAndError pg_query_raw_parse(const char* input)


LONG_MAX = limits.LONG_MAX


def get_postgresql_version():
    "Return the ``PostgreSQL`` version as a tuple (`major`, `minor`)."

    version = PG_VERSION_NUM
    major, minor = divmod(version, 10_000)
    return (major, minor)


def parse_sql(str query):
    "Parse the given ``SQL`` `query` and return its abstract parse tree."

    cdef PgQueryInternalParsetreeAndError parsed
    cdef MemoryContext mctx
    cdef int i
    cdef const char *cstring

    utf8 = query.encode('utf-8')
    cstring = utf8

    mctx = pg_query_enter_memory_context()

    with nogil:
        parsed = pg_query_raw_parse(cstring)

    try:
        if parsed.tree is not NULL:
            stmts = PyTuple_New(parsed.tree.length)
            for i in range(parsed.tree.length):
                item = create(structs.list_nth(parsed.tree, i))
                Py_INCREF(item)
                PyTuple_SET_ITEM(stmts, i, item)
            return stmts
        elif parsed.error is NULL:
            return ()
        else:
            message = parsed.error.message.decode('utf8')
            cursorpos = parsed.error.cursorpos
            raise ParseError(message, cursorpos)
    finally:
        pg_query_exit_memory_context(mctx);


def parse_sql_json(str query):
    "Parse the given ``SQL`` `query` and return its JSON encoded parse tree."

    cdef PgQueryParseResult parsed
    cdef const char *cstring

    utf8 = query.encode('utf-8')
    cstring = utf8

    with nogil:
        parsed = pg_query_parse(cstring)

    try:
        if parsed.error:
            message = parsed.error.message.decode('utf8')
            cursorpos = parsed.error.cursorpos
            raise ParseError(message, cursorpos)

        return parsed.parse_tree.decode('utf8')
    finally:
        with nogil:
            pg_query_free_parse_result(parsed)


def parse_sql_protobuf(str query):
    "Parse the given ``SQL`` `query` and return its Protobuf encoded parse tree."

    cdef PgQueryProtobufParseResult parsed
    cdef const char *cstring

    utf8 = query.encode('utf-8')
    cstring = utf8

    with nogil:
        parsed = pg_query_parse_protobuf(cstring)

    try:
        if parsed.error:
            message = parsed.error.message.decode('utf8')
            cursorpos = parsed.error.cursorpos
            raise ParseError(message, cursorpos)

        return PyBytes_FromStringAndSize(parsed.parse_tree.data, parsed.parse_tree.len)
    finally:
        with nogil:
            pg_query_free_protobuf_parse_result(parsed)


def parse_plpgsql_json(str query):
    "Parse the given ``pgpgsql`` `query` and return its JSON encoded parse tree."

    cdef PgQueryPlpgsqlParseResult parsed
    cdef const char *cstring

    utf8 = query.encode('utf-8')
    cstring = utf8

    with nogil:
        parsed = pg_query_parse_plpgsql(cstring)

    try:
        if parsed.error:
            message = parsed.error.message.decode('utf8')
            cursorpos = parsed.error.cursorpos
            raise ParseError(message, cursorpos)

        return parsed.plpgsql_funcs.decode('utf8')
    finally:
        with nogil:
            pg_query_free_plpgsql_parse_result(parsed)


def fingerprint(str query):
    "Compute and return a *signature* of the given ``SQL`` `query`."

    cdef PgQueryFingerprintResult result
    cdef const char *cstring

    utf8 = query.encode('utf-8')
    cstring = utf8

    with nogil:
        result = pg_query_fingerprint(cstring)

    try:
        if result.error:
            message = result.error.message.decode('utf8')
            cursorpos = result.error.cursorpos
            raise ParseError(message, cursorpos)

        return result.fingerprint_str.decode('ascii')
    finally:
        with nogil:
            pg_query_free_fingerprint_result(result)


def split(str stmts, bint with_parser=True, bint only_slices=False):
    """Split the given `stmts` string into a sequence of the single ``SQL`` statements.

    By default this uses the *parser* to perform the job; when `with_parser` is ``False``
    the *scanner* variant is used, indicated when the statements may contain parse errors.

    When `only_slices` is ``True``, return a sequence of ``slice`` instances, one for each
    statement, instead of statements text.

    NB: leading and trailing whitespace are removed from the statements.
    """

    cdef PgQuerySplitResult splitted
    cdef const char *cstring
    cdef int i = 0
    cdef int prev_offset = 0
    cdef int start
    cdef int end
    utf8 = stmts.encode('utf-8')
    cstring = utf8

    with nogil:
        if with_parser:
            splitted = pg_query_split_with_parser(cstring)
        else:
            splitted = pg_query_split_with_scanner(cstring)

    try:
        if splitted.error:
            message = splitted.error.message.decode('utf8')
            cursorpos = splitted.error.cursorpos
            raise ParseError(message, cursorpos)

        result = []
        while i < splitted.n_stmts:
            start = splitted.stmts[i].stmt_location
            end = splitted.stmts[i].stmt_location + splitted.stmts[i].stmt_len
            stmt = utf8[start:end].decode('utf-8').strip()
            if only_slices:
                # Adjust offsets, we remove leading/trailing whitespace above
                cur_offset = stmts.index(stmt, prev_offset)
                result.append(slice(cur_offset, cur_offset + len(stmt)))
                prev_offset = cur_offset + 1
            else:
                result.append(stmt)
            i += 1
        return tuple(result)
    finally:
        with nogil:
            pg_query_free_split_result(splitted)


def deparse(bytes protobuf):
    "Convert the `protobuf` serialized parse tree into an equivalent ``SQL`` statement."

    cdef PgQueryProtobuf tree
    cdef PgQueryDeparseResult deparsed

    PyBytes_AsStringAndSize(protobuf, &tree.data, <Py_ssize_t *>&tree.len)
    with nogil:
         deparsed = pg_query_deparse_protobuf(tree)

    try:
        if deparsed.error:
            message = deparsed.error.message.decode('utf8')
            cursorpos = deparsed.error.cursorpos
            raise ParseError(message, cursorpos)

        return deparsed.query.decode('utf-8')
    finally:
        with nogil:
            pg_query_free_deparse_result(deparsed)
