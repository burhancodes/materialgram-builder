Name:           materialgram
Version:        5.7.0.1
Release:        2%{?dist}
Summary:        Telegram Desktop fork with material icons and some improvements

License:        GPLv3
URL:            https://github.com/kukuruzka165/materialgram

%description
Telegram Desktop fork with Material Design and other improvements, which is based on the Telegram API and the MTProto secure protocol.

%prep
cd %{_sourcedir}/

%build
# (Add any build commands here if required)

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/dbus-1
mkdir -p %{buildroot}/usr/share/icons
mkdir -p %{buildroot}/usr/share/metainfo

# Copy the executable
cp -a %{_sourcedir}/usr/bin/materialgram %{buildroot}/usr/bin/

# Copy shared files
cp -a %{_sourcedir}/usr/share/* %{buildroot}/usr/share/

%files
/usr/bin/materialgram
/usr/share/applications/*
/usr/share/dbus-1/*
/usr/share/icons/*
/usr/share/metainfo/*

%changelog
* Sat Nov 02 2024 burhanverse <burhanverse@proton.me> - 5.7.0.1-2
- Initial RPM package
