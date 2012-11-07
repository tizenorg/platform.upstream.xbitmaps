#
# spec file for package xbitmaps
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
Name:           xbitmaps
Version:        1.1.1
Release:        0
License:        MIT
Summary:        Base X bitmaps
Url:            http://xorg.freedesktop.org/releases/individual/data/
Group:          Development/Libraries/C and C++

Source:         %{name}-%{version}.tar.bz2
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

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files devel
%defattr(-,root,root)
%{_includedir}/X11/bitmaps
%{_datadir}/pkgconfig/xbitmaps.pc

%changelog
