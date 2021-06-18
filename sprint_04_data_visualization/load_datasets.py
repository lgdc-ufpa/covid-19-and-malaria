import os
import pandas as pd


def load_mean_daily_deaths():
	
	input_path = os.path.join(os.getcwd(), '..', 'sprint_03_data_analysis', 'output')
	input_file = 'output_06_daily_mean_deaths_covid_by_city.csv'

	df_mean = pd.read_csv(os.path.join(input_path, input_file))

	df_mean.set_index('codmun', inplace=True)

	df_mean.index = df_mean.index.map(str).map(lambda x: x.split('.')[0])

	return df_mean


def load_mean_daily_deaths_2020():
	
	input_path = os.path.join(os.getcwd(), '..', 'sprint_03_data_analysis', 'output')
	input_file = 'output_07_daily_mean_deaths_covid_by_city_2020.csv'

	df_mean = pd.read_csv(os.path.join(input_path, input_file))

	df_mean.set_index('codmun', inplace=True)

	df_mean.index = df_mean.index.map(str).map(lambda x: x.split('.')[0])

	return df_mean


def load_covid():

    file_covid = 'output_02_data_02_covid_cities_confirmed_cases.csv'
    path_input_file_covid = os.path.join(os.getcwd(), '..', 
                                         'sprint_03_data_analysis', 'output', 
                                         file_covid)
    df_covid = pd.read_csv(path_input_file_covid, delimiter=';')
    del df_covid['Unnamed: 0']
    
    df_covid['codmun'] = df_covid['codmun'].map(str).map(
    	lambda codmun: codmun.split('.')[0])
    
    return df_covid.set_index('codmun')


def load_IPA():

    input_path = os.path.join(os.getcwd(), '..', 'sprint_01_data_collection', 'data_08')
    input_file = 'odm6_malarianone.csv.csv'

    return pd.read_csv(os.path.join(input_path, input_file))


def load_cfc_2020():

    input_path = os.path.join(os.getcwd(), 'output', 'data')
    input_file = 'CFC_2020.csv'
    
    df_cfc_2020 = pd.read_csv(os.path.join(input_path, input_file)).set_index('codmun')
    
    df_cfc_2020.index = df_cfc_2020.index.map(str).map(
    	lambda codmun: codmun.split('.')[0])
    
    return df_cfc_2020


def load_cfm_2020():

    input_path = os.path.join(os.getcwd(), 'output', 'data')
    input_file = 'CFM_2020.csv'
    
    df_cfm_2020 = pd.read_csv(os.path.join(input_path, input_file)).set_index('codmun')
    
    df_cfm_2020.index = df_cfm_2020.index.map(str).map(
    	lambda codmun: codmun.split('.')[0])
    
    return df_cfm_2020


def load_cfm_all_years():

    input_path = os.path.join(os.getcwd(), 'output', 'data')
    input_file = 'CFM_all_years.csv'
    
    df_cfm_all_years = pd.read_csv(os.path.join(input_path, input_file)).set_index('codmun')
    
    df_cfm_all_years.index = df_cfm_all_years.index.map(str).map(lambda codmun: codmun.split('.')[0])
    
    return df_cfm_all_years
