import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app

# Connect to your app pages
from apps import app1, app2, bar_chart, linecharts, scatterplotmat, scatterplotmat2, stock, pc

server = app.server

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
    'Thousands of workers were discharged from their workplaces, while others shifted to remote work. '

stock_str = 'As unemployment rates soared during the COVID-19 pandemic, the U.S. stock market plunged '\
    'as investors hastily sold their holdings in anticipation of worker layoffs. '\
    'Unlike the Great Recession of 2008, stocks plunged between March and April of 2020 for the COVID-19 pandemic. '\
    'During the Great Recession, stocks appeared to have slowly declined over successive months.'

conclusion_str = 'Ultimately, this project analyzed and answered several research questions pertaining to the US economy and the \
impact the pandemic had on it. The outbreak led to a sharp increase in unemployment rates which contributed to a decrease in the \
gross domestic product as both are strongly negatively correlated. Although covid cases did not have a direct correlation to unemployment,\
the pandemic contributed to the spike in unemployment rates. This resulted in unemployment benefits and temporary layoffs along with lockdown \
restrictions. Furthermore, both the 2008 recession and the 2020 pandemic left dents on the US economy, the US has proven to recover \
with help of policies and government intervention.'

introduction_str = 'The interpolation of COVID-19 created a global pandemic which launched the United States into another recession. \
Ultimately, this pandemic changed all aspects of everyday life, including work-life balance, education, entertainment, and the economy. \
In order to preserve human life, and keep the pandemic to a minimum, many businesses were forced to shut down or lay off employees resulting \
in a huge disruption to the supply chains. This brings up several questions: how has the pandemic affected the US economy specifically? \
Is there a specific correlation between the positive cases and economic indicators such as GDP and unemployment? How does COVID-19’s \
impact on the stock market compare with the 2007-8 financial crisis? This project attempts to answer each question by using visualizations \
such as heat maps, suprise maps, line charts, bar charts, scatterplot matrix, pearson correlation matrix, and candlestick charts. '


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.Div([
            dcc.Link('    COVID-19 Impact on U.S. Economy', href='/',  style={"marginLeft": "1rem","fontFamily":"Blippo, fantasy", "textDecoration": "none", "fontSize": '3rem', 'color': '#e2f7ff'})
        ]),
        dcc.Link('Home Page', href='/', className='button'),
        dcc.Link('Unemployment Analysis Dashboard', href='/apps/unemployment', className='button'),
        dcc.Link('Line Charts', href='/apps/linecharts', className='button'),
        # dcc.Link('Bar Chart', href='/apps/barchart', className='button'),
        dcc.Link('Scatter Plot', href='/apps/scatterplotmat2', className='button'),
        dcc.Link('Stock Analysis Dashboard', href='/apps/stock', className='button'),
        dcc.Link('Pearson Correlation Matrix', href='/apps/pc', className='button')
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
        html.H3('Summary'),
        html.P(summary, style={'color': '#e2f7ff'}),
        html.H3('Introduction'),
        html.P(introduction_str, style={'color': '#e2f7ff'}),
        html.H3('U.S. Unemployment Analysis'),
        html.P(unemployment, style={'color': '#e2f7ff'}),
        html.Div([html.P('To view the line charts related to unemployment visit ', style={'color': '#e2f7ff', 'display': 'inline'}), html.A('the line charts subsection.', href='/apps/linecharts'),]),
        html.Div([html.P('To interact with different visualizations including heat maps, surprise maps, scatterplot matrix, bar charts, and line charts related to unemployment visit ', style={'color': '#e2f7ff', 'display': 'inline'}), html.A('the unemployment dashboard.', href='/apps/unemployment'),]),
        html.Div([html.P('To view the pearson correlation matrix on GDP, unemployment, and covid related attributes visit ', style={'color': '#e2f7ff', 'display': 'inline'}), html.A('the correlation matrix subsection', href='/apps/pc'),]),
        html.Div([html.P('To view the scatterplot matrix for different components color coded by unemployment rate visit ', style={'color': '#e2f7ff', 'display': 'inline'}), html.A('the scatterplot matrix subsection', href='/apps/scatterplotmat2'),]),

        html.H3('U.S. Stock Analysis'),
        html.P(stock_str, style={'color': '#e2f7ff'}),
        html.Div([html.P('To interact with different visualizations related to our stock analysis visit ', style={'color': '#e2f7ff', 'display': 'inline'}), html.A('our stack analysis dashboard.', href='/apps/stock'),]),
        html.H3('Conclusion'),
        html.P(conclusion_str, style={'color': '#e2f7ff'}),

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
    if pathname == '/apps/pc':
        return pc.layout
    if pathname == '/':
        return layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)