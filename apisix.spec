%ifarch loongarch64
%global __requires_exclude ^libwasmtime\\.so.*$
%endif

Name:           apisix
Version:       3.9.1 
Release:        2%{?dist}
Summary:        Apache APISIX is a distributed gateway for APIs and Microservices, focused on high performance and reliability.

License:        ASL 2.0
URL:            http://apisix.apache.org/
#Source0:        

#BuildRequires:  
Requires: openldap-devel
Requires: pcre
Requires: which
#Requires: file

%description
Apache APISIX is a distributed gateway for APIs and Microservices, focused on high performance and reliability.

#prep
#%autosetup


#build
#%configure
#%make_build


%install
#%make_install
mkdir -p %{buildroot}
cp -r /tmp/build/output/apisix/usr %{buildroot}
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp -r /usr/lib/systemd/system/apisix.service %{buildroot}/usr/lib/systemd/system/
cp -r /usr/lib/systemd/system/openresty.service %{buildroot}/usr/lib/systemd/system/
#cp -r /usr/local/apisix/conf/config.yaml %{buildroot}
#cp -r /usr/local/apisix/conf/config-default.yaml %{buildroot}

%files
/usr/bin/apisix
/usr/local/apisix
/usr/local/openresty
/usr/lib/systemd/system/apisix.service
/usr/lib/systemd/system/openresty.service
#/usr/local/apisix/conf/config.yaml
#/usr/local/apisix/conf/config-default.yaml


%changelog
* Wed Mar 18 2026 Wenlong Zhang <zhangwenlong@loongson.cn>
- init

