#!/usr/bin/env python3
"""City page generator — produces SEO city pages with per-city content."""

import os

CITIES = [
    {
        "slug": "ahmedabad",
        "name": "Ahmedabad",
        "state": "Gujarat",
        "state_code": "IN-GJ",
        "region_label": "Ahmedabad &amp; Gujarat",
        "subtag": "Ahmedabad &amp; Gujarat",
        "discom": "Torrent Power / UGVCL",
        "wind_range": "4-6 m/s",
        "wind_quality": "very good",
        "geography": "Ahmedabad sits on the open plains of Gujarat with consistent westerly winds blowing in from the Arabian Sea. Annual average wind speeds across the city range from <strong>4 to 6 m/s</strong>, putting it in the upper bracket of Indian urban wind resources.",
        "intro": "Ahmedabad's open plains, Gulf-of-Khambhat sea breeze, and rapidly expanding industrial belt make it one of India's strongest urban wind markets. Windora installs vertical axis wind turbines for bungalows in Bopal, factories in Sanand, farmhouses in Mehmedabad, and homes across the whole Greater Ahmedabad region.",
        "factors": [
            "Torrent Power / UGVCL tariffs reach ₹8-12+/unit at high consumption",
            "Strong industrial base — Sanand, Naroda, Vatva, Odhav, Changodar belts",
            "Pre-monsoon and monsoon winds are especially strong",
            "Gujarat state incentives for renewable energy installations",
            "Farmhouse boom in Bopal, SG Highway, Mehmedabad outskirts",
        ],
        "example": "A 5 kW Hybrid Solar+Wind on a SG Highway bungalow generates ~13,500 kWh/year — payback in 4-5 years at Torrent tariffs.",
        "areas": [
            "<strong>Central</strong> — Navrangpura, Paldi, Vastrapur, Maninagar",
            "<strong>West</strong> — SG Highway, Bopal, Bodakdev, Thaltej, Ambli",
            "<strong>South</strong> — Vejalpur, Prahladnagar, Satellite, Jodhpur (Ahd)",
            "<strong>North/East</strong> — Gota, Chandkheda, Naroda, Vastral",
            "<strong>Industrial</strong> — Sanand, Naroda, Vatva, Odhav, Changodar, GIDC zones",
            "<strong>Periphery</strong> — Mehmedabad, Sanand, Bavla, Kalol, Gandhinagar",
        ],
        "faqs": [
            ("Is Ahmedabad summer heat a problem for turbines?", "Our turbines are rated for ambient temperatures up to 55°C and have thermal protection. Gujarat's heat actually correlates with strong pre-monsoon winds, so generation peaks during summer."),
            ("Does Gujarat offer subsidies?", "Gujarat has historically been a leader in renewable energy incentives. Commercial buyers qualify for accelerated depreciation (40-80% in year 1). Residential incentives vary year to year — we help check current schemes during the quote."),
            ("Can I install at my Sanand factory?", "Yes — Sanand and the broader industrial corridor see excellent wind exposure. We've designed 25-100 kW arrays for factories there. The setback distances from buildings work well for vertical axis turbines."),
        ],
    },
    {
        "slug": "kolkata",
        "name": "Kolkata",
        "state": "West Bengal",
        "state_code": "IN-WB",
        "region_label": "Kolkata &amp; West Bengal",
        "subtag": "Kolkata &amp; West Bengal",
        "discom": "CESC / WBSEDCL",
        "wind_range": "3-5 m/s",
        "wind_quality": "good",
        "geography": "Kolkata sits on the Gangetic delta with moderate but consistent winds. Annual averages range from <strong>3-5 m/s</strong>, with strong southerly sea-breeze influence and monsoon winds blowing in from the Bay of Bengal.",
        "intro": "Kolkata's Bay-of-Bengal breeze, frequent monsoon, and rising CESC tariffs make wind energy an attractive choice for the city's homes, offices, and commercial buildings. From South Kolkata bungalows to Salt Lake offices to Howrah industrial zones, Windora delivers vertical axis wind turbines across the Greater Kolkata region.",
        "factors": [
            "CESC tariffs among India's highest (₹9-14+/unit) — fast payback",
            "Cyclone-rated installation (Bay of Bengal cyclone zone)",
            "Strong monsoon winds (June-Sept) when solar drops 60-70%",
            "Tech sector growth in Salt Lake / Rajarhat / New Town",
            "Coastal humid environment — handled by our marine-grade coatings",
        ],
        "example": "A 5 kW Hybrid on a New Alipore bungalow generates ~11,000 kWh/year — cuts a ₹12,000 CESC bill to ~₹2,500. Payback 4-5 years.",
        "areas": [
            "<strong>South Kolkata</strong> — Alipore, Ballygunge, Jodhpur Park, New Alipore, Tollygunge",
            "<strong>North Kolkata</strong> — Shyambazar, Hatibagan, Burrabazar",
            "<strong>Central</strong> — Park Street, Camac Street, Esplanade",
            "<strong>East</strong> — Salt Lake, Sector V, New Town, Rajarhat",
            "<strong>Howrah</strong> — Liluah, Bally, Belur, Shibpur",
            "<strong>Industrial</strong> — Howrah-Hooghly belt, Dum Dum, Behala",
        ],
        "faqs": [
            ("Will it survive a Bay of Bengal cyclone?", "Yes — our turbines are rated to 55 m/s survival winds (cyclone-grade). Automatic over-speed protection brakes the rotor when winds exceed safe operating limits. We've installed across cyclone-prone West Bengal coast successfully."),
            ("How does Kolkata humidity affect equipment?", "All Kolkata installations include marine-grade coatings, stainless hardware, and sealed IP65 generators. Designed for humid coastal environments."),
            ("Can I get net metering with CESC?", "Yes — West Bengal has an active rooftop renewable net-metering policy. We handle the CESC/WBSEDCL application end-to-end."),
        ],
    },
    {
        "slug": "jaipur",
        "name": "Jaipur",
        "state": "Rajasthan",
        "state_code": "IN-RJ",
        "region_label": "Jaipur &amp; Rajasthan",
        "subtag": "Jaipur &amp; Rajasthan",
        "discom": "JVVNL",
        "wind_range": "4-6 m/s",
        "wind_quality": "very good",
        "geography": "Jaipur sits in the semi-arid Aravalli foothills with strong westerly winds blowing across Rajasthan's open plains. Annual average wind speeds range from <strong>4-6 m/s</strong>, with summer pre-monsoon winds exceeding 7 m/s — putting Jaipur among India's best urban wind sites.",
        "intro": "Jaipur and its surrounding Rajasthan region have some of India's best wind resources for small turbines. Combined with extreme summer AC loads and rising JVVNL tariffs, wind energy delivers exceptional ROI here. Windora installs across Greater Jaipur, Jodhpur, Udaipur, and the wider Rajasthan belt.",
        "factors": [
            "Among India's strongest urban winds (Rajasthan corridor)",
            "Extreme summer AC load (May-July) = high power bills = fast payback",
            "Rajasthan state renewable incentives + accelerated depreciation",
            "Many farmhouses and large residential plots on city periphery",
            "Heritage hotels & resorts pursuing eco-tourism credentials",
        ],
        "example": "A 5 kW Tulip turbine on a Bani Park bungalow generates ~13,000-16,000 kWh/year — cuts a ₹10,000/month JVVNL bill to ~₹1,500. Payback 3.5-5 years.",
        "areas": [
            "<strong>Central</strong> — C-Scheme, Bani Park, Civil Lines, MI Road",
            "<strong>North/East</strong> — Vidyadhar Nagar, Vaishali Nagar, Jhotwara, Sikar Road",
            "<strong>South</strong> — Malviya Nagar, Mansarovar, JLN Marg, Jagatpura",
            "<strong>West</strong> — Vaishali, Gandhi Path, Ajmer Road, Sirsi Road",
            "<strong>Periphery</strong> — Sanganer, Tonk Road farmhouses, Kukas, Achrol",
            "<strong>Beyond</strong> — Jodhpur, Udaipur, Kota, Ajmer (across Rajasthan)",
        ],
        "faqs": [
            ("Is Rajasthan heat a problem for wind turbines?", "Our turbines handle ambient up to 55°C. Rajasthan's heat correlates with the strongest wind periods (pre-monsoon), so it's actually a great place for wind."),
            ("Wind vs solar for Rajasthan?", "Both are strong here. For homes with high evening/night AC loads, hybrid wind+solar dramatically outperforms solar alone. Solar handles 10 AM-5 PM peak; wind handles evening/night."),
            ("Can I install at my Jaisalmer / Bikaner farmhouse?", "Yes — these are some of India's windiest sites. Often we recommend full off-grid systems for remote desert farmhouses since the wind resource is so consistent."),
        ],
    },
    {
        "slug": "surat",
        "name": "Surat",
        "state": "Gujarat",
        "state_code": "IN-GJ",
        "region_label": "Surat &amp; South Gujarat",
        "subtag": "Surat &amp; South Gujarat",
        "discom": "DGVCL",
        "wind_range": "4-7 m/s",
        "wind_quality": "very good",
        "geography": "Surat sits on the Gulf of Khambhat coast where the Tapi River meets the Arabian Sea. Strong onshore sea-breeze creates one of urban Gujarat's best wind regimes — annual averages of <strong>4-7 m/s</strong>.",
        "intro": "Surat's coastal location, booming diamond and textile industries, and strong purchasing power make it a prime market for wind energy. Windora installs across the city's residential pockets, industrial estates, and surrounding agricultural belts.",
        "factors": [
            "Coastal sea-breeze on Gulf of Khambhat — excellent wind resource",
            "DGVCL tariffs rising with industrial demand",
            "Strong diamond/textile industry — high commercial loads",
            "Cyclone-grade engineering needed (handled by our 55 m/s rating)",
            "Hazira industrial port zone — large factory installations",
        ],
        "example": "A 10 kW commercial system on a Sachin GIDC factory generates ~22,000 kWh/year. Payback 3-4 years on DGVCL commercial tariffs.",
        "areas": [
            "<strong>City Core</strong> — Athwa Lines, Ghod Dod Road, Piplod, Vesu",
            "<strong>West</strong> — Vesu, Pal, Adajan, Rander, Causeway Road",
            "<strong>South</strong> — Magdalla, Dumas Road, Bhatar",
            "<strong>Industrial</strong> — Hazira, Sachin GIDC, Pandesara, Pal GIDC",
            "<strong>Periphery</strong> — Kamrej, Bardoli, Mota Varachha, Olpad",
        ],
        "faqs": [
            ("Will salt air corrode my turbine?", "Coastal Surat installations use marine-grade epoxy coatings, stainless hardware, and sealed IP65 generators. Designed for the saline environment."),
            ("Is Surat windy enough for commercial-scale?", "Yes — among the best urban wind in India. Hazira and the coastal corridor see steady 5-7 m/s; commercial installations are highly economical here."),
            ("Can I get Gujarat state subsidies?", "Gujarat is one of India's most supportive renewable states. Commercial buyers get accelerated depreciation. Residential schemes vary — we check current options during quote."),
        ],
    },
    {
        "slug": "lucknow",
        "name": "Lucknow",
        "state": "Uttar Pradesh",
        "state_code": "IN-UP",
        "region_label": "Lucknow &amp; UP",
        "subtag": "Lucknow &amp; UP",
        "discom": "UPPCL / MVVNL",
        "wind_range": "3-5 m/s",
        "wind_quality": "good",
        "geography": "Lucknow sits on the open Gangetic plains with moderate, consistent winds. Annual averages range from <strong>3-5 m/s</strong>, with strong pre-monsoon and monsoon winds blowing through Uttar Pradesh.",
        "intro": "Lucknow's growing residential market, frequent power cuts, and high summer AC loads make wind energy increasingly attractive. From Gomti Nagar bungalows to Hazratganj offices to farmhouses on the city periphery, Windora delivers vertical axis turbines across the UP capital region.",
        "factors": [
            "UPPCL tariffs rising with consumption-slab structure",
            "Frequent rural power cuts (still common in surrounding UP)",
            "High AC load from May through September",
            "Growing tech and government sector workforce",
            "Many farmhouses in periphery — Mohanlalganj, Malihabad, Barabanki",
        ],
        "example": "A 3 kW Helical on a Gomti Nagar bungalow generates ~5,000 kWh/year. Saves ~₹45,000/year. Payback 5-6 years.",
        "areas": [
            "<strong>Central</strong> — Hazratganj, Aliganj, Mahanagar, Indira Nagar",
            "<strong>South</strong> — Gomti Nagar, Vibhuti Khand, Vipul Khand",
            "<strong>North/West</strong> — Aminabad, Chowk, Lalbagh",
            "<strong>Outer</strong> — Sushant Golf City, Sultanpur Road, Sitapur Road",
            "<strong>Periphery</strong> — Mohanlalganj, Malihabad, Bakshi Ka Talab",
            "<strong>Beyond</strong> — Kanpur, Allahabad, Varanasi (across UP)",
        ],
        "faqs": [
            ("Is the UP capital windy enough?", "Yes — 3-5 m/s average is well within our turbine's operating range (we start at 1.5 m/s). Pre-monsoon winds are especially strong in central UP."),
            ("Can it power my Mohanlalganj farmhouse?", "Yes — periphery farmhouses often have excellent wind exposure. Off-grid hybrid systems are popular here for full energy independence."),
            ("How fast is UPPCL net-metering approval?", "Typically 4-8 weeks. We handle the full application paperwork through UPPCL/MVVNL."),
        ],
    },
    {
        "slug": "nagpur",
        "name": "Nagpur",
        "state": "Maharashtra",
        "state_code": "IN-MH",
        "region_label": "Nagpur &amp; Vidarbha",
        "subtag": "Nagpur &amp; Vidarbha",
        "discom": "MSEDCL",
        "wind_range": "3-5 m/s",
        "wind_quality": "good",
        "geography": "Nagpur is the geographic centre of India, on the eastern Deccan plateau with open landscapes that favour steady wind flow. Annual averages range from <strong>3-5 m/s</strong>, with strong pre-monsoon and monsoon winds.",
        "intro": "Nagpur — India's geographic centre — has emerged as a strong wind energy market. The combination of rising MSEDCL tariffs, intense summer heat, and many independent bungalows makes Windora's vertical axis turbines a smart investment for the Vidarbha region.",
        "factors": [
            "MSEDCL tariffs reach ₹13+/unit at high slabs",
            "Hot summers (45°C+) = extreme AC load = high bills",
            "MIHAN SEZ and Butibori industrial corridor growth",
            "Open land plots in Wardha Road, Hingna, Khapri farmhouses",
            "Maharashtra renewable energy state policy support",
        ],
        "example": "A 5 kW Tulip on a Civil Lines bungalow generates ~10,500 kWh/year. Cuts an ₹8,000/month bill to ~₹1,500. Payback 5 years.",
        "areas": [
            "<strong>Central</strong> — Civil Lines, Dharampeth, Ramdaspeth, Sitabuldi",
            "<strong>West</strong> — Pratap Nagar, Trimurti Nagar, Bajaj Nagar",
            "<strong>South</strong> — Manish Nagar, Wardha Road, Sonegaon",
            "<strong>East</strong> — Wardhaman Nagar, Mhalgi Nagar",
            "<strong>Industrial</strong> — MIHAN SEZ, Butibori, Hingna MIDC",
            "<strong>Periphery</strong> — Khapri, Bhandara Road, Amravati Road farmhouses",
        ],
        "faqs": [
            ("Will it handle Nagpur summer heat?", "Yes — our turbines are rated for ambient up to 55°C. Summers are when generation matters most (high AC load) and our systems are designed for it."),
            ("Is wind better than solar for Nagpur?", "Hybrid is best. Solar handles peak summer afternoons; wind handles evenings and monsoon. Nagpur's diverse load profile benefits from both."),
            ("Can I install at my MIHAN factory?", "Yes — MIHAN's open layout is ideal for commercial-scale arrays. We've designed 25-100 kW installations for the SEZ."),
        ],
    },
    {
        "slug": "indore",
        "name": "Indore",
        "state": "Madhya Pradesh",
        "state_code": "IN-MP",
        "region_label": "Indore &amp; MP",
        "subtag": "Indore &amp; Madhya Pradesh",
        "discom": "MPPKVVCL",
        "wind_range": "3-5 m/s",
        "wind_quality": "good",
        "geography": "Indore sits on the Malwa plateau at ~550m elevation with steady seasonal winds. Annual averages of <strong>3-5 m/s</strong>, with strong winds in pre-monsoon and during the Malwa winter belt.",
        "intro": "Indore is repeatedly ranked India's cleanest city — and now its growing tech and pharma sector is leading another quiet revolution: rooftop renewable energy. Windora installs vertical axis wind turbines across Indore's bungalow belts, IT parks, and surrounding industrial zones.",
        "factors": [
            "MPPKVVCL tariffs and frequent slab revisions",
            "Strong civic interest in clean energy (cleanest city culture)",
            "Pithampur industrial belt — large commercial demand",
            "IT corridor (Crystal IT Park, Super Corridor) growth",
            "Many bungalow plots in Vijay Nagar, Bicholi Mardana, Kanadia",
        ],
        "example": "A 3 kW Helical on a Vijay Nagar bungalow generates ~5,500 kWh/year. Saves ₹45,000/year at MP tariffs. Payback 5-6 years.",
        "areas": [
            "<strong>Central</strong> — Old Palasia, New Palasia, Race Course Road",
            "<strong>East/North</strong> — Vijay Nagar, Scheme No. 78, Bicholi Mardana",
            "<strong>West</strong> — Saket Nagar, Mahalaxmi Nagar, Bhanwar Kuan",
            "<strong>Tech Belt</strong> — Super Corridor, Crystal IT Park, AB Road",
            "<strong>Industrial</strong> — Pithampur, Sanwer Road, Dewas Road, Rau-Pithampur belt",
            "<strong>Periphery</strong> — Kanadia, Bicholi Hapsi, Mhow Road",
        ],
        "faqs": [
            ("Is Madhya Pradesh windy enough?", "Yes — Indore's plateau elevation gives it more steady wind than lower-elevation cities. We see strong performance for residential and commercial sizes."),
            ("Will my apartment society approve?", "Indore's clean-city culture often makes societies more receptive. We provide the noise/structural documentation needed for society approval."),
            ("Can I install at my Pithampur factory?", "Yes — Pithampur's industrial zoning and open layouts make it ideal for 25-100 kW commercial arrays."),
        ],
    },
    {
        "slug": "bhopal",
        "name": "Bhopal",
        "state": "Madhya Pradesh",
        "state_code": "IN-MP",
        "region_label": "Bhopal &amp; MP",
        "subtag": "Bhopal &amp; Madhya Pradesh",
        "discom": "MPMKVVCL",
        "wind_range": "3-5 m/s",
        "wind_quality": "good",
        "geography": "Bhopal sits on the Vindhya plateau next to its iconic lakes. The hill-and-lake geography creates moderate but consistent winds — annual averages of <strong>3-5 m/s</strong>, with strong monsoon-season winds.",
        "intro": "Bhopal — MP's capital and the City of Lakes — combines government, education, and growing industrial sectors. The city's hilly geography and lake-side winds create good conditions for vertical axis wind turbines. Windora installs across Bhopal residential, government, and commercial zones.",
        "factors": [
            "MPMKVVCL tariffs at upper consumption slabs",
            "Government buildings increasingly adopting renewable mandates",
            "Mandideep industrial belt — strong commercial demand",
            "BHEL and other large-employer campuses",
            "Lake-effect winds add to the wind resource",
        ],
        "example": "A 3 kW Helical on an Arera Colony bungalow generates ~5,200 kWh/year — saves ~₹42,000/year on MP tariffs.",
        "areas": [
            "<strong>Central</strong> — Arera Colony, Shyamla Hills, MP Nagar, Indrapuri",
            "<strong>South</strong> — Kolar Road, Bagh Sevaniya, Awadhpuri",
            "<strong>East</strong> — Bairagarh, Ashoka Garden, Hoshangabad Road",
            "<strong>Industrial</strong> — Mandideep, Govindpura, Sonkach Road",
            "<strong>Periphery</strong> — Sehore Road, Raisen Road farmhouses",
        ],
        "faqs": [
            ("Does the lake geography affect wind?", "Lakes actually add to the wind — large open water surfaces create thermal-driven breezes during the day, supplementing the regional wind flow."),
            ("Can government buildings get installations?", "Yes — we work with state government and public sector clients. Special procurement procedures apply; we handle the necessary documentation."),
            ("Is Mandideep good for commercial installs?", "Yes — Mandideep's open industrial layout and good wind exposure make it ideal for 25-100 kW arrays. We've quoted multiple factories there."),
        ],
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wind Turbine in {name} | Vertical VAWT &amp; Hybrid Systems | Windora Energy</title>
    <meta name="description" content="Wind turbine in {name} — vertical axis turbines for homes, farms, and businesses across {name} &amp; {state}. Low-wind optimized, near-silent, India-engineered. Free site analysis from Windora Energy.">
    <meta name="keywords" content="wind turbine in {name}, vertical wind turbine {name}, rooftop wind turbine {name}, residential wind turbine {name}, wind energy {name}, hybrid solar wind {name}, small wind turbine {name}, {state} wind turbine, Windora {name}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="geo.region" content="{state_code}">
    <meta name="geo.placename" content="{name}, {state}, India">
    <link rel="canonical" href="https://windoraenergy.com/cities/wind-turbine-{slug}.html">
    <link rel="icon" type="image/png" href="../assets/images/logo.png">
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="stylesheet" href="../assets/css/animations.css">
    <link rel="stylesheet" href="../assets/css/extra.css">
    <link rel="stylesheet" href="../assets/css/subpage.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Windora Energy — {name}","image":"https://windoraenergy.com/assets/images/logo.png","telephone":"+91-91373-69043","email":"info@windoraenergy.com","areaServed":{{"@type":"City","name":"{name}"}}}}</script>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://windoraenergy.com/"}},{{"@type":"ListItem","position":3,"name":"Wind Turbine in {name}","item":"https://windoraenergy.com/cities/wind-turbine-{slug}.html"}}]}}</script>
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
<div class="top-bar"><div class="top-bar-container"><div class="top-bar-left"><a href="tel:+919137369043"><i class="fas fa-phone-alt"></i> +91 91373 69043</a><a href="mailto:info@windoraenergy.com"><i class="fas fa-envelope"></i> info@windoraenergy.com</a></div><div class="top-bar-right"><span><i class="fas fa-map-marker-alt"></i> {region_label}</span></div></div></div>
<nav class="navbar scrolled" id="navbar"><div class="nav-container"><a href="../index.html" class="nav-logo"><img src="../assets/images/logo.png" alt="Wind Turbine {name} — Windora" class="logo-img"></a><ul class="nav-menu" id="navMenu"><li class="nav-item"><a href="../index.html" class="nav-link">Home</a></li><li class="nav-item"><a href="../index.html#products" class="nav-link">Products</a></li><li class="nav-item"><a href="../index.html#sectors" class="nav-link">Solutions</a></li><li class="nav-item"><a href="../blog/index.html" class="nav-link">Blog</a></li><li class="nav-item"><a href="../index.html#contact" class="nav-link cta-btn">Get Free Site Analysis</a></li></ul><div class="hamburger" id="hamburger"><span></span><span></span><span></span></div></div></nav>

<section class="subpage-hero">
    <div class="container">
        <nav class="breadcrumbs"><a href="../index.html">Home</a><span class="sep">›</span><span class="current">Wind Turbine in {name}</span></nav>
        <span class="subpage-tag">{subtag}</span>
        <h1 class="subpage-title">Wind Turbine in {name}</h1>
        <p class="subpage-subtitle">{intro}</p>
        <div class="subpage-hero-cta">
            <a href="../index.html#contact" class="btn btn-primary"><i class="fas fa-search-location"></i><span>{name} Survey</span></a>
            <a href="https://wa.me/919137369043?text=Hi%20Windora%2C%20{name}%20wind%20turbine%20enquiry." class="btn btn-outline" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i><span>WhatsApp</span></a>
        </div>
    </div>
</section>

<section class="content-section">
    <div class="container">
        <div class="content-grid">
            <div class="content-main">
                <h2>Why Wind Energy Works in {name}</h2>
                <p>{geography} That makes {name} a {wind_quality} fit for Windora's vertical axis wind turbines, which start generating at just 1.5 m/s.</p>
                <ul>
{factor_items}
                </ul>

                <div class="callout">
                    <p><strong>Real example:</strong> {example}</p>
                </div>

                <h2>Coverage Across {name}</h2>
                <ul>
{area_items}
                </ul>

                <h2>Best Products for {name}</h2>
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

                <h2>{name} Pricing Indicators</h2>
                <ul>
                    <li><strong>1.5 kW rooftop turbine:</strong> ₹1.8-2.5 lakh</li>
                    <li><strong>3 kW residential:</strong> ₹3-5 lakh</li>
                    <li><strong>5 kW Tulip / Hybrid:</strong> ₹6-9 lakh</li>
                    <li><strong>10 kW Hybrid:</strong> ₹14-20 lakh</li>
                </ul>
                <p>All installations include the local {discom} net-metering paperwork, civil works, structural mounting, and 15-25 year warranty.</p>

                <h2>FAQ — Wind Turbine {name}</h2>
{faq_items}
            </div>

            <aside class="content-sidebar">
                <div class="sidebar-card"><h4>Products in {name}</h4><ul>
                    <li><a href="../products/helical-vertical-wind-turbine.html">Helical Turbine</a></li>
                    <li><a href="../products/tulip-vertical-wind-turbine.html">Tulip Turbine</a></li>
                    <li><a href="../products/hybrid-solar-wind-system.html">Hybrid Solar + Wind</a></li>
                    <li><a href="../products/off-grid-wind-system.html">Off-Grid Systems</a></li>
                </ul></div>
                <div class="sidebar-card"><h4>{name} Solutions</h4><ul>
                    <li><a href="../solutions/wind-turbine-for-home.html">For {name} Homes</a></li>
                    <li><a href="../solutions/wind-turbine-for-farm.html">For Farms</a></li>
                    <li><a href="../solutions/rooftop-wind-turbine.html">Rooftop Turbines</a></li>
                    <li><a href="../solutions/low-wind-turbine-india.html">Low Wind India</a></li>
                </ul></div>
                <div class="sidebar-card"><h4>Other Cities</h4><ul>
                    <li><a href="wind-turbine-mumbai.html">Mumbai</a></li>
                    <li><a href="wind-turbine-pune.html">Pune</a></li>
                    <li><a href="wind-turbine-delhi.html">Delhi NCR</a></li>
                    <li><a href="wind-turbine-bangalore.html">Bangalore</a></li>
                    <li><a href="wind-turbine-chennai.html">Chennai</a></li>
                    <li><a href="wind-turbine-hyderabad.html">Hyderabad</a></li>
                </ul></div>
                <div class="sidebar-cta"><h4>{name} Site Visit</h4><p>Free survey, sizing, and quote within 48-72 hours.</p><a href="../index.html#contact" class="btn"><i class="fas fa-arrow-right"></i><span>Book Survey</span></a></div>
            </aside>
        </div>
    </div>
</section>

<section class="page-cta">
    <div class="container">
        <h2>Wind &amp; Hybrid Energy in {name}</h2>
        <p>Free survey across {name} and {state}. Custom system for your home, farm, or business.</p>
        <div class="page-cta-buttons">
            <a href="../index.html#contact" class="btn btn-primary"><i class="fas fa-search-location"></i><span>{name} Survey</span></a>
            <a href="tel:+919137369043" class="btn btn-outline"><i class="fas fa-phone-alt"></i><span>+91 91373 69043</span></a>
        </div>
    </div>
</section>

<a href="https://wa.me/919137369043?text=Hi%20Windora%2C%20{name}." class="float-btn float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i><span class="float-label">Chat on WhatsApp</span></a>
<a href="tel:+919137369043" class="float-btn float-call" aria-label="Call"><i class="fas fa-phone-alt"></i></a>
<button class="back-to-top" id="backToTop"><i class="fas fa-arrow-up"></i></button>

<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><img src="../assets/images/logo.png" alt="Windora Energy" class="footer-logo"><p>Wind &amp; hybrid energy solutions engineered for Indian conditions.</p><p class="footer-tag"><strong>Engineered for Low Wind Performance.</strong></p></div><div class="footer-links"><h4>Products</h4><ul><li><a href="../products/helical-vertical-wind-turbine.html">Helical Turbine</a></li><li><a href="../products/tulip-vertical-wind-turbine.html">Tulip Turbine</a></li><li><a href="../products/hybrid-solar-wind-system.html">Hybrid Solar + Wind</a></li><li><a href="../products/off-grid-wind-system.html">Off-Grid Systems</a></li></ul></div><div class="footer-links"><h4>Cities</h4><ul><li><a href="wind-turbine-mumbai.html">Mumbai</a></li><li><a href="wind-turbine-pune.html">Pune</a></li><li><a href="wind-turbine-delhi.html">Delhi NCR</a></li><li><a href="wind-turbine-bangalore.html">Bangalore</a></li><li><a href="wind-turbine-chennai.html">Chennai</a></li><li><a href="wind-turbine-hyderabad.html">Hyderabad</a></li><li><a href="wind-turbine-ahmedabad.html">Ahmedabad</a></li><li><a href="wind-turbine-kolkata.html">Kolkata</a></li><li><a href="wind-turbine-jaipur.html">Jaipur</a></li><li><a href="wind-turbine-surat.html">Surat</a></li><li><a href="wind-turbine-lucknow.html">Lucknow</a></li><li><a href="wind-turbine-nagpur.html">Nagpur</a></li><li><a href="wind-turbine-indore.html">Indore</a></li><li><a href="wind-turbine-bhopal.html">Bhopal</a></li></ul></div><div class="footer-contact"><h4>Get in Touch</h4><p><i class="fas fa-map-marker-alt"></i> Mira Road East, MH 401107</p><p><i class="fas fa-phone-alt"></i> <a href="tel:+919137369043">+91 91373 69043</a></p><p><i class="fas fa-envelope"></i> <a href="mailto:info@windoraenergy.com">info@windoraenergy.com</a></p></div></div><div class="footer-bottom"><p>&copy; 2026 Windora Energy. All rights reserved.</p></div></div></footer>
<script src="../assets/js/main.js"></script>
</body>
</html>
'''

for city in CITIES:
    factor_items = "\n".join(f"                    <li>{f}</li>" for f in city["factors"])
    area_items = "\n".join(f"                    <li>{a}</li>" for a in city["areas"])
    faq_items = "\n".join(
        f'                <details class="faq-item" style="margin-bottom: 12px;"><summary><span>{q}</span><i class="fas fa-plus"></i></summary><div class="faq-answer"><p>{a}</p></div></details>'
        for q, a in city["faqs"]
    )
    html = TEMPLATE.format(
        factor_items=factor_items,
        area_items=area_items,
        faq_items=faq_items,
        **city
    )
    path = f"cities/wind-turbine-{city['slug']}.html"
    with open(path, "w") as fp:
        fp.write(html)
    print(f"WROTE {path}")
