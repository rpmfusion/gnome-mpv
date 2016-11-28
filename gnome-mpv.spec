%global glib2_version 2.44
%global gtk3_version 3.18
%global mpv_version 1.20

Name:           gnome-mpv
Version:        0.10
Release:        2%{?dist}
Summary:        A simple GTK+ frontend for mpv

License:        GPLv3+
URL:            https://github.com/gnome-mpv/gnome-mpv
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  intltool >= 0.40.6
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(mpv) >= %{mpv_version}
Requires:       youtube-dl >= 2016.03.06
Requires:       hicolor-icon-theme

%description
GNOME MPV interacts with mpv via the client API exported by libmpv,
allowing access to mpv's powerful playback capabilities.

%prep
%autosetup

%build
%configure
%make_build V=1

%install
%make_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/io.github.GnomeMpv.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.GnomeMpv.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/io.github.GnomeMpv.appdata.xml
%{_datadir}/applications/io.github.GnomeMpv.desktop
%{_datadir}/glib-2.0/schemas/io.github.GnomeMpv.gschema.xml
# The old GSchema is left installed for settings migration.
%{_datadir}/glib-2.0/schemas/org.gnome-mpv.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}*.svg

%changelog
* Mon Nov 28 2016 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.10-2
- Bump release

* Fri Jul 29 2016 Maxim Orlov <murmansksity@gmail.com> - 0.10-1
- Update to 0.10
- Add missing Requires: hicolor-icon-theme

* Wed May 18 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9-1.R
- Update to 0.9
- Use a new SourceURL
- Update glib2 dep version
- Update gtk3 dep version
- Remove NOCONFIGURE=1 ./autogen.sh
- Remove BR automake, autoconf-archive

* Mon Apr 18 2016 Maxim Orlov <murmansksity@gmail.com> - 0.8-1.R
- Update to 0.8
- Add AUTHORS %%doc
- Add mpv dep version
- Update gtk3 dep version
- Change app ID to io.github.GnomeMpv

* Sat Jan 30 2016 Maxim Orlov <murmansksity@gmail.com> - 0.7-1.R
- Update to 0.7
- Add AppData
- Add symbolic icon

* Sat Nov 14 2015 Maxim Orlov <murmansksity@gmail.com> - 0.6-3.R
- Fix E: explicit-lib-dependency mpv-libs (rpmlint)

* Fri Nov 13 2015 Maxim Orlov <murmansksity@gmail.com> - 0.6-2.R
- Update dependencies (mpv-libs-devel, mpv-libs)

* Mon Oct 26 2015 Maxim Orlov <murmansksity@gmail.com> - 0.6-1.R
- Update to 0.6
- Add autoconf-archive BR
- Add NOCONFIGURE=1 ./autogen.sh
- Add V=1 (Make the build verbose)
- Remove autoreconf, intltoolize calls

* Sat Oct 17 2015 Maxim Orlov <murmansksity@gmail.com> - 0.5-2.R
- Remove requires mpv
- Minor spec cleanup

* Mon Aug 17 2015 Maxim Orlov <murmansksity@gmail.com> - 0.5-1.R
- Initial package.