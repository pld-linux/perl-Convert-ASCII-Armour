#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	ASCII-Armour
Summary:	Convert::ASCII::Armour - convert binary octets into ASCII armoured messages
Summary(pl):	Convert::ASCII::Armour - konwersja binarnych danych na komunikaty kodowane w ASCII
Name:		perl-Convert-ASCII-Armour
Version:	1.4
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e0e61ff6b014062d6feecaea3f09018
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MIME-Base64
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::ASCII::Armor Perl module converts hashes of binary octets
into ASCII messages suitable for transfer over 6-bit clean transport
channels. The encoded ASCII resembles PGP's armoured messages, but are
in no way compatible with PGP.

%description -l pl
Modu³ Perla Convert::ASCII::Armor konwertuje hashe z binarnymi danymi
na komunikaty kodowane w ASCII, odpowiednie dla transmisji poprzez
6-bitowe kana³y transportowe. Zakodowane ASCII jest podobne do
komunikatów szyfrowanych PGP, lecz nie jest w ¿aden sposów zgodne z
PGP.

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
%dir %{perl_vendorlib}/Convert/ASCII
%{perl_vendorlib}/Convert/ASCII/*.pm
%{_mandir}/man3/*
