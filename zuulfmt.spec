%global         sum A Zuul/Ansible yaml formatter/prettifier.

Name:           zuulfmt
Version:        0.1.0
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://docs.softwarefactory-project.io/%{name}
Source0:        https://tarballs.softwarefactory-project.io/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Buildrequires:  python3-devel

Requires:       python3

%description
%{sum}

%prep
%autosetup -n zuulfmt-%{version}

%build
PBR_VERSION=%{version} %{__python3} setup.py build

%install
PBR_VERSION=%{version} %{__python3} setup.py install --skip-build --root %{buildroot}

%files
%{python3_sitelib}/*
%{_bindir}/*

%changelog
* Tue Jan  5 2021 Tristan Cacqueray <tdecacqu@redhat.com> - 0.1.0-1
- Initial packaging
