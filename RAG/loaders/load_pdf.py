from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader

# Generate the sample PDFs first
from RAG.generators.generate_pdf import generate_pdf


RAG_DIR = Path(__file__).resolve().parents[1]
PDF_DIR = RAG_DIR / "data" / "generated"

# Generate a single-page PDF
generate_pdf(
    "library_notice_single.pdf",
    [[
        "Library Notice",
        "Library opens at 8 AM",
        "Library closes at 6 PM",
    ]],
)

# Generate a multiple-page PDF
generate_pdf(
    "library_notice_multiple.pdf",
    [
        [
            "Page 1: Library Notice",
            "Library opens at 8 AM",
            "Library closes at 6 PM",
        ],
        [
            "Page 2: Library Rules",
            "Maintain silence in the library",
            "Return books on time",
        ],
        [
            "Page 3: Contact Information",
            "Email: library@example.com",
            "Phone: 1234567890",
        ],
    ],
)


class PDFPageLoader(BaseLoader):

    def __init__(self, pdf_path):
        self.pdf_path = Path(pdf_path)

    def lazy_load(self):
        # Read the PDF and return one Document per page
        reader = PdfReader(str(self.pdf_path))
        total_pages = len(reader.pages)

        for page_index, page in enumerate(reader.pages):
            yield Document(
                page_content=page.extract_text() or "",
                metadata={
                    "source": str(self.pdf_path),
                    "source_type": "pdf",
                    "page": page_index,
                    "total_pages": total_pages,
                },
            )


# Read the generated PDFs
pdf_files = [
    PDF_DIR / "library_notice_single.pdf",
    PDF_DIR / "library_notice_multiple.pdf",
]

for pdf_path in pdf_files:
    loader = PDFPageLoader(pdf_path)
    count = 0

    print(f"\nPDF: {pdf_path.name}")

    for document in loader.lazy_load():
        count += 1
        text = " ".join(document.page_content.split())

        print("PAGE:", document.metadata["page"] + 1)
        print("STATUS:", "TEXT FOUND" if text else "NO EXTRACTABLE TEXT")
        # Print the extracted text
        print("CONTENT:")
        print(document.page_content)

        # Print document metadata
        print("METADATA:", document.metadata)

    print("TOTAL PAGES PROCESSED:", count)

# Expected output:
# library_notice_single.pdf  - 1 page processed
# library_notice_multiple.pdf - 3 pages processed
# Total: 4 pages processed