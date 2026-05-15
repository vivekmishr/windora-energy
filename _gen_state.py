#!/usr/bin/env python3
"""State page generator — produces SEO state-level pages."""

STATES = [
    {
        "slug": "maharashtra",
        "name": "Maharashtra",
        "code": "IN-MH",
        "intro": "Maharashtra is one of India's most progressive renewable energy markets — strong industrial demand, supportive MSEDCL net-metering policy, varied geography (coastal Konkan to plateau Vidarbha) that suits wind energy, and rising tariffs that accelerate payback. Windora delivers vertical axis wind turbines, solar panels, and hybrid systems across the entire state.",
        "geography": "Maharashtra spans coastal Konkan, the Mumbai metro, the Western Ghats, the Pune-Nashik plateau, and the Vidarbha plains. This range gives diverse wind regimes — coastal Mumbai sees 4-7 m/s, plateau Pune 3-5 m/s, Vidarbha 3-4 m/s, and the Western Ghats above 6 m/s in season.",
        "wind_avg": "3-7 m/s (varies by region)",
        "discom": "MSEDCL (statewide), Adani Electricity / Tata Power (Mumbai island), Torrent Power (Surat-Maharashtra border)",
        "factors": [
            "MSEDCL slabs reach ₹13+/unit residential, higher for commercial",
            "Active state net-metering policy",
            "Industrial corridor — Pune-Nashik, MIDC zones, Aurangabad, Nagpur",
            "Strong Mumbai metro market with high tariffs and frequent cuts",
            "Maharashtra State Renewable Energy Development Agency (MEDA) schemes",
        ],
        "cities": [
            ("Mumbai", "wind-turbine-mumbai.html"),
            ("Pune", "wind-turbine-pune.html"),
            ("Nagpur", "wind-turbine-nagpur.html"),
        ],
        "extra_areas": "Thane, Navi Mumbai, Kalyan-Dombivli, Vasai-Virar, Mira-Bhayandar, Nashik, Aurangabad, Solapur, Kolhapur, Amravati, Latur, Akola, Sangli, Ratnagiri, Sindhudurg, Chandrapur, Wardha, Beed, Buldhana, Nanded",
    },
    {
        "slug": "gujarat",
        "name": "Gujarat",
        "code": "IN-GJ",
        "intro": "Gujarat is India's premier wind state — long coastline, open plains, and the most supportive renewable energy policy framework. Wind turbines work exceptionally well across Gujarat for both residential and commercial sites, with payback periods among the shortest in India.",
        "geography": "Gujarat's western coastline runs from the Gulf of Kutch to the Gulf of Khambhat — strong sea-breeze in all major cities. Inland plains add steady terrestrial winds. Annual averages range 4-7 m/s across most populated areas.",
        "wind_avg": "4-7 m/s (excellent)",
        "discom": "Torrent Power (Ahmedabad/Surat), DGVCL, UGVCL, MGVCL, PGVCL (zones)",
        "factors": [
            "Best urban wind resource of any Indian state",
            "Gujarat's pioneer renewable energy policy + accelerated depreciation",
            "Strong industrial demand (Sanand, Hazira, Jamnagar, Ankleshwar)",
            "Cyclone-grade engineering already standard for Gujarat installations",
            "Diamond/textile/petrochemical industries — large commercial demand",
        ],
        "cities": [
            ("Ahmedabad", "wind-turbine-ahmedabad.html"),
            ("Surat", "wind-turbine-surat.html"),
        ],
        "extra_areas": "Vadodara, Rajkot, Bhavnagar, Jamnagar, Gandhinagar, Junagadh, Anand, Nadiad, Mehsana, Bharuch, Ankleshwar, Vapi, Navsari, Valsad, Porbandar, Bhuj, Morbi, Surendranagar",
    },
    {
        "slug": "karnataka",
        "name": "Karnataka",
        "code": "IN-KA",
        "intro": "Karnataka combines a strong wind resource (especially on the Deccan plateau and along the Western Ghats) with a fast-growing IT/tech sector chasing ESG goals. Windora installs vertical axis turbines and hybrid systems for residential, commercial, and agricultural sites across the state.",
        "geography": "Karnataka rises from the Arabian Sea coast through the Western Ghats up to the Deccan plateau where Bengaluru sits at ~920 metres. Coastal regions see 5-7 m/s; plateau cities 3-5 m/s; the western ghat passes can exceed 8 m/s seasonally.",
        "wind_avg": "3-7 m/s",
        "discom": "BESCOM (Bangalore), MESCOM, HESCOM, GESCOM, CESC Mysore",
        "factors": [
            "BESCOM tariffs progressive; commercial slabs high",
            "IT sector ESG goals push corporate renewable adoption",
            "Karnataka's renewable policy among India's best",
            "Coffee/spice estates in Coorg, Chikmagalur — strong wind exposure",
            "Coastal Mangalore-Karwar belt — excellent wind resource",
        ],
        "cities": [
            ("Bangalore", "wind-turbine-bangalore.html"),
        ],
        "extra_areas": "Mysore, Mangalore, Hubli-Dharwad, Belgaum, Gulbarga, Bellary, Davangere, Tumkur, Shivamogga, Hassan, Mandya, Udupi, Coorg, Chikmagalur, Bidar, Raichur, Bagalkot",
    },
    {
        "slug": "tamil-nadu",
        "name": "Tamil Nadu",
        "code": "IN-TN",
        "intro": "Tamil Nadu is India's wind energy powerhouse — home to the Muppandal wind farm corridor and decades of utility-scale wind experience. The state's coastal urban areas also benefit from exceptional wind resources for small/residential turbines. Windora serves Chennai, Coimbatore, Madurai, and the entire TN region.",
        "geography": "Tamil Nadu's geography uniquely concentrates wind — the Palghat Gap funnels strong winds across the state from June through September, while the Coromandel coast brings steady sea-breeze year-round. Average winds range from 5-8 m/s in much of the state.",
        "wind_avg": "5-8 m/s (best in India)",
        "discom": "TANGEDCO (statewide)",
        "factors": [
            "Best wind state in India — strongest urban + commercial resource",
            "TANGEDCO net-metering supportive",
            "Strong industrial base — Sriperumbudur, Oragadam, Hosur, Coimbatore",
            "Coastal cyclone exposure — handled by our 55 m/s survival rating",
            "Tamil Nadu Energy Development Agency (TEDA) renewable schemes",
        ],
        "cities": [
            ("Chennai", "wind-turbine-chennai.html"),
        ],
        "extra_areas": "Coimbatore, Madurai, Tiruchirappalli, Salem, Tirunelveli, Erode, Vellore, Tuticorin, Kanchipuram, Hosur, Tirupur, Karur, Dindigul, Cuddalore, Nagercoil, Kanyakumari, Pondicherry (UT adjacent)",
    },
    {
        "slug": "rajasthan",
        "name": "Rajasthan",
        "code": "IN-RJ",
        "intro": "Rajasthan combines India's strongest desert winds, intense summer AC loads, and rising JVVNL tariffs — creating exceptional ROI for wind energy. From Jaipur urban installations to remote Thar desert off-grid systems, Windora delivers wind + hybrid solutions across the state.",
        "geography": "Rajasthan ranges from semi-arid Aravalli foothills (Jaipur, Udaipur) to true desert (Jaisalmer, Bikaner, Barmer). Strong westerly winds blow across most of the state, with desert zones seeing 6-9 m/s averages.",
        "wind_avg": "4-9 m/s (highest in north-west)",
        "discom": "JVVNL (Jaipur), AVVNL (Ajmer), JdVVNL (Jodhpur)",
        "factors": [
            "Among India's strongest wind resources",
            "Extreme summer AC load = high bills = fast payback",
            "Rajasthan Renewable Energy Corporation (RREC) supports installations",
            "Heritage hotels in Jaipur/Udaipur/Jaisalmer want eco-certification",
            "Many farmhouses and large residential plots",
        ],
        "cities": [
            ("Jaipur", "wind-turbine-jaipur.html"),
        ],
        "extra_areas": "Jodhpur, Udaipur, Kota, Ajmer, Bikaner, Alwar, Bharatpur, Sikar, Pali, Tonk, Bhilwara, Sri Ganganagar, Hanumangarh, Jaisalmer, Barmer, Chittorgarh, Banswara, Dungarpur",
    },
    {
        "slug": "telangana-andhra-pradesh",
        "name": "Telangana &amp; Andhra Pradesh",
        "code": "IN-TG",
        "intro": "The Telangana–Andhra Pradesh region combines coastal AP's strong sea-breeze with Telangana's plateau winds — a productive market for vertical axis wind turbines. From Hyderabad villas to Visakhapatnam coast installations to remote farms, Windora serves the whole region.",
        "geography": "Telangana sits on the Deccan plateau (3-5 m/s), while coastal Andhra Pradesh enjoys exceptional Bay of Bengal sea-breeze (5-8 m/s). Combined, the region has diverse wind profiles suitable for our full product range.",
        "wind_avg": "3-8 m/s (best on AP coast)",
        "discom": "TSSPDCL/TSNPDCL (Telangana), APSPDCL/APEPDCL/APCPDCL (AP)",
        "factors": [
            "Coastal AP — among India's best urban wind",
            "Hyderabad IT/pharma sector ESG demand",
            "AP cyclone exposure — handled by Windora 55 m/s rating",
            "Strong farm/agriculture sector in AP — irrigation + cold storage demand",
            "Telangana RE policy supportive of distributed renewable",
        ],
        "cities": [
            ("Hyderabad", "wind-turbine-hyderabad.html"),
        ],
        "extra_areas": "Visakhapatnam, Vijayawada, Guntur, Tirupati, Nellore, Rajahmundry, Kakinada, Anantapur, Kurnool, Karimnagar, Warangal, Nizamabad, Khammam, Mahbubnagar, Adilabad",
    },
    {
        "slug": "madhya-pradesh",
        "name": "Madhya Pradesh",
        "code": "IN-MP",
        "intro": "Madhya Pradesh — India's heart — combines plateau geography, growing industrial sectors (Pithampur, Mandideep), and a clean-energy culture (Indore is India's cleanest city repeatedly). Windora installs across MP's residential, commercial, and agricultural sectors.",
        "geography": "MP sits on the Malwa-Vindhya plateau at 300-700m elevation. Moderate but consistent winds (3-5 m/s average) with strong monsoon and pre-monsoon periods. Open plains plus elevated terrain suit vertical axis turbines.",
        "wind_avg": "3-5 m/s",
        "discom": "MPMKVVCL (Bhopal), MPPKVVCL (Indore), MPPaKVVCL (Jabalpur)",
        "factors": [
            "MP electricity tariffs at upper slabs significant",
            "Indore-Pithampur industrial corridor — strong commercial market",
            "Cleanest city culture (Indore) drives clean-energy adoption",
            "MP Urja Vikas Nigam schemes for renewable installations",
            "Many farmhouses across Bhopal-Sehore-Vidisha belt",
        ],
        "cities": [
            ("Indore", "wind-turbine-indore.html"),
            ("Bhopal", "wind-turbine-bhopal.html"),
        ],
        "extra_areas": "Jabalpur, Gwalior, Ujjain, Sagar, Dewas, Satna, Ratlam, Rewa, Khargone, Burhanpur, Chhindwara, Singrauli, Hoshangabad, Vidisha, Sehore",
    },
    {
        "slug": "kerala",
        "name": "Kerala",
        "code": "IN-KL",
        "intro": "Kerala combines the Western Ghats' elevated wind, the Arabian Sea coast's reliable monsoon breeze, and India's highest electricity tariffs — making renewable energy especially economical. Windora serves homes, resorts, and commercial buildings across Kochi, Thiruvananthapuram, Kozhikode, and the entire state.",
        "geography": "Kerala's narrow strip between the Western Ghats and Arabian Sea creates a unique wind profile — strong onshore sea-breeze meeting orographic winds from the hills. Annual averages of 3-6 m/s with strong monsoon (June-Sept) and pre-monsoon winds.",
        "wind_avg": "3-6 m/s (strong monsoon peaks)",
        "discom": "KSEB (statewide)",
        "factors": [
            "Kerala has India's highest residential tariffs (₹10-13+/unit)",
            "Strong monsoon winds when solar drops 60-70%",
            "Tourism/hospitality sector chases eco-certification",
            "KSEB net-metering supportive",
            "Many independent homes vs apartments — favourable for installation",
        ],
        "cities": [],
        "extra_areas": "Kochi, Thiruvananthapuram, Kozhikode, Thrissur, Kollam, Palakkad, Alappuzha, Malappuram, Kannur, Kasaragod, Pathanamthitta, Idukki, Ernakulam, Kottayam, Wayanad",
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wind Turbine in {name} | Vertical VAWT &amp; Hybrid Systems | Windora Energy</title>
    <meta name="description" content="Wind turbine in {name} — vertical axis turbines, solar panels, and hybrid green energy systems for homes, farms, and businesses across {name}. Low-wind optimized for Indian conditions. Free site analysis.">
    <meta name="keywords" content="wind turbine {name}, vertical wind turbine {name}, rooftop wind turbine {name}, residential wind turbine {name}, wind energy {name}, hybrid solar wind {name}, small wind turbine {name}, {name} renewable energy">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="geo.region" content="{code}">
    <meta name="geo.placename" content="{name}, India">
    <link rel="canonical" href="https://windoraenergy.com/states/wind-turbine-{slug}.html">
    <link rel="icon" type="image/png" href="../assets/images/logo.png">
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="stylesheet" href="../assets/css/animations.css">
    <link rel="stylesheet" href="../assets/css/extra.css">
    <link rel="stylesheet" href="../assets/css/subpage.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Windora Energy — {name}","image":"https://windoraenergy.com/assets/images/logo.png","telephone":"+91-91373-69043","email":"info@windoraenergy.com","areaServed":{{"@type":"State","name":"{name}"}}}}</script>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://windoraenergy.com/"}},{{"@type":"ListItem","position":3,"name":"Wind Turbine in {name}","item":"https://windoraenergy.com/states/wind-turbine-{slug}.html"}}]}}</script>
    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-N3GTX10XW5"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', 'G-N3GTX10XW5');
    </script>
</head>
<body class="subpage-body">
<div class="top-bar"><div class="top-bar-container"><div class="top-bar-left"><a href="tel:+919137369043"><i class="fas fa-phone-alt"></i> +91 91373 69043</a><a href="mailto:info@windoraenergy.com"><i class="fas fa-envelope"></i> info@windoraenergy.com</a></div><div class="top-bar-right"><span><i class="fas fa-map-marker-alt"></i> {name}</span></div></div></div>
<nav class="navbar scrolled" id="navbar"><div class="nav-container"><a href="../index.html" class="nav-logo"><img src="../assets/images/logo.png" alt="Wind Turbine {name} — Windora" class="logo-img"></a><ul class="nav-menu" id="navMenu"><li class="nav-item"><a href="../index.html" class="nav-link">Home</a></li><li class="nav-item"><a href="../index.html#products" class="nav-link">Products</a></li><li class="nav-item"><a href="../index.html#sectors" class="nav-link">Solutions</a></li><li class="nav-item"><a href="../blog/index.html" class="nav-link">Blog</a></li><li class="nav-item"><a href="../index.html#contact" class="nav-link cta-btn">Get Free Site Analysis</a></li></ul><div class="hamburger" id="hamburger"><span></span><span></span><span></span></div></div></nav>

<section class="subpage-hero">
    <div class="container">
        <nav class="breadcrumbs"><a href="../index.html">Home</a><span class="sep">›</span><span class="current">Wind Turbine in {name}</span></nav>
        <span class="subpage-tag">{name}</span>
        <h1 class="subpage-title">Wind Turbine in {name}</h1>
        <p class="subpage-subtitle">{intro}</p>
        <div class="subpage-hero-cta">
            <a href="../index.html#contact" class="btn btn-primary"><i class="fas fa-search-location"></i><span>{name} Survey</span></a>
            <a href="https://wa.me/919137369043?text=Hi%20Windora%2C%20{name}%20wind%20enquiry." class="btn btn-outline" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i><span>WhatsApp</span></a>
        </div>
    </div>
</section>

<section class="content-section">
    <div class="container">
        <div class="content-grid">
            <div class="content-main">
                <h2>Why Wind Energy in {name}?</h2>
                <p>{geography}</p>
                <p><strong>Average annual wind:</strong> {wind_avg}<br>
                <strong>Major distribution companies:</strong> {discom}</p>

                <h3>Key factors driving wind adoption in {name}:</h3>
                <ul>
{factor_items}
                </ul>

                <h2>Cities &amp; Regions We Serve in {name}</h2>
                {city_links}
                <p>We also serve smaller cities and rural areas across {name}: {extra_areas}.</p>

                <h2>Best Products for {name}</h2>
                <table class="spec-table">
                    <thead><tr><th>Property Type</th><th>Recommended</th><th>Capacity</th></tr></thead>
                    <tbody>
                        <tr><td>Apartment / flat</td><td><a href="../products/helical-vertical-wind-turbine.html">Helical VAWT</a></td><td>1.5 kW</td></tr>
                        <tr><td>Bungalow / villa</td><td><a href="../products/helical-vertical-wind-turbine.html">Helical VAWT</a></td><td>3-5 kW</td></tr>
                        <tr><td>Farmhouse / large plot</td><td><a href="../products/tulip-vertical-wind-turbine.html">Tulip VAWT</a></td><td>5-10 kW</td></tr>
                        <tr><td>Office / commercial</td><td><a href="../products/hybrid-solar-wind-system.html">Hybrid Solar+Wind</a></td><td>5-25 kW</td></tr>
                        <tr><td>Factory / industrial</td><td><a href="../products/hybrid-solar-wind-system.html">Hybrid Solar+Wind</a></td><td>25-100 kW</td></tr>
                        <tr><td>Remote / off-grid site</td><td><a href="../products/off-grid-wind-system.html">Off-Grid System</a></td><td>2-50 kW custom</td></tr>
                    </tbody>
                </table>

                <h2>State-Specific Considerations</h2>
                <p>Each Indian state has its own electricity tariff structure, net-metering rules, and renewable energy policy. In {name}, the local DISCOM is {discom}, and we handle all the necessary documentation and applications as part of our turnkey installation service.</p>
                <p>For accelerated payback, commercial buyers in {name} should also explore:</p>
                <ul>
                    <li><strong>Accelerated depreciation</strong> — 40-80% in year 1 under Income Tax Act</li>
                    <li><strong>State-level renewable energy incentives</strong> — varies year to year, we check current schemes during quote</li>
                    <li><strong>Net-metering credit</strong> — export excess generation at credit rates</li>
                    <li><strong>NABARD / SFAC finance</strong> — for agricultural installations</li>
                </ul>

                <h2>Frequently Asked Questions</h2>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Is {name} windy enough for a small wind turbine?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>Yes — average winds in {name} are within Windora's productive range (we start at 1.5 m/s). We confirm specific site wind via a free survey before quoting.</p></div></details>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>How long does installation take?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>Typically 4-8 weeks from signed quote to live generation. Includes civil works, electrical installation, and DISCOM net-metering paperwork.</p></div></details>
                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>Do you serve smaller towns in {name}?</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>Yes — we install across all populated areas in {name}. For remote sites we add a logistics premium but the system economics still work, especially for off-grid configurations.</p></div></details>
            </div>

            <aside class="content-sidebar">
                <div class="sidebar-card"><h4>Products</h4><ul>
                    <li><a href="../products/helical-vertical-wind-turbine.html">Helical Turbine</a></li>
                    <li><a href="../products/tulip-vertical-wind-turbine.html">Tulip Turbine</a></li>
                    <li><a href="../products/hybrid-solar-wind-system.html">Hybrid Solar + Wind</a></li>
                    <li><a href="../products/off-grid-wind-system.html">Off-Grid Systems</a></li>
                </ul></div>
                <div class="sidebar-card"><h4>Solutions</h4><ul>
                    <li><a href="../solutions/wind-turbine-for-home.html">For Homes</a></li>
                    <li><a href="../solutions/wind-turbine-for-farm.html">For Farms</a></li>
                    <li><a href="../solutions/rooftop-wind-turbine.html">Rooftop Turbines</a></li>
                    <li><a href="../solutions/low-wind-turbine-india.html">Low Wind India</a></li>
                </ul></div>
                <div class="sidebar-card"><h4>Other States</h4><ul>
                    <li><a href="wind-turbine-maharashtra.html">Maharashtra</a></li>
                    <li><a href="wind-turbine-gujarat.html">Gujarat</a></li>
                    <li><a href="wind-turbine-karnataka.html">Karnataka</a></li>
                    <li><a href="wind-turbine-tamil-nadu.html">Tamil Nadu</a></li>
                    <li><a href="wind-turbine-rajasthan.html">Rajasthan</a></li>
                    <li><a href="wind-turbine-telangana-andhra-pradesh.html">Telangana / AP</a></li>
                    <li><a href="wind-turbine-madhya-pradesh.html">Madhya Pradesh</a></li>
                    <li><a href="wind-turbine-kerala.html">Kerala</a></li>
                </ul></div>
                <div class="sidebar-cta"><h4>{name} Site Visit</h4><p>Free survey, custom sizing, written quote within 48 hours.</p><a href="../index.html#contact" class="btn"><i class="fas fa-arrow-right"></i><span>Book Survey</span></a></div>
            </aside>
        </div>
    </div>
</section>

<section class="page-cta">
    <div class="container">
        <h2>Wind &amp; Hybrid Energy Across {name}</h2>
        <p>Free site survey, custom system design, transparent quote. Cities and rural sites alike.</p>
        <div class="page-cta-buttons">
            <a href="../index.html#contact" class="btn btn-primary"><i class="fas fa-search-location"></i><span>{name} Survey</span></a>
            <a href="tel:+919137369043" class="btn btn-outline"><i class="fas fa-phone-alt"></i><span>+91 91373 69043</span></a>
        </div>
    </div>
</section>

<a href="https://wa.me/919137369043?text=Hi%20Windora%2C%20{name}." class="float-btn float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i><span class="float-label">Chat on WhatsApp</span></a>
<a href="tel:+919137369043" class="float-btn float-call" aria-label="Call"><i class="fas fa-phone-alt"></i></a>
<button class="back-to-top" id="backToTop"><i class="fas fa-arrow-up"></i></button>

<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><img src="../assets/images/logo.png" alt="Windora Energy" class="footer-logo"><p>Wind &amp; hybrid energy solutions engineered for Indian conditions.</p><p class="footer-tag"><strong>Engineered for Low Wind Performance.</strong></p></div><div class="footer-links"><h4>Products</h4><ul><li><a href="../products/helical-vertical-wind-turbine.html">Helical Turbine</a></li><li><a href="../products/tulip-vertical-wind-turbine.html">Tulip Turbine</a></li><li><a href="../products/hybrid-solar-wind-system.html">Hybrid Solar + Wind</a></li><li><a href="../products/off-grid-wind-system.html">Off-Grid Systems</a></li></ul></div><div class="footer-links"><h4>States</h4><ul><li><a href="wind-turbine-maharashtra.html">Maharashtra</a></li><li><a href="wind-turbine-gujarat.html">Gujarat</a></li><li><a href="wind-turbine-karnataka.html">Karnataka</a></li><li><a href="wind-turbine-tamil-nadu.html">Tamil Nadu</a></li><li><a href="wind-turbine-rajasthan.html">Rajasthan</a></li><li><a href="wind-turbine-telangana-andhra-pradesh.html">Telangana / AP</a></li><li><a href="wind-turbine-madhya-pradesh.html">MP</a></li><li><a href="wind-turbine-kerala.html">Kerala</a></li></ul></div><div class="footer-contact"><h4>Get in Touch</h4><p><i class="fas fa-map-marker-alt"></i> Mira Road East, MH 401107</p><p><i class="fas fa-phone-alt"></i> <a href="tel:+919137369043">+91 91373 69043</a></p><p><i class="fas fa-envelope"></i> <a href="mailto:info@windoraenergy.com">info@windoraenergy.com</a></p></div></div><div class="footer-bottom"><p>&copy; 2026 Windora Energy. All rights reserved.</p></div></div></footer>
<script src="../assets/js/main.js"></script>
</body>
</html>
'''

for state in STATES:
    factor_items = "\n".join(f"                    <li>{f}</li>" for f in state["factors"])
    if state["cities"]:
        city_links_list = ", ".join(f'<a href="../cities/{slug}">{name}</a>' for name, slug in state["cities"])
        city_links = f"<p>Major cities with dedicated city pages: {city_links_list}.</p>"
    else:
        city_links = ""
    html = TEMPLATE.format(
        factor_items=factor_items,
        city_links=city_links,
        **state
    )
    path = f"states/wind-turbine-{state['slug']}.html"
    with open(path, "w") as fp:
        fp.write(html)
    print(f"WROTE {path}")
