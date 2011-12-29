# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/qsymbols
# catalog-date 2009-06-25 00:34:53 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-qsymbols
Version:	20090625
Release:	1
Summary:	Maths symbol abbreviations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qsymbols
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qsymbols.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qsymbols.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qsymbols.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides macros for defining systematic mnemonic abbreviations,
starting with ` for math symbols and \" for arrows, using
standard symbols as well as those from the amsfonts bundle and
the stmaryrd package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/qsymbols/qsymbols.sty
%doc %{_texmfdistdir}/doc/latex/qsymbols/CATALOG
%doc %{_texmfdistdir}/doc/latex/qsymbols/COPYING
%doc %{_texmfdistdir}/doc/latex/qsymbols/MANIFEST
%doc %{_texmfdistdir}/doc/latex/qsymbols/README
%doc %{_texmfdistdir}/doc/latex/qsymbols/qsymbols.pdf
%doc %{_texmfdistdir}/doc/latex/qsymbols/qsymbols.tex
#- source
%doc %{_texmfdistdir}/source/latex/qsymbols/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
