import fitz
from pypdf import PdfReader

from src.util import generate_abs_path


# pdf形式で読み取り可能な場合
def read_file(page_number, file_path):
    reader = PdfReader(file_path)
    page = reader.pages[page_number]
    test = page.extract_text()
    print(test)


# pdf形式で読み取り不可能な場合(画像として読み取る)
import re

import fitz
import pytesseract
from PIL import Image


def clean_text(text):
    cleaned_text = re.sub(r"\s+", " ", text)
    return cleaned_text.strip()


pdf_document = fitz.open(generate_abs_path("/pdf/EEindex_論文.pdf"))
image_list = []
for page_number in range(pdf_document.page_count):
    page = pdf_document[page_number]
    image_list.append(page.get_pixmap())

extracted_text = ""
for image in image_list:
    pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
    text = pytesseract.image_to_string(pil_image, lang="eng")
    extracted_text += text + "\n"
cleaned_text = clean_text(extracted_text)

output_path = generate_abs_path("/data/extracted_text.txt")
with open(output_path, mode="w") as f:
    f.write(cleaned_text)
