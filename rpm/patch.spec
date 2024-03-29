Name:       patch
Summary:    The GNU patch command, for modifying/upgrading files
Version:    2.7.6
Release:    1
License:    GPLv3
URL:        https://github.com/sailfishos/patch
Source0:    %{name}-%{version}.tar.xz
Patch1:     0001-Fix-execute-to-work-with-recent-gnulib.patch
BuildRequires: bison

%description
The patch program applies diff files to originals.  The diff command
is used to compare an original to a changed file.  Diff lists the
changes made to the file.  A person who has the original file can then
use the patch command with the diff file to add the changes to their
original file (patching the file).

Patch should be installed because it is a common way of upgrading
applications.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
echo %{version} | cut -d '+' -f 1 > .tarball-version
cp .tarball-version .version

CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"

./bootstrap --gnulib-srcdir=../gnulib/
%configure
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%license COPYING
%doc NEWS README
%{_bindir}/*
%doc %{_mandir}/*/*


