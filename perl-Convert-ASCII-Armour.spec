%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	ASCII-Armour
Summary:	Convert::ASCII::Armour perl module
Summary(pl):	Modu³ perla Convert::ASCII::Armour
Name:		perl-Convert-ASCII-Armour
Version:	1.4
Release:	7
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}

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
