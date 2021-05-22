import pandas as pd
import numpy as np
import os


###############################
# DONE: 01 - Get Path to CSVs #
###############################

project_path = os.sep.join(os.getcwd().split(os.sep)[1:-1])

data_root_path = os.path.join(os.sep, project_path, 'sprint_01_data_collection')

data_relative_paths = os.listdir(data_root_path)

data_abs_paths = list(
    map(lambda path: os.path.join(data_root_path, path), data_relative_paths))

#######################################################
# DONE: 02 - Load dataset data 01 - Amaz, muni, espec #
#######################################################

path_data_01: str = next(filter(lambda path: 'data_01' in path, data_abs_paths))

data_01_files: list = os.listdir(path_data_01)

am_mun_esp_files: list = list(filter(lambda file: 'Amazonia_Mun_Especie' in file, data_01_files))

am_mun_esp_files_oredered: list = sorted(am_mun_esp_files)

paths_am_mun_esp_files_oredered: list = list(map(lambda file: os.path.join(path_data_01, file), am_mun_esp_files_oredered))

df_data_01_am_mun_esp = pd.DataFrame()

ok = True

for path in paths_am_mun_esp_files_oredered:

	try:

		# file -i <file_name> -> to check encoding

		df_temp = pd.read_table(path, encoding='utf-16le', delimiter='\t')

		########################
		# Creating year column #
		########################

		year = df_temp.columns[2].split('_')[-1] # Falciparum_<year> column

		n_lines = df_temp.shape[0]

		df_temp['Ano'] = np.array([year for _ in range(n_lines)])

		#####################
		# Stratify by State #
		#####################

		def retrieve_state(city: str) -> str:
			return city.split('(')[-1].replace(')', '')

		df_temp['Estado'] = np.array([retrieve_state(city) for city in df_temp['Municipio']])

		######################################
		# Removing State name from City name #
		######################################

		df_temp['Municipio'] = df_temp['Municipio'].apply(lambda city: city.split('(')[0].strip())

		####################
		# Renaming columns #
		####################
		
		new_columns = list(map(lambda column: column.replace('_' + year, ''), df_temp.columns))

		df_temp.columns = new_columns

		#########################
		# Concatenate dataframe #
		#########################

		df_data_01_am_mun_esp = df_data_01_am_mun_esp.append(df_temp)	

	except UnicodeDecodeError as e:

		print(path, e, '\n')

##########
# PRINTS #
##########

# print(df_data_01_am_mun_esp.shape)
# print(df_data_01_am_mun_esp.head())

############
# SAVE CSV #
############

output_path = os.path.join(os.getcwd(), 'output', 'output_01_data_01_AM_mun_especie.csv')

df_data_01_am_mun_esp.to_csv(output_path, sep=';', decimal='.')
