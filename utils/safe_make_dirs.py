from pathlib import Path


def safe_make_dirs(directory_name):
    """
Create a directory (and parent directories as needed) safely
    :param directory_name: Path to the directory to be created
    """
    Path(directory_name).mkdir(parents=True, exist_ok=True)
