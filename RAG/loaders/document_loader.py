
from pathlib import Path

from langchain_core.documents import Document

from RAG.generators.generate_pdf import generate_sample_pdfs
from RAG.generators.generate_text import generate_sample_text
from RAG.generators.generate_csv import generate_sample_csv

from RAG.loaders.pdf_loader import PDFPageLoader
from RAG.loaders.text_loader import TextFileLoader
from RAG.loaders.csv_loader import CSVFileLoader


# ========================================
# DIRECTORIES
# ========================================

RAG_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = RAG_DIR / "data" / "generated"


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
    directory = Path(directory)

    # Find all supported files
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
# GENERATE SAMPLE FILES
# ========================================

generate_sample_pdfs()
generate_sample_text()
generate_sample_csv()


# ========================================
# LOAD GENERATED FILES
# ========================================

documents = load_documents(DATA_DIR)