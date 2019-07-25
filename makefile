project_name := pyepgdb

INSTALL_PROGRAM := install
INSTALL_DATA := install -m 644

prefix := /usr/local
datarootdir := $(prefix)/share
exec_prefix := $(prefix)
datadir := $(datarootdir)/$(project_name)
bindir := $(exec_prefix)/bin
docdir := $(datarootdir)/doc/$(project_name)

.PHONY: all clean distclean install uninstall

all:
	python3 setup.py bdist

clean:
	$(RM) -r build/ dist/ "$(project_name).egg-info/"

distclean: clean
	find $(project_name) -type d -name '__pycache__' | xargs $(RM) -r

install:
	@ # package
	python3 setup.py install --root="$(DESTDIR)" --prefix="$(prefix)"
	@ # readme
	mkdir -p "$(DESTDIR)$(docdir)/"
	$(INSTALL_DATA) README.md "$(DESTDIR)$(docdir)/"

uninstall:
	@ # package
	./uninstall "$(DESTDIR)" "$(prefix)"
	@ # readme
	$(RM) -r "$(DESTDIR)$(docdir)/"
