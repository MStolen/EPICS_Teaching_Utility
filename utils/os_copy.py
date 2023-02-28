import platform
import os


def os_copy(source_file, dest_file):
    if platform.system() == 'Windows':
        os.system(fr'copy {source_file} {dest_file}')
    else:
        os.system(f'cp -r {source_file} {dest_file}')
