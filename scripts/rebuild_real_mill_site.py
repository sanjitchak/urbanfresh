#!/usr/bin/env python3
"""Rebuild UrbanFresh around the verified Village Daha Madanpur mill and catalogue."""

from __future__ import annotations

import json
from html import escape
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
PHONE = "+91 94335 69217"
PHONE_LINK = "+919433569217"
ADDRESS = "119/6, Highway, Village Daha, Madanpur, Karnal 132001, Haryana, India"
CSS_VERSION = "20260714-11"
JS_VERSION = "20260714-2"
WA_TEXT = "Hello UrbanFresh, I would like a bulk rice quote."
WA_URL = f"https://wa.me/919433569217?text={WA_TEXT.replace(' ', '%20').replace(',', '%2C')}"
GUIDE_SLUG = "1121-vs-1509-vs-1401-basmati-rice.html"


PRODUCTS = [
    {
        "slug": "1121-basmati-rice.html",
        "name": "1121 Basmati Rice",
        "group": "Basmati rice",
        "tag": "Extra-long grain basmati",
        "title": "1121 Basmati Rice Manufacturer in Karnal | UrbanFresh",
        "meta": "Buy 1121 Basmati rice from an UrbanFresh rice mill in Karnal. Explore Raw, Steam, Sella and Golden Sella options for bulk and export orders.",
        "summary": "A widely traded extra-long grain basmati variety for wholesale, food service, retail brands and export requirements.",
        "detail": "The mill catalogue includes 1121 in Raw, Steam, Sella and Golden Sella processing styles. Buyers should send the required process, quantity, pack and destination so crop, specification and availability can be checked against the order.",
        "image": "category-1121.webp",
        "variants": [("1121 Steam Basmati Rice", "1121-steam.webp"), ("1121 Sella Basmati Rice", "1121-sella.webp"), ("1121 Golden Sella Basmati Rice", "1121-golden-sella.webp"), ("1121 Raw Basmati Rice", "1121-raw.webp")],
    },
    {
        "slug": "1509-basmati-rice.html",
        "name": "1509 Basmati Rice",
        "group": "Basmati rice",
        "tag": "Commercial basmati",
        "title": "1509 Basmati Rice Manufacturer in Karnal | UrbanFresh",
        "meta": "Request 1509 Basmati rice from UrbanFresh in Karnal. Compare Raw, Steam, White Sella and Golden Sella options for wholesale and export supply.",
        "summary": "A familiar basmati choice for commercial buying programmes that need multiple processing and packaging options.",
        "detail": "UrbanFresh can discuss 1509 Raw, Steam, White Sella and Golden Sella requirements. The useful starting point is a complete commercial brief with quantity, pack format, buyer market and delivery location.",
        "image": "category-1509.webp",
        "variants": [("1509 Steam Basmati Rice", "1509-steam.webp"), ("1509 White Sella Basmati Rice", "1509-sella.webp"), ("1509 Golden Sella Basmati Rice", "1509-golden-sella.webp"), ("1509 Raw Basmati Rice", "1509-raw.webp")],
    },
    {
        "slug": "traditional-basmati-rice.html",
        "name": "Traditional Basmati Rice",
        "group": "Basmati rice",
        "tag": "Classic basmati",
        "title": "Traditional Basmati Rice Supplier | UrbanFresh Karnal",
        "meta": "Source Traditional Basmati rice from UrbanFresh in Karnal. Ask about Raw, Steam, Sella and Golden Sella processing for bulk and branded orders.",
        "summary": "Classic basmati positioning for buyers who value a traditional product story, aroma and established market recognition.",
        "detail": "The mill range covers Traditional Basmati in Raw, Steam, Sella and Golden Sella styles. Final crop, ageing, cooking and grain parameters should be agreed in the buyer specification.",
        "image": "category-traditional.webp",
        "variants": [("Traditional Raw Basmati Rice", "traditional-raw.webp"), ("Traditional Sella Basmati Rice", "traditional-sella.webp"), ("Traditional Steam Basmati Rice", "traditional-steam.webp"), ("Traditional Golden Sella Basmati Rice", "traditional-golden-sella.webp")],
    },
    {
        "slug": "1401-basmati-rice.html",
        "name": "1401 Basmati Rice",
        "group": "Basmati rice",
        "tag": "Numbered basmati",
        "title": "1401 Basmati Rice Manufacturer in Karnal | UrbanFresh",
        "meta": "Request bulk 1401 Basmati rice from UrbanFresh Rice Mills in Karnal. Raw, Steam, White Sella and Golden Sella requirements are welcome.",
        "summary": "A numbered basmati option for buyers comparing grain presentation, processing style, pack and commercial position.",
        "detail": "UrbanFresh lists 1401 Basmati in Raw, Steam, White Sella and Golden Sella formats. Send the intended market and order details so the mill can review the right specification.",
        "image": "category-1401.webp",
        "variants": [("1401 Steam Basmati Rice", "1401-steam.webp"), ("1401 White Sella Basmati Rice", "1401-sella.webp"), ("1401 Golden Sella Basmati Rice", "1401-golden-sella.webp"), ("1401 Raw Basmati Rice", "1401-raw.webp")],
    },
    {
        "slug": "pusa-basmati-rice.html",
        "name": "Pusa Basmati Rice",
        "group": "Basmati rice",
        "tag": "Established basmati range",
        "title": "Pusa Basmati Rice Manufacturer in Karnal | UrbanFresh",
        "meta": "Buy Pusa Basmati rice from UrbanFresh Rice Mills in Karnal. Explore Raw, Steam, Sella and Golden Sella options for bulk and export enquiries.",
        "summary": "An established basmati range offered across the processing styles commonly requested in Indian and export trade.",
        "detail": "The Pusa Basmati range includes Raw, Steam, Sella and Golden Sella rice. Quote discussions are tied to the required crop, quantity, packaging and delivery market.",
        "image": "category-pusa.webp",
        "variants": [("Pusa Steam Basmati Rice", "pusa-steam.webp"), ("Pusa Sella Basmati Rice", "pusa-sella.webp"), ("Pusa Golden Sella Basmati Rice", "pusa-golden-sella.webp"), ("Pusa Raw Basmati Rice", "pusa-raw.webp")],
    },
    {
        "slug": "1718-basmati-rice.html",
        "name": "1718 Basmati Rice",
        "group": "Basmati rice",
        "tag": "Modern basmati",
        "title": "1718 Basmati Rice Manufacturer in Karnal | UrbanFresh",
        "meta": "Request 1718 Basmati rice from UrbanFresh in Karnal. Compare Raw, Steam, Sella and Golden Sella processing for bulk, wholesale and export orders.",
        "summary": "A modern basmati selection for buyers comparing long-grain presentation, processing options and commercial fit.",
        "detail": "UrbanFresh offers 1718 Basmati conversations across Raw, Steam, Sella and Golden Sella formats. Exact grain, cooking and commercial parameters are confirmed per requirement.",
        "image": "category-1718.webp",
        "variants": [("1718 Steam Basmati Rice", "1718-steam.webp"), ("1718 Raw Basmati Rice", "1718-raw.webp"), ("1718 Golden Sella Basmati Rice", "1718-golden-sella.webp"), ("1718 Sella Basmati Rice", "1718-sella.webp")],
    },
    {
        "slug": "sugandha-rice.html",
        "name": "Sugandha Rice",
        "group": "Non-basmati rice",
        "tag": "Long-grain non-basmati",
        "title": "Sugandha Rice Manufacturer and Supplier | UrbanFresh",
        "meta": "Source Sugandha rice from UrbanFresh Rice Mills in Karnal. Raw, Steam, Sella and Golden Sella options are available for bulk trade enquiries.",
        "summary": "A long-grain non-basmati option for buyers balancing presentation, processing choice and commercial value.",
        "detail": "The mill catalogue includes Sugandha Raw, Steam, Sella and Golden Sella rice. Buyers should define the required quality parameters rather than rely on a generic website specification.",
        "image": "category-sugandha.webp",
        "variants": [("Sugandha Raw Rice", "sugandha-raw.webp"), ("Sugandha Steam Rice", "sugandha-steam.webp"), ("Sugandha Sella Rice", "sugandha-sella.webp"), ("Sugandha Golden Sella Rice", "sugandha-golden-sella.webp")],
    },
    {
        "slug": "sharbati-rice.html",
        "name": "Sharbati Rice",
        "group": "Non-basmati rice",
        "tag": "Value-led rice range",
        "title": "Sharbati Rice Manufacturer and Supplier | UrbanFresh",
        "meta": "Request Sharbati rice from UrbanFresh Rice Mills in Karnal. Explore Raw, Steam, Sella and Golden Sella formats for wholesale and export buying.",
        "summary": "A value-led non-basmati rice range used in wholesale, food-service and price-conscious packaged-rice programmes.",
        "detail": "UrbanFresh lists Sharbati rice in Raw, Steam, Sella and Golden Sella formats. The correct commercial option depends on the buyer market, pack and target specification.",
        "image": "category-sharbati.webp",
        "variants": [("Sharbati Raw Rice", "sharbati-raw.webp"), ("Sharbati Steam Rice", "sharbati-steam.webp"), ("Sharbati Sella Rice", "sharbati-sella.webp"), ("Sharbati Golden Sella Rice", "sharbati-golden-sella.webp")],
    },
    {
        "slug": "pr-11-rice.html",
        "name": "PR 11 Rice",
        "group": "Non-basmati rice",
        "tag": "Trade rice",
        "title": "PR 11 Rice Manufacturer and Supplier | UrbanFresh Karnal",
        "meta": "Buy PR 11 rice from UrbanFresh Rice Mills in Karnal. Ask about Raw, Steam, Sella and Golden Sella options for bulk and institutional orders.",
        "summary": "A practical trade rice range for wholesale, institutional and food-service requirements where consistency and value matter.",
        "detail": "The PR 11 range covers Raw, Steam, Sella and Golden Sella processing. Share volume, frequency and destination to start a useful supply discussion.",
        "image": "category-pr11.webp",
        "variants": [("PR 11 Raw Rice", "pr11-raw.webp"), ("PR 11 Steam Rice", "pr11-steam.webp"), ("PR 11 Sella Rice", "pr11-sella.webp"), ("PR 11 Golden Sella Rice", "pr11-golden-sella.webp")],
    },
    {
        "slug": "parmal-rice.html",
        "name": "Parmal Rice",
        "group": "Non-basmati rice",
        "tag": "Everyday commercial rice",
        "title": "Parmal Rice Manufacturer and Supplier | UrbanFresh Karnal",
        "meta": "Request Parmal rice from UrbanFresh Rice Mills in Karnal. Raw, Steam, Sella and Golden Sella formats are available for bulk trade buying.",
        "summary": "An everyday commercial rice option for high-volume wholesale, food-service and institutional procurement.",
        "detail": "UrbanFresh lists Parmal Raw, Steam, Sella and Golden Sella rice. Confirm the required grain, broken percentage, polish, packing and dispatch schedule in the order brief.",
        "image": "category-parmal.webp",
        "variants": [("Parmal Steam Rice", "parmal-steam.webp"), ("Parmal Sella Rice", "parmal-sella.webp"), ("Parmal Golden Sella Rice", "parmal-golden-sella.webp"), ("Parmal Raw Rice", "parmal-raw.webp")],
    },
    {
        "slug": "sona-masoori-raw-rice.html",
        "name": "Sona Masoori Raw Rice",
        "group": "Non-basmati rice",
        "tag": "Medium-grain South Indian rice",
        "title": "Sona Masoori Raw Rice Supplier | UrbanFresh Rice Mills",
        "meta": "Source Sona Masoori Raw rice through UrbanFresh Rice Mills. Send quantity, packaging and destination for a bulk wholesale or export quotation.",
        "summary": "A lightweight, medium-grain rice associated with South Indian cooking and valued for its soft cooked texture and versatility.",
        "detail": "Sona Masoori Raw Rice is commonly used for steamed rice, pulao and everyday dishes. Buyers should confirm crop, grain, moisture, broken tolerance, polish and packing for the target market.",
        "image": "category-sona-masoori.webp",
        "variants": [("Sona Masoori Raw Rice", "sona-masoori-raw.webp")],
    },
    {
        "slug": "pesticide-residue-free-raw-rice.html",
        "name": "Pesticide Residue Free Raw Rice",
        "group": "Residue-controlled rice",
        "tag": "Buyer-tested raw rice",
        "title": "Residue-Free Raw Rice Supplier | UrbanFresh Karnal",
        "meta": "Discuss pesticide residue free Raw rice with UrbanFresh in Karnal. Buyer limits, crop, testing, laboratory reports and availability are confirmed per order.",
        "summary": "Raw rice enquiries for markets that require defined pesticide-residue limits and buyer-reviewed laboratory evidence.",
        "detail": "The mill catalogue includes 1401 and Pusa residue-controlled Raw rice options. Residue requirements vary by market, so the buyer must share the applicable limits and request current lot-specific testing.",
        "image": "category-prf-raw.webp",
        "variants": [("1401 Pesticide Residue Free Raw Rice", "prf-1401-raw.webp"), ("Pusa Pesticide Residue Free Raw Rice", "prf-pusa-raw.webp")],
        "controlled": True,
    },
    {
        "slug": "pesticide-residue-free-steam-rice.html",
        "name": "Pesticide Residue Free Steam Rice",
        "group": "Residue-controlled rice",
        "tag": "Buyer-tested steam rice",
        "title": "Residue-Free Steam Rice Supplier | UrbanFresh Karnal",
        "meta": "Request pesticide residue free Steam rice from UrbanFresh in Karnal. Testing scope, buyer limits, crop and laboratory documentation are checked per lot.",
        "summary": "Steam rice sourcing for buyers whose destination market or internal programme specifies pesticide-residue controls.",
        "detail": "A residue-controlled Steam rice order begins with the destination standard, variety, quantity and test scope. UrbanFresh confirms feasibility and current evidence against the actual lot.",
        "image": "category-prf-steam.webp",
        "variants": [("Pesticide Residue Free Steam Rice", "category-prf-steam.webp")],
        "controlled": True,
    },
    {
        "slug": "pesticide-residue-free-sella-rice.html",
        "name": "Pesticide Residue Free Sella Rice",
        "group": "Residue-controlled rice",
        "tag": "Buyer-tested parboiled rice",
        "title": "Residue-Free Sella Rice Supplier | UrbanFresh Karnal",
        "meta": "Discuss pesticide residue free Sella rice with UrbanFresh in Karnal. Buyer residue limits, processing, crop and laboratory reports are confirmed per order.",
        "summary": "Sella or parboiled rice for programmes where the buyer defines residue limits and reviews current test documentation.",
        "detail": "Residue-controlled Sella rice is quoted only after the buyer shares the variety, destination limits, volume and testing expectations. Final compliance is tied to current lot evidence.",
        "image": "category-prf-sella.webp",
        "variants": [("Pesticide Residue Free Sella Rice", "category-prf-sella.webp")],
        "controlled": True,
    },
    {
        "slug": "pesticide-residue-free-golden-sella-rice.html",
        "name": "Pesticide Residue Free Golden Sella Rice",
        "group": "Residue-controlled rice",
        "tag": "Buyer-tested golden sella",
        "title": "Residue-Free Golden Sella Rice | UrbanFresh Karnal",
        "meta": "Request pesticide residue free Golden Sella rice from UrbanFresh. Destination limits, variety, crop, processing and current test reports are checked per lot.",
        "summary": "Golden Sella rice sourcing for markets that need defined residue controls alongside a buyer-approved product specification.",
        "detail": "The enquiry should include the variety, destination, residue standard, quantity, pack and delivery timeline. Current testing and commercial feasibility are confirmed for the offered lot.",
        "image": "category-prf-golden-sella.webp",
        "variants": [("Pesticide Residue Free Golden Sella Rice", "category-prf-golden-sella.webp")],
        "controlled": True,
    },
]


def image_path(name: str) -> str:
    return f"assets/images/ricefarm/{name}"


def organization_schema() -> dict:
    return {
        "@type": ["Organization", "LocalBusiness"],
        "name": "UrbanFresh Rice Mills",
        "url": "https://urbanfresh.in/",
        "logo": "https://urbanfresh.in/assets/images/urbanfresh-logo.webp",
        "telephone": "+91-94335-69217",
        "foundingDate": "1978",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "119/6, Highway, Village Daha, Madanpur",
            "addressLocality": "Karnal",
            "addressRegion": "Haryana",
            "postalCode": "132001",
            "addressCountry": "IN",
        },
        "areaServed": ["India", "International"],
    }


def header(active: str = "") -> str:
    links = [
        ("home", "index.html", "Home"),
        ("products", "products.html", "Rice Products"),
        ("about", "about.html", "About the Mill"),
        ("infrastructure", "infrastructure.html", "Infrastructure"),
        ("quality", "quality.html", "Quality"),
    ]
    nav = "".join(f'<a class="{"active" if key == active else ""}" href="{href}">{label}</a>' for key, href, label in links)
    return dedent(f"""
      <a class="skip-link" href="#main">Skip to content</a>
      <div class="topbar"><div class="container topbar-inner"><span>Rice mill at <strong>Village Daha, Madanpur, Karnal</strong></span><div class="topbar-list"><a href="tel:{PHONE_LINK}">{PHONE}</a><span>India and export enquiries welcome</span></div></div></div>
      <header class="site-header"><div class="container nav-wrap"><a class="brand" href="index.html" aria-label="UrbanFresh Rice Mills home"><img class="brand-mark" src="assets/images/urbanfresh-logo.webp" width="50" height="50" alt="UrbanFresh rice grain and sunrise logo"><span class="brand-copy"><span class="brand-name">UrbanFresh</span><span class="brand-tag">Rice Mills · Karnal</span></span></a><button class="menu-toggle" type="button" aria-label="Open navigation" aria-expanded="false" data-menu-toggle><span></span></button><nav class="main-nav" aria-label="Main navigation" data-main-nav>{nav}<a class="button button-sm {"active" if active == "contact" else ""}" href="contact.html#quote">Get a Quote</a></nav></div></header>
    """).strip()


def footer(contact_page: bool = False) -> str:
    quote_href = "#quote" if contact_page else "contact.html#quote"
    return dedent(f"""
      <footer class="site-footer"><div class="container footer-grid">
        <div class="footer-brand"><a class="brand" href="index.html"><img class="brand-mark" src="assets/images/urbanfresh-logo.webp" width="50" height="50" alt=""><span class="brand-copy"><span class="brand-name">UrbanFresh</span><span class="brand-tag">Rice Mills · Karnal</span></span></a><p>A family-operated rice mill established in 1978, serving bulk buyers from Village Daha Madanpur, Karnal.</p></div>
        <div><h2 class="footer-title">Mill</h2><div class="footer-links"><a href="about.html">About UrbanFresh</a><a href="infrastructure.html">Infrastructure</a><a href="quality.html">Quality Control</a><a href="certifications.html">Certifications</a><a href="private-label.html">Private Label</a></div></div>
        <div><h2 class="footer-title">Rice range</h2><div class="footer-links"><a href="products.html">All Rice Products</a><a href="{GUIDE_SLUG}">1121 vs 1509 vs 1401 Guide</a><a href="1121-basmati-rice.html">1121 Basmati</a><a href="pusa-basmati-rice.html">Pusa Basmati</a><a href="sugandha-rice.html">Sugandha Rice</a><a href="pr-11-rice.html">PR 11 Rice</a></div></div>
        <div><h2 class="footer-title">Contact</h2><div class="footer-links"><span>119/6, Highway, Village Daha, Madanpur</span><span>Karnal 132001, Haryana, India</span><a href="tel:{PHONE_LINK}">{PHONE}</a><a href="{WA_URL}" target="_blank" rel="noopener">WhatsApp UrbanFresh</a><a href="{quote_href}">Quote form</a></div></div>
      </div><div class="container footer-bottom"><span>© <span data-year></span> UrbanFresh Rice Mills.</span><span>Availability, specifications, certificates and terms are confirmed per enquiry.</span></div></footer>
      <a class="whatsapp-float" href="{WA_URL}" target="_blank" rel="noopener" aria-label="Chat with UrbanFresh on WhatsApp">Quote on WhatsApp</a>
      <div class="mobile-cta"><a class="button button-whatsapp" href="{WA_URL}" target="_blank" rel="noopener">Chat on WhatsApp</a><a class="button" href="{quote_href}">Get Quote</a></div>
      <script src="assets/js/site.js?v={JS_VERSION}" defer></script>
    """).strip()


def render_page(filename: str, title: str, meta: str, body: str, active: str, schema: dict, image: str, body_class: str = "", contact_page: bool = False) -> None:
    canonical = "https://urbanfresh.in/" if filename == "index.html" else f"https://urbanfresh.in/{filename}"
    image_url = f"https://urbanfresh.in/{image}"
    html = dedent(f"""\
    <!doctype html>
    <html lang="en-IN">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{escape(title)}</title>
      <meta name="description" content="{escape(meta, quote=True)}">
      <link rel="canonical" href="{canonical}">
      <meta name="robots" content="index,follow,max-image-preview:large">
      <meta name="theme-color" content="#0f3d2e">
      <meta property="og:type" content="website">
      <meta property="og:site_name" content="UrbanFresh Rice Mills">
      <meta property="og:title" content="{escape(title, quote=True)}">
      <meta property="og:description" content="{escape(meta, quote=True)}">
      <meta property="og:url" content="{canonical}">
      <meta property="og:image" content="{image_url}">
      <link rel="icon" href="assets/images/favicon.png" type="image/png">
      <link rel="stylesheet" href="assets/css/site.css?v={CSS_VERSION}">
      <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":"))}</script>
    </head>
    <body class="{body_class}">
      {header(active)}
      <main id="main">{body}</main>
      {footer(contact_page)}
    </body>
    </html>
    """)
    (ROOT / filename).write_text(html, encoding="utf-8")


def page_hero(kicker: str, title: str, text: str, image: str, crumbs: list[tuple[str, str | None]]) -> str:
    crumb_html = "".join(f'<a href="{href}">{escape(label)}</a>' if href else f'<span>{escape(label)}</span>' for label, href in crumbs)
    return dedent(f"""
      <section class="page-hero custom-hero" style="--page-image:url('/{image_path(image)}')"><div class="container"><div class="breadcrumbs">{crumb_html}</div><div class="page-hero-content"><div class="hero-kicker">{escape(kicker)}</div><h1>{escape(title)}</h1><p>{escape(text)}</p></div></div></section>
    """).strip()


def render_product_page(product: dict) -> None:
    variants = "".join(dedent(f"""
      <article class="variant-card"><img src="{image_path(image)}" alt="{escape(label)} supplied by UrbanFresh Rice Mills" loading="lazy" width="900" height="650"><div><span>{escape(product['group'])}</span><h3>{escape(label)}</h3><a class="text-link" href="contact.html#quote">Request this rice</a></div></article>
    """).strip() for label, image in product["variants"])
    same_group = [item for item in PRODUCTS if item["group"] == product["group"] and item["slug"] != product["slug"]][:3]
    related = "".join(f'<article class="benefit-card"><span class="number">{i:02d}</span><h3>{escape(item["name"])}</h3><a class="text-link" href="{item["slug"]}">View product</a></article>' for i, item in enumerate(same_group, 1))
    controlled_note = "Current lot-specific laboratory evidence and the buyer's applicable residue limits must be reviewed before acceptance." if product.get("controlled") else "Crop, ageing, grain, cooking, moisture, broken tolerance, packing and availability are confirmed against the buyer's accepted specification."
    faq = [
        (f"Which {product['name']} processing styles can I request?", f"The UrbanFresh catalogue shows {', '.join(label for label, _ in product['variants'])}. Current availability is checked when you send the requirement."),
        (f"How do I get a bulk {product['name']} price?", "Send quantity, packaging, delivery city or country, buyer type and purchase timeline. A rice price without these details is rarely useful."),
        ("Can UrbanFresh pack rice for my brand?", "Private-label and buyer-specified packaging enquiries are welcome. Share pack sizes, material, artwork status and destination-market labelling needs."),
    ]
    faq_html = "".join(f'<details class="faq"><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in faq)
    guide_link = ""
    if product["name"] in {"1121 Basmati Rice", "1509 Basmati Rice", "1401 Basmati Rice"}:
        guide_link = dedent(f"""
          <section class="section-sm guide-callout"><div class="container guide-callout-grid"><div><p class="section-label">Buyer guide</p><h2>Comparing 1121, 1509 and 1401?</h2><p>Learn what grain appearance can show, why processing style matters and how to verify a bulk sample before buying.</p></div><a class="button button-arrow" href="{GUIDE_SLUG}">Read the Comparison</a></div></section>
        """)
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            organization_schema(),
            {
                "@type": "Product",
                "name": product["name"],
                "image": [f"https://urbanfresh.in/{image_path(image)}" for _, image in product["variants"]],
                "description": product["summary"],
                "category": product["group"],
                "url": f"https://urbanfresh.in/{product['slug']}",
                "brand": {"@type": "Brand", "name": "UrbanFresh"},
                "manufacturer": {"@type": "Organization", "name": "UrbanFresh Rice Mills"},
            },
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
        ],
    }
    body = page_hero(product["tag"], product["name"], product["summary"], product["image"], [("Home", "index.html"), ("Rice Products", "products.html"), (product["name"], None)]) + dedent(f"""
      <section class="section"><div class="container content-grid"><article class="prose"><p class="section-label">Milled in Karnal</p><h2>Buy {escape(product['name'])} against a real requirement</h2><p>{escape(product['detail'])}</p><div class="availability-note">{escape(controlled_note)}</div><h2>What to include in your enquiry</h2><p>Tell UrbanFresh the processing style, approximate metric tons, required pack, delivery city or destination port and buying timeline. Add important quality parameters or request guidance if your customer has not fixed them yet.</p><h2>Mill and supply context</h2><p>Your enquiry is handled from our rice mill at {ADDRESS}. The mill was established in 1978 and is equipped for cleaning, parboiling, drying, milling, sorting and packaging. Commercial feasibility is confirmed for each order.</p></article><aside class="info-panel"><h2>Quote {escape(product['name'])}</h2><p>Send a mill-ready buying brief.</p><div class="spec-list"><div class="spec-row"><span>Product</span><strong>{escape(product['name'])}</strong></div><div class="spec-row"><span>Processes</span><strong>{len(product['variants'])} listed options</strong></div><div class="spec-row"><span>Quantity</span><strong>Required</strong></div><div class="spec-row"><span>Packaging</span><strong>Buyer specified</strong></div><div class="spec-row"><span>Mill</span><strong>Daha Madanpur, Karnal</strong></div></div><a class="button button-arrow" href="contact.html#quote">Get Product Quote</a></aside></div></section>
      {guide_link}
      <section class="section surface"><div class="container"><div class="section-head"><div><p class="section-label">Processing options</p><h2 class="section-title">See the rice formats in the mill catalogue.</h2></div><p class="section-lede">These are real product photographs from the manufacturing mill. Appearance can vary by crop and lot, so final samples and specifications should be approved commercially.</p></div><div class="variant-grid">{variants}</div></div></section>
      <section class="section"><div class="container"><p class="section-label">Buying questions</p><h2 class="section-title">Before you request {escape(product['name'])}.</h2><div class="faq-list">{faq_html}</div></div></section>
      <section class="section surface"><div class="container"><p class="section-label">Related rice</p><h2 class="section-title">Compare other mill products.</h2><div class="benefit-grid">{related}</div></div></section>
      <section class="section-sm quote-band"><div class="container quote-band-grid"><div><h2>Need a bulk {escape(product['name'])} quote?</h2><p>Send process, volume, packing, destination and timeline in one message.</p></div><a class="button button-arrow" href="contact.html#quote">Request Quote</a></div></section>
    """)
    render_page(product["slug"], product["title"], product["meta"], body, "products", schema, image_path(product["image"]), f"product-page product-{product['slug'].split('.')[0]}")


def render_products() -> None:
    groups = ["Basmati rice", "Non-basmati rice", "Residue-controlled rice"]
    group_copy = {
        "Basmati rice": ("Indian basmati rice", "Six basmati ranges with actual Raw, Steam, Sella and Golden Sella mill photographs."),
        "Non-basmati rice": ("Indian non-basmati rice", "Five commercial rice ranges for wholesale, food-service, institutional and export enquiries."),
        "Residue-controlled rice": ("Pesticide residue free rice", "Four processing categories for buyers who define residue limits and review current testing."),
    }
    sections = []
    all_items = []
    position = 1
    for group in groups:
        heading, lede = group_copy[group]
        cards = []
        for product in [item for item in PRODUCTS if item["group"] == group]:
            cards.append(dedent(f"""
              <article class="catalog-card"><a class="catalog-image" href="{product['slug']}"><img src="{image_path(product['image'])}" alt="{escape(product['name'])} from UrbanFresh Rice Mills" loading="lazy" width="900" height="620"></a><div class="catalog-copy"><span>{escape(product['tag'])}</span><h3><a href="{product['slug']}">{escape(product['name'])}</a></h3><p>{escape(product['summary'])}</p><a class="text-link" href="{product['slug']}">View rice options</a></div></article>
            """).strip())
            all_items.append({"@type": "ListItem", "position": position, "url": f"https://urbanfresh.in/{product['slug']}", "name": product["name"]})
            position += 1
        sections.append(dedent(f"""
          <section class="section {'' if group == 'Non-basmati rice' else 'surface'}"><div class="container"><div class="section-head"><div><p class="section-label">{escape(group)}</p><h2 class="section-title">{escape(heading)}</h2></div><p class="section-lede">{escape(lede)}</p></div><div class="catalog-grid">{''.join(cards)}</div></div></section>
        """).strip())
    schema = {"@context": "https://schema.org", "@graph": [organization_schema(), {"@type": "CollectionPage", "name": "UrbanFresh Rice Product Catalogue", "url": "https://urbanfresh.in/products.html", "mainEntity": {"@type": "ItemList", "numberOfItems": len(all_items), "itemListElement": all_items}}]}
    body = page_hero("Complete mill catalogue", "Basmati and non-basmati rice from Karnal.", "Explore every rice range and processing category listed by our Village Daha Madanpur mill, then request a quote against your exact requirement.", "mill-hero-2.webp", [("Home", "index.html"), ("Rice Products", None)]) + "".join(sections) + dedent("""
      <section class="section-sm quote-band"><div class="container quote-band-grid"><div><h2>Found the right rice?</h2><p>Send the variety, process, quantity, packaging and destination for a mill-ready quotation.</p></div><a class="button button-arrow" href="contact.html#quote">Get a Quote</a></div></section>
    """)
    render_page("products.html", "Rice Products Manufacturer in Karnal | UrbanFresh", "Explore UrbanFresh basmati, non-basmati and residue-controlled rice products from our Karnal mill, with real product photos and processing options.", body, "products", schema, image_path("mill-hero-2.webp"))


def render_home() -> None:
    catalog_names = [item["name"] for item in PRODUCTS]
    schema = {"@context": "https://schema.org", "@graph": [organization_schema(), {"@type": "WebSite", "name": "UrbanFresh Rice Mills", "url": "https://urbanfresh.in/"}, {"@type": "OfferCatalog", "name": "UrbanFresh Rice Catalogue", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Product", "name": name}} for name in catalog_names]}]}
    featured = "".join(dedent(f"""
      <article class="catalog-card compact"><a class="catalog-image" href="{p['slug']}"><img src="{image_path(p['image'])}" alt="{escape(p['name'])} produced at the UrbanFresh mill" loading="lazy" width="900" height="620"></a><div class="catalog-copy"><span>{escape(p['group'])}</span><h3><a href="{p['slug']}">{escape(p['name'])}</a></h3><a class="text-link" href="{p['slug']}">See processing options</a></div></article>
    """).strip() for p in PRODUCTS[:6])
    body = dedent(f"""
      <section class="hero real-hero" style="--hero-image:url('/{image_path('mill-hero-1.webp')}')"><div class="container hero-inner"><div class="hero-content"><div class="hero-kicker">Rice manufacturer in Karnal, Haryana</div><h1>A real rice mill. <span>A complete product range.</span></h1><p>UrbanFresh represents our family-operated rice mill at Village Daha Madanpur, Karnal. Established in 1978, the mill produces basmati and non-basmati rice for Indian and overseas buyers.</p><div class="hero-actions"><a class="button button-arrow" href="contact.html#quote">Request a Mill Quote</a><a class="button button-ghost" href="products.html">View All Rice Products</a></div><div class="hero-note"><span>230 MT daily capacity</span><span>3 production units</span><span>30+ country reach</span></div></div></div></section>
      <section class="fact-strip"><div class="container fact-grid"><div><strong>1978</strong><span>Mill established</span></div><div><strong>230 MT</strong><span>Stated daily production capacity</span></div><div><strong>3</strong><span>Production units</span></div><div><strong>30+</strong><span>Countries reached</span></div></div></section>
      <section class="section"><div class="container intro-grid"><div class="photo-stack"><img src="{image_path('mill-about-1.webp')}" alt="White rice in an open jute sack" width="900" height="700"><img src="{image_path('mill-about-2.webp')}" alt="Rice grains presented for trade" loading="lazy" width="700" height="700"></div><div><p class="section-label">UrbanFresh Rice Mills</p><h2 class="section-title">From paddy procurement to packed rice.</h2><p class="section-lede">The mill handles paddy selection, drying, parboiling, cleaning, milling, sorting and packaging. Modern pre-cleaners, de-huskers, polishers, sortex equipment, bins and magnets support the production flow.</p><ul class="check-list"><li>Family-operated rice manufacturing base in Karnal.</li><li>Basmati, non-basmati and residue-controlled rice ranges.</li><li>Bulk trade, export and buyer-brand packaging conversations.</li></ul><p><a class="button button-outline button-arrow" href="infrastructure.html">See the Mill Infrastructure</a></p></div></div></section>
      <section class="section surface"><div class="container"><div class="section-head"><div><p class="section-label">Basmati rice range</p><h2 class="section-title">Six basmati varieties, shown with real mill photographs.</h2></div><p class="section-lede">Each product page includes the processing formats listed by the mill. Final crop, specification and availability are confirmed against your enquiry.</p></div><div class="catalog-grid">{featured}</div><p class="section-action"><a class="button button-arrow" href="products.html">Explore Complete Catalogue</a></p></div></section>
      <section class="section"><div class="container guide-feature"><div class="guide-feature-images"><img src="{image_path('category-1121.webp')}" alt="1121 Basmati rice grains" loading="lazy" width="700" height="520"><img src="{image_path('category-1509.webp')}" alt="1509 Basmati rice grains" loading="lazy" width="700" height="520"><img src="{image_path('category-1401.webp')}" alt="1401 Basmati rice grains" loading="lazy" width="700" height="520"></div><div><p class="section-label">Buyer guide</p><h2 class="section-title">1121, 1509 or 1401: what can the grain actually tell you?</h2><p class="section-lede">Compare like-for-like processing, inspect uniformity and chalkiness, then cook a controlled sample. Grain appearance is useful, but it should support a written specification rather than replace one.</p><a class="button button-outline button-arrow" href="{GUIDE_SLUG}">Read the Comparison Guide</a></div></div></section>
      <section class="section surface-dark"><div class="container split"><div><p class="section-label">Plant and process</p><h2 class="section-title">Built for cleaning, parboiling, drying and milling.</h2><p class="section-lede">The parboiling process uses treated soft water and sensor-controlled soaking. Mechanised drying is designed for uniform drying, while milling equipment supports cleaning, sorting, polishing and contamination control.</p><p><a class="button button-ghost button-arrow" href="infrastructure.html">Tour the Infrastructure</a></p></div><div class="dark-photo"><img src="{image_path('mill-plant.webp')}" alt="Rice processing plant at the Karnal mill" loading="lazy" width="900" height="720"></div></div></section>
      <section class="section"><div class="container content-grid"><article class="prose"><p class="section-label">Quality and registrations</p><h2>Checks begin before paddy enters the plant.</h2><p>Field procurement, drying, storage, pre-cleaning, de-stoning, grading, paddy separation, metal detection and trained supervision all form part of the mill's stated quality process.</p><p>Available mill documents include ISO 22000:2018, FSSAI, APEDA, U.S. FDA registration, Importer Exporter Code and rice-mill registrations. Buyers should request current copies and verify their scope for the intended order.</p><p><a class="button button-outline" href="quality.html">Quality Process</a> <a class="button button-outline" href="certifications.html">View Certificates</a></p></article><aside class="address-panel"><p class="section-label">Mill location</p><h2>119/6, Highway</h2><p>Village Daha, Madanpur<br>Karnal 132001, Haryana, India</p><a class="button button-arrow" href="contact.html#quote">Send Your Requirement</a></aside></div></section>
      <section class="section surface"><div class="container"><div class="section-head"><div><p class="section-label">Buyer questions</p><h2 class="section-title">Start with the facts that affect the order.</h2></div></div><div class="faq-list"><details class="faq"><summary>Which rice varieties does UrbanFresh manufacture?</summary><p>The catalogue covers six basmati ranges, five non-basmati ranges and four residue-controlled processing categories.</p></details><details class="faq"><summary>Where is the UrbanFresh rice mill?</summary><p>The manufacturing address is {ADDRESS}.</p></details><details class="faq"><summary>Can I request private-label packing?</summary><p>Yes. Send the rice, pack sizes, material, artwork status, volume and destination market for review.</p></details><details class="faq"><summary>Can overseas buyers and merchant exporters enquire?</summary><p>Yes. Include the destination country or port, product, volume, packaging and documentation expectations.</p></details></div></div></section>
      <section class="section-sm quote-band"><div class="container quote-band-grid"><div><h2>Send your requirement to the mill.</h2><p>Tell us the rice, process, quantity, pack and destination. We will review the commercial fit.</p></div><a class="button button-arrow" href="contact.html#quote">Get My Quote</a></div></section>
    """)
    render_page("index.html", "Rice Mill in Karnal | UrbanFresh Rice Manufacturer", "UrbanFresh is a family-operated rice mill in Village Daha Madanpur, Karnal, producing basmati and non-basmati rice for Indian and export buyers.", body, "home", schema, image_path("mill-hero-1.webp"))


def render_about() -> None:
    schema = {"@context": "https://schema.org", "@graph": [organization_schema(), {"@type": "AboutPage", "name": "About UrbanFresh Rice Mills", "url": "https://urbanfresh.in/about.html"}]}
    gallery = "".join(f'<figure><img src="{image_path(name)}" alt="{alt}" loading="lazy" width="900" height="700"></figure>' for name, alt in [
        ("mill-about-1.webp", "White rice in an open jute sack"), ("mill-about-2.webp", "Rice grains presented for trade"), ("mill-about-3.webp", "Basmati rice with paddy stalks and wooden utensils"), ("mill-about-4.webp", "Paddy and white rice in jute sacks and bowls"), ("mill-choose.webp", "Rice grains arranged around kitchen utensils"), ("mill-about-panel.webp", "Cooked basmati rice served in a bowl"),
    ])
    body = page_hero("Family rice business since 1978", "A Karnal rice mill built across generations.", "UrbanFresh represents our family-operated manufacturing mill at Village Daha Madanpur, with three production units and a rice business history beginning in 1978.", "mill-about-3.webp", [("Home", "index.html"), ("About the Mill", None)]) + dedent(f"""
      <section class="section"><div class="container split"><div><p class="section-label">Our mill story</p><h2 class="section-title">From a family enterprise to an integrated rice operation.</h2><p class="section-lede">The business began in 1978 and grew into three production units serving Indian and overseas buyers. The mill's work covers procurement, processing, quality control, packaging and commercial coordination.</p><p>Our rice range has reached buyers across more than 30 countries. The operating principle remains practical: understand the buyer's market, match the right rice and processing style, then confirm the specification and terms before production.</p></div><div class="photo-stack"><img src="{image_path('mill-about-3.webp')}" alt="Basmati rice with paddy stalks and wooden utensils" width="900" height="700"><img src="{image_path('mill-about-4.webp')}" alt="Paddy and white rice presented in jute and bowls" loading="lazy" width="700" height="700"></div></div></section>
      <section class="fact-strip"><div class="container fact-grid"><div><strong>1978</strong><span>Established</span></div><div><strong>3</strong><span>Production units</span></div><div><strong>230 MT</strong><span>Daily capacity stated by the mill</span></div><div><strong>30+</strong><span>Countries reached</span></div></div></section>
      <section class="section surface"><div class="container"><div class="section-head"><div><p class="section-label">Our rice</p><h2 class="section-title">Rice photographs supplied by the manufacturing business.</h2></div><p class="section-lede">These source images show the products and rice story behind the UrbanFresh buying conversation.</p></div><div class="mill-gallery">{gallery}</div></div></section>
      <section class="section"><div class="container"><p class="section-label">How we work</p><h2 class="section-title">A complete requirement comes before a commercial promise.</h2><div class="benefit-grid"><article class="benefit-card"><span class="number">01</span><h3>Understand the buyer</h3><p>Market, channel, destination, volume and buying timeline shape the right product discussion.</p></article><article class="benefit-card"><span class="number">02</span><h3>Match the mill product</h3><p>Basmati, non-basmati, processing style and packaging are aligned with the intended use.</p></article><article class="benefit-card"><span class="number">03</span><h3>Confirm before supply</h3><p>Specification, evidence, availability, price, packaging and dispatch are tied to the accepted order.</p></article></div></div></section>
      <section class="section-sm quote-band"><div class="container quote-band-grid"><div><h2>Talk directly about your rice requirement.</h2><p>UrbanFresh uses your product, volume, pack and destination to start the mill conversation.</p></div><a class="button button-arrow" href="contact.html#quote">Contact the Mill</a></div></section>
    """)
    render_page("about.html", "About UrbanFresh Rice Mill in Karnal | Since 1978", "Meet UrbanFresh Rice Mills at Village Daha Madanpur, Karnal. Our family-operated rice business began in 1978 and now runs three production units.", body, "about", schema, image_path("mill-about-3.webp"))


def render_infrastructure() -> None:
    schema = {"@context": "https://schema.org", "@graph": [organization_schema(), {"@type": "WebPage", "name": "UrbanFresh Rice Mill Infrastructure", "url": "https://urbanfresh.in/infrastructure.html", "about": {"@type": "Thing", "name": "Rice milling, parboiling and drying infrastructure"}}]}
    body = page_hero("Rice processing infrastructure", "A mill built for controlled processing from paddy to pack.", "See the plant systems used for cleaning, parboiling, drying, milling, sorting and packaging at our Village Daha Madanpur manufacturing base.", "mill-infrastructure.webp", [("Home", "index.html"), ("Infrastructure", None)]) + dedent(f"""
      <section class="section"><div class="container split"><div class="photo-frame"><img src="{image_path('mill-infrastructure.webp')}" alt="UrbanFresh rice mill infrastructure in Karnal" width="1000" height="760"></div><div><p class="section-label">The plant</p><h2 class="section-title">Modern equipment across the processing line.</h2><p class="section-lede">The stated daily production capacity is 230 metric tons. The mill uses pre-cleaners, de-huskers, polishers, sortex equipment, silky polishers, rice bins and magnets across the manufacturing flow.</p><ul class="check-list"><li>Paddy procurement, drying and warehousing.</li><li>Cleaning, de-stoning, grading and separation.</li><li>Parboiling, drying, milling, sorting and polishing.</li><li>Packaging and logistics coordination.</li></ul></div></div></section>
      <section class="section surface"><div class="container"><p class="section-label">Processing systems</p><h2 class="section-title">Four connected parts of the mill.</h2><div class="process-grid light-process"><div class="process-step"><span class="step-number">01</span><h3>Parboiling</h3><p>Treated soft water, controlled temperatures and sensor-equipped soaking bins support the parboiling process.</p></div><div class="process-step"><span class="step-number">02</span><h3>Drying</h3><p>Mechanised, sensor-based temperature control is used to promote uniform drying and reduce grain breakage.</p></div><div class="process-step"><span class="step-number">03</span><h3>Milling</h3><p>Cleaning, de-husking, sorting, polishing, magnets and rice bins support a controlled production flow.</p></div><div class="process-step"><span class="step-number">04</span><h3>Packing</h3><p>Product, pack format, quality brief and logistics are coordinated against the accepted order.</p></div></div></div></section>
      <section class="section surface-dark"><div class="container photo-feature"><img src="{image_path('mill-video.webp')}" alt="Terraced rice fields in a green valley" loading="lazy" width="1200" height="760"><div><p class="section-label">Mill operations</p><h2 class="section-title">Production is only one part of dependable supply.</h2><p class="section-lede">The buyer's specification, quality evidence, packaging, documentation, destination and dispatch plan all have to remain aligned through the order.</p><a class="button button-ghost button-arrow" href="contact.html#quote">Send a Production Enquiry</a></div></div></section>
      <section class="section"><div class="container photo-pair"><figure><img src="{image_path('mill-plant.webp')}" alt="Industrial rice plant and processing equipment" loading="lazy" width="900" height="700"><figcaption>Plant and processing equipment</figcaption></figure><figure><img src="{image_path('mill-hero-3.webp')}" alt="Terraced rice fields during the growing season" loading="lazy" width="900" height="700"><figcaption>Rice cultivation</figcaption></figure></div></section>
      <section class="section-sm quote-band"><div class="container quote-band-grid"><div><h2>Need mill capacity for a real order?</h2><p>Send product, process, volume, pack, destination and required timeline for a feasibility review.</p></div><a class="button button-arrow" href="contact.html#quote">Check Order Fit</a></div></section>
    """)
    render_page("infrastructure.html", "Rice Mill Infrastructure in Karnal | UrbanFresh", "Explore UrbanFresh rice mill infrastructure in Village Daha Madanpur, Karnal, including parboiling, drying, milling, sorting and packaging systems.", body, "infrastructure", schema, image_path("mill-infrastructure.webp"))


def render_quality() -> None:
    schema = {"@context": "https://schema.org", "@graph": [organization_schema(), {"@type": "WebPage", "name": "UrbanFresh Rice Quality Control", "url": "https://urbanfresh.in/quality.html", "about": {"@type": "Thing", "name": "Rice quality control and research"}}]}
    body = page_hero("Rice quality control", "Checks from paddy procurement to packed rice.", "The mill's quality process begins in the field and continues through drying, storage, cleaning, milling, sorting, packing and commercial approval.", "mill-quality.webp", [("Home", "index.html"), ("Quality", None)]) + dedent(f"""
      <section class="section"><div class="container split"><div class="photo-frame"><img src="{image_path('mill-quality.webp')}" alt="Rice quality control at UrbanFresh Rice Mills" width="1000" height="760"></div><div><p class="section-label">Procurement and process control</p><h2 class="section-title">Quality begins before milling.</h2><p class="section-lede">Representatives review paddy during harvest, while drying, transport and warehouse storage are managed before the grain enters the plant. Production checks then continue across cleaning, grading, separation and milling.</p><ul class="check-list"><li>Pre-cleaners, de-stoners and precision graders.</li><li>Paddy separators, de-huskers, magnets and metal detectors.</li><li>Trained supervision at key processing stages.</li><li>Buyer-approved specification before commercial closure.</li></ul></div></div></section>
      <section class="section surface"><div class="container content-grid"><article class="prose"><h2>What buyers should confirm</h2><p>A product name does not replace a commercial specification. Variety, process, crop, grain, moisture, broken tolerance, polish, cooking expectations, packaging and destination requirements should be written into the order discussion.</p><h2>Research and development</h2><p>The mill states that it invests in research, process improvement and technical participation to keep pace with changing rice technology and market requirements.</p><div class="availability-note">Certificate scope, laboratory evidence and destination compliance can change. Request current documents for the actual product and lot before placing an order.</div><p><a class="button button-arrow" href="certifications.html">View Mill Certificates</a></p></article><aside class="photo-frame compact-frame"><img src="{image_path('mill-rd.webp')}" alt="Research and development in rice processing" loading="lazy" width="800" height="900"></aside></div></section>
      <section class="section"><div class="container"><p class="section-label">A practical order flow</p><h2 class="section-title">Evidence should follow the requirement.</h2><div class="benefit-grid"><article class="benefit-card"><span class="number">01</span><h3>Define the market</h3><p>Destination and customer type determine which specifications and documents matter.</p></article><article class="benefit-card"><span class="number">02</span><h3>Approve the rice</h3><p>Product, process, sample and commercial parameters should be accepted before production.</p></article><article class="benefit-card"><span class="number">03</span><h3>Verify current evidence</h3><p>Ask for documents and laboratory information applicable to the offered order and lot.</p></article></div></div></section>
      <section class="section-sm quote-band"><div class="container quote-band-grid"><div><h2>Have a target rice specification?</h2><p>Send it with volume, pack, destination and timeline for mill review.</p></div><a class="button button-arrow" href="contact.html#quote">Send Specification</a></div></section>
    """)
    render_page("quality.html", "Rice Quality Control at Karnal Mill | UrbanFresh", "See UrbanFresh rice quality control from paddy procurement through drying, cleaning, milling, sorting, metal detection, packing and buyer approval.", body, "quality", schema, image_path("mill-quality.webp"))


def render_certifications() -> None:
    certificates = [
        (1, "ISO 22000:2018 certificate"), (2, "Importer Exporter Code document"), (3, "U.S. Food and Drug registration"), (4, "FSSAI licence"), (5, "APEDA registration"), (7, "Rice mill registration"), (8, "QRO compliance document"), (9, "Importer Exporter Code record"), (10, "Mill certification document"), (11, "Mill compliance document"), (12, "Mill registration document"),
    ]
    cards = "".join(f'<figure class="certificate-card"><a href="{image_path(f"certificate-{number}.webp")}" target="_blank" rel="noopener"><img src="{image_path(f"certificate-{number}.webp")}" alt="{escape(label)} for the manufacturing mill" loading="lazy" width="900" height="1200"></a><figcaption>{escape(label)}</figcaption></figure>' for number, label in certificates)
    schema = {"@context": "https://schema.org", "@graph": [organization_schema(), {"@type": "CollectionPage", "name": "UrbanFresh Manufacturing Mill Certifications", "url": "https://urbanfresh.in/certifications.html", "about": [label for _, label in certificates]}]}
    body = page_hero("Mill registrations and certificates", "Manufacturing documents available for buyer review.", "View the certificate and registration images supplied by the Village Daha Madanpur manufacturing mill, then request current copies for your order.", "certificate-1.webp", [("Home", "index.html"), ("Certifications", None)]) + dedent(f"""
      <section class="section"><div class="container"><div class="content-grid"><article class="prose"><h2>Documents shown by the manufacturing mill</h2><p>The source mill lists ISO 22000:2018, FSSAI, APEDA, U.S. FDA registration, Importer Exporter Code, rice-mill registration and related compliance documents.</p><p>The document images show the manufacturing legal entity named on each record. UrbanFresh is the customer-facing brand used on this website.</p><div class="availability-note"><strong>Buyer verification:</strong> registrations can expire, renew or apply to a specific legal entity, unit, product or market. Request current full-resolution copies and verify validity and scope before placing an order.</div></article><aside class="info-panel"><h2>Need documents?</h2><p>Tell us the destination, rice, volume and certificates your buyer requires.</p><a class="button button-arrow" href="contact.html#quote">Request Current Copies</a></aside></div><div class="certificate-grid">{cards}</div></div></section>
      <section class="section-sm quote-band"><div class="container quote-band-grid"><div><h2>Checking documents for an order?</h2><p>Send the destination and buyer checklist so the relevant current records can be reviewed.</p></div><a class="button button-arrow" href="contact.html#quote">Send Checklist</a></div></section>
    """)
    render_page("certifications.html", "Rice Mill Certifications and Registrations | UrbanFresh", "View registrations and certificates supplied by the UrbanFresh manufacturing mill, including ISO 22000:2018, FSSAI, APEDA and export records.", body, "quality", schema, image_path("certificate-1.webp"))


def render_contact() -> None:
    varieties = "".join(f"<option>{escape(item['name'])}</option>" for item in PRODUCTS)
    schema = {"@context": "https://schema.org", "@graph": [organization_schema(), {"@type": "ContactPage", "name": "Request a Rice Mill Quote", "url": "https://urbanfresh.in/contact.html"}]}
    body = page_hero("Bulk rice quotation", "Send your requirement directly to the Karnal mill.", "Choose from the full basmati, non-basmati and residue-controlled catalogue, then add volume, packaging, destination and buying timeline.", "mill-hero-3.webp", [("Home", "index.html"), ("Get a Quote", None)]) + dedent(f"""
      <section class="section"><div class="container quote-layout"><aside class="quote-copy surface-dark"><p class="section-label">UrbanFresh, Karnal</p><h2 class="section-title">A useful quote starts with a useful brief.</h2><p class="section-lede">Rice prices change with product, process, quantity, pack and destination. Fill in what you know and ask us to advise where needed.</p><div class="contact-stack"><a class="contact-card" href="tel:{PHONE_LINK}"><small>Call UrbanFresh</small><strong>{PHONE}</strong></a><a class="contact-card" href="{WA_URL}" target="_blank" rel="noopener"><small>WhatsApp</small><strong>Start a direct chat</strong></a><div class="contact-card"><small>Rice mill location</small><strong>{ADDRESS}</strong></div></div></aside>
        <form class="quote-form" id="quote" data-quote-form novalidate><div class="form-grid">
          <div class="field"><label for="name">Name or company <span aria-hidden="true">*</span></label><input id="name" name="name" autocomplete="organization" required placeholder="Your name or business"></div>
          <div class="field"><label for="phone">Phone or WhatsApp <span aria-hidden="true">*</span></label><input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required placeholder="Country code and number"></div>
          <div class="field field-full"><label for="location">Delivery city or country *</label><input id="location" name="location" autocomplete="country-name" required placeholder="Example: Delhi, Dubai, London"></div>
          <div class="field"><label for="buyer_type">Buyer type</label><select id="buyer_type" name="buyer_type"><option value="">Select</option><option>Wholesaler / distributor</option><option>Merchant exporter</option><option>Food-service buyer</option><option>Retail rice brand</option><option>Institutional buyer</option><option>Other</option></select></div>
          <div class="field"><label for="variety">Rice product</label><select id="variety" name="variety"><option value="">Please advise</option>{varieties}<option>Other / not sure</option></select></div>
          <div class="field"><label for="processing">Processing style</label><select id="processing" name="processing"><option value="">Please advise</option><option>Raw / White</option><option>Steam</option><option>Sella / Parboiled</option><option>Golden Sella</option></select></div>
          <div class="field"><label for="quantity">Approximate quantity *</label><input id="quantity" name="quantity" required placeholder="Example: 25 MT or 1 container"></div>
          <div class="field"><label for="packaging">Packaging</label><input id="packaging" name="packaging" placeholder="Example: 25 kg bags"></div>
          <div class="field"><label for="timeline">Purchase timeline</label><select id="timeline" name="timeline"><option value="">Select</option><option>Immediately</option><option>Within 30 days</option><option>Within 1 to 3 months</option><option>Planning or comparing</option></select></div>
          <div class="field field-full"><label for="message">Other requirements</label><textarea id="message" name="message" placeholder="Target specification, destination port, branding, certificates or questions"></textarea></div>
          <div class="field honeypot" aria-hidden="true"><label for="website">Website</label><input id="website" name="website" tabindex="-1" autocomplete="off"></div>
          <div class="field-full"><button class="button button-arrow form-submit" type="submit">Save My Quote Request</button><p class="form-note">We save your request in our private lead sheet. You can continue on WhatsApp after submitting for a faster reply.</p><div class="form-status" data-form-status role="status" aria-live="polite" tabindex="-1"></div></div>
        </div></form></div></section>
      <section class="section surface"><div class="container advice-row"><div><p class="section-label">Mill-ready enquiry</p><h2 class="section-title">Specific details help us give a useful answer.</h2></div><blockquote class="buyer-example">“1121 Steam, 25 MT, 25 kg bags, delivery to Mumbai within 30 days.”<cite>A complete quote brief</cite></blockquote></div></section>
    """)
    render_page("contact.html", "Request a Bulk Rice Mill Quote | UrbanFresh Karnal", "Request a rice quote from UrbanFresh Rice Mills at Village Daha Madanpur, Karnal. Send product, process, quantity, packaging, destination and timeline.", body, "contact", schema, image_path("mill-hero-3.webp"), contact_page=True)


def render_landing_pages() -> None:
    pages = [
        ("basmati-rice-manufacturer-india.html", "Basmati Rice Manufacturer in India | UrbanFresh Karnal", "UrbanFresh is a basmati rice manufacturer in Village Daha Madanpur, Karnal, with six basmati ranges, modern processing and bulk export capability.", "Basmati rice manufacturer in India", "Manufacturing basmati rice from Karnal since 1978.", "Six basmati product ranges, four common processing styles and a plant built for cleaning, parboiling, drying, milling, sorting and packing.", "mill-hero-2.webp"),
        ("basmati-rice-exporter-india.html", "Basmati Rice Exporter from India | UrbanFresh Karnal", "Source Indian basmati rice through UrbanFresh in Karnal. Importers can request product, processing, packaging, documentation and destination-based quotations.", "Basmati rice exporter from India", "Prepare an export-ready basmati requirement.", "Importers, distributors and rice brands can discuss six basmati ranges, buyer-specified packing and destination documentation with our Karnal mill.", "mill-hero-3.webp"),
        ("rice-manufacturer-for-merchant-exporters.html", "Rice Manufacturer for Merchant Exporters | UrbanFresh", "Merchant exporters can source basmati and non-basmati rice through UrbanFresh in Karnal with mill-side product, packing and documentation coordination.", "Rice mill for merchant exporters", "Bring the overseas buyer brief directly to the mill.", "UrbanFresh gives merchant exporters a direct path to discuss rice, processing, quantity, packaging, destination and buyer documentation.", "mill-hero-1.webp"),
        ("private-label.html", "Private Label Rice Manufacturer in India | UrbanFresh", "Build a private-label rice requirement with UrbanFresh Rice Mills in Karnal. Choose rice, process, pack size, material, artwork, volume and destination.", "Private-label rice manufacturing", "Your rice brand starts with the product and pack brief.", "UrbanFresh welcomes buyer-brand enquiries across basmati and non-basmati ranges. Share pack sizes, material, artwork status, quantity and destination market.", "mill-about-2.webp"),
    ]
    for filename, title, meta, kicker, heading, intro, image in pages:
        schema = {"@context": "https://schema.org", "@graph": [organization_schema(), {"@type": "Service", "name": heading, "provider": {"@type": "Organization", "name": "UrbanFresh Rice Mills"}, "areaServed": ["India", "International"], "url": f"https://urbanfresh.in/{filename}"}]}
        body = page_hero(kicker, heading, intro, image, [("Home", "index.html"), (heading, None)]) + dedent(f"""
          <section class="section"><div class="container content-grid"><article class="prose"><h2>Start with a complete commercial brief</h2><p>{escape(intro)} The mill is located at {ADDRESS}, was established in 1978 and states a daily production capacity of 230 metric tons across three production units.</p><h2>Products available for discussion</h2><p>Buyers can ask about 1121, 1509, Traditional, 1401, Pusa and 1718 Basmati, as well as Sugandha, Sharbati, PR 11, Parmal and Sona Masoori Raw Rice. Residue-controlled Raw, Steam, Sella and Golden Sella enquiries are also listed.</p><h2>What UrbanFresh needs from you</h2><ul><li>Rice variety and processing style.</li><li>Quantity, purchase frequency and target timeline.</li><li>Pack size, material and buyer-brand requirements.</li><li>Delivery city, destination country or port.</li><li>Quality, testing and document expectations.</li></ul><div class="availability-note">Product, capacity, documents, samples, specification, pricing and delivery terms are confirmed against the actual enquiry.</div></article><aside class="info-panel"><h2>Mill enquiry</h2><p>Send these details together.</p><div class="spec-list"><div class="spec-row"><span>Rice</span><strong>Product + process</strong></div><div class="spec-row"><span>Volume</span><strong>Metric tons</strong></div><div class="spec-row"><span>Pack</span><strong>Size + material</strong></div><div class="spec-row"><span>Destination</span><strong>City / port / country</strong></div><div class="spec-row"><span>Timeline</span><strong>Buying window</strong></div></div><a class="button button-arrow" href="contact.html#quote">Send Requirement</a></aside></div></section>
          <section class="section surface"><div class="container split"><div class="photo-frame"><img src="{image_path(image)}" alt="Rice sourcing visual for {escape(heading)}" loading="lazy" width="1000" height="760"></div><div><p class="section-label">Karnal mill base</p><h2 class="section-title">Manufacturing from Village Daha, Madanpur, Karnal.</h2><p class="section-lede">The plant covers paddy handling, parboiling, drying, cleaning, milling, sorting and packaging. Buyers can review the infrastructure, quality process and available registrations before commercial closure.</p><p><a class="button button-outline" href="infrastructure.html">Infrastructure</a> <a class="button button-outline" href="certifications.html">Certificates</a></p></div></div></section>
          <section class="section-sm quote-band"><div class="container quote-band-grid"><div><h2>Have a buyer requirement ready?</h2><p>Send product, volume, pack, destination and timeline in one message.</p></div><a class="button button-arrow" href="contact.html#quote">Request Quote</a></div></section>
        """)
        render_page(filename, title, meta, body, "", schema, image_path(image))


def render_buyer_guide() -> None:
    faq = [
        ("Can I identify 1121, 1509 and 1401 Basmati only by looking at the grain?", "You can use grain appearance for an initial comparison, but sight alone is not reliable authentication. Compare the same processing style, measure a representative sample, cook it under controlled conditions and confirm the written product specification."),
        ("Why should Steam rice be compared with Steam rice?", "Raw, Steam, Sella and Golden Sella are processing styles that change colour, surface appearance and cooking behaviour. Comparing different processing styles can hide the differences you are trying to evaluate between varieties."),
        ("Which Basmati variety is chosen for extra-long cooked presentation?", "1121 Basmati is widely shortlisted when extra-long grain presentation and elongation are priorities. The offered lot still needs to be checked because crop, ageing, milling and sorting affect the final result."),
        ("What should a bulk buyer request before placing an order?", "Request a representative sample, processing style, crop and ageing details, average grain measurement, broken tolerance, moisture, cooking expectations, packaging, current documents and a written commercial specification."),
    ]
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            organization_schema(),
            {
                "@type": "Article",
                "headline": "1121 vs 1509 vs 1401 Basmati Rice: How Buyers Can Tell the Difference",
                "description": "A practical grain and cooking comparison of 1121, 1509 and 1401 Basmati rice for wholesale and export buyers.",
                "url": f"https://urbanfresh.in/{GUIDE_SLUG}",
                "datePublished": "2026-07-14",
                "dateModified": "2026-07-14",
                "author": {"@type": "Organization", "name": "UrbanFresh Rice Mills"},
                "publisher": {"@type": "Organization", "name": "UrbanFresh Rice Mills", "logo": {"@type": "ImageObject", "url": "https://urbanfresh.in/assets/images/urbanfresh-logo.webp"}},
                "image": [
                    f"https://urbanfresh.in/{image_path('category-1121.webp')}",
                    f"https://urbanfresh.in/{image_path('category-1509.webp')}",
                    f"https://urbanfresh.in/{image_path('category-1401.webp')}",
                ],
                "about": ["1121 Basmati Rice", "1509 Basmati Rice", "1401 Basmati Rice", "Basmati rice grain identification"],
            },
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}} for question, answer in faq]},
        ],
    }
    faq_html = "".join(f'<details class="faq"><summary>{escape(question)}</summary><p>{escape(answer)}</p></details>' for question, answer in faq)
    body = page_hero(
        "Basmati buyer guide",
        "1121 vs 1509 vs 1401 Basmati Rice: how can a buyer tell the difference?",
        "A practical way to compare grain appearance, processing style and cooked performance before you approve a bulk rice specification.",
        "category-1121.webp",
        [("Home", "index.html"), ("Rice Products", "products.html"), ("1121 vs 1509 vs 1401", None)],
    ) + dedent(f"""
      <section class="section"><div class="container article-layout"><article class="buyer-article">
        <div class="article-meta"><span>Buyer education</span><time datetime="2026-07-14">14 July 2026</time><span>UrbanFresh Rice Mills, Karnal</span></div>
        <p class="article-lead">1121, 1509 and 1401 are three important numbered Basmati varieties. A common buyer question is simple: if three samples are all Steam rice, how do you tell them apart by looking at the grains?</p>
        <div class="quick-answer"><strong>Short answer:</strong> compare like with like, inspect a representative grain sample and then run the same cooking test on every sample. Appearance can help you screen rice, but it cannot replace the supplier's written variety, crop and quality specification.</div>

        <h2 id="processing-first">First, compare the same processing style</h2>
        <p>Before comparing varieties, check whether every sample has been processed in the same way. Raw or White, Steam, Sella and Golden Sella are processing styles. They can change the grain's colour, surface and cooking behaviour.</p>
        <p>That means 1121 Steam should be compared with 1509 Steam and 1401 Steam. Comparing 1121 Steam with 1401 Golden Sella may tell you more about processing than variety.</p>

        <div class="comparison-visuals" aria-label="Basmati rice grain comparison photographs">
          <figure><img src="{image_path('1121-steam.webp')}" alt="1121 Steam Basmati rice grains" loading="lazy" width="900" height="650"><figcaption><strong>1121 Steam</strong><span>Extra-long grain presentation</span></figcaption></figure>
          <figure><img src="{image_path('1509-steam.webp')}" alt="1509 Steam Basmati rice grains" loading="lazy" width="900" height="650"><figcaption><strong>1509 Steam</strong><span>Commercial long-grain option</span></figcaption></figure>
          <figure><img src="{image_path('1401-steam.webp')}" alt="1401 Steam Basmati rice grains" loading="lazy" width="900" height="650"><figcaption><strong>1401 Steam</strong><span>Aromatic numbered Basmati</span></figcaption></figure>
        </div>
        <p class="image-note">The photographs are reference examples from the mill catalogue. Crop, ageing, polishing, sorting, lighting and the offered lot can change appearance.</p>

        <h2 id="at-a-glance">1121 vs 1509 vs 1401 at a glance</h2>
        <div class="table-scroll" role="region" aria-label="1121, 1509 and 1401 Basmati rice comparison" tabindex="0"><table class="comparison-table">
          <caption>Practical screening points for bulk buyers</caption>
          <thead><tr><th scope="col">Buyer question</th><th scope="col">1121 Basmati</th><th scope="col">1509 Basmati</th><th scope="col">1401 Basmati</th></tr></thead>
          <tbody>
            <tr><th scope="row">Common buying position</th><td>Often shortlisted for premium extra-long presentation.</td><td>Often discussed as a practical commercial Basmati option.</td><td>Often considered when aroma and cooked-kernel uniformity matter.</td></tr>
            <tr><th scope="row">What to inspect dry</th><td>Average kernel length, slenderness, uniformity, taper, chalkiness and broken percentage.</td><td>The same measurements, with close attention to lot uniformity because similar processing can resemble 1121.</td><td>Uniformity, shape, chalkiness, broken percentage and consistency across the sample.</td></tr>
            <tr><th scope="row">What to inspect cooked</th><td>Elongation, separation, shape retention, aroma and mouthfeel.</td><td>Elongation, cooking yield, separation, texture and consistency.</td><td>Uniform cooked shape, aroma, separation and texture.</td></tr>
            <tr><th scope="row">Do not approve from</th><td colspan="3">One photograph, a few hand-picked grains or a product name without a written lot specification.</td></tr>
          </tbody>
        </table></div>

        <h2 id="visual-check">A six-step grain check for buyers</h2>
        <ol class="numbered-checks">
          <li><strong>Label every sample.</strong><span>Record the claimed variety, processing style, crop, ageing and supplier before opening the sample.</span></li>
          <li><strong>Compare a representative quantity.</strong><span>Do not judge the lot from four or five attractive grains selected by hand.</span></li>
          <li><strong>Use the same surface and light.</strong><span>Spread each sample separately on a clean, dark, matte surface under neutral light.</span></li>
          <li><strong>Measure, do not guess.</strong><span>Check a random set of kernels for average length and width. Record broken, chalky, damaged and discoloured grains.</span></li>
          <li><strong>Cook equal samples the same way.</strong><span>Use equal rice weight, soaking time, water, vessel and cooking time. Compare elongation, separation, aroma, shape and texture.</span></li>
          <li><strong>Match the result to the contract.</strong><span>Keep a sealed approval sample and make sure the agreed variety and quality limits appear in the written commercial specification.</span></li>
        </ol>

        <h2 id="variety-not-grade">Variety is not the same as grade</h2>
        <p>A rice sample can be genuine 1121, 1509 or 1401 and still fail a buyer's quality target. Variety names do not tell you the broken percentage, moisture, foreign matter, polish, crop, ageing, residue position, cooking result or packaging quality.</p>
        <p>This is why a useful purchase enquiry combines the variety with the processing style and measurable acceptance points. For example: “1121 Steam Basmati, current or aged crop as agreed, buyer-approved grain and cooking specification, 25 kg bags, delivery to the stated destination.”</p>

        <h2 id="choosing">Which variety should you choose?</h2>
        <div class="choice-grid">
          <article><h3>Choose 1121 for</h3><p>Buyers prioritising extra-long visual presentation and strong cooked elongation, subject to sample and specification approval.</p><a class="text-link" href="1121-basmati-rice.html">View 1121 options</a></article>
          <article><h3>Choose 1509 for</h3><p>Commercial buying programmes balancing long-grain presentation, cooking performance, availability and target price.</p><a class="text-link" href="1509-basmati-rice.html">View 1509 options</a></article>
          <article><h3>Choose 1401 for</h3><p>Buyers comparing aroma, cooked-kernel uniformity and an alternative numbered Basmati position.</p><a class="text-link" href="1401-basmati-rice.html">View 1401 options</a></article>
        </div>

        <h2 id="quote-brief">What to send the mill for an accurate quote</h2>
        <p>Send the variety, processing style, approximate metric tons, pack size and material, destination, buying timeline and any fixed quality limits. If you have not finalised the variety, send your target cooked result and market position so the mill can discuss an appropriate sample.</p>
        <div class="availability-note"><strong>Practical rule:</strong> photographs help start the conversation. A representative sample, controlled cooking test and accepted written specification should finish it.</div>

        <h2 id="questions">Buyer questions about 1121, 1509 and 1401</h2>
        <div class="faq-list">{faq_html}</div>

        <div class="article-sources"><h2>Technical references</h2><p>This guide combines the buyer question in the supplied transcript with mill product photographs and established variety information.</p><ul><li><a href="https://icar.gov.in/en/crop-science/basmati-rice-varieties" target="_blank" rel="noopener">ICAR: Basmati rice varieties</a></li><li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5890003/" target="_blank" rel="noopener">Pusa Basmati 1121 and related improved varieties</a></li><li><a href="https://www.apeda.gov.in/sites/default/files/product/NEWLY_RELEASED_BASMATI_VARIETIES.pdf" target="_blank" rel="noopener">APEDA: newly released Basmati varieties</a></li></ul></div>
      </article>
      <aside class="article-aside"><div><p class="section-label">In this guide</p><nav aria-label="Article contents"><a href="#processing-first">Compare processing first</a><a href="#at-a-glance">Difference at a glance</a><a href="#visual-check">Six-step grain check</a><a href="#variety-not-grade">Variety vs grade</a><a href="#choosing">Which variety to choose</a><a href="#quote-brief">Build a quote brief</a></nav></div><div class="article-quote"><h2>Compare a real sample</h2><p>Send your rice, process, quantity, pack and destination.</p><a class="button button-arrow" href="contact.html#quote">Request a Mill Quote</a></div></aside>
      </div></section>
      <section class="section-sm quote-band"><div class="container quote-band-grid"><div><h2>Need help choosing the right Basmati?</h2><p>Tell UrbanFresh what your buyer wants to see after cooking, then request comparable mill samples.</p></div><a class="button button-arrow" href="contact.html#quote">Send Your Requirement</a></div></section>
    """)
    render_page(
        GUIDE_SLUG,
        "1121 vs 1509 vs 1401 Basmati Rice: Buyer Guide | UrbanFresh",
        "Compare 1121, 1509 and 1401 Basmati rice by grain appearance, processing style and cooked performance. A practical guide for bulk rice buyers.",
        body,
        "",
        schema,
        image_path("category-1121.webp"),
        "buyer-guide-page",
    )


def render_sitemap() -> None:
    pages = [
        ("", "weekly", "1.0"), ("products.html", "monthly", "0.9"), ("about.html", "monthly", "0.8"), ("infrastructure.html", "monthly", "0.8"), ("quality.html", "monthly", "0.8"), ("certifications.html", "monthly", "0.7"), ("contact.html", "monthly", "0.9"),
        (GUIDE_SLUG, "monthly", "0.9"),
        ("basmati-rice-manufacturer-india.html", "monthly", "0.9"), ("basmati-rice-exporter-india.html", "monthly", "0.9"), ("rice-manufacturer-for-merchant-exporters.html", "monthly", "0.8"), ("private-label.html", "monthly", "0.8"),
    ] + [(item["slug"], "monthly", "0.9") for item in PRODUCTS]
    urls = "\n".join(f'  <url><loc>https://urbanfresh.in/{slug}</loc><changefreq>{freq}</changefreq><priority>{priority}</priority></url>' for slug, freq, priority in pages)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")


def main() -> None:
    for product in PRODUCTS:
        render_product_page(product)
    render_products()
    render_home()
    render_about()
    render_infrastructure()
    render_quality()
    render_certifications()
    render_contact()
    render_landing_pages()
    render_buyer_guide()
    render_sitemap()
    print(f"Rebuilt UrbanFresh with {len(PRODUCTS)} product pages.")


if __name__ == "__main__":
    main()
