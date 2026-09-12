from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGAL_ENTITY = "Rajesh Industries"
ADDRESS_PARTS = (
    "119/6, Mile Stone, GT Road",
    "Opp to Neelkanth Dhaba",
    "Daha Madanpur Village, Near Namastey Chowk",
    "Karnal, Haryana - 132001, India",
)
STREET_ADDRESS = ", ".join(ADDRESS_PARTS[:3])


class LegalEntityAddressTests(unittest.TestCase):
    def test_legal_entity_and_address_are_visible_on_every_page(self) -> None:
        pages = sorted(ROOT.glob("*.html"))
        self.assertEqual(len(pages), 30)
        for page in pages:
            source = page.read_text(encoding="utf-8")
            self.assertIn(LEGAL_ENTITY, source, page.name)
            for part in ADDRESS_PARTS:
                self.assertIn(part, source, page.name)

    def test_organization_schema_uses_legal_name_and_exact_address(self) -> None:
        for page in sorted(ROOT.glob("*.html")):
            source = page.read_text(encoding="utf-8")
            scripts = re.findall(
                r'<script type="application/ld\+json">(.*?)</script>',
                source,
                flags=re.DOTALL,
            )
            organizations = []
            for script in scripts:
                data = json.loads(script)
                nodes = data.get("@graph", [data])
                organizations.extend(
                    node
                    for node in nodes
                    if "Organization" in node.get("@type", [])
                )
            if not organizations:
                self.assertEqual(page.name, "thank-you.html")
                continue
            organization = organizations[0]
            self.assertEqual(organization["legalName"], LEGAL_ENTITY, page.name)
            self.assertEqual(
                organization["address"]["streetAddress"], STREET_ADDRESS, page.name
            )


if __name__ == "__main__":
    unittest.main()
