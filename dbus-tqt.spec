%define		tde_version	3.5.13.2
Summary:	Dbus TQT Interface
Name:		dbus-tqt
Version:	0.63
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.fau.de/trinity/releases/%{tde_version}/dependencies/%{name}-trinity-%{tde_version}.tar.xz
# Source0-md5:	cab0649d08671ce19da623a8fb6275bb
BuildRequires:	cmake >= 2.8
BuildRequires:	dbus-devel
BuildRequires:	pkgconfig
BuildRequires:	libstdc++-devel
BuildRequires:	libtqtinterface-devel >= %{tde_version}
BuildRequires:	qt-devel >= 6:3.3.8d
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	qt >= 6:3.3.8d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dbus TQT Interface.

%package devel
Summary:	%{name} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	dbus-qt-devel

%description devel
Development files for %{name}.

%prep
%setup -q -n %{name}-trinity-%{tde_version}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-tqt-1.so.*.*.*
%ghost %{_libdir}/libdbus-tqt-1.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/dbus-1.0/dbus/connection.h
%{_includedir}/dbus-1.0/dbus/dbus-qt.h
%{_includedir}/dbus-1.0/dbus/message.h
%{_includedir}/dbus-1.0/dbus/server.h
%{_libdir}/libdbus-tqt-1.so
%{_libdir}/libdbus-tqt-1.la
%{_pkgconfigdir}/dbus-tqt.pc
