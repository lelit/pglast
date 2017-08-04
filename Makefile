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
	@echo
	@echo "Build targets"
	@echo "============="
	@echo

help::
	@echo "build"
	@echo "    build the module"

.PHONY: build
build: enums libpg_query/libpg_query.a pg_query/parser.c

libpg_query/libpg_query.a:
	$(MAKE) -C libpg_query build

pg_query/parser.c: pg_query/parser.pyx
	$(PYTHON) setup.py build_ext --inplace

help::
	@echo "enums"
	@echo "    extract Python enums from PG sources"

PY_ENUMS_DIR := pg_query/enums
PG_INCLUDE_DIR := libpg_query/src/postgres/include
.PHONY: enums
enums: $(PY_ENUMS_DIR)/nodes.py $(PY_ENUMS_DIR)/primnodes.py $(PY_ENUMS_DIR)/parsenodes.py

$(PY_ENUMS_DIR)/nodes.py: $(PG_INCLUDE_DIR)/nodes/nodes.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@

$(PY_ENUMS_DIR)/primnodes.py: $(PG_INCLUDE_DIR)/nodes/primnodes.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@

$(PY_ENUMS_DIR)/parsenodes.py: $(PG_INCLUDE_DIR)/nodes/parsenodes.h
	$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $@

help::
	@echo "check"
	@echo "    run the test suite"

.PHONY: check
check: build
	pytest tests/

include Makefile.virtualenv
include Makefile.release
