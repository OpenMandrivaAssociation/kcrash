%define major 5
%define libname %mklibname KF5Crash %{major}
%define devname %mklibname KF5Crash -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kcrash
Version:	5.41.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 crash handling library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)

%description
The KDE Frameworks 5 crash handling library.

%package -n %{libname}
Summary: The KDE Frameworks 5 crash handling library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 crash handling library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: cmake(ECM)
Requires: cmake(KF5CoreAddons)
Requires: cmake(KF5WindowSystem)
Requires: cmake(Qt5Core)

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Crash
%{_libdir}/qt5/mkspecs/modules/*.pri
