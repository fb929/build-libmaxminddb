Name:           libmaxminddb
Version:        1.11.0
Release:        0%{?dist}
Summary:        C library for the MaxMind DB file format

License:        Apache License
URL:            https://github.com/maxmind/libmaxminddb
Source0:        https://github.com/maxmind/libmaxminddb/releases/download/%{version}/libmaxminddb-%{version}.tar.gz

BuildRequires:  gcc, make, autoconf, automake, libtool

%description
The libmaxminddb library provides a C library for reading MaxMind DB files, including the GeoIP2 databases from MaxMind.

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir}
make %{?_smp_mflags}
make check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_libdir}/libmaxminddb.so*
%{_libdir}/libmaxminddb.a
%{_libdir}/libmaxminddb.la
%{_libdir}/pkgconfig/libmaxminddb.pc
%{_includedir}/maxminddb.h
%{_includedir}/maxminddb_config.h
%{_bindir}/mmdblookup
%{_mandir}/man1/mmdblookup.1*
%{_mandir}/man3/MMDB_*.3*
%{_mandir}/man3/libmaxminddb.3*
