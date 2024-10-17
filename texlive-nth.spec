Name:		texlive-nth
Version:	54252
Release:	2
Summary:	Generate English ordinal numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nth
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nth.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The command \nth{<number>} generates English ordinal numbers of
the form 1st, 2nd, 3rd, 4th, etc. LaTeX package options may
specify that the ordinal mark be superscripted, and that
negative numbers may be treated; Plain TeX users have no access
to package options, so need to redefine macros for these
changes.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/nth

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
