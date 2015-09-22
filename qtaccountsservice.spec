%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Qt-style API for AccountsService
Name:		qtaccountsservice
Version:	0.6.0
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/mauios/qtaccountsservice
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.xz
Source1:	qtaccountsservice.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
Requires:	%{libname} = %{EVRD}
Requires:	accountsservice

%track
prog %{name} = {
	url = http://downloads.sourceforge.net/project/mauios/hawaii/qtaccountsservice
	regex = "%{name}-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Qt-style API for AccountsService.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
%{name} main library.

%package -n %{develname}
Summary:	Development library for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{libname}
Development files and libraries for %{name}.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_libdir}/qml/QtAccountsService/libdeclarative_accountsservice.so
%{_libdir}/qml/QtAccountsService/plugins.qmltypes
%{_libdir}/qml/QtAccountsService/qmldir


%files -n %{libname}
%{_libdir}/libQtAccountsService.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/QtAccountsService/QtAccountsService
%{_includedir}/QtAccountsService/QtAccountsService/AccountsManager
%{_includedir}/QtAccountsService/QtAccountsService/UserAccount
%{_includedir}/QtAccountsService/QtAccountsService/UsersModel
%{_includedir}/QtAccountsService/qtaccountsservice/*.h
%{_libdir}/cmake/QtAccountsService/*.cmake
%{_libdir}/libQtAccountsService.so
