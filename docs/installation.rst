.. -*- coding: utf-8 -*-
.. :Project:   pglast -- Installation
.. :Created:   gio 10 ago 2017 10:03:58 CEST
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2017, 2018, 2021 Lele Gaifax
..

==============
 Installation
==============

As usual, the easiest way is with pip::

  $ pip install pglast

Alternatively you can clone the repository::

  $ git clone https://github.com/lelit/pglast.git --recursive

and install from there::

  $ pip install ./pglast

Development
-----------

There is a set of *makefiles* implementing the most common operations, a ``make help`` will
show a brief table of contents. A comprehensive test suite, based on pytest__, covers 99% of
the source lines.

__ https://docs.pytest.org/en/latest/
