import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("DJIA2.0.csv"))

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
                value='open',
                )  

    ]),
    

    dcc.Graph(id='djia-graphic'),

    dcc.Slider(
        id='month--slider',
        min=1,
        max=12,
        value=12,
        #marks={str(month): str(month) for month in df['Month'].unique()},
        marks={
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'jun',
        7: 'jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'

    },
        step=None,
    )


])

@app.callback(
    Output('djia-graphic', 'figure'),
    #Input('yaxis-column', 'value'),
    Input('month--slider', 'value'))
def update_graph(yaxis_column_name, month_value):
    #dff = df[df['Month'] == month_value]
    filtered_df = df[df.Month == month_value]
    
    #dropdown_optons['Open', 'Hign', 'Low', 'Close', 'Adj Close', 'Volume']

    fig = px.line(filtered_df, x="Date", y="High")
    
    fig.update_layout()

    return fig










#fig = px.line(df, x="Date", y="High")
#fig.show()


if __name__ == '__main__':
    app.run_server(debug=True)

