from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JS = (ROOT / "assets/js/site.js").read_text(encoding="utf-8")
GENERATOR = (ROOT / "scripts/rebuild_real_mill_site.py").read_text(encoding="utf-8")


class FormEmailTests(unittest.TestCase):
    def test_form_requires_buyer_email_and_keeps_honeypot(self) -> None:
        self.assertIn(
            "const requiredNames = ['name', 'phone', 'email', 'location', 'quantity'];",
            JS,
        )
        self.assertIn('Business email <span aria-hidden="true">*</span>', GENERATOR)
        self.assertIn('name="email" type="email"', GENERATOR)
        self.assertIn('name="website"', GENERATOR)

    def test_frontend_emails_before_saving_sheet_backup(self) -> None:
        endpoint_call = JS.index("await fetch(EMAIL_ENDPOINT")
        sheet_call = JS.index("await fetch(GOOGLE_SHEETS_ENDPOINT")
        self.assertLess(endpoint_call, sheet_call)
        self.assertIn("https://email.urbanfreshrice.com/submit.php", JS)
        self.assertIn("Email confirmation failed.", JS)

    def test_buyer_email_is_in_whatsapp_follow_up(self) -> None:
        self.assertIn("`Business email: ${data.get('email')}`", JS)
        self.assertIn("We could not email your confirmation.", JS)


if __name__ == "__main__":
    unittest.main()
