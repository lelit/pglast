CREATE COLLATION french (locale = 'fr_FR.utf8')

CREATE COLLATION IF NOT EXISTS french (locale = 'fr_FR.utf8')

CREATE COLLATION german_phonebook (provider = icu, locale = 'de-u-co-phonebk')

CREATE COLLATION german FROM "de_DE"

CREATE COLLATION IF NOT EXISTS german FROM "de_DE"

CREATE COLLATION mycoll2 ( LC_COLLATE = "POSIX", LC_CTYPE = "POSIX" )
