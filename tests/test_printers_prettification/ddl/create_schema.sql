CREATE SCHEMA hollywood
       CREATE TABLE films (title text, release date, awards text[])
       CREATE INDEX by_release ON films (release)
=
CREATE SCHEMA hollywood
  CREATE TABLE films (
      title text
    , release date
    , awards text[]
  )
  CREATE INDEX by_release
    ON films (release)
