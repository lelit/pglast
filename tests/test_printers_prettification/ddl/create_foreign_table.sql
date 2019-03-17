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
