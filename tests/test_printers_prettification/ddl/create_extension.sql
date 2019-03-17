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
