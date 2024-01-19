from pathlib import Path


def generate_abs_path(path):
    """絶対パスを生成

    Arg:
      path (str): artificial_satellite/からの相対パス

    Return:
      str: 引数pathへの絶対パス
    """
    return str(Path(__file__).parents[1]) + path
