# UrbanFresh SEO improvement loop

This is a local, no-cost version of the useful idea behind Atom Eve's SEO Improver: measure rankings, make one high-confidence improvement, then check whether it worked.

## What is already implemented

- One primary search intent per page in `keyword-map.csv`
- Unique titles, descriptions, H1 headings and canonical URLs
- Organisation, product, service and page-level structured data
- Search-friendly static HTML with internal links
- `robots.txt` and `sitemap.xml`
- Quote calls-to-action on every commercial page
- A structured WhatsApp quote form so organic traffic can become a qualified enquiry
- Local technical audit at `scripts/seo_audit.py`

## Run the local audit

From the `urbanfresh` folder:

```bash
python3 scripts/seo_audit.py
```

Run it after every website change. It checks titles, descriptions, canonical URLs, H1 count, JSON-LD, image alt text and broken local links.

## Monthly improvement loop

1. Open Google Search Console after the site is live and exported data is available.
2. Compare the last 28 days with the previous 28 days.
3. Record each important query and page in `monthly-log.csv`.
4. Pick only one high-leverage opportunity:
   - a query ranking roughly positions 8–20 with useful impressions;
   - a page with impressions but weak click-through rate;
   - two pages competing for the same query;
   - a page whose clicks or position are declining.
5. Make one focused change: sharpen title, answer the missing buyer question, improve internal links, add genuine proof, or strengthen the quote path.
6. Record the change and wait four weeks before judging it.
7. Keep improvements that increase qualified traffic or quote leads. Revert or rewrite changes that do not.

## Free-first data stack

- Google Search Console: actual queries, clicks, impressions and average position.
- This local audit: technical checks and broken links.
- The quote form/WhatsApp conversation: manually count qualified leads in `monthly-log.csv`.

DataForSEO is optional later. It adds competitor rankings and keyword-gap data, but it is not required to launch or to learn from the first sale. Start with Search Console once UrbanFresh is live and indexed.

## Human review rules

- Never publish invented certifications, capacity, test results, export registrations, customer logos or testimonials.
- Do not create many near-duplicate city or country pages.
- Update one intent page at a time and measure the result.
- Treat quote leads—not traffic alone—as the business outcome.
