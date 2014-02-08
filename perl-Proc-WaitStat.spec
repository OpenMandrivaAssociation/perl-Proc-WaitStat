%define upstream_name    Proc-WaitStat
%define upstream_version 1.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    9

Summary:	Proc::WaitStat - Interpret and act on wait() status values
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Proc/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(IPC::Signal)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
This module contains functions for interpreting and acting on wait
status values.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Proc/WaitStat.pm
%{_mandir}/*/*


%changelog
* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-6mdv2010.1
+ Revision: 505012
- tighten spec file

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.00-5mdv2010.0
+ Revision: 430531
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.00-4mdv2009.0
+ Revision: 258277
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.00-3mdv2009.0
+ Revision: 246338
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.00-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdv2007.0
+ Revision: 131202
- Import perl-Proc-WaitStat

* Wed Feb 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdk
- initial Mandriva package

