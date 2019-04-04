SELECT m.name FROM manufacturers m
WHERE (m.deliver_date = CURRENT_DATE
       OR m.deliver_time = CURRENT_TIME
       OR m.deliver_ts IN (LOCALTIME, CURRENT_TIMESTAMP, LOCALTIMESTAMP))
   AND m.who = CURRENT_USER
   AND m.role = CURRENT_ROLE

SELECT 'a', 123, 3.14159, $$this is a "complex" string containing apostrophe (')
and newline (\n)$$, U&'Euro symbol: \20ac', 'Naïve',
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

SELECT pc.id, pc.values[1] FROM ONLY ns.table

SELECT 'accbf276-705b-11e7-b8e4-0242ac120002'::UUID as "X"

SELECT 'foo' as "Naïve"

SELECT 'foo' as """DoubleQuoted"""

SELECT CAST('accbf276-705b-11e7-b8e4-0242ac120002' AS uuid) as "X"

SELECT CAST('accbf276-705b-11e7-b8e4-0242ac120002' AS "MySchema"."MyType") as "X"

SELECT pc.id as x, common.func(pc.name, ' ')
FROM ns.table pc
ORDER BY pc.name ASC NULLS LAST

SELECT * FROM manufacturers
ORDER BY EXTRACT('year' FROM deliver_date) ASC,
         EXTRACT('month' FROM deliver_date) ASC,
         EXTRACT('day' FROM deliver_date) ASC

SELECT (DATE '2001-02-16', DATE '2001-12-21') OVERLAPS
       (DATE '2001-10-30', DATE '2002-10-30')

select ((c.one + 1) * (c.two - 1)) / (c.three + 1) from sometable c

select true
from sometable c
where ((c.one + 1) * (c.two - 1)) / (c.three + 1) > 1

SELECT pc.id as "foo bar"
FROM ns.table pc
ORDER BY pc.name DESC NULLS FIRST

SELECT x.id, (select count(*) FROM sometable as y where y.id = x.id) count
from firsttable as x

select id, count(*) FROM sometable GROUP BY id
order by id desc nulls last

select id, count(*) FROM sometable GROUP BY GROUPING SETS ((c1, c2), (c1, c3))

select id, count(*) FROM sometable GROUP BY GROUPING SETS (id, c2)

select id, count(*) FROM sometable GROUP BY CUBE (id, c2)

select id, count(*) FROM sometable GROUP BY ROLLUP (id, c2)

select id, count(*) FROM sometable
GROUP BY GROUPING SETS ((id, c1), CUBE(c2, c3))

SELECT id, count(*) FROM sometable GROUP BY id having count(*) > 2
order by count(*) using @> nulls first

SELECT DISTINCT value FROM sometable WHERE NOT disabled

SELECT DISTINCT ON (pc.id) pc.id as x, pc.foo, pc.bar, other.some
FROM ns.table AS pc, ns.other as other
WHERE pc.id < 10 and pc.foo = 'a'
  and (pc.foo = 'b' or pc.foo = 'c'
       and (x = 1 or x = 2))

select a,b from sometable
union
select c,d from othertable

select a,b from sometable
union all
select c,d from othertable

select a,b from sometable
except
select c,d from othertable

select a,b from sometable
intersect all
select c,d from othertable

SELECT count(distinct a) from sometable

SELECT 1 OPERATOR(pg_catalog.>) 0

SELECT (a + b)::int

SELECT (a, b, c) = (d, e, f)

SELECT * FROM generate_series(1, 10) as t(i int)

SELECT array_agg(a ORDER BY b DESC) FROM sometable

SELECT count(*) AS a, count(*) FILTER (WHERE i < 5 or i > 10) AS b
FROM sometable

SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY income) FROM households

SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname)
FROM empsalary

SELECT depname, empno, salary,
       rank() OVER (PARTITION BY depname ORDER BY salary DESC)
FROM empsalary

SELECT salary, sum(salary) OVER () FROM empsalary

SELECT salary, sum(salary) OVER (ORDER BY salary) FROM empsalary

SELECT "Depname", "Empno", "Salary", enroll_date,
      rank() OVER (PARTITION BY "Depname" ORDER BY "Salary" DESC, "Empno") AS pos
FROM empsalary

SELECT sum(salary) OVER "X", avg(salary) OVER y
FROM empsalary
WINDOW "X" AS (PARTITION BY depname ORDER BY salary DESC),
       y as (order by salary)

SELECT sum(salary) OVER (x), avg(salary) OVER y
FROM empsalary
WINDOW x AS (PARTITION BY depname ORDER BY salary DESC),
       y as (order by salary)

SELECT CustomerID,
       SUM(TotalDue) OVER(PARTITION BY CustomerID
                          ORDER BY OrderDate
                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
FROM SalesOrderHeader

SELECT CustomerID,
       SUM(TotalDue) OVER(PARTITION BY CustomerID
                          ORDER BY OrderDate
                          RANGE BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)
FROM SalesOrderHeader

SELECT CustomerID,
       SUM(TotalDue) OVER(PARTITION BY CustomerID
                          ORDER BY OrderDate
                          RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
FROM SalesOrderHeader

SELECT CustomerID,
       SUM(TotalDue) OVER(PARTITION BY CustomerID
                          ORDER BY OrderDate
                          ROWS BETWEEN 0 PRECEDING AND 2 FOLLOWING)
FROM SalesOrderHeader

SELECT CustomerID,
       SUM(TotalDue) OVER(PARTITION BY CustomerID
                          ORDER BY OrderDate
                          ROWS BETWEEN 1 PRECEDING AND 2 PRECEDING)
FROM SalesOrderHeader

SELECT CustomerID,
       SUM(TotalDue) OVER(PARTITION BY CustomerID
                          ORDER BY OrderDate
                          ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
FROM SalesOrderHeader

SELECT "CustomerID",
       SUM(TotalDue) OVER(PARTITION BY "CustomerID"
                          ORDER BY "OrderDate"
                          RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
FROM SalesOrderHeader

select a.id, b.value
from sometable a join othertable b on b.id = a.id

select a.id, b.value
from sometable a natural join othertable b

select a."Id", b.value
from sometable a join othertable b using ("Id")

select a.* from a left join (select distinct id from b) as b on a."Id" = b."Id"

select name from sometable limit 2 offset 3

select name from sometable offset 3 fetch next 2 rows only

SELECT m.* FROM mytable m FOR UPDATE

SELECT m.* FROM mytable m FOR UPDATE NOWAIT

SELECT m.* FROM mytable m FOR UPDATE SKIP LOCKED

SELECT m.* FROM mytable m FOR KEY SHARE

SELECT m.* FROM mytable m FOR NO KEY UPDATE

SELECT m.* FROM mytable m FOR SHARE of m nowait

select case a.value when 0 then '1' else '2' end from sometable a

select case when a.value = 0 then '1' else '2' end from sometable a

SELECT schedule[1:2][1:1] FROM sal_emp WHERE name = 'Bill'

SELECT schedule[:2][2:] FROM sal_emp WHERE name = 'Bill'

SELECT schedule[:][1:1] FROM sal_emp WHERE name = 'Bill'

SELECT concat_lower_or_upper(a => 'Hello', b => 'World')

SELECT concat_lower_or_upper('Hello', 'World', "UpperCase" => true)

SELECT (arrayfunction($1,$2))[42]

SELECT (arrayfunction(1)).field1[42][7]."Field2"

SELECT (myfunc(x)).* FROM some_table

SELECT (myfunc(x)).a, (myfunc(x)).b, (myfunc(x)).c FROM some_table

SELECT (compositecol).a FROM sometable

SELECT ("Sometable"."CompositeCol")."A" FROM sometable

SELECT * FROM unnest(ARRAY['a','b','c','d','e','f']) WITH ORDINALITY

SELECT * FROM pg_ls_dir('.') WITH ORDINALITY AS t(ls,n)

SELECT * FROM ROWS FROM(generate_series(10,11), get_users()) WITH ORDINALITY

SELECT * FROM (VALUES (1),(2),(3)) v(r)
 LEFT JOIN ROWS FROM( foo_sql(11,13), foo_mat(11,13) )
 WITH ORDINALITY AS f(i1,s1,i2,s2,o) ON (r+i1+i2)<100

SELECT * FROM t1 CROSS JOIN t2

SELECT i.q1, i.q2, ss.column1
FROM int8_tbl i, LATERAL (VALUES (i.*::int8_tbl)) ss

SELECT * FROM (VALUES (1, 'one'), (2, 'two')) AS t (num, "English")

SELECT ARRAY(SELECT age FROM employees)

SELECT ARRAY[]

SELECT m.name AS mname, pname
FROM manufacturers m, LATERAL get_product_names(m.id) pname

SELECT m.name AS mname, pname
FROM manufacturers m LEFT JOIN LATERAL get_product_names(m.id) pname ON true

SELECT "A".id, "B".id
FROM table_a AS "A" RIGHT JOIN table_b AS "B" ON "A".id = "B".id

SELECT a.id, b.id
FROM table_a FULL JOIN table_b ON a.id = b.id

SELECT a.* FROM (my_table AS a JOIN your_table AS b ON a.value = b.value) AS c

SELECT a.* FROM (my_table AS a JOIN your_table AS b ON a.value = b.value) AS "C"

SELECT m.name FROM manufacturers m
WHERE (m.deliver_date = CURRENT_DATE
       OR m.deliver_time = CURRENT_TIME
       OR m.deliver_ts IN (LOCALTIME, CURRENT_TIMESTAMP, LOCALTIMESTAMP))
   AND m.who = CURRENT_USER
   AND m.role = CURRENT_ROLE

SELECT m.id FROM manufacturers m WHERE m.deliver_date IS NULL

SELECT m.id FROM manufacturers m WHERE m.deliver_date IS NOT NULL

SELECT t1.c1 FROM t1 WHERE (a IS NULL) != (b IS NULL)

SELECT true IS true

SELECT true IS NOT true

SELECT true IS false

SELECT true IS NOT false

SELECT true IS unknown

SELECT true IS NOT unknown

SELECT m.id FROM manufacturers m WHERE ROW(m.hours, m.minutes) < ROW(10, 20)

WITH t AS (
    SELECT random() as x FROM generate_series(1, 3)
  )
SELECT * FROM t
UNION ALL
SELECT * FROM t

WITH "T" AS (
    SELECT random() as x FROM generate_series(1, 3)
  )
SELECT * FROM "T"
UNION ALL
SELECT * FROM "T"

SELECT * FROM "T"
UNION ALL
SELECT * FROM "T"
ORDER BY 1, 2, 3

SELECT * FROM "T"
UNION ALL
SELECT * FROM "T"
ORDER BY 1, 2, 3
LIMIT 2 OFFSET 1

WITH RECURSIVE employee_recursive("Distance", employee_name, manager_name) AS (
    SELECT 1, employee_name, manager_name
    FROM employee
    WHERE manager_name = 'Mary'
  UNION ALL
    SELECT er."Distance" + 1, e.employee_name, e.manager_name
    FROM employee_recursive er, employee e
    WHERE er.employee_name = e.manager_name
  )
SELECT distance, employee_name FROM employee_recursive

SELECT true FROM sometable as "ST" WHERE "ST"."Value" = ANY(ARRAY[1,2])

SELECT true FROM sometable WHERE id1 is distinct from id2

SELECT true FROM sometable WHERE id1 is not distinct from id2

SELECT NULLIF(value, othervalue) FROM sometable

SELECT x, x IS OF (text) AS is_text FROM q

SELECT x, x IS OF ("MyType") AS "IsMyType" FROM q

SELECT x, x IS NOT OF (text) AS is_not_text FROM q

SELECT true FROM sometable WHERE value IN (1,2,3)

SELECT true FROM sometable WHERE value NOT IN (1,2,3)

SELECT true FROM sometable WHERE email LIKE 'lele@%'

SELECT true FROM sometable WHERE email NOT LIKE 'lele@%'

SELECT true FROM sometable WHERE email ILIKE 'lele@%'

SELECT true FROM sometable WHERE email NOT ILIKE 'lele@%'

SELECT true FROM sometable WHERE email SIMILAR TO 'lele@_*'

SELECT true FROM sometable WHERE email NOT SIMILAR TO 'lele@_+'

SELECT true FROM sometable WHERE email SIMILAR TO 'lele@_*' ESCAPE 'X'

SELECT true FROM sometable WHERE value between 1 and 5

SELECT true FROM sometable WHERE value not between 1 and 5

SELECT true FROM sometable WHERE value BETWEEN SYMMETRIC 5 and 1

SELECT true FROM sometable WHERE value NOT BETWEEN SYMMETRIC 5 and 1

SELECT user, session_user, current_catalog, current_schema

SELECT value FROM sometable WHERE id = $1

SELECT value FROM sometable WHERE id = ?

SELECT value FROM sometable WHERE value like $1

SELECT concat_ws($1::VARCHAR, p.last_name, p.first_name) AS "Redactor"
FROM procs AS sp
WHERE sp.cid = $2::UUID AND sp.name ILIKE $3::VARCHAR(192)
ORDER BY sp.name

SELECT CAST(1.234 AS NUMERIC(5,2))

SELECT now()::time(0) with time zone

SELECT now()::timestamp(0) with time zone

SELECT
  pc.id,
  pc.person_id,
  pc.company_id,
  concat_ws(' ', p.last_name, p.first_name) AS "Person",
  p.last_name,
  p.first_name,
  p.gender,
  p.birthdate,
  p.code,
  pc.person_contract_kind_id,
  ck.name AS "ContractKind",
  pc.validity,
  pc.validity @> CURRENT_DATE AS "Valid",
  (SELECT format('[%s] %s',
                 count(*),
                 string_agg(CASE
                              WHEN (cp.role_id IS NOT NULL
                                    AND cp.company_site_id IS NOT NULL)
                                THEN format('%s %s (%s)', pcr.code, pcr.name, cs.name)
                              WHEN (cp.role_id IS NOT NULL)
                                THEN format('%s %s', pcr.code, pcr.name)
                              ELSE cs.name
                            END, ', ')) AS format_1
   FROM risk.company_persons AS cp
   LEFT OUTER JOIN risk.company_sites AS cs ON cs.id = cp.company_site_id
   LEFT OUTER JOIN risk.project_company_roles AS pcr ON pcr.id = cp.role_id
   WHERE cp.person_id = pc.person_id) AS "Roles"
FROM risk.person_contracts AS pc
JOIN risk.persons AS p ON p.id = pc.person_id
JOIN risk.person_contract_kinds AS ck ON ck.id = pc.person_contract_kind_id
WHERE pc.company_id = 'accbf276-705b-11e7-b8e4-0242ac120002'
  AND pc.validity @> CURRENT_DATE = true
ORDER BY "Person"

SELECT coalesce(deliver_date, today) from manufacturers

SELECT nullif(deliver_date, today) from manufacturers

SELECT greatest(deliver_date, today) from manufacturers

SELECT least(deliver_date, today) from manufacturers

SELECT a < ('foo' COLLATE "fr_FR") FROM test1

SELECT a < b COLLATE "de_DE" FROM test1

SELECT * FROM test1 ORDER BY a || b COLLATE "fr_FR"

SELECT variadic_function(VARIADIC ARRAY['param1']);

SELECT variadic_function('value1', VARIADIC ARRAY['param2']);
