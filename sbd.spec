Summary:	Netcat-clone with strong encryption
Summary(pl):	Klon Netcata z mocnym szyfrowaniem
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

%description -l pl
sbd to klon Netcata zaprojektowany tak, aby by� przeno�ny i oferowa�
mocne szyfrowanie. Dzia�a na systemach uniksowych oraz Microsoft
Win32. Pozwala na szyfrowanie AES-CBC-128 + HMAC-SHA1 (dzi�ki
Christophe'owi Devine), uruchamianie program�w (opcja -e), wyb�r portu
�r�d�owego, ci�g�e ponowne ��czenie z op�nieniem i par� innych
rzeczy. Obs�ugiwana jest tylko komunikacja TCP/IP.

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
