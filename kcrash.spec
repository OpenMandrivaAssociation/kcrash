%define major 5
%define libname %mklibname KF5Crash %{major}
%define devname %mklibname KF5Crash -d
%define debug_package %{nil}

Name: kcrash
Version: 4.99.0
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 crash handling library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

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
Requires: extra-cmake-modules5
Requires: cmake(KF5CoreAddons)
Requires: cmake(KF5WindowSystem)
Requires: cmake(Qt5Core)

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

%files

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Crash
%{_libdir}/qt5/mkspecs/modules/*.pri
