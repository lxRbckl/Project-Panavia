from panaviaFunctions.functionsGetJSON import getJSON

import dash
import plotly.figure_factory as ff
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def create():
    '''  '''

    settings = getJSON('settingsStyle.json')

    return html.Div([

        html.H1('create')

    ], style = settings['panaviaTab'])
