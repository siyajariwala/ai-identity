import chromadb

from chunk import chunk_text, extract_text
from paths import CHROMA_DIR, I765_PDF

# Create a ChromaDB client that saves data locally
client = chromadb.PersistentClient(path=str(CHROMA_DIR))

# Fresh ingest each run (avoids duplicate-ID errors if you re-run this script)
try:
    client.delete_collection("immigration_docs")
except Exception:
    pass
collection = client.get_or_create_collection(name="immigration_docs")

# Extract and chunk the PDF
pdf_path = str(I765_PDF)
text = extract_text(pdf_path)
chunks = chunk_text(text)

# Store each chunk in ChromaDB
# Each chunk needs a unique ID
for i, chunk in enumerate(chunks):
    collection.add(
        documents=[chunk],
        ids=[f"i765-chunk-{i}"],
    )

print(f"Stored {len(chunks)} chunks in ChromaDB!")
print("Testing a search...")

# Test it — search for something
results = collection.query(
    query_texts=["how to apply for work authorization"],
    n_results=2,
)

print(f"\nTop result:\n{results['documents'][0][0]}")
