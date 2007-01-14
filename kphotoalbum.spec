# $Revision: 1.4 $
%define		_snap	2006-12-09
%define		_rel	0.1
Summary:	Kphotoalbum
Summary(pl):	Kphotoalbum
Name:		kphotoalbum
Version:	3.0
Release:	0.%(echo %{_snap} | tr -d -).%{_rel}
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://kphotoalbum.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	c6989033ebb5d221aaa55e0d58cef0b1
#Source0:	http://kphotoalbum.org/snapshots/%{name}-%{_snap}-noi18n.tar.gz
URL:		http://kphotoalbum.org/
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPhotoAlbum is a tool which you can use to easily sort your images. It
provides many functionalities to sort them and find them easily.

%description -l pl
KPhotoAlbum jest narz�dziem, kt�rem mo�esz w prosty spos�b sortowa�
twoje obrazy. Dostarcza wiele mo�liwo�ci do sortowania i szukania ich
w prosty spos�b.

%prep
#%setup -q -n %{name}-%{_snap}-noi18n
%setup -q 

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
