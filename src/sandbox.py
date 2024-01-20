from src.util import generate_abs_path

text = "今夜は月が綺麗ですね。"
with open(generate_abs_path("/data/a.txt"), mode="w", encoding="utf-8") as f:
    f.write(text)
