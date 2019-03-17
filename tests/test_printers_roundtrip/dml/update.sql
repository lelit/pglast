update sometable set value = 'foo' where id = 'bar'

UPDATE weather SET temp_lo = temp_lo+1, temp_hi = temp_lo+15, prcp = DEFAULT
WHERE city = 'San Francisco' AND date = '2003-07-03'
RETURNING temp_lo, temp_hi, prcp

UPDATE employees SET sales_count = sales_count + 1 FROM accounts
WHERE accounts.name = 'Acme Corporation'
AND employees.id = accounts.sales_person

UPDATE employees SET sales_count = sales_count + 1 WHERE id =
  (SELECT sales_person FROM accounts WHERE name = 'Acme Corporation')

WITH acme_persons(id) as (SELECT id FROM accounts WHERE name = 'Acme Corporation')
UPDATE employees SET sales_count = sales_count + 1
WHERE id=(select id from acme_persons)

UPDATE accounts SET (contact_first_name, contact_last_name) =
    (SELECT first_name, last_name FROM salesmen
     WHERE salesmen.id = accounts.sales_id)

UPDATE tictactoe
SET board[1:3][1:3] = '{{" "," "," "},{" "," "," "},{" "," "," "}}'
WHERE game = 1

UPDATE extensions
SET values[0] = '.gif'
WHERE mime_type = 'image/gif'

UPDATE extensions SET values[0] = $1 WHERE mime_type = $2 Returning "Changed"
