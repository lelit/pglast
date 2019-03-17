COMMENT ON VIEW "MySchema"."MyView" IS
  'Lorem ipsum dolor sit amet, consectetur adipisicing elit,'
  ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  ' Ut enimad minim veniam, quis nostrud exercitation ullamco laboris.'
=
COMMENT ON VIEW "MySchema"."MyView"
  IS 'Lorem ipsum dolor sit amet, consectetur adipisicin'
     'g elit, sed do eiusmod tempor incididunt ut labore'
     ' et dolore magna aliqua. Ut enimad minim veniam, q'
     'uis nostrud exercitation ullamco laboris.'
:
{'split_string_literals_threshold': 50}
