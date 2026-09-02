from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CompetitiveComparisonTests(unittest.TestCase):
    def test_homepage_contains_aggressive_factual_comparison(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("UrbanFresh versus ordinary sourcing", homepage)
        self.assertIn("Don’t settle for a mill that leaves your order to guesswork.", homepage)
        self.assertIn("The UrbanFresh advantage", homepage)
        self.assertIn("The ordinary sourcing risk", homepage)
        self.assertEqual(homepage.count('class="advantage-row"'), 5)

    def test_comparison_is_responsive_and_source_owned(self) -> None:
        source = (ROOT / "scripts/rebuild_real_mill_site.py").read_text(encoding="utf-8")
        css = (ROOT / "assets/css/site.css").read_text(encoding="utf-8")
        self.assertIn("Direct mill-side feasibility review.", source)
        self.assertIn(".advantage-row", css)
        self.assertIn(".advantage-head { display: none; }", css)


if __name__ == "__main__":
    unittest.main()
