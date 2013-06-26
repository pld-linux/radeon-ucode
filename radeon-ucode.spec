#
%define		nameprog radeon

Summary:	Firmware for the radeon driver
Name:		%{nameprog}-ucode
Version:	20130626
Release:	1
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
Source7:	http://people.freedesktop.org/~agd5f/radeon_ucode/BARTS_smc.bin
# Source7-md5:	24a4c72d0bc120ffd2283e428faf432b
Source8:	http://people.freedesktop.org/~agd5f/radeon_ucode/BONAIRE_ce.bin
# Source8-md5:	44ec9d529b6fb44d4dd0a219e3218a1e
Source9:	http://people.freedesktop.org/~agd5f/radeon_ucode/BONAIRE_mc.bin
# Source9-md5:	ef4e1c28226020f29718c1b4a71e4936
Source10:	http://people.freedesktop.org/~agd5f/radeon_ucode/BONAIRE_me.bin
# Source10-md5:	16a295b3cfe280ea070727713049a2d9
Source11:	http://people.freedesktop.org/~agd5f/radeon_ucode/BONAIRE_mec.bin
# Source11-md5:	e2a1fb791002c7ce24f770d234700104
Source12:	http://people.freedesktop.org/~agd5f/radeon_ucode/BONAIRE_pfp.bin
# Source12-md5:	48db59feaf30154dc5183301781ee7c5
Source13:	http://people.freedesktop.org/~agd5f/radeon_ucode/BONAIRE_rlc.bin
# Source13-md5:	85eabd2f0f48679eeade573c471814ad
Source14:	http://people.freedesktop.org/~agd5f/radeon_ucode/BONAIRE_sdma.bin
# Source14-md5:	0f6501d69df393af36f8f3bcb59d3835
Source15:	http://people.freedesktop.org/~agd5f/radeon_ucode/BONAIRE_uvd.bin
# Source15-md5:	303438f5daec8e0661a3d1272606c558
Source16:	http://people.freedesktop.org/~agd5f/radeon_ucode/BTC_rlc.bin
# Source16-md5:	25d61fad839b30b263f52328c1f678fb
Source17:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_mc.bin
# Source17-md5:	158f8e21ccf228ef063888c4f637fbf0
Source18:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_me.bin
# Source18-md5:	8012e24b187c6b1ba17fa48691c3b048
Source19:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_pfp.bin
# Source19-md5:	87b95689bb03323faf917bda6aa1cd11
Source20:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAICOS_smc.bin
# Source20-md5:	03d4c15eeda157c96819088253acb46a
Source21:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAYMAN_mc.bin
# Source21-md5:	b8f97a70b25104e3ca24b8b8ade19997
Source22:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAYMAN_me.bin
# Source22-md5:	5b4feb3f418fa1725ae7ea2633071118
Source23:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAYMAN_pfp.bin
# Source23-md5:	53671bbdd823e4b14dbaab63bd5f248f
Source24:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAYMAN_rlc.bin
# Source24-md5:	0c8ca68a18efff6e890cd5ea176c052a
Source25:	http://people.freedesktop.org/~agd5f/radeon_ucode/CAYMAN_smc.bin
# Source25-md5:	1884c8c5e6e6af4f088c38ae25721f42
Source26:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_me.bin
# Source26-md5:	2b244d41832f46382bfbb8994522dcdd
Source27:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_pfp.bin
# Source27-md5:	23915e382ea0d2f2491a19146ca3001c
Source28:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_rlc.bin
# Source28-md5:	e8770d3d588f24dc6f1a8609c9db3467
Source29:	http://people.freedesktop.org/~agd5f/radeon_ucode/CEDAR_smc.bin
# Source29-md5:	e8618d8a65add54200e73f5580fc48d0
Source30:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_me.bin
# Source30-md5:	fa937b6596298b4bbc9edb6df4adca2a
Source31:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_pfp.bin
# Source31-md5:	2dca2882a14e1d6a43792f786471ec51
Source32:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_rlc.bin
# Source32-md5:	e8770d3d588f24dc6f1a8609c9db3467
Source33:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_smc.bin
# Source33-md5:	aeb83918c9fb268b0a4cbb03f2dfab3f
Source34:	http://people.freedesktop.org/~agd5f/radeon_ucode/CYPRESS_uvd.bin
# Source34-md5:	fb23b281dcc94a035d374e709c9842bd
Source35:	http://people.freedesktop.org/~agd5f/radeon_ucode/HAINAN_ce.bin
# Source35-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source36:	http://people.freedesktop.org/~agd5f/radeon_ucode/HAINAN_mc.bin
# Source36-md5:	3bbdb66a8d049cf2b7f85ebfe4d8df94
Source37:	http://people.freedesktop.org/~agd5f/radeon_ucode/HAINAN_me.bin
# Source37-md5:	9545cef078ac83b037e1727c06ee6af2
Source38:	http://people.freedesktop.org/~agd5f/radeon_ucode/HAINAN_pfp.bin
# Source38-md5:	ba3d0e27b8cbcdb24181040595255d3e
Source39:	http://people.freedesktop.org/~agd5f/radeon_ucode/HAINAN_rlc.bin
# Source39-md5:	3519612cd874d840a510d575559d6b9b
Source40:	http://people.freedesktop.org/~agd5f/radeon_ucode/HAINAN_smc.bin
# Source40-md5:	9a39456f0001671d1d6d9dc30a581fe0
Source41:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_me.bin
# Source41-md5:	fa937b6596298b4bbc9edb6df4adca2a
Source42:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_pfp.bin
# Source42-md5:	2dca2882a14e1d6a43792f786471ec51
Source43:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_rlc.bin
# Source43-md5:	e8770d3d588f24dc6f1a8609c9db3467
Source44:	http://people.freedesktop.org/~agd5f/radeon_ucode/JUNIPER_smc.bin
# Source44-md5:	2dbce2e58ef5b9c79a1fd2e671d78f35
Source45:	http://people.freedesktop.org/~agd5f/radeon_ucode/KABINI_ce.bin
# Source45-md5:	44ec9d529b6fb44d4dd0a219e3218a1e
Source46:	http://people.freedesktop.org/~agd5f/radeon_ucode/KABINI_me.bin
# Source46-md5:	b1469ac001eaf8d5a04d91395c5257f8
Source47:	http://people.freedesktop.org/~agd5f/radeon_ucode/KABINI_mec.bin
# Source47-md5:	c6f8cda051fea873ce8e306afb9f20c5
Source48:	http://people.freedesktop.org/~agd5f/radeon_ucode/KABINI_pfp.bin
# Source48-md5:	92bbe966f67d6998cc96f150e3db2df5
Source49:	http://people.freedesktop.org/~agd5f/radeon_ucode/KABINI_rlc.bin
# Source49-md5:	24c0f737db80a07d784a226036aac9da
Source50:	http://people.freedesktop.org/~agd5f/radeon_ucode/KABINI_sdma.bin
# Source50-md5:	0f6501d69df393af36f8f3bcb59d3835
Source51:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_ce.bin
# Source51-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source52:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_mc.bin
# Source52-md5:	3bbdb66a8d049cf2b7f85ebfe4d8df94
Source53:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_me.bin
# Source53-md5:	9545cef078ac83b037e1727c06ee6af2
Source54:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_pfp.bin
# Source54-md5:	417f193fd055a6842d5a4cad2ef624e1
Source55:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_rlc.bin
# Source55-md5:	466d29f573fefcb60bae26b8c867d6e5
Source56:	http://people.freedesktop.org/~agd5f/radeon_ucode/OLAND_smc.bin
# Source56-md5:	42069d2e8978b87a0b9319a2caa32d41
Source57:	http://people.freedesktop.org/~agd5f/radeon_ucode/PALM_me.bin
# Source57-md5:	7d9ff6962e7bcc10b6eecd811d029dc8
Source58:	http://people.freedesktop.org/~agd5f/radeon_ucode/PALM_pfp.bin
# Source58-md5:	3f9d2af72e73d44aec16a496e7fc7fef
Source59:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_ce.bin
# Source59-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source60:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_mc.bin
# Source60-md5:	96b18c6f7c74ad4cecb04fca967ca433
Source61:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_me.bin
# Source61-md5:	5e899b3ff3e128453784b8fdacb947bb
Source62:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_pfp.bin
# Source62-md5:	6a1f860df54aa4d462339322ba363092
Source63:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_rlc.bin
# Source63-md5:	3d2c150b3626419131bbc9a5864c7f1d
Source64:	http://people.freedesktop.org/~agd5f/radeon_ucode/PITCAIRN_smc.bin
# Source64-md5:	b4b17dd30f14ceab88446c20796767d5
Source65:	http://people.freedesktop.org/~agd5f/radeon_ucode/R600_rlc.bin
# Source65-md5:	f74a5163948bde215be6b689ca24afde
Source66:	http://people.freedesktop.org/~agd5f/radeon_ucode/R700_rlc.bin
# Source66-md5:	5d186be14cc2cc328d02698ae4317a1b
Source67:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_me.bin
# Source67-md5:	9334c37ae709f8faa6120c3ad7a5adb7
Source68:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_pfp.bin
# Source68-md5:	23915e382ea0d2f2491a19146ca3001c
Source69:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_rlc.bin
# Source69-md5:	e8770d3d588f24dc6f1a8609c9db3467
Source70:	http://people.freedesktop.org/~agd5f/radeon_ucode/REDWOOD_smc.bin
# Source70-md5:	33480e5daef82d4039cabcc111917478
Source71:	http://people.freedesktop.org/~agd5f/radeon_ucode/RV710_smc.bin
# Source71-md5:	3e08d61531b186e66abbe8ca4b7aac90
Source72:	http://people.freedesktop.org/~agd5f/radeon_ucode/RV710_uvd.bin
# Source72-md5:	7aa399a248c0d42fba9439ae0fbc5d90
Source73:	http://people.freedesktop.org/~agd5f/radeon_ucode/RV730_smc.bin
# Source73-md5:	9fb755c1d51474635887122169ce77cc
Source74:	http://people.freedesktop.org/~agd5f/radeon_ucode/RV770_smc.bin
# Source74-md5:	5e6e079252159d1960080e170eb96e4c
Source75:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO2_me.bin
# Source75-md5:	5844be40ff36dcc30d161765e1a46e31
Source76:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO2_pfp.bin
# Source76-md5:	3804aabfa24cc8a45b2a579b3398b96b
Source77:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_me.bin
# Source77-md5:	5844be40ff36dcc30d161765e1a46e31
Source78:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_pfp.bin
# Source78-md5:	1d569f6fe2e5bd262739789ebe089996
Source79:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_rlc.bin
# Source79-md5:	687e72d53413710b0a3e9330333b2dbe
Source80:	http://people.freedesktop.org/~agd5f/radeon_ucode/SUMO_uvd.bin
# Source80-md5:	51d9e0e2247c313c5bfc8fa7bb5b213d
Source81:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_ce.bin
# Source81-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source82:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_mc.bin
# Source82-md5:	96b18c6f7c74ad4cecb04fca967ca433
Source83:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_me.bin
# Source83-md5:	5e899b3ff3e128453784b8fdacb947bb
Source84:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_pfp.bin
# Source84-md5:	6a1f860df54aa4d462339322ba363092
Source85:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_rlc.bin
# Source85-md5:	8e3f8b42b798737b6888e89050e37c0e
Source86:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_smc.bin
# Source86-md5:	69d0115a4a07ba98b5ee56e41aac1c8f
Source87:	http://people.freedesktop.org/~agd5f/radeon_ucode/TAHITI_uvd.bin
# Source87-md5:	201877fa59f2fe4d896d5e6b6c1d2e1c
Source88:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_mc.bin
# Source88-md5:	158f8e21ccf228ef063888c4f637fbf0
Source89:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_me.bin
# Source89-md5:	8012e24b187c6b1ba17fa48691c3b048
Source90:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_pfp.bin
# Source90-md5:	25f26ba407a9bb13528b903c617209c8
Source91:	http://people.freedesktop.org/~agd5f/radeon_ucode/TURKS_smc.bin
# Source91-md5:	4fe0f4dafe21f0efa6301a888eed4470
Source92:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_ce.bin
# Source92-md5:	a5f07f65a9ef260c0077021ecae43dc7
Source93:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_mc.bin
# Source93-md5:	96b18c6f7c74ad4cecb04fca967ca433
Source94:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_me.bin
# Source94-md5:	a291d177203e882872ba809f82010077
Source95:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_pfp.bin
# Source95-md5:	8929a87c20f87426578518e3fafa12f2
Source96:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_rlc.bin
# Source96-md5:	f8ee65f13adc45fe229a48128b7cd8f2
Source97:	http://people.freedesktop.org/~agd5f/radeon_ucode/VERDE_smc.bin
# Source97-md5:	2443ed77790c7ba390db43903b8eebd5
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
	%{SOURCE64} \
	%{SOURCE65} \
	%{SOURCE66} \
	%{SOURCE67} \
	%{SOURCE68} \
	%{SOURCE69} \
	%{SOURCE70} \
	%{SOURCE71} \
	%{SOURCE72} \
	%{SOURCE73} \
	%{SOURCE74} \
	%{SOURCE75} \
	%{SOURCE76} \
	%{SOURCE77} \
	%{SOURCE78} \
	%{SOURCE79} \
	%{SOURCE80} \
	%{SOURCE81} \
	%{SOURCE82} \
	%{SOURCE83} \
	%{SOURCE84} \
	%{SOURCE85} \
	%{SOURCE86} \
	%{SOURCE87} \
	%{SOURCE88} \
	%{SOURCE89} \
	%{SOURCE90} \
	%{SOURCE91} \
	%{SOURCE92} \
	%{SOURCE93} \
	%{SOURCE94} \
	%{SOURCE95} \
	%{SOURCE96} \
	%{SOURCE97} \
	$RPM_BUILD_ROOT/lib/firmware/radeon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE*
/lib/firmware/radeon
