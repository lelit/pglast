# -*- coding: utf-8 -*-
# :Project:   pg_query -- Test for the printers/ddl.py module
# :Created:   gio 09 nov 2017 10:57:55 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

import pytest

from pg_query.printer import IndentedStream
import pg_query.printers

from test_dml_printers import roundtrip


# Make pyflakes happy
pg_query.printers


CREATE_INDEXES = """\
create index aidx on atbl (value)
;;
create index aidx on atbl using gin (value)
;;
create unique index if not exists aidx on atbl (value)
;;
create index aidx on atbl (value) where value is not null
;;
create index aidx on atbl (value1 asc nulls first, value2 desc nulls last)
;;
create index concurrently aidx on atbl using gin (value)
with (fastupdate = ON, gin_pending_list_limit = 100)
;;
create index aidx on atbl (value) tablespace foo
;;
create index aidx on atbl (value collate "it_IT")
;;
CREATE INDEX test_index ON test_table (col varchar_pattern_ops)
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_INDEXES.split('\n;;\n')))
def test_create_indexes(sql):
    roundtrip(sql)


CREATE_TABLES = """\
create table a (id serial primary key, value integer)
;;
create table a (id serial, value integer null unique)
;;
create table a (id serial, value integer not null)
;;
create table a (id serial, value integer not null default 1)
;;
create table if not exists a (id serial)
;;
create temporary table if not exists a (id serial)
;;
create temporary table a (id serial) on commit drop
;;
create temporary table a (id serial) on commit delete rows
;;
create temporary table a (id serial) on commit preserve rows
;;
create unlogged table if not exists a (id serial)
;;
create table a (value integer) inherits (b, c)
;;
create table a (name text not null check (position('@' in name) = 0))
;;
create table a (value integer not null check (value < 10) no inherit)
;;
create table a (
  id serial primary key,
  v integer references b(id) on delete cascade on update cascade
)
;;
create table a (
  id serial primary key,
  v integer references b(id) on delete set default on update restrict
)
;;
create table a (
  id serial primary key,
  v integer references b(id) on delete restrict on update set default
)
;;
create table a (
  id serial primary key,
  v integer references b(id) on delete restrict on update set null
)
;;
CREATE TABLE a(t text collate "C")
;;
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
;;
CREATE TABLE films (
    code        char(5) CONSTRAINT firstkey PRIMARY KEY,
    title       varchar(40) NOT NULL,
    did         integer NOT NULL,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute
)
;;
CREATE TABLE distributors (
     did    integer PRIMARY KEY DEFAULT nextval('serial'),
     name   varchar(40) NOT NULL CHECK (name <> '')
)
;;
CREATE TABLE array_int (
    vector  int[][]
)
;;
CREATE TABLE films (
    code        char(5),
    title       varchar(40),
    did         integer,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute,
    CONSTRAINT production UNIQUE(date_prod)
)
;;
CREATE TABLE distributors (
    did     integer,
    name    varchar(40)
    CONSTRAINT con1 CHECK (did > 100 AND name <> '')
)
;;
CREATE TABLE films (
    code        char(5),
    title       varchar(40),
    did         integer,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to second(3),
    CONSTRAINT code_title PRIMARY KEY(code,title)
)
;;
CREATE TABLE distributors (
    did     integer,
    name    varchar(40),
    UNIQUE(name) WITH (fillfactor=70)
)
WITH (fillfactor=70)
;;
CREATE TABLE circles (
    c circle,
    EXCLUDE USING gist (c WITH &&)
)
;;
CREATE TABLE contracts (
  id id_t NOT NULL,
  company_id id_t NOT NULL,
  company_contract_kind_id id_t NULL
    REFERENCES company_contract_kinds (id) ON DELETE SET NULL ON UPDATE CASCADE,
  validity period_t NOT NULL,
  PRIMARY KEY (id),
  EXCLUDE USING gist (cast(company_id AS text) WITH =, validity WITH &&)
)
;;
CREATE TABLE contracts (
  company_id id_t NOT NULL,
  validity period_t NOT NULL,
  EXCLUDE USING gist ((company_id::text) WITH =, validity WITH &&)
)
;;
CREATE TABLE cities (
  id id_t NOT NULL,
  name text NOT NULL,
  region_id id_t NOT NULL,
  country_id id_t NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (region_id, country_id) REFERENCES regions (id, country_id) MATCH FULL
)
;;
CREATE TABLE cities (
  id id_t NOT NULL,
  name text NOT NULL,
  region_id id_t NOT NULL,
  country_id id_t NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (region_id, country_id)
    REFERENCES regions (id, country_id) MATCH SIMPLE ON DELETE RESTRICT ON UPDATE CASCADE
)
;;
CREATE TABLE cinemas (
        id serial,
        name text,
        location text
) TABLESPACE diskvol1
;;
CREATE TABLE employees OF employee_type (
    PRIMARY KEY (name),
    salary WITH OPTIONS DEFAULT 1000
)
;;
CREATE TABLE measurement (
    logdate         date not null,
    peaktemp        int,
    unitsales       int
) PARTITION BY RANGE (logdate)
;;
CREATE TABLE measurement_year_month (
    logdate         date not null,
    peaktemp        int,
    unitsales       int
) PARTITION BY RANGE (EXTRACT(YEAR FROM logdate), EXTRACT(MONTH FROM logdate))
;;
CREATE TABLE cities (
    city_id      bigserial not null,
    name         text not null,
    population   bigint
) PARTITION BY LIST (left(lower(name), 1))
;;
CREATE TABLE measurement_y2016m07
    PARTITION OF measurement (
    unitsales DEFAULT 0
) FOR VALUES FROM ('2016-07-01') TO ('2016-08-01')
;;
CREATE TABLE measurement_ym_older
    PARTITION OF measurement_year_month
    FOR VALUES FROM (MINVALUE, MINVALUE) TO (2016, MAXVALUE)
;;
CREATE TABLE cities_ab
    PARTITION OF cities (
    CONSTRAINT city_id_nonzero CHECK (city_id != 0)
) FOR VALUES IN ('a', 'b')
"""


@pytest.mark.parametrize('sql', (sql.strip() for sql in CREATE_TABLES.split('\n;;\n')))
def test_create_tables(sql):
    roundtrip(sql)


EXAMPLES = (
    ## CREATE TABLE
    (
        """\
create table a (id serial primary key, value integer)""",
        """\
CREATE TABLE a (
    id serial PRIMARY KEY
  , value integer
)""",
        None
    ),
    (
        """\
CREATE TABLE films (
    code        char(5),
    title       varchar(40),
    did         integer,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to second(3),
    CONSTRAINT code_title PRIMARY KEY(code,title)
)""",
        """\
CREATE TABLE films (
    code char(5)
  , title varchar(40)
  , did integer
  , date_prod date
  , kind varchar(10)
  , len interval hour to second (3)
  , CONSTRAINT code_title PRIMARY KEY (code, title)
)""",
        None
    ),
)


@pytest.mark.parametrize('original, expected, options', EXAMPLES)
def test_prettification(original, expected, options):
    prettified = IndentedStream(**(options or {}))(original)
    assert expected == prettified, "%r != %r" % (expected, prettified)
