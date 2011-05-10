Name:		shtool
Version:	2.0.8
Release:	7
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

