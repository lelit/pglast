DELETE FROM films

DELETE FROM ONLY films

DELETE FROM tasks WHERE status = 'DONE' RETURNING *

DELETE FROM employees
WHERE EXISTS(SELECT id FROM acme_persons WHERE name='lele')

DELETE FROM employees
WHERE id != ALL(SELECT id FROM acme_persons WHERE name='lele')

WITH acme_persons(id) as (SELECT id FROM accounts WHERE name = 'Acme Corporation')
DELETE FROM employees
WHERE id IN (SELECT id FROM acme_persons)

DELETE FROM films USING producers
WHERE producer_id = producers.id AND producers.name = 'foo'

DELETE FROM extensions WHERE values[0] = $1
