Summary:	Game based on Spacetaxi
Summary(pl):	Gra oparta na Spacetaxi
Name:		taxipilot
Version:	0.8.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6e566a5028aa74195ff3cdbe948b9ee8
BuildRequires:	arts-kde-devel
BuildRequires:	kdemultimedia-devel
URL:		http://taxipilot.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_htmldir	%{_docdir}/kde/HTML

%description
TaxiPilot is a little game, based on Spacetaxi game for C64.
Objective is to pick up passengers waiting on a number of platforms
and to drop them where they want to go.      

%description -l pl
TaxiPilot jest ma�� gr�, opart� na grze Spacetaxi napisanej dla C64.
Celem jest zbieranie pasa�er�w czekaj�cych na licznych platformach i
dostarczanie ich do miejsca gdzie �ycz� sobie by� dowiezieni.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post -p   /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_libdir}/mcop/*.mcop*
%{_datadir}/apps/%{name}
%{_applnkdir}/Games/%{name}.desktop
%{_pixmapsdir}/*/*/apps/*.png
%{_htmldir}/*/%{name}