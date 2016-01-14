%global pkg_name apache-resource-bundles
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global jar_version 1.4
%global lh_version 1.1
%global id_version 1.1

Name:		%{?scl_prefix}%{pkg_name}
Version:	2
Release:	11.9%{?dist}
Summary:	Apache Resource Bundles

License:	ASL 2.0
URL:		http://repo1.maven.org/maven2/org/apache/apache-resource-bundles/
Source0:	http://repo1.maven.org/maven2/org/apache/%{pkg_name}/%{version}/%{pkg_name}-%{version}.pom
Source1:	http://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/%{jar_version}/apache-jar-resource-bundle-%{jar_version}-sources.jar
Source2:	http://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/%{jar_version}/apache-jar-resource-bundle-%{jar_version}.pom
Source3:	http://repo1.maven.org/maven2/org/apache/apache-license-header-resource-bundle/%{lh_version}/apache-license-header-resource-bundle-%{lh_version}-sources.jar
Source4:	http://repo1.maven.org/maven2/org/apache/apache-license-header-resource-bundle/%{lh_version}/apache-license-header-resource-bundle-%{lh_version}.pom
Source5:	http://repo1.maven.org/maven2/org/apache/apache-incubator-disclaimer-resource-bundle/%{id_version}/apache-incubator-disclaimer-resource-bundle-%{id_version}-sources.jar
Source6:	http://repo1.maven.org/maven2/org/apache/apache-incubator-disclaimer-resource-bundle/%{id_version}/apache-incubator-disclaimer-resource-bundle-%{id_version}.pom

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}maven-compiler-plugin
BuildRequires:  %{?scl_prefix}maven-install-plugin
BuildRequires:  %{?scl_prefix}maven-jar-plugin
BuildRequires:  %{?scl_prefix}maven-remote-resources-plugin
BuildRequires:  %{?scl_prefix}maven-resources-plugin
BuildRequires:  %{?scl_prefix}maven-surefire-plugin
BuildRequires:  %{?scl_prefix}maven-site-plugin

BuildArch:	noarch

%description
An archive which contains templates for generating the necessary license files
and notices for all Apache releases.

%prep
%setup -c -T -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp %SOURCE0 ./pom.xml

# jar
mkdir -p apache-jar-resource-bundle
pushd apache-jar-resource-bundle
jar xvf %SOURCE1
cp %SOURCE2 ./pom.xml
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

# license-header
mkdir -p apache-license-header-resource-bundle
pushd apache-license-header-resource-bundle
jar xvf %SOURCE3
cp %SOURCE4 ./pom.xml
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

# incubator-disclaimer
mkdir -p apache-incubator-disclaimer-resource-bundle
pushd apache-incubator-disclaimer-resource-bundle
jar xvf %SOURCE5
cp %SOURCE6 ./pom.xml
mkdir -p src/main/resources
mv META-INF src/main/resources
popd
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file :apache-jar-resource-bundle apache-resource-bundles/jar
%mvn_file :apache-license-header-resource-bundle apache-resource-bundles/license-header
%mvn_file :apache-incubator-disclaimer-resource-bundle apache-resource-bundles/incubator-disclaimer
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%{_javadir}/%{pkg_name}

%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-11.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2-11.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2-11.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-11.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-11.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-11.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 2-11.3
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2-11
- Mass rebuild 2013-12-27

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 2-9
- Build with xmvn

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2-5
- Fix pom file names and add_to_maven_depmap calls (Resolves rhbz#655790)

* Wed Sep 8 2010 Alexander Kurtakov <akurtako@redhat.com> 2-4
- Add maven-site-plugin BR.
- Use newer names of maven plugins.

* Mon Feb  1 2010 Mary Ellen Foster <mefoster at gmail.com> 2-3
- Fix license 

* Tue Jan 19 2010 Mary Ellen Foster <mefoster at gmail.com> 2-2
- Add plugin dependencies from POMs
- Fix description
- Remove maven-release plugin (not on Fedora yet)

* Mon Jan 18 2010 Mary Ellen Foster <mefoster at gmail.com> 2-1
- Initial package
