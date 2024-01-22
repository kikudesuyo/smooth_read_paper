from src.extract.read_pdf import PdfExtractor
from src.translation.translation import translate_text
from src.util import generate_abs_path

instance = PdfExtractor(0, generate_abs_path("/pdf/特別研究ポスター.pdf"))
print(instance.extract_text().replace("\n", ""))
instance.extract_image()
