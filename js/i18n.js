/* =========================================
   Homepage i18n (ko / en / ja)
   - Korean is the source text written in index.html; it is captured from the DOM on load.
   - Elements opt in with data-i18n (innerHTML), data-i18n-alt, data-i18n-aria.
   - Keys missing from en/ja fall back to Korean.
   ========================================= */
(function () {
    const LANGS = ['ko', 'en', 'ja'];
    const STORAGE_KEY = 'berapt-lang';
    const BOT_UA = /bot|crawl|spider|slurp|yeti|lighthouse/i;

    const I18N = {
        en: {
            'meta.title': 'BeRapt - The Hub of the Subculture Creative Ecosystem',
            'meta.description': 'BeRapt uses technology to transform the global subculture creative market, building an ecosystem where creators gain more opportunities and fans enjoy richer experiences.',
            'contact.copied': 'Email address copied.',

            'brand.berapt': 'BeRapt',
            'brand.pick': 'ShoulderPick',
            'brand.shoulder': 'Shoulder',
            'store.google': 'Get it on Google Play',
            'store.apple': 'Download on the App Store',

            'nav.vision': 'Vision',
            'nav.services': 'Services',
            'nav.activities': 'Activities',
            'nav.history': 'History',
            'nav.news': 'News',
            'nav.contact': 'Contact',
            'nav.insights': 'Insights',
            'nav.menu': 'Menu',

            'vision.sub': 'Creators win fans with their work on <strong class="vision-highlight">ShoulderPick</strong>,<br/>deepen those relationships through <strong class="vision-highlight">Shoulder</strong> memberships,<br/>and bring it all to life as physical goods — that is the original content ecosystem we are building.',
            'vision.v1.title': 'Monetization',
            'vision.v1.desc': 'We provide direct and indirect business tools that help creators become financially independent.',
            'vision.v2.title': 'Originality',
            'vision.v2.desc': 'Beyond the endless copies of AI — the special experience of owning a physical piece filled with an artist\'s inspiration.',
            'vision.v3.title': 'Endless Connection',
            'vision.v3.desc': 'From online to offline events, we design immersive subculture experiences at every touchpoint where fandom lives.',
            'vision.name.title': 'What is <strong>BeRapt</strong>?',
            'vision.name.desc': '<em>Be</em> : to become&nbsp;&nbsp;·&nbsp;&nbsp;<em>Rapt</em> : completely absorbed, captivated',
            'vision.name.text': '<strong class="vision-highlight">BeRapt</strong> builds services that create experiences<br/>people can wholeheartedly immerse themselves in.',

            'services.headline': 'Two platforms connecting<br/>creators and fandom',
            'services.sub': 'With two revenue models — an open platform and a subscription community —<br/>we are creating an environment where creators can make a living from their art alone.',
            'pick.identity': '"YouTube for Illustrators"',
            'pick.desc': 'When creators post their artwork, revenue is shared based on fans\' views and interest (Pick) data. An indirect revenue model that earns through the power of content alone, with no sales effort required.',
            'pick.f1': 'Pick voting boosts exposure for popular content, with YouTube-style automatic revenue sharing',
            'pick.f2': 'Just upload your work — goods production, sales, and settlement in one click',
            'pick.f3': 'One of Korea\'s largest subculture illustration services',
            'shoulder.identity': '"A YouTube Membership–Style Fan Community"',
            'shoulder.desc': 'Offers exclusive content for paid subscribers, such as unreleased drafts and high-resolution originals. Close communication between artists and fans generates stable monthly recurring revenue.',
            'shoulder.f1': 'Subscription-based monthly revenue, plus one-time tips',
            'shoulder.f2': 'Exclusive members-only content',
            'shoulder.f3': 'A close-knit community for fans and creators',

            'occ.sub': 'We maximize the value of digital IP through physical goods.<br/>The warmth of an artist\'s hand, which AI cannot imitate, becomes something you can hold.',
            'occ.s1.title': 'ShoulderPick OCC Vol.1',
            'occ.s2.title': 'ShoulderPick OCC Vol.2',
            'occ.s3.title': 'ShoulderPick OCC Vol.3',
            'occ.s4.title': 'ShoulderPick OCC Vol.4',
            'occ.s1.front': 'The first limited-edition collection that launched the BeRapt ecosystem',
            'occ.s2.front': 'More participating artists, plus hand-signed artist cards',
            'occ.s3.front': 'The third series, carrying on the collection\'s popularity',
            'occ.s4.front': 'The fourth collection in the ShoulderPick OCC series',
            'occ.s1.back': 'BeRapt\'s first original goods. Produced in small quantities, it is now a hard-to-find collection.',
            'occ.s2.back': 'An upgraded collection with an expanded artist lineup and hand-signed artist cards.',
            'occ.s3.back': 'With hand-signed and digital signatures added, a collection made for collectors.',
            'occ.s4.back': 'Introducing the newest collection in the ShoulderPick OCC series.',
            'occ.soldout': 'Sold out',
            'occ.onsale': 'On sale',
            'occ.cta': 'Shop now',

            'activities.headline': 'Meet BeRapt in Person',
            'activities.sub': 'Vivid moments from offline events, exhibitions, and partnerships.',
            'activities.alt': 'BeRapt activity',

            'history.headline': 'Our Journey',
            'history.sub': 'From our founding in 2022 to today — building a subculture creative ecosystem.',
            'history.2025.apr': 'Selected for the 7th Changgu Program, run jointly by the Ministry of SMEs and Startups and Google Play',
            'history.2025.mar': 'Launched ShoulderPick\'s first original goods — OCC',
            'history.2024.oct': 'Launched the ShoulderPick iOS and Android apps simultaneously',
            'history.2024.aug1': 'Launched ShoulderPick, a subculture image site',
            'history.2024.aug2': 'Selected for the KOCCA 2024 Global Launchpad &lt;Japan&gt; program',
            'history.2024.jul1': 'Selected for the RAPA 2024 Cre-UP program',
            'history.2024.jul2': 'Selected for Korea Credit Guarantee Fund Startup-NEST, Cohort 16',
            'history.2024.jan': 'Raised a Pre-A round from Amutus (Japan)',
            'history.2023.dec': 'Launched the Shoulder iOS app',
            'history.2023.jun': 'Official launch of Shoulder and its Android app',
            'history.2023.apr': 'Selected for TIPS, plus overseas marketing and startup commercialization support programs',
            'history.2023.mar': 'Signed an MOU with Flitto, a crowdsourced translation platform',
            'history.2023.jan': 'Beta launch of Shoulder, a community for supporting artists',
            'history.2022.dec': 'Raised a seed round from Kimgisa Lab',
            'history.2022.nov': 'Signed an MOU with Crack Entertainment, a webtoon artist agency',
            'history.2022.may': 'BeRapt founded',

            'news.headline': 'BeRapt in the News',
            'news.sub': 'Stories about BeRapt that caught the media\'s attention.',
            'news.n1.source': 'IT Chosun',
            'news.n1.title': 'BeRapt selected for the 7th Changgu Program by the Ministry of SMEs and Startups and Google Play',
            'news.n2.source': 'Chosun Biz',
            'news.n2.title': 'BeRapt raises a Pre-A round from Japan\'s Amutus',
            'news.n3.source': 'Next Daily',
            'news.n3.title': 'BeRapt, operator of artist-support community Shoulder, selected for TIPS',

            'insights.headline': 'Insights',
            'insights.more': 'View all articles (Korean) →',

            'contact.headline': 'Let\'s Build Together',
            'contact.sub': 'We welcome all inquiries about investment, partnerships, careers, and more.',
            'contact.email': 'Email',
            'contact.hint': 'Click to copy',
            'contact.phone': 'Phone',
            'contact.phone.value': '+82-70-4115-4732',
            'contact.address': 'Address',
            'contact.address.value': '#406, 14 Magokjungang 8-ro, Gangseo-gu, Seoul 07801, Korea',

            'footer.company': 'BeRapt Inc.',
            'footer.reg': 'Business Registration No.: 411-88-02619 · Mail-Order Sales Registration No.: 2022-Seoul Gangnam-05265',
            'footer.info': 'CEO: Wonje Lee · Tel: +82-70-4115-4732 · Address: #406, 14 Magokjungang 8-ro, Gangseo-gu, Seoul 07801, Korea',
        },

        ja: {
            'meta.title': 'BeRapt - サブカルチャー創作エコシステムの中心',
            'meta.description': 'BeRaptはITの力で世界のサブカルチャー創作市場を革新します。クリエイターにはより多くの機会を、ファンにはより豊かな体験を届けるエコシステムをつくります。',
            'contact.copied': 'メールアドレスをコピーしました。',

            'brand.berapt': 'BeRapt',
            'brand.pick': 'ShoulderPick',
            'brand.shoulder': 'Shoulder',
            'store.google': 'Google Play で手に入れよう',
            'store.apple': 'App Store からダウンロード',

            'nav.vision': 'ビジョン',
            'nav.services': 'サービス',
            'nav.activities': '活動',
            'nav.history': '沿革',
            'nav.news': 'ニュース',
            'nav.contact': 'お問い合わせ',
            'nav.insights': 'インサイト',
            'nav.menu': 'メニュー',

            'vision.sub': '<strong class="vision-highlight">ShoulderPick</strong>の作品でファンを獲得し、<br/><strong class="vision-highlight">Shoulder</strong>のサブスク型メンバーシップで関係を深め、<br/>それを実物として完成させるオリジナルコンテンツのエコシステムを築きます。',
            'vision.v1.title': '収益化',
            'vision.v1.desc': '直接・間接のビジネス機能を提供し、クリエイターの経済的自立を支援します。',
            'vision.v2.title': 'オリジナリティ',
            'vision.v2.desc': '無限に複製されるAIの残像を超え、作家のインスピレーションが宿る実物を所有する特別な体験。',
            'vision.v3.title': '無限のつながり',
            'vision.v3.desc': 'オンラインからオフラインの現場まで、ファンダムが息づくあらゆる接点で立体的なサブカルチャー体験をデザインします。',
            'vision.name.title': '<strong>BeRapt</strong>とは？',
            'vision.name.desc': '<em>Be</em> : 〜になる&nbsp;&nbsp;·&nbsp;&nbsp;<em>Rapt</em> : 完全に没頭した、心を奪われた',
            'vision.name.text': '<strong class="vision-highlight">BeRapt</strong>は、人々が何かに心から没頭できる<br/>体験を生み出すサービスをつくっていきます。',

            'services.headline': '創作とファンダムをつなぐ<br/>2つのプラットフォーム',
            'services.sub': 'オープンプラットフォームとサブスク型コミュニティ、2つの収益構造で<br/>クリエイターがイラストだけで生活できる環境をつくります。',
            'pick.identity': '「イラストレーター版YouTube」',
            'pick.desc': 'クリエイターがイラストを投稿すると、ファンの閲覧数と関心度（Pick）データに応じて収益が分配されます。営業活動なしに、コンテンツの力だけで収益を生み出す間接収益モデルです。',
            'pick.f1': 'Pick投票で人気コンテンツの露出を拡大、YouTube型の自動収益分配',
            'pick.f2': '作品をアップロードするだけで、グッズの制作・販売・精算までワンクリック',
            'pick.f3': '韓国最大級のサブカルチャーイラストサービス',
            'shoulder.identity': '「YouTubeメンバーシップ型ファンコミュニティ」',
            'shoulder.desc': '有料会員限定のコンテンツ（未公開ラフ、高画質の原本など）を提供します。作家とファンの密なコミュニケーションにより、安定した月額定期収益を生み出します。',
            'shoulder.f1': 'サブスク型の月額定期収益に加え、単発の応援機能も提供',
            'shoulder.f2': 'メンバー限定コンテンツの提供',
            'shoulder.f3': 'ファンとクリエイターが密につながるコミュニティ',

            'occ.sub': '実物グッズの販売を通じて、デジタルIPの価値を最大化します。<br/>AIには真似できない作家の温もりを、手に取れる価値として届けます。',
            'occ.s1.title': 'ShoulderPick OCC Vol.1',
            'occ.s2.title': 'ShoulderPick OCC Vol.2',
            'occ.s3.title': 'ShoulderPick OCC Vol.3',
            'occ.s4.title': 'ShoulderPick OCC Vol.4',
            'occ.s1.front': 'BeRaptエコシステムの始まりを告げた初期限定コレクション',
            'occ.s2.front': '参加作家の拡大と作家直筆サインカードを追加',
            'occ.s3.front': 'シリーズの人気を受け継ぐ第3弾',
            'occ.s4.front': 'ShoulderPick OCCシリーズ第4弾コレクション',
            'occ.s1.back': 'BeRapt創作エコシステム初のオリジナルグッズ。少量生産のため、今では入手困難なコレクション。',
            'occ.s2.back': '作家ラインナップを拡大し、直筆サインカードを加えたアップグレード版コレクション。',
            'occ.s3.back': '直筆サインとデジタルサインを追加し、コレクション性を高めたシリーズ。',
            'occ.s4.back': '新登場、ShoulderPick OCCシリーズの最新コレクション。',
            'occ.soldout': '完売',
            'occ.onsale': '販売中',
            'occ.cta': '購入する',

            'activities.headline': '現場で出会うBeRapt',
            'activities.sub': 'オフラインイベント、展示会、パートナーシップの現場の生き生きとした瞬間。',
            'activities.alt': 'BeRaptの活動',

            'history.headline': 'BeRaptの歩み',
            'history.sub': '2022年の設立から現在まで、サブカルチャー創作エコシステムを築いてきた道のり。',
            'history.2025.apr': '中小ベンチャー企業部・Google Play共同「チャング・プログラム」第7期に最終選定',
            'history.2025.mar': 'ShoulderPick初のオリジナルグッズ「OCC」販売開始',
            'history.2024.oct': 'ShoulderPick iOS/Androidアプリを同時リリース',
            'history.2024.aug1': 'サブカルチャー画像サイト「ShoulderPick」リリース',
            'history.2024.aug2': '韓国コンテンツ振興院 2024 グローバルLaunchpad〈日本〉プログラムに最終選定',
            'history.2024.jul1': '韓国電波振興協会 2024 Cre-UPプログラムに最終選定',
            'history.2024.jul2': '信用保証基金 Startup-NEST 第16期に最終選定',
            'history.2024.jan': '日本の株式会社アムタスよりPre-Aラウンドの投資を獲得',
            'history.2023.dec': '「Shoulder」iOSアプリをリリース',
            'history.2023.jun': '「Shoulder」正式リリースおよびAndroidアプリをリリース',
            'history.2023.apr': 'TIPSに最終選定、海外マーケティング・創業事業化支援事業にも同時選定',
            'history.2023.mar': '集合知翻訳ソリューションの株式会社FlittoとMOU締結',
            'history.2023.jan': '作家応援コミュニティ「Shoulder」ベータ版リリース',
            'history.2022.dec': 'Kimgisa Labよりシードラウンドの投資を獲得',
            'history.2022.nov': 'ウェブトゥーン作家エージェンシーの株式会社Crack EntertainmentとMOU締結',
            'history.2022.may': 'BeRapt設立',

            'news.headline': 'BeRaptニュース',
            'news.sub': 'メディアが注目したBeRaptのストーリー。',
            'news.n1.source': 'IT朝鮮',
            'news.n1.title': 'BeRapt、中小ベンチャー企業部・Google Play共同「チャング・プログラム」第7期に選定',
            'news.n2.source': '朝鮮ビズ',
            'news.n2.title': 'BeRapt、日本のアムタスからPre-Aラウンドの投資を獲得',
            'news.n3.source': 'ネクストデイリー',
            'news.n3.title': '作家応援コミュニティ「Shoulder」運営のBeRapt、TIPSに選定',

            'insights.headline': 'インサイト',
            'insights.more': 'すべての記事を見る（韓国語）→',

            'contact.headline': '一緒につくりましょう',
            'contact.sub': '投資、提携、採用など、BeRaptに関するあらゆるお問い合わせを歓迎します。',
            'contact.email': 'メール',
            'contact.hint': 'クリックでコピー',
            'contact.phone': '電話',
            'contact.phone.value': '+82-70-4115-4732',
            'contact.address': '住所',
            'contact.address.value': '〒07801 韓国ソウル特別市江西区麻谷中央8路14 406号',

            'footer.company': '株式会社BeRapt',
            'footer.reg': '事業者登録番号：411-88-02619 · 通信販売業申告番号：第2022-ソウル江南-05265号',
            'footer.info': '代表：イ・ウォンジェ · 電話：+82-70-4115-4732 · 住所：〒07801 韓国ソウル特別市江西区麻谷中央8路14 406号',
        },
    };

    // Korean source, captured from the page as written
    const source = {
        'meta.title': document.title,
        'meta.description': document.querySelector('meta[property="og:description"]').content,
        'contact.copied': '이메일이 복사되었습니다',
    };
    document.querySelectorAll('[data-i18n]').forEach(el => {
        if (!(el.dataset.i18n in source)) source[el.dataset.i18n] = el.innerHTML;
    });
    document.querySelectorAll('[data-i18n-alt]').forEach(el => {
        if (!(el.dataset.i18nAlt in source)) source[el.dataset.i18nAlt] = el.alt;
    });
    document.querySelectorAll('[data-i18n-aria]').forEach(el => {
        if (!(el.dataset.i18nAria in source)) source[el.dataset.i18nAria] = el.getAttribute('aria-label');
    });

    let current = 'ko';

    function t(key) {
        const dict = I18N[current];
        return (dict && dict[key]) || source[key] || key;
    }

    function detect() {
        const param = new URLSearchParams(location.search).get('lang');
        if (LANGS.includes(param)) return param;
        try {
            const saved = localStorage.getItem(STORAGE_KEY);
            if (LANGS.includes(saved)) return saved;
        } catch (e) {}
        // Crawlers always get the Korean source page
        if (BOT_UA.test(navigator.userAgent)) return 'ko';
        for (const l of navigator.languages || [navigator.language]) {
            const code = (l || '').slice(0, 2).toLowerCase();
            if (LANGS.includes(code)) return code;
        }
        return 'en';
    }

    function apply(lang) {
        current = lang;
        document.documentElement.lang = lang;
        document.title = t('meta.title');
        document.querySelectorAll('[data-i18n]').forEach(el => { el.innerHTML = t(el.dataset.i18n); });
        document.querySelectorAll('[data-i18n-alt]').forEach(el => { el.alt = t(el.dataset.i18nAlt); });
        document.querySelectorAll('[data-i18n-aria]').forEach(el => { el.setAttribute('aria-label', t(el.dataset.i18nAria)); });
        document.querySelectorAll('.lang-btn').forEach(btn => {
            const active = btn.dataset.lang === lang;
            btn.classList.toggle('active', active);
            btn.setAttribute('aria-pressed', active);
        });
    }

    function setLang(lang) {
        apply(lang);
        try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) {}
        const url = new URL(location.href);
        if (lang === 'ko') url.searchParams.delete('lang');
        else url.searchParams.set('lang', lang);
        history.replaceState(null, '', url);
    }

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', () => setLang(btn.dataset.lang));
    });

    apply(detect());

    window.beraptI18n = { t, setLang };
})();
