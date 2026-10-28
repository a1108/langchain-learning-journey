
from pathlib import Path
from reportlab.pdfgen import canvas

# ========================================
# DIRECTORIES
# ========================================

RAG_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = RAG_DIR / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ========================================
# GENERATE PDF
# ========================================

def generate_pdf(filename: str, pages: list[list[str]]) -> None:
    # Create the PDF
    pdf_path = OUTPUT_DIR / filename
    pdf = canvas.Canvas(str(pdf_path))

    # Write each page
    for page_number, lines in enumerate(pages):
        y_position = 750

        for line in lines:
            # Handle text containing newline characters
            for text_line in line.splitlines():
                pdf.drawString(60, y_position, text_line)
                y_position -= 30

        # Move to the next page
        if page_number < len(pages) - 1:
            pdf.showPage()

    # Save the PDF
    pdf.save()
    print(f"PDF generated: {pdf_path}")