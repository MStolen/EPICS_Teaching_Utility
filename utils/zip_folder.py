import os
import zipfile


def zip_folder(input_directory, output_file):
    """
Create a zip file archive of a folder
    :param input_directory: Path to target folder
    :param output_file: Path to output file
    """
    # Check for .zip extension
    if ~output_file.endswith('.zip'):
        output_file += '.zip'
    # Create zip output file
    zf = zipfile.ZipFile(output_file, 'w')
    # Progress all files and directories in given directory and add them to the zip archive
    for dirname, subdirs, files in os.walk(input_directory):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
