import os
import pandas as pd
from plots import *
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

######################
# DONE: LOAD DATASET #
######################


project_path = os.sep.join(os.getcwd().split(os.sep)[1:-1])

data_root_path = os.path.join(os.sep, project_path, 'sprint_03_data_analysis', 'output')

file_csv_output_01 = 'output_01_data_01_AM_mun_especie.csv'

path_sprint_03_data_analysis_output_01_csv = os.path.join(data_root_path, file_csv_output_01)
df = pd.read_csv(path_sprint_03_data_analysis_output_01_csv, delimiter=';')

del df['Unnamed: 0']

df = df[df['Estado'] != 'Total']

print(df.info())

"""
RangeIndex: 9101 entries, 0 to 9100
Data columns (total 10 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Unnamed: 0  9101 non-null   int64  
 1   CD          9101 non-null   object 
 2   Municipio   9101 non-null   object 
 3   Falciparum  9101 non-null   float64
 4   Mista       9101 non-null   float64
 5   Vivax       9101 non-null   float64
 6   Malarie     9101 non-null   int64  
 7   Ovale       9101 non-null   int64  
 8   Ano         9101 non-null   int64  
 9   Estado      9101 non-null   object 
dtypes: float64(3), int64(4), object(3)
memory usage: 711.1+ KB
"""
#############################
# TODO: DATA VISUALIZATIONS #
#############################

##############################
# Data analysis exploitation #
##############################

df.describe()

print(df['Vivax'].sum()) # 795600.3940000001

print(df['Falciparum'].sum()) # 402047.081

print(df['Malarie'].sum()) # 3674

int(df['Ovale'].sum()) # 102

"""
Vivax > Falciparum > Malarie > Ovale
"""

####################################
# DONE: Distribution plots         #
# IMPOSSIBLE WITH CATEGORICAL DATA #
####################################

path_output = os.path.join(os.getcwd(), 'output')

distplot(df, 'Falciparum', kde=True).savefig(os.path.join(path_output, 'output_01.png'))

distplot(df, 'Vivax', kde=True).savefig(os.path.join(path_output, 'output_02.png'))

distplot(df, 'Malarie', kde=True).savefig(os.path.join(path_output, 'output_03.png'))

distplot(df, 'Ovale', kde=True).savefig(os.path.join(path_output, 'output_04.png'))

jointplot(df, 'Estado', 'Falciparum').savefig(os.path.join(path_output, 'output_05.png'))

jointplot(df, 'Estado', 'Vivax').savefig(os.path.join(path_output, 'output_06.png'))

jointplot(df, 'Estado', 'Malarie').savefig(os.path.join(path_output, 'output_07.png'))

jointplot(df, 'Estado', 'Ovale').savefig(os.path.join(path_output, 'output_08.png'))

jointplot(df, 'Ano', 'Falciparum').savefig(os.path.join(path_output, 'output_09.png'))

jointplot(df, 'Ano', 'Vivax').savefig(os.path.join(path_output, 'output_10.png'))

jointplot(df, 'Ano', 'Malarie').savefig(os.path.join(path_output, 'output_11.png'))

jointplot(df, 'Ano', 'Ovale').savefig(os.path.join(path_output, 'output_12.png'))

pairplot(df).savefig(os.path.join(path_output, 'output_13.png'))

sns.set(rc={'figure.figsize': (10, 10)})

pairplot(df[['Falciparum', 'Vivax', 'Estado']], hue='Estado').savefig(os.path.join(path_output, 'output_14.png'))

pairplot(df[['Falciparum', 'Vivax', 'Estado', 'Ano']], hue='Estado').savefig(os.path.join(path_output, 'output_15.png'))

pairplot(df[['Falciparum', 'Vivax', 'Estado', 'Ano']], hue='Estado', kind='kde').savefig(os.path.join(path_output, 'output_16.png'))


pairplot(df[['Falciparum', 'Vivax', 'Estado']], hue='Estado', kind='kde').savefig(os.path.join(path_output, 'output_17.png'))

pairplot(df[['Falciparum', 'Vivax', 'Estado']], hue='Estado', kind='reg').savefig(os.path.join(path_output, 'output_18.png'))

pairplot(df[['Falciparum', 'Vivax', 'Estado']], hue='Estado', kind='reg').savefig(os.path.join(path_output, 'output_19.png'))

pairplot(df[['Falciparum', 'Vivax', 'Estado', 'Ano']][df['Ano'] >= 2020], hue='Estado', kind='reg').savefig(os.path.join(path_output, 'output_20.png'))

pairplot(df[['Falciparum', 'Vivax', 'Estado', 'Ano']][df['Ano'] >= 2020], hue='Estado', kind='hex').savefig(os.path.join(path_output, 'output_21.png'))

pairplot(df[['Falciparum', 'Vivax', 'Ano']][df['Ano'] >= 2020], hue='Ano', kind='scatter', diag_kind='kde').savefig(os.path.join(path_output, 'output_22.png'))

pairplot(df[['Falciparum', 'Vivax', 'Ano']][df['Ano'] >= 2020], hue='Ano', kind='scatter', diag_kind='hist').savefig(os.path.join(path_output, 'output_23.png'))

pairplot(df[['Falciparum', 'Vivax', 'Ano']][df['Ano'] >= 2020], hue='Ano', kind='kde', diag_kind='kde').savefig(os.path.join(path_output, 'output_24.png'))

pairplot(df[['Falciparum', 'Vivax', 'Ano']][df['Ano'] >= 2020], hue='Ano', kind='reg', diag_kind='kde').savefig(os.path.join(path_output, 'output_25.png'))

##########################
# DONE: CATEGORICAL PLOT #
##########################

barplot(df, x='Estado', y='Falciparum').figure.savefig(os.path.join(path_output, 'output_26.png'))

barplot(df, x='Estado', y='Vivax').figure.savefig(os.path.join(path_output, 'output_27.png'))

barplot(df, x='Ano', y='Falciparum').figure.savefig(os.path.join(path_output, 'output_28.png'))

barplot(df, x='Ano', y='Vivax').figure.savefig(os.path.join(path_output, 'output_29.png'))

sns.set(rc={'figure.figsize': (30, 10)})

barplot(df[df['Ano'] >= 2010], x='Estado', y='Falciparum', hue='Ano').figure.savefig(os.path.join(path_output, 'output_30.png'))

barplot(df[df['Ano'] >= 2010], x='Estado', y='Vivax', hue='Ano').figure.savefig(os.path.join(path_output, 'output_31.png'))

barplot(df[df['Ano'] >= 2010], x='Ano', y='Falciparum', hue='Estado').figure.savefig(os.path.join(path_output, 'output_32.png'))

barplot(df[df['Ano'] >= 2010], x='Ano', y='Vivax', hue='Estado').figure.savefig(os.path.join(path_output, 'output_33.png'))

sns.set(rc={'figure.figsize': (10, 10)})

countplot(df, x='Estado').set_title('Municípios por estado').figure.savefig(os.path.join(path_output, 'output_34.png'))

boxplot(df, x='Estado', y='Falciparum').set_title('Falciparum por estado').figure.savefig(os.path.join(path_output, 'output_35.png'))

boxplot(df, x='Ano', y='Falciparum').set_title('Falciparum por ano').figure.savefig(os.path.join(path_output, 'output_36.png'))

boxplot(df, x='Estado', y='Vivax').set_title('Vivax por estado').figure.savefig(os.path.join(path_output, 'output_37.png'))

boxplot(df, x='Ano', y='Vivax').set_title('Vivax por ano').figure.savefig(os.path.join(path_output, 'output_38.png'))

sns.set(rc={'figure.figsize': (30, 10)})

boxplot(df, x='Estado', y='Falciparum', hue='Ano').set_title('Falciparum por Estado e ano').figure.savefig(os.path.join(path_output, 'output_39.png'))

boxplot(df, x='Ano', y='Falciparum', hue='Estado').set_title('Falciparum por ano e Estado').figure.savefig(os.path.join(path_output, 'output_40.png'))

boxplot(df, x='Estado', y='Vivax', hue='Ano').set_title('Vivax por Estado e ano').figure.savefig(os.path.join(path_output, 'output_41.png'))

boxplot(df, x='Ano', y='Vivax', hue='Estado').set_title('Vivax por ano e Estado').figure.savefig(os.path.join(path_output, 'output_42.png'))

sns.set(rc={'figure.figsize': (20, 10)})

violinplot(df, x='Estado', y='Falciparum').set_title('Falciparum por estado').figure.savefig(os.path.join(path_output, 'output_43.png'))

violinplot(df, x='Ano', y='Falciparum').set_title('Falciparum por ano').figure.savefig(os.path.join(path_output, 'output_44.png'))

violinplot(df, x='Estado', y='Vivax').set_title('Vivax por estado').figure.savefig(os.path.join(path_output, 'output_45.png'))

violinplot(df, x='Ano', y='Vivax').set_title('Vivax por ano').figure.savefig(os.path.join(path_output, 'output_46.png'))

sns.set(rc={'figure.figsize': (30, 10)})

stripplot(df, x='Estado', y='Falciparum', hue='Ano', dodge=True).set_title('Falciparum por Estado e ano').figure.savefig(os.path.join(path_output, 'output_47.png'))

stripplot(df, x='Ano', y='Falciparum', hue='Estado', dodge=True).set_title('Falciparum por ano e Estado').figure.savefig(os.path.join(path_output, 'output_48.png'))

stripplot(df, x='Estado', y='Vivax', hue='Ano', dodge=True).set_title('Vivax por Estado e ano').figure.savefig(os.path.join(path_output, 'output_49.png'))

stripplot(df, x='Ano', y='Vivax', hue='Estado', dodge=True).set_title('Vivax por ano e Estado').figure.savefig(os.path.join(path_output, 'output_50.png'))

catplot(df, x='Ano', y='Falciparum', col='Estado', kind='bar', aspect=1.7, col_wrap=2).savefig(os.path.join(path_output, 'output_51.png'))

catplot(df, x='Ano', y='Falciparum', col='Estado', kind='box', aspect=1.7, col_wrap=2).savefig(os.path.join(path_output, 'output_52.png'))

catplot(df, x='Ano', y='Falciparum', col='Estado', kind='strip', aspect=1.7, col_wrap=2).savefig(os.path.join(path_output, 'output_53.png'))

catplot(df, x='Ano', y='Vivax', col='Estado', kind='bar', aspect=1.7, col_wrap=2).savefig(os.path.join(path_output, 'output_54.png'))

catplot(df, x='Ano', y='Vivax', col='Estado', kind='box', aspect=1.7, col_wrap=2).savefig(os.path.join(path_output, 'output_55.png'))

catplot(df, x='Ano', y='Vivax', col='Estado', kind='strip', aspect=1.7, col_wrap=2).savefig(os.path.join(path_output, 'output_56.png'))

#########################
# DONE: MATRICIAL PLOTS #
#########################

sns.set(rc={'figure.figsize': (20, 10)})

heatmap(df.pivot_table(values='Falciparum', index='Estado', columns='Ano'), cmap='magma').set_title('Falciparum').figure.savefig(os.path.join(path_output, 'output_57.png'))

heatmap(df.pivot_table(values='Vivax', index='Estado', columns='Ano'), cmap='magma').set_title('Vivax').figure.savefig(os.path.join(path_output, 'output_58.png'))

clustermap(df.pivot_table(values='Falciparum', index='Estado', columns='Ano'), cmap='magma').tsavefig(os.path.join(path_output, 'output_59.png'))

clustermap(df.pivot_table(values='Vivax', index='Estado', columns='Ano'), cmap='magma').savefig(os.path.join(path_output, 'output_60.png'))
