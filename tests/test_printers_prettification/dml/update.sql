update sometable set value='foo', changed=NOW where id='bar' and value<>'foo'
=
UPDATE sometable
SET value = 'foo'
  , changed = now
WHERE (id = 'bar')
  AND (value <> 'foo')

update sometable set value=null
=
UPDATE sometable
SET value = NULL

update sometable set value='foo', changed=NOW where id='bar' and value<>'foo'
=
UPDATE sometable
SET value = 'foo', changed = now
WHERE (id = 'bar') AND (value <> 'foo')
:
{'compact_lists_margin': 80}

update sometable set value='foo', changed=NOW where id='bar' and value<>'foo'
=
UPDATE sometable
SET value = 'foo', changed = now
WHERE (id = 'bar')
  AND (value <> 'foo')
:
{'compact_lists_margin': 33}
