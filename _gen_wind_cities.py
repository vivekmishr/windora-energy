#!/usr/bin/env python3
"""Wind-belt town page generator — 56 high wind-potential locations across 5 states.

Companion to _gen_city.py (which builds the 14 metro pages). These are smaller
wind-corridor towns; content is driven by accurate per-town wind geography, with
district-level coverage (no fabricated neighbourhood lists). Pune is intentionally
omitted — it already has a metro page at cities/wind-turbine-pune.html.
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

# Per-state shared config
STATES = {
    "Gujarat":     {"code": "IN-GJ", "slug": "gujarat",       "hub": "wind-turbine-gujarat.html"},
    "Tamil Nadu":  {"code": "IN-TN", "slug": "tamil-nadu",    "hub": "wind-turbine-tamil-nadu.html"},
    "Karnataka":   {"code": "IN-KA", "slug": "karnataka",     "hub": "wind-turbine-karnataka.html"},
    "Maharashtra": {"code": "IN-MH", "slug": "maharashtra",   "hub": "wind-turbine-maharashtra.html"},
    "Rajasthan":   {"code": "IN-RJ", "slug": "rajasthan",     "hub": "wind-turbine-rajasthan.html"},
}

# name, slug, state, district, region, discom, wind_range, wind_quality, note
CITIES = [
    # ---------------- Gujarat (PGVCL — Saurashtra & Kutch) ----------------
    ("Bhuj", "bhuj", "Gujarat", "Kutch", "Kutch", "PGVCL", "5-7 m/s", "excellent",
     "Bhuj sits in the heart of Kutch, one of India's premier wind regions, where the Gulf of Kutch sea-breeze and open desert plains deliver some of the strongest, most consistent winds in the country."),
    ("Kutch", "kutch", "Gujarat", "Kutch", "Kutch", "PGVCL", "6-8 m/s", "excellent",
     "The Kutch region — from the Gulf coast to the Banni grasslands — is among the windiest districts in India, with large utility wind farms already operating around Naliya, Lakhpat, and Mandvi."),
    ("Mandvi", "mandvi", "Gujarat", "Kutch", "coastal Kutch", "PGVCL", "5-7 m/s", "excellent",
     "Mandvi's Arabian Sea coastline gives it a powerful, year-round onshore sea-breeze — ideal for both rooftop and ground-mounted vertical axis turbines."),
    ("Naliya", "naliya", "Gujarat", "Kutch", "Kutch", "PGVCL", "6-8 m/s", "excellent",
     "Naliya (Nakhatrana taluka) is one of the windiest locations in India and already hosts major wind farms — making it outstanding for small wind and hybrid systems."),
    ("Jamnagar", "jamnagar", "Gujarat", "Jamnagar", "Saurashtra coast", "PGVCL", "5-7 m/s", "excellent",
     "Jamnagar, on the Gulf of Kutch, combines a strong coastal wind regime with heavy industrial power demand from its refineries and brass industry."),
    ("Porbandar", "porbandar", "Gujarat", "Porbandar", "Saurashtra coast", "PGVCL", "5-7 m/s", "excellent",
     "Porbandar's exposed Saurashtra coastline delivers steady onshore winds throughout the year, well-suited to homes, farms, and coastal businesses."),
    ("Dwarka", "dwarka", "Gujarat", "Devbhumi Dwarka", "Saurashtra coast", "PGVCL", "6-8 m/s", "excellent",
     "Dwarka, on Gujarat's western tip, is one of the windiest coastal towns in India — strong, reliable sea-breeze makes it ideal for wind energy."),
    ("Okha", "okha", "Gujarat", "Devbhumi Dwarka", "Saurashtra coast", "PGVCL", "6-8 m/s", "excellent",
     "Okha, at the western extremity of Saurashtra, has an exceptional coastal wind resource driven by the open Arabian Sea — excellent for off-grid and hybrid systems."),
    ("Rajkot", "rajkot", "Gujarat", "Rajkot", "Saurashtra", "PGVCL", "4-6 m/s", "very good",
     "Rajkot, the commercial heart of Saurashtra, sits on open plains with steady winds and high industrial and residential power demand."),
    ("Morbi", "morbi", "Gujarat", "Morbi", "Saurashtra", "PGVCL", "4-6 m/s", "very good",
     "Morbi — India's ceramic capital — pairs a strong Saurashtra wind resource with very high industrial loads, giving wind and hybrid systems fast payback."),
    ("Surendranagar", "surendranagar", "Gujarat", "Surendranagar", "Saurashtra", "PGVCL", "4-6 m/s", "very good",
     "Surendranagar, on the edge of the Little Rann, has wide-open plains and dry, steady winds well-suited to wind generation."),
    ("Bhavnagar", "bhavnagar", "Gujarat", "Bhavnagar", "Gulf of Khambhat", "PGVCL", "4-6 m/s", "very good",
     "Bhavnagar, on the Gulf of Khambhat, benefits from a strong onshore sea-breeze and a large industrial and shipbreaking economy."),
    ("Amreli", "amreli", "Gujarat", "Amreli", "Saurashtra", "PGVCL", "4-6 m/s", "very good",
     "Amreli, in interior Saurashtra, lies in an established wind-farm belt with reliable seasonal winds for residential and agricultural use."),
    ("Junagadh", "junagadh", "Gujarat", "Junagadh", "Saurashtra", "PGVCL", "4-6 m/s", "very good",
     "Junagadh, near the Girnar hills and the Saurashtra coast, sees consistent winds enhanced by its varied terrain."),

    # ---------------- Tamil Nadu (TANGEDCO) ----------------
    ("Coimbatore", "coimbatore", "Tamil Nadu", "Coimbatore", "Palghat Gap", "TANGEDCO", "5-7 m/s", "excellent",
     "Coimbatore sits beside the Palghat Gap, a natural funnel in the Western Ghats that gives the region one of the strongest, most famous wind resources in India."),
    ("Tirunelveli", "tirunelveli", "Tamil Nadu", "Tirunelveli", "Aralvaimozhi Gap", "TANGEDCO", "6-8 m/s", "excellent",
     "Tirunelveli lies along the Aralvaimozhi and Shengottai wind gaps — part of the Muppandal corridor, the largest onshore wind cluster in Asia."),
    ("Thoothukudi", "thoothukudi", "Tamil Nadu", "Thoothukudi", "Gulf of Mannar coast", "TANGEDCO", "5-7 m/s", "excellent",
     "Thoothukudi (Tuticorin), on the Gulf of Mannar, combines a powerful coastal wind regime with major port and industrial demand."),
    ("Kanyakumari", "kanyakumari", "Tamil Nadu", "Kanyakumari", "Muppandal", "TANGEDCO", "6-9 m/s", "excellent",
     "Kanyakumari is home to Muppandal — one of Asia's largest wind farms — thanks to the extreme, year-round winds funnelled through India's southern tip."),
    ("Tenkasi", "tenkasi", "Tamil Nadu", "Tenkasi", "Shengottai Gap", "TANGEDCO", "6-8 m/s", "excellent",
     "Tenkasi sits at the Shengottai gap in the Western Ghats, channelling strong, consistent winds across the district."),
    ("Dindigul", "dindigul", "Tamil Nadu", "Dindigul", "Palani foothills", "TANGEDCO", "5-7 m/s", "excellent",
     "Dindigul, at the foot of the Palani Hills, lies in an established wind-farm belt with strong seasonal winds."),
    ("Madurai", "madurai", "Tamil Nadu", "Madurai", "southern Tamil Nadu", "TANGEDCO", "4-6 m/s", "very good",
     "Madurai, on the southern Tamil Nadu plains, has a steady wind resource and high year-round cooling loads."),
    ("Erode", "erode", "Tamil Nadu", "Erode", "Kongu", "TANGEDCO", "4-6 m/s", "very good",
     "Erode, in the Kongu wind belt, sees reliable winds well-suited to textile units, farms, and homes."),
    ("Salem", "salem", "Tamil Nadu", "Salem", "Kongu", "TANGEDCO", "4-6 m/s", "very good",
     "Salem's hilly Kongu terrain creates good wind exposure for residential and commercial systems."),
    ("Namakkal", "namakkal", "Tamil Nadu", "Namakkal", "Kongu plateau", "TANGEDCO", "5-7 m/s", "excellent",
     "Namakkal's windy plateau already hosts wind farms and pairs well with its large poultry and agri-business loads."),
    ("Karur", "karur", "Tamil Nadu", "Karur", "Kongu", "TANGEDCO", "5-7 m/s", "excellent",
     "Karur sits in a well-known Tamil Nadu wind-farm belt with strong, consistent winds for homes, textile units, and farms."),

    # ---------------- Karnataka (BESCOM / HESCOM / GESCOM / MESCOM) ----------------
    ("Chitradurga", "chitradurga", "Karnataka", "Chitradurga", "North Karnataka plateau", "BESCOM", "5-7 m/s", "excellent",
     "Chitradurga is one of Karnataka's flagship wind regions, with large wind farms across its open, elevated plateau."),
    ("Gadag", "gadag", "Karnataka", "Gadag", "North Karnataka", "HESCOM", "5-7 m/s", "excellent",
     "Gadag — site of the Kappatagudda hills wind farms — has a strong, steady wind resource across North Karnataka."),
    ("Ballari", "ballari", "Karnataka", "Ballari", "Deccan plateau", "GESCOM", "4-6 m/s", "very good",
     "Ballari (Bellary), on the open Deccan plateau, combines good winds with high industrial demand."),
    ("Vijayapura", "vijayapura", "Karnataka", "Vijayapura", "North Karnataka", "HESCOM", "4-6 m/s", "very good",
     "Vijayapura (Bijapur), on the North Karnataka plateau, has dry, steady winds well-suited to wind generation."),
    ("Belagavi", "belagavi", "Karnataka", "Belagavi", "Western Karnataka", "HESCOM", "4-6 m/s", "very good",
     "Belagavi (Belgaum), near the Western Ghats, sees reliable winds enhanced by its varied terrain."),
    ("Dharwad", "dharwad", "Karnataka", "Dharwad", "Hubli-Dharwad belt", "HESCOM", "4-6 m/s", "very good",
     "Dharwad, in the Hubli-Dharwad belt, has a consistent wind resource and growing commercial demand."),
    ("Haveri", "haveri", "Karnataka", "Haveri", "North Karnataka", "HESCOM", "5-7 m/s", "excellent",
     "Haveri lies in an active North Karnataka wind-farm zone with strong, dependable winds."),
    ("Koppal", "koppal", "Karnataka", "Koppal", "Deccan plateau", "GESCOM", "4-6 m/s", "very good",
     "Koppal, on the open Deccan plateau, has steady winds suited to farms, homes, and industry."),
    ("Tumakuru", "tumakuru", "Karnataka", "Tumakuru", "central Karnataka", "BESCOM", "4-6 m/s", "very good",
     "Tumakuru (Tumkur), on Karnataka's central plateau, has good wind exposure and fast-growing power demand."),
    ("Davanagere", "davanagere", "Karnataka", "Davanagere", "central Karnataka", "BESCOM", "5-7 m/s", "excellent",
     "Davanagere, in central Karnataka's wind belt, has a strong, consistent wind resource for residential and industrial use."),
    ("Shivamogga", "shivamogga", "Karnataka", "Shivamogga", "Malnad foothills", "MESCOM", "4-6 m/s", "very good",
     "Shivamogga (Shimoga), in the Malnad foothills, sees reliable monsoon and seasonal winds."),

    # ---------------- Maharashtra (MSEDCL) — Pune omitted (metro page exists) ----------------
    ("Satara", "satara", "Maharashtra", "Satara", "Sahyadri ghats", "MSEDCL", "6-8 m/s", "excellent",
     "Satara's Chalkewadi and Vankusawade plateaus host some of India's largest wind farms — its Sahyadri ridge winds are outstanding."),
    ("Sangli", "sangli", "Maharashtra", "Sangli", "Sahyadri", "MSEDCL", "5-7 m/s", "excellent",
     "Sangli, along the Sahyadri ranges, lies in a major Maharashtra wind-farm belt with strong, steady winds."),
    ("Kolhapur", "kolhapur", "Maharashtra", "Kolhapur", "Western Ghats", "MSEDCL", "5-7 m/s", "excellent",
     "Kolhapur, at the foot of the Western Ghats, has excellent ridge-and-pass winds and high residential and industrial demand."),
    ("Dhule", "dhule", "Maharashtra", "Dhule", "Khandesh", "MSEDCL", "5-7 m/s", "excellent",
     "Dhule, in the Khandesh wind corridor, already hosts extensive wind farms and offers a strong, reliable resource."),
    ("Ahmednagar", "ahmednagar", "Maharashtra", "Ahmednagar", "western Maharashtra", "MSEDCL", "5-7 m/s", "excellent",
     "Ahmednagar — with the Supa and Parner wind clusters — sits in one of Maharashtra's most active wind regions."),
    ("Nashik", "nashik", "Maharashtra", "Nashik", "Deccan plateau", "MSEDCL", "4-6 m/s", "very good",
     "Nashik, on the Deccan plateau near the Western Ghats, has good winds and strong residential, agri, and industrial demand."),
    ("Solapur", "solapur", "Maharashtra", "Solapur", "Maharashtra plains", "MSEDCL", "4-6 m/s", "very good",
     "Solapur, on the open Maharashtra plains, has a dry, steady wind resource and intense summer cooling loads."),
    ("Aurangabad", "aurangabad", "Maharashtra", "Chhatrapati Sambhajinagar", "Marathwada", "MSEDCL", "4-6 m/s", "very good",
     "Aurangabad (Chhatrapati Sambhajinagar), a major Marathwada industrial hub, pairs steady winds with high commercial demand."),
    ("Beed", "beed", "Maharashtra", "Beed", "Marathwada", "MSEDCL", "4-6 m/s", "very good",
     "Beed, in interior Marathwada, has wide-open plains and reliable seasonal winds for farms and homes."),
    ("Osmanabad", "osmanabad", "Maharashtra", "Dharashiv", "Marathwada", "MSEDCL", "4-6 m/s", "very good",
     "Osmanabad (Dharashiv), on the Marathwada plateau, has a steady wind resource well-suited to agricultural and residential systems."),

    # ---------------- Rajasthan (JdVVNL / JVVNL / AVVNL) ----------------
    ("Jaisalmer", "jaisalmer", "Rajasthan", "Jaisalmer", "Thar Desert", "JdVVNL", "6-8 m/s", "excellent",
     "Jaisalmer is the heart of India's Thar wind-and-solar belt — its vast open desert delivers among the strongest, most consistent winds in the country."),
    ("Barmer", "barmer", "Rajasthan", "Barmer", "Thar Desert", "JdVVNL", "6-8 m/s", "excellent",
     "Barmer, deep in the Thar Desert, has an exceptional wind and solar resource across its open arid plains."),
    ("Jodhpur", "jodhpur", "Rajasthan", "Jodhpur", "Thar edge", "JdVVNL", "5-7 m/s", "excellent",
     "Jodhpur, on the edge of the Thar, combines strong desert winds with extreme summer cooling loads — ideal for hybrid wind+solar."),
    ("Bikaner", "bikaner", "Rajasthan", "Bikaner", "Thar Desert", "JdVVNL", "5-7 m/s", "excellent",
     "Bikaner's open desert terrain gives it a powerful, dependable wind resource for homes, farms, and industry."),
    ("Nagaur", "nagaur", "Rajasthan", "Nagaur", "western Rajasthan", "JdVVNL", "5-7 m/s", "excellent",
     "Nagaur, in arid central-western Rajasthan, sits in an active wind-farm belt with strong, steady winds."),
    ("Pali", "pali", "Rajasthan", "Pali", "western Rajasthan", "JdVVNL", "4-6 m/s", "very good",
     "Pali, in western Rajasthan, has reliable winds and high industrial demand from its textile clusters."),
    ("Sikar", "sikar", "Rajasthan", "Sikar", "Shekhawati", "JVVNL", "4-6 m/s", "very good",
     "Sikar, in the Shekhawati region, has dry, steady winds well-suited to wind and hybrid systems."),
    ("Jhunjhunu", "jhunjhunu", "Rajasthan", "Jhunjhunu", "Shekhawati", "JVVNL", "4-6 m/s", "very good",
     "Jhunjhunu, in Shekhawati, sees consistent winds across its open semi-arid terrain."),
    ("Ajmer", "ajmer", "Rajasthan", "Ajmer", "Aravalli belt", "AVVNL", "4-6 m/s", "very good",
     "Ajmer, in the Aravalli belt, has good wind exposure shaped by its hills and open valleys."),
    ("Udaipur", "udaipur", "Rajasthan", "Udaipur", "Aravalli hills", "AVVNL", "4-6 m/s", "very good",
     "Udaipur, set among the Aravalli hills and lakes, has varied terrain that creates good local wind conditions."),
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wind Turbine in @@NAME@@ | Vertical VAWT &amp; Hybrid Systems | Windora Energy</title>
    <meta name="description" content="Wind turbine in @@NAME@@ — vertical axis turbines for homes, farms, and businesses across @@NAME@@ &amp; @@STATE@@. @@WINDQUALITY_CAP@@ wind resource (@@WINDRANGE@@), low-wind optimized, near-silent. Free video analysis from Windora Energy.">
    <meta name="keywords" content="wind turbine in @@NAME@@, vertical wind turbine @@NAME@@, rooftop wind turbine @@NAME@@, residential wind turbine @@NAME@@, wind energy @@NAME@@, hybrid solar wind @@NAME@@, small wind turbine @@NAME@@, @@STATE@@ wind turbine, Windora @@NAME@@">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="geo.region" content="@@STATECODE@@">
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
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://windoraenergy.com/"},{"@type":"ListItem","position":2,"name":"@@STATE@@","item":"https://windoraenergy.com/states/@@STATEHUB@@"},{"@type":"ListItem","position":3,"name":"Wind Turbine in @@NAME@@","item":"https://windoraenergy.com/cities/wind-turbine-@@SLUG@@.html"}]}</script>
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
<nav class="navbar scrolled" id="navbar"><div class="nav-container"><a href="../index.html" class="nav-logo"><img src="../assets/images/logo.png" alt="Wind Turbine @@NAME@@ — Windora" class="logo-img"></a><ul class="nav-menu" id="navMenu"><li class="nav-item"><a href="../index.html" class="nav-link">Home</a></li><li class="nav-item"><a href="../index.html#products" class="nav-link">Products</a></li><li class="nav-item"><a href="../index.html#sectors" class="nav-link">Solutions</a></li><li class="nav-item"><a href="../blog/index.html" class="nav-link">Blog</a></li><li class="nav-item"><a href="../index.html#contact" class="nav-link cta-btn">Get Free Video Analysis</a></li></ul><div class="hamburger" id="hamburger"><span></span><span></span><span></span></div></div></nav>

<section class="subpage-hero">
    <div class="container">
        <nav class="breadcrumbs"><a href="../index.html">Home</a><span class="sep">›</span><a href="../states/@@STATEHUB@@">@@STATE@@</a><span class="sep">›</span><span class="current">Wind Turbine in @@NAME@@</span></nav>
        <span class="subpage-tag">@@NAME@@ &amp; @@REGION@@</span>
        <h1 class="subpage-title">Wind Turbine in @@NAME@@</h1>
        <p class="subpage-subtitle">@@NOTE@@ Windora installs low-wind vertical axis wind turbines and hybrid solar+wind systems for homes, farms, and businesses across @@NAME@@ and @@DISTRICT@@ district.</p>
        <div class="subpage-hero-cta">
            <a href="../index.html#contact" class="btn btn-primary"><i class="fas fa-search-location"></i><span>@@NAME@@ Video Analysis</span></a>
            <a href="https://wa.me/919137369043?text=Hi%20Windora%2C%20@@NAME_ENC@@%20wind%20turbine%20enquiry." class="btn btn-outline" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i><span>WhatsApp</span></a>
        </div>
    </div>
</section>

<section class="content-section">
    <div class="container">
        <div class="content-grid">
            <div class="content-main">
                <h2>Why Wind Energy Works in @@NAME@@</h2>
                <p>@@NOTE@@ With annual averages around <strong>@@WINDRANGE@@</strong>, @@NAME@@ is a @@WINDQUALITY@@ fit for Windora's vertical axis wind turbines, which start generating at just 3.5 m/s.</p>
                <ul>
                    <li>@@WINDQUALITY_CAP@@ wind resource — @@REGION@@ is among India's stronger wind zones</li>
                    <li>@@DISCOM@@ grid tariffs climb steeply at higher consumption slabs</li>
                    <li>High summer cooling loads across @@STATE@@ — fast payback on self-generation</li>
                    <li>@@STATE@@ renewable-energy incentives + accelerated depreciation for businesses</li>
                    <li>Strong fit for farms, farmhouses, homes, and industry around @@NAME@@</li>
                </ul>

                <div class="callout">
                    <p><strong>Why it pays off:</strong> A 5 kW hybrid solar+wind system in @@NAME@@ can generate roughly 10,000–16,000 kWh a year given the local @@WINDRANGE@@ wind resource — typically cutting a high @@DISCOM@@ bill by 70–90% with a 4–6 year payback.</p>
                </div>

                <h2>Coverage Across @@DISTRICT@@</h2>
                <ul>
                    <li><strong>@@NAME@@ town</strong> — rooftop and ground-mounted systems for homes, shops, and offices</li>
                    <li><strong>@@DISTRICT@@ district</strong> — surrounding taluks, villages, and agricultural land</li>
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

                <div data-nosnippet>

                <h2>@@NAME@@ Pricing Indicators</h2>
                <ul>
                    <li><strong>1.5 kW rooftop turbine:</strong> ₹1.8-2.5 lakh</li>
                    <li><strong>3 kW residential:</strong> ₹3-5 lakh</li>
                    <li><strong>5 kW Tulip / Hybrid:</strong> ₹6-9 lakh</li>
                    <li><strong>10 kW Hybrid:</strong> ₹14-20 lakh</li>
                </ul>

                </div>
                <p>All installations include the local @@DISCOM@@ net-metering paperwork, civil works, structural mounting, and 15-25 year warranty.</p>

                <h2>FAQ — Wind Turbine @@NAME@@</h2>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Is @@NAME@@ windy enough for a small wind turbine?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>@@NOTE@@ Our vertical axis turbines start generating at just 3.5 m/s, so they perform reliably across @@NAME@@ and @@DISTRICT@@ district.</p></div></details>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Which DISCOM handles net-metering in @@NAME@@?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>@@DISCOM@@ manages the local grid connection in @@NAME@@. We handle the entire net-metering application and paperwork as part of our turnkey installation.</p></div></details>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Should I choose wind, solar, or hybrid in @@NAME@@?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>For most @@STATE@@ sites we recommend a hybrid solar+wind system — solar covers sunny afternoons while wind covers evenings, nights, and the monsoon, giving the most consistent year-round output.</p></div></details>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Can you install off-grid for a remote @@DISTRICT@@ farm?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>Yes. Given the strong @@WINDRANGE@@ wind resource around @@NAME@@, off-grid and battery-backed hybrid systems work very well for remote farms and farmhouses with weak or no grid supply.</p></div></details>
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
                    <li><a href="../states/@@STATEHUB@@"><strong>All @@STATE@@ &raquo;</strong></a></li>
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

<a href="https://wa.me/919137369043?text=Hi%20Windora%2C%20@@NAME_ENC@@." class="float-btn float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i><span class="float-label">Chat on WhatsApp</span></a>
<a href="tel:+919137369043" class="float-btn float-call" aria-label="Call"><i class="fas fa-phone-alt"></i></a>
<button class="back-to-top" id="backToTop"><i class="fas fa-arrow-up"></i></button>

<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><img src="../assets/images/logo.png" alt="Windora Energy" class="footer-logo"><p>Wind &amp; hybrid energy solutions engineered for Indian conditions.</p><p class="footer-tag"><strong>Engineered for Low Wind Performance.</strong></p></div><div class="footer-links"><h4>Products</h4><ul><li><a href="../products/helical-vertical-wind-turbine.html">Helical Turbine</a></li><li><a href="../products/tulip-vertical-wind-turbine.html">Tulip Turbine</a></li><li><a href="../products/hybrid-solar-wind-system.html">Hybrid Solar + Wind</a></li><li><a href="../products/off-grid-wind-system.html">Off-Grid Systems</a></li></ul></div><div class="footer-links"><h4>States</h4><ul><li><a href="../states/wind-turbine-gujarat.html">Gujarat</a></li><li><a href="../states/wind-turbine-tamil-nadu.html">Tamil Nadu</a></li><li><a href="../states/wind-turbine-karnataka.html">Karnataka</a></li><li><a href="../states/wind-turbine-maharashtra.html">Maharashtra</a></li><li><a href="../states/wind-turbine-rajasthan.html">Rajasthan</a></li></ul></div><div class="footer-contact"><h4>Get in Touch</h4><p><i class="fas fa-map-marker-alt"></i> Mira Road East, MH 401107</p><p><i class="fas fa-phone-alt"></i> <a href="tel:+919137369043">+91 91373 69043</a></p><p><i class="fas fa-envelope"></i> <a href="mailto:info@windoraenergy.com">info@windoraenergy.com</a></p></div></div><div class="footer-bottom"><p>&copy; 2026 Windora Energy. All rights reserved.</p></div></div></footer>
<script src="../assets/js/main.js"></script>
</body>
</html>
'''

# index towns by state for sibling links
by_state = {}
for c in CITIES:
    by_state.setdefault(c[2], []).append(c)

written = []
for (name, slug, state, district, region, discom, wind_range, wind_quality, note) in CITIES:
    st = STATES[state]
    # sibling list: up to 7 other towns in same state
    sibs = [s for s in by_state[state] if s[1] != slug][:7]
    sib_items = "\n".join(
        f'                    <li><a href="wind-turbine-{s[1]}.html">{s[0]}</a></li>' for s in sibs
    )
    html = TEMPLATE
    repl = {
        "@@NAME@@": name,
        "@@NAME_ENC@@": name.replace(" ", "%20"),
        "@@SLUG@@": slug,
        "@@STATE@@": state,
        "@@STATECODE@@": st["code"],
        "@@STATEHUB@@": st["hub"],
        "@@DISTRICT@@": district,
        "@@REGION@@": region,
        "@@DISCOM@@": discom,
        "@@WINDRANGE@@": wind_range,
        "@@WINDQUALITY@@": wind_quality,
        "@@WINDQUALITY_CAP@@": wind_quality[0].upper() + wind_quality[1:],
        "@@NOTE@@": note,
        "@@SIBLINGS@@": sib_items,
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    path = os.path.join(BASE, "cities", f"wind-turbine-{slug}.html")
    with open(path, "w") as fp:
        fp.write(html)
    written.append(f"cities/wind-turbine-{slug}.html")

print(f"WROTE {len(written)} city pages")
for w in written:
    print("  " + w)
