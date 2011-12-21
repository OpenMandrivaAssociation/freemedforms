%define oname		FreeMedForms
%define major		1
%define Werror_cflags	%nil

Name:		freemedforms
Version:	0.6.0
Release:	1
License:	GPLv3+
Summary:	Open-source Prescriber
Url:		http://www.freemedforms.com
Group:		Office
Source0:	http://freemedforms.googlecode.com/files/freemedformsfullsources-%{version}.tgz
Patch0:		freemedforms-0.6.0-mdv-use-system-quazip.patch
Patch1:		freemedforms-0.6.0-desktop.patch
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
Requires:	%{name} = %{EVRD}

%description devel
FreeMedForms is a free, open source, multiplatform medical forms manager.
It can be used for clinical research and patient database management.

%prep
%setup -q -n %{name}-%{version}
#patch0 -p1
%patch1 -p1
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
%__mv %{buildroot}%{_datadir}/%{name}/doc/%{name}/* %{buildroot}%{_docdir}/%{name}
%__rm -rf %{buildroot}%{_datadir}/%{name}/doc

# Fix permissions for directories
find %{buildroot} -type d -exec chmod 755 \;

%files
%defattr(-,root,root,755)
%{_bindir}/%{name}
%{_libdir}/%{name}/*.so.1*
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_libdir}/%{name}/libAccountBase.so
%{_libdir}/%{name}/libAccount.so
%{_libdir}/%{name}/libAgenda.so
%{_libdir}/%{name}/libBaseWidgets.so
%{_libdir}/%{name}/libCategory.so
%{_libdir}/%{name}/libCore.so
%{_libdir}/%{name}/libDrugsBase.so
%{_libdir}/%{name}/libDrugs.so
%{_libdir}/%{name}/libFormManager.so
%{_libdir}/%{name}/libGir.so
%{_libdir}/%{name}/libICD.so
%{_libdir}/%{name}/libListView.so
%{_libdir}/%{name}/libMainWindow.so
%{_libdir}/%{name}/libPadTools.so
%{_libdir}/%{name}/libPatientBase.so
%{_libdir}/%{name}/libPMH.so
%{_libdir}/%{name}/libPrinter.so
%{_libdir}/%{name}/libTemplates.so
%{_libdir}/%{name}/libTextEditor.so
%{_libdir}/%{name}/libUserManager.so
%{_libdir}/%{name}/libXmlIO.so
%{_libdir}/%{name}/libZipCodes.so
%{_libdir}/%{name}/*.pluginspec
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%doc COPYING.txt README.txt

%files devel
%{_libdir}/%{name}/libAggregation.so
%{_libdir}/%{name}/libCalendar.so
%{_libdir}/%{name}/libExtensionSystem.so
%{_libdir}/%{name}/libMedicalUtils.so
%{_libdir}/%{name}/libquazip.so
%{_libdir}/%{name}/libTranslationUtils.so
%{_libdir}/%{name}/libUtils.so

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/databases
%dir %{_datadir}/%{name}/forms
%dir %{_datadir}/%{name}/profiles
%dir %{_datadir}/%{name}/sql
%dir %{_datadir}/%{name}/package_helpers
%dir %{_datadir}/%{name}/pixmap/64x64
%dir %{_datadir}/%{name}/textfiles
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmap
%dir %{_datadir}/%{name}/pixmap/16x16
%dir %{_datadir}/%{name}/pixmap/16x16/flags
%dir %{_datadir}/%{name}/pixmap/32x32
%dir %{_datadir}/%{name}/pixmap/64x64
%dir %{_datadir}/%{name}/pixmap/splashscreens
%dir %{_datadir}/%{name}/pixmap/svg
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/databases
%{_datadir}/%{name}/forms
%{_datadir}/%{name}/profiles
%{_datadir}/%{name}/sql
%{_datadir}/%{name}/pixmap/16x16/*.png
%{_datadir}/%{name}/pixmap/16x16/flags/*.png
%{_datadir}/%{name}/pixmap/32x32/*.png
%{_datadir}/%{name}/pixmap/64x64/*.png
%{_datadir}/%{name}/pixmap/64x64/*.jpg
%{_datadir}/%{name}/pixmap/splashscreens/*.png
%{_datadir}/%{name}/pixmap/svg/*.svg
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/%{name}/textfiles/*
%{_datadir}/%{name}/package_helpers/*
