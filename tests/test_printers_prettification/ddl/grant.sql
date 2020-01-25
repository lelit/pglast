GRANT ALL ON SCHEMA foo TO role1, role2 WITH GRANT OPTION
=
GRANT ALL PRIVILEGES
  ON SCHEMA foo
  TO role1, role2
  WITH GRANT OPTION

GRANT update(field1) ON TABLE tab1 TO role1
=
GRANT UPDATE (field1)
  ON TABLE tab1
  TO role1

GRANT all(field1, field2) ON TABLE tab2 TO role2
=
GRANT ALL PRIVILEGES (field1, field2)
  ON TABLE tab2
  TO role2
