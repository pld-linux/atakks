Summary:	atakks game
Summary(pl.UTF-8):	Gra atakks
Name:		atakks
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://team.gcu-squad.org/~fab/down/%{name}.tgz
# Source0-md5:	9153c731620bf85bb60d00a1c93b621e
Source1:	%{name}.desktop
Patch0:		%{name}-dir.patch
URL:		http://team.gcu-squad.org/~fab/
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel
Requires:	SDL >= 1.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ataxx is some old Chinese reflexion game, like othello, and can be
played by two players.

%description -l pl.UTF-8
Ataxx to stara chińska gra umysłowa, jak otello, w którą może grać
dwóch graczy.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
rm -f atakks

LDFLAGS="%{rpmldflags} -lSDL -lpthread -L/usr/X11R6/lib"
CFLAGS="%{rpmcflags} -Wall -ansi -DUS -I/usr/X11R6/include"
%{__cc} $LDFLAGS $CFLAGS -o %{name} *.c

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Games/*
