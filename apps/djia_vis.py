import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import pathlib

app = dash.Dash(__name__)

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("DJIA.csv"))

fig = px.line(df, x="Date", y="High")
fig.show()














if __name__ == '__main__':
    app.run_server(debug=True)

