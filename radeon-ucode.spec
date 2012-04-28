#
%define		nameprog radeon

Summary:	Firmware for the radeon driver
Name:		%{nameprog}-ucode
Version:	20120428
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://people.freedesktop.org/~agd5f/radeon_ucode/LICENSE.radeon
# Source0-md5:	e56b405656593a0c97e478513051ea0e
Source1:	http://people.freedesktop.org/~agd5f/radeon_ucode/ARUBA_me.bin
# Source1-md5:	59375dccb37f974c045575cd9428009a
Source2:	http://people.freedesktop.org/~agd5f/radeon_ucode/ARUBA_pfp.bin
# Source2-md5:	b3072fac01a6eab4711c18148c8bc305
Source3:	http://people.freedesktop.org/~agd5f/radeon_ucode/ARUBA_rlc.bin
# Source3-md5:	01cc2b2897a3aff6b1ddbe0a41b6f4b5
Source4:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_mc.bin
# Source4-md5:	158f8e21ccf228ef063888c4f637fbf0
Source5:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_me.bin
# Source5-md5:	8012e24b187c6b1ba17fa48691c3b048
Source6:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_pfp.bin
# Source6-md5:	b08d560e8f57d700fd67957584e0567c
Source7:	http://people.freedesktop.org/~agd5f/radeon_ucode/BTC_rlc.bin
# Source7-md5:	dba354c1b18ed82518052a0f0a6dcab3
Source8:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_mc.bin
# Source8-md5:	158f8e21ccf228ef063888c4f637fbf0
Source9:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_me.bin
# Source9-md5:	8012e24b187c6b1ba17fa48691c3b048
Source10:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_pfp.bin
# Source10-md5:	87b95689bb03323faf917bda6aa1cd11
Source11:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAYMAN_mc.bin
# Source11-md5:	b8f97a70b25104e3ca24b8b8ade19997
Source12:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAYMAN_me.bin
# Source12-md5:	5b4feb3f418fa1725ae7ea2633071118
Source13:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAYMAN_pfp.bin
# Source13-md5:	53671bbdd823e4b14dbaab63bd5f248f
Source14:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAYMAN_rlc.bin
# Source14-md5:	6190409ee8d4392f1d0f58751734e2e3
Source15:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_me.bin
# Source15-md5:	2b244d41832f46382bfbb8994522dcdd
Source16:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_pfp.bin
# Source16-md5:	23915e382ea0d2f2491a19146ca3001c
Source17:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_rlc.bin
# Source17-md5:	f7c005e3be9f47b8911e2044b4219db4
Source18:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_me.bin
# Source18-md5:	fa937b6596298b4bbc9edb6df4adca2a
Source19:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_pfp.bin
# Source19-md5:	2dca2882a14e1d6a43792f786471ec51
Source20:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_rlc.bin
# Source20-md5:	f7c005e3be9f47b8911e2044b4219db4
Source21:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_me.bin
# Source21-md5:	fa937b6596298b4bbc9edb6df4adca2a
Source22:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_pfp.bin
# Source22-md5:	2dca2882a14e1d6a43792f786471ec51
Source23:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_rlc.bin
# Source23-md5:	f7c005e3be9f47b8911e2044b4219db4
Source24:	http://people.freedesktop.org/~agd5f/radeon_ucode/PALM_me.bin
# Source24-md5:	7d9ff6962e7bcc10b6eecd811d029dc8
Source25:	http://people.freedesktop.org/~agd5f/radeon_ucode/PALM_pfp.bin
# Source25-md5:	3f9d2af72e73d44aec16a496e7fc7fef
Source26:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_ce.bin
# Source26-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source27:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_mc.bin
# Source27-md5:	96b18c6f7c74ad4cecb04fca967ca433
Source28:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_me.bin
# Source28-md5:	5e899b3ff3e128453784b8fdacb947bb
Source29:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_pfp.bin
# Source29-md5:	6a1f860df54aa4d462339322ba363092
Source30:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_rlc.bin
# Source30-md5:	d47f11a28fd38018d218b7cdd074f8e8
Source31:	http://people.freedesktop.org/~agd5f/radeon_ucode/R600_rlc.bin
# Source31-md5:	f74a5163948bde215be6b689ca24afde
Source32:	http://people.freedesktop.org/~agd5f/radeon_ucode/R700_rlc.bin
# Source32-md5:	411b41ca3117ca88dbd9689a57f09a89
Source33:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_me.bin
# Source33-md5:	9334c37ae709f8faa6120c3ad7a5adb7
Source34:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_pfp.bin
# Source34-md5:	23915e382ea0d2f2491a19146ca3001c
Source35:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_rlc.bin
# Source35-md5:	f7c005e3be9f47b8911e2044b4219db4
Source36:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO2_me.bin
# Source36-md5:	5844be40ff36dcc30d161765e1a46e31
Source37:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO2_pfp.bin
# Source37-md5:	3804aabfa24cc8a45b2a579b3398b96b
Source38:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_me.bin
# Source38-md5:	5844be40ff36dcc30d161765e1a46e31
Source39:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_pfp.bin
# Source39-md5:	1d569f6fe2e5bd262739789ebe089996
Source40:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_rlc.bin
# Source40-md5:	2e3ffeec63f2e0b99323238fc5f96c9c
Source41:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_ce.bin
# Source41-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source42:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_mc.bin
# Source42-md5:	96b18c6f7c74ad4cecb04fca967ca433
Source43:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_me.bin
# Source43-md5:	5e899b3ff3e128453784b8fdacb947bb
Source44:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_pfp.bin
# Source44-md5:	6a1f860df54aa4d462339322ba363092
Source45:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_rlc.bin
# Source45-md5:	893d48dc24a4457bb9faa4179b8bb081
Source46:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_mc.bin
# Source46-md5:	158f8e21ccf228ef063888c4f637fbf0
Source47:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_me.bin
# Source47-md5:	8012e24b187c6b1ba17fa48691c3b048
Source48:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_pfp.bin
# Source48-md5:	25f26ba407a9bb13528b903c617209c8
Source49:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_ce.bin
# Source49-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source50:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_mc.bin
# Source50-md5:	96b18c6f7c74ad4cecb04fca967ca433
Source51:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_me.bin
# Source51-md5:	a291d177203e882872ba809f82010077
Source52:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_pfp.bin
# Source52-md5:	8929a87c20f87426578518e3fafa12f2
Source53:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_rlc.bin
# Source53-md5:	d6f9b6d4c0de8708dccb4d4b89d71cc5
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
	%{SOURCE28} \
	%{SOURCE29} \
	%{SOURCE30} \
	%{SOURCE31} \
	%{SOURCE32} \
	%{SOURCE33} \
	%{SOURCE34} \
	%{SOURCE35} \
	%{SOURCE36} \
	%{SOURCE37} \
	%{SOURCE38} \
	%{SOURCE39} \
	%{SOURCE40} \
	%{SOURCE41} \
	%{SOURCE42} \
	%{SOURCE43} \
	%{SOURCE44} \
	%{SOURCE45} \
	%{SOURCE46} \
	%{SOURCE47} \
	%{SOURCE48} \
	%{SOURCE49} \
	%{SOURCE50} \
	%{SOURCE51} \
	%{SOURCE52} \
	%{SOURCE53} \
	$RPM_BUILD_ROOT/lib/firmware/radeon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE*
/lib/firmware/radeon
