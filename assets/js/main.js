// Header scroll
const hdr = document.getElementById('hdr');
let tk = false;
window.addEventListener('scroll', () => {
    if (!tk) {
        requestAnimationFrame(() => {
            hdr.classList.toggle('scrolled', window.scrollY > 40);
            tk = false;
        });
        tk = true;
    }
}, { passive: true });

// Language selector
document.querySelectorAll('.lb').forEach(b => {
    b.addEventListener('click', () => {
        if (window.i18nSetLang) {
            window.i18nSetLang(b.textContent.trim().toLowerCase());
        } else {
            document.querySelectorAll('.lb').forEach(x => x.classList.remove('on'));
            b.classList.add('on');
        }
    });
});

// Mobile drawer
const drawer   = document.getElementById('mob-drawer');
const overlay  = document.getElementById('mob-overlay');
const mobOpen  = document.getElementById('mob-open');
const mobClose = document.getElementById('mob-close');

function openDrawer() {
    drawer.classList.add('open');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
}
function closeDrawer() {
    drawer.classList.remove('open');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
}

mobOpen.addEventListener('click', openDrawer);
mobClose.addEventListener('click', closeDrawer);
overlay.addEventListener('click', closeDrawer);
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDrawer(); });

// Scroll reveal
const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
}, { threshold: 0.08, rootMargin: '0px 0px -48px 0px' });

document.querySelectorAll('.rv').forEach(el => io.observe(el));
