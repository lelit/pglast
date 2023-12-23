.. -*- coding: utf-8 -*-
.. :Project:   pglast -- DO NOT EDIT: generated automatically
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017-2023 Lele Gaifax
..

================================================================
 :mod:`pglast.enums.xml` --- Constants extracted from `xml.h`__
================================================================

__ https://github.com/pganalyze/libpg_query/blob/2a00188/src/postgres/include/utils/xml.h

.. module:: pglast.enums.xml
   :synopsis: Constants extracted from xml.h


.. class:: pglast.enums.xml.PgXmlStrictness

   Corresponds to the `PgXmlStrictness enum <https://github.com/pganalyze/libpg_query/blob/2a00188/src/postgres/include/utils/xml.h#L39>`__.

   .. data:: PG_XML_STRICTNESS_LEGACY

   .. data:: PG_XML_STRICTNESS_WELLFORMED

   .. data:: PG_XML_STRICTNESS_ALL


.. class:: pglast.enums.xml.XmlBinaryType

   Corresponds to the `XmlBinaryType enum <https://github.com/pganalyze/libpg_query/blob/2a00188/src/postgres/include/utils/xml.h#L33>`__.

   .. data:: XMLBINARY_BASE64

   .. data:: XMLBINARY_HEX


.. class:: pglast.enums.xml.XmlStandaloneType

   Corresponds to the `XmlStandaloneType enum <https://github.com/pganalyze/libpg_query/blob/2a00188/src/postgres/include/utils/xml.h#L25>`__.

   .. data:: XML_STANDALONE_YES

   .. data:: XML_STANDALONE_NO

   .. data:: XML_STANDALONE_NO_VALUE

   .. data:: XML_STANDALONE_OMITTED
