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
%setup

%build
./configure
make
make check

%install
make install

%post
echo '/usr/local/lib' > /etc/ld.so.conf.d/libmaxminddb.conf
ldconfig

%postun
# Do this only during uninstall process (not during update)
if [ $1 -eq 0 ]; then
    rm -f /etc/ld.so.conf.d/libmaxminddb.conf
    ldconfig
fi

%files
/usr/local/lib/libmaxminddb.*
/usr/local/lib/pkgconfig/libmaxminddb.pc
/usr/local/include/maxminddb*
