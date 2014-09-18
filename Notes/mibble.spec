Name: mibble 

Summary: Mib compiler

Version: 2.9.3

Release: 1.guavus%{?dist}

License: GPLv2

Group: System Environment/Libraries

Source: mibble-2.9.3.tar.gz

BuildRoot: %{tmppath}/%{name}%{version}%{release}root%(%{_id_u} -n)

%define sonamever 1

%description
 Mibble Browser

%prep

%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/java

cp -r . $RPM_BUILD_ROOT/usr/share/java/

rm -rf $RPM_BUILD_ROOT/usr/share/java/src
rm -rf $RPM_BUILD_ROOT/usr/share/java/bin
rm -rf $RPM_BUILD_ROOT/usr/share/java/doc
rm -rf $RPM_BUILD_ROOT/usr/share/java/build.xml

mkdir -p $RPM_BUILD_ROOT/usr/local/

cp -r bin $RPM_BUILD_ROOT/usr/local/bin


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
/usr/share/java
/usr/local/bin
