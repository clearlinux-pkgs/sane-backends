#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sane-backends
Version  : 1.0.30
Release  : 14
URL      : https://gitlab.com/sane-project/backends/uploads/c3dd60c9e054b5dee1e7b01a7edc98b0/sane-backends-1.0.30.tar.gz
Source0  : https://gitlab.com/sane-project/backends/uploads/c3dd60c9e054b5dee1e7b01a7edc98b0/sane-backends-1.0.30.tar.gz
Summary  : Backends for SANE, the universal scanner interface
Group    : Development/Tools
License  : GPL-2.0
Requires: sane-backends-bin = %{version}-%{release}
Requires: sane-backends-config = %{version}-%{release}
Requires: sane-backends-data = %{version}-%{release}
Requires: sane-backends-lib = %{version}-%{release}
Requires: sane-backends-license = %{version}-%{release}
Requires: sane-backends-locales = %{version}-%{release}
Requires: sane-backends-man = %{version}-%{release}
Requires: imagescan
BuildRequires : ghostscript
BuildRequires : imagescan
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(libv4l1)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : systemd-dev
BuildRequires : tiff-dev
Patch1: 0001-Add-stateless-support.patch
Patch2: 0002-Search-for-backends-in-usr-local-lib64-sane.patch

%description
How to configure, build, and install SANE.
Introduction:
=============
SANE stands for Scanner Access Now Easy.
This package contains the SANE libraries (this means backends and
network scanning parts) and the command line frontend scanimage.
You always find the most recent version of SANE on:

%package bin
Summary: bin components for the sane-backends package.
Group: Binaries
Requires: sane-backends-data = %{version}-%{release}
Requires: sane-backends-config = %{version}-%{release}
Requires: sane-backends-license = %{version}-%{release}

%description bin
bin components for the sane-backends package.


%package config
Summary: config components for the sane-backends package.
Group: Default

%description config
config components for the sane-backends package.


%package data
Summary: data components for the sane-backends package.
Group: Data

%description data
data components for the sane-backends package.


%package dev
Summary: dev components for the sane-backends package.
Group: Development
Requires: sane-backends-lib = %{version}-%{release}
Requires: sane-backends-bin = %{version}-%{release}
Requires: sane-backends-data = %{version}-%{release}
Provides: sane-backends-devel = %{version}-%{release}
Requires: sane-backends = %{version}-%{release}

%description dev
dev components for the sane-backends package.


%package doc
Summary: doc components for the sane-backends package.
Group: Documentation
Requires: sane-backends-man = %{version}-%{release}

%description doc
doc components for the sane-backends package.


%package lib
Summary: lib components for the sane-backends package.
Group: Libraries
Requires: sane-backends-data = %{version}-%{release}
Requires: sane-backends-license = %{version}-%{release}

%description lib
lib components for the sane-backends package.


%package license
Summary: license components for the sane-backends package.
Group: Default

%description license
license components for the sane-backends package.


%package locales
Summary: locales components for the sane-backends package.
Group: Default

%description locales
locales components for the sane-backends package.


%package man
Summary: man components for the sane-backends package.
Group: Default

%description man
man components for the sane-backends package.


%prep
%setup -q -n sane-backends-1.0.30
cd %{_builddir}/sane-backends-1.0.30
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589816541
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static --disable-avahi
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1589816541
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sane-backends
cp %{_builddir}/sane-backends-1.0.30/COPYING %{buildroot}/usr/share/package-licenses/sane-backends/74a8a6531a42e124df07ab5599aad63870fa0bd4
%make_install
%find_lang sane-backends
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/sane
mv %{buildroot}/etc/sane.d/* %{buildroot}/usr/share/defaults/sane/
mkdir -p %{buildroot}/usr/lib/udev/rules.d
install -m0644 tools/udev/libsane.rules %{buildroot}/usr/lib/udev/rules.d/60-libsane.rules
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gamma4scanimage
/usr/bin/sane-config
/usr/bin/sane-find-scanner
/usr/bin/saned
/usr/bin/scanimage
/usr/bin/umax_pp

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/60-libsane.rules

%files data
%defattr(-,root,root,-)
/usr/share/defaults/sane/abaton.conf
/usr/share/defaults/sane/agfafocus.conf
/usr/share/defaults/sane/apple.conf
/usr/share/defaults/sane/artec.conf
/usr/share/defaults/sane/artec_eplus48u.conf
/usr/share/defaults/sane/avision.conf
/usr/share/defaults/sane/bh.conf
/usr/share/defaults/sane/canon.conf
/usr/share/defaults/sane/canon630u.conf
/usr/share/defaults/sane/canon_dr.conf
/usr/share/defaults/sane/cardscan.conf
/usr/share/defaults/sane/coolscan.conf
/usr/share/defaults/sane/coolscan2.conf
/usr/share/defaults/sane/coolscan3.conf
/usr/share/defaults/sane/dc210.conf
/usr/share/defaults/sane/dc240.conf
/usr/share/defaults/sane/dc25.conf
/usr/share/defaults/sane/dell1600n_net.conf
/usr/share/defaults/sane/dll.conf
/usr/share/defaults/sane/dmc.conf
/usr/share/defaults/sane/epjitsu.conf
/usr/share/defaults/sane/epson.conf
/usr/share/defaults/sane/epson2.conf
/usr/share/defaults/sane/epsonds.conf
/usr/share/defaults/sane/fujitsu.conf
/usr/share/defaults/sane/genesys.conf
/usr/share/defaults/sane/gt68xx.conf
/usr/share/defaults/sane/hp.conf
/usr/share/defaults/sane/hp3900.conf
/usr/share/defaults/sane/hp4200.conf
/usr/share/defaults/sane/hp5400.conf
/usr/share/defaults/sane/hs2p.conf
/usr/share/defaults/sane/ibm.conf
/usr/share/defaults/sane/kodak.conf
/usr/share/defaults/sane/kodakaio.conf
/usr/share/defaults/sane/kvs1025.conf
/usr/share/defaults/sane/leo.conf
/usr/share/defaults/sane/lexmark.conf
/usr/share/defaults/sane/ma1509.conf
/usr/share/defaults/sane/magicolor.conf
/usr/share/defaults/sane/matsushita.conf
/usr/share/defaults/sane/microtek.conf
/usr/share/defaults/sane/microtek2.conf
/usr/share/defaults/sane/mustek.conf
/usr/share/defaults/sane/mustek_usb.conf
/usr/share/defaults/sane/nec.conf
/usr/share/defaults/sane/net.conf
/usr/share/defaults/sane/p5.conf
/usr/share/defaults/sane/pie.conf
/usr/share/defaults/sane/pieusb.conf
/usr/share/defaults/sane/pixma.conf
/usr/share/defaults/sane/plustek.conf
/usr/share/defaults/sane/plustek_pp.conf
/usr/share/defaults/sane/qcam.conf
/usr/share/defaults/sane/ricoh.conf
/usr/share/defaults/sane/rts8891.conf
/usr/share/defaults/sane/s9036.conf
/usr/share/defaults/sane/saned.conf
/usr/share/defaults/sane/sceptre.conf
/usr/share/defaults/sane/sharp.conf
/usr/share/defaults/sane/sm3840.conf
/usr/share/defaults/sane/snapscan.conf
/usr/share/defaults/sane/sp15c.conf
/usr/share/defaults/sane/st400.conf
/usr/share/defaults/sane/stv680.conf
/usr/share/defaults/sane/tamarack.conf
/usr/share/defaults/sane/teco1.conf
/usr/share/defaults/sane/teco2.conf
/usr/share/defaults/sane/teco3.conf
/usr/share/defaults/sane/test.conf
/usr/share/defaults/sane/u12.conf
/usr/share/defaults/sane/umax.conf
/usr/share/defaults/sane/umax1220u.conf
/usr/share/defaults/sane/umax_pp.conf
/usr/share/defaults/sane/v4l.conf
/usr/share/defaults/sane/xerox_mfp.conf

%files dev
%defattr(-,root,root,-)
/usr/include/sane/sane.h
/usr/include/sane/saneopts.h
/usr/lib64/libsane.so
/usr/lib64/pkgconfig/sane-backends.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/sane\-backends/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsane.so.1
/usr/lib64/libsane.so.1.0.30
/usr/lib64/sane/libsane-abaton.so
/usr/lib64/sane/libsane-abaton.so.1
/usr/lib64/sane/libsane-abaton.so.1.0.30
/usr/lib64/sane/libsane-agfafocus.so
/usr/lib64/sane/libsane-agfafocus.so.1
/usr/lib64/sane/libsane-agfafocus.so.1.0.30
/usr/lib64/sane/libsane-apple.so
/usr/lib64/sane/libsane-apple.so.1
/usr/lib64/sane/libsane-apple.so.1.0.30
/usr/lib64/sane/libsane-artec.so
/usr/lib64/sane/libsane-artec.so.1
/usr/lib64/sane/libsane-artec.so.1.0.30
/usr/lib64/sane/libsane-artec_eplus48u.so
/usr/lib64/sane/libsane-artec_eplus48u.so.1
/usr/lib64/sane/libsane-artec_eplus48u.so.1.0.30
/usr/lib64/sane/libsane-as6e.so
/usr/lib64/sane/libsane-as6e.so.1
/usr/lib64/sane/libsane-as6e.so.1.0.30
/usr/lib64/sane/libsane-avision.so
/usr/lib64/sane/libsane-avision.so.1
/usr/lib64/sane/libsane-avision.so.1.0.30
/usr/lib64/sane/libsane-bh.so
/usr/lib64/sane/libsane-bh.so.1
/usr/lib64/sane/libsane-bh.so.1.0.30
/usr/lib64/sane/libsane-canon.so
/usr/lib64/sane/libsane-canon.so.1
/usr/lib64/sane/libsane-canon.so.1.0.30
/usr/lib64/sane/libsane-canon630u.so
/usr/lib64/sane/libsane-canon630u.so.1
/usr/lib64/sane/libsane-canon630u.so.1.0.30
/usr/lib64/sane/libsane-canon_dr.so
/usr/lib64/sane/libsane-canon_dr.so.1
/usr/lib64/sane/libsane-canon_dr.so.1.0.30
/usr/lib64/sane/libsane-cardscan.so
/usr/lib64/sane/libsane-cardscan.so.1
/usr/lib64/sane/libsane-cardscan.so.1.0.30
/usr/lib64/sane/libsane-coolscan.so
/usr/lib64/sane/libsane-coolscan.so.1
/usr/lib64/sane/libsane-coolscan.so.1.0.30
/usr/lib64/sane/libsane-coolscan2.so
/usr/lib64/sane/libsane-coolscan2.so.1
/usr/lib64/sane/libsane-coolscan2.so.1.0.30
/usr/lib64/sane/libsane-coolscan3.so
/usr/lib64/sane/libsane-coolscan3.so.1
/usr/lib64/sane/libsane-coolscan3.so.1.0.30
/usr/lib64/sane/libsane-dc210.so
/usr/lib64/sane/libsane-dc210.so.1
/usr/lib64/sane/libsane-dc210.so.1.0.30
/usr/lib64/sane/libsane-dc240.so
/usr/lib64/sane/libsane-dc240.so.1
/usr/lib64/sane/libsane-dc240.so.1.0.30
/usr/lib64/sane/libsane-dc25.so
/usr/lib64/sane/libsane-dc25.so.1
/usr/lib64/sane/libsane-dc25.so.1.0.30
/usr/lib64/sane/libsane-dell1600n_net.so
/usr/lib64/sane/libsane-dell1600n_net.so.1
/usr/lib64/sane/libsane-dell1600n_net.so.1.0.30
/usr/lib64/sane/libsane-dll.so
/usr/lib64/sane/libsane-dll.so.1
/usr/lib64/sane/libsane-dll.so.1.0.30
/usr/lib64/sane/libsane-dmc.so
/usr/lib64/sane/libsane-dmc.so.1
/usr/lib64/sane/libsane-dmc.so.1.0.30
/usr/lib64/sane/libsane-epjitsu.so
/usr/lib64/sane/libsane-epjitsu.so.1
/usr/lib64/sane/libsane-epjitsu.so.1.0.30
/usr/lib64/sane/libsane-epson.so
/usr/lib64/sane/libsane-epson.so.1
/usr/lib64/sane/libsane-epson.so.1.0.30
/usr/lib64/sane/libsane-epson2.so
/usr/lib64/sane/libsane-epson2.so.1
/usr/lib64/sane/libsane-epson2.so.1.0.30
/usr/lib64/sane/libsane-epsonds.so
/usr/lib64/sane/libsane-epsonds.so.1
/usr/lib64/sane/libsane-epsonds.so.1.0.30
/usr/lib64/sane/libsane-fujitsu.so
/usr/lib64/sane/libsane-fujitsu.so.1
/usr/lib64/sane/libsane-fujitsu.so.1.0.30
/usr/lib64/sane/libsane-genesys.so
/usr/lib64/sane/libsane-genesys.so.1
/usr/lib64/sane/libsane-genesys.so.1.0.30
/usr/lib64/sane/libsane-gt68xx.so
/usr/lib64/sane/libsane-gt68xx.so.1
/usr/lib64/sane/libsane-gt68xx.so.1.0.30
/usr/lib64/sane/libsane-hp.so
/usr/lib64/sane/libsane-hp.so.1
/usr/lib64/sane/libsane-hp.so.1.0.30
/usr/lib64/sane/libsane-hp3500.so
/usr/lib64/sane/libsane-hp3500.so.1
/usr/lib64/sane/libsane-hp3500.so.1.0.30
/usr/lib64/sane/libsane-hp3900.so
/usr/lib64/sane/libsane-hp3900.so.1
/usr/lib64/sane/libsane-hp3900.so.1.0.30
/usr/lib64/sane/libsane-hp4200.so
/usr/lib64/sane/libsane-hp4200.so.1
/usr/lib64/sane/libsane-hp4200.so.1.0.30
/usr/lib64/sane/libsane-hp5400.so
/usr/lib64/sane/libsane-hp5400.so.1
/usr/lib64/sane/libsane-hp5400.so.1.0.30
/usr/lib64/sane/libsane-hp5590.so
/usr/lib64/sane/libsane-hp5590.so.1
/usr/lib64/sane/libsane-hp5590.so.1.0.30
/usr/lib64/sane/libsane-hpljm1005.so
/usr/lib64/sane/libsane-hpljm1005.so.1
/usr/lib64/sane/libsane-hpljm1005.so.1.0.30
/usr/lib64/sane/libsane-hs2p.so
/usr/lib64/sane/libsane-hs2p.so.1
/usr/lib64/sane/libsane-hs2p.so.1.0.30
/usr/lib64/sane/libsane-ibm.so
/usr/lib64/sane/libsane-ibm.so.1
/usr/lib64/sane/libsane-ibm.so.1.0.30
/usr/lib64/sane/libsane-kodak.so
/usr/lib64/sane/libsane-kodak.so.1
/usr/lib64/sane/libsane-kodak.so.1.0.30
/usr/lib64/sane/libsane-kodakaio.so
/usr/lib64/sane/libsane-kodakaio.so.1
/usr/lib64/sane/libsane-kodakaio.so.1.0.30
/usr/lib64/sane/libsane-kvs1025.so
/usr/lib64/sane/libsane-kvs1025.so.1
/usr/lib64/sane/libsane-kvs1025.so.1.0.30
/usr/lib64/sane/libsane-kvs20xx.so
/usr/lib64/sane/libsane-kvs20xx.so.1
/usr/lib64/sane/libsane-kvs20xx.so.1.0.30
/usr/lib64/sane/libsane-kvs40xx.so
/usr/lib64/sane/libsane-kvs40xx.so.1
/usr/lib64/sane/libsane-kvs40xx.so.1.0.30
/usr/lib64/sane/libsane-leo.so
/usr/lib64/sane/libsane-leo.so.1
/usr/lib64/sane/libsane-leo.so.1.0.30
/usr/lib64/sane/libsane-lexmark.so
/usr/lib64/sane/libsane-lexmark.so.1
/usr/lib64/sane/libsane-lexmark.so.1.0.30
/usr/lib64/sane/libsane-ma1509.so
/usr/lib64/sane/libsane-ma1509.so.1
/usr/lib64/sane/libsane-ma1509.so.1.0.30
/usr/lib64/sane/libsane-magicolor.so
/usr/lib64/sane/libsane-magicolor.so.1
/usr/lib64/sane/libsane-magicolor.so.1.0.30
/usr/lib64/sane/libsane-matsushita.so
/usr/lib64/sane/libsane-matsushita.so.1
/usr/lib64/sane/libsane-matsushita.so.1.0.30
/usr/lib64/sane/libsane-microtek.so
/usr/lib64/sane/libsane-microtek.so.1
/usr/lib64/sane/libsane-microtek.so.1.0.30
/usr/lib64/sane/libsane-microtek2.so
/usr/lib64/sane/libsane-microtek2.so.1
/usr/lib64/sane/libsane-microtek2.so.1.0.30
/usr/lib64/sane/libsane-mustek.so
/usr/lib64/sane/libsane-mustek.so.1
/usr/lib64/sane/libsane-mustek.so.1.0.30
/usr/lib64/sane/libsane-mustek_usb.so
/usr/lib64/sane/libsane-mustek_usb.so.1
/usr/lib64/sane/libsane-mustek_usb.so.1.0.30
/usr/lib64/sane/libsane-mustek_usb2.so
/usr/lib64/sane/libsane-mustek_usb2.so.1
/usr/lib64/sane/libsane-mustek_usb2.so.1.0.30
/usr/lib64/sane/libsane-nec.so
/usr/lib64/sane/libsane-nec.so.1
/usr/lib64/sane/libsane-nec.so.1.0.30
/usr/lib64/sane/libsane-net.so
/usr/lib64/sane/libsane-net.so.1
/usr/lib64/sane/libsane-net.so.1.0.30
/usr/lib64/sane/libsane-niash.so
/usr/lib64/sane/libsane-niash.so.1
/usr/lib64/sane/libsane-niash.so.1.0.30
/usr/lib64/sane/libsane-p5.so
/usr/lib64/sane/libsane-p5.so.1
/usr/lib64/sane/libsane-p5.so.1.0.30
/usr/lib64/sane/libsane-pie.so
/usr/lib64/sane/libsane-pie.so.1
/usr/lib64/sane/libsane-pie.so.1.0.30
/usr/lib64/sane/libsane-pieusb.so
/usr/lib64/sane/libsane-pieusb.so.1
/usr/lib64/sane/libsane-pieusb.so.1.0.30
/usr/lib64/sane/libsane-pixma.so
/usr/lib64/sane/libsane-pixma.so.1
/usr/lib64/sane/libsane-pixma.so.1.0.30
/usr/lib64/sane/libsane-plustek.so
/usr/lib64/sane/libsane-plustek.so.1
/usr/lib64/sane/libsane-plustek.so.1.0.30
/usr/lib64/sane/libsane-plustek_pp.so
/usr/lib64/sane/libsane-plustek_pp.so.1
/usr/lib64/sane/libsane-plustek_pp.so.1.0.30
/usr/lib64/sane/libsane-qcam.so
/usr/lib64/sane/libsane-qcam.so.1
/usr/lib64/sane/libsane-qcam.so.1.0.30
/usr/lib64/sane/libsane-ricoh.so
/usr/lib64/sane/libsane-ricoh.so.1
/usr/lib64/sane/libsane-ricoh.so.1.0.30
/usr/lib64/sane/libsane-ricoh2.so
/usr/lib64/sane/libsane-ricoh2.so.1
/usr/lib64/sane/libsane-ricoh2.so.1.0.30
/usr/lib64/sane/libsane-rts8891.so
/usr/lib64/sane/libsane-rts8891.so.1
/usr/lib64/sane/libsane-rts8891.so.1.0.30
/usr/lib64/sane/libsane-s9036.so
/usr/lib64/sane/libsane-s9036.so.1
/usr/lib64/sane/libsane-s9036.so.1.0.30
/usr/lib64/sane/libsane-sceptre.so
/usr/lib64/sane/libsane-sceptre.so.1
/usr/lib64/sane/libsane-sceptre.so.1.0.30
/usr/lib64/sane/libsane-sharp.so
/usr/lib64/sane/libsane-sharp.so.1
/usr/lib64/sane/libsane-sharp.so.1.0.30
/usr/lib64/sane/libsane-sm3600.so
/usr/lib64/sane/libsane-sm3600.so.1
/usr/lib64/sane/libsane-sm3600.so.1.0.30
/usr/lib64/sane/libsane-sm3840.so
/usr/lib64/sane/libsane-sm3840.so.1
/usr/lib64/sane/libsane-sm3840.so.1.0.30
/usr/lib64/sane/libsane-snapscan.so
/usr/lib64/sane/libsane-snapscan.so.1
/usr/lib64/sane/libsane-snapscan.so.1.0.30
/usr/lib64/sane/libsane-sp15c.so
/usr/lib64/sane/libsane-sp15c.so.1
/usr/lib64/sane/libsane-sp15c.so.1.0.30
/usr/lib64/sane/libsane-st400.so
/usr/lib64/sane/libsane-st400.so.1
/usr/lib64/sane/libsane-st400.so.1.0.30
/usr/lib64/sane/libsane-stv680.so
/usr/lib64/sane/libsane-stv680.so.1
/usr/lib64/sane/libsane-stv680.so.1.0.30
/usr/lib64/sane/libsane-tamarack.so
/usr/lib64/sane/libsane-tamarack.so.1
/usr/lib64/sane/libsane-tamarack.so.1.0.30
/usr/lib64/sane/libsane-teco1.so
/usr/lib64/sane/libsane-teco1.so.1
/usr/lib64/sane/libsane-teco1.so.1.0.30
/usr/lib64/sane/libsane-teco2.so
/usr/lib64/sane/libsane-teco2.so.1
/usr/lib64/sane/libsane-teco2.so.1.0.30
/usr/lib64/sane/libsane-teco3.so
/usr/lib64/sane/libsane-teco3.so.1
/usr/lib64/sane/libsane-teco3.so.1.0.30
/usr/lib64/sane/libsane-test.so
/usr/lib64/sane/libsane-test.so.1
/usr/lib64/sane/libsane-test.so.1.0.30
/usr/lib64/sane/libsane-u12.so
/usr/lib64/sane/libsane-u12.so.1
/usr/lib64/sane/libsane-u12.so.1.0.30
/usr/lib64/sane/libsane-umax.so
/usr/lib64/sane/libsane-umax.so.1
/usr/lib64/sane/libsane-umax.so.1.0.30
/usr/lib64/sane/libsane-umax1220u.so
/usr/lib64/sane/libsane-umax1220u.so.1
/usr/lib64/sane/libsane-umax1220u.so.1.0.30
/usr/lib64/sane/libsane-umax_pp.so
/usr/lib64/sane/libsane-umax_pp.so.1
/usr/lib64/sane/libsane-umax_pp.so.1.0.30
/usr/lib64/sane/libsane-v4l.so
/usr/lib64/sane/libsane-v4l.so.1
/usr/lib64/sane/libsane-v4l.so.1.0.30
/usr/lib64/sane/libsane-xerox_mfp.so
/usr/lib64/sane/libsane-xerox_mfp.so.1
/usr/lib64/sane/libsane-xerox_mfp.so.1.0.30

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sane-backends/74a8a6531a42e124df07ab5599aad63870fa0bd4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gamma4scanimage.1
/usr/share/man/man1/sane-config.1
/usr/share/man/man1/sane-find-scanner.1
/usr/share/man/man1/scanimage.1
/usr/share/man/man5/sane-abaton.5
/usr/share/man/man5/sane-agfafocus.5
/usr/share/man/man5/sane-apple.5
/usr/share/man/man5/sane-artec.5
/usr/share/man/man5/sane-artec_eplus48u.5
/usr/share/man/man5/sane-as6e.5
/usr/share/man/man5/sane-avision.5
/usr/share/man/man5/sane-bh.5
/usr/share/man/man5/sane-canon.5
/usr/share/man/man5/sane-canon630u.5
/usr/share/man/man5/sane-canon_dr.5
/usr/share/man/man5/sane-cardscan.5
/usr/share/man/man5/sane-coolscan.5
/usr/share/man/man5/sane-coolscan2.5
/usr/share/man/man5/sane-coolscan3.5
/usr/share/man/man5/sane-dc210.5
/usr/share/man/man5/sane-dc240.5
/usr/share/man/man5/sane-dc25.5
/usr/share/man/man5/sane-dll.5
/usr/share/man/man5/sane-dmc.5
/usr/share/man/man5/sane-epjitsu.5
/usr/share/man/man5/sane-epson.5
/usr/share/man/man5/sane-epson2.5
/usr/share/man/man5/sane-epsonds.5
/usr/share/man/man5/sane-fujitsu.5
/usr/share/man/man5/sane-genesys.5
/usr/share/man/man5/sane-gt68xx.5
/usr/share/man/man5/sane-hp.5
/usr/share/man/man5/sane-hp3500.5
/usr/share/man/man5/sane-hp3900.5
/usr/share/man/man5/sane-hp4200.5
/usr/share/man/man5/sane-hp5400.5
/usr/share/man/man5/sane-hp5590.5
/usr/share/man/man5/sane-hpljm1005.5
/usr/share/man/man5/sane-hs2p.5
/usr/share/man/man5/sane-ibm.5
/usr/share/man/man5/sane-kodak.5
/usr/share/man/man5/sane-kodakaio.5
/usr/share/man/man5/sane-kvs1025.5
/usr/share/man/man5/sane-kvs20xx.5
/usr/share/man/man5/sane-kvs40xx.5
/usr/share/man/man5/sane-leo.5
/usr/share/man/man5/sane-lexmark.5
/usr/share/man/man5/sane-ma1509.5
/usr/share/man/man5/sane-magicolor.5
/usr/share/man/man5/sane-matsushita.5
/usr/share/man/man5/sane-microtek.5
/usr/share/man/man5/sane-microtek2.5
/usr/share/man/man5/sane-mustek.5
/usr/share/man/man5/sane-mustek_usb.5
/usr/share/man/man5/sane-mustek_usb2.5
/usr/share/man/man5/sane-nec.5
/usr/share/man/man5/sane-net.5
/usr/share/man/man5/sane-niash.5
/usr/share/man/man5/sane-p5.5
/usr/share/man/man5/sane-pie.5
/usr/share/man/man5/sane-pieusb.5
/usr/share/man/man5/sane-pixma.5
/usr/share/man/man5/sane-plustek.5
/usr/share/man/man5/sane-plustek_pp.5
/usr/share/man/man5/sane-qcam.5
/usr/share/man/man5/sane-ricoh.5
/usr/share/man/man5/sane-ricoh2.5
/usr/share/man/man5/sane-rts8891.5
/usr/share/man/man5/sane-s9036.5
/usr/share/man/man5/sane-sceptre.5
/usr/share/man/man5/sane-scsi.5
/usr/share/man/man5/sane-sharp.5
/usr/share/man/man5/sane-sm3600.5
/usr/share/man/man5/sane-sm3840.5
/usr/share/man/man5/sane-snapscan.5
/usr/share/man/man5/sane-sp15c.5
/usr/share/man/man5/sane-st400.5
/usr/share/man/man5/sane-stv680.5
/usr/share/man/man5/sane-tamarack.5
/usr/share/man/man5/sane-teco1.5
/usr/share/man/man5/sane-teco2.5
/usr/share/man/man5/sane-teco3.5
/usr/share/man/man5/sane-test.5
/usr/share/man/man5/sane-u12.5
/usr/share/man/man5/sane-umax.5
/usr/share/man/man5/sane-umax1220u.5
/usr/share/man/man5/sane-umax_pp.5
/usr/share/man/man5/sane-usb.5
/usr/share/man/man5/sane-v4l.5
/usr/share/man/man5/sane-xerox_mfp.5
/usr/share/man/man7/sane.7
/usr/share/man/man8/saned.8

%files locales -f sane-backends.lang
%defattr(-,root,root,-)

