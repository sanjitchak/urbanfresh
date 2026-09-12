from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAIM = "Our production facility is fully automated."


class AutomationClaimTests(unittest.TestCase):
    def test_claim_is_visible_on_every_html_page(self) -> None:
        pages = sorted(ROOT.glob("*.html"))
        self.assertEqual(len(pages), 30)
        for page in pages:
            self.assertIn(CLAIM, page.read_text(encoding="utf-8"), page.name)

    def test_generator_owns_the_sitewide_claim(self) -> None:
        generator = (ROOT / "scripts/rebuild_real_mill_site.py").read_text(
            encoding="utf-8"
        )
        self.assertIn(f'AUTOMATION_CLAIM = "{CLAIM}"', generator)
        self.assertIn("Fully automated production facility", generator)


if __name__ == "__main__":
    unittest.main()
