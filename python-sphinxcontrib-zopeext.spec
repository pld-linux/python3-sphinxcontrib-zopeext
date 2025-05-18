Summary:	Sphinx extension zopeext
Summary(pl.UTF-8):	Rozszerzenie Sphinksa zopeext
Name:		python-sphinxcontrib-zopeext
# keep 0.2.x here for python2 support
Version:	0.2.4
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-zopeext/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-zopeext/sphinxcontrib-zopeext-%{version}.tar.gz
# Source0-md5:	905dfe63cecc87f9005c46d4a88196fa
URL:		https://pypi.org/project/sphinxcontrib-zopeext/
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
Requires:	python-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the zopeext Sphinx extension. It provides some
support for Zope interfaces by providing an autointerface directive
that acts like autoclass except uses the Zope interface methods for
attribute and method lookup (the interface mechanism hides the
attributes and method so the usual autoclass directive fails.)
Interfaces are intended to be very different beasts than regular
python classes, and as a result require customized access to
documentation, signatures etc.

%description -l pl.UTF-8
Ten pakiet zawiera rozszerzenie Sphinksa, zapewniające pewną obsługę
interfejsów Zope poprzez udostępnienie dyrektywy autointerface,
zachowującą się jak autoclass z tym wyjątkiem, że wykorzystuje metody
interfejsu Zope do wyszukiwania atrybutów i metod (mechanizm
interfejsu ukrywa atrybuty i metody, więc zwykła dyrektywa autoclass
zawodzi). Interfejsy mają być zupełnie inne niż zwykłe klasy pythonowe
i w efekcie wymagają dostosowanego dostępu do dokumentacji, sygnatur
itp.

%prep
%setup -q -n sphinxcontrib-zopeext-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python-sphinxcontrib-zopeext-%{version}
%{__mv} $RPM_BUILD_ROOT%{py_sitescriptdir}/sphinxcontrib/zopeext/example.py $RPM_BUILD_ROOT%{_examplesdir}/python-sphinxcontrib-zopeext-%{version}
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/sphinxcontrib/zopeext/example.py[co]

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.rst
%{py_sitescriptdir}/sphinxcontrib/zopeext
%{py_sitescriptdir}/sphinxcontrib_zopeext-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_zopeext-%{version}-py*-nspkg.pth
%{_examplesdir}/python-sphinxcontrib-zopeext-%{version}
