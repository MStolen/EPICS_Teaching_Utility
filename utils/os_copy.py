import platform
import os


def os_copy(source_file, dest_file):
    """
Copy a file or directory using native OS commands
    :param source_file: path to the file to be copied
    :param dest_file: path to the destination of the copied file
    """
    if platform.system() == 'Windows':
        os.system(fr'copy {source_file} {dest_file}')
    else:
        os.system(f'cp -r {source_file} {dest_file}')
