%global tl_name nth
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Generate English ordinal numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/misc/nth.sty
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nth.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The command \nth{<number>} generates English ordinal numbers of the form
1st, 2nd, 3rd, 4th, etc. LaTeX package options may specify that the
ordinal mark be superscripted, and that negative numbers may be treated;
Plain TeX users have no access to package options, so need to redefine
macros for these changes.

