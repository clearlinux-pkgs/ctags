#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ctags
Version  : 5.8
Release  : 2
URL      : http://downloads.sourceforge.net/ctags/ctags-5.8.tar.gz
Source0  : http://downloads.sourceforge.net/ctags/ctags-5.8.tar.gz
Summary  : Exuberant Ctags - a multi-language source code indexing tool
Group    : Development/Tools
License  : GPL-2.0
Requires: ctags-bin
Requires: ctags-doc
Patch1: ctags-5.7-destdir.patch
Patch2: cve-2014-7204.patch

%description
Exuberant Ctags generates an index (or tag) file of language objects
found in source files for many popular programming languages. This index
makes it easy for text editors and other tools to locate the indexed
items. Exuberant Ctags improves on traditional ctags because of its
multilanguage support, its ability for the user to define new languages
searched by regular expressions, and its ability to generate emacs-style
TAGS files.

Install ctags if you are going to use your system for programming.

%package bin
Summary: bin components for the ctags package.
Group: Binaries

%description bin
bin components for the ctags package.


%package doc
Summary: doc components for the ctags package.
Group: Documentation

%description doc
doc components for the ctags package.


%prep
%setup -q -n ctags-5.8
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
pushd %{buildroot}%{_bindir}
ln -s ctags etags
popd
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ctags
/usr/bin/etags

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
