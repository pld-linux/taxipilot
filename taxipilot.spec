Summary:	Game based on Spacetaxi
Summary(pl.UTF-8):	Gra oparta na Spacetaxi
Name:		taxipilot
Version:	0.9.01
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	b07f27628fc58bf931ec36342396eded
URL:		http://taxipilot.sourceforge.net/
#BuildRequires:	arts-kde-devel
BuildRequires:	kdemultimedia-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
TaxiPilot is a little game, based on Spacetaxi game for C64.
Objective is to pick up passengers waiting on a number of platforms
and to drop them where they want to go.

%description -l pl.UTF-8
TaxiPilot jest małą grą, opartą na grze Spacetaxi napisanej dla C64.
Celem jest zbieranie pasażerów czekających na licznych platformach i
dostarczanie ich do miejsca gdzie życzą sobie być dowiezieni.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_libdir}/*.la
%{_libdir}/mcop/*.mcop*
%{_datadir}/apps/%{name}
%{_applnkdir}/Games/%{name}.desktop
%{_pixmapsdir}/*/*/apps/*.png
