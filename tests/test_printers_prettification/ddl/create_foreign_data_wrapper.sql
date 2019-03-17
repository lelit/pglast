CREATE FOREIGN DATA WRAPPER mywrapper validator myvalf OPTIONS (debug 'true', foo 'bar')
=
CREATE FOREIGN DATA WRAPPER mywrapper
  VALIDATOR myvalf
  OPTIONS (debug 'true'
         , foo 'bar')

CREATE FOREIGN DATA WRAPPER mywrapper validator myvalf OPTIONS (debug 'true', foo 'bar')
=
CREATE FOREIGN DATA WRAPPER mywrapper
  VALIDATOR myvalf
  OPTIONS (debug 'true', foo 'bar')
:
{'compact_lists_margin': 40}

CREATE FOREIGN DATA WRAPPER mywrapper validator myvalf
OPTIONS (debug 'true', foo 'bar', abra 'cadabra')
=
CREATE FOREIGN DATA WRAPPER mywrapper
  VALIDATOR myvalf
  OPTIONS (debug 'true'
         , foo 'bar'
         , abra 'cadabra')
:
{'compact_lists_margin': 40}

CREATE FOREIGN DATA WRAPPER file HANDLER myhandler validator myvalf
=
CREATE FOREIGN DATA WRAPPER file
  HANDLER myhandler
  VALIDATOR myvalf

CREATE FOREIGN DATA WRAPPER file HANDLER myhandler validator myvalf
=
CREATE FOREIGN DATA WRAPPER file
  HANDLER myhandler VALIDATOR myvalf
:
{'compact_lists_margin': 40}
