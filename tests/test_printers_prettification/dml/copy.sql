COPY manual_export TO STDOUT WITH (FORMAT CSV, HEADER)
=
COPY manual_export TO STDOUT
WITH (FORMAT csv
    , HEADER)

COPY country TO STDOUT (format csv, delimiter '|', null '~', freeze 0)
=
COPY country TO STDOUT
WITH (FORMAT csv
    , DELIMITER '|'
    , NULL '~'
    , FREEZE 0)

COPY country TO PROGRAM 'gzip > /usr1/proj/bray/sql/country_data.gz'
=
COPY country TO PROGRAM 'gzip > /usr1/proj/bray/sql/country_data.gz'
