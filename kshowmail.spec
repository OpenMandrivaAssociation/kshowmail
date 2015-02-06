Summary:	Show and delete mail on pop3 servers
Name:		kshowmail
Version:	4.1
Release:	3
License:	GPLv2+
Group:		Networking/Mail
Url:		http://sourceforge.net/projects/kshowmail
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel

%description
KShowmail is a KDE utility to show headers or the complete mails on pop3
servers without transferring them to the local mail client. Unpleasant mails
can be deleted on the server. The information can be refreshed via timers.

%files -f %{name}.lang
%{_bindir}/kshowmail
%{_libdir}/kde4/kcm_kshowmailconfig*
%{_datadir}/applications/kde4/kshowmail.desktop
%{_datadir}/apps/kshowmail
%{_datadir}/icons/hicolor/*/apps/kshowmail.png
%{_datadir}/kde4/services/kshowmailconfig*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

