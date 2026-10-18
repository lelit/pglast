SELECT EXTRACT(epoch FROM now())

SELECT OVERLAY('abc' PLACING 'x' FROM 2)

SELECT value IS NORMALIZED

SELECT (a OR b) IS NFC NORMALIZED

SELECT (value IS NULL) IS NFKC NORMALIZED

SELECT pg_catalog.normalize(value)

SELECT pg_catalog.is_normalized(value)

SELECT pg_catalog.normalize(value, form)

SELECT pg_catalog.is_normalized(value, form)

SELECT pg_catalog.normalize(value, 'nfc')

SELECT pg_catalog.is_normalized(value, 'invalid')

SELECT pg_catalog.normalize(value, NULL)

SELECT pg_catalog.is_normalized(value, 1)

SELECT ts AT TIME ZONE (a + b)

SELECT ts AT TIME ZONE (y AT TIME ZONE 'UTC')

SELECT (a + b) AT LOCAL
