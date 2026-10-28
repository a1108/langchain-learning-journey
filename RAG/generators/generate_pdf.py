
from pathlib import Path
from reportlab.pdfgen import canvas


# ========================================
# DIRECTORIES
# ========================================

RAG_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = RAG_DIR / "data" / "generated"


# ========================================
# GENERATE PDF
# ========================================

def generate_pdf(filename: str, pages: list[list[str]]) -> None:
    # Create the output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Create the PDF
    pdf_path = OUTPUT_DIR / filename
    pdf = canvas.Canvas(str(pdf_path))

    # Write content to each page
    for page_index, lines in enumerate(pages):
        y_position = 750

        for line in lines:
            # Handle text containing newline characters
            for text_line in line.splitlines():
                pdf.drawString(60, y_position, text_line)
                y_position -= 30

        # Move to the next page
        if page_index < len(pages) - 1:
            pdf.showPage()

    # Save the PDF
    pdf.save()
    print(f"PDF generated: {pdf_path}")


# ========================================
# GENERATE SAMPLE PDF FILES
# ========================================

def generate_sample_pdfs() -> None:
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