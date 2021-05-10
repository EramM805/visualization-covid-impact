# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df = pd.read_csv(DATA_PATH.joinpath("Unemployment-2005-2021(n).csv"))
fig = px.line(df, x="Year", y="Unemployment Rate")

df_gdp_us = pd.read_csv(DATA_PATH.joinpath("GDP_us.csv"))
fig2 = px.line(df_gdp_us, x="DATE", y="GDP",template="plotly_dark")

df_unemployement_us = pd.read_csv(DATA_PATH.joinpath("Unemployement-2005-2021-US.csv"))
fig3 = px.line(df_unemployement_us, x="DATE", y="UNRATE",template="plotly_dark")

fig.update_traces(mode='lines+markers') 
layout = html.Div(children=[
        html.H1(
        children='Line charts',
        style={
            'textAlign': 'center',
            # 'color': colors['text']
        }
    ),
     html.H3(children='US GDP', style={
        # 'color': colors['text']
    }),
    dcc.Graph(
        id='gdp-us-line-chart',
        figure=fig2
    ),

   html.H3(children='US unemployement rate', style={
        # 'color': colors['text']
    }),
    dcc.Graph(
        id='unemployement-us-line-chart',
        figure=fig3
    ),

    

    html.H3(children='Unemployement rates per state.', style={
        # 'color': colors['text']
    }),
    
    #credit for dropdown code to @peterye
   html.Div([
            html.Pre(children="Month"),
            dcc.Dropdown(
                id='month-dropdown', value='January', clearable=False,
                persistence=True, persistence_type='local',
                options=[{'label': x, 'value': x} for x in sorted(df["Month"].unique())],
            )
            ]),
    
     html.Div([
            html.Pre(children="State"),
            dcc.Checklist(
                id='state-check-list', value=['Alabama'],
                options = [{'label': i, 'value': i} for i in df['State'].unique()],
                labelStyle={'display': 'inline'},
            )
            ]),

    dcc.Graph(
        id='unemployement-state-line-chart',
    ),

])

@app.callback(
    Output(component_id='unemployement-state-line-chart', component_property='figure'),
    [Input(component_id='month-dropdown', component_property='value'),
    Input(component_id='state-check-list', component_property='value')
    ]
)
def display_value(month_chosen, states_chosen):
    df_fltr = df[(df['Month'] == month_chosen)]
    df_fltr = df_fltr[df_fltr["State"].isin(states_chosen)]
    fig = px.line(df_fltr, x="Year", y="Unemployment Rate", template="plotly_dark", color='State')
    return fig