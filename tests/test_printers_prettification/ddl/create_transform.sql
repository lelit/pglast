CREATE OR REPLACE TRANSFORM FOR int LANGUAGE SQL (
        FROM SQL WITH FUNCTION prsd_lextype(internal),
        TO SQL WITH FUNCTION int4recv(internal))
=
CREATE OR REPLACE TRANSFORM FOR integer LANGUAGE sql (
  FROM SQL WITH FUNCTION prsd_lextype (internal),
  TO SQL WITH FUNCTION int4recv (internal))
