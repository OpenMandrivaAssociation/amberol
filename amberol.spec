Name:           amberol
Version:        0.10.3
Release:        1
Summary:        A small and simple sound and music player that is well integrated with GNOME.
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/amberol/
Source0:        https://gitlab.gnome.org/World/amberol/-/archive/%{version}/amberol-%{version}.tar.bz2
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  meson
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0)


%description
A small and simple sound and music player that is well integrated with GNOME.
Amberol aspires to be as small, unintrusive, and simple as possible. It does
not manage your music collection; it does not let you manage playlists, smart
or otherwise; it does not let you edit the metadata for your songs; it does
not show you lyrics for your songs, or the Wikipedia page for your bands.
Amberol plays music, and nothing else.

%prep
%autosetup -n %{name}-%{version} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
