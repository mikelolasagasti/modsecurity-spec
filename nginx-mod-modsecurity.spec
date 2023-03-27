%global nginx_modname modsecurity
%global origname nginx-module-%{nginx_modname}
%global path ModSecurity-nginx

Name:           nginx-mod-modsecurity
Version:        1.0.3
Release:        %autorelease
Summary:        Nginx modsecurity

License:        Apache2
URL:            https://github.com/SpiderLabs/ModSecurity-nginx
Source0:        %{url}/archive/v%{version}/%{origname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  nginx-mod-devel
BuildRequires:  libmodsecurity-devel

Suggest:        mod_security_crs

%description
%{summary}.

%prep
%autosetup -n %{path}-%{version}


%build
%nginx_modconfigure
%nginx_modbuild


%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_modsecurity_module.so %{buildroot}%{nginx_moddir}
install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_modsecurity_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-modsecurity.conf
popd


%files
%license LICENSE
%doc README.md
%{nginx_moddir}/ngx_http_modsecurity_module.so
%{nginx_modconfdir}/mod-modsecurity.conf


%changelog
%autochangelog
