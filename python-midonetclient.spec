%global srcvendor  MidoNet
%global srcname midonetclient

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{srcname}
Version:        XXX
Release:        XXX
Summary:        %{srcvendor} CLI

# midonet-cli is GPLv3 licensed, the rest ASL 2.0
License:        ASL 2.0 and GPLv3
URL:            https://www.midonet.org/
Source0:        https://github.com/midonet/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       python-httplib2
Requires:       python-webob

%description
%{srcvendor} Command Line Interface

%prep
%setup -q -n %{name}-%{upstream_version}

%build
%{__python2} setup.py build

%install
PBR_VERSION="%{version}" SKIP_PIP_INSTALL=1 %{__python2} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE LICENSE.mn-ctl
%doc README
%{python2_sitelib}/midonetclient
%{python2_sitelib}/midonetclient-*-py%{python2_version}.egg-info
%{_bindir}/midonet-cli

%changelog
