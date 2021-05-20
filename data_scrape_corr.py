import datetime
import pandas as pd

#Month, positive,probableCases,negative,pending,totalTestResultsSource,totalTestResults,hospitalizedCurrently,hospitalizedCumulative,inIcuCurrently,inIcuCumulative,onVentilatorCurrently,onVentilatorCumulative,recovered,dataQualityGrade,lastUpdateEt,dateModified,checkTimeEt,death,hospitalized,dateChecked,totalTestsViral,positiveTestsViral,negativeTestsViral,positiveCasesViral,deathConfirmed,deathProbable,totalTestEncountersViral,totalTestsPeopleViral,totalTestsAntibody,positiveTestsAntibody,negativeTestsAntibody,totalTestsPeopleAntibody,positiveTestsPeopleAntibody,negativeTestsPeopleAntibody,totalTestsPeopleAntigen,positiveTestsPeopleAntigen,totalTestsAntigen,positiveTestsAntigen,fips,positiveIncrease,negativeIncrease,total,totalTestResultsIncrease,posNeg,deathIncrease,hospitalizedIncrease,hash,commercialScore,negativeRegularScore,negativeScore,positiveScore,score,grade

covid_data_read = pd.read_csv('./data/covid_data_us.csv', delimiter=',')

covid_data_read['date_updated'] = pd.to_datetime(covid_data_read["date"], format='%Y-%m-%d')
covid_data_read['Month'] = covid_data_read['date_updated'].dt.strftime("%B")
covid_data_read['Year'] = covid_data_read['date_updated'].dt.strftime("%Y")

covid_data_read = covid_data_read.fillna(0)
covid_data_read = covid_data_read[covid_data_read['Year'] == '2020']
covid_data_read = covid_data_read.groupby(['Month', 'Year']).mean()

unemployment_data = pd.read_csv('./data/Unemployement-2005-2021-US.csv', delimiter=',')
unemployment_data['date_updated'] = pd.to_datetime(unemployment_data["DATE"], format='%Y-%m-%d')
unemployment_data['Month'] = unemployment_data['date_updated'].dt.strftime("%B")
unemployment_data['Year'] = unemployment_data['date_updated'].dt.strftime("%Y")

unemployment_data = unemployment_data[unemployment_data['Year'] == '2020']

gdp_data = pd.read_csv('./data/gdp_per_month.csv', delimiter=',')
gdp_data['date_updated'] = pd.to_datetime(gdp_data["DATE"], format='%Y-%m-%d')
gdp_data['Month'] = gdp_data['date_updated'].dt.strftime("%B")
gdp_data['Year'] = gdp_data['date_updated'].dt.strftime("%Y")
final_df = pd.merge(unemployment_data, covid_data_read, on="Month")
final_df = pd.merge(gdp_data, final_df, on="Month")

final_df = final_df.drop(columns=['DATE_x', 'date_updated_x', 'DATE_y', 'Year_x','Month', 'date_updated_y', 'Year_y', 'states', 'totalTestResults', 'totalTestResultsIncrease', 'deathIncrease', 'inIcuCurrently', 'hospitalizedIncrease', 'hospitalizedCurrently', 'negativeIncrease', 'onVentilatorCurrently', 'positiveIncrease'])
final_df = final_df.rename(columns={'USALORSGPNOSTSAM': 'GDP', 'UNRATE': 'Uemployment Rate'})
final_df.to_csv(path_or_buf = './data/corr_data.csv')
# print(final_df)

