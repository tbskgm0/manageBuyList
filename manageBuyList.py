import gspread
from oauth2client.service_account import ServiceAccountCredentials
import key

SCOPES = [key.SPREADSHHET_URL, key.DRIVE_URL]

SERVICE_ACCOUNT_FILE = key.ACCOUNT_FILE
print(f"SERVICE_ACCOUNT_FILE: {SERVICE_ACCOUNT_FILE}")

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)

gs = gspread.authorize(credentials)

SPREADSHEET_KEY = key.SPREADSHEET_KEY
worksheet = gs.open_by_key(SPREADSHEET_KEY).worksheet("シート1")
print(worksheet.acell("C2").value)

