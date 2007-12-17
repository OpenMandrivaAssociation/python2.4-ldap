%define name    python2.4-ldap
%define modname python-ldap
%define version 2.3.1
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Python 2.4 LDAP bindings
Source0: 	%{modname}-%{version}.tar.gz
License:	Modified CNRI Open Source License
Group: 		Development/Python
Url: 		http://python-ldap.sourceforge.net/
BuildRequires:	openldap-devel >= 2.3
BuildRequires:	python2.4-devel
Requires:	    python2.4

%description
python-ldap provides an object-oriented API to access LDAP directory 
servers from Python programs. Mainly it wraps the OpenLDAP 2.x libs 
for that purpose.

Additionally the package contains modules for other LDAP-related stuff 
(e.g. processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%prep
%setup -q -n %modname-%version
perl -pi -e 's,^(library_dirs.*=).*,$1,g' setup.cfg
chmod a+r -R .

%build
export CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/sasl"
python2.4 setup.py build

%install
rm -Rf %{buildroot}
python2.4 setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc CHANGES README INSTALL TODO Demo/

