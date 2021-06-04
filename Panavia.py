# Panavia by Alex Arbuckle #


import dash
import dash_table
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from panaviaFunction.functionGetJSON import getJSON
from panaviaFunction.functionSetJSON import setJSON
from panaviaFunction.functionGetLocation import getLocation


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


@app.callback(Output('menuContent', 'children'),
              Input('menuId', 'value'))
def menuFunction(arg):
    '''  '''

    return {'homeValue' : panaviaHome(arg), 'createValue' : panaviaCreate(arg), 'openValue' : panaviaOpen(arg)}[arg]


def panaviaHome(arg):
    '''  '''

    if (arg == 'homeValue'):

        figure = getJSON('settingFigure.json')
        setting = getJSON('settingStyle.json')
        return html.Div([

            html.Div([

                html.Div([

                    dcc.Dropdown(id = 'dropdownId',
                                 placeholder = 'Select Wheel',
                                 style = setting['panaviaHome']['homeDropdown'],
                                 options = [{'label' : i, 'value' : i} for i in list(figure)[1:]])

                ], style = setting['panaviaHome']['style'])

            ], style = setting['panaviaContent']),

            html.Div([

                html.Div([

                    dcc.Graph(id = 'graphId',
                              style = setting['panaviaHome']['homeGraph']['style'],
                              config = setting['panaviaHome']['homeGraph']['config'])

                ], style = setting['panaviaHome']['style'])

            ], style = setting['panaviaContent']),

            html.Div([

                html.Div([

                    html.Button(id = 'homeButtonId',
                                children = 'Submit',
                                style = setting['panaviaHome']['homeButton']),

                    html.Button(children = '',
                                id = 'homeResponseId',
                                style = setting['panaviaHome']['homeResponse'])

                ])

            ], style= setting['panaviaContent'])

        ])


@app.callback(Output('graphId', 'figure'),
              Input('dropdownId', 'value'))
def homeFunction(arg):
    '''  '''

    figure = getJSON('settingFigure.json')
    setting = getJSON('settingStyle.json')
    arg = 'Recent' if (arg is None) else (arg)
    return {'data' : [go.Scattermapbox(

        lat = [],
        lon = [],
        customdata = [],
        mode = setting['panaviaHome']['homeFigure']['mode'],
        marker = setting['panaviaHome']['homeFigure']['marker'],
        selected = setting['panaviaHome']['homeFigure']['selected']

        )],

        'layout' : go.Layout(

            mapbox = setting['panaviaHome']['homeFigure']['mapbox'],
            margin = setting['panaviaHome']['homeFigure']['margin'],
            clickmode = setting['panaviaHome']['homeFigure']['clickmode']

        ),

    }


@app.callback(Output('homeResponseId', 'children'),
              Input('homeButtonId', 'n_clicks'),
              State('dropdownId', 'value'))
def responseFunction(*args):
    '''  '''

    figure = getJSON('settingFigure.json')

    if (args[0]):

        figure['Recent'] = figure[args[1]]
        setJSON(figure)

        return figure['Recent']['a']

    return figure['Recent']['a']


def panaviaCreate(arg):
    '''  '''

    if (arg == 'createValue'):

        figure = getJSON('settingFigure.json')
        setting = getJSON('settingStyle.json')
        return html.Div([

            html.Div([

                html.Div([

                    dcc.Input(value = '',
                              type = 'text',
                              id = 'inputId',
                              placeholder = 'Wheel Name',
                              style = setting['panaviaCreate']['createInput'])

                ]),

                html.Div([

                    dcc.Textarea(value = '',
                                 id = 'textareaId',
                                 placeholder = 'Wheel Description',
                                 style = setting['panaviaCreate']['createTextarea'])

                ])

            ], style = setting['panaviaContent']),

            html.Div([

                html.Div([

                    dash_table.DataTable(editable = True,
                                         id = 'dataTableId',
                                         style_cell = setting['panaviaCreate']['createDataTable']['style_cell'],
                                         style_header = setting['panaviaCreate']['createDataTable']['style_header'],
                                         columns = [{'name' : str(i), 'id' : str(i)} for i in setting['wheelSpeed']],
                                         data = [{j : None for j in setting['wheelSpeed']} for i in setting['wheelSpeed']])

                    ], style = setting['panaviaCreate']['createDataTable']['style'])

            ], style = setting['panaviaContent']),

            html.Div([

                html.Div([

                    html.Button(children = 'Submit',
                                id = 'createButtonId',
                                style = setting['panaviaCreate']['createButton']),

                    html.Button(disabled = True,
                                id = 'createResponseId',
                                children = '',
                                style = setting['panaviaCreate']['createResponse'])

                ])

            ], style = setting['panaviaContent'])

        ])


@app.callback(Output('createResponseId', 'children'),
              Input('createButtonId', 'n_clicks'),
              State('textareaId', 'value'),
              State('inputId', 'value'))
def functionResponse(*args):
    '''  '''

    print(args)

    return 'ok'

def panaviaOpen(arg):
    '''  '''

    if (arg == 'openValue'):

        return html.Div([

            html.H1('open')

        ], style = setting['panaviaContent'])


if (__name__ == '__main__'):

    app.run_server(port = 8888)
