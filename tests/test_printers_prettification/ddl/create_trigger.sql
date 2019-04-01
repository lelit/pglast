CREATE TRIGGER trg_auth_users_100_log_changes BEFORE INSERT OR UPDATE OF password
ON auth.users FOR EACH ROW EXECUTE PROCEDURE auth.crypt_user_password()
=
CREATE TRIGGER trg_auth_users_100_log_changes
  BEFORE INSERT OR UPDATE OF password
  ON auth.users
  FOR EACH ROW
    EXECUTE PROCEDURE auth.crypt_user_password()

CREATE TRIGGER trig2 INSTEAD OF UPDATE ON table1 FOR EACH ROW EXECUTE PROCEDURE trigfunc('param')
=
CREATE TRIGGER trig2
  INSTEAD OF UPDATE
  ON table1
  FOR EACH ROW
    EXECUTE PROCEDURE trigfunc('param')

CREATE TRIGGER trg_celery_periodic_tasks_950_after_update AFTER UPDATE ON celery.periodic_tasks FOR EACH ROW
WHEN (OLD.active IS DISTINCT FROM NEW.active OR OLD.args IS DISTINCT FROM NEW.args
OR OLD.kwargs IS DISTINCT FROM NEW.kwargs OR OLD.options IS DISTINCT FROM NEW.options
OR OLD.run_every IS DISTINCT FROM NEW.run_every OR OLD.run_at_minutes IS DISTINCT FROM NEW.run_at_minutes
OR OLD.run_at_hours IS DISTINCT FROM NEW.run_at_hours OR OLD.run_on_weekdays IS DISTINCT FROM NEW.run_on_weekdays
OR OLD.run_on_days IS DISTINCT FROM NEW.run_on_days OR OLD.run_on_months IS DISTINCT FROM NEW.run_on_months)
EXECUTE PROCEDURE celery.notify_periodic_tasks_changed()
=
CREATE TRIGGER trg_celery_periodic_tasks_950_after_update
  AFTER UPDATE
  ON celery.periodic_tasks
  FOR EACH ROW
    WHEN (((   old.active IS DISTINCT FROM new.active
            OR old.args IS DISTINCT FROM new.args
            OR old.kwargs IS DISTINCT FROM new.kwargs
            OR old.options IS DISTINCT FROM new.options
            OR old.run_every IS DISTINCT FROM new.run_every
            OR old.run_at_minutes IS DISTINCT FROM new.run_at_minutes
            OR old.run_at_hours IS DISTINCT FROM new.run_at_hours
            OR old.run_on_weekdays IS DISTINCT FROM new.run_on_weekdays
            OR old.run_on_days IS DISTINCT FROM new.run_on_days
            OR old.run_on_months IS DISTINCT FROM new.run_on_months)))
    EXECUTE PROCEDURE celery.notify_periodic_tasks_changed()

CREATE TRIGGER trig1 AFTER UPDATE ON schema1.table1
FOR EACH ROW WHEN (new.col1 IS DISTINCT FROM old.col1)
EXECUTE PROCEDURE schema1.func1()
=
CREATE TRIGGER trig1
  AFTER UPDATE
  ON schema1.table1
  FOR EACH ROW
    WHEN (new.col1 IS DISTINCT FROM old.col1)
    EXECUTE PROCEDURE schema1.func1()
