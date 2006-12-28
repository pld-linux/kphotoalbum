# $Revision: 1.1 $
Summary:	Kphotoalbum
Summary(pl):	Kphotoalbu,
Name:		kphotoalbum
Version:	20061209noi18n
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://kphotoalbum.org/snapshots/%{name}-2006-12-09-noi18n.tar.gz
# Source0-md5:	aa00aa
Patch0:		%{name}-namespace.patch
URL:		http://kphotoalbum.org/
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPhotoAlbum is a tool which you can use to easily sort your images. It provides many functionalities to sort them and find them easily.

%description -l pl
Program do opisywania i wyszukiwania zdjec.

%prep
%setup -q -n %{name}-2006-12-09-noi18n
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}
