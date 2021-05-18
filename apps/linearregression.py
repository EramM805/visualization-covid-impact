import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import dash_core_components as dcc
import dash_html_components as html
import pathlib
import pandas as pd
from scipy.stats import pearsonr
import pingouin as pg
import seaborn as sns
from scipy.signal import correlate
import matplotlib.pyplot as plt
from scipy import stats


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

dfg = pd.read_csv(DATA_PATH.joinpath("Unemployment-2005-2021(n).csv"))
covid_data = pd.read_csv(DATA_PATH.joinpath("US_COVID_DATA.csv"))

covid_df = covid_data[(covid_data['Year'] == 2020)]
covid_df_2 = covid_df[['Month', 'positive', 'state']]
covid_df_2 = covid_df_2.rename(columns={"state": "State Code"})
covid_month = covid_df_2.groupby(['State Code', 'Month']).mean()
year_df = dfg[dfg['Year'] == 2020]
year_df = year_df[['Month', 'Unemployment Total', 'State Code']]
year_df = year_df.groupby(['State Code', 'Month']).mean()
final_df = covid_month
final_df['Unemployment Total'] = year_df['Unemployment Total']
final_df = final_df.dropna()
# final_df = final_df['Unemployment Total' <= ]
final_df = final_df[(np.abs(stats.zscore(final_df)) < 3).all(axis=1)]

# X = final_df['positive'].values.reshape(-1, 1)
# Y = final_df['Unemployment Total']
# X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0, shuffle=False)

# model = LinearRegression()
# model.fit(X_train, y_train)

# x_range = np.linspace(X.min(), X.max(), 100)
# y_range = model.predict(x_range.reshape(-1, 1))

# print(model.score(X, Y))

X = final_df['positive']
Y = final_df['Unemployment Total']
corr = pg.corr(x=X, y=Y)

print(corr)

corr_arr = correlate(X, Y)

    #print(covid_month['positive'])
# fig4 = go.Figure(
# data=[
# go.Bar(name='Unemployment', x=year_df['Month'], y =year_df['Unemployment Total']),
# go.Bar(name='Postive Covid Cases', x=covid_month.index, y =covid_month['positive']),
# ])
# # Change the bar mode
# fig4.update_layout(barmode='group', template="plotly_dark", title=loc)
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
line = slope*X+intercept


# fig = go.Figure([
fig = px.scatter(final_df, x="positive", y="Unemployment Total", trendline="ols", template="plotly_dark")

fig2 = go.Figure([
    go.Scatter(
                  x=X,
                  y=Y,
                  mode='markers',
                  marker=go.Marker(color='rgb(255, 127, 14)'),
                  name='Data'
                  ),

    go.Scatter(
                  x=X,
                  y=line,
                  mode='lines',
                  marker=go.Marker(color='rgb(31, 119, 180)'),
                  name='Fit'
                  )
])

    # go.Scatter(x=X_test.squeeze(), y=y_test, name='test', mode='markers'),
    # go.Scatter(
    # x = X,
    # y = corr_arr,
    # mode = 'lines',
    # name = 'Convolution',
    # marker = dict(
    #     color='#53354A'
    # ))
# ])

# g = sns.JointGrid(data=final_df, x='positive', y='Unemployment Total', xlim=(140, 190), ylim=(40, 100), height=5)
# g = g.plot_joint(sns.regplot, color="xkcd:muted blue")
# g = g.plot_marginals(sns.distplot, kde=False, bins=12, color="xkcd:bluey grey")
# g.ax_joint.text(145, 95, 'r = 0.45, p < .001', fontstyle='italic')
# plt.tight_layout()
results = px.get_trendline_results(fig)
results = results.iloc[0]["px_fit_results"].summary()
print(results)


layout = html.Div(children=[
    dcc.Graph(
        id='linear-regression-positive-unemployment',
        figure=fig
    ),
    #  dcc.Graph(
    #     id='linear-regression-positive-unemployment-2',
    #     figure=fig2
    # ),

])

# fig.show()
