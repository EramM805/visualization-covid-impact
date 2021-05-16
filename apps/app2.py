import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
import plotly.graph_objects as go


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

dfg = pd.read_csv(DATA_PATH.joinpath("Unemployment-2005-2021(n).csv"))
dfg_s = pd.read_csv(DATA_PATH.joinpath("SDD_Final.csv"))

covid_data = pd.read_csv(DATA_PATH.joinpath("US_COVID_DATA.csv"))
# df = pd.read_csv(DATA_PATH.joinpath("Unemployment-2005-2021(n).csv"))
# fig3 = px.line(df, x="Year", y="Unemployment Rate")


layout = html.Div([
    html.H1('Unemployment Rates by State', style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}),

    html.Div([
        html.Div([
            html.Pre(children="Year", style={"fontSize":"150%", "background": "black", 'color': '#7FDBFF'}),
            dcc.Slider(
                id='year-slider',
                min=2006,
                max=2020,
                value=2020,
                persistence=True,
                persistence_type='session',
                marks={
                    2006: {'label': '2006'},
                    2007: {'label': '2007'},
                    2008: {'label': '2008'},
                    2009: {'label': '2009'},
                    2010: {'label': '2010'},
                    2011: {'label': '2011'},
                    2012: {'label': '2012'},
                    2013: {'label': '2013'},
                    2014: {'label': '2014'},
                    2015: {'label': '2015'},
                    2016: {'label': '2016'},
                    2017: {'label': '2017'},
                    2018: {'label': '2018'},
                    2019: {'label': '2019'},
                    2020: {'label': '2020'}
                }
            )  
            
            # dcc.Dropdown(
            #     id='year-slider', value=2020, clearable=False,
            #     persistence=True, persistence_type='session',
            #     options=[{'label': x, 'value': x} for x in sorted(dfg["Year"].unique())],
            #     style={'color': '#7FDBFF', 'text': '#7FDBFF'}
            # )
        ]),

        

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

    html.Div(className='row', children = [
   
            # html.Div([
       
            # html.Pre(children="Month", style={"fontSize": "150%", "background": "black", 'color': '#7FDBFF'}),
            # dcc.Dropdown(
            #     id='month-dropdown', value='April', clearable=False,
            #     persistence=True, persistence_type='local',
            #     options=[{'label': x, 'value': x} for x in (dfg["Month"].unique())],
            #     style={'color': '#7FDBFF', 'text': '#7FDBFF'}
            # )
            # ]),
            html.Div(className='row', children=[

                html.Div([
                    html.H3(children='US Unemployment Rate by Year and Month', 
                        style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}
                    ),
                    dcc.Graph(id='heat-map', style={'display': 'inline-block'}),
                    html.Div([
                    html.Pre(children="Month", style={"fontSize": "150%", "background": "black", 'color': '#7FDBFF'}),
                        dcc.Dropdown(
                            id='month-dropdown', value='April', clearable=False,
                            persistence=True, persistence_type='local',
                            options=[{'label': x, 'value': x} for x in (dfg["Month"].unique())],
                            style={'color': '#7FDBFF', 'text': '#7FDBFF'}
                        ),
                    ], style={'paddingLeft': '5%', 'paddingRight': '5%'}),
                ],className = 'six columns'),
                html.Div([
                    html.H3(children='US Unemployment Rate by Year and Month', 
                        style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}
                    ),
                    

                    dcc.Graph(id='unemployement-state-line-chart-2', style={'display': 'inline-block'})
                ],className = 'six columns'),
                    
                
                
            ] , style={'padding': '2%','borderBottom': '2px solid #7FDBFF'}),
            ]),

    dcc.Graph(id="bar-chart-2", style={'padding': '2%','borderBottom': '2px solid #7FDBFF'}),

    html.Div([
        html.H3(children='US Unemployment Surprise Map by Year (April Only)', 
        style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}
        ),
        html.Div(children=[    
        dcc.Graph(id='surprise-map', style={'display': 'inline-block'}) 
        ]),   
    ], className='row', style={'padding': '2%','borderBottom': '2px solid #7FDBFF'}),

    ], className='row', style={"textAlign": "center", "background": "black", 'color': '#7FDBFF'}),
    
],className=colors)


@app.callback(
    [Output(component_id='heat-map', component_property='figure'),
    Output(component_id='surprise-map', component_property='figure'),
    Output(component_id='unemployement-state-line-chart-2', component_property='figure'),
    Output(component_id='bar-chart-2', component_property='figure')],
    [Input(component_id='year-slider', component_property='value'),
    Input(component_id='month-dropdown', component_property='value'),
    Input(component_id='heat-map', component_property='clickData')
]
)
def display_value(pymnt_chosen, month_chosen, clickData):
    df_fltr = dfg[(dfg['Month'] == "January")]
    df_fltr = df_fltr[df_fltr["State Code"] == "AL"]
    loc = "AL"
    if clickData is not None:            
        location = clickData['points'][0]['location']
        df_fltr = dfg[(dfg['Month'] == month_chosen)]
        df_fltr = df_fltr[df_fltr["State Code"] == location]
        loc = clickData['points'][0]['location']
    dfg_fltrd = dfg[(dfg['Month'] == month_chosen) &
                    (dfg["Year"] == pymnt_chosen)]
    dfg_fltrd = dfg_fltrd.groupby(["State Code", 'State', 'Labor Force Total'])[['Unemployment Rate']].sum()
    dfg_fltrd_surprise = dfg_s[(dfg_s['Month'] == 'April') &
                    (dfg_s["Year"] == pymnt_chosen)]
    dfg_fltrd_surprise = dfg_fltrd_surprise.groupby(["State Code", 'State'])[['Value']].sum()
    #print(dfg_fltrd_surprise)
    
    dfg_fltrd_surprise.reset_index(inplace=True)
    dfg_fltrd.reset_index(inplace=True)

    fig = px.choropleth(dfg_fltrd, locations="State Code", hover_data=['State','Labor Force Total', 'Unemployment Rate'],
                        locationmode="USA-states", color="Unemployment Rate", labels={'Unemployment Rate':'Unemployment Rate (%)'},template='plotly_dark', color_continuous_scale=px.colors.sequential.YlOrRd,range_color=(0, 20),
                        scope="usa")
    fig2 = px.choropleth(dfg_fltrd_surprise, locations="State Code", hover_data=['State', 'Value'],
                        locationmode="USA-states", color="Value", labels={'Value':'Surprise Value'},template='plotly_dark', color_continuous_midpoint=0, color_continuous_scale=px.colors.diverging.balance,
                        scope="usa")
    
    fig3 = px.line(df_fltr, x="Year", y="Unemployment Rate", template="plotly_dark", title=loc)

    year_df = dfg[(dfg['Year'] == 2020) & (dfg['State Code'] == loc)]
    covid_df = covid_data[(covid_data['Year'] == 2020) & (covid_data['state'] == loc)]
    # fig4 = px.bar(
    #     year_df, 
    #     y="Unemployment Total", 
    #     x="Month", 
    #     hover_data=["State", "Unemployment Rate","Unemployment Total", "Year", "Month"], 
    #     labels = {'Month': 'Months', 'Unemployment Rate': 'Unemployment Rate (%)'},
    #     template="plotly_dark"
    # )
    # animals=['giraffes', 'orangutans', 'monkeys']
    #Month, positive
    covid_df_2 = covid_df[['Month', 'positive']]
    covid_month = covid_df_2.groupby(['Month']).mean()
    print(covid_month['positive'])
    fig4 = go.Figure(
    data=[
    go.Bar(name='Unemployment', x=year_df['Month'], y =year_df['Unemployment Total']),
    go.Bar(name='Covid', x=covid_month.index, y =covid_month['positive']),
    ])
    # Change the bar mode
    fig4.update_layout(barmode='group', template="plotly_dark")



    # print("fig3 is ", fig3)
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

    
    return [fig, fig2, fig3, fig4]