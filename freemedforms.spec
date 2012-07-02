%define major		1
%define Werror_cflags	%nil

Name:		freemedforms
Version:	0.7.6
Release:	1
License:	GPLv3+
Summary:	Electronical Medical Record
Url:		http://www.freemedforms.com
Group:		Office
Source0:	http://freemedforms.googlecode.com/files/freemedformsfullsources-%{version}.tgz
Patch0:		freemedforms-0.7.3-mdv-use_system_quazip.patch
BuildRequires:	doxygen
BuildRequires:	qt4-devel >= 4.6.2
#BuildRequires:	quazip-devel
BuildRequires:	qt4-database-plugin-sqlite
BuildRequires:	dos2unix
Requires:	qt4-database-plugin-sqlite
Suggests:	%{name}-doc = %{version}

%description
FreeMedForms is a multi-user, Open EMR (electronic medical record) manager.
It is free and open source. The main objective of FreeMedForms is to create
a highly dynamic EMR manager where patient files are defined by a set of XML
scripted files. Interoperability and internationalization are main objectives
too.

FreeMedForms is intended to be used:

* in general medical practice (unique doctor office, groups),
* in small clinics and hospitals,
* in clinical research groups.

%package common
Summary:		Common libraries for FreeMedForms and its derivatives

%description common
This package contains common libraries used by FreeMedForms and its derivatives
including FreeDiams.

%package -n freediams
Summary:	Standalone prescriber
Requires:	%{name}-common = %{version}
Suggests:	freediams-doc = %{version}

%description -n freediams
FreeDiams prescriber is the result of FreeMedForms prescriber plugins built
into a standalone application. FreeDiams is a multi-platform (MacOS, Linux,
FreeBSD, Windows), free and open source released under the GPLv3 license.

It is mainly developed by medical doctors and is intended for use by these same
professionals. It can be used alone to prescribe and / or test drug
interactions within a prescription. It can be linked to any application thanks
to its command line parameters.

FreeDiams can manage multiple drugs databases. Some drugs databases are already
available:

* French (sources: AFSSAPS)
* Canadian (sources: HCDPD)
* USA (sources: FDA)
* South African (sources: AEPI)

The interactions database (source: AFSSAPS) give access to many informations:

* interactions by themselves
* risk level
* nature of the risk
* management of the interaction

%package devel
Summary:	Development files for FreeMedForms
Group:		Development/C++
Requires:	%{name} = %{version}

%description devel
FreeMedForms is a free, open source, multiplatform medical forms manager.
It can be used for clinical research and patient database management.

%package doc-en
Summary:	English documentation for FreeMedForms
Requires:	locales-en
Provides:	%{name}-doc = %{EVRD}

%description doc-en
FreeMedForms documentation in English.

%package doc-fr
Summary:	French documentation for FreeMedForms
Requires:	locales-fr
Provides:	%{name}-doc = %{EVRD}

%description doc-fr
FreeMedForms documentation in French.

%package -n freediams-doc-en
Summary:	English documentation for FreeDiams
Requires:	locales-en
Provides:	freediams-doc = %{EVRD}

%description -n freediams-doc-en
FreeDiams documentation in English.

%package -n freediams-doc-fr
Summary:	French documentation for FreeDiams
Requires:	locales-fr
Provides:	freediams-doc = %{EVRD}

%description -n freediams-doc-fr
FreeDiams documentation in French.

%prep
%setup -q -n %{name}-%{version}
#patch0 -p1
dos2unix *.txt

%build
lrelease global_resources/translations/*.ts

pushd freemedforms
%qmake_qt4 -r -config release "CONFIG+=LINUX_INTEGRATED" INSTALL_ROOT_PATH="%{_prefix}" LIBRARY_BASENAME="%{_lib}" LOWERED_APPNAME="%{name}" %{name}.pro
%make
popd

pushd freediams
%qmake_qt4 -r -config release "CONFIG+=LINUX_INTEGRATED" INSTALL_ROOT_PATH="%{_prefix}" LIBRARY_BASENAME="%{_lib}" LOWERED_APPNAME="freediams" freediams.pro
%make
popd


%install
pushd freemedforms
%makeinstall_std INSTALL_ROOT=%{buildroot}
popd

pushd freediams
%makeinstall_std INSTALL_ROOT=%{buildroot}
popd

%__install -D -m 644 global_resources/pixmap/svg/freemedforms.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/freemedforms.svg
%__install -D -m 644 global_resources/pixmap/svg/freediams.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/freediams.svg

# files for the doc package
%__install -d %{buildroot}%{_docdir}/%{name}
%__mv %{buildroot}%{_docdir}/freemedforms-project/freemedforms/ %{buildroot}%{_docdir}/
%__mv %{buildroot}%{_docdir}/freemedforms-project/freediams/ %{buildroot}%{_docdir}/
%__rm -rf %{buildroot}%{_docdir}/freemedforms-project/

%files
%defattr(-,root,root,755)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.pluginspec
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}
%doc COPYING.txt README.txt
%exclude %{_docdir}/%{name}/en
%exclude %{_docdir}/%{name}/fr

%files doc-en
%defattr(-,root,root,755)
%{_docdir}/%{name}/en

%files doc-fr
%defattr(-,root,root,755)
%{_docdir}/%{name}/fr

%files devel
%defattr(-,root,root,755)
%{_libdir}/%{name}-common/*.so

%files common
%defattr(-,root,root,755)
%{_libdir}/%{name}-common/*.so.*

%files -n freediams
%defattr(-,root,root,755)
%{_bindir}/freediams
%{_libdir}/freediams
%{_datadir}/freediams
%{_datadir}/applications/freediams.desktop
%{_datadir}/pixmaps/freediams.svg
%{_iconsdir}/hicolor/scalable/apps/freediams.svg
%doc COPYING.txt README.txt
%exclude %{_docdir}/freediams/en
%exclude %{_docdir}/freediams/fr

%files -n freediams-doc-en
%defattr(-,root,root,755)
%{_docdir}/freediams/en

%files -n freediams-doc-fr
%defattr(-,root,root,755)
%{_docdir}/freediams/fr
