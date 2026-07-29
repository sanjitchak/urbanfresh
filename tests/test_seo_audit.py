from __future__ import annotations

import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import seo_audit  # noqa: E402


class ProductSnippetAuditTests(unittest.TestCase):
    def test_product_without_offer_review_or_rating_is_rejected(self) -> None:
        data = {
            "@context": "https://schema.org",
            "@graph": [
                {"@type": "Product", "name": "1121 Basmati Rice"},
            ],
        }

        self.assertEqual(
            seo_audit.unsupported_product_snippets(data),
            ["1121 Basmati Rice"],
        )

    def test_product_with_truthful_offer_is_allowed(self) -> None:
        data = {
            "@type": "Product",
            "name": "Example Product",
            "offers": {
                "@type": "Offer",
                "price": 100,
                "priceCurrency": "INR",
            },
        }

        self.assertEqual(seo_audit.unsupported_product_snippets(data), [])

    def test_item_page_does_not_claim_product_rich_result(self) -> None:
        data = {
            "@type": "ItemPage",
            "name": "1121 Basmati Rice",
            "mainEntity": {"@type": "Thing", "name": "1121 Basmati Rice"},
        }

        self.assertEqual(seo_audit.unsupported_product_snippets(data), [])


class DatasetAuditTests(unittest.TestCase):
    def test_dataset_without_license_is_rejected(self) -> None:
        data = {
            "@type": "Dataset",
            "name": "Example price list",
            "description": "An example dataset without stated use terms.",
        }

        self.assertEqual(
            seo_audit.datasets_missing_license(data),
            ["Example price list"],
        )

    def test_generated_price_dataset_has_visible_versioned_license(self) -> None:
        page = ROOT / "rice-price-india.html"
        html = page.read_text(encoding="utf-8")
        parser = seo_audit.PageParser()
        parser.feed(html)
        structured_data = json.loads(seo_audit.clean(parser.jsonld_parts))
        datasets = [
            node
            for node in seo_audit.json_objects(structured_data)
            if node.get("@type") == "Dataset"
        ]

        self.assertEqual(len(datasets), 1)
        self.assertEqual(
            datasets[0].get("license"),
            {
                "@type": "CreativeWork",
                "name": "UrbanFresh Rice Price Data Use Terms, version 1",
                "url": "https://urbanfresh.in/rice-price-india.html#data-license-v1",
            },
        )
        self.assertTrue(datasets[0].get("isAccessibleForFree"))
        self.assertIn('id="data-license-v1"', html)


class SiteStructureAuditTests(unittest.TestCase):
    def test_orphan_pages_require_an_inbound_link_from_an_indexable_page(self) -> None:
        pages = {"index.html", "products.html", "orphan.html"}
        outgoing = {
            "index.html": {"products.html"},
            "products.html": {"index.html"},
            "orphan.html": {"orphan.html"},
        }

        self.assertEqual(
            seo_audit.orphan_pages(pages, outgoing),
            ["orphan.html"],
        )

    def test_keyword_map_reports_missing_extra_and_duplicate_intents(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "keyword-map.csv"
            path.write_text(
                "page,primary_search_intent,buyer_stage,conversion_action\n"
                "index.html,rice mill in Karnal,Commercial,Request quote\n"
                "extra.html,rice mill in Karnal,Commercial,Request quote\n",
                encoding="utf-8",
            )

            issues = seo_audit.keyword_map_issues(
                {"index.html", "products.html"},
                path,
            )

        self.assertIn(
            'keyword intent "rice mill in Karnal" is assigned to both index.html and extra.html',
            issues,
        )
        self.assertIn("keyword map is missing sitemap page products.html", issues)
        self.assertIn("keyword map page is absent from sitemap: extra.html", issues)

    def test_generated_pages_with_visible_crumbs_have_breadcrumb_schema(self) -> None:
        for page in sorted(ROOT.glob("*.html")):
            html = page.read_text(encoding="utf-8")
            if '<div class="breadcrumbs">' not in html:
                continue
            parser = seo_audit.PageParser()
            parser.feed(html)
            structured_data = json.loads(seo_audit.clean(parser.jsonld_parts))
            breadcrumbs = [
                node
                for node in seo_audit.json_objects(structured_data)
                if node.get("@type") == "BreadcrumbList"
            ]
            self.assertEqual(len(breadcrumbs), 1, page.name)
            items = breadcrumbs[0].get("itemListElement", [])
            self.assertGreaterEqual(len(items), 2, page.name)
            self.assertEqual(items[0].get("item"), "https://urbanfresh.in/", page.name)
            self.assertEqual(items[-1].get("item"), parser.canonical, page.name)

    def test_generated_sitemap_has_a_local_image_for_every_page(self) -> None:
        root = ET.parse(ROOT / "sitemap.xml").getroot()
        namespace = {
            "sm": seo_audit.SITEMAP_NAMESPACE,
            "image": seo_audit.IMAGE_SITEMAP_NAMESPACE,
        }
        entries = root.findall("sm:url", namespace)
        self.assertTrue(entries)
        for entry in entries:
            page_url = entry.findtext("sm:loc", namespaces=namespace)
            image_urls = [
                node.findtext("image:loc", namespaces=namespace)
                for node in entry.findall("image:image", namespace)
            ]
            self.assertTrue(image_urls, page_url)
            for image_url in image_urls:
                self.assertIsNotNone(image_url, page_url)
                image_path = ROOT / image_url.removeprefix(
                    "https://urbanfresh.in/"
                )
                self.assertTrue(image_path.exists(), image_url)


if __name__ == "__main__":
    unittest.main()
