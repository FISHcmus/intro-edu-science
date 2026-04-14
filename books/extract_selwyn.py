"""
Extract Neil Selwyn's "Distrusting Educational Technology" (2014) from PDF to raw text.
Run with: /path/to/.venv/bin/python extract_selwyn.py
"""

import fitz  # PyMuPDF
import sys

PDF_PATH = "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/Distrusting Educational Technology - Selwyn.pdf"
OUT_PATH = "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/selwyn_raw.txt"


def extract_raw(pdf_path: str, out_path: str) -> None:
    doc = fitz.open(pdf_path)
    print(f"Total pages: {doc.page_count}", file=sys.stderr)

    with open(out_path, "w", encoding="utf-8") as f:
        for i in range(doc.page_count):
            page = doc[i]
            text = page.get_text()
            f.write(f"=== PAGE {i + 1} ===\n")
            f.write(text)
            f.write("\n")

    print(f"Raw text written to: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    extract_raw(PDF_PATH, OUT_PATH)
