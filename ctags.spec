#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ctags
Version  : 6.0.20230205.0
Release  : 100
URL      : https://github.com/universal-ctags/ctags/archive/p6.0.20230205.0/ctags-6.0.20230205.0.tar.gz
Source0  : https://github.com/universal-ctags/ctags/archive/p6.0.20230205.0/ctags-6.0.20230205.0.tar.gz
Summary  : Exuberant Ctags - a multi-language source code indexing tool
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 MIT
Requires: ctags-bin = %{version}-%{release}
Requires: ctags-filemap = %{version}-%{release}
Requires: ctags-license = %{version}-%{release}
Requires: ctags-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-locale
BuildRequires : pkgconfig(jansson)
BuildRequires : pkgconfig(libpcre2-8)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : pypi-docutils
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: ctags-filemap = %{version}-%{release}

%description bin
bin components for the ctags package.


%package filemap
Summary: filemap components for the ctags package.
Group: Default

%description filemap
filemap components for the ctags package.


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
%setup -q -n ctags-p6.0.20230205.0
cd %{_builddir}/ctags-p6.0.20230205.0
pushd ..
cp -a ctags-p6.0.20230205.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675632600
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%autogen --disable-static --enable-etags
make  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%autogen --disable-static --enable-etags
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1675632600
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ctags
cp %{_builddir}/ctags-p%{version}/COPYING %{buildroot}/usr/share/package-licenses/ctags/74a8a6531a42e124df07ab5599aad63870fa0bd4 || :
cp %{_builddir}/ctags-p%{version}/Units/parser-ldscript.r/ld-hello.d/LICENSE %{buildroot}/usr/share/package-licenses/ctags/3127907a7623734f830e8c69ccee03b693bf993e || :
cp %{_builddir}/ctags-p%{version}/misc/packcc/LICENSE %{buildroot}/usr/share/package-licenses/ctags/66933c0a887d692b09075639ec0e118d4e8bc045 || :
cp %{_builddir}/ctags-p%{version}/win32/license/LICENCE.pcre2 %{buildroot}/usr/share/package-licenses/ctags/cc7132d685cfac1cac53709962b52590e160450f || :
cp %{_builddir}/ctags-p%{version}/win32/license/LICENSE.janssen %{buildroot}/usr/share/package-licenses/ctags/26a708b97cbb50e3fce8078dd21d65c8fdd5a605 || :
cp %{_builddir}/ctags-p%{version}/win32/license/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/ctags/c01c212bdf3925189f673e2081b44094023860ea || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ctags
/usr/bin/etags
/usr/bin/optscript
/usr/bin/readtags
/usr/share/clear/optimized-elf/bin*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-ctags

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ctags/26a708b97cbb50e3fce8078dd21d65c8fdd5a605
/usr/share/package-licenses/ctags/3127907a7623734f830e8c69ccee03b693bf993e
/usr/share/package-licenses/ctags/66933c0a887d692b09075639ec0e118d4e8bc045
/usr/share/package-licenses/ctags/74a8a6531a42e124df07ab5599aad63870fa0bd4
/usr/share/package-licenses/ctags/c01c212bdf3925189f673e2081b44094023860ea
/usr/share/package-licenses/ctags/cc7132d685cfac1cac53709962b52590e160450f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ctags.1
/usr/share/man/man1/readtags.1
/usr/share/man/man5/ctags-json-output.5
/usr/share/man/man5/tags.5
/usr/share/man/man7/ctags-client-tools.7
/usr/share/man/man7/ctags-faq.7
/usr/share/man/man7/ctags-incompatibilities.7
/usr/share/man/man7/ctags-lang-asm.7
/usr/share/man/man7/ctags-lang-elm.7
/usr/share/man/man7/ctags-lang-gdscript.7
/usr/share/man/man7/ctags-lang-iPythonCell.7
/usr/share/man/man7/ctags-lang-inko.7
/usr/share/man/man7/ctags-lang-javascript.7
/usr/share/man/man7/ctags-lang-julia.7
/usr/share/man/man7/ctags-lang-kconfig.7
/usr/share/man/man7/ctags-lang-python.7
/usr/share/man/man7/ctags-lang-r.7
/usr/share/man/man7/ctags-lang-rmarkdown.7
/usr/share/man/man7/ctags-lang-sql.7
/usr/share/man/man7/ctags-lang-systemtap.7
/usr/share/man/man7/ctags-lang-tcl.7
/usr/share/man/man7/ctags-lang-verilog.7
/usr/share/man/man7/ctags-optlib.7
