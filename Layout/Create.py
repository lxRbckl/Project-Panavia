import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from Panavia import app, setGraph, getGraph, getStyle, getCenter

graph = getGraph()
style = 9
createLayout = html.Div([

    html.H1('create')

])
