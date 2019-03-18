Name:		pie
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/

%description
Lorem ipsum dolor sit amet, consectetur adipisici elit, sed
eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquid ex ea commodi consequat. Quis aute iure reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.

%prep
%build

%install
mkdir -p %buildroot/usr/bin/
echo "int main() {}" >xx.c
gcc -O2 -fno-PIE xx.c -o     %buildroot/usr/bin/telnet
strip %buildroot/usr/bin/telnet
install -D -m 755 /bin/mount %buildroot/usr/bin/mount


%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/usr/bin/telnet
/usr/bin/mount

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
