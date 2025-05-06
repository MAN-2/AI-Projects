import pdfminer.high_level

def extract_text_from_pdf(pdf_path):
    """Extracts text from a resume PDF."""
    with open(pdf_path, "rb") as file:
        return pdfminer.high_level.extract_text(file)
