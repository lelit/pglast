CREATE EVENT TRIGGER abort_ddl ON ddl_command_start EXECUTE PROCEDURE abort_any_command()
=
CREATE EVENT TRIGGER abort_ddl ON ddl_command_start
  EXECUTE PROCEDURE abort_any_command()

create event trigger abort_ddl on ddl_command_start
when tag in ('foo', 'bar') execute procedure a()
=
CREATE EVENT TRIGGER abort_ddl ON ddl_command_start
  WHEN tag IN ('foo', 'bar')
  EXECUTE PROCEDURE a()

create event trigger abort_ddl on ddl_command_start
when tag in ('foo', 'bar') and tag in ('other') execute procedure a()
=
CREATE EVENT TRIGGER abort_ddl ON ddl_command_start
  WHEN tag IN ('foo', 'bar')
   AND tag IN ('other')
  EXECUTE PROCEDURE a()
