%define	name	kshowmail
%define	version	4.0.1
%define	release	%mkrel	1

Name:		%{name}
Summary:	Show and delete mail on pop3 servers
Version:	%{version}
Release:	%{release}
Url:		http://sourceforge.net/projects/kshowmail
License:	GPLv2+
Group:		Networking/Mail
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Source0:	%{name}-%{version}.tar.gz
Provides:       %{name} = %{version}-%{release}

BuildRequires:  kdelibs4-devel
BuildRequires:  kdenetwork4-devel
BuildRequires:  kdepim4-devel

%description
KShowmail is a KDE utility to show headers or the complete mails on pop3
servers without transfering them to the local mail client. Unpleasant mails
can be deleted on the server.  The information can be refreshed via timers.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
cd build
%{makeinstall_std}
kbuildsycoca4
cd -

%files
%defattr(-,root,root)
%{_bindir}/kshowmail
%{_libdir}/kde4/kcm_kshowmailconfig*
%{_datadir}/applications/kde4/kshowmail.desktop
%{_datadir}/apps/kshowmail
%doc %{_datadir}/doc/HTML/en/kshowmail
%{_datadir}/icons/hicolor/*/apps/kshowmail.png
%{_datadir}/kde4/services/kshowmailconfig*
%{_datadir}/locale/*/LC_MESSAGES/kshowmail.mo

%clean
rm -rf "%{buildroot}"


%changelog
* Wed Apr 27 2011 Johnny A. Solbu <solbu@mandriva.org> 4.0.1-1mdv2011.0
- New version 4.0.1
- Import kshowmail-4.0.1 from Mandrivauser.de

  * Wed Jul 28 2010 Jens Ornot <rpm@mandrivauser.de> 4.0.1-1mud2010.1
    - a bugfix release
    - Bug fixed: KShowmail has chrashed when it deleting mails.
  
  * Tue Jul 08 2010 Oliver Burger <rpm@mandrivauser.de> 4.0-1mud2010.1
    - initial package for Mandriva Linux

* Wed Sep 24 2008 Funda Wang <fundawang@mandriva.org> 3.3.0-2mdv2009.0
+ Revision: 287672
- requires kio_pop3

* Sat Aug 02 2008 Funda Wang <fundawang@mandriva.org> 3.3.0-1mdv2009.0
+ Revision: 260616
- New version 3.3.0
- switch to /opt

* Tue Jul 22 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.2.1-3mdv2009.0
+ Revision: 240921
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 09 2007 Funda Wang <fundawang@mandriva.org> 3.2.1-1mdv2008.0
+ Revision: 60843
- use hicolor theme
- add missing files for kcontrol module
- use xdg menu
- New version 3.2.1

* Mon Apr 23 2007 Laurent Montel <lmontel@mandriva.org> 3.1.2-1mdv2008.0
+ Revision: 17176
- 3.1.2
  Fix compile under x86_64
  Use macro for doc file

* Fri Sep 01 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-09-01 15:03:09 (59335)
- Rebuild

* Thu Aug 03 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-03 09:49:53 (43145)
- import kshowmail-3.1.0-3mdk

* Thu Dec 15 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.1.0-3mdk
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

