Summary:	LGeneral game - data files
Summary(pl):	Gra Linux General - pliki z danymi
Name:		lgeneral-data
Version:	1.1.3
Release:	1
License:	GPL
Group:		Applications/Games
BuildArch:	noarch
Source0:	http://dl.sourceforge.net/lgeneral/%{name}-%{version}.tar.gz
# Source0-md5:	786feb83f163834a22e3e85e1970145f
Patch0:		%{name}-inst_dir.patch
Patch1:		%{name}-directories.patch
URL:		http://lgames.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains data files for the game.

%description -l pl
LGeneral jest turow± gr± strategiczn± zainspirowan± o Panzer General.
Ten pakiet zawiera pliki z danymi dla tej gry.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%{_datadir}/lgeneral/gfx/*/*
%{_datadir}/lgeneral/maps/*
%{_datadir}/lgeneral/nations/*
%{_datadir}/lgeneral/scenarios/*
%{_datadir}/lgeneral/sounds/*
%{_datadir}/lgeneral/units/*
