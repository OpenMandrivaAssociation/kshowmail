Name:		kshowmail
Summary:	Show and delete mail on pop3 servers
Version:	4.1
Release:	1
Url:		http://sourceforge.net/projects/kshowmail
License:	GPLv2+
Group:		Networking/Mail
Source0:	%{name}-%{version}.tar.gz

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
%makeinstall_std
kbuildsycoca4
cd -
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/kshowmail
%{_libdir}/kde4/kcm_kshowmailconfig*
%{_datadir}/applications/kde4/kshowmail.desktop
%{_datadir}/apps/kshowmail
%doc %{_docdir}/HTML/*/kshowmail/*
%{_datadir}/icons/hicolor/*/apps/kshowmail.png
%{_datadir}/kde4/services/kshowmailconfig*


%changelog
* Tue Jul 12 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.1-1
+ Revision: 689717
- remove useless junk

  + Johnny A. Solbu <solbu@mandriva.org>
    - New version
    - Spec cleanup

  + Eugeni Dodonov <eugeni@mandriva.com>
    - Imported to cooker.
    - Created package structure for kshowmail.


* Fri Sep 01 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-09-01 15:03:09 (59335)
- Rebuild

* Thu Aug 03 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-03 09:49:53 (43145)
- import kshowmail-3.1.0-3mdk

* Thu Dec 15 2005 Nicolas L�cureuil <neoclust@mandriva.org> 3.1.0-3mdk
- Fix BuildRequires
- use mkrel

* Fri May 06 2005 Laurent MONTEL <lmontel@mandriva.com> 3.1.0-2mdk
- Fix buildrequires

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.1.0-1mdk
- 3.1.0

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0.4-5mdk
- Rebuild

* Mon Feb 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0.4-4mdk
- Rebuild

