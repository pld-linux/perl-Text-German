%include	/usr/lib/rpm/macros.perl
Summary:	Text-German perl module
Summary(pl):	Modu³ perla Text-German
Name:		perl-Text-German
Version:	0.03
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-German-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-German perl module.

%description -l pl
Modu³ perla Text-German.

%prep
%setup -q -n Text-German-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/German.pm
%{perl_sitelib}/Text/German
%{_mandir}/man3/*
