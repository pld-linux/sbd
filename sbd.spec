Summary:	Netcat-clone with strong encryption
Name:		sbd
Version:	1.27
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://www.cycom.se/uploads/114/28/%{name}-%{version}.tar.gz
# Source0-md5:	71fd4a554d96904ffc5e20ecb465daf9
URL:		http://www.cycom.se/dl/sbd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sbd is a Netcat-clone, designed to be portable and offer strong
encryption. It runs on Unix-like operating systems and on Microsoft
Win32. sbd features AES-CBC-128 + HMAC-SHA1 encryption (by Christophe
Devine), program execution (-e option), choosing source port,
continuous reconnection with delay, and some other nice features. Only
TCP/IP communication is supported.

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
