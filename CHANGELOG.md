# UrbanFresh project handoff

Read this file first when starting a new chat. Keep it concise and update it with every material change so the next chat can continue safely.

## Current state

- Production site: `https://urbanfresh.in/`
- International site: `https://urbanfreshrice.com/` (live on GitHub Pages with HTTPS enforced)
- Repository: `sanjitchak/urbanfresh`, default branch `main`
- Local project: `/Users/Administrator/Downloads/RIce business/urbanfresh`
- SEO audit baseline: 29 HTML pages passing the expanded local audit as of 2026-07-26
- Search Console: service account has Full access; authenticated sitemap submission is working
- Deployment automation: SEO-relevant pushes to `main` wait for the live sitemap, submit it to Search Console, and verify the recorded sitemap
- Monthly SEO automation: active on the first Monday at 10:00 AM IST; uses Search Console as the first-party source and Ubersuggest as secondary research

## Open items

- Commit and push the current SEO hardening changes, then verify GitHub Pages,
  Search Console sitemap submission and the first live IndexNow submission.

## Change history

### 2026-07-26 — Crawl structure and automatic SEO guardrails prepared

- Added a truthful local image entry for every one of the 28 public sitemap
  URLs and matching `BreadcrumbList` structured data to all 27 generated pages
  that show visible breadcrumbs.
- Added homepage and sitewide contextual links to the basmati-manufacturer,
  overseas-supply and merchant-exporter pages so no indexable landing page is
  orphaned.
- Expanded `seo/keyword-map.csv` from 16 to all 28 indexable sitemap URLs with
  distinct, page-specific buyer intents and conversion actions.
- Extended the local audit and regression tests to reject sitemap/canonical
  drift, missing image entries, orphan pages, incomplete keyword coverage and
  duplicate primary intents.
- Ignored generated weekly report folders so the scheduled measurement job
  cannot dirty the publishing branch; the existing 2026-07-21 report and
  rankings files remained byte-for-byte unchanged.
- Removed the render-blocking Google Fonts CSS `@import`, added direct
  stylesheet loading with Google Fonts preconnects, and preloaded each public
  page's exact existing CSS hero WebP at high priority without changing page
  content or layout. Focused tests protect the font and hero-preload contract.
- Added the separately implemented IndexNow deployment handoff and weekly
  GitHub quality workflow; the dry run validated all 28 canonical page URLs.
- Raised evidence thresholds in the local SEO improver to 100 impressions for
  page-change opportunities and 50 impressions for cannibalization checks, so
  small or noisy samples cannot trigger automated content suggestions.
- Rebuilt all generated pages; the 29-page SEO audit, all 30 unit tests and
  `git diff --check` passed. These combined changes are local only and have not
  been committed, deployed or submitted live.

### 2026-07-26 — Desktop WhatsApp floating icon added

- Replaced the desktop “Quote on WhatsApp” text pill with a compact, circular
  WhatsApp icon linked to the existing prefilled mill chat.
- Preserved the existing mobile bottom CTA and hid the floating icon at the
  mobile breakpoint to avoid duplicate or overlapping controls.
- Rebuilt all 29 pages and verified the rendered 60 px control at desktop width;
  the SEO audit, all 16 unit tests and `git diff --check` passed.
- Published commit `5a9952d`; GitHub Pages deployment `30169545097` and Search
  Console sitemap workflow `30169545375` succeeded. Live desktop QA confirmed
  the new stylesheet, circular icon and prefilled domestic quote link.

### 2026-07-25 — Separate international buyer site wired in

- Added `urbanfreshrice.com` to the Organization entity references, global
  navigation and footer while keeping `urbanfresh.in` focused on domestic India
  sales.
- Added contextual international-site links only on the existing exporter and
  merchant-exporter landing pages.
- Added reciprocal hreflang for the genuine About-page pair and an audit map so
  broken declarations fail local validation.
- Extended the weekly SEO runner to collect both domain properties and added a
  `domain` column to the monthly experiment log.
- Reinstalled the existing Monday 09:00 local schedule with the dual-domain
  runner; the LaunchAgent passed `plutil` validation and loaded successfully.
- Search Console now reports the earlier Product-snippet issue as Passed with
  zero invalid items; the prior open warning is closed.
- Deployed commit `488c06c`; the GitHub Pages and domestic Search Console
  sitemap workflows succeeded. Live checks confirmed the navigation/footer
  links, contextual export link and reciprocal About-page hreflang.

### 2026-07-22 — First-party mill photography integrated

- Added optimized WebP photographs of the processing plant, mill office and RI-marked chimney supplied by the mill team.
- Replaced generic imagery in prominent homepage and About-page proof areas, and added a captioned photographed-at-our-mill gallery to the Infrastructure page.
- Added descriptive image alt text and truthful Organization, AboutPage and WebPage image references without changing product or capacity claims.
- Validated all 29 pages, all 14 unit tests, desktop and mobile layouts, image loading, mobile CTAs and zero browser console errors.
- Deployed the photo integration as commit `b4aa295`; GitHub Pages and the Search Console sitemap workflow succeeded, and the live pages plus all three image assets returned HTTP 200.

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
