#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ctags
Version  : 5.8
Release  : 10
URL      : https://sourceforge.net/projects/ctags/files/ctags/5.8/ctags-5.8.tar.gz
Source0  : https://sourceforge.net/projects/ctags/files/ctags/5.8/ctags-5.8.tar.gz
Summary  : Exuberant Ctags - a multi-language source code indexing tool
Group    : Development/Tools
License  : GPL-2.0
Requires: ctags-bin = %{version}-%{release}
Requires: ctags-license = %{version}-%{release}
Requires: ctags-man = %{version}-%{release}
Patch1: ctags-5.7-destdir.patch
Patch2: cve-2014-7204.patch
Patch3: build.patch

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
Requires: ctags-license = %{version}-%{release}
Requires: ctags-man = %{version}-%{release}

%description bin
bin components for the ctags package.


%package license
Summary: license components for the ctags package.
Group: Default

%description license
license components for the ctags package.


%package man
Summary: man components for the ctags package.
Group: Default

%description man
man components for the ctags package.


%prep
%setup -q -n ctags-5.8
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539760731
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1539760731
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ctags
cp COPYING %{buildroot}/usr/share/package-licenses/ctags/COPYING
%make_install
## install_append content
pushd %{buildroot}%{_bindir}
ln -s ctags etags
popd
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ctags
/usr/bin/etags

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ctags/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ctags.1
