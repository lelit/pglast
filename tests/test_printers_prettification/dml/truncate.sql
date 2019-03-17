truncate sometable cascade
=
TRUNCATE TABLE sometable CASCADE

truncate foo, only bar
=
TRUNCATE TABLE foo, ONLY bar

TRUNCATE bigtable, fattable RESTART IDENTITY
=
TRUNCATE TABLE bigtable, fattable RESTART IDENTITY
