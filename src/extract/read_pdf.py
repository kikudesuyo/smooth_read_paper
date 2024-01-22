import fitz
import pytesseract
from PIL import Image
from pypdf import PdfReader

from src.util import generate_abs_path


# pdf形式で読み取り可能な場合
class PdfExtractor:
    def __init__(self, page_number, pdf_path) -> None:
        reader = PdfReader(pdf_path)
        self.page = reader.pages[page_number]

    def extract_text(self):
        text = self.page.extract_text()
        return text

    def extract_image(self):
        count = 0
        print(self.page.images)
        for image_object in self.page.images:
            with open(generate_abs_path(f"/pdf/img/image{count}.jpg"), mode="wb") as f:
                f.write(image_object.data)
                count += 1


def clean_text(text):
    return text.replace("\n", "")


def read_text_as_image(page_number, file_path):
    pdf_document = fitz.open(file_path)
    page = pdf_document[page_number]
    image = page.get_pixmap()
    pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
    text = pytesseract.image_to_string(pil_image, lang="eng")
    cleaned_text = clean_text(text)
    return cleaned_text
