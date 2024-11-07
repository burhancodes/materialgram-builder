Name:           materialgram
Version:        5.7.0.1
Release:        7%{?dist}
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

%preun
  pkill -f '/usr/bin/materialgram' || true

%postun
if [ "$1" = 0 ]; then
  # Only remove user data if the package is fully uninstalled (not upgraded)
  for userdir in /home/*; do
    if [ -d "$userdir/.local/share/materialgram" ]; then
      rm -rf "$userdir/.local/share/materialgram"
    fi
  done

  # Also check the current user's home, if $HOME is set
  if [ -n "$HOME" ] && [ -d "$HOME/.local/share/materialgram" ]; then
    rm -rf "$HOME/.local/share/materialgram"
  fi
fi

%changelog
* Thu Nov 07 2024 burhanverse <burhanverse@proton.me> - 5.7.0.1-7
- Release RPM package
