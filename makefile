project_name := pyepgdb

INSTALL_PROGRAM := install
INSTALL_DATA := install -m 644

prefix := /usr/local
datarootdir := $(prefix)/share
exec_prefix := $(prefix)
datadir := $(datarootdir)/$(project_name)
bindir := $(exec_prefix)/bin
docdir := $(datarootdir)/doc/$(project_name)

.PHONY: all clean install uninstall doc

all:
	python3 setup.py bdist

clean:
	find "$(project_name)" -type d -name '__pycache__' | xargs $(RM) -r
	$(RM) -r build/ dist/ "$(project_name).egg-info/"
	$(RM) -r doc/_build/

install:
	python3 setup.py install --root="$(DESTDIR)" --prefix="$(prefix)"
	mkdir -p "$(DESTDIR)$(docdir)/"
	$(INSTALL_DATA) README.md "$(DESTDIR)$(docdir)/"

uninstall:
	./uninstall "$(DESTDIR)" "$(prefix)"
	$(RM) -r "$(DESTDIR)$(docdir)/"

doc:
	mkdir -p doc/_build/
	cp -t doc/_build/ doc/conf.py doc/index.rst doc/Makefile
	sphinx-apidoc --module-first --separate -o doc/_build/ -- "$(project_name)"
	$(RM) doc/_build/modules.rst
	cd doc/_build/ && make html
