Name:		texlive-multiobjective
Version:	15878
Release:	1
Summary:	Symbols for multibojective optimisation etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multiobjective
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a series of operators commonly used in
papers related to multiobjective optimisation, multiobjective
evolutionary algorithms, multicriteria decision making and
similar fields.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/multiobjective/multiobjective.sty
%doc %{_texmfdistdir}/doc/latex/multiobjective/README
%doc %{_texmfdistdir}/doc/latex/multiobjective/multiobjective.pdf
#- source
%doc %{_texmfdistdir}/source/latex/multiobjective/multiobjective.dtx
%doc %{_texmfdistdir}/source/latex/multiobjective/multiobjective.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
