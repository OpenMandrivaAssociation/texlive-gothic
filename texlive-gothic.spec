Name:		texlive-gothic
Version:	20190130
Release:	1
Summary:	A collection of old German-style fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/gothic
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gothic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gothic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of fonts that reproduce those used in "old German"
printing. The set comprises Gothic, Schwabacher and Fraktur
fonts, a pair of handwriting fonts, Suetterlin and Schwell, and
a font containing decorative initials. In addition, there are
two re-encoding packages for Haralambous's fonts, providing T1,
using virtual fonts, and OT1 and T1, using Metafont.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/gothic
%{_texmfdistdir}/fonts/tfm/public/gothic
%doc %{_texmfdistdir}/doc/fonts/gothic

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
