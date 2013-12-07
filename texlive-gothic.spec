# revision 15878
# category Package
# catalog-ctan /fonts/gothic
# catalog-date 2009-01-16 17:12:15 +0100
# catalog-license collection
# catalog-version undef
Name:		texlive-gothic
Version:	20090116
Release:	5
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
%{_texmfdistdir}/dvips/gothic/config.yfrak
%{_texmfdistdir}/fonts/afm/public/gothic/yfrak.afm
%{_texmfdistdir}/fonts/afm/public/gothic/ygoth.afm
%{_texmfdistdir}/fonts/afm/public/gothic/yswab.afm
%{_texmfdistdir}/fonts/map/dvips/gothic/yfrak.map
%{_texmfdistdir}/fonts/source/public/gothic/cmfrabase.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfrak.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfraklow.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfrakmis.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfraknum.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfrakoth.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfrakupp.mf
%{_texmfdistdir}/fonts/source/public/gothic/schwell.mf
%{_texmfdistdir}/fonts/source/public/gothic/su-lig.mf
%{_texmfdistdir}/fonts/source/public/gothic/su-low.mf
%{_texmfdistdir}/fonts/source/public/gothic/su-spec.mf
%{_texmfdistdir}/fonts/source/public/gothic/su-upp.mf
%{_texmfdistdir}/fonts/source/public/gothic/suet14.mf
%{_texmfdistdir}/fonts/source/public/gothic/xxfrak.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrabase.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrak.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfraklow.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrakmis.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfraknum.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrakoth.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrakupp.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygotbase.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygoth.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothgen.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothlig.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothlow.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothmis.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothnum.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothupp.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinit.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitA.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitB.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitC.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitD.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitE.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitF.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitG.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitH.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitJ.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitK.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitL.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitM.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitN.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitO.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitP.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitQ.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitR.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitS.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitT.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitU.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitV.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitW.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitX.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitY.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitZ.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitas.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitdd.mf
%{_texmfdistdir}/fonts/source/public/gothic/yintbase.mf
%{_texmfdistdir}/fonts/source/public/gothic/ysmfrak.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswab.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswabase.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswablow.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswabmis.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswabnum.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswabupp.mf
%{_texmfdistdir}/fonts/tfm/public/gothic/cmfrak.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/schwell.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/suet14.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/tfrak.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/tfrakls.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/tgoth.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/tswab.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/yfrak.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/ygoth.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/yinit.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/yinitas.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/yinitdd.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/yswab.tfm
%{_texmfdistdir}/fonts/type1/public/gothic/yfrak.pfb
%{_texmfdistdir}/fonts/type1/public/gothic/ygoth.pfb
%{_texmfdistdir}/fonts/type1/public/gothic/yswab.pfb
%{_texmfdistdir}/fonts/vf/public/gothic/tfrak.vf
%{_texmfdistdir}/fonts/vf/public/gothic/tfrakls.vf
%{_texmfdistdir}/fonts/vf/public/gothic/tgoth.vf
%{_texmfdistdir}/fonts/vf/public/gothic/tswab.vf
%doc %{_texmfdistdir}/doc/fonts/gothic/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090116-2
+ Revision: 752370
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090116-1
+ Revision: 718574
- texlive-gothic
- texlive-gothic
- texlive-gothic
- texlive-gothic

