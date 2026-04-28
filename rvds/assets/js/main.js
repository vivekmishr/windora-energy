/* RVDS Technology — interactive behaviours
   - sticky/scrolled header
   - parallax for hero background and shapes
   - scroll reveal observer
   - animated counters
   - FAQ accordion
   - mobile nav toggle
   - smooth nav-link active state on scroll
*/

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const nav = document.querySelector('.nav');
  const navToggle = document.querySelector('.nav-toggle');
  const heroBg = document.querySelector('.hero-bg');
  const shapes = document.querySelectorAll('.hero-shape');
  const navLinks = document.querySelectorAll('.nav-menu a[href^="#"]');
  const sections = document.querySelectorAll('section[id]');

  /* ---------- header on scroll ---------- */
  const onScroll = () => {
    const y = window.scrollY;
    if (header) header.classList.toggle('scrolled', y > 50);

    /* parallax: hero background slow drift */
    if (heroBg) {
      heroBg.style.transform = `translate3d(0, ${y * 0.35}px, 0) scale(${1 + y * 0.0003})`;
    }

    /* parallax: floating shapes move at different speeds */
    shapes.forEach((s, i) => {
      const speed = 0.18 + i * 0.08;
      s.style.transform = `translate3d(0, ${y * speed}px, 0)`;
    });

    /* active nav link */
    let current = '';
    sections.forEach((sec) => {
      const top = sec.offsetTop - 120;
      if (y >= top) current = sec.id;
    });
    navLinks.forEach((l) => {
      l.classList.toggle('active', l.getAttribute('href') === '#' + current);
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- mobile nav ---------- */
  if (navToggle) {
    navToggle.addEventListener('click', () => nav.classList.toggle('open'));
  }
  navLinks.forEach((l) =>
    l.addEventListener('click', () => nav.classList.remove('open'))
  );

  /* ---------- scroll reveal ---------- */
  const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add('show');
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -60px 0px' }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('show'));
  }

  /* ---------- animated counters ---------- */
  const counters = document.querySelectorAll('.count');
  const animateCount = (el) => {
    const target = parseFloat(el.dataset.target || '0');
    const suffix = el.dataset.suffix || '';
    const dur = 1800;
    const start = performance.now();
    const tick = (now) => {
      const t = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - t, 3);
      const value = target * eased;
      el.textContent =
        (target >= 100 ? Math.round(value).toLocaleString('en-IN') : value.toFixed(1)) + suffix;
      if (t < 1) requestAnimationFrame(tick);
      else el.textContent = (target >= 100 ? Math.round(target).toLocaleString('en-IN') : target.toFixed(1)) + suffix;
    };
    requestAnimationFrame(tick);
  };
  if ('IntersectionObserver' in window) {
    const co = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            animateCount(e.target);
            co.unobserve(e.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach((c) => co.observe(c));
  }

  /* ---------- FAQ accordion ---------- */
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach((item) => {
    const q = item.querySelector('.faq-q');
    const a = item.querySelector('.faq-a');
    q.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      // close all
      faqItems.forEach((it) => {
        it.classList.remove('open');
        it.querySelector('.faq-a').style.maxHeight = '0px';
      });
      if (!isOpen) {
        item.classList.add('open');
        a.style.maxHeight = a.scrollHeight + 'px';
      }
    });
  });

  /* ---------- smooth scroll for hash links ---------- */
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id.length > 1) {
        const target = document.querySelector(id);
        if (target) {
          e.preventDefault();
          const top = target.getBoundingClientRect().top + window.scrollY - 80;
          window.scrollTo({ top, behavior: 'smooth' });
        }
      }
    });
  });

  /* ---------- contact form ----------
     Form posts directly to FormSubmit (sales@rvds.co.in) — see action attribute.
     We only update the button label so the user gets feedback while the browser
     navigates to the FormSubmit confirmation/redirect. No preventDefault().
  */
  const form = document.querySelector('#contact-form');
  if (form) {
    form.addEventListener('submit', () => {
      const btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.textContent = 'Sending…';
      }
    });
  }

  /* ---------- "submitted=1" thank-you banner ---------- */
  if (new URLSearchParams(location.search).get('submitted') === '1') {
    const banner = document.createElement('div');
    banner.style.cssText =
      'position:fixed;top:90px;left:50%;transform:translateX(-50%);z-index:200;' +
      'background:#1bbf8a;color:#fff;padding:14px 22px;border-radius:12px;' +
      'box-shadow:0 12px 30px rgba(27,191,138,0.4);font-weight:600;font-size:14px;';
    banner.textContent = '✓ Thanks! Your enquiry has been sent to sales@rvds.co.in — we will call you shortly.';
    document.body.appendChild(banner);
    setTimeout(() => { banner.style.transition = 'opacity .6s'; banner.style.opacity = '0'; }, 6000);
    setTimeout(() => banner.remove(), 7000);
  }

  /* ---------- subtle tilt on solution cards ---------- */
  document.querySelectorAll('.solution-card').forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5;
      const y = (e.clientY - r.top) / r.height - 0.5;
      card.style.transform = `translateY(-10px) rotateX(${y * -4}deg) rotateY(${x * 4}deg)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
});
