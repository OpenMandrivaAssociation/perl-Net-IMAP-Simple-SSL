%define realname Net-IMAP-Simple-SSL
%define name perl-%{realname}
%define version 1.3
%define release %mkrel 9

Summary:	SSL support for Net::IMAP::Simple
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{realname}-%{version}.tar.bz2
Requires:	perl(Net::IMAP::Simple)
%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
Buildrequires: perl(IO::Socket::SSL)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
This module is a subclass of Net::IMAP::SImple that includes SSL support.
The interface is identical.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Net/IMAP/Simple/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

