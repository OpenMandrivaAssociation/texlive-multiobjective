%global tl_name multiobjective
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Symbols for multiobjective optimisation etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multiobjective
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiobjective.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a series of operators commonly used in papers
related to multiobjective optimisation, multiobjective evolutionary
algorithms, multicriteria decision making and similar fields.

