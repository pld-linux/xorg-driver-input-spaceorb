# http://lists.x.org/archives/xorg-devel/2009-February/000220.html
Summary:	X.org input driver for SpaceOrb devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla urządzeń SpaceOrb
Name:		xorg-driver-input-spaceorb
Version:	1.1.1
Release:	3.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-spaceorb-%{version}.tar.bz2
# Source0-md5:	c7fb96281874733480ba86a5a0a3b5af
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for SpaceOrb devices.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla urządzeń SpaceOrb.

%prep
%setup -q -n xf86-input-spaceorb-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/spaceorb_drv.so
#%{_mandir}/man4/spaceorb.4*
