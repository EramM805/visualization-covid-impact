  
# script to parse our data
import pandas as pd

# import dataset
states_data = pd.read_csv('./data/ststdsadata.csv', delimiter=',')

# state codes mapping
us_state_abbrev = {
'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

#fix column names and removed null rows
states_data.columns = ['FIPS Code', 'State', 'Year', 'Month', 'Civilian Non-Institutional Population', 'Labor Force Total', 'Labor Force Percent of Population', 'Employment Total', 
    'Employment Percent of Population', 'Unemployment Total', 'Unemployment Rate']
states_data = states_data.iloc[9:]

# 1st month from 2007-2021
by_month_data = states_data.loc[(states_data['Year'] > '2007')]
by_month_data['State Code'] = by_month_data['State'].map(us_state_abbrev)
by_month_data = by_month_data.reset_index()

by_month_data.to_csv(path_or_buf = './data/Unemployment-2007-2021.csv')



print(by_month_data)