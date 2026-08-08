from __future__ import annotations

import re
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FONT_STYLESHEET = "https://fonts.googleapis.com/css2?family=Bitter:wght@500;600;650;700&family=Source+Sans+3:wght@400;500;600;700&display=swap"
SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[dict[str, str | None]] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        if tag == "link":
            self.links.append(dict(attrs))


def page_links(path: Path) -> list[dict[str, str | None]]:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.links


class PerformanceHeadTests(unittest.TestCase):
    def test_internal_home_links_use_the_canonical_root(self) -> None:
        for page in sorted(ROOT.glob("*.html")):
            html = page.read_text(encoding="utf-8")
            self.assertNotIn('href="index.html"', html, page.name)

        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        for target in (
            "infrastructure.html#mill-photos",
            "contact.html#quote",
            "sugandha-rice.html",
            "pesticide-residue-free-raw-rice.html",
        ):
            self.assertIn(f'href="{target}"', homepage, target)

    def test_fonts_load_directly_in_every_page_head_without_css_import(self) -> None:
        css = (ROOT / "assets" / "css" / "site.css").read_text(encoding="utf-8")
        self.assertNotIn("@import", css)

        for page in sorted(ROOT.glob("*.html")):
            links = page_links(page)
            self.assertIn(
                {"rel": "preconnect", "href": "https://fonts.googleapis.com"},
                links,
                page.name,
            )
            self.assertTrue(
                any(
                    link.get("rel") == "preconnect"
                    and link.get("href") == "https://fonts.gstatic.com"
                    and "crossorigin" in link
                    for link in links
                ),
                page.name,
            )
            self.assertTrue(
                any(
                    link.get("rel") == "stylesheet"
                    and link.get("href") == FONT_STYLESHEET
                    for link in links
                ),
                page.name,
            )

    def test_every_public_page_preloads_its_exact_css_hero_webp(self) -> None:
        sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
        namespace = {"sm": SITEMAP_NAMESPACE}
        page_urls = [
            entry.findtext("sm:loc", namespaces=namespace)
            for entry in sitemap.findall("sm:url", namespace)
        ]
        self.assertEqual(len(page_urls), 28)

        for page_url in page_urls:
            self.assertIsNotNone(page_url)
            relative = page_url.removeprefix("https://urbanfresh.in/")
            page = ROOT / (relative or "index.html")
            html = page.read_text(encoding="utf-8")
            hero_matches = re.findall(
                r"--(?:hero|page)-image:url\('/([^']+\.webp)'\)",
                html,
            )
            self.assertEqual(len(hero_matches), 1, page.name)
            hero_url = f"https://urbanfresh.in/{hero_matches[0]}"
            self.assertTrue((ROOT / hero_matches[0]).exists(), page.name)

            preloads = [
                link
                for link in page_links(page)
                if link.get("rel") == "preload" and link.get("as") == "image"
            ]
            self.assertEqual(len(preloads), 1, page.name)
            self.assertEqual(preloads[0].get("href"), hero_url, page.name)
            self.assertEqual(preloads[0].get("fetchpriority"), "high", page.name)


if __name__ == "__main__":
    unittest.main()
