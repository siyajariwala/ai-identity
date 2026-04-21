from pathlib import Path

from pypdf import PdfReader

from paths import I765_PDF


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
    return full_text


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        # Don't cut mid-word — extend to nearest space
        if end < len(text) and text[end] != " ":
            end = text.rfind(" ", start, end + 1)
            if end == -1:  # no space found, just cut at chunk_size
                end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks


if __name__ == "__main__":
    pdf = Path(I765_PDF)
    if not pdf.is_file():
        raise SystemExit(f"Missing PDF: {pdf}")
    text = extract_text(str(pdf))
    chunks = chunk_text(text)  # split the text into overlapping chunks

    print(f"Total chunks created: {len(chunks)}")
    print(f"\nExample chunk 1:\n{chunks[0]}")
    print(f"\nExample chunk 2:\n{chunks[1]}")
