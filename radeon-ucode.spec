#
%define		nameprog radeon

Summary:	Firmware for the radeon driver
Name:		%{nameprog}-ucode
Version:	20130402
Release:	2
License:	distributable
Group:		Base/Kernel
Source0:	http://people.freedesktop.org/~agd5f/radeon_ucode/LICENSE.radeon
# Source0-md5:	9c2faab1bfca55e1510d6bde67206f9c
Source1:	http://people.freedesktop.org/~agd5f/radeon_ucode/ARUBA_me.bin
# Source1-md5:	59375dccb37f974c045575cd9428009a
Source2:	http://people.freedesktop.org/~agd5f/radeon_ucode/ARUBA_pfp.bin
# Source2-md5:	b3072fac01a6eab4711c18148c8bc305
Source3:	http://people.freedesktop.org/~agd5f/radeon_ucode/ARUBA_rlc.bin
# Source3-md5:	246d1c75a5946829f6864dbd5f71d850
Source4:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_mc.bin
# Source4-md5:	158f8e21ccf228ef063888c4f637fbf0
Source5:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_me.bin
# Source5-md5:	8012e24b187c6b1ba17fa48691c3b048
Source6:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_pfp.bin
# Source6-md5:	b08d560e8f57d700fd67957584e0567c
Source7:	http://people.freedesktop.org/~agd5f/radeon_ucode/BTC_rlc.bin
# Source7-md5:	7cc579e3ae5c6a27f4de339884f5714e
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
# Source14-md5:	0c8ca68a18efff6e890cd5ea176c052a
Source15:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_me.bin
# Source15-md5:	2b244d41832f46382bfbb8994522dcdd
Source16:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_pfp.bin
# Source16-md5:	23915e382ea0d2f2491a19146ca3001c
Source17:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_rlc.bin
# Source17-md5:	e8770d3d588f24dc6f1a8609c9db3467
Source18:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_me.bin
# Source18-md5:	fa937b6596298b4bbc9edb6df4adca2a
Source19:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_pfp.bin
# Source19-md5:	2dca2882a14e1d6a43792f786471ec51
Source20:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_rlc.bin
# Source20-md5:	e8770d3d588f24dc6f1a8609c9db3467
Source21:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_uvd.bin
# Source21-md5:	fb23b281dcc94a035d374e709c9842bd
Source22:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_me.bin
# Source22-md5:	fa937b6596298b4bbc9edb6df4adca2a
Source23:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_pfp.bin
# Source23-md5:	2dca2882a14e1d6a43792f786471ec51
Source24:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_rlc.bin
# Source24-md5:	e8770d3d588f24dc6f1a8609c9db3467
Source25:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_ce.bin
# Source25-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source26:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_mc.bin
# Source26-md5:	3bbdb66a8d049cf2b7f85ebfe4d8df94
Source27:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_me.bin
# Source27-md5:	9545cef078ac83b037e1727c06ee6af2
Source28:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_pfp.bin
# Source28-md5:	417f193fd055a6842d5a4cad2ef624e1
Source29:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_rlc.bin
# Source29-md5:	f5b03bf6244fe76a8e5575671c110b3a
Source30:	http://people.freedesktop.org/~agd5f/radeon_ucode/PALM_me.bin
# Source30-md5:	7d9ff6962e7bcc10b6eecd811d029dc8
Source31:	http://people.freedesktop.org/~agd5f/radeon_ucode/PALM_pfp.bin
# Source31-md5:	3f9d2af72e73d44aec16a496e7fc7fef
Source32:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_ce.bin
# Source32-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source33:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_mc.bin
# Source33-md5:	96b18c6f7c74ad4cecb04fca967ca433
Source34:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_me.bin
# Source34-md5:	5e899b3ff3e128453784b8fdacb947bb
Source35:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_pfp.bin
# Source35-md5:	6a1f860df54aa4d462339322ba363092
Source36:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_rlc.bin
# Source36-md5:	3d2c150b3626419131bbc9a5864c7f1d
Source37:	http://people.freedesktop.org/~agd5f/radeon_ucode/R600_rlc.bin
# Source37-md5:	f74a5163948bde215be6b689ca24afde
Source38:	http://people.freedesktop.org/~agd5f/radeon_ucode/R700_rlc.bin
# Source38-md5:	5d186be14cc2cc328d02698ae4317a1b
Source39:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_me.bin
# Source39-md5:	9334c37ae709f8faa6120c3ad7a5adb7
Source40:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_pfp.bin
# Source40-md5:	23915e382ea0d2f2491a19146ca3001c
Source41:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_rlc.bin
# Source41-md5:	e8770d3d588f24dc6f1a8609c9db3467
Source42:	http://people.freedesktop.org/~agd5f/radeon_ucode/RV710_uvd.bin
# Source42-md5:	7aa399a248c0d42fba9439ae0fbc5d90
Source43:	http://people.freedesktop.org/~agd5f/radeon_ucode/RV770_uvd.bin
# Source43-md5:	cc804b5e09fb2de1e18274441a6c5b21
Source44:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO2_me.bin
# Source44-md5:	5844be40ff36dcc30d161765e1a46e31
Source45:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO2_pfp.bin
# Source45-md5:	3804aabfa24cc8a45b2a579b3398b96b
Source46:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_me.bin
# Source46-md5:	5844be40ff36dcc30d161765e1a46e31
Source47:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_pfp.bin
# Source47-md5:	1d569f6fe2e5bd262739789ebe089996
Source48:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_rlc.bin
# Source48-md5:	687e72d53413710b0a3e9330333b2dbe
Source49:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_uvd.bin
# Source49-md5:	51d9e0e2247c313c5bfc8fa7bb5b213d
Source50:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_ce.bin
# Source50-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source51:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_mc.bin
# Source51-md5:	96b18c6f7c74ad4cecb04fca967ca433
Source52:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_me.bin
# Source52-md5:	5e899b3ff3e128453784b8fdacb947bb
Source53:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_pfp.bin
# Source53-md5:	6a1f860df54aa4d462339322ba363092
Source54:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_rlc.bin
# Source54-md5:	8e3f8b42b798737b6888e89050e37c0e
Source55:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_uvd.bin
# Source55-md5:	f791dbf736a82e6bd9bb249e87445c7f
Source56:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_mc.bin
# Source56-md5:	158f8e21ccf228ef063888c4f637fbf0
Source57:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_me.bin
# Source57-md5:	8012e24b187c6b1ba17fa48691c3b048
Source58:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_pfp.bin
# Source58-md5:	25f26ba407a9bb13528b903c617209c8
Source59:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_ce.bin
# Source59-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source60:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_mc.bin
# Source60-md5:	96b18c6f7c74ad4cecb04fca967ca433
Source61:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_me.bin
# Source61-md5:	a291d177203e882872ba809f82010077
Source62:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_pfp.bin
# Source62-md5:	8929a87c20f87426578518e3fafa12f2
Source63:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_rlc.bin
# Source63-md5:	f8ee65f13adc45fe229a48128b7cd8f2
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
	%{SOURCE54} \
	%{SOURCE55} \
	%{SOURCE56} \
	%{SOURCE57} \
	%{SOURCE58} \
	%{SOURCE59} \
	%{SOURCE60} \
	%{SOURCE61} \
	%{SOURCE62} \
	%{SOURCE63} \
	$RPM_BUILD_ROOT/lib/firmware/radeon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE*
/lib/firmware/radeon
