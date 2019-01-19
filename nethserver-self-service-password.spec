Summary: NethServer configuration for self-service-password
%define name nethserver-self-service-password
%define version 0.1
%define release 1
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools
Requires: self-service-password
Requires: nethserver-httpd-virtualhosts
Requires: nethserver-rh-php71-php-fpm
#AutoReq: no

%description
NethServer configuration for self-service-password
(https://ltb-project.org/documentation/self-service-password)

%prep
%setup

%post
%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} %{buildroot} $RPM_BUILD_ROOT > default.lst

%clean
rm -rf $RPM_BUILD_ROOT

%files -f default.lst
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Jan 19 2019 Dan Brown <dan@familybrown.org> - 0.1-1.el7
- Initial release
