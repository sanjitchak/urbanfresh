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

    def test_direct_email_is_secondary_to_form_and_whatsapp(self) -> None:
        self.assertIn('CONTACT_EMAIL = "sanjit@urbanfreshrice.com"', GENERATOR)
        self.assertIn('EMAIL_URL = "mailto:sanjit@urbanfreshrice.com?subject=Domestic%20rice%20quote"', GENERATOR)
        self.assertIn('<small>Email the mill</small><strong>{CONTACT_EMAIL}</strong>', GENERATOR)
        self.assertIn('<a href="{quote_href}">Quote form</a><a href="{EMAIL_URL}">Email: {CONTACT_EMAIL}</a>', GENERATOR)
        self.assertIn('<div class="mobile-cta"><a class="button button-whatsapp"', GENERATOR)
        self.assertNotIn('<div class="mobile-cta"><a class="button" href="{EMAIL_URL}"', GENERATOR)


if __name__ == "__main__":
    unittest.main()
