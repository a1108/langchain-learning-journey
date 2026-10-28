
from pathlib import Path
import csv


# ========================================
# DIRECTORIES
# ========================================

RAG_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = RAG_DIR / "data" / "generated"


# ========================================
# GENERATE CSV
# ========================================

def generate_csv(filename: str, rows: list[dict[str, str]]) -> None:
    # Create the output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    csv_path = OUTPUT_DIR / filename

    if not rows:
        raise ValueError("CSV rows cannot be empty.")

    # Write CSV data
    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV generated: {csv_path}")


# ========================================
# GENERATE SAMPLE CSV
# ========================================

def generate_sample_csv() -> None:
    rows = [
        {"student_id": "S101", "name": "Ravi", "course": "Python", "fee": "5000"},
        {"student_id": "S102", "name": "Priya", "course": "Java", "fee": "6000"},
        {"student_id": "S103", "name": "Rahul", "course": "Data Science", "fee": "12000"},
    ]

    generate_csv("students.csv", rows)


# Expected output:
# CSV generated: .../RAG/data/generated/students.csv

# Use load() when you need all Document objects as a list, such as when passing them to a text splitter.
# Use lazy_load() for large CSV files when processing documents incrementally, one Document object at a time.
# Use lazy_load() when processing and storing documents in batches.