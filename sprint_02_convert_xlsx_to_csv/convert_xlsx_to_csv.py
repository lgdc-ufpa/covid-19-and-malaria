import os
import pandas as pd

"""
Convert files in sprint_01_data_collection/
"""

def convert_xlsx_to_csv(files: list) -> None:
    """Convert xlsx to csv and remove older xslx files"""

    for file in files:

        df = pd.read_excel(file)

        file_path_without_extension = file.split('.')[0]

        file_path_csv = file_path_without_extension + '.csv'

        df.to_csv(file_path_csv) # convert

        os.remove(file) # remove

project_path = os.sep.join(os.getcwd().split(os.sep)[1:-1])

data_root_path = os.path.join(os.sep, project_path, 'sprint_01_data_collection')

data_relative_paths = os.listdir(data_root_path)

data_abs_paths = list(
    map(lambda path: os.path.join(data_root_path, path), data_relative_paths))

abs_file_paths = []

for path in data_abs_paths:
    for file in os.listdir(path):
        extension = file.split('.')[-1]
        if extension == 'xlsx':         
            abs_file_paths.append(os.path.join(path, file))

convert_xlsx_to_csv(files=abs_file_paths)

