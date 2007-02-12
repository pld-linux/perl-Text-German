#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	German
Summary:	Text::German - German grundform reduction
Summary(pl.UTF-8):   Text::German - redukcja niemieckich "Grundformen"
Name:		perl-Text-German
Version:	0.06
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9e968525f7385c80d636a4ba68d27bf4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a rather incomplete implementaion of work done by Gudrun
Putze-Meier <gudrun.pm@t-online.de>. I have to confess that I never
read her original paper. So all credit belongs to her, all bugs are
mine. I tried to get some insight from an implementation of two
students of mine. They remain anonymous because their work was the
worst piece of code I ever saw. My code behaves mostly as their
implementation did except it is about 75 times faster.

%description -l pl.UTF-8
To jest raczej niepełna implementacja pracy autorstwa Gudrun
Putze-Meier <gudrun.pm@t-online.de>. Autor modułu przyznaje, że nigdy
nie czytał jej oryginalnego artykułu, więc cały zaszczyt przysługuje
jej, a błędy autorowi modułu. Autor próbował korzystać z implementacji
swoich dwóch studentów, którzy pozostaną anonimowi, ponieważ ich praca
była najgorszym kawałkiem kodu, jaki widział autor. Ten kod zachowuje
się w większości tak, jak implementacja studentów, ale jest około 75
razy szybszy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Text/German.pm
%{perl_vendorlib}/Text/German
%{_mandir}/man3/*
