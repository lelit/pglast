create index aidx on atbl (value)

create index aidx on atbl using gin (value)

create unique index if not exists aidx on atbl (value)

create index aidx on atbl (value) where value is not null

create index aidx on atbl (value1 asc nulls first, value2 desc nulls last)

create index concurrently aidx on atbl using gin (value)
with (fastupdate = ON, gin_pending_list_limit = 100)

create index aidx on atbl (value) tablespace foo

create index aidx on atbl (value collate "it_IT")

CREATE INDEX test_index ON test_table (col varchar_pattern_ops)

CREATE INDEX aidx ON atbl USING gin(value public.trgm_pattern_ops)
