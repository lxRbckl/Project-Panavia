# Panavia by Alex Arbuckle #


import dash
from json import dump, load
#from panaviaHome import home
#from panaviaLoad import load
#from panaviaCreate import create
import plotly.figure_factory as ff
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def setJSON(arg):
    '''  '''

    with open('panaviaData.json', 'w') as fileVariable:

        dump(fileVariable, arg, indent = 4)


def getJSON(arg):
    '''  '''

    with open(arg, 'r') as fileVariable:

        return load(fileVariable)


app = dash.Dash()
settings = getJSON('panaviaSettings.json')
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

                     dcc.Tab(label = 'Load',
                             value = 'load',
                             style = settings['headerTabOff'],
                             selected_style = settings['headerTabOn'])

                 ])

    ], style = settings['panaviaMenu']),

    html.Div(id = 'content')

])


@app.callback(Output('content', 'children'), Input('menu', 'value'))
def contentFunction(tab):
    '''  '''

    return {'home' : home(), 'create' : create(), 'load' : load()}[tab]


if (__name__ == '__main__'):

    app.run_server()
