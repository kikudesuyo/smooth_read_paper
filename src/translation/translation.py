import deepl

from src.constant.api_key import DEEPL_API_KEY
from src.util import generate_abs_path


def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """Translate text from source_lang to target_lang
    Args:
        text (str): text to translate
        source_lang (str): source language
        target_lang (str): target language
    Returns:
        str: translated text

    Note:
        source_lang and target_lang must be one of the following:
        "BULGARIAN": "bg",
        "CZECH": "cs",
        "DANISH": "da",
        "GERMAN": "de",
        "GREEK": "el",
        "ENGLISH": "en",
        "ENGLISH_BRITISH": "en-GB",
        "ENGLISH_AMERICAN": "en-US",
        "SPANISH": "es",
        "ESTONIAN": "et",
        "FINNISH": "fi",
        "FRENCH": "fr",
        "HUNGARIAN": "hu",
        "INDONESIAN": "id",
        "ITALIAN": "it",
        "JAPANESE": "ja",
        "KOREAN": "ko",
        "LITHUANIAN": "lt",
        "LATVIAN": "lv",
        "NORWEGIAN": "nb",
        "DUTCH": "nl",
        "POLISH": "pl",
        "PORTUGUESE": "pt",
        "PORTUGUESE_BRAZILIAN": "pt-BR",
        "PORTUGUESE_EUROPEAN": "pt-PT",
        "ROMANIAN": "ro",
        "RUSSIAN": "ru",
        "SLOVAK": "sk",
        "SLOVENIAN": "sl",
        "SWEDISH": "sv",
        "TURNISH": "tr",
        "UKRAINIAN": "uk",
        "CHINESE": "zh",


    """
    translator = deepl.Translator(DEEPL_API_KEY)
    result = translator.translate_text(
        text, source_lang=source_lang, target_lang=target_lang
    )
    return result.text


text = "경마에서 우승해서 다행입니다!"
translated_text = translate_text(text, "KO", "ja")
with open(generate_abs_path("/data/translation.txt"), mode="w", encoding="utf-8") as f:
    f.write(translated_text)
