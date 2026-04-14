# importing necessary libraries
from pathlib import Path

from pypdf import PdfReader

from paths import I765_PDF

_pdf = Path(I765_PDF)
if not _pdf.is_file():
    raise SystemExit(f"Missing PDF: {_pdf}")

reader = PdfReader(str(_pdf))

# extracting text from each page of the PDF
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() or ""

print(full_text[:2000])  # print first 2000 characters just to check
print(f"\n\nTotal pages: {len(reader.pages)}")
print(f"Total characters: {len(full_text)}")
