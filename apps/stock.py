import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
import plotly.graph_objects as go
from sklearn.decomposition import PCA

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("DJIA2.0.csv"))

# fig = px.line(df, x="Date", y="High")
month_selc = df['Month'].unique()

df['Date'] = pd.to_datetime(df['Date'])
df_2008 = df[df['Date'].dt.year == 2008]
df_2020 = df[df['Date'].dt.year == 2020]
df_pca = df.drop('Date', axis=1)
df_pca = df_pca.drop('Month', axis=1)
df_pca = df_pca.drop('Year', axis=1)
print(df_pca.dtypes)

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

    html.Div([ 
        
        dcc.Dropdown(
            id='xaxis-column',
            options=[{'label': i, 'value': i} for i in month_selc],
            value='Jan',
            )  

    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    html.Div([ 
        dcc.Checklist(
            id='toggle-rangeslider',
            options=[{'label': 'Include Rangeslider', 
                    'value': 'slider'}],
            value=['slider']
        )
    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    dcc.Graph(id='djia-graphic'),    
    dcc.Graph(id='djia-graphic-2'),
    dcc.Graph(id="graph1"),
    dcc.Graph(id="graph2"),

    html.Div([
    dcc.Graph(id="stock_pca"),
    html.P("Number of components:"),
    dcc.Slider(
        id='pca_slider',
        min=2, max=5, value=3,
        marks={i: str(i) for i in range(2,6)})
    ])
])

@app.callback(
    [Output(component_id='djia-graphic', component_property='figure'),
    Output(component_id='djia-graphic-2', component_property='figure'),
    Output(component_id='graph1', component_property='figure'),
    Output(component_id='graph2', component_property='figure'),
    Output("stock_pca", "figure")],
    [Input(component_id='yaxis-column', component_property='value'),
    Input(component_id='xaxis-column', component_property='value'),
    Input(component_id='toggle-rangeslider', component_property='value'),
    Input("pca_slider", "value")])
    #Input('month--slider', 'value'))
def update_graph(yaxis_column_name, xaxis_column_name, value, n_components):
    # x column name is month
    # y column name is other
    # df = df[df['Month'] == xaxis_column_name]
    # df =
    # dff = df[df['Month'] == xaxis_column_name]
    # dff_2020 = df['Year'] = 2020
    dff_2020 = df[(df['Month'] == xaxis_column_name) & (df['Year'] == 2020)]
    dff_2020 = dff_2020[[yaxis_column_name, 'Month', 'Date', 'Year']] 
    dff_2008 = df[(df['Month'] == xaxis_column_name) & (df['Year'] == 2008)]
    dff_2008 = dff_2008[[yaxis_column_name, 'Month', 'Date', 'Year']] 
    # dff = df[(df['Month'] == xaxis_column_name) &
    #                 (df[] == yaxis_column_name)]
    
    
    #dropdown_optons['Open', 'Hign', 'Low', 'Close', 'Adj Close', 'Volume']

    # fig = px.line(df,x=df[df['Month'] == xaxis_column_name]['Date'], y=df['High'])
    
    #fig.update_layout()
    fig = px.line(dff_2020, x="Date", template="plotly_dark", y=yaxis_column_name)
    fig2 = px.line(dff_2008, x="Date", template="plotly_dark", y=yaxis_column_name)

    candle1 = go.Figure(go.Candlestick(
        x=df_2008['Date'],
        open=df_2008['Open'],
        high=df_2008['High'],
        low=df_2008['Low'],
        close=df_2008['Close']
    ))

    candle2 = go.Figure(go.Candlestick(
        x=df_2020['Date'],
        open=df_2020['Open'],
        high=df_2020['High'],
        low=df_2020['Low'],
        close=df_2020['Close']
    ))

    candle1.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    candle2.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    pca = PCA(n_components=n_components)
    components = pca.fit_transform(df_pca)

    var = pca.explained_variance_ratio_.sum() * 100

    labels = {str(i): f"PC {i+1}" 
              for i in range(n_components)}
    labels['color'] = 'Median Price'

    fig_pca_stock = px.scatter_matrix(
        components,
        color=df_pca.High,
        dimensions=range(n_components),
        labels=labels,
        title=f'Total Explained Variance: {var:.2f}%')
    fig_pca_stock.update_traces(diagonal_visible=False)

    return [fig, fig2, candle1, candle2, fig_pca_stock]