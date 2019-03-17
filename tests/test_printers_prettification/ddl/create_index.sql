create index concurrently aidx on atbl using gin (value)
with (fastupdate = ON, gin_pending_list_limit = 100)
=
CREATE INDEX CONCURRENTLY aidx
  ON atbl USING gin (value)
  WITH (fastupdate = 'on'
      , gin_pending_list_limit = 100)
