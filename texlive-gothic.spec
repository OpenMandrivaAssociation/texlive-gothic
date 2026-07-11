%global tl_name gothic
%global tl_revision 49869

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A collection of old German-style fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gothic
License:	collection
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gothic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gothic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gothic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of fonts that reproduce those used in "old German" printing
and handwriting. The set comprises Gothic, Schwabacher and Fraktur
fonts, a pair of handwriting fonts, Sutterlin and Schwell, and a font
containing decorative initials. In addition, there are two re-encoding
packages for Haralambous's fonts, providing T1, using virtual fonts, and
OT1 and T1, using Metafont.

