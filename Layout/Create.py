# Import <
import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from Panavia import app, setGraph, getGraph, getStyle, getCenter

# >


# UI <
style = getStyle('Create')
createLayout = html.Div([

    # Error Message <
    dcc.ConfirmDialog(id = 'createConfirmdialogId',
                      message = 'Wheel already exists.'),

    # >

    # Input <
    html.Div([

        # Title <
        html.Div([

            dcc.Input(id = 'createInputId',
                      placeholder = 'Wheel Name',
                      style = style['inputStyle']),

        ]),

        # >

        # Description <
        html.Div([

            dcc.Textarea(id = 'createTextareaId',
                         style = style['textareaStyle'],
                         placeholder = 'Wheel Description')

        ])

        # >

    ], style = style['divStyle']),

    # >


    html.Div([

        html.Div([

            # DataTable <
            dt.DataTable(editable = True,
                         id = 'createDatatableId',
                         style_cell = style['datatableStyle_cell'],
                         style_header = style['datatableStyle_header'],
                         data = [{j : None for j in style['wheelSpeed']} for i in style['wheelSpeed']],
                         columns = [{'name' : str(i),
                                     'id' : str(i)}

                                    for i in style['wheelSpeed']])

            # >

        ], style = style['divDivStyle'])

    ], style = style['divStyle']),

    html.Div([

        html.Div([

            # Submit <
            html.Button(children = 'Submit',
                        id = 'createButtonIdA',
                        style = style['buttonStyleA']),

            # >

            # Current <
            html.Button(id = 'createButtonIdB',
                        style = style['buttonStyleB'])

            # >

        ], style = style['divDivStyle'])

    ], style = style['divStyle'])

])

# >


@app.callback(Output('createConfirmdialogId', 'displayed'),
              Output('createButtonIdB', 'children'),
              Input('createButtonIdA', 'n_clicks'),
              State('createDatatableId', 'data'),
              State('createTextareaId', 'value'),
              State('createInputId', 'value'))
def buttonFunction(*args):
    '''  '''

    try:

        if (args[3]):

            if (args[3] in getGraph().keys()):

                return (True, getGraph()['Recent']['Title'])

            dictVariable = {}
            graph = getGraph()
            lat, lon = getCenter()
            dictVariable['lat'] = lat
            dictVariable['lon'] = lon
            dictVariable['Data'] = args[1]
            dictVariable['Title'] = args[3]
            dictVariable['Description'] = args[2]

            graph['Recent'] = dictVariable
            graph[args[3]] = dictVariable
            setGraph(graph)

        return (False, getGraph()['Recent']['Title'])

    except:

        return (False, None)
