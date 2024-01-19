import requests

from src.constant.api_key import DEEPL_API_KEY


def translate_english_text(text, target_language="JA", deepl_api_key="YOUR_API_KEY"):
    """Translate English text to target language using DeepL API."""
    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    params = {
        "text": text,
        "target_lang": target_language,
        "auth_key": deepl_api_key,
    }
    response = requests.post(url, headers=headers, data=params)
    if response.status_code == 200:
        translated_text = response.json()["translations"][0]["text"]
        return translated_text
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


# 使用例
english_text = "I have a pen. I have an apple. Ugh! Apple pen! I have a pen. I have pineapple. Ugh! Pineapple pen! Apple pen. Pineapple pen. Ugh! Pen pineapple apple pen!"
translated_text = translate_english_text(
    english_text, target_language="JA", deepl_api_key=DEEPL_API_KEY
)

print(f"English Text: {english_text}")
print(f"Translated Text: {translated_text}")
