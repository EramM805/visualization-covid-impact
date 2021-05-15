# script to parse our data
import pandas as pd

# import dataset
states_data = pd.read_csv('./data/SurpriseData.csv', delimiter=',')

# state codes mapping
us_state_abbrev = {
' Alabama': 'AL', ' Alaska': 'AK', ' Arizona': 'AZ', ' Arkansas': 'AR', ' California': 'CA', ' Colorado': 'CO',
' Connecticut': 'CT', ' Delaware': 'DE', ' Florida': 'FL', ' Georgia': 'GA', ' Hawaii': 'HI', ' Idaho': 'ID',
' Illinois': 'IL', ' Indiana': 'IN', ' Iowa': 'IA', ' Kansas': 'KS', ' Kentucky': 'KY', ' Louisiana': 'LA',
' Maine': 'ME', ' Maryland': 'MD', ' Massachusetts': 'MA', ' Michigan': 'MI', ' Minnesota': 'MN', ' Mississippi': 'MS',
' Missouri': 'MO', ' Montana': 'MT', ' Nebraska': 'NE', ' Nevada': 'NV', ' New Hampshire': 'NH', ' New Jersey': 'NJ',
' New Mexico': 'NM', ' New York': 'NY', ' North Carolina': 'NC', ' North Dakota': 'ND', 'Ohio': 'OH', ' Oklahoma': 'OK',
' Oregon': 'OR', ' Pennsylvania': 'PA', ' Rhode Island': 'RI', ' South Carolina': 'SC', ' South Dakota': 'SD',
' Tennessee': 'TN', ' Texas': 'TX', ' Utah': 'UT', ' Vermont': 'VT', ' Virginia': 'VA', ' Washington': 'WA',
' West Virginia': 'WV', ' Wisconsin': 'WI', ' Wyoming': 'WY'}

us_state_remove_space = {
' Alabama': 'Alabama', ' Alaska': 'Alaska', ' Arizona': 'Arizona', ' Arkansas': 'Arkansas', ' California': 'California', ' Colorado': 'Colorado',
' Connecticut': 'Connecticut', ' Delaware': 'Delaware', ' Florida': 'Florida', ' Georgia': 'Georgia', ' Hawaii': 'Hawaii', ' Idaho': 'Idaho',
' Illinois': 'Illinois', ' Indiana': 'Indiana', ' Iowa': 'Iowa', ' Kansas': 'Kansas', ' Kentucky': 'Kentucky', ' Louisiana': 'Louisiana',
' Maine': 'Maine', ' Maryland': 'Maryland', ' Massachusetts': 'Massachusetts', ' Michigan': 'Michigan', ' Minnesota': 'Minnesota', ' Mississippi': 'Mississippi',
' Missouri': 'Missouri', ' Montana': 'Montana', ' Nebraska': 'Nebraska', ' Nevada': 'Nevada', ' New Hampshire': 'New Hampshire', ' New Jersey': 'New Jersey',
' New Mexico': 'New Mexico', ' New York': 'New York', ' North Carolina': 'North Carolina', ' North Dakota': 'North Dakota', 'Ohio': 'Ohio', ' Oklahoma': 'Oklahoma',
' Oregon': 'Oregon', ' Pennsylvania': 'Pennsylvania', ' Rhode Island': 'Rhode Island', ' South Carolina': 'South Carolina', ' South Dakota': 'South Dakota',
' Tennessee': 'Tennessee', ' Texas': 'Texas', ' Utah': 'Utah', ' Vermont': 'Vermont', ' Virginia': 'Virginia', ' Washington': 'Washington',
' West Virginia': 'West Virginia', ' Wisconsin': 'Wisconsin', ' Wyoming': 'Wyoming'}

#fix column names and removed null rows
states_data.columns = ['Year', 'Month', 'State', 'Value']
#states_data = states_data.iloc[2:]

months = {1: 'January',
   2: 'February',
   3: 'March', 
   4: 'April',
   5: 'May',
   6: 'June',
   7: 'July',
   8: 'August',
   9: 'September',
   10: 'October',
   11: 'November',
   12: 'December'}
# 3rd month from 2007-2021
by_month_data = states_data.loc[(states_data['Year'] > 2005)]
by_month_data['State Code'] = by_month_data['State'].map(us_state_abbrev)
by_month_data = by_month_data.reset_index()
by_month_data['Month'] = by_month_data['Month'].map(months).fillna(by_month_data['Month'])
by_month_data['State'] = by_month_data['State'].map(us_state_remove_space).fillna(by_month_data['State'])
by_month_data.to_csv(path_or_buf = './data/Suprise_Data_2006-202-Final.csv')

print(by_month_data)