#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SVG
Summary:	perl extension to generate SVG images
Summary(pl):	rozszerzenie perla do generowania obrazow SVG
Name:		perl-SVG
Version:	2.27
Release:	1
License:	Perl license
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	d7af31798b18927ff1e569a1e2d3a7e6
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVG.pm is a perl extention to generate stand-alone or inline SVG
(scaleable vector graphics) images using the W3C SVG xml
recommendation.

%prep
%setup -q -n %{pdir}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
# if module isn't noarch, use:
# %{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
