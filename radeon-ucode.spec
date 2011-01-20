#
%define		nameprog radeon

Summary:	Firmware for the radeon driver
Name:		%{nameprog}-ucode
Version:	20110120
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://people.freedesktop.org/~agd5f/radeon_ucode/LICENSE.radeon
# Source0-md5:	982ae689f0c68715fc65161991bc36c3
Source1:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_mc.bin
# Source1-md5:	158f8e21ccf228ef063888c4f637fbf0
Source2:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_me.bin
# Source2-md5:	8012e24b187c6b1ba17fa48691c3b048
Source3:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_pfp.bin
# Source3-md5:	b08d560e8f57d700fd67957584e0567c
Source4:	http://people.freedesktop.org/~agd5f/radeon_ucode/BTC_rlc.bin
# Source4-md5:	dba354c1b18ed82518052a0f0a6dcab3
Source5:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_mc.bin
# Source5-md5:	158f8e21ccf228ef063888c4f637fbf0
Source6:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_me.bin
# Source6-md5:	8012e24b187c6b1ba17fa48691c3b048
Source7:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_pfp.bin
# Source7-md5:	87b95689bb03323faf917bda6aa1cd11
Source8:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_me.bin
# Source8-md5:	2b244d41832f46382bfbb8994522dcdd
Source9:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_pfp.bin
# Source9-md5:	23915e382ea0d2f2491a19146ca3001c
Source10:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_rlc.bin
# Source10-md5:	f7c005e3be9f47b8911e2044b4219db4
Source11:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_me.bin
# Source11-md5:	fa937b6596298b4bbc9edb6df4adca2a
Source12:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_pfp.bin
# Source12-md5:	2dca2882a14e1d6a43792f786471ec51
Source13:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_rlc.bin
# Source13-md5:	f7c005e3be9f47b8911e2044b4219db4
Source14:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_me.bin
# Source14-md5:	fa937b6596298b4bbc9edb6df4adca2a
Source15:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_pfp.bin
# Source15-md5:	2dca2882a14e1d6a43792f786471ec51
Source16:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_rlc.bin
# Source16-md5:	f7c005e3be9f47b8911e2044b4219db4
Source17:	http://people.freedesktop.org/~agd5f/radeon_ucode/PALM_me.bin
# Source17-md5:	7d9ff6962e7bcc10b6eecd811d029dc8
Source18:	http://people.freedesktop.org/~agd5f/radeon_ucode/PALM_pfp.bin
# Source18-md5:	3f9d2af72e73d44aec16a496e7fc7fef
Source19:	http://people.freedesktop.org/~agd5f/radeon_ucode/R600_rlc.bin
# Source19-md5:	f74a5163948bde215be6b689ca24afde
Source20:	http://people.freedesktop.org/~agd5f/radeon_ucode/R700_rlc.bin
# Source20-md5:	411b41ca3117ca88dbd9689a57f09a89
Source21:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_me.bin
# Source21-md5:	9334c37ae709f8faa6120c3ad7a5adb7
Source22:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_pfp.bin
# Source22-md5:	23915e382ea0d2f2491a19146ca3001c
Source23:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_rlc.bin
# Source23-md5:	f7c005e3be9f47b8911e2044b4219db4
Source24:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_rlc.bin
# Source24-md5:	2e3ffeec63f2e0b99323238fc5f96c9c
Source25:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_mc.bin
# Source25-md5:	158f8e21ccf228ef063888c4f637fbf0
Source26:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_me.bin
# Source26-md5:	8012e24b187c6b1ba17fa48691c3b048
Source27:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_pfp.bin
# Source27-md5:	25f26ba407a9bb13528b903c617209c8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the radeon driver.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/radeon

install %{SOURCE0} .

install %{SOURCE1} \
	%{SOURCE2} \
	%{SOURCE3} \
	%{SOURCE4} \
	%{SOURCE5} \
	%{SOURCE6} \
	%{SOURCE7} \
	%{SOURCE8} \
	%{SOURCE9} \
	%{SOURCE10} \
	%{SOURCE11} \
	%{SOURCE12} \
	%{SOURCE13} \
	%{SOURCE14} \
	%{SOURCE15} \
	%{SOURCE16} \
	%{SOURCE17} \
	%{SOURCE18} \
	%{SOURCE19} \
	%{SOURCE20} \
	%{SOURCE21} \
	%{SOURCE22} \
	%{SOURCE23} \
	%{SOURCE24} \
	%{SOURCE25} \
	%{SOURCE26} \
	%{SOURCE27} \
	$RPM_BUILD_ROOT/lib/firmware/radeon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE*
/lib/firmware/radeon
