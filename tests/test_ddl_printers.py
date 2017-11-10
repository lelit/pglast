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
create table a (value integer) inherits (b, c)
;;
create table a (name text not null check (position('@' in name) = 0))
;;
create table a (value integer not null check (value < 10) no inherit)
;;
create table a (id serial primary key, v integer references b(id))
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
