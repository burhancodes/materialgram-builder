Name:           materialgram
Version:        5.7.0.1
Release:        4%{?dist}
Summary:        Telegram Desktop fork with material icons and some improvements

License:        GPLv3
URL:            https://github.com/kukuruzka165/materialgram

%description
Telegram Desktop fork with Material Design and other improvements, which is based on the Telegram API and the MTProto secure protocol.

%prep
cd %{_sourcedir}/

%build

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/dbus-1
mkdir -p %{buildroot}/usr/share/icons
mkdir -p %{buildroot}/usr/share/metainfo

cp -a %{_sourcedir}/usr/bin/materialgram %{buildroot}/usr/bin/

cp -a %{_sourcedir}/usr/share/* %{buildroot}/usr/share/

%files
/usr/bin/materialgram
%dir /usr/share/applications
/usr/share/applications/*
%dir /usr/share/dbus-1
/usr/share/dbus-1/*
%dir /usr/share/icons
/usr/share/icons/*
%dir /usr/share/metainfo
/usr/share/metainfo/*

%postun
if [ "$1" = 0 ]; then
  rm -rf $HOME/.local/share/materialgram
fi

%changelog
* Sat Nov 06 2024 burhanverse <burhanverse@proton.me> - 5.7.0.1-4
- Add GPG verification
- Release RPM package
