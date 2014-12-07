%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Qt-style API for AccountsService
Name:		qtaccountsservice
Version:	0.1.2
Release:	3
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/mauios/qtaccountsservice
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Source1:	qtaccountsservice.rpmlintrc
BuildRequires:	cmake
BuildRequires:	qt5-devel
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
%dir %{_libdir}/hawaii/qml/QtAccountsService
%{_libdir}/hawaii/qml/QtAccountsService/libdeclarative_accountsservice.so
%{_libdir}/hawaii/qml/QtAccountsService/plugins.qmltypes
%{_libdir}/hawaii/qml/QtAccountsService/qmldir


%files -n %{libname}
%{_libdir}/*qtaccountsservice-qt5.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/QtAccountsService
%dir %{_libdir}/cmake/QtAccountsService
%{_includedir}/QtAccountsService/AccountsManager
%{_includedir}/QtAccountsService/UserAccount
%{_includedir}/QtAccountsService/UsersModel
%{_includedir}/QtAccountsService/*.h
%{_libdir}/cmake/QtAccountsService/*.cmake
%{_libdir}/*qtaccountsservice-qt5.so

