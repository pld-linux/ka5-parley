%define		kdeappsver	21.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		parley
Summary:	parley
Name:		ka5-%{kaname}
Version:	21.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	227b29a9bb54b4375cee63739deb2981
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel >= 5.11.1
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkeduvocdocument-devel >= %{kdeapssver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kross-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-sonnet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parley is a program to help you memorize things. Parley supports many
language specific features but can be used for other learning tasks
just as well. It uses the spaced repetition learning method, also
known as flash cards.

Creating new vocabulary collections with Parley is easy, but of course
it is even better if you can use some of our premade files. Have a
look at the store.kde.org page or use the "Download New Collections"
feature directly in Parley.

Features

• Different test types • Mixed Letters (order the letters, anagram
like) to get to know new words • Multiple choice • Written tests -
type the words (including clever correction mechanisms) • Example
sentences can be used to create 'fill in the gap' tests • Article
training • Comparison forms (adjectives and/or adverbs) • Conjugations
• Synonym/Antonym/Paraphrase

• Fast test setup with all options in one dialog • More than two
languages (for example English, Chinese Traditional and Chinese
Simplified) • Find words (also by word type) quickly • Easy lesson
management • Premade vocabulary files ready to use • Share and
download vocabulary using Get Hot New Stuff • Open XML file format
(shared with KWordQuiz, Kanagram and KHangMan) that can be edited by
hand and is easily usable with scripts

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/parley
%{_desktopdir}/org.kde.parley.desktop
%{_datadir}/config.kcfg/documentsettings.kcfg
%{_datadir}/config.kcfg/languagesettings.kcfg
%{_datadir}/config.kcfg/parley.kcfg
%{_iconsdir}/hicolor/128x128/apps/parley.png
%{_iconsdir}/hicolor/16x16/apps/parley.png
%{_iconsdir}/hicolor/32x32/apps/parley.png
%{_iconsdir}/hicolor/48x48/apps/parley.png
%{_iconsdir}/hicolor/64x64/apps/parley.png
%{_iconsdir}/hicolor/scalable/apps/parley-parley.svgz
%{_iconsdir}/hicolor/scalable/apps/parley-simple.svgz
%{_iconsdir}/hicolor/scalable/apps/parley.svgz
%{_iconsdir}/oxygen/16x16/actions/cards-block.png
%{_iconsdir}/oxygen/16x16/actions/edit-entry.png
%{_iconsdir}/oxygen/16x16/actions/edit-table-row.png
%{_iconsdir}/oxygen/16x16/actions/lesson-add.png
%{_iconsdir}/oxygen/16x16/actions/lesson-remove.png
%{_iconsdir}/oxygen/16x16/actions/list-add-card.png
%{_iconsdir}/oxygen/16x16/actions/list-remove-card.png
%{_iconsdir}/oxygen/16x16/actions/multiple-choice.png
%{_iconsdir}/oxygen/16x16/actions/practice-setup.png
%{_iconsdir}/oxygen/16x16/actions/practice-start.png
%{_iconsdir}/oxygen/16x16/actions/practice-stop.png
%{_iconsdir}/oxygen/16x16/actions/remove-duplicates.png
%{_iconsdir}/oxygen/16x16/actions/set-language.png
%{_iconsdir}/oxygen/16x16/actions/specific-setup.png
%{_iconsdir}/oxygen/22x22/actions/cards-block.png
%{_iconsdir}/oxygen/22x22/actions/edit-entry.png
%{_iconsdir}/oxygen/22x22/actions/edit-table-row.png
%{_iconsdir}/oxygen/22x22/actions/lesson-add.png
%{_iconsdir}/oxygen/22x22/actions/lesson-remove.png
%{_iconsdir}/oxygen/22x22/actions/list-add-card.png
%{_iconsdir}/oxygen/22x22/actions/list-remove-card.png
%{_iconsdir}/oxygen/22x22/actions/multiple-choice.png
%{_iconsdir}/oxygen/22x22/actions/practice-setup.png
%{_iconsdir}/oxygen/22x22/actions/practice-start.png
%{_iconsdir}/oxygen/22x22/actions/practice-stop.png
%{_iconsdir}/oxygen/22x22/actions/remove-duplicates.png
%{_iconsdir}/oxygen/22x22/actions/set-language.png
%{_iconsdir}/oxygen/22x22/actions/specific-setup.png
%{_iconsdir}/oxygen/32x32/actions/cards-block.png
%{_iconsdir}/oxygen/32x32/actions/edit-entry.png
%{_iconsdir}/oxygen/32x32/actions/edit-table-row.png
%{_iconsdir}/oxygen/32x32/actions/lesson-add.png
%{_iconsdir}/oxygen/32x32/actions/lesson-remove.png
%{_iconsdir}/oxygen/32x32/actions/list-add-card.png
%{_iconsdir}/oxygen/32x32/actions/list-remove-card.png
%{_iconsdir}/oxygen/32x32/actions/multiple-choice.png
%{_iconsdir}/oxygen/32x32/actions/practice-setup.png
%{_iconsdir}/oxygen/32x32/actions/practice-start.png
%{_iconsdir}/oxygen/32x32/actions/practice-stop.png
%{_iconsdir}/oxygen/32x32/actions/remove-duplicates.png
%{_iconsdir}/oxygen/32x32/actions/set-language.png
%{_iconsdir}/oxygen/32x32/actions/specific-setup.png
%{_iconsdir}/oxygen/48x48/actions/cards-block.png
%{_iconsdir}/oxygen/48x48/actions/edit-entry.png
%{_iconsdir}/oxygen/48x48/actions/edit-table-row.png
%{_iconsdir}/oxygen/48x48/actions/lesson-add.png
%{_iconsdir}/oxygen/48x48/actions/lesson-remove.png
%{_iconsdir}/oxygen/48x48/actions/list-add-card.png
%{_iconsdir}/oxygen/48x48/actions/list-remove-card.png
%{_iconsdir}/oxygen/48x48/actions/multiple-choice.png
%{_iconsdir}/oxygen/48x48/actions/practice-setup.png
%{_iconsdir}/oxygen/48x48/actions/practice-start.png
%{_iconsdir}/oxygen/48x48/actions/practice-stop.png
%{_iconsdir}/oxygen/48x48/actions/remove-duplicates.png
%{_iconsdir}/oxygen/48x48/actions/set-language.png
%{_iconsdir}/oxygen/48x48/actions/specific-setup.png
%{_iconsdir}/oxygen/scalable/actions/cards-block.svgz
%{_iconsdir}/oxygen/scalable/actions/edit-entry.svgz
%{_iconsdir}/oxygen/scalable/actions/edit-table-row.svgz
%{_iconsdir}/oxygen/scalable/actions/lesson-add.svgz
%{_iconsdir}/oxygen/scalable/actions/lesson-remove.svgz
%{_iconsdir}/oxygen/scalable/actions/list-add-card.svgz
%{_iconsdir}/oxygen/scalable/actions/list-remove-card.svgz
%{_iconsdir}/oxygen/scalable/actions/practice-setup.svgz
%{_iconsdir}/oxygen/scalable/actions/practice-start.svgz
%{_iconsdir}/oxygen/scalable/actions/remove-duplicates.svgz
%{_iconsdir}/oxygen/scalable/actions/set-language.svgz
%{_iconsdir}/oxygen/scalable/actions/specific-setup.svgz
%dir %{_datadir}/kxmlgui5/parley
%{_datadir}/kxmlgui5/parley/dashboardui.rc
%{_datadir}/kxmlgui5/parley/editorui.rc
%{_datadir}/kxmlgui5/parley/parleyui.rc
%{_datadir}/kxmlgui5/parley/practicesummaryui.rc
%{_datadir}/kxmlgui5/parley/practiceui.rc
%{_datadir}/kxmlgui5/parley/statisticsui.rc
%dir %{_datadir}/kxmlgui5/parley/themes
%{_datadir}/kxmlgui5/parley/themes/bees_theme.desktop
%{_datadir}/kxmlgui5/parley/themes/bees_theme.svgz
%{_datadir}/kxmlgui5/parley/themes/bees_theme_preview.jpg
%{_datadir}/kxmlgui5/parley/themes/theme_reference.desktop
%{_datadir}/kxmlgui5/parley/themes/theme_reference.svgz
%{_datadir}/kxmlgui5/parley/themes/theme_reference_preview.jpg
%{_datadir}/metainfo/org.kde.parley.appdata.xml
%dir %{_datadir}/parley
%dir %{_datadir}/parley/plugins
%{_datadir}/parley/plugins/example.desktop
%{_datadir}/parley/plugins/example.py
%{_datadir}/parley/plugins/google_dictionary.desktop
%{_datadir}/parley/plugins/google_dictionary.py
%{_datadir}/parley/plugins/leo-dict.desktop
%{_datadir}/parley/plugins/leo-dict.py
%dir %{_datadir}/parley/plugins/mwclient
%{_datadir}/parley/plugins/mwclient/LICENSE.md
%{_datadir}/parley/plugins/mwclient/README.rst
%{_datadir}/parley/plugins/mwclient/__init__.py
%{_datadir}/parley/plugins/mwclient/client.py
%{_datadir}/parley/plugins/mwclient/errors.py
%{_datadir}/parley/plugins/mwclient/ex.py
%{_datadir}/parley/plugins/mwclient/image.py
%{_datadir}/parley/plugins/mwclient/listing.py
%{_datadir}/parley/plugins/mwclient/page.py
%dir %{_datadir}/parley/plugins/mwclient/requests_oauthlib
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/__init__.py
%dir %{_datadir}/parley/plugins/mwclient/requests_oauthlib/compliance_fixes
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/__init__.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/douban.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/facebook.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/fitbit.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/linkedin.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/mailchimp.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/slack.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/weibo.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/oauth1_auth.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/oauth1_session.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/oauth2_auth.py
%{_datadir}/parley/plugins/mwclient/requests_oauthlib/oauth2_session.py
%{_datadir}/parley/plugins/mwclient/six.LICENSE
%{_datadir}/parley/plugins/mwclient/six.README
%{_datadir}/parley/plugins/mwclient/six.py
%{_datadir}/parley/plugins/mwclient/sleep.py
%{_datadir}/parley/plugins/mwclient/util.py
%{_datadir}/parley/plugins/wiktionary_sound.desktop
%{_datadir}/parley/plugins/wiktionary_sound.py
%dir %{_datadir}/parley/themes
%{_datadir}/parley/themes/bees_theme.desktop
%{_datadir}/parley/themes/bees_theme.svgz
%{_datadir}/parley/themes/bees_theme_preview.jpg
%{_datadir}/parley/themes/theme_reference.desktop
%{_datadir}/parley/themes/theme_reference.svgz
%{_datadir}/parley/themes/theme_reference_preview.jpg
%{_datadir}/parley/tips
%dir %{_datadir}/parley/xslt
%{_datadir}/parley/xslt/flashcards.xsl
%{_datadir}/parley/xslt/table.xsl
%{_datadir}/knsrcfiles/parley-themes.knsrc
%{_datadir}/knsrcfiles/parley.knsrc
