CREATE POLICY test_policy ON some_table AS PERMISSIVE
    FOR ALL
    TO some_role
    USING ( current_user = c1 )
    WITH CHECK ( current_user = c2)

CREATE POLICY test_policy ON some_table AS RESTRICTIVE
    FOR UPDATE
    TO CURRENT_USER
    USING ( current_user = c1 )
