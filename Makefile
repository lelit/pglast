# -*- coding: utf-8 -*-
# :Project:   pglast — Development Makefile
# :Created:   gio 03 ago 2017 14:52:45 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025, 2026 Lele Gaifax
#

export TOPDIR := $(CURDIR)
ifeq ($(VIRTUAL_ENV),)
export VENVDIR := $(TOPDIR)/env
else
export VENVDIR := $(VIRTUAL_ENV)
endif
export PYTHON := $(VENVDIR)/bin/python
export CYTHON := $(VENVDIR)/bin/cython
export SHELL := bash
export SYS_PYTHON := $(shell command -v python3)

GENERATED_DOCS := $(shell git grep -l "DO NOT EDIT: " docs/)
GENERATED_SRCS := $(shell git grep -l "DO NOT EDIT: " pglast/)

all: virtualenv libpg_query/Makefile help

libpg_query/Makefile:
	git submodule update --init

help::
	@printf "\nBuild targets\n"
	@printf   "=============\n\n"

help::
	@printf "build\n\tbuild the module and update derivated sources\n"

.PHONY: build
build: virtualenv
build: $(VENVDIR)/libpg_query.hash
build: $(VENVDIR)/extension.timestamp
build: enums
build: keywords
build: type-stubs
build: printers-doc

FORCE:
$(VENVDIR)/libpg_query.hash: FORCE
	@git -C libpg_query rev-parse HEAD > $@.new
	@if test -r $@ && cmp --quiet $@ $@.new; \
	 then rm $@.new; \
	 else mv $@.new $@; echo "Updated $@"; \
	fi

$(VENVDIR)/extension.timestamp: setup.py
$(VENVDIR)/extension.timestamp: libpg_query/libpg_query.a
$(VENVDIR)/extension.timestamp: pglast/parser.c
	$(PYTHON) setup.py build_ext --inplace --force
	@touch $@

libpg_query/libpg_query.a: libpg_query/Makefile
libpg_query/libpg_query.a: libpg_query/src/*.c libpg_query/src/*.h
	$(MAKE) -C libpg_query build

pglast/parser.c: pglast/ast.pyx
pglast/parser.c: pglast/parser.pyx
pglast/parser.c: pglast/structs.pxd
	$(CYTHON) pglast/parser.pyx
	@: Ensure postgres.h is included as early as possible, to support win32
	printf "%s\n" '/^#include "postgres.h"/m1' 'wq' | ed -s pglast/parser.c

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

PY_ENUMS := $(filter-out pglast/enums/__init__.py,$(shell ls pglast/enums/*.py))
PY_ENUM_STUBS := $(PY_ENUMS:.py=.pyi)
PG_INCLUDE_DIR := libpg_query/src/postgres/include

.PHONY: enums
enums: $(PY_ENUMS)

$(PY_ENUMS) $(PY_ENUM_STUBS): tools/extract_enums.py
$(PY_ENUMS) $(PY_ENUM_STUBS): libpg_query/libpg_query.a
$(PY_ENUMS) $(PY_ENUM_STUBS): $(VENVDIR)/libpg_query.hash

define extract_enums
$(PYTHON) tools/extract_enums.py -I $(PG_INCLUDE_DIR) $< $(basename $@).py docs/$(basename $(notdir $@)).rst
endef

pglast/enums/%.py pglast/enums/%.pyi: $(PG_INCLUDE_DIR)/nodes/%.h
	$(extract_enums)

pglast/enums/lockdefs.py pglast/enums/lockdefs.pyi: $(PG_INCLUDE_DIR)/storage/lockdefs.h
	$(extract_enums)

pglast/enums/pg_am.py pglast/enums/pg_am.pyi: $(PG_INCLUDE_DIR)/catalog/pg_am.h
	$(extract_enums)

pglast/enums/pg_attribute.py pglast/enums/pg_attribute.pyi: $(PG_INCLUDE_DIR)/catalog/pg_attribute.h
	$(extract_enums)

pglast/enums/pg_class.py pglast/enums/pg_class.pyi: $(PG_INCLUDE_DIR)/catalog/pg_class.h
	$(extract_enums)

pglast/enums/pg_trigger.py pglast/enums/pg_trigger.pyi: $(PG_INCLUDE_DIR)/catalog/pg_trigger.h
	$(extract_enums)

pglast/enums/xml.py pglast/enums/xml.pyi: $(PG_INCLUDE_DIR)/utils/xml.h
	$(extract_enums)

pglast/enums/cmptype.py pglast/enums/cmptype.pyi: $(PG_INCLUDE_DIR)/access/cmptype.h
	$(extract_enums)

help::
	@printf "keywords\n\textract Python keyword sets from PG sources\n"

.PHONY: keywords
keywords: pglast/keywords.py

pglast/keywords.py pglast/keywords.pyi: tools/extract_keywords.py
pglast/keywords.py pglast/keywords.pyi: libpg_query/libpg_query.a
pglast/keywords.py pglast/keywords.pyi: $(VENVDIR)/libpg_query.hash
pglast/keywords.py pglast/keywords.pyi: $(PG_INCLUDE_DIR)/parser/kwlist.h
	$(PYTHON) tools/extract_keywords.py $(PG_INCLUDE_DIR)/parser/kwlist.h pglast/keywords.py

pglast/ast.pyx pglast/ast.pyi: tools/extract_ast.py libpg_query/srcdata/struct_defs.json
pglast/ast.pyx pglast/ast.pyi: $(PY_ENUMS)
	$(PYTHON) tools/extract_ast.py pglast/ docs/ast.rst

help::
	@printf "type-stubs\n\tgenerate Python type stubs for generated modules\n"

PRINTER_STUBS := pglast/printers/ddl.pyi pglast/printers/dml.pyi pglast/printers/sfuncs.pyi

.PHONY: type-stubs
type-stubs: enums
type-stubs: keywords
type-stubs: pglast/ast.pyi
type-stubs: $(PY_ENUM_STUBS)
type-stubs: pglast/enums/__init__.pyi
type-stubs: pglast/keywords.pyi
type-stubs: $(PRINTER_STUBS)

pglast/printers/%.pyi: pglast/printers/%.py tools/extract_printer_stubs.py
	$(PYTHON) tools/extract_printer_stubs.py $< $@

pglast/enums/__init__.pyi: pglast/enums/__init__.py Makefile
	{ \
	  printf "%s\n" "# -*- coding: utf-8 -*-"; \
	  printf "%s\n" "# :Project:   pglast — DO NOT EDIT: type stubs automatically extracted from __init__.py"; \
	  printf "%s\n" "# :Author:    Lele Gaifax <lele@metapensiero.it>"; \
	  printf "%s\n" "# :License:   GNU General Public License version 3 or later"; \
	  printf "%s\n" "#"; \
	  printf "\n"; \
	  sed -n '/^from \./p' $<; \
	} > $@

help::
	@printf "printers-doc\n\tupdate printers documentation\n"

PG_NODES := $(PG_INCLUDE_DIR)/nodes/nodes.h $(PG_INCLUDE_DIR)/nodes/parsenodes.h \
	    $(PG_INCLUDE_DIR)/nodes/primnodes.h $(PG_INCLUDE_DIR)/nodes/value.h

.PHONY: printers-doc
printers-doc: $(GENERATED_DOCS)

$(GENERATED_DOCS): $(PG_NODES)
$(GENERATED_DOCS): tools/extract_printers_doc.py
$(GENERATED_DOCS): libpg_query/libpg_query.a
$(GENERATED_DOCS): $(VENVDIR)/libpg_query.hash
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
	$(COVERAGE) run -m pytest tests/
	$(MAKE) -C docs SPHINXBUILD=$(SPHINXBUILD) doctest
	$(COVERAGE) json -o $(TOPDIR)/coverage.json

include Makefile.virtualenv
include Makefile.release
