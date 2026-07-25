from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = (ROOT / "scripts/rebuild_real_mill_site.py").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/site.css").read_text(encoding="utf-8")


class WhatsAppFloatTests(unittest.TestCase):
    def test_desktop_float_is_an_accessible_icon(self) -> None:
        self.assertIn('class="whatsapp-float"', GENERATOR)
        self.assertIn('aria-label="Chat with UrbanFresh on WhatsApp"', GENERATOR)
        self.assertIn('<svg viewBox="0 0 24 24"', GENERATOR)
        self.assertIn(".whatsapp-float svg", CSS)

    def test_mobile_layout_hides_the_float(self) -> None:
        self.assertIn(".whatsapp-float { display: none; }", CSS)


if __name__ == "__main__":
    unittest.main()
