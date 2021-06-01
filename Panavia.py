# Panavia by Alex Arbuckle #


import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from panaviaFunction.functionGet import getJSON
from panaviaFunction.functionSet import setJSON


app = dash.Dash()
setting = getJSON('settingStyle.json')
app.layout = html.Div([

    html.Div([

        html.H1('Panavia', style = setting['panaviaMenu']['menuTitle']),

        dcc.Tabs(id = 'menuId',
                 value = 'homeValue',
                 children = [

                     dcc.Tab(label = 'Home',
                             value = 'homeValue',
                             style = setting['panaviaMenu']['menuUnselected'],
                             selected_style = setting['panaviaMenu']['menuSelected']),

                     dcc.Tab(label = 'Create',
                             value = 'createValue',
                             style = setting['panaviaMenu']['menuUnselected'],
                             selected_style = setting['panaviaMenu']['menuSelected']),

                     dcc.Tab(label = 'Open',
                             value = 'openValue',
                             style = setting['panaviaMenu']['menuUnselected'],
                             selected_style = setting['panaviaMenu']['menuSelected']),

                 ]),

    ], style = setting['panaviaMenu']['style']),

    html.Div(id = 'menuContent')

])


@app.callback(Output('menuContent', 'children'), Input('menuId', 'value'))
def contentFunction(arg):
    '''  '''

    return {'homeValue' : panaviaHome(arg), 'createValue' : panaviaCreate(arg), 'openValue' : panaviaOpen(arg)}[arg]


def panaviaHome(arg):
    '''  '''

    if (arg == 'homeValue'):

        setting = getJSON('settingStyle.json')
        homeFigure = {'data' : [go.Scattermapbox(

                lat = [],
                lon = [],
                customdata = [],
                mode = setting['panaviaHome']['homeChoropleth']['mode'],
                marker = setting['panaviaHome']['homeChoropleth']['marker'],
                selected = setting['panaviaHome']['homeChoropleth']['selected']

            )],

            'layout' : go.Layout(

                mapbox = setting['panaviaHome']['homeChoropleth']['mapbox'],
                margin = setting['panaviaHome']['homeChoropleth']['margin'],
                clickmode = setting['panaviaHome']['homeChoropleth']['clickmode']

            )

        }

        return html.Div([

            html.Div([

                html.Div([

                    dcc.Graph(id = 'graphId',
                              figure = homeFigure,
                              style = setting['panaviaHome']['graph']['style'],
                              config = setting['panaviaHome']['graph']['config'])

                ], style = setting['panaviaHome']['style'])

            ], style = setting['panaviaContent'])

        ])


def panaviaCreate(arg):
    '''  '''

    if (arg == 'createValue'):

        return html.Div([

            html.H1('create')

        ], style = setting['panaviaContent'])


def panaviaOpen(arg):
    '''  '''

    if (arg == 'openValue'):

        return html.Div([

            html.H1('open')

        ], style = setting['panaviaContent'])


if (__name__ == '__main__'):

    app.run_server()
