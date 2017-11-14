#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bndl-lamp-basic
Version  : 1.3
Release  : 12
URL      : http://localhost/cgit/projects/bndl-lamp-basic/snapshot/bndl-lamp-basic-1.3.tar.gz
Source0  : http://localhost/cgit/projects/bndl-lamp-basic/snapshot/bndl-lamp-basic-1.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: bndl-lamp-basic-autostart
Requires: bndl-lamp-basic-config

%description
No detailed description available

%package autostart
Summary: autostart components for the bndl-lamp-basic package.
Group: Default

%description autostart
autostart components for the bndl-lamp-basic package.


%package config
Summary: config components for the bndl-lamp-basic package.
Group: Default

%description config
config components for the bndl-lamp-basic package.


%prep
%setup -q -n bndl-lamp-basic-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510692086
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1510692086
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/httpd.service
/usr/lib/systemd/system/multi-user.target.wants/php-fpm.service

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/httpd.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/php-fpm.service
