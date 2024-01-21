import os

from invoke import task


@task
def run(c, filename):
    path = os.path.abspath(os.path.dirname(__file__))
    # Windows環境用のコマンド
    if os.name == "nt":
        c.run(f"set PYTHONPATH=%PYTHONPATH%;{path} & python {filename}")
    else:
        c.run(f'export PYTHONPATH="$PYTHONPATH:{path}" && python {filename}')


@task
def test(c, filename):
    path = os.path.abspath(os.path.dirname(__file__))
    if os.name == "nt":
        c.run(f"set PYTHONPATH=%PYTHONPATH%;{path} & python -m unittest {filename}")
    else:
        c.run(
            f'export PYTHONPATH="$PYTHONPATH:{path}" && python -m unittest {filename}'
        )


@task
def test_all(c):
    """Run all tests
    Caution:
        Command `invoke test_all` is not available.
        Use `invoke test-all` instead.
    """
    path = os.path.abspath(os.path.dirname(__file__))
    if os.name == "nt":
        c.run(f"set PYTHONPATH=%PYTHONPATH%;{path} & python -m unittest discover")
    else:
        c.run(f'export PYTHONPATH="$PYTHONPATH:{path}" && python -m unittest')


def translate(text):
    import sys

    path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(path)
    from src.translation.translation import translate_text

    translated_text = translate_text(text, "ja", "en-GB")
    print(translated_text)


@task
def commit(c, commit_type, message):
    japanese_text = translate(message)
    c.run(f"git commit -m '{commit_type}: {message}'")
