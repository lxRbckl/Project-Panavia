from panaviaFunctions.functionsGetJSON import getJSON

import dash
import plotly.express as px
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

def tabHome(tab):
    '''  '''

    if (tab == 'home'):

        settings = getJSON('settingsStyle.json')

        return html.Div([

            html.Div([

                html.H1('home')

            ], style = settings['homeMap'])

        ], style = settings['panaviaTab'])
