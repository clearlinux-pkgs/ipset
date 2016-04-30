#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipset
Version  : 6.24
Release  : 5
URL      : http://ipset.netfilter.org/ipset-6.24.tar.bz2
Source0  : http://ipset.netfilter.org/ipset-6.24.tar.bz2
Summary  : Userspace library for the ipset extensions and the kernel interface
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: ipset-bin
Requires: ipset-lib
Requires: ipset-doc
BuildRequires : grep
BuildRequires : pkgconfig(libmnl)

%description
This is the ipset source tree. Follow the next steps to install ipset.
If you upgrade from an earlier 5.x release, please read the UPGRADE
instructions too.

%package bin
Summary: bin components for the ipset package.
Group: Binaries

%description bin
bin components for the ipset package.


%package dev
Summary: dev components for the ipset package.
Group: Development
Requires: ipset-lib
Requires: ipset-bin

%description dev
dev components for the ipset package.


%package doc
Summary: doc components for the ipset package.
Group: Documentation

%description doc
doc components for the ipset package.


%package lib
Summary: lib components for the ipset package.
Group: Libraries

%description lib
lib components for the ipset package.


%prep
%setup -q -n ipset-6.24

%build
%configure --disable-static --with-kmod=no
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipset

%files dev
%defattr(-,root,root,-)
/usr/include/libipset/data.h
/usr/include/libipset/errcode.h
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
/usr/include/libipset/ui.h
/usr/include/libipset/utils.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
