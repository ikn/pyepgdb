project_name := pyepgdb

INSTALL_PROGRAM := install
INSTALL_DATA := install -m 644

prefix := /usr/local
datarootdir := $(prefix)/share
exec_prefix := $(prefix)
datadir := $(datarootdir)/$(project_name)
bindir := $(exec_prefix)/bin
docdir := $(datarootdir)/doc/$(project_name)

.PHONY: all clean install uninstall doc test coverage

all:
	python3 setup.py bdist

clean:
	find "$(project_name)" -type d -name '__pycache__' | xargs $(RM) -r
	$(RM) -r build/ dist/ "$(project_name).egg-info/"
	$(RM) -r doc/_build/
	$(RM) -r .coverage htmlcov/

install:
	python3 setup.py install --root="$(or $(DESTDIR),/)" --prefix="$(prefix)"
	mkdir -p "$(DESTDIR)$(docdir)/"
	$(INSTALL_DATA) README.md "$(DESTDIR)$(docdir)/"

uninstall:
	./uninstall "$(DESTDIR)" "$(prefix)"
	$(RM) -r "$(DESTDIR)$(docdir)/"

doc:
	mkdir -p doc/_build/
	cp -t doc/_build/ doc/conf.py doc/*.rst doc/Makefile
	sphinx-apidoc --module-first --separate -o doc/_build/ \
	    -- "$(project_name)"
	$(RM) doc/_build/modules.rst
	cd doc/_build/ && make html

test:
	PYTHONPATH=. python3 test.py -v

coverage:
	PYTHONPATH=. coverage3 run test.py
	coverage3 report
	coverage3 html
