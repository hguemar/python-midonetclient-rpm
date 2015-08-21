%global vendor  MidoNet
%global srcname midonetclient

Name:           %{srcname}
Version:        XXX
Release:        XXX
Summary:        %{vendor} MidoNet CLI

License:        ASL 2.0
URL:            https://www.midonet.org/
Source0:        https://github.com/midonet/python-%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       python-httplib2
Requires:       python-webob

%description
This package provides %{vendor} Command Line Interface

%prep
%setup -q -n %{srcname}-%{upstream_version}

%build
%{__python2} setup.py build

%install
PBR_VERSION="%{version}" SKIP_PIP_INSTALL=1 %{__python2} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{python2_sitelib}/midonetclient
%{python2_sitelib}/midonetclient-%{version}-py%{python2_version}.egg-info

%changelog
