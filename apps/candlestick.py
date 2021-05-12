import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pathlib
from app import app
import pandas as pd
import datetime as dt

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("DJIA2.0.csv"))
df['Date'] = pd.to_datetime(df['Date'])
df_2008 = df[df['Date'].dt.year == 2008]
df_2020 = df[df['Date'].dt.year == 2020]

layout = html.Div([
    dcc.Checklist(
        id='toggle-rangeslider',
        options=[{'label': 'Include Rangeslider', 
                  'value': 'slider'}],
        value=['slider']
    ),
    dcc.Graph(id="graph1"),
    dcc.Graph(id="graph2")
])

@app.callback(
    [Output(component_id='graph1', component_property='figure'),
    Output(component_id='graph2', component_property='figure')],
    [Input(component_id='toggle-rangeslider', component_property='value')])
def display_candlestick(value):
    fig1 = go.Figure(go.Candlestick(
        x=df_2008['Date'],
        open=df_2008['Open'],
        high=df_2008['High'],
        low=df_2008['Low'],
        close=df_2008['Close']
    ))

    fig2 = go.Figure(go.Candlestick(
        x=df_2020['Date'],
        open=df_2020['Open'],
        high=df_2020['High'],
        low=df_2020['Low'],
        close=df_2020['Close']
    ))

    fig1.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    fig2.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    return fig1, fig2