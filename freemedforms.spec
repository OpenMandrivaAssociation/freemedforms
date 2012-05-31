%define oname		FreeMedForms
%define major		1
%define Werror_cflags	%nil

Name:		freemedforms
Version:	0.7.3
Release:	1
License:	GPLv3+
Summary:	Open-source Prescriber
Url:		http://www.freemedforms.com
Group:		Office
Source0:	http://freemedforms.googlecode.com/files/freemedformsfullsources-%{version}.tgz
Patch0:		freemedforms-0.7.0-mdv-use-system-quazip.patch
BuildRequires:	doxygen
BuildRequires:	qt4-devel >= 4.6.2
#BuildRequires:	quazip-devel
BuildRequires:	qt4-database-plugin-sqlite
BuildRequires:	dos2unix
Requires:	qt4-database-plugin-sqlite
Requires:	%{name}-data = %{EVRD}
Suggests:	%{name}-doc = %{EVRD}

%description
FreeMedForms is a free, open source, multiplatform medical forms manager.
It can be used for clinical research and patient database management.  

%package data
Summary:	Data files for %{oname}

%description data
FreeMedForms is a free, open source, multiplatform medical forms manager.
It can be used for clinical research and patient database management.

%package devel
Summary:	Development files for %{oname}
Group:		Development/C++
Requires:	%{name} = %{version}

%description devel
FreeMedForms is a free, open source, multiplatform medical forms manager.
It can be used for clinical research and patient database management.

%prep
%setup -q -n %{name}-%{version}
#patch0 -p1
dos2unix *.txt

%build
lrelease global_resources/translations/*.ts
%qmake_qt4 -r -config release "CONFIG+=LINUX_INTEGRATED" INSTALL_ROOT_PATH="%{_prefix}" LIBRARY_BASENAME="%{_lib}" LOWERED_APPNAME="%{name}" %{name}.pro
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%__install -D -m 644 global_resources/pixmap/svg/freemedforms.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/freemedforms.svg

# files for the doc package
%__install -d %{buildroot}%{_docdir}/%{name}
%__mv %{buildroot}%{_docdir}/freemedforms-project/freemedforms/ %{buildroot}%{_docdir}/
%__rm -rf %{buildroot}%{_docdir}/freemedforms-project/

# Fix permissions for directories
find %{buildroot} -type d -exec chmod 755 \;

%files
%defattr(-,root,root,755)
%{_bindir}/%{name}
#%{_libdir}/%{name}/*.so.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.pluginspec
%{_libdir}/%{name}-common/*.so.*
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%doc COPYING.txt README.txt

%files devel
%{_libdir}/%{name}-common/*.so

%files data
%defattr(644,root,root,755)
%{_datadir}/%{name}
