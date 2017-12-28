# -*- coding: utf-8 -*-
# :Project:   pg_query -- Test for the printers/ddl.py module
# :Created:   gio 09 nov 2017 10:57:55 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

from ast import literal_eval

import pytest

from pg_query.printer import IndentedStream
import pg_query.printers

from test_dml_printers import roundtrip


# Make pyflakes happy
pg_query.printers


COMMENTS = """\
COMMENT ON ACCESS METHOD rtree IS 'R-Tree access method'

COMMENT ON AGGREGATE my_aggregate (double precision) IS 'Computes sample variance'

COMMENT ON CAST (text AS int4) IS 'Allow casts from text to int4'

COMMENT ON COLLATION "fr_CA" IS 'Canadian French'

COMMENT ON COLUMN my_table.my_column IS 'Employee ID number'

COMMENT ON CONVERSION my_conv IS 'Conversion to UTF8'

COMMENT ON CONSTRAINT bar_col_cons ON bar IS 'Constrains column col'

COMMENT ON CONSTRAINT dom_col_constr ON DOMAIN dom IS 'Constrains col of domain'

COMMENT ON DATABASE my_database IS 'Development Database'

COMMENT ON DOMAIN my_domain IS 'Email Address Domain'

COMMENT ON EXTENSION hstore IS 'implements the hstore data type'

COMMENT ON FOREIGN DATA WRAPPER mywrapper IS 'my foreign data wrapper'

COMMENT ON FOREIGN TABLE my_foreign_table IS 'Employee Information in other database'

COMMENT ON FUNCTION my_function (timestamp) IS 'Returns Roman Numeral'

COMMENT ON INDEX my_index IS 'Enforces uniqueness on employee ID'

COMMENT ON LANGUAGE plpython IS 'Python support for stored procedures'

COMMENT ON LARGE OBJECT 346344 IS 'Planning document'

COMMENT ON MATERIALIZED VIEW my_matview IS 'Summary of order history'

COMMENT ON OPERATOR ^ (text, text) IS 'Performs intersection of two texts'

COMMENT ON OPERATOR - (NONE, integer) IS 'Unary minus'

COMMENT ON OPERATOR CLASS int4ops USING btree IS '4 byte integer operators for btrees'

COMMENT ON OPERATOR FAMILY integer_ops USING btree IS 'all integer operators for btrees'

COMMENT ON POLICY my_policy ON mytable IS 'Filter rows by users'

COMMENT ON ROLE my_role IS 'Administration group for finance tables'

COMMENT ON RULE my_rule ON my_table IS 'Logs updates of employee records'

COMMENT ON SCHEMA my_schema IS 'Departmental data'

COMMENT ON SEQUENCE my_sequence IS 'Used to generate primary keys'

COMMENT ON SERVER myserver IS 'my foreign server'

COMMENT ON STATISTICS my_statistics IS 'Improves planner row estimations'

COMMENT ON TABLE my_schema.my_table IS 'Employee Information'

COMMENT ON TABLESPACE my_tablespace IS 'Tablespace for indexes'

COMMENT ON TEXT SEARCH CONFIGURATION my_config IS 'Special word filtering'

COMMENT ON TEXT SEARCH DICTIONARY swedish IS 'Snowball stemmer for Swedish language'

COMMENT ON TEXT SEARCH PARSER my_parser IS 'Splits text into words'

COMMENT ON TEXT SEARCH TEMPLATE snowball IS 'Snowball stemmer'

COMMENT ON TRANSFORM FOR hstore LANGUAGE plpythonu
        IS 'Transform between hstore and Python dict'

COMMENT ON TRIGGER my_trigger ON my_table IS 'Used for RI'

COMMENT ON TYPE complex IS 'Complex number data type'

COMMENT ON VIEW my_view IS
  'Lorem ipsum dolor sit amet, consectetur adipisicing elit,'
  ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  ' Ut enimad minim veniam, quis nostrud exercitation ullamco laboris.'
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in COMMENTS.split('\n\n')))
def test_comments(sql):
    roundtrip(sql)


CREATE_ACCESS_METHODS = """\
CREATE ACCESS METHOD heptree TYPE INDEX HANDLER heptree_handler

CREATE ACCESS METHOD "Heptree" TYPE INDEX HANDLER "MySchema"."MyHandler"
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_ACCESS_METHODS.split('\n\n')))
def test_create_access_methods(sql):
    roundtrip(sql)


CREATE_AGGREGATES = """\
CREATE AGGREGATE sum (complex)
(
    sfunc = complex_add,
    stype = complex,
    initcond = '(0,0)'
)

CREATE AGGREGATE sum (complex)
(
    sfunc = complex_add,
    stype = complex,
    initcond = '(0,0)',
    parallel = safe
)

CREATE AGGREGATE avg (float8)
(
    sfunc = float8_accum,
    stype = float8[],
    finalfunc = float8_avg,
    initcond = '{0,0,0}'
)

CREATE AGGREGATE sum (complex)
(
    sfunc = complex_add,
    stype = complex,
    initcond = '(0,0)',
    msfunc = complex_add,
    minvfunc = complex_sub,
    mstype = complex,
    minitcond = '(0,0)'
)

CREATE AGGREGATE array_accum (anyelement)
(
    sfunc = array_append,
    stype = anyarray,
    initcond = '{}'
)

CREATE AGGREGATE array_agg (anynonarray)
(
    sfunc = array_agg_transfn,
    stype = internal,
    finalfunc = array_agg_finalfn,
    finalfunc_extra
)

CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement)
(
    sfunc = ordered_set_transition,
    stype = internal,
    finalfunc = percentile_disc_final,
    finalfunc_extra
)

CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement)
(
    sfunc = ordered_set_transition,
    stype = internal,
    finalfunc = percentile_disc_final,
    finalfunc_extra,
    hypotetical
)
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_AGGREGATES.split('\n\n')))
def test_create_aggregates(sql):
    roundtrip(sql)


CREATE_CASTS = """\
CREATE CAST (bigint AS int4) WITH FUNCTION int4(bigint) AS ASSIGNMENT

CREATE CAST (varchar AS citext) WITHOUT FUNCTION AS ASSIGNMENT

CREATE CAST (citext AS varchar) WITHOUT FUNCTION AS IMPLICIT

CREATE CAST (text AS casttesttype) WITHOUT FUNCTION

CREATE CAST (text AS casttesttype) WITHOUT FUNCTION AS IMPLICIT

CREATE CAST (int4 AS casttesttype) WITH INOUT

CREATE CAST (int4 AS casttesttype) WITH FUNCTION int4_casttesttype(int4) AS IMPLICIT
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_CASTS.split('\n\n')))
def test_create_casts(sql):
    roundtrip(sql)


CREATE_COLLATIONS = """\
CREATE COLLATION french (locale = 'fr_FR.utf8')

CREATE COLLATION IF NOT EXISTS french (locale = 'fr_FR.utf8')

CREATE COLLATION german_phonebook (provider = icu, locale = 'de-u-co-phonebk')

CREATE COLLATION german FROM "de_DE"

CREATE COLLATION IF NOT EXISTS german FROM "de_DE"

CREATE COLLATION mycoll2 ( LC_COLLATE = "POSIX", LC_CTYPE = "POSIX" )
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_COLLATIONS.split('\n\n')))
def test_create_collations(sql):
    roundtrip(sql)


CREATE_CONVERSIONS = """\
CREATE CONVERSION myconv FOR 'UTF8' TO 'LATIN1' FROM myfunc

CREATE DEFAULT CONVERSION myconv FOR 'UTF8' TO 'LATIN1' FROM myfunc
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_CONVERSIONS.split('\n\n')))
def test_create_conversions(sql):
    roundtrip(sql)


CREATE_DATABASES = """\
CREATE DATABASE sales OWNER salesapp TABLESPACE salesspace

CREATE DATABASE music LC_COLLATE 'sv_SE.utf8' LC_CTYPE 'sv_SE.utf8' TEMPLATE template0

CREATE DATABASE music2
    LC_COLLATE 'sv_SE.iso885915' LC_CTYPE 'sv_SE.iso885915'
    ENCODING LATIN9
    TEMPLATE template0
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_DATABASES.split('\n\n')))
def test_create_databases(sql):
    roundtrip(sql)


CREATE_FOREIGN_DATA_WRAPPERS = """\
CREATE FOREIGN DATA WRAPPER dummy

CREATE FOREIGN DATA WRAPPER file HANDLER file_fdw_handler

CREATE FOREIGN DATA WRAPPER mywrapper OPTIONS (debug 'true')
"""


@pytest.mark.parametrize('sql', (sql.strip()
                                 for sql in CREATE_FOREIGN_DATA_WRAPPERS.split('\n\n')))
def test_create_foreign_data_wrappers(sql):
    roundtrip(sql)


CREATE_INDEXES = """\
create index aidx on atbl (value)

create index aidx on atbl using gin (value)

create unique index if not exists aidx on atbl (value)

create index aidx on atbl (value) where value is not null

create index aidx on atbl (value1 asc nulls first, value2 desc nulls last)

create index concurrently aidx on atbl using gin (value)
with (fastupdate = ON, gin_pending_list_limit = 100)

create index aidx on atbl (value) tablespace foo

create index aidx on atbl (value collate "it_IT")

CREATE INDEX test_index ON test_table (col varchar_pattern_ops)
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_INDEXES.split('\n\n')))
def test_create_indexes(sql):
    roundtrip(sql)


CREATE_OPERATORS = """\
CREATE OPERATOR "MySchema".+ (
    LEFTARG = box,
    RIGHTARG = box,
    PROCEDURE = area_sum_procedure
)

CREATE OPERATOR === (
    LEFTARG = box,
    RIGHTARG = box,
    PROCEDURE = area_equal_procedure,
    COMMUTATOR = ===,
    NEGATOR = !==,
    RESTRICT = area_restriction_procedure,
    JOIN = area_join_procedure,
    HASHES, MERGES
)

CREATE OPERATOR === (
    LEFTARG = box,
    RIGHTARG = box,
    PROCEDURE = area_equal_procedure,
    COMMUTATOR = OPERATOR("MySchema".===),
    NEGATOR = !==,
    RESTRICT = area_restriction_procedure,
    JOIN = area_join_procedure,
    HASHES, MERGES
)
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_OPERATORS.split('\n\n')))
def test_create_operators(sql):
    roundtrip(sql)


CREATE_SEQUENCES = """\
CREATE SEQUENCE serial START 101

CREATE TEMP SEQUENCE serial

CREATE TEMP SEQUENCE serial NO CYCLE

CREATE SEQUENCE IF NOT EXISTS "SomeSchema"."SomeSerial" as smallint

CREATE TEMP SEQUENCE serial INCREMENT 2 MINVALUE 5 NO MAXVALUE

CREATE TEMP SEQUENCE serial INCREMENT 2 MINVALUE 5 MAXVALUE 15 START WITH 7 CYCLE

CREATE SEQUENCE serial OWNED BY "SomeSchema"."SomeTable"."SomeColumn"
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_SEQUENCES.split('\n\n')))
def test_create_sequences(sql):
    roundtrip(sql)


CREATE_SCHEMAS = """\
create schema myschema

create schema authorization joe

create schema if not exists test authorization joe

create schema test authorization public

create schema test authorization current_user

create schema test authorization session_user
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_SCHEMAS.split('\n\n')))
def test_create_schemas(sql):
    roundtrip(sql)


CREATE_TABLES = """\
create table a (id serial primary key, value integer)

create table a (id serial, value integer null unique)

create table a (id serial, value integer not null)

create table a (id serial, value integer not null default 1)

create table if not exists a (id serial)

create temporary table if not exists a (id serial)

create temporary table a (id serial) on commit drop

create temporary table a (id serial) on commit delete rows

create temporary table a (id serial) on commit preserve rows

create temporary table a (id serial) inherits ("BaseTable") on commit preserve rows

create unlogged table if not exists a (id serial)

create table a (value integer) inherits (b, c)

create table a (name text not null check (position('@' in name) = 0))

create table a (value integer not null check (value < 10) no inherit)

create table "Someschema"."Sometable" (a integer primary key)

create table a (id serial primary key, value integer) with oids

create table a (id serial primary key, value integer) without oids

create table a (
  id serial primary key,
  v integer references b(id) on delete cascade on update cascade
)

create table a (
  id serial primary key,
  v integer references b(id) on delete set default on update restrict
)

create table a (
  id serial primary key,
  v integer references b(id) on delete restrict on update set default
)

create table a (
  id serial primary key,
  v integer references b(id) on delete restrict on update set null
)

CREATE TABLE a(t text collate "C")

CREATE TABLE ages (
  id integer primary key,
  age1 interval year,
  age2 interval month,
  age3 interval day,
  age4 interval hour,
  age5 interval minute,
  age6a interval second,
  age6b interval second (5),
  age7 interval year to month,
  age8 interval day to hour,
  age9 interval day to minute,
  age10a interval day to second,
  age10b interval day to second (5),
  age11 interval hour to minute,
  age11 interval hour to second,
  age11a interval minute to second,
  age11b interval minute to second (5)
)

CREATE TABLE films (
    code        char(5) CONSTRAINT firstkey PRIMARY KEY,
    title       varchar(40) NOT NULL,
    did         integer NOT NULL,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute
)

CREATE TABLE distributors (
     did    integer PRIMARY KEY DEFAULT nextval('serial'),
     name   varchar(40) NOT NULL CHECK (name <> '')
)

CREATE TABLE array_int (
    vector  int[][]
)

CREATE TABLE films (
    code        char(5),
    title       varchar(40),
    did         integer,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute,
    CONSTRAINT production UNIQUE(date_prod)
)

CREATE TABLE distributors (
    did     integer,
    name    varchar(40)
    CONSTRAINT con1 CHECK (did > 100 AND name <> '')
)

CREATE TABLE films (
    code        char(5),
    title       varchar(40),
    did         integer,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to second(3),
    CONSTRAINT code_title PRIMARY KEY(code,title)
)

CREATE TABLE distributors (
    did     integer,
    name    varchar(40),
    UNIQUE(name) USING INDEX TABLESPACE indexes
)

CREATE TABLE distributors (
    did     integer,
    name    varchar(40),
    UNIQUE(name) WITH (fillfactor=70) USING INDEX TABLESPACE indexes
)
WITH (fillfactor=70)

CREATE TABLE distributors (
    did     integer,
    name    varchar(40)
) INHERITS ("BaseTable") WITH (fillfactor=70)

CREATE TABLE circles (
    c circle,
    EXCLUDE USING gist (c WITH &&)
)

CREATE TABLE contracts (
  id id_t NOT NULL,
  company_id id_t NOT NULL,
  company_contract_kind_id id_t NULL
    REFERENCES company_contract_kinds (id) ON DELETE SET NULL ON UPDATE CASCADE,
  validity period_t NOT NULL,
  PRIMARY KEY (id),
  EXCLUDE USING gist (cast(company_id AS text) WITH =, validity WITH &&)
)

CREATE TABLE contracts (
  company_id id_t NOT NULL,
  validity period_t NOT NULL,
  EXCLUDE USING gist ((company_id::text) WITH =, validity WITH &&)
)

CREATE TABLE cities (
  id id_t NOT NULL,
  name text NOT NULL,
  region_id id_t NOT NULL,
  country_id id_t NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (region_id, country_id) REFERENCES regions (id, country_id) MATCH FULL
)

CREATE TABLE cities (
  id id_t NOT NULL,
  name text NOT NULL,
  region_id id_t NOT NULL,
  country_id id_t NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (region_id, country_id)
    REFERENCES regions (id, country_id) MATCH SIMPLE ON DELETE RESTRICT ON UPDATE CASCADE
)

CREATE TABLE cinemas (
        id serial,
        name text,
        location text
) TABLESPACE diskvol1

CREATE TABLE employees OF employee_type (
    PRIMARY KEY (name),
    salary WITH OPTIONS DEFAULT 1000
)

CREATE TABLE measurement (
    logdate         date not null,
    peaktemp        int,
    unitsales       int
) PARTITION BY RANGE (logdate)

CREATE TABLE measurement_year_month (
    logdate         date not null,
    peaktemp        int,
    unitsales       int
) PARTITION BY RANGE (EXTRACT(YEAR FROM logdate), EXTRACT(MONTH FROM logdate))

CREATE TABLE cities (
    city_id      bigserial not null,
    name         text not null,
    population   bigint
) PARTITION BY LIST (left(lower(name), 1))

CREATE TABLE measurement_y2016m07
    PARTITION OF measurement (
    unitsales DEFAULT 0
) FOR VALUES FROM ('2016-07-01') TO ('2016-08-01')

CREATE TABLE measurement_y2016m07
    PARTITION OF measurement (
    unitsales DEFAULT 0
) FOR VALUES FROM ('2016-07-01') TO ('2016-08-01')

CREATE TABLE measurement_y2016m07
    PARTITION OF measurement (
    unitsales DEFAULT 0
) FOR VALUES FROM ('2016-07-01') TO ('2016-08-01')

CREATE TABLE measurement_ym_older
    PARTITION OF measurement_year_month
    FOR VALUES FROM (MINVALUE, MINVALUE) TO (2016, MAXVALUE)

CREATE TABLE cities_ab
    PARTITION OF cities (
    CONSTRAINT city_id_nonzero CHECK (city_id != 0)
) FOR VALUES IN ('a', 'b')
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_TABLES.split('\n\n')))
def test_create_tables(sql):
    roundtrip(sql)


CREATE_TABLES_AS = """\
CREATE TABLE films2 AS TABLE films

CREATE TABLE films2 AS TABLE films WITH NO DATA

CREATE TABLE films2 WITH OIDS AS TABLE films

CREATE TABLE films2 WITHOUT OIDS AS TABLE films

CREATE TABLE films2 AS VALUES (1,2)

CREATE TEMPORARY TABLE films2 AS VALUES (1,2)

CREATE TABLE films2 WITH (fillfactor=70) ON COMMIT PRESERVE ROWS AS VALUES (1,2)

CREATE TABLE films2 ON COMMIT DELETE ROWS TABLESPACE "Foo" AS TABLE films

CREATE TABLE films2 ON COMMIT DROP AS TABLE films

CREATE UNLOGGED TABLE IF NOT EXISTS "SomeSchema".films2 (id, title) AS
  SELECT id, title FROM films

CREATE TABLE films_recent AS
  SELECT * FROM films WHERE date_prod >= '2002-01-01'
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_TABLES_AS.split('\n\n')))
def test_create_tables_as(sql):
    roundtrip(sql)


DROPS = """\
drop access method some_name cascade

DROP AGGREGATE myrank(VARIADIC "any" ORDER BY VARIADIC "any")

DROP AGGREGATE myavg(integer), myavg(bigint)

DROP CAST (text AS int)

DROP COLLATION german

DROP CONVERSION myname

drop database if exists mydb

DROP DOMAIN "NameSpace"."Domain"

DROP EVENT TRIGGER snitch

DROP EXTENSION hstore

DROP FOREIGN DATA WRAPPER dbi

DROP FOREIGN TABLE films, distributors

drop function slower_one(int, int)

drop function if exists "Mine".generic_function

DROP INDEX title_idx

DROP INDEX CONCURRENTLY title_idx

DROP LANGUAGE plsample

DROP MATERIALIZED VIEW order_summary

DROP OPERATOR ^ (integer, integer)

DROP OPERATOR ~ (none, bit), ! (bigint, none)

DROP OPERATOR CLASS widget_ops USING btree

DROP OPERATOR FAMILY "My".float_ops USING btree

drop owned by "White"

drop owned by current_user cascade

DROP POLICY p1 ON my_table

DROP PUBLICATION mypublication

DROP ROLE myrole

DROP RULE newrule ON mytable

DROP SEQUENCE serial

DROP SCHEMA a,"B" CASCADE

DROP SERVER IF EXISTS foo CASCADE

DROP STATISTICS IF EXISTS
    accounting.users_uid_creation,
    public.grants_user_role

DROP SUBSCRIPTION mysub

DROP SUBSCRIPTION IF EXISTS mysub CASCADE

drop table foo.bar

DROP TABLESPACE IF EXISTS mystuff

DROP TEXT SEARCH CONFIGURATION my_english

DROP TEXT SEARCH CONFIGURATION IF EXISTS my_english CASCADE

DROP TEXT SEARCH DICTIONARY english

DROP TEXT SEARCH DICTIONARY IF EXISTS english CASCADE

DROP TEXT SEARCH TEMPLATE thesaurus

DROP TEXT SEARCH TEMPLATE IF EXISTS "Thesaurus" CASCADE

DROP TRANSFORM FOR hstore LANGUAGE plpythonu

DROP TRIGGER "If_dist_exists" ON "Films"

DROP USER IF EXISTS barry, "White"

DROP USER MAPPING IF EXISTS FOR bob SERVER foo

DROP USER MAPPING FOR user SERVER "Foo"

DROP USER MAPPING FOR current_user SERVER foo

DROP TYPE "Foo", bar RESTRICT

DROP VIEW x.y
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in DROPS.split('\n\n')))
def test_drops(sql):
    roundtrip(sql)


# Prettification samples: each sample may be composed by either two or three parts,
# respectively the original statement, the expected outcome and an optional options
# dictionary. The original and the expected statements are separated by a standalone "=",
# while the options dictionary is introduced by a standalone ":".

SAMPLES = r"""
CREATE DATABASE "NewDB"
    WITH ENCODING = 'UTF8'
         TEMPLATE = 'template0'
         LC_COLLATE = 'it_IT.UTF-8'
         LC_CTYPE = 'it_IT.UTF-8'
         ALLOW_CONNECTIONS = true
         CONNECTION LIMIT = 2
         IS_TEMPLATE = false
=
CREATE DATABASE "NewDB"
  WITH encoding = 'UTF8'
       template = 'template0'
       lc_collate = 'it_IT.UTF-8'
       lc_ctype = 'it_IT.UTF-8'
       allow_connections = true
       connection limit = 2
       is_template = false

CREATE DOMAIN foo integer
=
CREATE DOMAIN foo AS integer

CREATE DOMAIN "Foo" integer CONSTRAINT "Non_Negative" CHECK (value > 0)
=
CREATE DOMAIN "Foo" AS integer CONSTRAINT "Non_Negative" CHECK (value > 0)

CREATE DOMAIN foo varchar(10) not null default 'null'
=
CREATE DOMAIN foo AS varchar(10) NOT NULL DEFAULT 'null'

CREATE DOMAIN foo varchar(10) collate "it_IT" default 'null'
=
CREATE DOMAIN foo AS varchar(10) COLLATE "it_IT" DEFAULT 'null'

CREATE EVENT TRIGGER abort_ddl ON ddl_command_start EXECUTE PROCEDURE abort_any_command()
=
CREATE EVENT TRIGGER abort_ddl ON ddl_command_start
  EXECUTE PROCEDURE abort_any_command()

create event trigger abort_ddl on ddl_command_start
when tag in ('foo', 'bar') execute procedure a()
=
CREATE EVENT TRIGGER abort_ddl ON ddl_command_start
  WHEN tag IN ('foo', 'bar')
  EXECUTE PROCEDURE a()

create event trigger abort_ddl on ddl_command_start
when tag in ('foo', 'bar') and tag in ('other') execute procedure a()
=
CREATE EVENT TRIGGER abort_ddl ON ddl_command_start
  WHEN tag IN ('foo', 'bar')
   AND tag IN ('other')
  EXECUTE PROCEDURE a()

CREATE EXTENSION IF NOT EXISTS hstore
=
CREATE EXTENSION IF NOT EXISTS hstore

CREATE EXTENSION "Foobar" VERSION '1' CASCADE
=
CREATE EXTENSION "Foobar"
  WITH version '1'
       CASCADE

CREATE EXTENSION hstore SCHEMA public FROM unpackaged
=
CREATE EXTENSION hstore
  WITH schema public
       from 'unpackaged'

create index concurrently aidx on atbl using gin (value)
with (fastupdate = ON, gin_pending_list_limit = 100)
=
CREATE INDEX CONCURRENTLY aidx
  ON atbl USING gin (value)
  WITH (fastupdate = 'on'
      , gin_pending_list_limit = 100)

CREATE SCHEMA hollywood
       CREATE TABLE films (title text, release date, awards text[])
       CREATE INDEX by_release ON films (release)
=
CREATE SCHEMA hollywood
  CREATE TABLE films (
      title text
    , release date
    , awards text[]
  )
  CREATE INDEX by_release
    ON films (release)

CREATE TEMP SEQUENCE serial INCREMENT 2 MINVALUE 5 MAXVALUE 15 START WITH 7 CYCLE
=
CREATE TEMPORARY SEQUENCE serial
  INCREMENT BY 2
  MINVALUE 5
  MAXVALUE 15
  START WITH 7
  CYCLE

create table a (id serial primary key, value integer)
=
CREATE TABLE a (
    id serial PRIMARY KEY
  , value integer
)

CREATE TABLE films (
    code        char(5),
    title       varchar(40),
    did         integer,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to second(3),
    CONSTRAINT code_title PRIMARY KEY(code,title)
)
=
CREATE TABLE films (
    code char(5)
  , title varchar(40)
  , did integer
  , date_prod date
  , kind varchar(10)
  , len interval hour to second (3)
  , CONSTRAINT code_title PRIMARY KEY (code, title)
)

create temporary table a (id serial) on commit drop
=
CREATE TEMPORARY TABLE a (
  id serial
) ON COMMIT DROP

CREATE TABLE distributors (
    did     integer,
    name    varchar(40),
    UNIQUE(name) WITH (fillfactor=70) USING INDEX TABLESPACE indexes
)
WITH (fillfactor=70)
=
CREATE TABLE distributors (
    did integer
  , name varchar(40)
  , UNIQUE (name) WITH (fillfactor = 70)
                  USING INDEX TABLESPACE indexes
) WITH (fillfactor = 70)

CREATE TABLE distributors (
    did     integer,
    name    varchar(40),
    UNIQUE(name) WITH (fillfactor=70) USING INDEX TABLESPACE indexes
)
WITH (fillfactor=70)
=
CREATE TABLE distributors (
  did integer,
  name varchar(40),
  UNIQUE (name) WITH (fillfactor = 70)
                USING INDEX TABLESPACE indexes
) WITH (fillfactor = 70)
:
{'comma_at_eoln': True}

CREATE TABLE measurement_y2016m07
    PARTITION OF measurement (
    unitsales DEFAULT 0
) FOR VALUES FROM ('2016-07-01') TO ('2016-08-01') TABLESPACE olddata
=
CREATE TABLE measurement_y2016m07 PARTITION OF measurement (
  unitsales WITH OPTIONS DEFAULT 0
) FOR VALUES FROM ('2016-07-01') TO ('2016-08-01')
  TABLESPACE olddata

COMMENT ON VIEW "MySchema"."MyView" IS
  'Lorem ipsum dolor sit amet, consectetur adipisicing elit,'
  ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  ' Ut enimad minim veniam, quis nostrud exercitation ullamco laboris.'
=
COMMENT ON VIEW "MySchema"."MyView"
  IS 'Lorem ipsum dolor sit amet, consectetur adipisicin'
     'g elit, sed do eiusmod tempor incididunt ut labore'
     ' et dolore magna aliqua. Ut enimad minim veniam, q'
     'uis nostrud exercitation ullamco laboris.'
:
{'split_string_literals_threshold': 50}

CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement)
(
    sfunc = ordered_set_transition,
    stype = internal,
    finalfunc = percentile_disc_final,
    finalfunc_extra
)
=
CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement) (
    sfunc = ordered_set_transition
  , stype = internal
  , finalfunc = percentile_disc_final
  , finalfunc_extra
)

CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement)
(
    sfunc = ordered_set_transition,
    stype = internal,
    finalfunc = percentile_disc_final,
    finalfunc_extra
)
=
CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement) (
  sfunc = ordered_set_transition,
  stype = internal,
  finalfunc = percentile_disc_final,
  finalfunc_extra
)
:
{'comma_at_eoln': True}

CREATE FOREIGN DATA WRAPPER mywrapper validator myvalf OPTIONS (debug 'true', foo 'bar')
=
CREATE FOREIGN DATA WRAPPER mywrapper
  VALIDATOR myvalf
  OPTIONS (debug 'true'
         , foo 'bar')

CREATE FOREIGN DATA WRAPPER mywrapper validator myvalf OPTIONS (debug 'true', foo 'bar')
=
CREATE FOREIGN DATA WRAPPER mywrapper
  VALIDATOR myvalf
  OPTIONS (debug 'true', foo 'bar')
:
{'compact_lists_margin': 40}

CREATE FOREIGN DATA WRAPPER mywrapper validator myvalf
OPTIONS (debug 'true', foo 'bar', abra 'cadabra')
=
CREATE FOREIGN DATA WRAPPER mywrapper
  VALIDATOR myvalf
  OPTIONS (debug 'true'
         , foo 'bar'
         , abra 'cadabra')
:
{'compact_lists_margin': 40}

CREATE FOREIGN DATA WRAPPER file HANDLER myhandler validator myvalf
=
CREATE FOREIGN DATA WRAPPER file
  HANDLER myhandler
  VALIDATOR myvalf

CREATE FOREIGN DATA WRAPPER file HANDLER myhandler validator myvalf
=
CREATE FOREIGN DATA WRAPPER file
  HANDLER myhandler VALIDATOR myvalf
:
{'compact_lists_margin': 40}

CREATE FOREIGN TABLE films (
    code        char(5) NOT NULL,
    title       varchar(40) NOT NULL,
    did         integer NOT NULL,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute
)
SERVER film_server
=
CREATE FOREIGN TABLE films (
    code char(5) NOT NULL
  , title varchar(40) NOT NULL
  , did integer NOT NULL
  , date_prod date
  , kind varchar(10)
  , len interval hour to minute
) SERVER film_server

CREATE FOREIGN TABLE films (
    code        char(5) NOT NULL,
    title       varchar(40) NOT NULL,
    did         integer NOT NULL,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute
)
SERVER film_server OPTIONS (foo 'bar', bar 'foo')
=
CREATE FOREIGN TABLE films (
    code char(5) NOT NULL
  , title varchar(40) NOT NULL
  , did integer NOT NULL
  , date_prod date
  , kind varchar(10)
  , len interval hour to minute
) SERVER film_server
  OPTIONS (foo 'bar'
         , bar 'foo')

CREATE FOREIGN TABLE measurement_y2016m07
    PARTITION OF measurement FOR VALUES FROM ('2016-07-01') TO ('2016-08-01')
    SERVER server_07
=
CREATE FOREIGN TABLE measurement_y2016m07 PARTITION OF measurement
  FOR VALUES FROM ('2016-07-01') TO ('2016-08-01')
  SERVER server_07
"""


@pytest.mark.parametrize('sample', (sample for sample in SAMPLES.split('\n\n')))
def test_prettification(sample):
    parts = sample.split('\n=\n')
    original = parts[0].strip()
    parts = parts[1].split('\n:\n')
    expected = parts[0].strip()
    if len(parts) == 2:
        options = literal_eval(parts[1])
    else:
        options = {}
    prettified = IndentedStream(**options)(original)
    assert expected == prettified, "%r != %r" % (expected, prettified)
