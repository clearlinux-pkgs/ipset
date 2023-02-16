#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipset
Version  : 7.17
Release  : 35
URL      : https://www.netfilter.org/pub/ipset/ipset-7.17.tar.bz2
Source0  : https://www.netfilter.org/pub/ipset/ipset-7.17.tar.bz2
Source1  : ipset.service
Summary  : Userspace library for the ipset extensions and the kernel interface
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: ipset-bin = %{version}-%{release}
Requires: ipset-lib = %{version}-%{release}
Requires: ipset-license = %{version}-%{release}
Requires: ipset-man = %{version}-%{release}
Requires: ipset-services = %{version}-%{release}
BuildRequires : grep
BuildRequires : pkgconfig(libmnl)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is the ipset source tree. Follow the next steps to install ipset.
If you upgrade from an earlier 5.x release, please read the UPGRADE
instructions too.

%package bin
Summary: bin components for the ipset package.
Group: Binaries
Requires: ipset-license = %{version}-%{release}
Requires: ipset-services = %{version}-%{release}

%description bin
bin components for the ipset package.


%package dev
Summary: dev components for the ipset package.
Group: Development
Requires: ipset-lib = %{version}-%{release}
Requires: ipset-bin = %{version}-%{release}
Provides: ipset-devel = %{version}-%{release}
Requires: ipset = %{version}-%{release}

%description dev
dev components for the ipset package.


%package lib
Summary: lib components for the ipset package.
Group: Libraries
Requires: ipset-license = %{version}-%{release}

%description lib
lib components for the ipset package.


%package license
Summary: license components for the ipset package.
Group: Default

%description license
license components for the ipset package.


%package man
Summary: man components for the ipset package.
Group: Default

%description man
man components for the ipset package.


%package services
Summary: services components for the ipset package.
Group: Systemd services

%description services
services components for the ipset package.


%prep
%setup -q -n ipset-7.17
cd %{_builddir}/ipset-7.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676575894
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --with-kmod=no \
--enable-bashcompl
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1676575894
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipset
cp %{_builddir}/ipset-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ipset/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/ipset-%{version}/libltdl/COPYING.LIB %{buildroot}/usr/share/package-licenses/ipset/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/ipset.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipset
/usr/bin/ipset-translate

%files dev
%defattr(-,root,root,-)
/usr/include/libipset/args.h
/usr/include/libipset/data.h
/usr/include/libipset/errcode.h
/usr/include/libipset/ipset.h
/usr/include/libipset/linux_ip_set.h
/usr/include/libipset/linux_ip_set_bitmap.h
/usr/include/libipset/linux_ip_set_hash.h
/usr/include/libipset/linux_ip_set_list.h
/usr/include/libipset/mnl.h
/usr/include/libipset/nf_inet_addr.h
/usr/include/libipset/nfproto.h
/usr/include/libipset/parse.h
/usr/include/libipset/pfxlen.h
/usr/include/libipset/print.h
/usr/include/libipset/session.h
/usr/include/libipset/transport.h
/usr/include/libipset/types.h
/usr/include/libipset/utils.h
/usr/include/libipset/xlate.h
/usr/lib64/libipset.so
/usr/lib64/pkgconfig/libipset.pc
/usr/share/man/man3/libipset.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libipset.so.13
/usr/lib64/libipset.so.13.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipset/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/ipset/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/ipset-translate.8
/usr/share/man/man8/ipset.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ipset.service
