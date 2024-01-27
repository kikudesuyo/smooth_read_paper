#Repository for smooth reading of English papers

## Precautions for use

Note: The DEEPL API must be obtained for translation.

Please refer to the following for how to obtain it.

https://auto-worker.com/blog/?p=5030

The obtained API key should be listed in src/constant/api_key.py.

The constant name is DEEPL_API_KEY.
(Example):

```
DEEPL_API_KEY = your_api_key
```

## Enabling virtual environments.

```
python -m venv .venv
```

```
#Unix
source .venv/bin/activate
#Windows
source .venv/Scripts/activate
```

## Install libraries.

```
pip install -r requirements.txt
```

## How to run

Put the PDF file you want to translate in the pdf directory

If you pass the file path to the function pdf_edition/extract_pdf.py,

it will translate the file into English and output it.

Use the following command to use invoke, After completing the above operations.

```
inv run filename
```

Note: that non-English print statements are garbled in Windows environment.

PS: This README.md has been translated into English using a translation function I created. (LOL)
