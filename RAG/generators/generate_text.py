
from pathlib import Path


# ========================================
# DIRECTORIES
# ========================================

RAG_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = RAG_DIR / "data" / "generated"


# ========================================
# GENERATE TEXT FILE
# ========================================

def generate_text(filename: str, content: str) -> None:
    # Create the output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Write the text file
    text_path = OUTPUT_DIR / filename
    text_path.write_text(content, encoding="utf-8")

    print(f"Text file generated: {text_path}")


# ========================================
# GENERATE SAMPLE TEXT FILE
# ========================================

def generate_sample_text() -> None:
    content = """Library Notice
Library opens at 8 AM
Library closes at 6 PM
Maintain silence in the library
Return books on time"""

    generate_text("library_notice.txt", content)


# Expected output:
# Text file generated: .../RAG/data/generated/library_notice.txt