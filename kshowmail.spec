%define	name	kshowmail
%define	version	4.1
%define	release	%mkrel	1

Name:		kshowmail
Summary:	Show and delete mail on pop3 servers
Version:	4.1
Release:	1
Url:		http://sourceforge.net/projects/kshowmail
License:	GPLv2+
Group:		Networking/Mail
Source0:	%{name}-%{version}.tar.gz
Provides:       %{name} = %{version}-%{release}

BuildRequires:  kdelibs4-devel
BuildRequires:  kdenetwork4-devel
BuildRequires:  kdepim4-devel

%description
KShowmail is a KDE utility to show headers or the complete mails on pop3
servers without transferring them to the local mail client. Unpleasant mails
can be deleted on the server. The information can be refreshed via timers.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
cd build
%{makeinstall_std}
kbuildsycoca4
cd -
%find_lang %name

%files -f %{name}.lang
%{_bindir}/kshowmail
%{_libdir}/kde4/kcm_kshowmailconfig*
%{_datadir}/applications/kde4/kshowmail.desktop
%{_datadir}/apps/kshowmail
%doc %{_docdir}/HTML/*/kshowmail/*
%{_datadir}/icons/hicolor/*/apps/kshowmail.png
%{_datadir}/kde4/services/kshowmailconfig*

%clean

