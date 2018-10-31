%define major 0
%define libname %mklibname QtAccountsService %{major}
%define develname %mklibname QtAccountsService -d
%define	upname qtaccountsservice

Summary:	Qt-style API for AccountsService
Name:		qt5-qtaccountsservice
Version:	1.2.0
Release:	2
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/lirios/qtaccountsservice
Source0:	https://github.com/lirios/qtaccountsservice/releases/download/v%{version}/%{upname}-%{version}.tar.xz
Source1:	qtaccountsservice.rpmlintrc

BuildRequires:	qbs
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
Requires:	%{libname} = %{EVRD}
Requires:	accountsservice

%description
Qt-style API for AccountsService.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Obsoletes:	%{mklibname qtaccountsservice 0} < 0.6.0-3
Obsoletes:	%{mklibname qt5-qtaccountsservice 0} < 0.6.0-3

%description -n %{libname}
%{name} main library.

%package -n %{develname}
Summary:	Development library for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Development files and libraries for %{name}.

%prep
%setup -qn %{upname}-%{version}
%apply_patches

%build
qbs setup-toolchains --type clang %{_bindir}/clang clang
qbs setup-qt %{_bindir}/qmake-qt5 qt5
qbs config profiles.qt5.baseProfile gcc
qbs build --no-install -d build profile:qt5 qbs.installRoot:/ qbs.installPrefix:usr modules.lirideployment.qmlDir:lib/qt/qml

%install
qbs install -d build --no-build -v --install-root %{buildroot} profile:qt5

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
