Name:           gnome-mpv
Version:        0.16
Release:        9%{?dist}
Summary:        A simple GTK+ frontend for mpv

License:        GPLv3+
URL:            https://github.com/gnome-mpv/gnome-mpv
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18
BuildRequires:  intltool >= 0.40.6
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  mpv-libs-devel
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
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.github.GnomeMpv.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.GnomeMpv.desktop

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/io.github.GnomeMpv.appdata.xml
%{_datadir}/applications/io.github.GnomeMpv.desktop
%{_datadir}/dbus-1/services/io.github.GnomeMpv.service
%{_datadir}/glib-2.0/schemas/io.github.GnomeMpv.gschema.xml
# The old GSchema is left installed for settings migration.
%{_datadir}/glib-2.0/schemas/org.gnome-mpv.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
 %{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Leigh Scott <leigh123linux@gmail.com> - 0.16-6
- Rebuild for new mpv

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.16-1
- Update to 0.16

* Wed Sep 12 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.15-2
- Remove obsolete scriptlets

* Wed Sep 12 2018 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.15-1
- Update to 0.15

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 19 2018 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.14-1
- Update to 0.14

* Tue Oct 17 2017 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.13-1
- Update to 0.13

* Fri Sep 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.12-3
- Add build requires mesa-libEGL-devel

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.12-1
- Update to 0.12

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.11-1
- Update to 0.11

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
