from pathlib import Path


def safe_make_dirs(directory_name):
    Path(directory_name).mkdir(parents=True, exist_ok=True)
