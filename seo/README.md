# UrbanFresh free local SEO improver

UrbanFresh has a complete local, no-subscription SEO improvement loop inspired by Atom Eve's SEO Improver. It measures first-party Google Search Console performance, compares the latest complete 28 days with the preceding 28 days, identifies a small number of evidence-backed opportunities and checks whether earlier movement was positive or negative.

It does not use DataForSEO, paid AI models, Vercel or Google-result scraping.

## What is implemented

- One primary search intent per page in `keyword-map.csv`
- Unique titles, descriptions, H1 headings and canonical URLs
- Organisation, product, service and page-level structured data
- Search-friendly static HTML with internal links
- `robots.txt` and `sitemap.xml`
- Quote calls-to-action and structured WhatsApp enquiry flow
- Technical audit at `scripts/seo_audit.py`
- Weekly ranking and opportunity report at `scripts/seo_improver.py`
- Free Search Console API access using a read-only service account
- Search Console CSV fallback when credentials are not configured
- Local macOS scheduling through `launchd`
- Stable recommendation IDs for striking distance, weak CTR, cannibalization and decay

## Run it now

From the repository root:

```bash
python3 scripts/seo_improver.py
```

Without Search Console credentials, this still produces a technical baseline and clearly records that ranking data is waiting for setup.

Reports are written to:

```text
reports/seo-improver/YYYY-MM-DD/
├── rankings.csv
└── report.md
```

## Ranking-data options

### Option A — automatic API access

Copy `.env.local.example` to `.env.local`, put the complete Google service-account key JSON into `GSC_CREDENTIALS_JSON`, add the service-account email as a restricted Search Console user, then run:

```bash
python3 scripts/seo_improver.py --verify-only
python3 scripts/seo_improver.py
```

The script uses only Python's standard library and the macOS OpenSSL binary.

### Option B — CSV exports

Export the current and previous Search Console comparison periods and save them as `seo/input/current.csv` and `seo/input/previous.csv`. Then run:

```bash
python3 scripts/seo_improver.py \
  --current-csv seo/input/current.csv \
  --previous-csv seo/input/previous.csv
```

See `seo/input/README.md` for accepted columns.

## Install the free weekly schedule on macOS

```bash
chmod +x scripts/run_weekly_seo.sh scripts/install_local_seo_schedule.sh
scripts/install_local_seo_schedule.sh
```

It runs every Monday at 09:00 local time. Run it immediately with:

```bash
launchctl kickstart -k gui/$UID/com.urbanfresh.seo-improver
```

Logs are written to `seo/scheduler.log` and `seo/scheduler-error.log`; both are gitignored.

## Unattended monthly improvement loop

The Codex desktop automation **UrbanFresh Monthly SEO Loop** runs on the first Monday of every month after the weekly measurement job. It:

1. Fast-forwards a clean local `main` branch from GitHub.
2. Collects the latest free Search Console data and reads the prior report and experiment log.
3. Evaluates the previous experiment, then makes at most one evidence-backed page change. If the sample is too small, it records a no-change month instead.
4. Runs the SEO audit, unit tests and Git diff checks.
5. Updates `seo/monthly-log.csv`, commits the result and pushes `main` to GitHub only when every check passes.

The automation does not invent business facts, create doorway pages or make unrelated design changes. A dirty worktree, unavailable credentials, failed validation or a non-fast-forward repository stops publishing for that run and leaves a report explaining why.

## Decision rules

The report considers:

- **Striking distance:** average position 4–20 with at least five impressions.
- **Weak CTR:** at least ten impressions and CTR below a conservative position-band benchmark.
- **Cannibalization:** the same query receiving impressions through at least two different pages.
- **Decay:** average position worsened by at least two places, or clicks fell by at least 30% from a meaningful prior level.

Only the five highest-scoring opportunities are reported, and the executive summary names one priority. The measurement script itself is read-only; the monthly Codex automation may implement only the single highest-confidence opportunity under the publishing safeguards below.

## Publishing safeguards

- Never publish invented certifications, capacity, test results, export registrations, customer logos or testimonials.
- Never create templated city or country pages without real market-specific evidence.
- Make only one evidence-backed content change at a time.
- Run `python3 scripts/seo_audit.py` before committing any SEO page change.
- Wait for the next comparable Search Console period before deciding whether a change worked.
- Treat qualified quote leads—not traffic alone—as the business outcome, and update `monthly-log.csv` during the monthly review.
