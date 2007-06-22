Summary:	KPhotoAlbum - tool to sort your images
Summary(pl.UTF-8):	Kphotoalbum - narzędzie do porządkowania zdjęć
Name:		kphotoalbum
Version:	3.0.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://kphotoalbum.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	ef4dfbe3dca4fe8162ce2183e795635c
URL:		http://kphotoalbum.org/
BuildRequires:	kdelibs-devel
BuildRequires:	libkipi-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPhotoAlbum is a tool which you can use to easily sort your images. It
provides many functionalities to sort them and find them easily.

%description -l pl.UTF-8
KPhotoAlbum jest narzędziem, którym można w prosty sposób porządkować
zdjęcia. Dostarcza wiele możliwości do sortowania i szukania ich w
prosty sposób.

%prep
%setup -q

%build
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kphotoalbum
%{_datadir}/apps/kphotoalbum
%{_datadir}/config/kphotoalbumrc
%{_desktopdir}/kde/kphotoalbum-import.desktop
%{_desktopdir}/kde/kphotoalbum.desktop
%{_iconsdir}/hicolor/*/apps/kphotoalbum.png
%{_datadir}/mimelnk/application/x-vnd.kde.kphotoalbum-import.desktop
