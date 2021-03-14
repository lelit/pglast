CREATE OPERATOR CLASS bloom_uuid_ops
DEFAULT FOR TYPE uuid USING bloom AS
    OPERATOR    1   =(uuid, uuid),
    FUNCTION    1   uuid_hash(uuid)

CREATE OPERATOR CLASS alt_opc1 FOR TYPE macaddr USING hash AS STORAGE macaddr

CREATE OPERATOR CLASS box_ops DEFAULT
        FOR TYPE box USING gist2 AS
        OPERATOR 1      <<,
        OPERATOR 2      &<,
        OPERATOR 3      &&,
        OPERATOR 4      &>,
        OPERATOR 5      >>,
        OPERATOR 6      ~=,
        OPERATOR 7      @>,
        OPERATOR 8      <@,
        OPERATOR 9      &<|,
        OPERATOR 10     <<|,
        OPERATOR 11     |>>,
        OPERATOR 12     |&>,
        OPERATOR 13     ~,
        OPERATOR 14     @,
        FUNCTION 1      gist_box_consistent(internal, box, smallint, oid, internal),
        FUNCTION 2      gist_box_union(internal, internal),
        -- don't need compress, decompress, or fetch functions
        FUNCTION 5      gist_box_penalty(internal, internal, internal),
        FUNCTION 6      gist_box_picksplit(internal, internal),
        FUNCTION 7      gist_box_same(box, box, internal)
