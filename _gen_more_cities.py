#!/usr/bin/env python3
"""Add high-wind city pages for the next-tier wind states (AP, MP, Kerala).

Uses the CURRENT city-page template (full 10-item nav, 3.5 m/s, Video Analysis),
matching cities/wind-turbine-jamnagar.html. Links to existing state hub pages.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# name, slug, state, state_code, district, region, discom, wind_range, wind_quality, state_hub, note
CITIES = [
    # ---- Andhra Pradesh (APSPDCL — Rayalaseema) ----
    ("Anantapur", "anantapur", "Andhra Pradesh", "IN-AP", "Anantapur", "Rayalaseema wind corridor", "APSPDCL", "6-8 m/s", "excellent", "wind-turbine-telangana-andhra-pradesh.html",
     "Anantapur is one of India's windiest districts — the Rayalaseema plateau channels strong, steady winds and already hosts large wind parks such as Beluguppa, making it outstanding for small wind and hybrid systems."),
    ("Kurnool", "kurnool", "Andhra Pradesh", "IN-AP", "Kurnool", "Rayalaseema", "APSPDCL", "5-7 m/s", "excellent", "wind-turbine-telangana-andhra-pradesh.html",
     "Kurnool, on the open Rayalaseema plateau, has a strong, reliable wind resource and hosts major wind and solar parks — excellent for distributed wind and hybrid systems."),
    ("Kadapa", "kadapa", "Andhra Pradesh", "IN-AP", "Kadapa", "Rayalaseema", "APSPDCL", "5-7 m/s", "excellent", "wind-turbine-telangana-andhra-pradesh.html",
     "Kadapa (Cuddapah), in the Rayalaseema wind belt, combines strong plateau winds with high summer cooling loads — ideal for hybrid wind+solar."),

    # ---- Madhya Pradesh (MPPKVVCL — Malwa / west MP) ----
    ("Dewas", "dewas", "Madhya Pradesh", "IN-MP", "Dewas", "Malwa plateau", "MPPKVVCL", "5-7 m/s", "excellent", "wind-turbine-madhya-pradesh.html",
     "Dewas, on the Malwa plateau, is one of Madhya Pradesh's flagship wind regions with large operating wind farms and a strong, consistent resource."),
    ("Mandsaur", "mandsaur", "Madhya Pradesh", "IN-MP", "Mandsaur", "Malwa plateau", "MPPKVVCL", "5-7 m/s", "excellent", "wind-turbine-madhya-pradesh.html",
     "Mandsaur, in western MP's Malwa wind belt, has a strong plateau wind resource and hosts significant operating wind capacity."),
    ("Ratlam", "ratlam", "Madhya Pradesh", "IN-MP", "Ratlam", "Malwa plateau", "MPPKVVCL", "4-6 m/s", "very good", "wind-turbine-madhya-pradesh.html",
     "Ratlam, on the Malwa plateau, has steady, dependable winds well-suited to homes, farms, and industry."),

    # ---- Kerala (KSEB — Palghat Gap / Western Ghats) ----
    ("Palakkad", "palakkad", "Kerala", "IN-KL", "Palakkad", "Palghat Gap", "KSEB", "5-7 m/s", "excellent", "wind-turbine-kerala.html",
     "Palakkad sits at the Palghat Gap — the same Western Ghats wind funnel that makes neighbouring Coimbatore famous — giving it Kerala's strongest, most reliable wind resource, especially around Kanjikode."),
    ("Idukki", "idukki", "Kerala", "IN-KL", "Idukki", "Western Ghats (Ramakkalmedu)", "KSEB", "6-8 m/s", "excellent", "wind-turbine-kerala.html",
     "Idukki's high Western Ghats ridges — especially Ramakkalmedu, one of India's windiest hill spots — funnel powerful, consistent winds ideal for wind and hybrid systems."),
]

STATE_NAME = {"Andhra Pradesh": "Andhra Pradesh", "Madhya Pradesh": "Madhya Pradesh", "Kerala": "Kerala"}

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wind Turbine in @@NAME@@ | Vertical VAWT &amp; Hybrid Systems | Windora Energy</title>
    <meta name="description" content="Wind turbine in @@NAME@@ — vertical axis turbines for homes, farms, and businesses across @@NAME@@ &amp; @@STATE@@. @@WQCAP@@ wind resource (@@WIND@@), low-wind optimized, near-silent. Free video analysis from Windora Energy.">
    <meta name="keywords" content="wind turbine in @@NAME@@, vertical wind turbine @@NAME@@, rooftop wind turbine @@NAME@@, residential wind turbine @@NAME@@, wind energy @@NAME@@, hybrid solar wind @@NAME@@, small wind turbine @@NAME@@, @@STATE@@ wind turbine, Windora @@NAME@@">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="geo.region" content="@@CODE@@">
    <meta name="geo.placename" content="@@NAME@@, @@STATE@@, India">
    <link rel="canonical" href="https://windoraenergy.com/cities/wind-turbine-@@SLUG@@.html">
    <link rel="icon" type="image/png" href="../assets/images/logo.png">
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="stylesheet" href="../assets/css/animations.css">
    <link rel="stylesheet" href="../assets/css/extra.css">
    <link rel="stylesheet" href="../assets/css/subpage.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Windora Energy — @@NAME@@","image":"https://windoraenergy.com/assets/images/logo.png","telephone":"+91-91373-69043","email":"info@windoraenergy.com","areaServed":{"@type":"City","name":"@@NAME@@"}}</script>
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://windoraenergy.com/"},{"@type":"ListItem","position":2,"name":"@@STATE@@","item":"https://windoraenergy.com/states/@@HUB@@"},{"@type":"ListItem","position":3,"name":"Wind Turbine in @@NAME@@","item":"https://windoraenergy.com/cities/wind-turbine-@@SLUG@@.html"}]}</script>
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is @@NAME@@ windy enough for a small wind turbine?","acceptedAnswer":{"@type":"Answer","text":"@@NOTE_PLAIN@@ Our vertical axis turbines start generating at just 3.5 m/s, so they perform reliably across @@NAME@@ and @@DISTRICT@@ district."}},{"@type":"Question","name":"Which DISCOM handles net-metering in @@NAME@@?","acceptedAnswer":{"@type":"Answer","text":"@@DISCOM@@ manages the local grid connection in @@NAME@@. We handle the entire net-metering application and paperwork as part of our turnkey installation."}},{"@type":"Question","name":"Should I choose wind, solar, or hybrid in @@NAME@@?","acceptedAnswer":{"@type":"Answer","text":"For most @@STATE@@ sites we recommend a hybrid solar-wind system - solar covers sunny afternoons while wind covers evenings, nights, and the monsoon, giving the most consistent year-round output."}}]}</script>
    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-N3GTX10XW5"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-N3GTX10XW5');
    </script>
</head>
<body class="subpage-body">
<div class="top-bar"><div class="top-bar-container"><div class="top-bar-left"><a href="tel:+919137369043"><i class="fas fa-phone-alt"></i> +91 91373 69043</a><a href="mailto:info@windoraenergy.com"><i class="fas fa-envelope"></i> info@windoraenergy.com</a></div><div class="top-bar-right"><span><i class="fas fa-map-marker-alt"></i> @@NAME@@ &amp; @@STATE@@</span></div></div></div>
<nav class="navbar scrolled" id="navbar"><div class="nav-container"><a href="../index.html" class="nav-logo"><img src="../assets/images/logo.png" alt="Wind Turbine @@NAME@@ — Windora" class="logo-img"></a><ul class="nav-menu" id="navMenu"><li class="nav-item"><a href="../index.html" class="nav-link">Home</a></li><li class="nav-item"><a href="../index.html#products" class="nav-link">Products</a></li><li class="nav-item"><a href="../index.html#sectors" class="nav-link">Solutions</a></li><li class="nav-item"><a href="../index.html#why" class="nav-link">Why Us</a></li><li class="nav-item"><a href="../pricing/wind-turbine-price-list.html" class="nav-link">Pricing</a></li><li class="nav-item"><a href="../tools/wind-energy-roi-calculator.html" class="nav-link">ROI Calc</a></li><li class="nav-item"><a href="../resources/index.html" class="nav-link">Resources</a></li><li class="nav-item"><a href="../blog/index.html" class="nav-link">Blog</a></li><li class="nav-item"><a href="../index.html#about" class="nav-link">About</a></li><li class="nav-item"><a href="../index.html#contact" class="nav-link cta-btn">Get Free Video Analysis</a></li></ul><div class="hamburger" id="hamburger"><span></span><span></span><span></span></div></div></nav>

<section class="subpage-hero">
    <div class="container">
        <nav class="breadcrumbs"><a href="../index.html">Home</a><span class="sep">›</span><a href="../states/@@HUB@@">@@STATE@@</a><span class="sep">›</span><span class="current">Wind Turbine in @@NAME@@</span></nav>
        <span class="subpage-tag">@@NAME@@ &amp; @@REGION@@</span>
        <h1 class="subpage-title">Wind Turbine in @@NAME@@</h1>
        <p class="subpage-subtitle">@@NOTE@@ Windora installs low-wind vertical axis wind turbines and hybrid solar+wind systems for homes, farms, and businesses across @@NAME@@ and @@DISTRICT@@ district.</p>
        <div class="subpage-hero-cta">
            <a href="../index.html#contact" class="btn btn-primary"><i class="fas fa-search-location"></i><span>@@NAME@@ Video Analysis</span></a>
            <a href="https://wa.me/919137369043?text=Hi%20Windora%2C%20@@ENC@@%20wind%20turbine%20enquiry." class="btn btn-outline" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i><span>WhatsApp</span></a>
        </div>
    </div>
</section>

<section class="content-section">
    <div class="container">
        <div class="content-grid">
            <div class="content-main">
                <h2>Why Wind Energy Works in @@NAME@@</h2>
                <p>@@NOTE@@ With annual averages around <strong>@@WIND@@</strong>, @@NAME@@ is a @@WQ@@ fit for Windora's vertical axis wind turbines, which start generating at just 3.5 m/s.</p>
                <ul>
                    <li>@@WQCAP@@ wind resource — @@REGION@@ is among India's stronger wind zones</li>
                    <li>@@DISCOM@@ grid tariffs climb steeply at higher consumption slabs</li>
                    <li>High summer cooling loads across @@STATE@@ — fast payback on self-generation</li>
                    <li>@@STATE@@ renewable-energy incentives + accelerated depreciation for businesses</li>
                    <li>Strong fit for farms, farmhouses, homes, and industry around @@NAME@@</li>
                </ul>

                <div class="callout">
                    <p><strong>Why it pays off:</strong> A 5 kW hybrid solar+wind system in @@NAME@@ can generate roughly 10,000–16,000 kWh a year given the local @@WIND@@ wind resource — typically cutting a high @@DISCOM@@ bill by 70–90% with a 4–6 year payback.</p>
                </div>

                <h2>Coverage Across @@DISTRICT@@</h2>
                <ul>
                    <li><strong>@@NAME@@ town</strong> — rooftop and ground-mounted systems for homes, shops, and offices</li>
                    <li><strong>@@DISTRICT@@ district</strong> — surrounding mandals/taluks, villages, and agricultural land</li>
                    <li><strong>Farms &amp; farmhouses</strong> — open-plot, off-grid, and hybrid systems across @@REGION@@</li>
                    <li><strong>Industry &amp; business</strong> — factories, hotels, cold storage, and commercial buildings</li>
                </ul>

                <h2>Best Products for @@NAME@@</h2>
                <table class="spec-table">
                    <thead><tr><th>Property Type</th><th>Recommended</th><th>Annual Output</th></tr></thead>
                    <tbody>
                        <tr><td>Apartment / flat</td><td><a href="../products/helical-vertical-wind-turbine.html">1.5 kW Helical</a></td><td>~2,800-3,500 kWh</td></tr>
                        <tr><td>Bungalow / villa</td><td><a href="../products/helical-vertical-wind-turbine.html">3-5 kW Helical</a></td><td>~5,500-9,500 kWh</td></tr>
                        <tr><td>Farmhouse / large plot</td><td><a href="../products/tulip-vertical-wind-turbine.html">5-10 kW Tulip</a></td><td>~10,000-22,000 kWh</td></tr>
                        <tr><td>Office / shop</td><td><a href="../products/hybrid-solar-wind-system.html">5-15 kW Hybrid</a></td><td>~10,000-30,000 kWh</td></tr>
                        <tr><td>Factory / hotel</td><td>25-100 kW arrays</td><td>~50,000+ kWh</td></tr>
                    </tbody>
                </table>

                <h2>@@NAME@@ Pricing Indicators</h2>
                <ul>
                    <li><strong>1.5 kW rooftop turbine:</strong> ₹1.8-2.5 lakh</li>
                    <li><strong>3 kW residential:</strong> ₹3-5 lakh</li>
                    <li><strong>5 kW Tulip / Hybrid:</strong> ₹6-9 lakh</li>
                    <li><strong>10 kW Hybrid:</strong> ₹14-20 lakh</li>
                </ul>
                <p>All installations include the local @@DISCOM@@ net-metering paperwork, civil works, structural mounting, and 15-25 year warranty.</p>

                <h2>FAQ — Wind Turbine @@NAME@@</h2>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Is @@NAME@@ windy enough for a small wind turbine?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>@@NOTE@@ Our vertical axis turbines start generating at just 3.5 m/s, so they perform reliably across @@NAME@@ and @@DISTRICT@@ district.</p></div></details>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Which DISCOM handles net-metering in @@NAME@@?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>@@DISCOM@@ manages the local grid connection in @@NAME@@. We handle the entire net-metering application and paperwork as part of our turnkey installation.</p></div></details>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Should I choose wind, solar, or hybrid in @@NAME@@?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>For most @@STATE@@ sites we recommend a hybrid solar+wind system — solar covers sunny afternoons while wind covers evenings, nights, and the monsoon, giving the most consistent year-round output.</p></div></details>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Can you install off-grid for a remote @@DISTRICT@@ farm?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>Yes. Given the strong @@WIND@@ wind resource around @@NAME@@, off-grid and battery-backed hybrid systems work very well for remote farms and farmhouses with weak or no grid supply.</p></div></details>
            </div>

            <aside class="content-sidebar">
                <div class="sidebar-card"><h4>Products in @@NAME@@</h4><ul>
                    <li><a href="../products/helical-vertical-wind-turbine.html">Helical Turbine</a></li>
                    <li><a href="../products/tulip-vertical-wind-turbine.html">Tulip Turbine</a></li>
                    <li><a href="../products/hybrid-solar-wind-system.html">Hybrid Solar + Wind</a></li>
                    <li><a href="../products/off-grid-wind-system.html">Off-Grid Systems</a></li>
                </ul></div>
                <div class="sidebar-card"><h4>Wind Turbines in @@STATE@@</h4><ul>
@@SIBLINGS@@
                    <li><a href="../states/@@HUB@@"><strong>All @@STATE@@ &raquo;</strong></a></li>
                </ul></div>
                <div class="sidebar-cta"><h4>@@NAME@@ Video Analysis</h4><p>Free remote analysis, sizing, and quote within 48-72 hours.</p><a href="../index.html#contact" class="btn"><i class="fas fa-arrow-right"></i><span>Book Now</span></a></div>
            </aside>
        </div>
    </div>
</section>

<section class="page-cta">
    <div class="container">
        <h2>Wind &amp; Hybrid Energy in @@NAME@@</h2>
        <p>Free remote video analysis across @@NAME@@ and @@STATE@@. Custom system for your home, farm, or business.</p>
        <div class="page-cta-buttons">
            <a href="../index.html#contact" class="btn btn-primary"><i class="fas fa-search-location"></i><span>@@NAME@@ Video Analysis</span></a>
            <a href="tel:+919137369043" class="btn btn-outline"><i class="fas fa-phone-alt"></i><span>+91 91373 69043</span></a>
        </div>
    </div>
</section>

<a href="https://wa.me/919137369043?text=Hi%20Windora%2C%20@@ENC@@." class="float-btn float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i><span class="float-label">Chat on WhatsApp</span></a>
<a href="tel:+919137369043" class="float-btn float-call" aria-label="Call"><i class="fas fa-phone-alt"></i></a>
<button class="back-to-top" id="backToTop"><i class="fas fa-arrow-up"></i></button>

<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><img src="../assets/images/logo.png" alt="Windora Energy" class="footer-logo"><p>Wind &amp; hybrid energy solutions engineered for Indian conditions.</p><p class="footer-tag"><strong>Engineered for Low Wind Performance.</strong></p></div><div class="footer-links"><h4>Products</h4><ul><li><a href="../products/helical-vertical-wind-turbine.html">Helical Turbine</a></li><li><a href="../products/tulip-vertical-wind-turbine.html">Tulip Turbine</a></li><li><a href="../products/hybrid-solar-wind-system.html">Hybrid Solar + Wind</a></li><li><a href="../products/off-grid-wind-system.html">Off-Grid Systems</a></li></ul></div><div class="footer-links"><h4>States</h4><ul><li><a href="../states/wind-turbine-gujarat.html">Gujarat</a></li><li><a href="../states/wind-turbine-tamil-nadu.html">Tamil Nadu</a></li><li><a href="../states/wind-turbine-karnataka.html">Karnataka</a></li><li><a href="../states/wind-turbine-maharashtra.html">Maharashtra</a></li><li><a href="../states/wind-turbine-rajasthan.html">Rajasthan</a></li></ul></div><div class="footer-contact"><h4>Get in Touch</h4><p><i class="fas fa-map-marker-alt"></i> Mira Road East, MH 401107</p><p><i class="fas fa-phone-alt"></i> <a href="tel:+919137369043">+91 91373 69043</a></p><p><i class="fas fa-envelope"></i> <a href="mailto:info@windoraenergy.com">info@windoraenergy.com</a></p></div></div><div class="footer-bottom"><p>&copy; 2026 Windora Energy. All rights reserved.</p></div></div></footer>
<script src="../assets/js/main.js"></script>
</body>
</html>
'''

by_state = {}
for c in CITIES:
    by_state.setdefault(c[2], []).append(c)

written = []
for (name, slug, state, code, district, region, discom, wind, wq, hub, note) in CITIES:
    sibs = [s for s in by_state[state] if s[1] != slug]
    sib_items = "\n".join(f'                    <li><a href="wind-turbine-{s[1]}.html">{s[0]}</a></li>' for s in sibs)
    note_plain = note.replace("—", "-").replace("+", "and")
    html = TEMPLATE
    for k, v in {
        "@@NAME@@": name, "@@ENC@@": name.replace(" ", "%20"), "@@SLUG@@": slug,
        "@@STATE@@": state, "@@CODE@@": code, "@@DISTRICT@@": district, "@@REGION@@": region,
        "@@DISCOM@@": discom, "@@WIND@@": wind, "@@WQ@@": wq,
        "@@WQCAP@@": wq[0].upper() + wq[1:], "@@HUB@@": hub, "@@NOTE@@": note,
        "@@NOTE_PLAIN@@": note_plain, "@@SIBLINGS@@": sib_items,
    }.items():
        html = html.replace(k, v)
    path = os.path.join(BASE, "cities", f"wind-turbine-{slug}.html")
    with open(path, "w") as fp:
        fp.write(html)
    written.append(f"cities/wind-turbine-{slug}.html")

print(f"WROTE {len(written)} pages")
for w in written:
    print("  " + w)
