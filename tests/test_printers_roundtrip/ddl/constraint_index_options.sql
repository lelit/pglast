CREATE TABLE t (a int PRIMARY KEY WITH (fillfactor = 50))

CREATE TABLE t (a int, b int, PRIMARY KEY (a) INCLUDE (b) WITH (fillfactor = 50))

CREATE TABLE t (a int, EXCLUDE USING gist (a WITH =) WITH (fillfactor = 50))

ALTER TABLE t ADD CONSTRAINT c PRIMARY KEY (a) WITH (fillfactor = 50, deduplicate_items)
