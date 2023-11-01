Name:           jbig2dec
Version:        0.16
Release:        1%{?dist}
Summary:        A decoder implementation of the JBIG2 image compression format 

Group:          System Environment/Libraries
License:        GPLv2
URL:            http://jbig2dec.sourceforge.net/
Source0:        https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs927/%{name}-%{version}.tar.gz
BuildRequires:  libtool
Requires:       %{name}-libs = %{version}-%{release}

Patch0:         CVE-2020-12268.patch

%description
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

%package  libs 
Summary:         A decoder implementation of the JBIG2 image compression format
Group:           System Environment/Libraries

%description  libs 
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

This package provides the shared jbig2dec library.

%package  devel
Summary:          Static library and header files for development with jbig2dec
Group:            Development/Libraries
Requires:         %{name}-libs = %{version}-%{release}

%description  devel
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

This package is only needed if you plan to develop or compile applications
which requires the jbig2dec library.


%prep
%setup -q
%patch0 -p1


%build
autoreconf -i
%configure
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%post libs -p /sbin/ldconfig

%postun  libs -p /sbin/ldconfig


%files
%doc CHANGES COPYING LICENSE README
%{_bindir}/jbig2dec
%{_mandir}/man?/jbig2dec.1.gz

%files  devel
%doc CHANGES COPYING LICENSE README
%{_includedir}/jbig2.h
%{_libdir}/libjbig2dec.so

%files  libs
%doc CHANGES COPYING LICENSE README
%{_libdir}/libjbig2dec.so.0
%{_libdir}/libjbig2dec.so.0.0.0



%changelog
* Thu Oct 08 2020 Nikola Forró <nforro@redhat.com> - 0.16-1
- Update to 0.16
  resolves: #1886011

* Sun Jun 28 2020 Nikola Forró <nforro@redhat.com> - 0.14-4
- Add explicit package version requirement on jbig2dec-libs to jbig2dec
  related: #1851058

* Fri Jun 26 2020 Nikola Forró <nforro@redhat.com> - 0.14-3
- Fix CVE-2020-12268
  resolves: #1851058

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 11 2017 Michael J Gruber <mjg@fedoraproject.org> - 0.14-1
- update to 0.14 (bugfix release)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 0.13.4
- Add fix for CVE-2017-7976 (#1443898)

* Wed May  3 2017 Pavel Zhukov <pzhukov@redhat.com> - 0.13-3
- Prevent segserv due to int overflow (#1443898)

* Tue Mar 07 2017  Pavel Zhukov <landgraf@fedoraproject.org> - 0.13-1
- New release 0.13

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 0.12-2
- New release (#1208076)
- Require autotools

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.11-7
- Add ARM64 patch

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Pavel Zhukov <landgraf@fedoraproject.org>  - 0.11-2.fc14
- Fixed some spec errors

* Tue Jan 11 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.11-1.fc14
- Initial package
