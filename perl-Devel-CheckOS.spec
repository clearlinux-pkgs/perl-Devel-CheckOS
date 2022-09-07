#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-CheckOS
Version  : 1.94
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-CheckOS-1.94.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-CheckOS-1.94.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Devel-CheckOS-bin = %{version}-%{release}
Requires: perl-Devel-CheckOS-license = %{version}-%{release}
Requires: perl-Devel-CheckOS-man = %{version}-%{release}
Requires: perl-Devel-CheckOS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Find::Rule)
BuildRequires : perl(Test::Warnings)

%description
This module provides a nice interface to looking at $^O, and also lets
you ask about OS "families" such as "Unix" (which encompasses Linux, *BSD,
AIX, HPUX, Solaris etc).

%package bin
Summary: bin components for the perl-Devel-CheckOS package.
Group: Binaries
Requires: perl-Devel-CheckOS-license = %{version}-%{release}

%description bin
bin components for the perl-Devel-CheckOS package.


%package dev
Summary: dev components for the perl-Devel-CheckOS package.
Group: Development
Requires: perl-Devel-CheckOS-bin = %{version}-%{release}
Provides: perl-Devel-CheckOS-devel = %{version}-%{release}
Requires: perl-Devel-CheckOS = %{version}-%{release}

%description dev
dev components for the perl-Devel-CheckOS package.


%package license
Summary: license components for the perl-Devel-CheckOS package.
Group: Default

%description license
license components for the perl-Devel-CheckOS package.


%package man
Summary: man components for the perl-Devel-CheckOS package.
Group: Default

%description man
man components for the perl-Devel-CheckOS package.


%package perl
Summary: perl components for the perl-Devel-CheckOS package.
Group: Default
Requires: perl-Devel-CheckOS = %{version}-%{release}

%description perl
perl components for the perl-Devel-CheckOS package.


%prep
%setup -q -n Devel-CheckOS-1.94
cd %{_builddir}/Devel-CheckOS-1.94

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-CheckOS
cp %{_builddir}/Devel-CheckOS-%{version}/ARTISTIC.txt %{buildroot}/usr/share/package-licenses/perl-Devel-CheckOS/be0627fff2e8aef3d2a14d5d7486babc8a4873ba || :
cp %{_builddir}/Devel-CheckOS-%{version}/GPL2.txt %{buildroot}/usr/share/package-licenses/perl-Devel-CheckOS/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/use-devel-assertos

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::AssertOS.3
/usr/share/man/man3/Devel::AssertOS::AIX.3
/usr/share/man/man3/Devel::AssertOS::Alias::MacOS.3
/usr/share/man/man3/Devel::AssertOS::Amiga.3
/usr/share/man/man3/Devel::AssertOS::Apple.3
/usr/share/man/man3/Devel::AssertOS::BSDOS.3
/usr/share/man/man3/Devel::AssertOS::BeOS.3
/usr/share/man/man3/Devel::AssertOS::Bitrig.3
/usr/share/man/man3/Devel::AssertOS::Cygwin.3
/usr/share/man/man3/Devel::AssertOS::DEC.3
/usr/share/man/man3/Devel::AssertOS::DGUX.3
/usr/share/man/man3/Devel::AssertOS::DragonflyBSD.3
/usr/share/man/man3/Devel::AssertOS::Dynix.3
/usr/share/man/man3/Devel::AssertOS::EBCDIC.3
/usr/share/man/man3/Devel::AssertOS::Extending.3
/usr/share/man/man3/Devel::AssertOS::FreeBSD.3
/usr/share/man/man3/Devel::AssertOS::GNUkFreeBSD.3
/usr/share/man/man3/Devel::AssertOS::HPUX.3
/usr/share/man/man3/Devel::AssertOS::Haiku.3
/usr/share/man/man3/Devel::AssertOS::Hurd.3
/usr/share/man/man3/Devel::AssertOS::Interix.3
/usr/share/man/man3/Devel::AssertOS::Irix.3
/usr/share/man/man3/Devel::AssertOS::Linux.3
/usr/share/man/man3/Devel::AssertOS::Linux::Debian.3
/usr/share/man/man3/Devel::AssertOS::Linux::Devuan.3
/usr/share/man/man3/Devel::AssertOS::Linux::Raspbian.3
/usr/share/man/man3/Devel::AssertOS::Linux::RealDebian.3
/usr/share/man/man3/Devel::AssertOS::Linux::Ubuntu.3
/usr/share/man/man3/Devel::AssertOS::Linux::UnknownDebianLike.3
/usr/share/man/man3/Devel::AssertOS::Linux::v2_6.3
/usr/share/man/man3/Devel::AssertOS::MPEiX.3
/usr/share/man/man3/Devel::AssertOS::MSDOS.3
/usr/share/man/man3/Devel::AssertOS::MSWin32.3
/usr/share/man/man3/Devel::AssertOS::MSYS.3
/usr/share/man/man3/Devel::AssertOS::MacOSX.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_0.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_1.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_10.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_11.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_12.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_13.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_14.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_15.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_2.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_3.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_4.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_5.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_6.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_7.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_8.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v10_9.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v11.3
/usr/share/man/man3/Devel::AssertOS::MacOSX::v12.3
/usr/share/man/man3/Devel::AssertOS::MacOSclassic.3
/usr/share/man/man3/Devel::AssertOS::MachTen.3
/usr/share/man/man3/Devel::AssertOS::MicrosoftWindows.3
/usr/share/man/man3/Devel::AssertOS::MidnightBSD.3
/usr/share/man/man3/Devel::AssertOS::Minix.3
/usr/share/man/man3/Devel::AssertOS::MirOSBSD.3
/usr/share/man/man3/Devel::AssertOS::NeXT.3
/usr/share/man/man3/Devel::AssertOS::NetBSD.3
/usr/share/man/man3/Devel::AssertOS::Netware.3
/usr/share/man/man3/Devel::AssertOS::OS2.3
/usr/share/man/man3/Devel::AssertOS::OS390.3
/usr/share/man/man3/Devel::AssertOS::OS400.3
/usr/share/man/man3/Devel::AssertOS::OSF.3
/usr/share/man/man3/Devel::AssertOS::OSFeatures::POSIXShellRedirection.3
/usr/share/man/man3/Devel::AssertOS::OpenBSD.3
/usr/share/man/man3/Devel::AssertOS::POSIXBC.3
/usr/share/man/man3/Devel::AssertOS::QNX.3
/usr/share/man/man3/Devel::AssertOS::QNX::Neutrino.3
/usr/share/man/man3/Devel::AssertOS::QNX::v4.3
/usr/share/man/man3/Devel::AssertOS::RISCOS.3
/usr/share/man/man3/Devel::AssertOS::Realtime.3
/usr/share/man/man3/Devel::AssertOS::SCO.3
/usr/share/man/man3/Devel::AssertOS::Solaris.3
/usr/share/man/man3/Devel::AssertOS::Sun.3
/usr/share/man/man3/Devel::AssertOS::SunOS.3
/usr/share/man/man3/Devel::AssertOS::SysVr4.3
/usr/share/man/man3/Devel::AssertOS::SysVr5.3
/usr/share/man/man3/Devel::AssertOS::Unicos.3
/usr/share/man/man3/Devel::AssertOS::Unix.3
/usr/share/man/man3/Devel::AssertOS::VMESA.3
/usr/share/man/man3/Devel::AssertOS::VMS.3
/usr/share/man/man3/Devel::AssertOS::VOS.3
/usr/share/man/man3/Devel::AssertOS::iOS.3
/usr/share/man/man3/Devel::CheckOS.3
/usr/share/man/man3/Devel::CheckOS::Families.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-CheckOS/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/perl-Devel-CheckOS/be0627fff2e8aef3d2a14d5d7486babc8a4873ba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/use-devel-assertos.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
