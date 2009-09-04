%define module Proc-WaitStat

Summary:	Proc::WaitStat - Interpret and act on wait() status values
Name:		perl-%{module}
Version:	1.00
Release:	%mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~rosch/Proc-WaitStat/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RO/ROSCH/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-IPC-Signal
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module contains functions for interpreting and acting on wait
status values.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Proc/WaitStat.pm
%{_mandir}/*/*


