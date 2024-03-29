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


def translate_into_japanese(japanese_text):
    import sys

    path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(path)
    from src.translation.translation import translate_into_english

    english_text = translate_into_english(japanese_text)
    return english_text


@task
def aa(c):
    """Add all files"""
    c.run("git add -A")


@task
def cfe(c, japanese_message):
    """Commit with feat:
    Args:
        japanese_message (str): to commit in Japanese
    Caution:
        japanese_message must be enclosed in double quotes.
    """
    english_text = translate_into_japanese(japanese_message)
    c.run(f'git commit -m "feat: {english_text}"')
    c.run("git push")


@task
def cfi(c, japanese_message):
    """Commit with fix:
    Args:
        japanese_message (str): to commit in Japanese
    Caution:
        japanese_message must be enclosed in double quotes.
    """
    english_text = translate_into_japanese(japanese_message)
    c.run(f'git commit -m "fix: {english_text}"')
    c.run("git push")


@task
def cr(c, japanese_message):
    """Commit with refactor:
    Args:
        japanese_message (str): to commit in Japanese
    Caution:
        japanese_message must be enclosed in double quotes.
    """
    english_text = translate_into_japanese(japanese_message)
    c.run(f'git commit -m "refactor: {english_text}"')
    c.run("git push")
