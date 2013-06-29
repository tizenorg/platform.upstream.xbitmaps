Name:           xbitmaps
Version:        1.1.1
Release:        0
License:        MIT
Summary:        Base X bitmaps
Url:            http://xorg.freedesktop.org/releases/individual/data/
Group:          Development/Libraries/C and C++

Source:         %{name}-%{version}.tar.bz2
Source1001: 	xbitmaps.manifest
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildArch:      noarch

%description
This package contains the base X bitmaps, which are used in many
legacy X clients.

%package devel
Summary:        Development files for the base X bitmaps
Group:          Development/Libraries/C and C++

%description devel
This package contains the base X bitmaps, which are used in many
legacy X clients.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/X11/bitmaps
%{_datadir}/pkgconfig/xbitmaps.pc

%changelog
