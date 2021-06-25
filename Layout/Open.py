import dash_table as dt
import plotly.express as px
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots
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

        # graph 1
        html.Div([

            dcc.Graph(id = 'openGraphIdA')

        ], style = style['divDivStyle']),

        # graph 2
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
def datatableFunctionA(arg):
    '''  '''

    dictVariable, style = {}, getStyle('Open')
    for key, value in [[k, v] for i in arg for k, v in i.items() if (v)]:

        if (key not in dictVariable.keys()):

            dictVariable[key] = [[], []]

        dictVariable[key][0].append(value)
        dictVariable[key][1].append(dictVariable[key][0].count(value))

    figure = make_subplots(rows = 1,
                           shared_yaxes = True,
                           horizontal_spacing = 0.001,
                           cols = len(dictVariable.keys()),
                           subplot_titles = tuple(dictVariable.keys()))

    # TODO:
    # so the problem we're now having is the wheel speeds are printing in sorted order.
    # we need to use json wheelSpeed variable to iterate through and put them in order.

    # x-axis : wheel speeds
    # y-axis : 0-37

    # so this is currently putting them in order- although the data is correct
    for c, i in enumerate(dictVariable.keys()):

        figure.add_trace(go.Scatter(

            mode = 'markers',
            x = dictVariable[i][1],
            y = dictVariable[i][0],
            marker = style['markerStyle']),

        col = (c + 1),
        row = 1)

    figure.update_layout(

        showlegend = False)

    return figure