
from pathlib import Path

from langchain_core.documents import Document

from RAG.generators.generate_pdf import generate_pdf
from RAG.generators.generate_text import generate_text
from RAG.generators.generate_csv import generate_csv

from RAG.loaders.pdf_loader import PDFPageLoader
from RAG.loaders.text_loader import TextFileLoader
from RAG.loaders.csv_loader import CSVFileLoader


# ========================================
# DIRECTORIES
# ========================================

RAG_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = RAG_DIR / "data" / "generated"


# ========================================
# GENERATE SAMPLE FILES
# ========================================

# Generate single-page PDF
generate_pdf(
    "library_notice_single.pdf",
    [[
        "Library Notice",
        "Library opens at 8 AM",
        "Library closes at 6 PM",
    ]],
)

# Generate multiple-page PDF
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

# Generate text file
generate_text(
    "library_notice.txt",
    """Library Notice
Library opens at 8 AM
Library closes at 6 PM
Maintain silence in the library
Return books on time""",
)

# Generate CSV file
generate_csv(
    "students.csv",
    [
        {
            "student_id": "S101",
            "name": "Ravi",
            "course": "Python",
            "fee": "5000",
        },
        {
            "student_id": "S102",
            "name": "Priya",
            "course": "Java",
            "fee": "6000",
        },
        {
            "student_id": "S103",
            "name": "Rahul",
            "course": "Data Science",
            "fee": "12000",
        },
    ],
)


# ========================================
# GENERIC DOCUMENT LOADER
# ========================================

def get_loader(file_path):
    # Identify the file type
    file_path = Path(file_path)

    if file_path.suffix.lower() == ".pdf":
        return PDFPageLoader(file_path)

    elif file_path.suffix.lower() == ".txt":
        return TextFileLoader(file_path)

    elif file_path.suffix.lower() == ".csv":
        return CSVFileLoader(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {file_path.suffix}"
        )


# ========================================
# LOAD ALL DOCUMENTS
# ========================================

def load_documents(directory) -> list[Document]:
    # Find all supported files in the directory
    directory = Path(directory)

    file_paths = sorted(
        file_path
        for file_path in directory.iterdir()
        if file_path.is_file()
        and file_path.suffix.lower() in [".pdf", ".txt", ".csv"]
    )

    documents = []

    # ========================================
    # PDF DOCUMENT
    # ========================================

    pdf_files = [
        file_path for file_path in file_paths
        if file_path.suffix.lower() == ".pdf"
    ]

    if pdf_files:
        print("\n# ========================================")
        print("# PDF DOCUMENT")
        print("# ========================================")

    for file_path in pdf_files:
        print(f"\nPDF: {file_path.name}")

        loader = get_loader(file_path)
        file_documents = loader.load()

        for document in file_documents:
            page_number = document.metadata["page"] + 1

            print(f"\nPAGE: {page_number}")
            print(
                "STATUS:",
                "TEXT FOUND" if document.page_content.strip()
                else "NO TEXT FOUND",
            )
            print("CONTENT:")
            print(document.page_content)
            print("\nMETADATA:", document.metadata)

        print(f"\nTOTAL PAGES PROCESSED: {len(file_documents)}")
        documents.extend(file_documents)

    # ========================================
    # TEXT DOCUMENT
    # ========================================

    text_files = [
        file_path for file_path in file_paths
        if file_path.suffix.lower() == ".txt"
    ]

    if text_files:
        print("\n# ========================================")
        print("# TEXT DOCUMENT")
        print("# ========================================")

    for file_path in text_files:
        print(f"\nTEXT: {file_path.name}")

        loader = get_loader(file_path)
        file_documents = loader.load()

        for document in file_documents:
            print("\nCONTENT:")
            print(document.page_content)
            print("\nMETADATA:", document.metadata)

        print(f"\nTOTAL DOCUMENTS: {len(file_documents)}")
        documents.extend(file_documents)

    # ========================================
    # CSV DOCUMENT
    # ========================================

    csv_files = [
        file_path for file_path in file_paths
        if file_path.suffix.lower() == ".csv"
    ]

    if csv_files:
        print("\n# ========================================")
        print("# CSV DOCUMENT")
        print("# ========================================")

    for file_path in csv_files:
        print(f"\nCSV: {file_path.name}")

        loader = get_loader(file_path)
        file_documents = loader.load()

        for document in file_documents:
            print(f"\nROW: {document.metadata['row']}")
            print(document.page_content)
            print("\nMETADATA:", document.metadata)

        print(f"\nTOTAL ROWS PROCESSED: {len(file_documents)}")
        documents.extend(file_documents)

    # ========================================
    # FINAL SUMMARY
    # ========================================

    print("\n# ========================================")
    print("# FINAL SUMMARY")
    print("# ========================================")
    print("TOTAL DOCUMENTS:", len(documents))
    print("========================================")

    return documents


# ========================================
# LOAD GENERATED FILES
# ========================================

documents = load_documents(DATA_DIR)