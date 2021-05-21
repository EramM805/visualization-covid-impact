import plotly.graph_objs as go
import pandas as pd
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("corr_data.csv"))
df = df.drop(columns=['Unnamed: 0'])
corr = df.corr()

print("df is ", df.columns)
fig = go.Figure([
    go.Heatmap(z=corr.values,
                  x=corr.index.values,
                  y=corr.columns.values,
                  colorscale=px.colors.diverging.RdBu),
                  
])

fig.update_layout(
        template="plotly_dark"
)

print("fig is \n", corr)

layout = html.Div(children=[
    dcc.Graph(
        id='correlation-mx',
        figure=fig
    ),

])
