CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement)
(
    sfunc = ordered_set_transition,
    stype = internal,
    finalfunc = percentile_disc_final,
    finalfunc_extra
)
=
CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement) (
    sfunc = ordered_set_transition
  , stype = internal
  , finalfunc = percentile_disc_final
  , finalfunc_extra
)

CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement)
(
    sfunc = ordered_set_transition,
    stype = internal,
    finalfunc = percentile_disc_final,
    finalfunc_extra
)
=
CREATE AGGREGATE percentile_disc (float8 ORDER BY anyelement) (
  sfunc = ordered_set_transition,
  stype = internal,
  finalfunc = percentile_disc_final,
  finalfunc_extra
)
:
{'comma_at_eoln': True}
