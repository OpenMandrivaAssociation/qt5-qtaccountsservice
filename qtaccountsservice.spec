Summary:	Qt-style API for AccountsService
Name:		qtaccountsservice
Version:	0.1.1
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/mauios/qtaccountsservice
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5)

%track
prog %{name} = {
	url = http://downloads.sourceforge.net/project/mauios/hawaii/qtaccountsservice
	regex = "%{name}-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Qt-style API for AccountsService.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
