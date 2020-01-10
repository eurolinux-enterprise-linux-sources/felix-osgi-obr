%global bundle org.osgi.service.obr

Name:           felix-osgi-obr
Version:        1.0.2
Release:        12%{?dist}
Summary:        Felix OSGi OBR Service API

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://felix.apache.org/site/apache-felix-osgi-bundle-repository.html
Source0:        http://www.apache.org/dist/felix/org.osgi.service.obr-%{version}-project.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  felix-osgi-core
BuildRequires:  felix-parent

%description
OSGi OBR Service API.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file : felix/%{bundle}.jar

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.2-12
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 1.0.2-11
- Migrate away from mvn-rpmbuild (Resolves: #997510)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-10
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.2-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Sep  4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-7
- Install LICENSE and NOTICE with javadoc package
- Build with maven
- Move POM file to _mavenpomdir from _datadir/maven2/poms
- Update to current packaging guidelines
- Add missing R: java, jpackage-utils

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.2-3
- Fix pom name.
- Adapt to current guidelines.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1.0.2-2
- Fix line length.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1.0.2-1
- Initial package.
