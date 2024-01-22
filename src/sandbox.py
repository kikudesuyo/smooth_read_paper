from src.extract.read_pdf import PdfExtractor
from src.translation.translation import translate_text
from src.util import generate_abs_path

# instance = PdfExtractor(0, generate_abs_path("/pdf/特別研究ポスター.pdf"))
# print(instance.extract_text().replace("\n", ""))
# instance.extract_image()

with open(generate_abs_path("/data/japanese_text.txt"), "r") as f:
    text = f.read()

english = translate_text(text, "ja", "en-us")
with open(generate_abs_path("/data/english_text.txt"), "w") as f:
    f.write(english)
