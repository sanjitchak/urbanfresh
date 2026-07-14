const LEADS_SHEET_NAME = 'Leads';
const HEADERS = [
  'Received at',
  'Name or company',
  'Phone or WhatsApp',
  'Delivery city or country',
  'Buyer type',
  'Rice variety',
  'Processing style',
  'Approximate quantity',
  'Packaging',
  'Purchase timeline',
  'Other requirements',
  'Source page',
  'Lead ID'
];

function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(10000);
    const data = e && e.parameter ? e.parameter : {};

    if (clean_(data.website)) {
      return response_({ ok: true });
    }

    const required = ['name', 'phone', 'location', 'quantity'];
    const missing = required.filter(function (key) { return !clean_(data[key]); });
    if (missing.length) {
      return response_({ ok: false, error: 'Missing required fields.' });
    }

    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    if (!spreadsheet) throw new Error('This script must be attached to a Google Sheet.');

    let sheet = spreadsheet.getSheetByName(LEADS_SHEET_NAME);
    if (!sheet) sheet = spreadsheet.insertSheet(LEADS_SHEET_NAME);
    ensureHeaders_(sheet);

    const leadId = clean_(data.lead_id) || Utilities.getUuid();
    if (leadExists_(sheet, leadId)) return response_({ ok: true, duplicate: true, leadId: leadId });

    sheet.appendRow([
      new Date(),
      safeCell_(data.name),
      safeCell_(data.phone),
      safeCell_(data.location),
      safeCell_(data.buyer_type),
      safeCell_(data.variety),
      safeCell_(data.processing),
      safeCell_(data.quantity),
      safeCell_(data.packaging),
      safeCell_(data.timeline),
      safeCell_(data.message),
      safeCell_(data.source_page),
      safeCell_(leadId)
    ]);

    return response_({ ok: true, leadId: leadId });
  } catch (error) {
    return response_({ ok: false, error: String(error && error.message ? error.message : error) });
  } finally {
    try { lock.releaseLock(); } catch (ignore) {}
  }
}

function ensureHeaders_(sheet) {
  const range = sheet.getRange(1, 1, 1, HEADERS.length);
  const current = range.getValues()[0];
  if (current.join('').trim()) return;
  range.setValues([HEADERS]);
  range.setFontWeight('bold');
  range.setBackground('#1f4b3a');
  range.setFontColor('#f8f4e9');
  sheet.setFrozenRows(1);
  sheet.autoResizeColumns(1, HEADERS.length);
}

function leadExists_(sheet, leadId) {
  if (sheet.getLastRow() < 2) return false;
  const values = sheet.getRange(2, HEADERS.length, sheet.getLastRow() - 1, 1).getDisplayValues();
  return values.some(function (row) { return row[0] === leadId; });
}

function clean_(value) {
  return String(value == null ? '' : value).trim().slice(0, 2000);
}

function safeCell_(value) {
  const cleaned = clean_(value);
  return /^[=+\-@]/.test(cleaned) ? "'" + cleaned : cleaned;
}

function response_(payload) {
  return ContentService
    .createTextOutput(JSON.stringify(payload))
    .setMimeType(ContentService.MimeType.JSON);
}
