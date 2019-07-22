ALTER POLICY test_policy ON some_table
    TO some_role
    USING ( current_user = c1 )
    WITH CHECK ( current_user = c2)
