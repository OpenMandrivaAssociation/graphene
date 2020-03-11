%global api	1.0
%global major	0
%define libname	%mklibname graphene %{api} %{major}
%define devname	%mklibname graphene %{api} -d
%define girname	%mklibname graphene-gir %{api}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	A thin layer of types for graphic libraries
Name:		graphene
Version:	1.10.0
Release:	2
License:	MIT
Group:          System/Libraries
URL:		https://github.com/ebassi/graphene
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig
BuildRequires:	meson

%description
Graphene provides a small set of mathematical types needed to implement graphic
libraries that deal with 2D and 3D transformations and projections.

%package -n %{libname}
Summary:	A thin layer of types for graphic libraries
Group:		System/Libraries
Obsoletes:	%{_lib}graphene0 < 1.8.0-2

%description -n %{libname}
Graphene provides a small set of mathematical types needed to implement graphic
libraries that deal with 2D and 3D transformations and projections.

%package -n %{devname}
Summary:	Header files for Graphene library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}graphene-devel < 1.8.0-2

%description -n %{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

%package        tests
Summary:        Tests for the %{name} package
Group:          System/Libraries

%description    tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%package -n %{girname}
Summary:	GObject introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}graphene-gir < 1.8.0-2

%description -n %{girname}
GObject introspection interface library for %{name}.

%prep
%autosetup

%build
# meson errors out without a utf8 LANG set
# https://github.com/mesonbuild/meson/issues/1085
export LANG=C.UTF-8

%meson
%meson_build


%install
%meson_install

%files -n %{libname}
%{_libdir}/libgraphene-1.0.so.%{major}{,.*}

%files -n %{devname}
%{_libdir}/libgraphene-1.0.so
%{_includedir}/graphene-1.0
%dir %{_libdir}/graphene-1.0
%{_libdir}/graphene-1.0/include
%{_libdir}/pkgconfig/graphene-1.0.pc
%{_libdir}/pkgconfig/graphene-gobject-1.0.pc
%{_datadir}/gir-1.0/Graphene-1.0.gir

%files -n %{girname}
%{_libdir}/girepository-1.0/Graphene-1.0.typelib

%files tests
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/
