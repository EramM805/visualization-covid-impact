import plotly.graph_objs as go
import pandas as pd
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
dfg = pd.read_csv(DATA_PATH.joinpath("Unemployment-2005-2021(n).csv"))
covid_data = pd.read_csv(DATA_PATH.joinpath("US_COVID_DATA.csv"))

df_gdp_us = pd.read_csv(DATA_PATH.joinpath("GDP_us.csv"))
# fig2 = px.line(df_gdp_us, x="DATE", y="GDP",template="plotly_dark")

col_names =  ['Unemployment Total', 'Positive Covid Cases']
df  = pd.DataFrame(columns = col_names)
df['Unemployment Total'] = dfg['Unemployment Total']
df['Positive Covid Cases'] = covid_data['positive']
df['Employment Total'] = dfg['Employment Total']
df['Negative Covid Cases'] = covid_data['negative']
df['GDP'] = df_gdp_us['GDP']

print("df is", df)

corr = df.corr()

# print("corr is \n", corr.values)

fig = go.Figure([
    go.Heatmap(z=corr.values,
                  x=corr.index.values,
                  y=corr.columns.values,
                  colorscale=px.colors.sequential.YlOrRd),
                  
])

fig.update_layout(
        template="plotly_dark"
)

print("fig is \n", corr)

layout = html.Div(children=[
    dcc.Graph(
        id='correlation-mx',
        figure=fig
    ),

])
