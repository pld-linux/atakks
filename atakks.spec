Summary:	atakks
Name:		atakks
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://team.gcu-squad.org/~fab/down/atakks.tgz
Source1:	%{name}.desktop
Patch0:		%{name}-dir.patch
URL:		http://team.gcu-squad.org/~fab/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
Requires:	SDL >= 1.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
Ataxx is some old chinese reflexion game, like othello, and can be
played by two players.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
rm -f atakks

LDFLAGS="-lSDL -lpthread -s -L/usr/X11R6/lib"
CFLAGS="-Wall -ansi -DUS"
gcc $LDFLAGS $CFLAGS -o %{name} *.c -I%{_includedir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT $RPM_BUILD_ROOT%{_applnkdir}/Games 
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install *.bmp $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{name} $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/*.bmp
%{_applnkdir}/Games/*
