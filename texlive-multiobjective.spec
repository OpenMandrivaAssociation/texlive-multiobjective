# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/multiobjective
# catalog-date 2008-09-09 11:27:07 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-multiobjective
Version:	1.0
Release:	8
Summary:	Symbols for multibojective optimisation etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multiobjective
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754223
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719086
- texlive-multiobjective
- texlive-multiobjective
- texlive-multiobjective
- texlive-multiobjective

