CREATE CAST (foo AS bar)WITHOUT FUNCTION
=
CREATE CAST (foo AS bar) WITHOUT FUNCTION

VACUUM (ANALYZE)stxdinp
=
VACUUM (ANALYZE) stxdinp

ALTER OPERATOR FAMILY alt_opf18 USING btree ADD FUNCTION 4  (int4, int2)btequalimage
=
ALTER OPERATOR FAMILY alt_opf18 USING btree
  ADD FUNCTION 4 (int4, int2) btequalimage

CREATE TABLE coll_pruning_multi (a text) PARTITION BY range ((substr(a, 1))COLLATE "POSIX", (substr(a, 1))COLLATE "C")
=
CREATE TABLE coll_pruning_multi (
  a text
) PARTITION BY range ((substr(a, 1)) COLLATE "POSIX"
                    , (substr(a, 1)) COLLATE "C")

DECLARE tablesample_cur CURSOR FOR SELECT id FROM test_tablesample TABLESAMPLE system(50)REPEATABLE (0)
=
DECLARE tablesample_cur CURSOR
  FOR SELECT id
      FROM test_tablesample TABLESAMPLE system(50) REPEATABLE (0)
