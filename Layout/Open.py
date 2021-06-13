import dash_table as dt
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from Panavia import app, setGraph, getGraph, getStyle


style = getStyle('Open')
openLayout = html.Div([

    dcc.ConfirmDialog(id = 'openConfirmdialogId',
                      message = 'Wheel already exists.'),

    html.Div([

        html.Div([

            dcc.Input(id = 'openInputId',
                      style = style['inputStyle'])

        ]),

        html.Div([

            dcc.Textarea(id = 'openTextareaId',
                         style = style['textareaStyle'])

        ])

    ], style = style['divStyle']),

    html.Div([

        html.Div([

            dt.DataTable(editable = True,
                         id = 'openDatatableIdA',
                         style_cell = style['datatableStyle_cell'],
                         style_header = style['datatableStyle_header'],
                         columns = [{'name' : str(i),
                                     'id' : str(i)}

                                    for i in style['wheelSpeed']])

        ], style = style['divDivStyle'])

    ], style = style['divStyle']),

    html.Div([

        html.Div([

            html.Button(children = 'Update',
                        id = 'openButtonIdA',
                        style = style['buttonStyleA']),

            html.Button(id = 'openButtonIdB',
                        style = style['buttonStyleB'])

        ], style = style['divDivStyle'])

    ], style = style['divStyle']),

    html.Div([

        # normal
        html.Div([

            dcc.Graph(id = 'openGraphIdA')

        ], style = style['divDivStyle']),

        # polar plot with pushable rangesliders to get iterative range
        html.Div([

            dcc.Graph(id = 'openGraphIdB')

        ], style = style['divDivStyle'])

    ], style = style['divStyle'])

])


@app.callback(Output('openInputId', 'value'),
              Output('openTextareaId', 'value'),
              Output('openDatatableIdA', 'data'),
              Output('openButtonIdB', 'children'),
              Output('openConfirmdialogId', 'displayed'),
              Input('openButtonIdA', 'n_clicks'),
              State('openInputId', 'value'),
              State('openTextareaId', 'value'),
              State('openDatatableIdA', 'data'))
def buttonFunction(*args):
    '''  '''

    try:

        graph = getGraph()

        if (args[0]):

            if (args[1] in graph.keys() and graph['Recent']['Title'] != args[1]):

                return (graph['Recent']['Title'],
                        args[2],
                        args[3],
                        graph['Recent']['Title'],
                        True)

            dictVariable = {}
            dictVariable['Data'] = args[3]
            dictVariable['Title'] = args[1]
            dictVariable['Description'] = args[2]
            dictVariable['lat'] = graph['Recent']['lat']
            dictVariable['lon'] = graph['Recent']['lon']

            del graph[graph['Recent']['Title']]
            graph['Recent'] = dictVariable
            graph[args[1]] = dictVariable
            setGraph(graph)

        graph = getGraph()
        return (graph['Recent']['Title'],
                graph['Recent']['Description'],
                graph['Recent']['Data'],
                graph['Recent']['Title'],
                False)

    except:

        return (None, None, None, None, False)


@app.callback(Output('openGraphIdA', 'figure'),
              Input('openDatatableIdA', 'data'))
def datatableFunction(arg):
    '''  '''

    try:

        for row in arg:

            pass

    except:

        return None
