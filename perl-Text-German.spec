%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	German
Summary:	Text::German - German grundform reduction
Name:		perl-Text-German
Version:	0.03
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a rather incomplete implementaion of work done by Gudrun
Putze-Meier <gudrun.pm@t-online.de>. I have to confess that I never read
her original paper. So all credit belongs to her, all bugs are mine. I
tried to get some insight from an implementation of two students of
mine. They remain anonymous because their work was the wost piece of
code I ever saw. My code behaves mostly as their implementation did
except it is about 75 times faster.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Text/German.pm
%{perl_sitelib}/Text/German
%{_mandir}/man3/*
