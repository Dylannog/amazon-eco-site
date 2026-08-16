/* Cookie consent banner + Google Consent Mode v2 update.
   Default state is set inline in <head> before gtag.js loads (denied unless
   previously granted). This file only renders the banner and pushes updates. */
(function () {
    var KEY = 'cookie-consent';

    var T = {
        en: {
            title: 'Cookies',
            body: 'We use Google Analytics to understand how visitors find and use this site. It sets a cookie. Nothing is used for advertising and we never sell your data.',
            more: 'Privacy Policy',
            accept: 'Accept',
            decline: 'Decline',
            privacy: '/privacy/'
        },
        de: {
            title: 'Cookies',
            body: 'Wir verwenden Google Analytics, um zu verstehen, wie Besucher diese Website finden und nutzen. Dabei wird ein Cookie gesetzt. Nichts davon dient der Werbung, und wir verkaufen Ihre Daten niemals.',
            more: 'Datenschutz',
            accept: 'Akzeptieren',
            decline: 'Ablehnen',
            privacy: '/privacy/'
        },
        es: {
            title: 'Cookies',
            body: 'Usamos Google Analytics para entender cómo los visitantes encuentran y usan este sitio. Instala una cookie. Nada se usa para publicidad y nunca vendemos tus datos.',
            more: 'Privacidad',
            accept: 'Aceptar',
            decline: 'Rechazar',
            privacy: '/privacy/'
        },
        pt: {
            title: 'Cookies',
            body: 'Usamos o Google Analytics para entender como os visitantes encontram e usam este site. Ele instala um cookie. Nada é usado para publicidade e nunca vendemos seus dados.',
            more: 'Privacidade',
            accept: 'Aceitar',
            decline: 'Recusar',
            privacy: '/privacy/'
        }
    };

    function read() {
        try { return localStorage.getItem(KEY); } catch (e) { return null; }
    }

    function save(value) {
        try { localStorage.setItem(KEY, value); } catch (e) { /* private mode */ }
    }

    function update(granted) {
        if (typeof window.gtag !== 'function') return;
        window.gtag('consent', 'update', {
            analytics_storage: granted ? 'granted' : 'denied'
        });
    }

    function decide(value, banner) {
        save(value);
        update(value === 'granted');
        banner.classList.remove('show');
        setTimeout(function () { banner.remove(); }, 400);
    }

    function render() {
        var lang = 'en';
        try { lang = localStorage.getItem('lang') || 'en'; } catch (e) { /* noop */ }
        var t = T[lang] || T.en;

        var banner = document.createElement('div');
        banner.className = 'cc';
        banner.setAttribute('role', 'dialog');
        banner.setAttribute('aria-live', 'polite');
        banner.setAttribute('aria-label', t.title);
        banner.innerHTML =
            '<p class="cc-txt">' + t.body +
            ' <a href="' + t.privacy + '">' + t.more + '</a></p>' +
            '<div class="cc-btns">' +
            '<button type="button" class="cc-no">' + t.decline + '</button>' +
            '<button type="button" class="cc-yes">' + t.accept + '</button>' +
            '</div>';

        document.body.appendChild(banner);
        banner.querySelector('.cc-yes').addEventListener('click', function () {
            decide('granted', banner);
        });
        banner.querySelector('.cc-no').addEventListener('click', function () {
            decide('denied', banner);
        });

        requestAnimationFrame(function () { banner.classList.add('show'); });
    }

    function init() {
        if (read()) return;
        render();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
