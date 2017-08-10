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
	@printf "clean\n\tremove rebuildable stuff\n"

.PHONY: clean
clean:
	$(MAKE) -C libpg_query clean
	rm -f pg_query/*.so

help::
	@printf "enums\n\textract Python enums from PG sources\n"

PY_ENUMS_DIR := pg_query/enums
PY_ENUMS := $(PY_ENUMS_DIR)/lockoptions.py $(PY_ENUMS_DIR)/nodes.py \
	    $(PY_ENUMS_DIR)/parsenodes.py $(PY_ENUMS_DIR)/primnodes.py
PG_INCLUDE_DIR := libpg_query/src/postgres/include

.PHONY: enums
enums: $(PY_ENUMS)

$(PY_ENUMS_DIR)/%.py: $(PG_INCLUDE_DIR)/nodes/%.h tools/extract_enums.py
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@

help::
	@printf "keywords\n\textract Python keyword sets from PG sources\n"

PY_KEYWORDS_DIR := pg_query
PY_KEYWORDS := $(PY_KEYWORDS_DIR)/keywords.py

.PHONY: keywords
keywords: $(PY_KEYWORDS)

$(PY_KEYWORDS): $(PG_INCLUDE_DIR)/parser/kwlist.h tools/extract_keywords.py
	$(PYTHON) tools/extract_keywords.py $< $@

help::
	@printf "check\n\trun the test suite\n"

.PHONY: check
check: build
	pytest tests/
	$(MAKE) -C docs doctest

include Makefile.virtualenv
include Makefile.release
