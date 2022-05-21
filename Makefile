# -*- coding: utf-8 -*-
# :Project:   pglast -- Development Makefile
# :Created:   gio 03 ago 2017 14:52:45 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2022 Lele Gaifax
#

export TOPDIR := $(CURDIR)
ifeq ($(VIRTUAL_ENV),)
export VENVDIR := $(TOPDIR)/env
else
export VENVDIR := $(VIRTUAL_ENV)
endif
export PYTHON := $(VENVDIR)/bin/python
export SHELL := /bin/bash
export SYS_PYTHON := $(shell command -v python3)

all: virtualenv libpg_query/Makefile help

libpg_query/Makefile:
	git submodule update --init

help::
	@printf "\nBuild targets\n"
	@printf   "=============\n\n"

help::
	@printf "build\n\tbuild the module\n"

.PHONY: build
build: virtualenv $(VENVDIR)/extension.timestamp

$(VENVDIR)/extension.timestamp: setup.py
$(VENVDIR)/extension.timestamp: libpg_query/libpg_query.a
$(VENVDIR)/extension.timestamp: pglast/ast.pyx pglast/parser.pyx
	touch pglast/parser.pyx
	$(PYTHON) setup.py build_ext --inplace --force
	@touch $@

libpg_query/libpg_query.a: libpg_query/Makefile
libpg_query/libpg_query.a: libpg_query/src/*.c libpg_query/src/*.h
	$(MAKE) -C libpg_query build

help::
	@printf "recythonize\n\tforce retranslation of the pyx module\n"

.PHONY: recythonize
recythonize:
	rm -f $(VENVDIR)/extension.timestamp
	$(MAKE) build

help::
	@printf "clean\n\tremove rebuildable stuff\n"

.PHONY: clean
clean:
	$(MAKE) -C docs SPHINXBUILD=$(SPHINXBUILD) clean
	$(MAKE) -C libpg_query clean
	rm -f pglast/*.so

help::
	@printf "distclean\n\tremove anything superfluous\n"

.PHONY: distclean
distclean:: clean
	rm -rf build dist
	git submodule deinit --all

help::
	@printf "enums\n\textract Python enums from PG sources\n"

PY_ENUMS := pglast/enums/lockoptions.py pglast/enums/lockdefs.py \
	    pglast/enums/nodes.py pglast/enums/parsenodes.py \
	    pglast/enums/pg_attribute.py pglast/enums/pg_class.py \
	    pglast/enums/pg_trigger.py \
	    pglast/enums/primnodes.py pglast/enums/xml.py \
	    pglast/enums/pg_am.py
PG_INCLUDE_DIR := libpg_query/src/postgres/include

.PHONY: enums
enums: $(PY_ENUMS)

$(PY_ENUMS): tools/extract_enums.py libpg_query/libpg_query.a
pglast/enums/%.py: $(PG_INCLUDE_DIR)/nodes/%.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@ docs/$(basename $(notdir $@)).rst
pglast/enums/lockdefs.py: $(PG_INCLUDE_DIR)/storage/lockdefs.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@ docs/$(basename $(notdir $@)).rst
pglast/enums/pg_am.py: $(PG_INCLUDE_DIR)/catalog/pg_am.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@ docs/$(basename $(notdir $@)).rst
pglast/enums/pg_attribute.py: $(PG_INCLUDE_DIR)/catalog/pg_attribute.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@ docs/$(basename $(notdir $@)).rst
pglast/enums/pg_class.py: $(PG_INCLUDE_DIR)/catalog/pg_class.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@ docs/$(basename $(notdir $@)).rst
pglast/enums/pg_trigger.py: $(PG_INCLUDE_DIR)/catalog/pg_trigger.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@ docs/$(basename $(notdir $@)).rst
pglast/enums/xml.py: $(PG_INCLUDE_DIR)/utils/xml.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@ docs/$(basename $(notdir $@)).rst

help::
	@printf "keywords\n\textract Python keyword sets from PG sources\n"

PY_KEYWORDS := pglast/keywords.py

.PHONY: keywords
keywords: $(PY_KEYWORDS)

$(PY_KEYWORDS): tools/extract_keywords.py libpg_query/libpg_query.a
$(PY_KEYWORDS): $(PG_INCLUDE_DIR)/parser/kwlist.h
	$(PYTHON) tools/extract_keywords.py $(PG_INCLUDE_DIR)/parser/kwlist.h $@

pglast/ast.pyx: tools/extract_ast.py libpg_query/srcdata/struct_defs.json
pglast/ast.pyx: $(PY_ENUMS)
	$(PYTHON) tools/extract_ast.py pglast/ docs/ast.rst

help::
	@printf "printers-doc\n\tupdate printers documentation\n"

PG_NODES := $(PG_INCLUDE_DIR)/nodes/nodes.h $(PG_INCLUDE_DIR)/nodes/parsenodes.h \
	    $(PG_INCLUDE_DIR)/nodes/primnodes.h $(PG_INCLUDE_DIR)/nodes/value.h

.PHONY: printers-doc
printers-doc: docs/ddl.rst docs/dml.rst

docs/ddl.rst docs/dml.rst: $(PG_NODES) tools/extract_printers_doc.py libpg_query/libpg_query.a
docs/%.rst: pglast/printers/%.py
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
COVERAGE = $(VENVDIR)/bin/coverage

.PHONY: check
check: build
	$(PYTEST) tests/
	$(MAKE) -C docs SPHINXBUILD=$(SPHINXBUILD) doctest
	$(COVERAGE) json -o $(TOPDIR)/coverage.json

include Makefile.virtualenv
include Makefile.release
