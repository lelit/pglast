alter subscription foo disable

alter subscription foo set publication x, y with (refresh = true)

alter subscription foo refresh publication

alter subscription foo refresh publication with (copy_data = true)
