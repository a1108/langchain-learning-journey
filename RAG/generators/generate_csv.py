
import csv
from pathlib import Path

# Define the directory where generated CSV files will be stored
RAG_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = RAG_DIR / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_csv(filename: str, rows: list[dict[str, str]]) -> None:
    # Create the CSV file at the specified output location
    csv_path = OUTPUT_DIR / filename

    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV generated: {csv_path}")

'''

# Generate a sample CSV file
generate_csv(
    "students.csv",
    [
        {"student_id": "S101", "name": "Ravi", "course": "Python", "fee": "5000"},
        {"student_id": "S102", "name": "Priya", "course": "Java", "fee": "6000"},
        {"student_id": "S103", "name": "Rahul", "course": "Data Science", "fee": "12000"},
    ],
)
'''

# Expected output:
# CSV generated: .../RAG/data/generated/students.csv

# Use load() when you need all Document objects as a list, such as when passing them to a text splitter.
# Use lazy_load() for large CSV files when processing documents incrementally, one Document object at a time.
# Use lazy_load() when processing and storing documents in batches.