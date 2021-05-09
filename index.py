import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1
from apps import scatterplotmat
from apps import scatterplotmat2


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname =='/apps/scatterplotmat':
        return scatterplotmat.layout
    elif pathname =='/apps/scatterplotmat2':
        return scatterplotmat2.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)