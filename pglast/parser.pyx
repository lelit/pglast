# -*- coding: utf-8 -*-
# :Project:   pglast -- Cython interface with libpg_query
# :Created:   mer 02 ago 2017 15:12:49 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2022, 2023 Lele Gaifax
#

#cython: language_level=3

from cpython.bytes cimport PyBytes_AsStringAndSize, PyBytes_FromStringAndSize
from cpython.list cimport PyList_New, PyList_SET_ITEM
from libc.stdint cimport int32_t, uint64_t, uint8_t
from libc cimport limits

from collections import namedtuple

from . import Error
from . cimport structs


include "ast.pyx"


class ParseError(Error):
    "Exception representing the error state returned by the PG parser."

    def __str__(self):
        message = self.args[0]
        if len(self.args) > 1:
            location = self.args[1]
            if location is not None:
                message += f', at index {location}'
        return message


class DeparseError(Error):
    "Exception representing the error state returned by the PG deparser."

    def __str__(self):
        message = self.args[0]
        if len(self.args) > 1:
            location = self.args[1]
            if location is not None:
                message += f', at position {location}'
        return message


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

    ctypedef struct PgQueryScanResult:
        PgQueryProtobuf pbuf
        PgQueryError *error

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

    PgQueryScanResult pg_query_scan(const char* input)
    void pg_query_free_scan_result(PgQueryScanResult result)

    int PG_QUERY_PARSE_DEFAULT


cdef extern from "src/pg_query_internal.h" nogil:
    ctypedef struct PgQueryInternalParsetreeAndError:
        structs.List* tree
        char* stderr_buffer
        PgQueryError* error

    ctypedef void* MemoryContext

    MemoryContext pg_query_enter_memory_context()
    void pg_query_exit_memory_context(MemoryContext ctx)

    PgQueryInternalParsetreeAndError pg_query_raw_parse(const char* input, int parser_options)


cdef extern from "protobuf-c/protobuf-c.h":
    ctypedef struct ProtobufCEnumDescriptor:
        pass

    ctypedef struct ProtobufCEnumValue:
        const char* name
        const char* c_name
        int value

    ProtobufCEnumValue* protobuf_c_enum_descriptor_get_value(const ProtobufCEnumDescriptor* d,
                                                             int value)


cdef extern from "protobuf/pg_query.pb-c.h" nogil:
    ctypedef enum PgQuery__Token:
        pass

    ctypedef enum PgQuery__KeywordKind:
        pass

    ctypedef struct PgQuery__ScanToken:
        int32_t start
        int32_t end
        PgQuery__Token token
        PgQuery__KeywordKind keyword_kind

    ctypedef struct PgQuery__ScanResult:
        size_t n_tokens
        PgQuery__ScanToken **tokens

    ProtobufCEnumDescriptor pg_query__token__descriptor
    ProtobufCEnumDescriptor pg_query__keyword_kind__descriptor

    PgQuery__ScanResult* pg_query__scan_result__unpack(void* allocator, size_t len,
                                                       const uint8_t* data)
    void pg_query__scan_result__free_unpacked(PgQuery__ScanResult* message, void* allocator)


LONG_MAX = limits.LONG_MAX


cdef class Displacements:
    """
    Helper class used to find the index of Unicode character from its offset in the
    corresponding UTF-8 encoded array.

    Example:

      >>> unicode = '€ 0.01'
      >>> utf8 = unicode.encode('utf-8')
      >>> d = pglast.parser.Displacements(unicode)
      >>> for offset in range(len(utf8)):
      ...   print(f'{offset} [{utf8[offset]:2x}] -> {d(offset)} [{unicode[d(offset)]}]')
      ...
      0 [e2] -> 0 [€]
      1 [82] -> 0 [€]
      2 [ac] -> 0 [€]
      3 [20] -> 1 [ ]
      4 [30] -> 2 [0]
      5 [2e] -> 3 [.]
      6 [30] -> 4 [0]
      7 [31] -> 5 [1]
    """

    # Build a sequence of (offset, index) tuples, for each character in the original string
    # that requires more than one byte once encoded in UTF-8. The sequence is kept in reverse
    # order, because to compute the index for an arbitrary offset we simply find the first
    # tuple with an offset less than or equal the given offset.

    cdef tuple displacements
    cdef unsigned long max_offset

    def __init__(self, str s):
        cdef unsigned long idx = 0
        cdef unsigned long ofs = 0
        cdef size_t c_len_in_utf8

        disps = []
        for c in s:
            c_len_in_utf8 = len(c.encode('utf-8'))
            if c_len_in_utf8 > 1:
                while c_len_in_utf8 > 0:
                    disps.append((ofs, idx))
                    c_len_in_utf8 -= 1
                    ofs += 1
            else:
                ofs += 1
            idx += 1
        self.max_offset = ofs - 1
        self.displacements = tuple(reversed(disps))

    def __call__(self, offset):
        if not 0 <= offset <= self.max_offset:
            # It may happen that the error is actually at the very end of the statement, giving
            # the message "syntax error at end of input", with a position that is beyond the
            # end of the string. Return None in such case
            return None

        for o, i in self.displacements:
            if o <= offset:
                return i + (offset - o)

        return offset


def get_postgresql_version():
    "Return the ``PostgreSQL`` version as a tuple (`major`, `minor`)."

    version = PG_VERSION_NUM
    major, minor = divmod(version, 10_000)
    return (major, minor)


def parse_sql(str query):
    "Parse the given ``SQL`` `query` and return its abstract syntax tree."

    cdef PgQueryInternalParsetreeAndError parsed
    cdef MemoryContext mctx
    cdef int i
    cdef const char *cstring

    utf8 = query.encode('utf-8')
    offset_to_index = Displacements(query)
    cstring = utf8

    mctx = pg_query_enter_memory_context()

    with nogil:
        parsed = pg_query_raw_parse(cstring, PG_QUERY_PARSE_DEFAULT)

    try:
        if parsed.tree is not NULL:
            stmts = PyTuple_New(parsed.tree.length)
            for i in range(parsed.tree.length):
                item = create(structs.list_nth(parsed.tree, i), offset_to_index)
                Py_INCREF(item)
                PyTuple_SET_ITEM(stmts, i, item)
            return stmts
        elif parsed.error is NULL:
            return ()
        else:
            message = parsed.error.message.decode('utf8')
            raise ParseError(message, offset_to_index(parsed.error.cursorpos-1))
    finally:
        pg_query_exit_memory_context(mctx);


def parse_sql_json(str query):
    "Parse the given ``SQL`` `query` and return its ``JSON`` encoded syntax tree."

    cdef PgQueryParseResult parsed
    cdef const char *cstring

    utf8 = query.encode('utf-8')
    cstring = utf8

    with nogil:
        parsed = pg_query_parse(cstring)

    try:
        if parsed.error:
            message = parsed.error.message.decode('utf8')
            offset_to_index = Displacements(query)
            raise ParseError(message, offset_to_index(parsed.error.cursorpos-1))

        return parsed.parse_tree.decode('utf8')
    finally:
        with nogil:
            pg_query_free_parse_result(parsed)


def parse_sql_protobuf(str query):
    "Parse the given ``SQL`` `query` and return its ``protobuf`` encoded syntax tree."

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
            offset_to_index = Displacements(query)
            raise ParseError(message, offset_to_index(parsed.error.cursorpos-1))

        return PyBytes_FromStringAndSize(parsed.parse_tree.data, parsed.parse_tree.len)
    finally:
        with nogil:
            pg_query_free_protobuf_parse_result(parsed)


def parse_plpgsql_json(str query):
    "Parse the given ``pgpgsql`` `query` and return its ``JSON`` encoded syntax tree."

    cdef PgQueryPlpgsqlParseResult parsed
    cdef const char *cstring

    utf8 = query.encode('utf-8')
    cstring = utf8

    with nogil:
        parsed = pg_query_parse_plpgsql(cstring)

    try:
        if parsed.error:
            message = parsed.error.message.decode('utf8')
            offset_to_index = Displacements(query)
            raise ParseError(message, offset_to_index(parsed.error.cursorpos-1))

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
            offset_to_index = Displacements(query)
            raise ParseError(message, offset_to_index(result.error.cursorpos-1))

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
            offset_to_index = Displacements(stmts)
            raise ParseError(message, offset_to_index(splitted.error.cursorpos-1))

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


def deparse_protobuf(bytes protobuf):
    "Convert the ``protobuf`` serialized parse tree into an equivalent ``SQL`` statement."

    cdef PgQueryProtobuf tree
    cdef PgQueryDeparseResult deparsed

    PyBytes_AsStringAndSize(protobuf, &tree.data, <Py_ssize_t *>&tree.len)
    with nogil:
         deparsed = pg_query_deparse_protobuf(tree)

    try:
        if deparsed.error:
            message = deparsed.error.message.decode('utf8')
            raise DeparseError(message, deparsed.error.cursorpos)

        return deparsed.query.decode('utf-8')
    finally:
        with nogil:
            pg_query_free_deparse_result(deparsed)


Token = namedtuple('Token', ('start', 'end', 'name', 'kind'))


def scan(str query):
    "Lexify the given ``SQL`` `query` and return a list of its lexical tokens."

    cdef PgQueryScanResult scanned
    cdef PgQuery__ScanResult* scan_result
    cdef PgQuery__ScanToken* scan_token
    cdef const ProtobufCEnumValue* tkind
    cdef const ProtobufCEnumValue* kwkind
    cdef const char* cstring
    cdef size_t i

    utf8 = query.encode('utf-8')
    offset_to_index = Displacements(query)
    cstring = utf8

    with nogil:
        scanned = pg_query_scan(cstring)

    try:
        if scanned.error:
            message = scanned.error.message.decode('utf8')
            raise ParseError(message, offset_to_index(scanned.error.cursorpos-1))

        with nogil:
            scan_result = pg_query__scan_result__unpack(NULL, scanned.pbuf.len,
                                                        <uint8_t*> scanned.pbuf.data)

        result = PyList_New(scan_result.n_tokens)

        for i in range(scan_result.n_tokens):
            scan_token = scan_result.tokens[i]
            tkind = protobuf_c_enum_descriptor_get_value(&pg_query__token__descriptor,
                                                         scan_token.token)
            kwkind = protobuf_c_enum_descriptor_get_value(&pg_query__keyword_kind__descriptor,
                                                          scan_token.keyword_kind)

            token = Token(offset_to_index(scan_token.start), offset_to_index(scan_token.end-1),
                          tkind.name.decode('ascii') if tkind != NULL else "UNKNOWN",
                          kwkind.name.decode('ascii'))
            Py_INCREF(token)
            PyList_SET_ITEM(result, i, token)

        with nogil:
            pg_query__scan_result__free_unpacked(scan_result, NULL)
    finally:
        with nogil:
            pg_query_free_scan_result(scanned)

    return result
