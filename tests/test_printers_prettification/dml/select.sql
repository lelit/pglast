select * from sometable
=
SELECT *
FROM sometable

select from sometable
=
SELECT
FROM sometable

select 'foo' as barname,b,c from sometable where c between 1 and 2
=
SELECT 'foo' AS barname
     , b
     , c
FROM sometable
WHERE c BETWEEN 1 AND 2

select 'foo' as barname,b,c from sometable where c between 1 and 2
=
SELECT 'foo' AS barname, b, c
FROM sometable
WHERE c BETWEEN 1 AND 2
:
{'compact_lists_margin': 80}

select 'foo' as barname,b,c,
       (select somevalue
        from othertable
        where othertable.x = 1 and othertable.y = 2 and othertable.z = 3)
from sometable where c between 1 and 2
=
SELECT 'foo' AS barname
     , b
     , c
     , (SELECT somevalue
        FROM othertable
        WHERE othertable.x = 1
          AND othertable.y = 2
          AND othertable.z = 3)
FROM sometable
WHERE c BETWEEN 1 AND 2

select 'foo' as barname,b,c,
       (select somevalue
        from othertable
        where othertable.x = 1 and othertable.y = 2 and othertable.z = 3)
from sometable where c between 1 and 2
=
SELECT 'foo' AS barname
     , b
     , c
     , (SELECT somevalue
        FROM othertable
        WHERE othertable.x = 1 AND othertable.y = 2 AND othertable.z = 3)
FROM sometable
WHERE c BETWEEN 1 AND 2
:
{'compact_lists_margin': 80}

select 'foo' as barname,b,c,
       (select somevalue
        from othertable
        where othertable.x = 1 and othertable.y = 2 and othertable.z = 3)
from sometable where c between 1 and 2
=
SELECT 'foo' AS barname
     , b
     , c
     , (SELECT somevalue
        FROM othertable
        WHERE othertable.x = 1
          AND othertable.y = 2
          AND othertable.z = 3)
FROM sometable
WHERE c BETWEEN 1 AND 2
:
{'compact_lists_margin': 60}

select 'foo' as barname,b,c,
       (select somevalue
        from othertable
        where othertable.x = 1 and othertable.y = 2 and othertable.z = 3)
from sometable where c between 1 and 2
=
SELECT 'foo' AS barname,
       b,
       c,
       (SELECT somevalue
        FROM othertable
        WHERE othertable.x = 1
          AND othertable.y = 2
          AND othertable.z = 3)
FROM sometable
WHERE c BETWEEN 1 AND 2
:
{'comma_at_eoln': True}

select 'foo' as barname,b,c from sometable where c between 1 and c.threshold
=
SELECT 'foo' AS barname
     , b
     , c
FROM sometable
WHERE c BETWEEN 1 AND c.threshold

select somefunc(1, 2, 3)
=
SELECT somefunc(1, 2, 3)

SELECT pe.id
FROM table1 as pe
INNER JOIN table2 AS pr ON pe.project_id = pr.id
LEFT JOIN table3 AS cp ON cp.person_id = pe.id
INNER JOIN table4 AS c ON cp.company_id = c.id
=
SELECT pe.id
FROM table1 AS pe
     INNER JOIN table2 AS pr ON pe.project_id = pr.id
     LEFT JOIN table3 AS cp ON cp.person_id = pe.id
     INNER JOIN table4 AS c ON cp.company_id = c.id

SELECT pe.id
FROM table1 as pe
INNER JOIN table2 AS pr ON pe.project_id = pr.id
LEFT JOIN (table3 AS cp INNER JOIN table4 AS c ON cp.company_id = c.id)
       ON cp.person_id = pe.id
=
SELECT pe.id
FROM table1 AS pe
     INNER JOIN table2 AS pr ON pe.project_id = pr.id
     LEFT JOIN (table3 AS cp
                INNER JOIN table4 AS c ON cp.company_id = c.id)
        ON cp.person_id = pe.id

SELECT sum(salary) OVER (x), avg(salary) OVER y
FROM empsalary
WINDOW x AS (PARTITION BY depname ORDER BY salary DESC),
       y as (order by salary)
=
SELECT sum(salary) OVER (x)
     , avg(salary) OVER y
FROM empsalary
WINDOW x AS (PARTITION BY depname
             ORDER BY salary DESC)
     , y AS (ORDER BY salary)

select c_id
from (select c_id, row_number() over (order by c_d_id) as rn,  count(*) over() max_rn
      from customer where c_d_id=5) t
where rn = (select floor(random()*(max_rn))+1)
=
SELECT c_id
FROM (SELECT c_id
           , row_number() OVER (ORDER BY c_d_id) AS rn
           , count(*) OVER () AS max_rn
      FROM customer
      WHERE c_d_id = 5) AS t
WHERE rn = (SELECT floor(random() * max_rn) + 1)

select a.* from a left join (select distinct id from b) as b on a.id = b.id
=
SELECT a.*
FROM a
     LEFT JOIN (SELECT DISTINCT id
                FROM b) AS b ON a.id = b.id

select a.one,
       not a.bool_flag and a.something is null or a.other = 3 as foo,
       a.value1 + b.value2 * b.value3 as bar
from sometable as a
where not a.bool_flag2 and a.something2 is null or a.other2 = 3
=
SELECT a.one
     ,    (NOT a.bool_flag
       AND a.something IS NULL)
       OR a.other = 3 AS foo
     , a.value1 + (b.value2 * b.value3) AS bar
FROM sometable AS a
WHERE (NOT a.bool_flag2
   AND a.something2 IS NULL)
   OR a.other2 = 3

select p.name, (select format('[%s] %s', count(*), r.name)
                from c join r on r.contract_id = c.id
                where c.person_id = p.id) as roles
from persons as p
where p.name like 'lele%' and ((select format('[%s] %s', count(*), r.name)
                                from c join r on r.contract_id = c.id
                                where c.person_id = p.id) ilike 'manager%')
=
SELECT p.name
     , (SELECT format('[%s] %s'
                    , count(*)
                    , r.name)
        FROM c
             INNER JOIN r ON r.contract_id = c.id
        WHERE c.person_id = p.id) AS roles
FROM persons AS p
WHERE p.name LIKE 'lele%'
  AND (SELECT format('[%s] %s'
                   , count(*)
                   , r.name)
       FROM c
            INNER JOIN r ON r.contract_id = c.id
       WHERE c.person_id = p.id) ILIKE 'manager%'

SELECT
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkl'
'mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
=
SELECT 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX'
       'YZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV'
       'WXYZ1234567890'
:
{'split_string_literals_threshold': 50}

SELECT
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkl'
'mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890'
=
SELECT E'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX'
        'YZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV'
        'WXYZ\n1234567890'
:
{'split_string_literals_threshold': 50}

SELECT '1234567890\abcdefghi'
=
SELECT '1234567890\a'
       'bcdefghi'
:
{'split_string_literals_threshold': 11}

SELECT TIMESTAMP '2001-02-16 20:38:40' AT TIME ZONE 'MST'
=
SELECT pg_catalog.timezone('MST'
                         , CAST('2001-02-16 20:38:40' AS timestamp))

SELECT TIMESTAMP '2001-02-16 20:38:40' AT TIME ZONE 'MST'
=
SELECT CAST('2001-02-16 20:38:40' AS timestamp) AT TIME ZONE 'MST'
:
{'special_functions': True}

SELECT * FROM manufacturers
ORDER BY EXTRACT('year' FROM deliver_date) ASC,
         EXTRACT('month' FROM deliver_date) ASC,
         EXTRACT('day' FROM deliver_date) ASC
=
SELECT *
FROM manufacturers
ORDER BY pg_catalog.extract('year', deliver_date) ASC
       , pg_catalog.extract('month', deliver_date) ASC
       , pg_catalog.extract('day', deliver_date) ASC

SELECT * FROM manufacturers
ORDER BY EXTRACT('year' FROM deliver_date) ASC,
         EXTRACT(month FROM deliver_date) ASC,
         EXTRACT('day' FROM deliver_date) ASC
=
SELECT *
FROM manufacturers
ORDER BY EXTRACT(YEAR FROM deliver_date) ASC
       , EXTRACT(MONTH FROM deliver_date) ASC
       , EXTRACT(DAY FROM deliver_date) ASC
:
{'special_functions': True}

SELECT (DATE '2001-02-16', DATE '2001-12-21') OVERLAPS
       (DATE '2001-10-30', DATE '2002-10-30')
=
SELECT pg_catalog."overlaps"(CAST('2001-02-16' AS date)
                           , CAST('2001-12-21' AS date)
                           , CAST('2001-10-30' AS date)
                           , CAST('2002-10-30' AS date))

SELECT (DATE '2001-02-16', DATE '2001-12-21') OVERLAPS
       (DATE '2001-10-30', DATE '2002-10-30')
=
SELECT (CAST('2001-02-16' AS date), CAST('2001-12-21' AS date)) OVERLAPS (CAST('2001-10-30' AS date), CAST('2002-10-30' AS date))
:
{'special_functions': True}

select email from subscribed where email not in (select email from tracks)
=
SELECT email
FROM subscribed
WHERE NOT email IN (SELECT email
                    FROM tracks)

SELECT true FROM sometable WHERE value = ANY(ARRAY[1,2])
=
SELECT TRUE
FROM sometable
WHERE value = ANY(ARRAY[1, 2])

SELECT false FROM sometable WHERE value != ALL(ARRAY[1,2])
=
SELECT FALSE
FROM sometable
WHERE value <> ALL(ARRAY[1, 2])

select c.name from table_a a, table_b b join table_c c on c.b_id = b.id where a.code = b.code
=
SELECT c.name
FROM table_a AS a
   , table_b AS b
     INNER JOIN table_c AS c ON c.b_id = b.id
WHERE a.code = b.code

select c.name from table_b b join table_c c on c.b_id = b.id, table_a a where a.code = b.code
=
SELECT c.name
FROM table_b AS b
     INNER JOIN table_c AS c ON c.b_id = b.id
   , table_a AS a
WHERE a.code = b.code

SELECT id, CASE WHEN (NOT EXISTS (SELECT TRUE FROM aaa WHERE a = 1) or exists (select true from bbb where b = 2)) and  id=1 THEN NULL ELSE NOT EXISTS (SELECT TRUE FROM ccc WHERE c = 1) END FROM bar
=
SELECT id
     , CASE
         WHEN (NOT EXISTS (SELECT TRUE
                           FROM aaa
                           WHERE a = 1)
            OR EXISTS (SELECT TRUE
                       FROM bbb
                       WHERE b = 2))
          AND id = 1
           THEN NULL
         ELSE NOT EXISTS (SELECT TRUE
                          FROM ccc
                          WHERE c = 1)
       END
FROM bar

select case a.a when 1 then 'one' when 2 then 'two' else 'something else' end from a
=
SELECT CASE a.a
         WHEN 1
           THEN 'one'
         WHEN 2
           THEN 'two'
         ELSE 'something else'
       END
FROM a

select case a.a when 1 then (select b from b) when 2 then (select c from c) else (select d from d) end from a
=
SELECT CASE a.a
         WHEN 1
           THEN (SELECT b
                 FROM b)
         WHEN 2
           THEN (SELECT c
                 FROM c)
         ELSE (SELECT d
               FROM d)
       END
FROM a

select x from d limit all
=
SELECT x
FROM d
LIMIT ALL

select x from d limit null
=
SELECT x
FROM d
LIMIT ALL

(select x from d1 order by y) intersect (select n from d2 group by y limit 3) limit 2
=
(SELECT x
 FROM d1
 ORDER BY y)
\n\
INTERSECT
\n\
(SELECT n
 FROM d2
 GROUP BY y
 LIMIT 3)
LIMIT 2

/*
header
*/ select /*one*/ 1
/*footer*/
=
/*
header
*/
SELECT /*one*/ 1
/*footer*/\s
:
{'preserve_comments': True}

-- header 1
-- header 2
select /*one*/ 1
/*
long
footer
*/
=
-- header 1
-- header 2
SELECT /*one*/ 1
/*
long
footer
*/\
:
{'preserve_comments': True}

-- header 1
-- header 2
select /*one*/ 1
/*
long
footer
*/
=
/*header 1*/ /*header 2*/ SELECT /*one*/ 1 /*long footer */
:
{'preserve_comments': True, 'raw_stream': True}

select 4294967310
=
SELECT 4294967310

select t1.*
from tab1 as t1
where t1.code like (select t2.code||'.%' from tab1 t2 where t2.id = 'foo')
=
SELECT t1.*
FROM tab1 AS t1
WHERE t1.code LIKE (SELECT t2.code || '.%'
                    FROM tab1 AS t2
                    WHERE t2.id = 'foo')

with recursive t(n) as (values (1) union all select n+1 from t where n < 100)
select sum(n) from t;
=
WITH RECURSIVE t(n)
  AS (VALUES (1)
\n\
      UNION ALL
\n\
      SELECT n + 1
      FROM t
      WHERE n < 100)
\n\
  SELECT sum(n)
  FROM t

with cte_1 as (select 1), cte_2 as (select * from cte_1)
select * from cte_2
=
WITH cte_1 AS (SELECT 1)
\n\
   , cte_2 AS (SELECT *
               FROM cte_1)
\n\
  SELECT *
  FROM cte_2

SELECT 1 FROM ONLY "public"."produit" x WHERE "produit_id"
OPERATOR(pg_catalog.=) $1 FOR KEY SHARE OF x
=
SELECT 1
FROM ONLY public.produit AS x
WHERE produit_id OPERATOR(pg_catalog.=) $1
FOR KEY SHARE OF x
