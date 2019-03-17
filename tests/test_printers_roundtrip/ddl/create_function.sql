CREATE OR REPLACE FUNCTION funca(somearg text, someotherarg text) RETURNS void
AS $$
BEGIN
    PERFORM $function$<some_string_literal>$function$;
    RETURN;
END;
$$ language plpgsql IMMUTABLE PARALLEL SAFE STRICT

CREATE FUNCTION funcb(somearg text) RETURNS TABLE(c1 int, c2 text)
AS $$
SELECT 1, 'Label 1'
$$ language sql SECURITY INVOKER

CREATE FUNCTION funcb() RETURNS TABLE(c1 int, c2 text)
AS $$
SELECT 1, 'Label 1'
$$ language sql SECURITY DEFINER

CREATE FUNCTION func_in_c(arg text) RETURNS text AS 'function_name', 'lib.so'
LANGUAGE C

CREATE FUNCTION funcc(arg text = 'default_val', OUT arg2 text, INOUT arg3 text, VARIADIC
arglist text[]) RETURNS SETOF integer AS $$
$$ language sql
