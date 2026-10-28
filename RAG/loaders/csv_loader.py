import csv
from pathlib import Path

from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader



# ========================================
# CUSTOM CSV LOADER
# ========================================

class CSVFileLoader(BaseLoader):

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def lazy_load(self):
        # Read the CSV file
        with self.file_path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as file:

            reader = csv.DictReader(file)

            for row_index, row in enumerate(reader):

                # Convert each CSV row into document content
                content = "\n".join(
                    f"{field}: {value}"
                    for field, value in row.items()
                    if value is not None
                )

                yield Document(
                    page_content=content,
                    metadata={
                        "source": str(self.file_path),
                        "source_type": "csv",
                        "row": row_index,
                        "student_id": row["student_id"],
                        "course": row["course"],
                    },
                )


# Note: Custom BaseLoader implementations allow us to control the content and metadata generated from structured source data.