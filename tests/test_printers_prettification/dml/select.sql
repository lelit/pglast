select * from sometable
=
SELECT *
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
        WHERE (othertable.x = 1)
          AND (othertable.y = 2)
          AND (othertable.z = 3))
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
        WHERE (othertable.x = 1) AND (othertable.y = 2) AND (othertable.z = 3))
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
        WHERE (othertable.x = 1)
          AND (othertable.y = 2)
          AND (othertable.z = 3))
FROM sometable
WHERE c BETWEEN 1 AND 2
:
{'compact_lists_margin': 75}

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
        WHERE (othertable.x = 1)
          AND (othertable.y = 2)
          AND (othertable.z = 3))
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
     LEFT JOIN table3 AS cp
               INNER JOIN table4 AS c ON cp.company_id = c.id
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
WHERE rn = (SELECT (floor((random() * max_rn)) + 1))

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
     , (   (    (NOT a.bool_flag)
            AND (a.something IS NULL))
        OR (a.other = 3)) AS foo
     , a.value1 + (b.value2 * b.value3) AS bar
FROM sometable AS a
WHERE ((    (NOT a.bool_flag2)
        AND (a.something2 IS NULL))
   OR (a.other2 = 3))

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
            INNER JOIN r ON (r.contract_id = c.id)
       WHERE (c.person_id = p.id)) ILIKE 'manager%'

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
                         , '2001-02-16 20:38:40'::timestamp)

SELECT TIMESTAMP '2001-02-16 20:38:40' AT TIME ZONE 'MST'
=
SELECT '2001-02-16 20:38:40'::timestamp AT TIME ZONE 'MST'
:
{'special_functions': True}

SELECT * FROM manufacturers
ORDER BY EXTRACT('year' FROM deliver_date) ASC,
         EXTRACT('month' FROM deliver_date) ASC,
         EXTRACT('day' FROM deliver_date) ASC
=
SELECT *
FROM manufacturers
ORDER BY pg_catalog.date_part('year', deliver_date) ASC
       , pg_catalog.date_part('month', deliver_date) ASC
       , pg_catalog.date_part('day', deliver_date) ASC

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
SELECT pg_catalog.overlaps('2001-02-16'::date
                         , '2001-12-21'::date
                         , '2001-10-30'::date
                         , '2002-10-30'::date)

SELECT (DATE '2001-02-16', DATE '2001-12-21') OVERLAPS
       (DATE '2001-10-30', DATE '2002-10-30')
=
SELECT ('2001-02-16'::date, '2001-12-21'::date) OVERLAPS ('2001-10-30'::date, '2002-10-30'::date)
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
