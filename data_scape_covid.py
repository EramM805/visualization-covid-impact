import datetime
import pandas as pd

#Month, year, state,positive,probableCases,negative,pending,totalTestResultsSource,totalTestResults,hospitalizedCurrently,hospitalizedCumulative,inIcuCurrently,inIcuCumulative,onVentilatorCurrently,onVentilatorCumulative,recovered,dataQualityGrade,lastUpdateEt,dateModified,checkTimeEt,death,hospitalized,dateChecked,totalTestsViral,positiveTestsViral,negativeTestsViral,positiveCasesViral,deathConfirmed,deathProbable,totalTestEncountersViral,totalTestsPeopleViral,totalTestsAntibody,positiveTestsAntibody,negativeTestsAntibody,totalTestsPeopleAntibody,positiveTestsPeopleAntibody,negativeTestsPeopleAntibody,totalTestsPeopleAntigen,positiveTestsPeopleAntigen,totalTestsAntigen,positiveTestsAntigen,fips,positiveIncrease,negativeIncrease,total,totalTestResultsIncrease,posNeg,deathIncrease,hospitalizedIncrease,hash,commercialScore,negativeRegularScore,negativeScore,positiveScore,score,grade

covid_data_read = pd.read_csv('./data/us_states_covid19_daily.csv', delimiter=',')

covid_data_read['date_updated'] = pd.to_datetime(covid_data_read["date"], format='%Y%m%d')
covid_data_read['Month'] = covid_data_read['date_updated'].dt.strftime("%B")
covid_data_read['Year'] = covid_data_read['date_updated'].dt.strftime("%Y")

covid_data_read = covid_data_read.fillna(0)
covid_data_read.to_csv(path_or_buf = './data/US_COVID_DATA.csv')
# date_time_obj = datetime.datetime.strptime('20210307', '%Y%m%d')
# by_month_data['Month'] = by_month_data['State'].map(us_state_abbrev)
# by_month_data = by_month_data.reset_index()
# by_month_data['Month'] = by_month_data['Month'].map(months).fillna(by_month_data['Month'])

# by_month_data.to_csv(path_or_buf = './data/Unemployment-2005-2021(n).csv')

