# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.io as pio
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("../data/Unemployment-2007-2021.csv")
df = df[df['Year'] =='2008']
df = df.groupby(['Month', 'State',],as_index=False)[['Unemployment Total','Unemployment Rate']].sum()
print (df[:5])


bar_chart = px.bar(
    data_frame = df,
    x = 'State',
    y = 'Unemployment Rate',
    color = "State",
    opacity = 0.9,
    orientation = "v",
    barmode = 'relative',

)

bar_chart.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=bar_chart
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
