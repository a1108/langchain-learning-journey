from pathlib import Path

from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader


# ========================================
# CUSTOM TEXT LOADER
# ========================================

class TextFileLoader(BaseLoader):

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def lazy_load(self):
        # Read the text file
        content = self.file_path.read_text(encoding="utf-8")

        # Convert the text file into a Document object
        yield Document(
            page_content=content,
            metadata={
                "source": str(self.file_path),
                "source_type": "text",
            },
        )

# Note: This loader creates one Document object for the entire text file.
