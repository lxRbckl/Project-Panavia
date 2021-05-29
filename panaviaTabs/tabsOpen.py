from panaviaFunctions.functionsGetJSON import getJSON

import dash
import plotly.figure_factory as ff
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def tabOpen(tab):
    '''  '''

    if (tab == 'open'):

        settings = getJSON('settingsStyle.json')

        return html.Div([

            html.H1('load')

        ], style = settings['panaviaTab'])
