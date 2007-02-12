Summary:	Netcat-clone with strong encryption
Summary(pl.UTF-8):	Klon Netcata z mocnym szyfrowaniem
Name:		sbd
Version:	1.37
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://tigerteam.se/dl/sbd/%{name}-%{version}.tar.gz
# Source0-md5:	fe633081eed1e5e7ac5936b32146f2ac
URL:		http://tigerteam.se/dl/sbd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sbd is a Netcat-clone, designed to be portable and offer strong
encryption. It runs on Unix-like operating systems and on Microsoft
Win32. sbd features AES-CBC-128 + HMAC-SHA1 encryption (by Christophe
Devine), program execution (-e option), choosing source port,
continuous reconnection with delay, and some other nice features. Only
TCP/IP communication is supported.

%description -l pl.UTF-8
sbd to klon Netcata zaprojektowany tak, aby był przenośny i oferował
mocne szyfrowanie. Działa na systemach uniksowych oraz Microsoft
Win32. Pozwala na szyfrowanie AES-CBC-128 + HMAC-SHA1 (dzięki
Christophe'owi Devine), uruchamianie programów (opcja -e), wybór portu
źródłowego, ciągłe ponowne łączenie z opóźnieniem i parę innych
rzeczy. Obsługiwana jest tylko komunikacja TCP/IP.

%prep
%setup -q

%build
%{__make} unix \
	CC="%{__cc}" \
	UNIX_CFLAGS="%{rpmcflags}" \
	UNIX_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
