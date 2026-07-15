# Ubersuggest external research — 2026-07-15

## Source

- Provider: Ubersuggest MCP using the OAuth-authorized Individual Lifetime account
- Tool: `keyword_overview`
- Country/database: India
- Research type: read-only connection and keyword-metric baseline

## Verified keyword metric

| Keyword | Search volume | SEO difficulty | CPC | Account-limit error |
|---|---:|---:|---:|---|
| basmati rice supplier india | 0 | 4 | 0 | None |

## Decision

The exact query has low reported difficulty but no reported demand. Combined with zero current Search Console rows, this is not enough evidence for a new keyword landing page.

Ubersuggest's site audit separately flagged `https://urbanfresh.in/contact.html` as a poorly formatted SEO URL. Its character and dynamic checks passed; only the keyword check failed. The URL is already short, readable and stable, with about 180 internal references. Instead of creating a risky URL migration, the existing contact page was aligned around the accurate phrase “Contact UrbanFresh Rice Mills” while retaining its bulk-rice-quote intent. The title, description, H1, ContactPage structured data and keyword map were updated together.

The next Ubersuggest crawl should verify whether that alignment clears the keyword check. A URL rename should be considered only if later search evidence justifies a migration and a permanent server-side redirect is available.

Ubersuggest metrics are third-party estimates. Search Console remains the source of truth for UrbanFresh impressions, clicks, CTR and average position.
