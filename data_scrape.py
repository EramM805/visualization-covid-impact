
# script to parse our data
import pandas as pd

# import dataset
states_data = pd.read_csv('./data/ststdsadata.csv', delimiter=',')

#fix column names and removed null rows
states_data.columns = ['FIPS Code', 'State', 'Year', 'Month', 'Civilian Non-Institutional Population', 'Labor Force Total', 'Labor Force Percent of Population', 'Employment Total', 
    'Employment Percent of Population', 'Unemployment Total', 'Unemployment Rate']
states_data = states_data.iloc[9:]

# 1st month from 2008 - 2021. This can be used for the first reserach question.
by_month_data = states_data.loc[(states_data['Month'] == '1') & (states_data['Year'] > '2007')]
by_month_data = by_month_data.reset_index()

by_month_data.to_csv(path_or_buf = './data/Unemployment-2007-2021.csv')

print(by_month_data)
