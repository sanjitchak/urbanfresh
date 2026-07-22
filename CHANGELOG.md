# UrbanFresh project handoff

Read this file first when starting a new chat. Keep it concise and update it with every material change so the next chat can continue safely.

## Current state

- Production site: `https://urbanfresh.in/`
- Repository: `sanjitchak/urbanfresh`, default branch `main`
- Local project: `/Users/Administrator/Downloads/RIce business/urbanfresh`
- SEO audit baseline: 29 HTML pages passing the local audit as of 2026-07-22
- Search Console: service account has Full access; authenticated sitemap submission is working
- Deployment automation: SEO-relevant pushes to `main` wait for the live sitemap, submit it to Search Console, and verify the recorded sitemap
- Monthly SEO automation: active on the first Monday at 10:00 AM IST; uses Search Console as the first-party source and Ubersuggest as secondary research

## Open items

- **2026-07-21 — Product snippets structured-data warning:** Search Console identified five invalid Product items on the homepage. PR #7 deployed the truthful correction as commit `67c9fb2`, replacing unsupported `Product` claims with `ItemList`, `ItemPage`, and `Thing` markup because UrbanFresh does not publish fixed offers or verified reviews on those pages. The live homepage and a live rice detail page were verified with zero Product nodes, and Search Console validation started on 2026-07-22. Keep this item open until Google reports validation passed.

## Change history

### 2026-07-22 — First-party mill photography integrated

- Added optimized WebP photographs of the processing plant, mill office and RI-marked chimney supplied by the mill team.
- Replaced generic imagery in prominent homepage and About-page proof areas, and added a captioned photographed-at-our-mill gallery to the Infrastructure page.
- Added descriptive image alt text and truthful Organization, AboutPage and WebPage image references without changing product or capacity claims.
- Validated all 29 pages, all 14 unit tests, desktop and mobile layouts, image loading, mobile CTAs and zero browser console errors.

### 2026-07-22 — Product snippets schema correction deployed

- Confirmed in Search Console that all five current invalid items are rice entries nested in the homepage catalogue.
- Removed unsupported Product-rich-result declarations site-wide instead of inventing `offers`, `review`, or `aggregateRating` data.
- Preserved truthful Organization, WebSite, ItemList, ItemPage, Thing, CollectionPage and FAQ structured data.
- Added an audit rule and unit tests that reject any future `Product` node missing Google-required offer, review or aggregate-rating data.
- Merged PR #7 as commit `67c9fb2`; verified the live sitemap submission and live homepage/product-page JSON-LD, then started Search Console fix validation.

### 2026-07-21 — Persistent cross-chat handoff added

- Added this changelog as the canonical starting point for new chats.
- Added root `AGENTS.md` instructions requiring agents and automations to read and maintain the handoff.
- Recorded the Search Console Product snippets warning as an unresolved item.

### 2026-07-18 — Automatic Search Console submission deployed

- Added stable sitemap `<lastmod>` handling and the authenticated `scripts/submit_sitemap.py` workflow.
- Stored `GSC_CREDENTIALS_JSON` as an encrypted GitHub Actions secret; no credential was committed.
- Upgraded the Search Console automation account from Restricted to Full and verified a real sitemap submission.
- Merged PR #5 as commit `d075d79`; the first GitHub Actions submission run completed successfully.
- Updated the monthly SEO automation to verify the live sitemap and Search Console record after a successful push.

### 2026-07-17 — Business-profile links added

- Added the UrbanFresh LinkedIn company page and Google Business Profile links to the generated site and deployed them through GitHub.

### 2026-07-15 — SEO measurement loop configured

- Configured the free local SEO improver with Google Search Console reporting, CSV fallback, technical auditing, monthly logging, and Ubersuggest research guidance.
- Established the rule of at most one evidence-backed content change per monthly run; no mass pages, invented claims, purchased links, or automatic outreach.

## Standard verification commands

```bash
python3 scripts/seo_audit.py
python3 -m unittest discover -s tests -v
git diff --check
python3 scripts/submit_sitemap.py --wait-for-live --verify
```

The final command changes external Search Console state and should run only after a successful SEO-relevant deployment.
