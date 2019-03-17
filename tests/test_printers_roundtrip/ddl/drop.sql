drop access method some_name cascade

DROP AGGREGATE myrank(VARIADIC "any" ORDER BY VARIADIC "any")

DROP AGGREGATE myavg(integer), myavg(bigint)

DROP CAST (text AS int)

DROP COLLATION german

DROP CONVERSION myname

drop database if exists mydb

DROP DOMAIN "NameSpace"."Domain"

DROP EVENT TRIGGER snitch

DROP EXTENSION hstore

DROP FOREIGN DATA WRAPPER dbi

DROP FOREIGN TABLE films, distributors

drop function slower_one(int, int)

drop function if exists "Mine".generic_function

DROP INDEX title_idx

DROP INDEX CONCURRENTLY title_idx

DROP LANGUAGE plsample

DROP MATERIALIZED VIEW order_summary

DROP OPERATOR ^ (integer, integer)

DROP OPERATOR ~ (none, bit), ! (bigint, none)

DROP OPERATOR CLASS widget_ops USING btree

DROP OPERATOR FAMILY "My".float_ops USING btree

drop owned by "White"

drop owned by current_user cascade

DROP POLICY p1 ON my_table

DROP PUBLICATION mypublication

DROP ROLE myrole

DROP RULE newrule ON mytable

DROP SEQUENCE serial

DROP SCHEMA a,"B" CASCADE

DROP SERVER IF EXISTS foo CASCADE

DROP STATISTICS IF EXISTS
    accounting.users_uid_creation,
    public.grants_user_role

DROP SUBSCRIPTION mysub

DROP SUBSCRIPTION IF EXISTS mysub CASCADE

drop table foo.bar

DROP TABLESPACE IF EXISTS mystuff

DROP TEXT SEARCH CONFIGURATION my_english

DROP TEXT SEARCH CONFIGURATION IF EXISTS my_english CASCADE

DROP TEXT SEARCH DICTIONARY english

DROP TEXT SEARCH DICTIONARY IF EXISTS english CASCADE

DROP TEXT SEARCH TEMPLATE thesaurus

DROP TEXT SEARCH TEMPLATE IF EXISTS "Thesaurus" CASCADE

DROP TRANSFORM FOR hstore LANGUAGE plpythonu

DROP TRIGGER "If_dist_exists" ON "Films"

DROP TRIGGER trig1 ON public."Films"

DROP USER IF EXISTS barry, "White"

DROP USER MAPPING IF EXISTS FOR bob SERVER foo

DROP USER MAPPING FOR user SERVER "Foo"

DROP USER MAPPING FOR current_user SERVER foo

DROP TYPE "Foo", bar RESTRICT

DROP VIEW x.y
