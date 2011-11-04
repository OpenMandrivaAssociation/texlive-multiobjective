# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/multiobjective
# catalog-date 2008-09-09 11:27:07 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-multiobjective
Version:	1.0
Release:	1
Summary:	Symbols for multibojective optimisation etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multiobjective
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a series of operators commonly used in
papers related to multiobjective optimisation, multiobjective
evolutionary algorithms, multicriteria decision making and
similar fields.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/multiobjective/multiobjective.sty
%doc %{_texmfdistdir}/doc/latex/multiobjective/README
%doc %{_texmfdistdir}/doc/latex/multiobjective/multiobjective.pdf
#- source
%doc %{_texmfdistdir}/source/latex/multiobjective/multiobjective.dtx
%doc %{_texmfdistdir}/source/latex/multiobjective/multiobjective.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
