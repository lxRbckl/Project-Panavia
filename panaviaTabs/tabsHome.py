from panaviaFunctions.functionsGetJSON import getJSON

import dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def home():
    '''  '''

    df = px.data.election()
    geojson = px.data.election_geojson()
    settings = getJSON('settingsStyle.json')

    return html.Div([

        html.Div([

            px.choropleth_mapbox(data_frame = df,
                                 geojson = geojson,
                                 color = 'Bergeron',
                                 locations = 'Bergeron',
                                 mapbox_style = 'open-street-map'

            ).show()

        ], style = settings['homeMap'])

    ], style = settings['panaviaTab'])
