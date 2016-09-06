%define major 0
%define libname %mklibname QtAccountsService %{major}
%define develname %mklibname QtAccountsService -d
%define	upname qtaccountsservice

Summary:	Qt-style API for AccountsService
Name:		qt5-qtaccountsservice
Version:	0.6.0
Release:	3
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/mauios/qtaccountsservice
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{upname}/%{upname}-%{version}.tar.xz
Source1:	qtaccountsservice.rpmlintrc
Patch0:		0001-Add-QDBusConnection-argument-to-AccountsManager.patch
Patch1:		0002-Initial-unit-test.patch
Patch2:		0003-Update-README.md.patch
Patch3:		0004-Remove-duplicate-API.patch
Patch4:		0005-Update-qml-plugin-types.patch
Patch5:		0006-Add-qml-example-for-current-login-user.patch
Patch6:		0007-Use-GPL2-license-for-examples.patch
Patch7:		0008-Add-Travis-CI.patch
Patch8:		0009-Install-cmake-and-ecm-manually.patch
Patch9:		0010-Refactor-Travis-CI.patch
Patch10:	0011-Use-the-new-Travis-CI-workers.patch
Patch11:	0012-Try-with-sudo.patch
Patch12:	0013-Fix-D-Bus-call-to-DeleteUser.patch
Patch13:	0014-Do-not-test-deleteUser-twice.patch
Patch14:	0015-Add-build-status-to-README.md.patch
Patch15:	0016-More-tests.patch
Patch16:	0017-Return-Q_NULLPTR-when-a-user-account-has-not-been-fo.patch
Patch17:	0018-Add-FakeUser.patch
Patch18:	0019-Remove-annoying-debug-messages-from-FakeAccounts.patch
Patch19:	0020-Use-the-same-bus-for-UserAccount-as-AccountsManager.patch
Patch20:	0021-Avoid-potential-crashes-during-tests.patch
Patch21:	0022-Add-GPLv2-license-text.patch
Patch22:	0023-Add-FDL-license-for-documentation.patch
Patch23:	0024-Replace-emit-with-Q_EMIT.patch
Patch24:	0025-Replace-QLatin1String-with-QStringLiteral.patch
Patch25:	0026-Make-AccountsManager-cacheUser-async.patch
Patch26:	0027-Delete-pending-call-watcher.patch
Patch27:	0028-Update-Travis-CI-configuration.patch
Patch28:	0029-Update-README.md.patch
Patch29:	0030-Update-.travis.yml.patch
Patch30:	0031-Add-Coverity-badge.patch
Patch31:	0032-Move-IRC-badge.patch
Patch32:	0033-Specify-the-language-with-Travis-CI.patch
Patch33:	0034-Use-gcc-4.8-and-clang-3.6-with-Travis-CI.patch
Patch34:	0035-Notify-Travis-CI-builds-on-IRC.patch
Patch35:	0036-Do-not-install-clang-3.6-with-Travis-CI.patch
Patch36:	0037-Silence-CMake-warnings.patch
Patch37:	0038-Fix-warnings.patch
Patch38:	0039-Add-listCachedUserAsync-API.patch
Patch39:	0040-For-sddm-QT_NO_CAST_FROM_ASCII-defined.patch
Patch40:	0041-Fix-iconFileName-does-not-exists-issue.patch
Patch41:	0042-By-reference.patch
Patch42:	0043-Cache-users-and-fix-userDelete-signal.patch
Patch43:	0044-Reserve-lists.patch
Patch44:	0045-Do-not-create-QString-from-const-char.patch
Patch45:	0046-Disable-QString-casting-from-const-char.patch

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
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
Obsoletes:	%{mklibname qtaccountsservice 0} < 0.6.0-3
Obsoletes:	%{mklibname qt5-qtaccountsservice 0} < 0.6.0-3

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
%setup -qn %{upname}-%{version}
%apply_patches

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
