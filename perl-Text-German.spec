%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	German
Summary:	Text::German - German grundform reduction
Summary(pl):	Text::German - redukcja niemieckich "Grundformen"
Name:		perl-Text-German
Version:	0.03
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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

%description -l pl
To jest raczej niepe³na implementacja pracy autorstwa Gudrun
Putze-Meier <gudrun.pm@t-online.de>. Autor modu³u przyznaje, ¿e nigdy
nie czyta³ jej oryginalnego artyku³u, wiêc ca³y zaszczyt przys³uguje
jej, a b³êdy autorowi modu³u. Autor próbowa³ korzystaæ z implementacji
swoich dwóch studentów, którzy pozostan± anonimowi, poniewa¿ ich praca
by³a najgorszym kawa³kiem kodu, jaki widzia³ autor. Ten kod zachowuje
siê w wiêkszo¶ci tak, jak implementacja studentów, ale jest oko³o 75
razy szybszy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
