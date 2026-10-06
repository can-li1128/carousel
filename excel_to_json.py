import openpyxl
import json
from datetime import datetime, date

excel_file = "2026spring.xlsx"
json_file = "2026spring.json"

# Open workbook
workbook = openpyxl.load_workbook(excel_file, data_only=True)
sheet = workbook.active

data = []

for row in sheet.iter_rows(min_row=2, values_only=True):
    title, isbn, author, publication_date, mms_id = row

    # Skip completely empty rows
    if not any(row):
        continue

    # Convert publication date to a JSON-friendly value
    if isinstance(publication_date, (datetime, date)):
        publication_date = publication_date.isoformat()
    elif publication_date is not None:
        publication_date = str(publication_date)

    record = {
        "title": str(title) if title is not None else "",
        "isbn": str(isbn) if isbn is not None else "",
        "author": str(author) if author is not None else "",
        "publicationDate": publication_date or "",
        "mmsId": str(mms_id) if mms_id is not None else ""
    }

    data.append(record)

# Save as JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully converted {len(data)} records.")
print(f"JSON file created: {json_file}")