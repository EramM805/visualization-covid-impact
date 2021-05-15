import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

dfg = pd.read_csv(DATA_PATH.joinpath("Unemployment-2005-2021(n).csv"))
dfg_s = pd.read_csv(DATA_PATH.joinpath("SDD_Final.csv"))



layout = html.Div([
    html.H1('Unemployment Rates by State', style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}),

    html.Div([
        html.Div([
            html.Pre(children="Year", style={"fontSize":"150%", "background": "black", 'color': '#7FDBFF'}),
            dcc.Dropdown(
                id='year-dropdown', value=2020, clearable=False,
                persistence=True, persistence_type='session',
                options=[{'label': x, 'value': x} for x in sorted(dfg["Year"].unique())],
                style={'color': '#7FDBFF', 'text': '#7FDBFF'}
            )
        ], className='six columns'),

        html.Div([
            html.Pre(children="Month", style={"fontSize": "150%", "background": "black", 'color': '#7FDBFF'}),
            dcc.Dropdown(
                id='month-dropdown', value='April', clearable=False,
                persistence=True, persistence_type='local',
                options=[{'label': x, 'value': x} for x in sorted(dfg["Month"].unique())],
                style={'color': '#7FDBFF', 'text': '#7FDBFF'}
            )
            ], className='six columns'),
    ], className='row', style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}),

    # html.Div([
    #     html.Div([
    #     html.H2('Unemployment Rates by Year and Month', style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}),

    #     dcc.Graph(id='heat-map'),
    #     ])
    # ]),

    #  html.Div([
    #     html.Div([
    #         html.H2('Surprise Map', style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}),
    #     dcc.Graph(id='suprise-map'),
    #     ])
    # ]),

    html.Div([
    html.H3(children='US Unemployement Rate by Year and Month', 
        style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}
    ),


    dcc.Graph(id='heat-map'),
    
    html.H3(children='US Unemployement Suprise Map by Year (April Only)', 
        style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}
    ),

    dcc.Graph(id='surprise-map')    
    ], className='row', style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}),
],className=colors)


@app.callback(
    [Output(component_id='heat-map', component_property='figure'),
    Output(component_id='surprise-map', component_property='figure')],
    [Input(component_id='year-dropdown', component_property='value'),
    Input(component_id='month-dropdown', component_property='value')]
)
def display_value(pymnt_chosen, month_chosen):
    dfg_fltrd = dfg[(dfg['Month'] == month_chosen) &
                    (dfg["Year"] == pymnt_chosen)]
    dfg_fltrd = dfg_fltrd.groupby(["State Code", 'State', 'Labor Force Total'])[['Unemployment Rate']].sum()
    dfg_fltrd_surprise = dfg_s[(dfg_s['Month'] == 'April') &
                    (dfg_s["Year"] == pymnt_chosen)]
    dfg_fltrd_surprise = dfg_fltrd_surprise.groupby(["State Code", 'State'])[['Value']].sum()
    print(dfg_fltrd_surprise)
    
    dfg_fltrd_surprise.reset_index(inplace=True)
    dfg_fltrd.reset_index(inplace=True)

    fig = px.choropleth(dfg_fltrd, locations="State Code", hover_data=['State','Labor Force Total', 'Unemployment Rate'],
                        locationmode="USA-states", color="Unemployment Rate", labels={'Unemployment Rate':'Unemployment Rate (%)'},template='plotly_dark', color_continuous_scale=px.colors.sequential.YlOrRd,range_color=(0, 20),
                        scope="usa")
    fig2 = px.choropleth(dfg_fltrd_surprise, locations="State Code", hover_data=['State', 'Value'],
                        locationmode="USA-states", color="Value", labels={'Value':'Surprise Value'},template='plotly_dark', color_continuous_midpoint=0, color_continuous_scale=px.colors.diverging.balance,
                        scope="usa")

    fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
    fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
    return [fig, fig2]