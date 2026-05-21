select extract(epoch from now())
=
SELECT pg_catalog.extract('epoch'
                        , now())

select extract(epoch from now())
=
SELECT EXTRACT(EPOCH FROM now())
:
{'special_functions': True}

select extract(epoch FROM now())
=
SELECT EXTRACT(EPOCH FROM now())
:
{'special_functions': True, 'raw_stream': True}

SELECT "extract"('epoch', now())
=
SELECT "extract"('epoch'
               , now())
:
{'special_functions': True}

SELECT "extract"('epoch', now())
=
SELECT "extract"('epoch', now())
:
{'special_functions': True, 'raw_stream': True}

CREATE VIEW v AS SELECT "extract"('epoch'::text, now() - now())
=
CREATE VIEW v
  AS SELECT "extract"(CAST('epoch' AS text)
                    , now() - now())
:
{'special_functions': True}

CREATE VIEW v AS SELECT "extract"('epoch'::text, now() - now())
=
CREATE VIEW v AS SELECT "extract"(CAST('epoch' AS text), now() - now())
:
{'special_functions': True, 'raw_stream': True}

SELECT pg_catalog.extract('epoch'::text, now())
=
SELECT pg_catalog.extract(CAST('epoch' AS text)
                        , now())

SELECT pg_catalog.extract('epoch'::text, now())
=
SELECT EXTRACT(CAST('epoch' AS text) FROM now())
:
{'special_functions': True}

SELECT pg_catalog.extract('epoch'::text, now())
=
SELECT EXTRACT(CAST('epoch' AS text) FROM now())
:
{'special_functions': True, 'raw_stream': True}
