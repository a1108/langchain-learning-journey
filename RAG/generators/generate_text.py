from pathlib import Path

# Define the directory where generated text files will be stored
RAG_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = RAG_DIR / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_text(filename: str, content: str) -> None:
    # Create the text file at the specified output location
    file_path = OUTPUT_DIR / filename
    file_path.write_text(content, encoding="utf-8")

    print(f"Text file generated: {file_path}")


# Generate a sample text file
'''
generate_text(
    "library_notice.txt",
    """Library Notice
Library opens at 8 AM
Library closes at 6 PM
Maintain silence in the library
""",
)
'''

# Expected output:
# Text file generated: .../RAG/data/generated/library_notice.txt
