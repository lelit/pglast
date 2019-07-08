create rule foo as on delete to bar do instead select baz(old.id, null::text) AS qux
=
CREATE RULE foo AS
  ON DELETE TO bar DO INSTEAD
    SELECT baz(old.id
             , NULL::text) AS qux