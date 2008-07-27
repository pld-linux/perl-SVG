#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SVG
Summary:	Perl extension to generate SVG images
Summary(pl.UTF-8):	Rozszerzenie Perla do generowania obrazów SVG
Name:		perl-SVG
Version:	2.33
Release:	2
# same as perl (general perl license)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	80aff1f4d107bf56696653895e5eed81
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVG.pm is a Perl extention to generate stand-alone or inline SVG
(Scaleable Vector Graphics) images using the W3C SVG XML
recommendation.

%description -l pl.UTF-8
SVG.pm to rozszerzenie Perla do generowania samodzielnych lub
wbudowanych obrazów SVG (Scaleable Vector Graphics - skalowalna
grafika wektorowa) z użyciem rekomendacji SVG SML W3C.

%prep
%setup -q -n %{pdir}-%{version}

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
%doc Changes README
%{perl_vendorlib}/%{pdir}.pm
%{perl_vendorlib}/%{pdir}
%{_mandir}/man3/*
