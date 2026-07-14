# UrbanFresh quote leads

This bound Google Apps Script stores website quote requests in a tab named `Leads`.

1. Create a Google Sheet named `UrbanFresh Quote Leads`.
2. Open **Extensions > Apps Script** from that sheet.
3. Replace the editor content with `Code.gs` and save.
4. Deploy as a web app. Run it as the sheet owner and allow access to anyone.
5. Paste the deployment URL into `GOOGLE_SHEETS_ENDPOINT` in `assets/js/site.js`.

The script creates the header row on the first submission, rejects incomplete requests, ignores the honeypot field, prevents duplicate lead IDs and protects cells from spreadsheet formulas.
