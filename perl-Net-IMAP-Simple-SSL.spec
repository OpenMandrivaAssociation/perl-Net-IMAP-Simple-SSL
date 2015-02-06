%define realname Net-IMAP-Simple-SSL

Summary:	SSL support for Net::IMAP::Simple
Name:		perl-%{realname}
Version:	1.3
Release:	12
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{realname}-%{version}.tar.bz2

BuildRequires: perl-devel
BuildRequires: perl(IO::Socket::SSL)
Requires:	perl(Net::IMAP::Simple)
BuildArch:	noarch

%description
This module is a subclass of Net::IMAP::SImple that includes SSL support.
The interface is identical.

%prep
%setup -q -n %{realname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Net/IMAP/Simple/*
%{_mandir}/*/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3-9mdv2010.0
+ Revision: 430511
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.3-8mdv2009.0
+ Revision: 241774
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-6mdv2008.0
+ Revision: 90054
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.3-5mdv2008.0
+ Revision: 25275
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3-4mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.3-3mdk
- BuildRequires

* Tue May 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.3-2mdk
- Requires Net::IMAP::Simple (not found automatically)

* Tue May 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.3-1mdk
- First Mandriva release

