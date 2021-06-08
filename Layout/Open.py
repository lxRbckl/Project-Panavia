import dash_table as dt
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from Panavia import app, setGraph, getGraph, getStyle


style = getStyle('Open')
openLayout = html.Div([

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
                         id = 'openDatatableId',
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

    ], style = style['divStyle'])

])


@app.callback(Output('openInputId', 'value'),
              Output('openTextareaId', 'value'),
              Output('openDatatableId', 'data'),
              Output('openButtonIdB', 'children'),
              Input('openButtonIdA', 'n_clicks'),
              State('openInputId', 'value'),
              State('openTextareaId', 'value'),
              State('openDatatableId', 'data'))
def buttonFunction(*args):
    '''  '''

    try:

        if (args[0]):

            dictVariable = {}
            graph = getGraph()
            dictVariable['Data'] = args[3]
            dictVariable['Title'] = args[1]
            dictVariable['Description'] = args[2]
            dictVariable['lat'] = graph['Recent']['lat']
            dictVariable['lon'] = graph['Recent']['lon']

            graph[graph['Recent']['Title']] = dictVariable
            graph['Recent'] = dictVariable
            setGraph(graph)

        graph = getGraph()
        return (graph['Recent']['Title'],
                graph['Recent']['Description'],
                graph['Recent']['Data'],
                graph['Recent']['Title'])

    except:

        return (None, None, None, None)