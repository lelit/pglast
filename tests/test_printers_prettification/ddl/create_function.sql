CREATE OR REPLACE FUNCTION auth.login(usr varchar(16), pwd varchar(16), OUT user_id integer, OUT first_name varchar(32), OUT last_name varchar(32)) AS $$
SELECT u.id, u.first_name, u.last_name FROM auth.users u
WHERE u.name = usr AND crypt(pwd, u.password) = u.password AND u.validity @> CURRENT_DATE;
$$ LANGUAGE sql STABLE
=
CREATE OR REPLACE FUNCTION auth.login(usr varchar(16)
                                    , pwd varchar(16)
                                    , OUT user_id integer
                                    , OUT first_name varchar(32)
                                    , OUT last_name varchar(32))
AS $$
SELECT u.id, u.first_name, u.last_name FROM auth.users u
WHERE u.name = usr AND crypt(pwd, u.password) = u.password AND u.validity @> CURRENT_DATE;
$$ LANGUAGE sql stable

CREATE FUNCTION funcb(somearg text) RETURNS TABLE(c1 int, c2 text)
AS $$
SELECT 1, 'Label 1'
$$ language sql stable SECURITY INVOKER
=
CREATE FUNCTION funcb(somearg text) RETURNS  TABLE (c1 integer, c2 text)
AS $$
SELECT 1, 'Label 1'
$$ LANGUAGE sql stable SECURITY INVOKER
