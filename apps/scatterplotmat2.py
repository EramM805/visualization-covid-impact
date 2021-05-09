import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
import statistics
app = dash.Dash(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("Unemployment-2007-2021.csv"))
#years = ["2008", "2009", "2010", "2011", "2012", "2013", "2014","2015", "2016", "2017", "2018", "2019", "2020"]


app.layout = html.Div([
    html.H1("United States Unemployment Statistics 2008 - 2020", style = {"textAlign": "center", "width": "100%", "fontSize": "150%"}),
    
    html.Div([
        
        
        html.Div([
        html.Pre(children="Year", style = {"textAlign": "center", "width": "100px", "fontSize": "150%"}),
        dcc.Dropdown(
            style = {"textAlign": "center", "width": "100px"},
            id="dropdown",
            options=[{"label": x, "value": x} for x in sorted(df["Year"].unique())],
            value=2008,
            clearable=False,
        )
        ], className = 'six columns'),

        html.Div([
        html.Pre(children="Month", style = {"textAlign": "center", "width": "100px", "fontSize": "150%"}),
        dcc.Dropdown(
            style = {"textAlign": "center", "width": "100px"},
            id="dropdown-month",
            options=[{"label": x, "value": x} for x in sorted(df["Month"].unique())],
            value="1",
            clearable=False,
        )
        ], className = 'six columns'),
    ], className = 'row'),
    
    dcc.Graph(id="scattermat"),
])

@app.callback(
    Output("scattermat", "figure"), 
    [Input("dropdown", "value"),
    Input("dropdown-month", "value")]
    )
def update_scattermat(year, month):
    year_df = df[(df['Year'] == year) & (df['Month'] == month)]
    #year_df = year_df.groupby(["Month"])[['Unemployment Total']]
    fig = px.scatter_matrix(year_df,
    dimensions=["Labor Force Percent of Population", "Employment Percent of Population", "Unemployment Rate"],
    color="State",
    #title="Scatterplot Matrix of Unemployment 2007",
    labels={col:col.replace(',', ' ') for col in df.columns}) # remove underscore
    
    fig.update_traces(diagonal_visible=False)
    fig.update_traces
    fig.update_layout(
    autosize=False,
    width = 1000,
    height = 1000,
    )
    return fig

app.run_server(debug=True)