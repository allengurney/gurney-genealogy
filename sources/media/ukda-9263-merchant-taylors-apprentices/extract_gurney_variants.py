"""Extract all Gurney-variant rows from the UKDA-SN-9263 Merchant Taylors apprentices spreadsheet.

Usage: python extract_gurney_variants.py
Writes gurney-variants-extract.csv alongside the spreadsheet.
"""
import csv
import os
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "merchant_taylors_uk_data_service.xlsx")
OUT = os.path.join(HERE, "gurney-variants-extract.csv")

ALLOWED = {
    "gurney", "gurnay", "gurnaye", "gourney", "gournay",
    "gurnee", "gurnie", "gurny", "gerney", "girney", "gyrney",
    "gurnoe", "gourny", "gourne", "gurne", "gerny", "gerneye",
    "gourneye", "gurnney",
}

# Surname-bearing columns per sheet, by zero-based index relative to the header row.
SURNAME_COLS = {
    "COMB":        [4, 5, 14, 15, 29, 30],
    "Court App":   [2, 4],
    "Redemptions": [4],
    "Patrimony":   [4, 5],
    "Freedoms":    [4, 5, 15, 16, 17, 29, 30, 31, 44, 55, 56, 65, 66, 68, 70, 71, 75],
}


def is_variant(value):
    if value is None:
        return False
    text = str(value).strip().lower()
    if not text:
        return False
    if text in ALLOWED:
        return True
    return text.startswith("de gourn") or text.startswith("de gurn")


def main():
    wb = openpyxl.load_workbook(SRC, read_only=True, data_only=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        for sheet_name, cols in SURNAME_COLS.items():
            ws = wb[sheet_name]
            headers = None
            for index, row in enumerate(ws.iter_rows(values_only=True)):
                if index == 0:
                    headers = row
                    writer.writerow(["Sheet", "RowIdx", *headers])
                    continue
                hit = any(
                    is_variant(row[c]) for c in cols if c < len(row)
                )
                if hit:
                    writer.writerow([sheet_name, index, *row])
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
