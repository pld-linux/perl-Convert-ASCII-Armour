%include	/usr/lib/rpm/macros.perl
Summary:	Convert-ASCII-Armour perl module
Summary(pl):	Modu� perla Convert-ASCII-Armour
Name:		perl-Convert-ASCII-Armour
Version:	1.4
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-ASCII-Armour-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::ASCII::Armor - Convert binary octets into ASCII armoured messages.

%prep
%setup -q -n Convert-ASCII-Armour-%{version}

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
%{perl_sitelib}/Convert/ASCII/*.pm
