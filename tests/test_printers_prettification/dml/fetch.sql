fetch all foo
=
FETCH FORWARD ALL FROM foo

fetch next in foo
=
FETCH NEXT FROM foo

fetch forward 1 from foo
=
FETCH NEXT FROM foo

fetch 1 from foo
=
FETCH NEXT FROM foo

fetch backward 1 from foo
=
FETCH PRIOR FROM foo

fetch prior in foo
=
FETCH PRIOR FROM foo

fetch absolute 1 foo
=
FETCH FIRST FROM foo

fetch absolute -1 foo
=
FETCH LAST FROM foo

fetch absolute 42 foo
=
FETCH ABSOLUTE 42 FROM foo
