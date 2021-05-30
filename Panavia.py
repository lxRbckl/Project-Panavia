# Panavia by Alex Arbuckle #
# pk.eyJ1IjoiZ2VybXg1MDAwIiwiYSI6ImNrcGJldzBlaDBwdHcydnBlemxpdWpvNGgifQ.UQpx7nqlgc1KS9f8YCY-dQ


import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from panaviaFunctions.functionsGetJSON import getJSON
from panaviaFunctions.functionsSetJSON import setJSON

app = dash.Dash()
settings = getJSON('settingsStyle.json')
app.layout = html.Div([

    html.Div([

        html.H1('Panavia', style = settings['panaviaHeader']),

        dcc.Tabs(id = 'menu',
                 value = 'home',
                 children = [

                     dcc.Tab(label = 'Home',
                             value = 'home',
                             style = settings['headerTabOff'],
                             selected_style = settings['headerTabOn']),

                     dcc.Tab(label = 'Create',
                             value = 'create',
                             style = settings['headerTabOff'],
                             selected_style = settings['headerTabOn']),

                     dcc.Tab(label = 'Open',
                             value = 'open',
                             style = settings['headerTabOff'],
                             selected_style = settings['headerTabOn'])

                 ])

    ], style = settings['panaviaMenu']),

    html.Div(id = 'tab')

])


@app.callback(Output('tab', 'children'), Input('menu', 'value'))
def tabFunction(tab):
    '''  '''

    return {'home' : tabHome(tab), 'create' : tabCreate(tab), 'open' : tabOpen(tab)}[tab]


def tabHome(tab):
    '''  '''

    if (tab == 'home'):

        homeMap = {

            'data' : [go.Scattermapbox(

                lat = [40.80105],
                lon = [-73.945155],
                mode = 'markers',
                customdata = ['ok'],
                marker = {'opacity' : 0.5, 'size' : 10},
                selected = {'marker' : {'opacity' : 1,
                                        'size' : 15}},
            )],

            'layout' : go.Layout(

                clickmode = 'event+select',
                margin = {'r' : 0, 't' : 0, 'l' : 0, 'b' : 0},
                mapbox = {'accesstoken' : settings['mapToken'],
                          'style' : 'dark',
                          'zoom' : 10,
                          'pitch' : 30,
                          'center' : {'lat' : 40.80105,
                                      'lon' : -73.945155

                                      }

                          }

            )

        }

        return html.Div([

            html.Div([

                dcc.Graph(id = 'homeMap',
                          figure = homeMap,
                          config = {'displayModeBar' : False},
                          style = {'borderRadius' : 5})

            ], style = settings['homeMap']),

            html.H1(id = 'opsen')

        ], style = settings['panaviaTab'])


@app.callback(Output('opsen', 'children'), Input('homeMap', 'selectedData'))
def display_click_data(clickdata):
    '''  '''

    print(clickdata)
    return clickdata


def tabCreate(tab):
    '''  '''

    if (tab == 'create'):

        return html.Div([

            html.H1('create')

        ], style = settings['panaviaTab'])


def tabOpen(tab):
    '''  '''

    if (tab == 'open'):

        return html.Div([

            html.H1('load')

        ], style = settings['panaviaTab'])


if (__name__ == '__main__'):

    app.run_server()
