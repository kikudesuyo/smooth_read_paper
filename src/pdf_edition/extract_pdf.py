from reportlab.pdfgen import canvas

from src.pdf_edition.read_pdf import PdfExtractor
from src.translation.translation import translate_text
from src.util import generate_abs_path


def output_english_pdf(pdf_path, output_path_dir):
    """Translate a pdf-format file into English and output it as a text file.
    Only available when the text information is recognized.

    Args:
        pdf_path (str): path to pdf-format file
        output_path_dir (str): path to output directory
    """
    pdf_data = PdfExtractor(pdf_path)
    page_length = pdf_data.get_page_number()
    for i in range(page_length):
        text = pdf_data.extract_text(i)
        japanese_text = translate_text(text, "en", "ja")
        with open(f"{output_path_dir}/text{i}.txt", mode="w", encoding="utf-8") as f:
            f.write(japanese_text)


# TODO: 未完成 pdfに出力する必要がある
def text_to_pdf(text_file, pdf_file):
    with open(text_file, mode="r") as f:
        text = f.read()
    print(text)
    pdf_file = canvas.Canvas(pdf_file)
    pdf_file.setFont("Helvetica", 12)
    pdf_file.drawString(72, 800, text)
    pdf_file.save()


# text_to_pdf(generate_abs_path("/data/text/text0.txt"), generate_abs_path("/data/a.pdf"))


output_english_pdf(
    generate_abs_path("/pdf/EEindex.pdf"), generate_abs_path("/data/text")
)
