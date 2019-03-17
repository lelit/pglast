insert into t (id, description)
values (1, 'this is short enough'), (2, 'this is too long, and will be splitted')
=
INSERT INTO t (id, description)
VALUES (1, 'this is short enough')
     , (2, 'this is too long, and will be splitted')

insert into t (id, description)
values (1, 'this is short enough'), (2, 'this is too long, and will be splitted')
=
INSERT INTO t (id, description)
VALUES (1, 'this is short enough')
     , (2, 'this is too long, an'
           'd will be splitted')
:
{'split_string_literals_threshold': 20}

insert into t (id, description)
values (1, 'this is short enough'), (2, 'this is too long, and will be splitted')
=
INSERT INTO t (id, description)
VALUES (1, 'this is short enough'),
       (2, 'this is too long, and will be splitted')
:
{'comma_at_eoln': True}
