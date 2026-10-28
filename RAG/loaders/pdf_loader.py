from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader


# ========================================
# CUSTOM PDF LOADER
# ========================================

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


# Use load() whenever you need all Document objects as a list.
# Use lazy_load() when processing a large collection incrementally,
# one Document object at a time.