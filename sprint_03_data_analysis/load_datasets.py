import os
import pandas as pd

def load_covid():
	input_path = os.path.join(os.getcwd(), 'output')
	
	input_file = 'output_02_data_02_covid_cities_confirmed_cases.csv'	

	df_covid = pd.read_csv(os.path.join(input_path, input_file), delimiter=';')

	del df_covid['Unnamed: 0']
	   
	df_covid['codmun'] = df_covid['codmun'].map(str).map(
		lambda codmun: codmun.split('.')[0])
	   
	return df_covid.set_index('codmun')