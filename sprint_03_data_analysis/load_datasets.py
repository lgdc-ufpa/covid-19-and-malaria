import os
import pandas as pd
import numpy as np
import pdb
from tqdm import tqdm
from typing import Callable


def load_covid():
    input_path = os.path.join(os.getcwd(), 'output')
    
    input_file = 'output_02_data_02_covid_cities_confirmed_cases.csv'   

    df_covid = pd.read_csv(os.path.join(input_path, input_file), delimiter=';')

    del df_covid['Unnamed: 0']
       
    df_covid['codmun'] = df_covid['codmun'].map(str).map(
        lambda codmun: codmun.split('.')[0])
       
    return df_covid.set_index('codmun')


def load_emergency_aid_and_process_it(chunksize: int = 1):

    list_process: list = []

    di_results: dict = {}

    df_results = pd.DataFrame([])
    
    def get_month(chunk: pd.core.frame.DataFrame = None) -> str:
        return str(chunk.iloc[0, 0])

    def get_framing(chunk: pd.core.frame.DataFrame = None) -> str:
        return str(chunk.iloc[0, 10])
    
    def process_01_number_framing_per_month(chunk, di_results: dict) -> None:        

        month: str = get_month(chunk)

        framing: str = get_framing(chunk)

        if month in di_results.keys():

            if framing in di_results[month].keys():

                di_results[month][framing] += 1

            else:

                di_results[month][framing] = 1

        else:

            di_results[month] = {}

            di_results[month][framing] = 1          

        return
    
    def get_function_name(_function: Callable) -> str:
            return _function.__name__

    def save_results(df_to_save: pd.core.frame.DataFrame, name: str, path: str):

        abs_path: str = os.path.join(path, name)

        df_to_save.to_csv(abs_path, function_name)

        return

    list_process.append(process_01_number_framing_per_month)    

    input_path = os.path.join(os.getcwd(), '..', 'sprint_01_data_collection', 'data_09')

    input_files = [file for file in os.listdir(input_path) if 'Auxilio' in file and '.csv' in file]

    for process in list_process:

        function_name = get_function_name(process)

        for file in input_files:            

            path_file = os.path.join(input_path, file)

            for chunk in tqdm(pd.read_csv(path_file, sep=';', chunksize=chunksize)):

                # print(chunk)      
                
                try:
                    has_UF = chunk[['UF']].iloc[0, 0].__class__ == str

                except TypeError as e:

                    print('has_UF went wrong')                    

                    pdb.set_trace()

                    raise e

                if has_UF:

                    process(chunk, di_results)

                    df_results = pd.DataFrame(di_results)       

        df_results.head()

        save_results(df_results, function_name)

        del di_results

        del df_results

# load_emergency_aid_and_process_it()
