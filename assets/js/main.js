// ========== LOADER ==========
window.addEventListener('load', () => {
    setTimeout(() => {
        document.getElementById('loader').classList.add('hidden');
    }, 1200);
});

// ========== SCROLL PROGRESS BAR ==========
const scrollProgress = document.createElement('div');
scrollProgress.className = 'scroll-progress';
document.body.appendChild(scrollProgress);

window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    scrollProgress.style.width = scrolled + '%';
});

// ========== NAVBAR SCROLL EFFECT ==========
const navbar = document.getElementById('navbar');
const backToTop = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }

    if (window.scrollY > 500) {
        backToTop.classList.add('visible');
    } else {
        backToTop.classList.remove('visible');
    }
});

// ========== BACK TO TOP ==========
backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ========== MOBILE MENU TOGGLE ==========
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// ========== ACTIVE NAV LINK ==========
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 150;
        if (window.scrollY >= sectionTop) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// ========== SCROLL REVEAL ANIMATION ==========
const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-up, .fade-in-up');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
});

revealElements.forEach(el => revealObserver.observe(el));

// ========== COUNTER ANIMATION ==========
const counters = document.querySelectorAll('.stat-number, .counter-number');

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
            entry.target.classList.add('counted');
            animateCounter(entry.target);
        }
    });
}, { threshold: 0.5 });

counters.forEach(counter => counterObserver.observe(counter));

function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-target'));
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;

    const update = () => {
        current += step;
        if (current < target) {
            el.textContent = Math.ceil(current).toLocaleString();
            requestAnimationFrame(update);
        } else {
            el.textContent = target.toLocaleString();
        }
    };
    update();
}

// ========== TYPING ANIMATION ==========
const typingText = document.getElementById('typingText');
const words = ['Every Home', 'Modern Businesses', 'Smart Cities', 'Sustainable Future'];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeEffect() {
    const currentWord = words[wordIndex];

    if (isDeleting) {
        typingText.textContent = currentWord.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typingText.textContent = currentWord.substring(0, charIndex + 1);
        charIndex++;
    }

    let typeSpeed = isDeleting ? 50 : 120;

    if (!isDeleting && charIndex === currentWord.length) {
        typeSpeed = 2000;
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        typeSpeed = 500;
    }

    setTimeout(typeEffect, typeSpeed);
}

setTimeout(typeEffect, 1500);

// ========== PARALLAX EFFECT ==========
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;

    // Hero parallax
    const heroParallax = document.querySelector('.hero-parallax');
    if (heroParallax) {
        heroParallax.style.transform = `translateY(${scrolled * 0.3}px)`;
    }

    // Animated turbines parallax
    const turbineLeft = document.querySelector('.turbine-left');
    const turbineRight = document.querySelector('.turbine-right');
    if (turbineLeft) {
        turbineLeft.style.transform = `scale(0.8) translateY(${scrolled * -0.1}px)`;
    }
    if (turbineRight) {
        turbineRight.style.transform = `scale(0.6) translateY(${scrolled * -0.15}px)`;
    }
});

// ========== TECHNOLOGY TABS ==========
const techTabs = document.querySelectorAll('.tech-tab');
const techPanels = document.querySelectorAll('.tech-panel');

techTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = tab.getAttribute('data-tab');

        techTabs.forEach(t => t.classList.remove('active'));
        techPanels.forEach(p => p.classList.remove('active'));

        tab.classList.add('active');
        document.getElementById(target).classList.add('active');
    });
});

// ========== TESTIMONIAL CAROUSEL ==========
const testimonialTrack = document.getElementById('testimonialTrack');
const dots = document.querySelectorAll('.dot');
let currentSlide = 0;
const totalSlides = dots.length;

function goToSlide(index) {
    currentSlide = index;
    testimonialTrack.style.transform = `translateX(-${index * 100}%)`;
    dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
    });
}

dots.forEach((dot, index) => {
    dot.addEventListener('click', () => goToSlide(index));
});

setInterval(() => {
    currentSlide = (currentSlide + 1) % totalSlides;
    goToSlide(currentSlide);
}, 5000);

// ========== CONTACT FORM ==========
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const button = contactForm.querySelector('.form-submit');
        const originalText = button.innerHTML;

        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> <span>Sending...</span>';
        button.disabled = true;

        try {
            const formData = new FormData(contactForm);
            const response = await fetch(contactForm.action, {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' }
            });

            if (response.ok) {
                button.innerHTML = '<i class="fas fa-check"></i> <span>Message Sent!</span>';
                button.style.background = 'linear-gradient(135deg, #2D9A4B, #3bc061)';
                contactForm.reset();
            } else {
                throw new Error('Submit failed');
            }
        } catch (err) {
            button.innerHTML = '<i class="fas fa-exclamation-triangle"></i> <span>Failed — try again</span>';
            button.style.background = 'linear-gradient(135deg, #d32f2f, #f44336)';
        }

        setTimeout(() => {
            button.innerHTML = originalText;
            button.disabled = false;
            button.style.background = '';
        }, 3000);
    });
}

// ========== RIPPLE EFFECT ON BUTTONS ==========
document.querySelectorAll('.btn, .product-btn, .cta-btn').forEach(button => {
    button.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        ripple.className = 'ripple';

        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';

        this.appendChild(ripple);

        setTimeout(() => ripple.remove(), 600);
    });
});

// ========== SMOOTH SCROLL ==========
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offsetTop = target.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// ========== CURSOR TRAIL EFFECT ==========
if (window.matchMedia('(min-width: 1024px)').matches) {
    const cursorTrail = document.createElement('div');
    cursorTrail.className = 'cursor-trail';
    document.body.appendChild(cursorTrail);

    let mouseX = 0, mouseY = 0;
    let trailX = 0, trailY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    document.querySelectorAll('a, button, .btn, .product-card, .commercial-card, .benefit-card').forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursorTrail.style.width = '40px';
            cursorTrail.style.height = '40px';
            cursorTrail.style.borderColor = 'var(--blue-accent)';
        });
        el.addEventListener('mouseleave', () => {
            cursorTrail.style.width = '20px';
            cursorTrail.style.height = '20px';
            cursorTrail.style.borderColor = 'var(--green)';
        });
    });

    function animateCursor() {
        trailX += (mouseX - trailX) * 0.15;
        trailY += (mouseY - trailY) * 0.15;
        cursorTrail.style.left = trailX + 'px';
        cursorTrail.style.top = trailY + 'px';
        requestAnimationFrame(animateCursor);
    }
    animateCursor();
}

// ========== FLOATING LEAVES ==========
function createLeaf() {
    const section = document.querySelector('.hero');
    if (!section) return;

    const leaf = document.createElement('div');
    leaf.style.cssText = `
        position: absolute;
        top: -20px;
        left: ${Math.random() * 100}%;
        width: ${10 + Math.random() * 10}px;
        height: ${10 + Math.random() * 10}px;
        background: radial-gradient(circle at 30% 30%, #3bc061, #2D9A4B);
        border-radius: 0 100% 0 100%;
        opacity: ${0.3 + Math.random() * 0.4};
        z-index: 3;
        pointer-events: none;
        animation: leaf-fall ${8 + Math.random() * 10}s linear;
    `;

    section.appendChild(leaf);
    setTimeout(() => leaf.remove(), 18000);
}

setInterval(createLeaf, 2000);

// ========== FEATURE CARDS TILT EFFECT ==========
document.querySelectorAll('.product-card, .commercial-card, .benefit-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotateX = (y - centerY) / 30;
        const rotateY = (centerX - x) / 30;

        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = '';
    });
});

console.log('%c Windora Energy ', 'background: linear-gradient(135deg, #0A2540, #2D9A4B); color: white; font-size: 20px; padding: 10px 20px; border-radius: 5px;');
console.log('%c Clean Energy. Green Future. ', 'color: #2D9A4B; font-size: 14px; font-weight: bold;');
