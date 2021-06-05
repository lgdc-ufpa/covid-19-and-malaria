import pandas as pd
import os
from tqdm import tqdm

###############################
# DONE: 01 - Get Path to CSVs #
###############################

project_path = os.sep.join(os.getcwd().split(os.sep)[1:-1])

data_root_path = os.path.join(os.sep, project_path, 'sprint_01_data_collection')

data_relative_paths = os.listdir(data_root_path)

data_abs_paths = list(
    map(lambda path: os.path.join(data_root_path, path), data_relative_paths))

############################################################
# Load dataset data 02 - HIST_PAINEL_COVIDBR_21mai2021.csv #
# Status: DONE
############################################################

path_data_02: str = next(filter(lambda path: 'data_02' in path, data_abs_paths))

data_02_file: list = os.listdir(path_data_02)[0]

abs_path_data_02_file = os.path.join(path_data_02, data_02_file)

df = pd.read_csv(abs_path_data_02_file, delimiter=';')

###############
# Select lines which MUNICIPE column is not none
# Status: DONE
###############

df_cities = df[df['municipio'].notnull()].reset_index(drop=False)
del df_cities['index']

#########
# cast data column into timestamp format
# Status: DONE
#########
df_cities['data'] = pd.to_datetime(df_cities['data'])


"""
df_cities.columns:

Index(['index', 'regiao', 'estado', 'municipio', 'coduf', 'codmun',
       'codRegiaoSaude', 'nomeRegiaoSaude', 'data', 'semanaEpi',
       'populacaoTCU2019', 'casosAcumulado', 'casosNovos', 'obitosAcumulado',
       'obitosNovos', 'Recuperadosnovos', 'emAcompanhamentoNovos',
       'interior/metropolitana'],
      dtype='object')
"""

#################
# Order df_cities by its columns
# Status: TODO

# mainly by municipe, casosNovos, casosAcumulado, and data
#################

df_cities_sorted = df_cities.copy()

df_cities_sorted.sort_values(by=['regiao', 'estado', 'municipio', 'coduf', 'codmun', 'codRegiaoSaude', 'nomeRegiaoSaude', 'data', 'semanaEpi', 'populacaoTCU2019', 'casosAcumulado', 'casosNovos', 'obitosAcumulado', 'obitosNovos', 'Recuperadosnovos', 'emAcompanhamentoNovos', 'interior/metropolitana']).reset_index(drop=False)

#######
# Deleting unused dataframes
# Status DONE
#######

del df
del df_cities

##########
# Creating df with only confirmed cases by city
# - Status: DONE

# 1. Creating list of df with only confirmed cases by city
# 2. concat the list into a df_cities_confirmed_cases

# obs: Using list of df and pd.concat is too far faster than pd.append a df to another one by one
##############

df_list_cities_confirmed_cases = []

for cod_city in tqdm(df_cities_sorted['codmun'].unique()):

    # select only cod_city cells
    df_cod_city = df_cities_sorted[df_cities_sorted['codmun'] == cod_city]
    
    # remove lines where accumulated cases is 0
    df_cod_city_confirmed_cases = df_cod_city[df_cod_city['casosAcumulado'] != 0]    
    
    # append to list of df
    df_list_cities_confirmed_cases.append(df_cod_city_confirmed_cases)        
    
    # save memory
    del df_cod_city
    del df_cod_city_confirmed_cases

df_cities_cofirmed_cases = pd.concat(df_list_cities_confirmed_cases).reset_index(drop=True)

###############################
# Save df_cities_cofirmed_cases
# - Status: DONE
###############################

output_path = os.path.join(os.getcwd(), 'output', 'output_02_data_02_covid_cities_confirmed_cases.csv')

df_cities_cofirmed_cases.to_csv(output_path, sep=';', decimal='.')

##########
# Creating df with only confirmed deaths by city
# - Status: DONE

# 1. Creating list of df with only confirmed deaths by city
# 2. concat the list into a df_cities_confirmed_deaths

# obs: Using list of df and pd.concat is too far faster than pd.append a df to another one by one
##############

df_list_cities_confirmed_deaths = []

for cod_city in tqdm(df_cities_sorted['codmun'].unique()):

    # select only cod_city cells
    df_cod_city = df_cities_sorted[df_cities_sorted['codmun'] == cod_city]
    
    # remove lines where accumulated deaths is 0
    df_cod_city_confirmed_deaths = df_cod_city[df_cod_city['obitosAcumulado'] != 0]    
    
    # append to list of df
    df_list_cities_confirmed_deaths.append(df_cod_city_confirmed_deaths)        
    
    # save memory
    del df_cod_city
    del df_cod_city_confirmed_deaths

df_cities_cofirmed_deaths = pd.concat(df_list_cities_confirmed_deaths).reset_index(drop=True)

###############################
# Save df_cities_cofirmed_cases
# - Status: DONE
###############################

output_path_confirmed_deaths = os.path.join(os.getcwd(), 'output', 'output_03_data_02_covid_cities_confirmed_deaths.csv')

df_cities_cofirmed_deaths.to_csv(output_path_confirmed_deaths, sep=';', decimal='.')
