# TODO:
# - package EMACS Lisp files
#
Summary:	A simple literate programming tool
Summary(pl.UTF-8):	Proste narzędzie do programowania literackiego
Name:		noweb
Version:	2.11b
Release:	0.1
License:	distributable
Group:		Applications
Source0:	ftp://www.eecs.harvard.edu/pub/nr/%{name}.tgz
# Source0-md5:	1df580723497b2f2efde07646abf764c
Patch0:		%{name}-makefile-destdir.patch
URL:		http://www.cs.tufts.edu/~nr/noweb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
noweb is designed to meet the needs of literate programmers while
remaining as simple as possible.

%description -l pl.UTF-8
noweb jest najprostszym możliwym narzędziem służącym do programowania
literackiego.

%prep
%setup -q

%patch0 -p1

%build
cd src
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd src
# XXX Where to put .el files?
# ELISP=???
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BIN=%{_bindir} \
	LIB=%{_libdir}/noweb \
	MAN=%{_mandir} \
	TEXINPUTS=%{_datadir}/texmf/noweb

%files
%defattr(644,root,root,755)
%doc src/{COPYRIGHT,FAQ,FAQ.html,README,VERSIONS}
%attr(755,root,root) %{_bindir}/cpif
%attr(755,root,root) %{_bindir}/htmltoc
%attr(755,root,root) %{_bindir}/nodefs
%attr(755,root,root) %{_bindir}/noindex
%attr(755,root,root) %{_bindir}/noroff
%attr(755,root,root) %{_bindir}/noroots
%attr(755,root,root) %{_bindir}/notangle
%attr(755,root,root) %{_bindir}/nountangle
%attr(755,root,root) %{_bindir}/noweave
%attr(755,root,root) %{_bindir}/noweb
%attr(755,root,root) %{_bindir}/nuweb2noweb

%{_libdir}/noweb

%{_mandir}/man1/cpif.1*
%{_mandir}/man1/htmltoc.1*
%{_mandir}/man1/nodefs.1*
%{_mandir}/man1/noindex.1*
%{_mandir}/man1/noroff.1*
%{_mandir}/man1/noroots.1*
%{_mandir}/man1/notangle.1*
%{_mandir}/man1/nountangle.1*
%{_mandir}/man1/noweave.1*
%{_mandir}/man1/noweb.1*
%{_mandir}/man1/nuweb2noweb.1*
%{_mandir}/man1/sl2h.1*
%{_mandir}/man7/nowebfilters.7*
%{_mandir}/man7/nowebstyle.7*

%{_datadir}/texmf/noweb


%clean
rm -rf $RPM_BUILD_ROOT
