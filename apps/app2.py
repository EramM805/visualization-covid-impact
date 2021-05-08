import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import pathlib

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
dfg = pd.read_csv(DATA_PATH.joinpath("Unemployment-2007-2021.csv"))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



# ------------------------------------------------------------------------------
# App layout
layout = html.Div([
    html.H1('Unemployment Rates by State', style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.Pre(children="Year", style={"fontSize":"150%"}),
            dcc.Dropdown(
                id='year-dropdown', value='2020', clearable=False,
                persistence=True, persistence_type='session',
                options=[{'label': x, 'value': x} for x in sorted(dfg["Year"].unique())]
            )
        ], className='six columns'),

        html.Div([
            html.Pre(children="Month", style={"fontSize": "150%"}),
            dcc.Dropdown(
                id='month-dropdown', value='4', clearable=False,
                persistence=True, persistence_type='local',
                options=[{'label': x, 'value': x} for x in sorted(dfg["Month"].unique())]
            )
            ], className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-map', figure={}),
])

@app.callback(
    Output(component_id='my-map', component_property='figure'),
    [Input(component_id='year-dropdown', component_property='value'),
     Input(component_id='month-dropdown', component_property='value')]
)
def display_value(year_chosen, month_chosen):
    dfg_fltrd = dfg[(dfg['Month'] == month_chosen) &
                    (dfg["Year"] == year_chosen)]
    dfg_fltrd = dfg_fltrd.groupby(["State"])[['Unemployment Rate']].sum()
    dfg_fltrd.reset_index(inplace=True)
    fig = px.choropleth(dfg_fltrd, locations="State",
                        locationmode="USA-states", color="Unemployment Rate",
                        scope="usa")
    return fig