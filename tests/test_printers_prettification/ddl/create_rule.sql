create rule foo as on delete to bar do instead select baz(old.id, null::text) AS qux
=
CREATE RULE foo AS
  ON DELETE TO bar
  DO INSTEAD SELECT baz(old.id
                      , CAST(NULL AS text)) AS qux

create rule "XX" as on insert to bar do nothing
=
CREATE RULE "XX" AS
  ON INSERT TO bar
  DO ALSO NOTHING

create rule "XX" as on insert to bar where new.x is null do nothing
=
CREATE RULE "XX" AS
  ON INSERT TO bar
  WHERE new.x IS NULL
  DO ALSO NOTHING

CREATE RULE notify_me AS ON UPDATE TO mytable DO ALSO (insert into audit (foo) values ('before'); NOTIFY mytable; insert into audit (foo) values ('after');)
=
CREATE RULE notify_me AS
  ON UPDATE TO mytable
  DO ALSO (
      INSERT INTO audit (foo)
      VALUES ('before')
    ; NOTIFY mytable
    ; INSERT INTO audit (foo)
      VALUES ('after')
  )

alter rule "XX" on "Foo" rename to "YY"
=
ALTER RULE "XX" ON "Foo" RENAME TO "YY"
