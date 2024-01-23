import fitz
import pytesseract
from PIL import Image
from pypdf import PdfReader

from src.util import generate_abs_path


# pdf形式で文字情報が読み取り可能な場合
class PdfExtractor:
    def __init__(self, pdf_path) -> None:
        self.reader = PdfReader(pdf_path)

    def extract_text(self, designated_page_number):
        page = self.reader.pages[designated_page_number]
        text = page.extract_text()
        cleaned_text = self.clean_text(text)
        return cleaned_text

    def extract_image(self, designated_page_number):
        page = self.reader.pages[designated_page_number]
        count = 0
        for image_object in page.images:
            with open(generate_abs_path(f"/pdf/img/image{count}.jpg"), mode="wb") as f:
                f.write(image_object.data)
                count += 1

    def get_page_number(self):
        return len(self.reader.pages)

    def clean_text(self, text):
        return text.replace("\n", "")


# pdf形式で文字情報が読み取り不可能な場合
class PdfExtractorAsImage:
    def __init__(self, pdf_path, language="eng") -> None:
        self.pdf_document = fitz.open(pdf_path)
        self.language = language

    def read_text_as_image(self, page_number):
        page = self.pdf_document[page_number]
        image = page.get_pixmap()
        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
        text = pytesseract.image_to_string(pil_image, lang=self.language)
        cleaned_text = self.clean_text(text)
        return cleaned_text

    def clean_text(self, text):
        return text.replace("\n", "")
