import pandas as pd


def read_spreadsheet(file):
    file_extension = file.split('.')[-1].upper()
    if file_extension == 'CSV':
        return pd.read_csv(file)
    elif file_extension == 'XLS' or file_extension == 'XLSX':
        return pd.read_excel(file)
    else:
        raise ValueError("Input file '{0}' does not have readable extension (csv, xls, xlsx)".format(file))
