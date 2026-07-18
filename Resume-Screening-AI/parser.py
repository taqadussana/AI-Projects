import pdfplumber
from docx import Document


def extract_pdf(path):
    text = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_docx(path):
    document = Document(path)

    return "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )