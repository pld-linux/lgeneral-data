Summary:	LGeneral game - data files
Summary(pl.UTF-8):	Gra Linux General - pliki z danymi
Name:		lgeneral-data
Version:	1.1.3
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/lgeneral/%{name}-%{version}.tar.gz
# Source0-md5:	786feb83f163834a22e3e85e1970145f
Patch0:		%{name}-inst_dir.patch
Patch1:		%{name}-directories.patch
URL:		http://lgames.sourceforge.net/LGeneral
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains Panzer General data files for the game.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera pliki z danymi Panzer General dla tej gry.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/lgeneral/gfx/flags/pg.bmp
%{_datadir}/lgeneral/gfx/terrain/pg
%{_datadir}/lgeneral/gfx/units/pg*.bmp
%{_datadir}/lgeneral/maps/pg
%{_datadir}/lgeneral/maps/pg.tdb
%{_datadir}/lgeneral/nations/pg.ndb
%{_datadir}/lgeneral/scenarios/pg
%{_datadir}/lgeneral/sounds/pg
%{_datadir}/lgeneral/units/pg.udb
