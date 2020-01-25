#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Unicode
%define		pnam	Normalize
Summary:	Unicode::Normalize - Unicode Normalization Forms
Summary(pl.UTF-8):	Unicode::Normalize - postaci normalne Unikodu
Name:		perl-Unicode-Normalize
Version:	1.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff424cf19587097b838615346878731c
URL:		http://search.cpan.org/dist/Unicode-Normalize/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module to create Unicode Normalization Forms.

%description -l pl.UTF-8
Ten moduł Perla tworzy postaci normalne Unikodu (Unicode Normalization
Forms).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Unicode/Normalize.pm
%dir %{perl_vendorarch}/auto/Unicode/Normalize
%attr(755,root,root) %{perl_vendorarch}/auto/Unicode/Normalize/Normalize.so
%{_mandir}/man3/Unicode::Normalize.3pm*
