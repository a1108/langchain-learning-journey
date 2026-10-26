from pathlib import Path
from reportlab.pdfgen import canvas

# Define the directory where generated PDFs will be stored
RAG_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = RAG_DIR / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_pdf(filename: str, pages: list[list[str]]) -> None:
    # Create the PDF at the specified output location
    pdf_path = OUTPUT_DIR / filename
    pdf = canvas.Canvas(str(pdf_path))

    # Write the given text on each page
    for page_number, lines in enumerate(pages):
        y_position = 750

        for line in lines:
            pdf.drawString(60, y_position, line)
            y_position -= 30

        # Move to the next page if more content remains
        if page_number < len(pages) - 1:
            pdf.showPage()

    # Save the generated PDF
    pdf.save()
    print(f"PDF generated: {pdf_path}")


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

# Expected output:
# PDF generated: .../RAG/data/generated/library_notice_single.pdf
# PDF generated: .../RAG/data/generated/library_notice_multiple.pdf
#
# library_notice_single.pdf   - 1 page
# library_notice_multiple.pdf - 3 pages