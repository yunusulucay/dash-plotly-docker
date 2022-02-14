# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_mantine_components as dmc
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from datetime import date
import json
import flask

server = flask.Flask(__name__)

app = dash.Dash(__name__, server=server)

colors = {"background":"blue"}

with open("configuration.json") as a:
    json_file = json.load(a)

csv_path = json_file["csv_path"]

df = pd.read_csv(csv_path, parse_dates=[0], index_col=0) 

df.index.name = ""

cols = df.columns

min_date = df.index.min().strftime("%Y-%m-%d")
max_date = df.index.max().strftime("%Y-%m-%d")

app.layout = html.Div([
    dmc.Affix(html.H1(
        "Dashboard by Yunus Emrah Uluçay"
    ), position={"top": 5, "left": 400}),
    html.Div(children="Select date from below"
    ),
    dcc.DatePickerRange(
        id="date-picker-range",
        min_date_allowed=min_date,
        max_date_allowed=max_date,
        initial_visible_month=min_date,
        start_date=min_date,
        end_date=max_date
    ),
    dcc.Graph(
        id="example-graph"
    ),
    dcc.RadioItems(
        id="radio-items",
        options=[
            {"label":"Histogram","value":"hist"},
            {"label":"Line Plot","value":"line"},
            {"label":"Scatter Plot","value":"scatter"}
        ],
        value="line",
        labelStyle={"display":"inline-block"}
    ),
    dcc.Dropdown(
        id="dropdown-1",
        options=[{'label': i, 'value': i} for i in cols],
        style={}
    ),
    dcc.Dropdown(
        id="dropdown-2",
        options=[{'label': i, 'value': i} for i in cols],
        style={}
    )
],
#style={"backgroundColor":colors["background"]}
)

@app.callback(
    Output("example-graph", "figure"),
    Output("dropdown-1", "style"),
    Output("dropdown-2", "style"),
    Input("date-picker-range","start_date"),
    Input("date-picker-range","end_date"),
    Input("radio-items","value"),
    Input("dropdown-1","value"),
    Input("dropdown-2","value")
)
def update_output(start_date, end_date, value, 
dd1_value, dd2_value):

    fig = go.Figure()

    if value=="hist":
        fig = go.Figure()

        style1 = {"display":"none"}
        style2 = {}

        if dd2_value:        
            fig = px.histogram(df[start_date:end_date],
            x=df[start_date:end_date][dd2_value].keys(), 
            y=df[start_date:end_date][dd2_value].values)

            fig.update_layout(
                title="Histogram Plot",
                xaxis_title="index",
                yaxis_title=dd2_value
            )

    elif value=="line":
        fig = go.Figure()

        for col in cols:
            
            fig.add_trace(go.Scatter(
            name=col,
            x=df[start_date:end_date].index,
            y=df[start_date:end_date][col],
            mode="lines",
            showlegend=True
            ))
        
        fig.update_layout(
            title="Line Plot",
            xaxis_title="index",
            yaxis_title="Count"
        )
        style1 = {"display":"none"}
        style2 = {"display":"none"}

    elif value=="scatter":
        fig = go.Figure()
        
        style1 = {}
        style2 = {}

        if dd1_value and dd2_value:
            fig = px.scatter(df[start_date:end_date],
            x=df[start_date:end_date][dd1_value], 
            y=df[start_date:end_date][dd2_value])

            fig.update_layout(
                title="Histogram Plot",
                xaxis_title=dd1_value,
                yaxis_title=dd2_value
            )

    return fig, style1, style2

if __name__=="__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)

