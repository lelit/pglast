CREATE DOMAIN foo integer
=
CREATE DOMAIN foo AS integer

CREATE DOMAIN "Foo" integer CONSTRAINT "Non_Negative" CHECK (value > 0)
=
CREATE DOMAIN "Foo" AS integer CONSTRAINT "Non_Negative" CHECK (value > 0)

CREATE DOMAIN foo varchar(10) not null default 'null'
=
CREATE DOMAIN foo AS varchar(10) NOT NULL DEFAULT 'null'

CREATE DOMAIN foo varchar(10) collate "it_IT" default 'null'
=
CREATE DOMAIN foo AS varchar(10) COLLATE "it_IT" DEFAULT 'null'
