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
df = pd.read_csv(DATA_PATH.joinpath("DJI.csv"))


layout = html.Div([

    html.Div([ 
        
        dcc.Dropdown(
            id='yaxis-column',
            options=[
                {'label': 'Open', 'value': 'Open'},
                {'label': 'High', 'value': 'High'},
                {'label': 'Low', 'value': 'Low'},
                {'label': 'Close', 'value': 'Close'},
                {'label': 'Adj Close', 'value': 'Adj Close'},
                {'label': 'Volume', 'value': 'Volume'},
                ],
                value='Open',
                )  

    ], style={'width': '48%', 'display': 'inline-block'}),

    
    dcc.Graph(id='djia-graphic'),
    dcc.Graph(id='djia-graphic-2'),
    dcc.Graph(id='djia-graphic-3'),
    #dcc.Graph(id='djia-grapics-4')

])

@app.callback(
    [Output(component_id='djia-graphic', component_property='figure'),
    Output(component_id='djia-graphic-2', component_property='figure'),
    Output(component_id='djia-graphic-3', component_property='figure')
    #Output(component_id='djia-graphic-4', component_property='figure')
    ],
    [Input(component_id='yaxis-column', component_property='value')])
    
def update_graph(yaxis_column_name):

    #dff_2020 = df[df['Year'] == 2020]
    #dff_2020 = dff_2020[[yaxis_column_name, 'Date', 'Year']] 

    dff_2020 = df[df['Date'].str.contains("2020")] 
    dff_2008 = df[df['Date'].str.contains("2009")] 

    fig = px.line(df, x="Date", template="plotly_dark", y=yaxis_column_name)
    fig2 = px.line(dff_2020, x="Date", template="plotly_dark", y=yaxis_column_name)
    fig3 = px.line(dff_2008, x="Date", template="plotly_dark", y=yaxis_column_name)
    #fig4 = px.scatter_matrix(components, labels=labels, dimensions=range(6), color=df['Date'])
    
    #fig4.update_traces(diagonal_visible=False)


    return [fig, fig2, fig3]
