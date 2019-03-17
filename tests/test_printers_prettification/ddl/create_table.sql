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
