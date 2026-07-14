# Free Google Search Console setup

The local SEO improver uses the Google Search Console API, which is free and read-only with this configuration.

## 1. Confirm the live property

1. Add `urbanfresh.in` as a Domain property in Google Search Console if it is not already present.
2. Verify ownership with the DNS TXT record provided by Google.
3. Submit `https://urbanfresh.in/sitemap.xml`.
4. Inspect the homepage and commercial landing pages and request indexing.

## 2. Create a read-only service account

In any Google Cloud project:

1. Enable **Google Search Console API**.
2. Open **IAM & Admin → Service Accounts**.
3. Create a service account named `seo-improver`. It needs no Google Cloud project role.
4. Open its **Keys** tab, add a JSON key and download it outside this repository.

In Search Console, open the `urbanfresh.in` property:

1. Go to **Settings → Users and permissions**.
2. Click **Add user**.
3. Paste the service account's `client_email` from the JSON file.
4. Choose **Restricted** permission.

## 3. Store the key locally

```bash
cp .env.local.example .env.local
```

Replace the example value with the complete service-account JSON on one line:

```dotenv
GSC_CREDENTIALS_JSON='{"type":"service_account", ... }'
```

`.env.local` is gitignored. Never commit or paste the real key into an issue, pull request or report. Delete the downloaded key file after the local environment value is working and separately store a secure backup only if needed.

## 4. Verify access

```bash
python3 scripts/seo_improver.py --verify-only
```

Success prints:

```text
Verified read-only Search Console access to sc-domain:urbanfresh.in
```

If the property is not listed, recheck the service-account email in Search Console and wait a minute for permissions to propagate.

## 5. Run the first report

```bash
python3 scripts/seo_improver.py
```

The script avoids incomplete recent data by ending each reporting window three days before the run date. The first report is a baseline; movement and decay become meaningful after later comparable periods exist.

## No-credential alternative

Use Search Console's Export button and follow `seo/input/README.md`. This stays completely local and does not require a service-account key, but it must be repeated manually for each reporting period.
