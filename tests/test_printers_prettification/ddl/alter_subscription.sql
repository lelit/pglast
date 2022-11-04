alter subscription mysub set publication insert_only
=
ALTER SUBSCRIPTION mysub SET PUBLICATION insert_only

alter subscription mysub set publication insert_only with (enabled = false)
=
ALTER SUBSCRIPTION mysub
  SET PUBLICATION insert_only
 WITH (enabled = false)

alter subscription "Mysub" add publication insert_only
=
ALTER SUBSCRIPTION "Mysub" ADD PUBLICATION insert_only

alter subscription "Mysub" add publication insert_only with (enabled = true)
=
ALTER SUBSCRIPTION "Mysub"
  ADD PUBLICATION insert_only
 WITH (enabled = true)

alter subscription "Mysub" drop publication insert_only
=
ALTER SUBSCRIPTION "Mysub" DROP PUBLICATION insert_only

alter subscription "Mysub" DROP publication insert_only with (enabled = false)
=
ALTER SUBSCRIPTION "Mysub"
 DROP PUBLICATION insert_only
 WITH (enabled = false)

alter subscription "Mysub" refresh publication
=
ALTER SUBSCRIPTION "Mysub" REFRESH PUBLICATION

alter subscription "Mysub" refresh publication with (copy_data = True)
=
ALTER SUBSCRIPTION "Mysub" REFRESH PUBLICATION
 WITH (copy_data = true)
