import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import app2, bar_chart, linecharts, scatterplotmat, scatterplotmat2, stock

styling = {
    'background': '#111111',
    'text': '#7FDBFF',
    'padding': '14px',
}
landing = {
    'background': '#111111',
    'text': '#7FDBFF',
    'padding': '2%',
    'height': '100vw',
}
text = {
    'color':'#e2f7ff',
}

summary = 'The effects of COVID-19 has impacted several facets of society. '\
    'It has caused the death of millions and has become the focus of several governments across the globe. '\
    'Specifically, the U.S. economy has suffered since the COVID-19 pandemic - '\
    'sparking mass unemployment rates across states and a stock market decline. '\
    'The purpose of this interactive visualization is to highlight how COVID-19 has '\
    'impacted the U.S. workforce and stock market.'
unemployment = 'As the COVID-19 pandemic spread rapidly throughout the world, '\
    'countries that were heavily impacted experienced a drastic increase in unemployment rate. '\
    'In the United States of America, unemployment rates peaked due to fear of the coronavirus. '\
    'Thousands of workers were discharged from their workplaces, while others shifted to remote work. '\
    'As indicated in the visualizations below, unemployment rates peaked in April of 2020 and '\
    'began to decrease steadily over time.'

stock = 'As unemployment rates soared during the COVID-19 pandemic, the U.S. stock market plunged '\
    'as investors hastily sold their holdings in anticipation of worker layoffs. '\
    'Unlike the Great Recession of 2008, stocks plunged between March and April of 2020 for the COVID-19 pandemic. '\
    'During the Great Recession, stocks appeared to have slowly declined over successive months.'


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.Div([
            dcc.Link('    COVID-19 Impact on U.S. Economy', href='/',  style={"marginLeft": "1rem","fontFamily":"Blippo, fantasy", "textDecoration": "none", "fontSize": '3rem', 'color': '#e2f7ff'})
        ]),
        dcc.Link('Unemployment', href='/apps/unemployment', className='button'),
        dcc.Link('Line Chart', href='/apps/linecharts', className='button'),
        dcc.Link('BarChart', href='/apps/barchart', className='button'),
        dcc.Link('ScatterPlot', href='/apps/scatterplotmat2', className='button'),
        dcc.Link('Stock', href='/apps/stock', className='button')
    ], className="row", style={"background": "black", 'color': '#7FDBFF', "marginBottom": '3rem'}),
    html.Div(id='page-content', children=[],style={"background": "black", 'color': '#7FDBFF'}, className = 'styling')
], style={"background": "black", 'color': '#7FDBFF'})

layout = html.Div([

    html.Div([
    html.Div([
        html.H1('COVID-19 Impact on U.S. Economy', style={'marginBottom': '1px'}),
        html.P('By: Eram Manasia, Jamescy Exime, Kenneth Feng, Mitchell Mui, Peter Ye, Ravid Rahman | Created with Dash Plotly.', style={'color': '#e2f7ff'}),
    ], style={'borderBottom': '2px solid rgb(80, 200, 255)'}),
    html.Div([
        html.P(summary, style={'color': '#e2f7ff'}),
        html.H3('U.S. Unemployment Analysis'),
        html.P(unemployment, style={'color': '#e2f7ff'}),
        html.H3('U.S. Stock Analysis'),
        html.P(stock, style={'color': '#e2f7ff'}),
    ], style={'marginTop':'2%'})
    ], style={'padding': '3%'})
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname =='/apps/scatterplotmat':
        return scatterplotmat.layout
    if pathname =='/apps/scatterplotmat2':
        return scatterplotmat2.layout
    if pathname == '/apps/unemployment':
        return app2.layout
    if pathname == '/apps/linecharts':
        return linecharts.layout
    if pathname == '/apps/barchart':
        return bar_chart.layout
    if pathname == '/apps/stock':
        return stock.layout
    if pathname == '/':
        return layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)