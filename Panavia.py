# Panavia by Alex Arbuckle #


from panaviaTabs.tabsHome import homeFunction
from panaviaTabs.tabsOpen import openFunction
from panaviaTabs.tabsCreate import createFunction
from panaviaFunctions.functionsGetJSON import getJSON

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


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

    return {'home' : homeFunction(), 'create' : createFunction(), 'open' : openFunction()}[tab]


if (__name__ == '__main__'):

    app.run_server()
