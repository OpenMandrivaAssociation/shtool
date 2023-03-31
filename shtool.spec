Name:		shtool
Version:	2.0.8
Release:	11
Summary:	Portable shell tool
Group:		Shells
License:	GPLv2+
URL:		http://www.gnu.org/software/shtool/
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
GNU shtool is a compilation of small but very stable and portable
shell scripts into a single shell tool. All ingredients were in
successful use over many years in various free software projects.
The compiled shtool program is intended to be used inside the source
tree of other free software packages. There it can overtake various
(usually non-portable) tasks related to the building and installation
of such a package. It especially can replace the old mkdir.sh,
install.sh and related scripts. 

%prep
%setup -q

%build
%configure
%make

%check
make check

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS RATIONAL README THANKS VERSION
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}
%{_bindir}/%{name}ize
%{_datadir}/%{name}/
%{_datadir}/aclocal/%{name}.m4



%changelog
* Tue May 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0.8-7
+ Revision: 673277
- imported package shtool


* Tue May 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0.8-7
- first mandriva release, imported and adapted from Fedora

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Fabian Affolter <fabian@bernewireless.net> - 2.0.8-5
- Rebuilt

* Sat Feb 27 2010 Fabian Affolter <fabian@bernewireless.net> - 2.0.8-4
- Rebuilt

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 08 2009 Fabian Affolter <fabian@bernewireless.net> - 2.0.8-2
- Added test suite

* Sat Dec 27 2008 Fabian Affolter <fabian@bernewireless.net> - 2.0.8-1
- Initial spec for Fedora
