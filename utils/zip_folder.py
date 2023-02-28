import os
import zipfile


def zip_folder(input_directory, output_file):
    zf = zipfile.ZipFile(output_file, 'w')
    for dirname, subdirs, files in os.walk(input_directory):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
