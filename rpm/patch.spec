Name:       patch
Summary:    The GNU patch command, for modifying/upgrading files
Version:    2.7.6
Release:    1
Group:      Development/Tools
License:    GPLv3
URL:        http://www.gnu.org/software/patch/patch.html
Source0:    ftp://ftp.gnu.org/gnu/patch/patch-%{version}.tar.xz
Patch0:     0001-Update-find_backup_file_name-calls-because-of-a-chan.patch
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
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1

%build
echo %{version} | cut -d '+' -f 1 > .tarball-version
cp .tarball-version .version

CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"

./bootstrap --gnulib-srcdir=../gnulib/
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%doc NEWS README
%{_bindir}/*
%doc %{_mandir}/*/*


