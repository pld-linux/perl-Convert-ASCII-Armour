#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	ASCII-Armour
Summary:	Convert::ASCII::Armour Perl module
Summary(cs):	Modul Convert::ASCII::Armour pro Perl
Summary(da):	Perlmodul Convert::ASCII::Armour
Summary(de):	Convert::ASCII::Armour Perl Modul
Summary(es):	Módulo de Perl Convert::ASCII::Armour
Summary(fr):	Module Perl Convert::ASCII::Armour
Summary(it):	Modulo di Perl Convert::ASCII::Armour
Summary(ja):	Convert::ASCII::Armour Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Convert::ASCII::Armour ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Convert::ASCII::Armour
Summary(pl):	Modu³ Perla Convert::ASCII::Armour
Summary(pt):	Módulo de Perl Convert::ASCII::Armour
Summary(pt_BR):	Módulo Perl Convert::ASCII::Armour
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Convert::ASCII::Armour
Summary(sv):	Convert::ASCII::Armour Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Convert::ASCII::Armour
Summary(zh_CN):	Convert::ASCII::Armour Perl Ä£¿é
Name:		perl-Convert-ASCII-Armour
Version:	1.4
Release:	9
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
%if 0%{!?_without_tests:1}
BuildRequires:        perl-Compress-Zlib
BuildRequires:        perl-Digest-MD5
BuildRequires:        perl-MIME-Base64
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::ASCII::Armor - Convert binary octets into ASCII armoured
messages.

%description -l pl
Convert::ASCII::Armor - konwertuje binarne dane na wiadomo¶ci kodowane
w ASCII.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_sitelib}/Convert/ASCII
%{perl_sitelib}/Convert/ASCII/*.pm
%{_mandir}/man3/*
