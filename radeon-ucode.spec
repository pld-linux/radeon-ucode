#
%define		nameprog radeon

Summary:	Firmware for the radeon driver
Name:		%{nameprog}-ucode
Version:	20091209
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://people.freedesktop.org/~agd5f/radeon_ucode/R600_rlc.bin
# Source0-md5:	f74a5163948bde215be6b689ca24afde
Source1:	http://people.freedesktop.org/~agd5f/radeon_ucode/R700_rlc.bin
# Source1-md5:	411b41ca3117ca88dbd9689a57f09a89
Source2:	http://people.freedesktop.org/~agd5f/radeon_ucode/LICENSE.radeon
# Source2-md5:	29d55111f2c9f6abdf3787e560a65109
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the radeon driver.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/radeon

install %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/radeon
install %{SOURCE2} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE*
/lib/firmware/radeon
