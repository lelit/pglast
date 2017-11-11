# -*- coding: utf-8 -*-
# :Project:   pg_query -- Development Makefile
# :Created:   gio 03 ago 2017 14:52:45 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

export TOPDIR := $(CURDIR)
export VENVDIR := $(TOPDIR)/env
export PYTHON := $(VENVDIR)/bin/python
export SHELL := /bin/bash
export SYS_PYTHON := $(shell which python3.6 || which python3)

all: virtualenv libpg_query/LICENSE help

libpg_query/LICENSE:
	git submodule update --init

help::
	@printf "\nBuild targets\n"
	@printf   "=============\n\n"

help::
	@printf "build\n\tbuild the module\n"

.PHONY: build
build: virtualenv enums keywords libpg_query/libpg_query.a pg_query/parser.c
	$(PYTHON) setup.py build_ext --inplace

libpg_query/libpg_query.a: libpg_query/LICENSE
	$(MAKE) -C libpg_query build

pg_query/parser.c: pg_query/parser.pyx
	$(PYTHON) setup.py build_ext --inplace

help::
	@printf "recythonize\n\tforce retranslation of the pyx module\n"

.PHONY: recythonize
recythonize:
	touch pg_query/parser.pyx
	$(MAKE) build

help::
	@printf "clean\n\tremove rebuildable stuff\n"

.PHONY: clean
clean:
	$(MAKE) -C docs SPHINXBUILD=$(SPHINXBUILD) clean
	$(MAKE) -C libpg_query clean
	rm -f pg_query/*.so

help::
	@printf "distclean\n\tremove anything superfluous\n"

.PHONY: distclean
distclean:: clean
	rm -rf build dist
	git submodule deinit --all

help::
	@printf "enums\n\textract Python enums from PG sources\n"

PY_ENUMS_DIR := pg_query/enums
PY_ENUMS := $(PY_ENUMS_DIR)/lockoptions.py $(PY_ENUMS_DIR)/nodes.py \
	    $(PY_ENUMS_DIR)/parsenodes.py $(PY_ENUMS_DIR)/primnodes.py \
	    $(PY_ENUMS_DIR)/pg_class.py
PG_INCLUDE_DIR := libpg_query/src/postgres/include

.PHONY: enums
enums: $(PY_ENUMS)

$(PY_ENUMS): tools/extract_enums.py libpg_query/pg_query.h
$(PY_ENUMS_DIR)/%.py: $(PG_INCLUDE_DIR)/nodes/%.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@ docs/$(basename $(notdir $@)).rst
$(PY_ENUMS_DIR)/pg_class.py: $(PG_INCLUDE_DIR)/catalog/pg_class.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@ docs/$(basename $(notdir $@)).rst

help::
	@printf "keywords\n\textract Python keyword sets from PG sources\n"

PY_KEYWORDS_DIR := pg_query
PY_KEYWORDS := $(PY_KEYWORDS_DIR)/keywords.py

.PHONY: keywords
keywords: $(PY_KEYWORDS)

$(PY_KEYWORDS): tools/extract_keywords.py libpg_query/pg_query.h
$(PY_KEYWORDS): $(PG_INCLUDE_DIR)/parser/kwlist.h
	$(PYTHON) tools/extract_keywords.py $(PG_INCLUDE_DIR)/parser/kwlist.h $@

PG_NODES := $(PG_INCLUDE_DIR)/nodes/nodes.h $(PG_INCLUDE_DIR)/nodes/parsenodes.h \
	    $(PG_INCLUDE_DIR)/nodes/primnodes.h $(PG_INCLUDE_DIR)/nodes/value.h

.PHONY: printers-doc
printers-doc: docs/ddl.rst docs/dml.rst

docs/ddl.rst docs/dml.rst: $(PG_NODES) tools/extract_printers_doc.py
docs/%.rst: pg_query/printers/%.py
	$(PYTHON) tools/extract_printers_doc.py $< $@ $(PG_NODES)

help::
	@printf "doc\n\tbuild Sphinx documentation\n"

SPHINXBUILD := $(VENVDIR)/bin/sphinx-build

.PHONY: doc
doc:
	$(MAKE) -C docs SPHINXBUILD=$(SPHINXBUILD) html

help::
	@printf "check\n\trun the test suite\n"

PYTEST = $(VENVDIR)/bin/pytest $(PYTEST_OPTIONS)

.PHONY: check
check: build
	$(PYTEST) tests/
	$(MAKE) -C docs SPHINXBUILD=$(SPHINXBUILD) doctest

include Makefile.virtualenv
include Makefile.release
