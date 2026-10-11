.. -*- coding: utf-8 -*-
.. :Project:   pglast — Operators precedence logic
.. :Created:   sab 10 ott 2026, 16:47:46
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   GNU General Public License version 3 or later
.. :Copyright: © 2026 Lele Gaifax
..

=========================================================
 :mod:`pglast.precedence` --- Operators precedence logic
=========================================================

The functions here answer the question *"does this node need to be wrapped in parentheses when
it is used as an operand of that other expression?"*, which cannot be decided by looking at a
node alone: the same node needs parens in one slot and not in another.

The vocabulary mirrors the ``PostgreSQL`` grammar rules: an expression is printed either in an
``a_expr``, a ``b_expr`` or a ``c_expr`` *context*, and the rule that handles a node determines
its *precedence*.

.. automodule:: pglast.precedence
   :synopsis: Precedence and position aware parenthesization of expressions
   :members:
