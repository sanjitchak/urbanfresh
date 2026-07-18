from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import rebuild_real_mill_site  # noqa: E402
import submit_sitemap  # noqa: E402


class SitemapLastmodTests(unittest.TestCase):
    def test_unchanged_page_keeps_existing_lastmod(self) -> None:
        result = rebuild_real_mill_site.choose_lastmod(
            "same html",
            "same html",
            "2026-07-01",
            "2026-07-18",
        )
        self.assertEqual(result, "2026-07-01")

    def test_changed_page_uses_build_date(self) -> None:
        result = rebuild_real_mill_site.choose_lastmod(
            "old html",
            "new html",
            "2026-07-01",
            "2026-07-18",
        )
        self.assertEqual(result, "2026-07-18")

    def test_load_sitemap_lastmods_uses_page_slugs(self) -> None:
        sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://urbanfresh.in/</loc><lastmod>2026-07-10</lastmod></url>
  <url><loc>https://urbanfresh.in/contact.html</loc><lastmod>2026-07-11</lastmod></url>
</urlset>
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sitemap.xml"
            path.write_text(sitemap, encoding="utf-8")
            result = rebuild_real_mill_site.load_sitemap_lastmods(path)

        self.assertEqual(result[""], "2026-07-10")
        self.assertEqual(result["contact.html"], "2026-07-11")


class SitemapSubmissionTests(unittest.TestCase):
    def test_wait_for_live_accepts_matching_sitemap(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sitemap.xml"
            path.write_bytes(b"<urlset></urlset>\n")
            with mock.patch.object(
                submit_sitemap,
                "fetch_live_sitemap",
                return_value=b"<urlset></urlset>\n",
            ):
                submit_sitemap.wait_for_live_sitemap(
                    path,
                    "https://urbanfresh.in/sitemap.xml",
                    timeout=0,
                )

    def test_dry_run_does_not_require_credentials(self) -> None:
        exit_code = submit_sitemap.main(["--dry-run"])
        self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
