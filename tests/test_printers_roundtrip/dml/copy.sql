copy binary manual_export TO STDOUT with null as '@'

copy binary manual_export from stdin using delimiters '|' with null as '@'

copy manual_export (a, b) to '/tmp/me.txt' with csv header escape as '^'

copy manual_export (a, b) to '/tmp/me.txt' with binary escape '^'

copy manual_export (a, b) to '/tmp/me.txt' with delimiter '|' csv header escape '^'

copy manual_export (a, b) to '/tmp/me.txt' with (header true)

copy manual_export from stdin with (format csv, header 1)

copy manual_export to stdout with (format csv, header 0)
