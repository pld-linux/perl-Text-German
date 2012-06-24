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
To jest raczej niepe�na implementacja pracy autorstwa Gudrun
Putze-Meier <gudrun.pm@t-online.de>. Autor modu�u przyznaje, �e nigdy
nie czyta� jej oryginalnego artyku�u, wi�c ca�y zaszczyt przys�uguje
jej, a b��dy autorowi modu�u. Autor pr�bowa� korzysta� z implementacji
swoich dw�ch student�w, kt�rzy pozostan� anonimowi, poniewa� ich praca
by�a najgorszym kawa�kiem kodu, jaki widzia� autor. Ten kod zachowuje
si� w wi�kszo�ci tak, jak implementacja student�w, ale jest oko�o 75
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
