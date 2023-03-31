%define modname	Proc-WaitStat
%define modver	1.00

Summary:	Proc::WaitStat - Interpret and act on wait() status values
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	20
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Proc/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(IPC::Signal)
BuildRequires:	perl-devel

%description
This module contains functions for interpreting and acting on wait
status values.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Proc/WaitStat.pm
%{_mandir}/man3/*

