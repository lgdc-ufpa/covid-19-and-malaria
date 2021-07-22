from dask import dataframe as dd
import dask
import os
import pandas as pd
from typing import Union


def load_covid():
    input_path = os.path.join(os.getcwd(), 'output')
    
    input_file = 'output_02_data_02_covid_cities_confirmed_cases.csv'   

    df_covid = pd.read_csv(os.path.join(input_path, input_file), delimiter=';')

    del df_covid['Unnamed: 0']
       
    df_covid['codmun'] = df_covid['codmun'].map(str).map(
        lambda codmun: codmun.split('.')[0])
       
    return df_covid.set_index('codmun')


def load_emergency_aid(blocksize: Union[str, float] = 25e6) -> dask.dataframe.core.DataFrame:
    """Return a dask dataframe

    blocksize: num bytes of each parallel dataframe chunk. egg:'25MB' or 25e6 """

    path_data_09_csvs = os.path.join(os.getcwd(), '..', 'sprint_01_data_collection', 'data_09', '*.csv')

    return dd.read_csv(path_data_09_csvs, sep=";", encoding="ISO-8859-1", blocksize=blocksize, dtype={
        'CPF RESPONSÁVEL': 'str',
        'CÓDIGO MUNICÍPIO IBGE': 'str',
        'NOME MUNICÍPIO': 'str', 
        'UF': 'str', 
        'NIS BENEFICIÁRIO': 'str', 
        'CPF BENEFICIÁRIO': 'str', 
        'NOME BENEFICIÁRIO': 'str', 
        'NIS RESPONSÁVEL': 'str', 
        'CPF RESPONSÁVEL': 'str', 
        'NOME RESPONSÁVEL': 'str', 
        'ENQUADRAMENTO': 'str', 
        'PARCELA': 'str', 
        'OBSERVAÇÃO': 'str', 
        'VALOR BENEFÍCIO': 'str'})
