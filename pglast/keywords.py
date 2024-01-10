# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from kwlist.h @ 16.1
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2024 Lele Gaifax
#

COL_NAME_KEYWORDS = {'between', 'bigint', 'bit', 'boolean', 'char', 'character', 'coalesce',
                     'dec', 'decimal', 'exists', 'extract', 'float', 'greatest', 'grouping',
                     'inout', 'int', 'integer', 'interval', 'json_array', 'json_arrayagg',
                     'json_object', 'json_objectagg', 'least', 'national', 'nchar', 'none',
                     'normalize', 'nullif', 'numeric', 'out', 'overlay', 'position',
                     'precision', 'real', 'row', 'setof', 'smallint', 'substring', 'time',
                     'timestamp', 'treat', 'trim', 'values', 'varchar', 'xmlattributes',
                     'xmlconcat', 'xmlelement', 'xmlexists', 'xmlforest', 'xmlnamespaces',
                     'xmlparse', 'xmlpi', 'xmlroot', 'xmlserialize', 'xmltable'}

RESERVED_KEYWORDS = {'all', 'analyse', 'analyze', 'and', 'any', 'array', 'as', 'asc',
                     'asymmetric', 'both', 'case', 'cast', 'check', 'collate', 'column',
                     'constraint', 'create', 'current_catalog', 'current_date', 'current_role',
                     'current_time', 'current_timestamp', 'current_user', 'default',
                     'deferrable', 'desc', 'distinct', 'do', 'else', 'end', 'except', 'false',
                     'fetch', 'for', 'foreign', 'from', 'grant', 'group', 'having', 'in',
                     'initially', 'intersect', 'into', 'lateral', 'leading', 'limit',
                     'localtime', 'localtimestamp', 'not', 'null', 'offset', 'on', 'only',
                     'or', 'order', 'placing', 'primary', 'references', 'returning', 'select',
                     'session_user', 'some', 'symmetric', 'system_user', 'table', 'then', 'to',
                     'trailing', 'true', 'union', 'unique', 'user', 'using', 'variadic',
                     'when', 'where', 'window', 'with'}

TYPE_FUNC_NAME_KEYWORDS = {'authorization', 'binary', 'collation', 'concurrently', 'cross',
                           'current_schema', 'freeze', 'full', 'ilike', 'inner', 'is',
                           'isnull', 'join', 'left', 'like', 'natural', 'notnull', 'outer',
                           'overlaps', 'right', 'similar', 'tablesample', 'verbose'}

UNRESERVED_KEYWORDS = {'abort', 'absent', 'absolute', 'access', 'action', 'add', 'admin',
                       'after', 'aggregate', 'also', 'alter', 'always', 'asensitive',
                       'assertion', 'assignment', 'at', 'atomic', 'attach', 'attribute',
                       'backward', 'before', 'begin', 'breadth', 'by', 'cache', 'call',
                       'called', 'cascade', 'cascaded', 'catalog', 'chain', 'characteristics',
                       'checkpoint', 'class', 'close', 'cluster', 'columns', 'comment',
                       'comments', 'commit', 'committed', 'compression', 'configuration',
                       'conflict', 'connection', 'constraints', 'content', 'continue',
                       'conversion', 'copy', 'cost', 'csv', 'cube', 'current', 'cursor',
                       'cycle', 'data', 'database', 'day', 'deallocate', 'declare', 'defaults',
                       'deferred', 'definer', 'delete', 'delimiter', 'delimiters', 'depends',
                       'depth', 'detach', 'dictionary', 'disable', 'discard', 'document',
                       'domain', 'double', 'drop', 'each', 'enable', 'encoding', 'encrypted',
                       'enum', 'escape', 'event', 'exclude', 'excluding', 'exclusive',
                       'execute', 'explain', 'expression', 'extension', 'external', 'family',
                       'filter', 'finalize', 'first', 'following', 'force', 'format',
                       'forward', 'function', 'functions', 'generated', 'global', 'granted',
                       'groups', 'handler', 'header', 'hold', 'hour', 'identity', 'if',
                       'immediate', 'immutable', 'implicit', 'import', 'include', 'including',
                       'increment', 'indent', 'index', 'indexes', 'inherit', 'inherits',
                       'inline', 'input', 'insensitive', 'insert', 'instead', 'invoker',
                       'isolation', 'json', 'key', 'keys', 'label', 'language', 'large',
                       'last', 'leakproof', 'level', 'listen', 'load', 'local', 'location',
                       'lock', 'locked', 'logged', 'mapping', 'match', 'matched',
                       'materialized', 'maxvalue', 'merge', 'method', 'minute', 'minvalue',
                       'mode', 'month', 'move', 'name', 'names', 'new', 'next', 'nfc', 'nfd',
                       'nfkc', 'nfkd', 'no', 'normalized', 'nothing', 'notify', 'nowait',
                       'nulls', 'object', 'of', 'off', 'oids', 'old', 'operator', 'option',
                       'options', 'ordinality', 'others', 'over', 'overriding', 'owned',
                       'owner', 'parallel', 'parameter', 'parser', 'partial', 'partition',
                       'passing', 'password', 'plans', 'policy', 'preceding', 'prepare',
                       'prepared', 'preserve', 'prior', 'privileges', 'procedural',
                       'procedure', 'procedures', 'program', 'publication', 'quote', 'range',
                       'read', 'reassign', 'recheck', 'recursive', 'ref', 'referencing',
                       'refresh', 'reindex', 'relative', 'release', 'rename', 'repeatable',
                       'replace', 'replica', 'reset', 'restart', 'restrict', 'return',
                       'returns', 'revoke', 'role', 'rollback', 'rollup', 'routine',
                       'routines', 'rows', 'rule', 'savepoint', 'scalar', 'schema', 'schemas',
                       'scroll', 'search', 'second', 'security', 'sequence', 'sequences',
                       'serializable', 'server', 'session', 'set', 'sets', 'share', 'show',
                       'simple', 'skip', 'snapshot', 'sql', 'stable', 'standalone', 'start',
                       'statement', 'statistics', 'stdin', 'stdout', 'storage', 'stored',
                       'strict', 'strip', 'subscription', 'support', 'sysid', 'system',
                       'tables', 'tablespace', 'temp', 'template', 'temporary', 'text', 'ties',
                       'transaction', 'transform', 'trigger', 'truncate', 'trusted', 'type',
                       'types', 'uescape', 'unbounded', 'uncommitted', 'unencrypted',
                       'unknown', 'unlisten', 'unlogged', 'until', 'update', 'vacuum', 'valid',
                       'validate', 'validator', 'value', 'varying', 'version', 'view', 'views',
                       'volatile', 'whitespace', 'within', 'without', 'work', 'wrapper',
                       'write', 'xml', 'year', 'yes', 'zone'}
