# UrbanFresh project handoff

Read this file first when starting a new chat. Keep it concise and update it with every material change so the next chat can continue safely.

## Current state

- Production site: `https://urbanfresh.in/`
- Repository: `sanjitchak/urbanfresh`, default branch `main`
- Local project: `/Users/Administrator/Downloads/RIce business/urbanfresh`
- SEO audit baseline: 29 HTML pages passing the local audit as of 2026-07-18
- Search Console: service account has Full access; authenticated sitemap submission is working
- Deployment automation: SEO-relevant pushes to `main` wait for the live sitemap, submit it to Search Console, and verify the recorded sitemap
- Monthly SEO automation: active on the first Monday at 10:00 AM IST; uses Search Console as the first-party source and Ubersuggest as secondary research

## Open items

- **2026-07-21 — Product snippets structured-data warning:** Search Console reported that either `offers`, `review`, or `aggregateRating` should be specified. The affected URL has not yet been identified in this chat. Do not invent prices, ratings, or reviews; inspect the affected Product markup and use only truthful business data before changing it.

## Change history

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
