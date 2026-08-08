# UrbanFresh project handoff

Read this file first when starting a new chat. Keep it concise and update it with every material change so the next chat can continue safely.

## Current state

- Production site: `https://urbanfresh.in/`
- International site: `https://urbanfreshrice.com/` (live on GitHub Pages with HTTPS enforced)
- Repository: `sanjitchak/urbanfresh`, default branch `main`
- Local project: `/Users/Administrator/Downloads/RIce business/urbanfresh`
- SEO audit baseline: 29 HTML pages and 38 tests passing the expanded local audit as of 2026-08-08
- Search Console: service account has Full access; authenticated sitemap submission is working
- Deployment automation: SEO-relevant pushes to `main` wait for the live
  sitemap and IndexNow key, submit and verify the sitemap in Search Console,
  then notify IndexNow
- Monitoring: weekly GitHub quality checks and a Monday 09:30 AM IST read-only
  dual-domain monitor; the evidence-gated monthly optimizer remains active on
  the first Monday at 10:00 AM IST

## Open items

- Search Console evidence remains sparse. Wait for a full comparable data
  period before allowing the monthly loop to test any page change.
- Search Console must recrawl `rice-price-india.html` before its non-critical
  Dataset `license` warning can be confirmed as cleared.
- URL Inspection on 2026-08-08 reported 24 of 28 canonical sitemap pages as
  indexed. `infrastructure.html`, `contact.html`, `sugandha-rice.html` and
  `pesticide-residue-free-raw-rice.html` remain pending Google recrawl after
  the internal-home-link and discovery-signal repair.

## Change history

### 2026-08-08 — Canonical discovery signals repaired

- Audited all 28 canonical sitemap URLs through the Search Console URL
  Inspection API. Twenty-four were submitted and indexed with matching Google
  and user canonicals; four were discovered or unknown to Google, with no
  robots, fetch or conflicting-canonical block reported.
- Replaced every generated and static internal home link to `index.html` with
  the canonical `/` URL, including the noindex thank-you page, so navigation
  no longer creates an unnecessary alternative-homepage signal.
- Added direct homepage context links to the pending Sugandha and
  residue-controlled Raw Rice pages while retaining the existing prominent
  Infrastructure and Quote links.
- Extended the SEO audit and regression suite to reject future internal
  `index.html` home links. The generator, 29-page audit, all 38 tests and
  `git diff --check` passed.
- Published commit `99b69c6`; Pages run `31248127794`, SEO quality run
  `31248128284` and Search Console/IndexNow run `31248128273` succeeded. The
  five checked live pages matched the repository byte-for-byte, and Search
  Console recorded the sitemap submission at `2026-08-08T08:19:41.144Z`.
- Google accepted priority-crawl requests for all four pending canonical URLs,
  and the `Discovered – currently not indexed` validation started on
  2026-08-08. Indexing remains a Google recrawl decision and is not yet
  claimed complete.

### 2026-08-03 — Monthly SEO review held for insufficient evidence

- Google Search Console's complete 2026-07-04 to 2026-07-31 period contained
  23 impressions and 0 clicks across reported query/page rows, while the
  preceding 28-day comparison contained no rows. The prior contact-page change
  remains unevaluable and was kept; the rice-price experiment is not due for
  review until 2026-08-12.
- The exact `urbanfresh.in` Ubersuggest project estimated 0 of 18 India-desktop
  tracked keywords in the top 100 and retained a 100/100 audit across 29
  successful pages. These estimates were kept separate from Search Console.
- Recorded one `No change - insufficient evidence` row in
  `seo/monthly-log.csv`. No page content, URL, navigation, form, sitemap or
  IndexNow file changed, so no discovery resubmission is warranted. Reviewed
  production deployment `72b40eabd1020cc1a8f202541cf95daadea710a1`.
- Rebuilt the 29-page site and passed the SEO audit, all 37 tests and
  `git diff --check`. Continue collecting data until a full comparable period
  and meaningful page/query sample exist.

### 2026-07-29 — Dataset license warning corrected

- Added a versioned, visible UrbanFresh data-use notice to the dated rice-price
  dataset instead of assigning a broad third-party reuse license.
- Added the matching Google-supported `license` CreativeWork object and
  `isAccessibleForFree` flag to the generated `Dataset` JSON-LD.
- Extended the local SEO audit and regression tests to reject future Dataset
  markup that omits a license.
- Rebuilt all 29 pages; the expanded SEO audit, all 37 tests, dry-run sitemap
  and IndexNow checks, and `git diff --check` passed.
- Published commit `4868feb`; Pages run `30443878938`, SEO quality run
  `30443879649` and Search Console/IndexNow run `30443879615` succeeded. The
  live price page matched the repository byte-for-byte and exposed the
  versioned license object and visible terms.

### 2026-07-29 — Domestic quote form connected to Hostinger SMTP

- Added a required business-email field to the domestic quote form and
  connected it to the existing shared Hostinger PHP mailer before the Google
  Sheets backup.
- The mailer sends the complete lead to `sanjit@growonlinetoday.com` and a
  branded confirmation containing the submitted brief to the buyer. WhatsApp
  remains the visible fallback if email delivery fails.
- Added regression coverage for the required email field, email-first delivery,
  Sheets fallback ordering and WhatsApp follow-up details.

### 2026-07-28 — SEO schedules backed up for hardware recovery

- Added a mirrored, secret-free recovery pack that inventories every domestic
  and international SEO schedule and preserves the exact Codex weekly-monitor
  and monthly-optimizer specifications with portable path placeholders.
- Documented clean-machine recovery, including the domestic repo's single
  two-domain macOS LaunchAgent, current-project Codex recreation, and the
  encrypted GitHub secret that must be restored separately after a repository
  transfer.
- Kept the existing Monday 09:00 IST technical checks cloud-hosted while
  excluding private Search Console report data and credentials from the
  repository. Added regression coverage for schedule completeness, path
  portability and credential exclusion.
- Existing active local and Codex schedules were preserved and not duplicated.
- Published the privacy-safe recovery state through commit `05b626c`; SEO
  quality run `30310979149` and Pages run `30310978240` succeeded. A manually
  triggered domestic report artifact from the superseded workflow was
  permanently deleted, GitHub confirmed zero remaining artifacts for that run,
  and the current workflow list contains no cloud report uploader.

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
- Rebuilt all generated pages; the 29-page SEO audit, all 30 unit tests,
  rendered 390/1440 px checks and `git diff --check` passed.
- Published commit `890ada9`. GitHub Pages run `30185516493`, weekly-quality
  run `30185516936` and discovery run `30185516886` succeeded. The live sitemap
  matched the repository byte-for-byte, Search Console recorded the submission
  at `2026-07-26T03:03:12.265Z`, and IndexNow accepted all 28 canonical URLs
  with HTTP 202.

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
