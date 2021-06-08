import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from Panavia import app, setGraph, getGraph, getStyle, getCenter


style = getStyle('Home')
homeLayout = html.Div([

    html.Div([

        html.Div([

            dcc.Dropdown(id = 'homeDropdownId',
                         placeholder = 'Search Wheel',
                         style = style['dropdownStyle'],
                         options = [{'label' : i['Title'],
                                     'value' : i['Title']}

                                    for i in list(getGraph().values())[1:]])

        ], style = style['divDivStyle'])

    ], style = style['divStyle']),

    html.Div([

        dcc.Graph(id = 'homeGraphId',
                  style = style['graphStyle'],
                  config = style['graphConfig'])

    ], style = style['divStyle']),

    html.Div([

        html.Div([

            html.Button(children = 'Submit',
                        id = 'homeButtonIdA',
                        style = style['buttonStyleA']),

            html.Button(id = 'homeButtonIdB',
                        style = style['buttonStyleB'])

        ], style = style['divDivStyle'])

    ], style = style['divStyle'])

])


@app.callback(Output('homeGraphId', 'figure'),
              Input('homeDropdownId', 'value'))
def dropdownFunction(arg):
    '''  '''

    graph = getGraph()

    if (arg):

        layoutMapbox = style['layoutMapbox']
        layoutMapbox['center'] = {'lat' : graph[arg]['lat'],
                                  'lon' : graph[arg]['lon']}

    else:

        mapboxCenter = getCenter()
        layoutMapbox = style['layoutMapbox']
        layoutMapbox['center'] = {'lat' : mapboxCenter[0],
                                  'lon' : mapboxCenter[1]}

    return {'data' : [go.Scattermapbox(

            hoverinfo = 'text',
            mode = style['dataMode'],
            marker = style['dataMarker'],
            selected = style['dataSelected'],
            lat = [i['lat'] for i in graph.values()],
            lon = [i['lon'] for i in graph.values()],
            hovertext = [i['Title'] for i in graph.values()],
            customdata = [i['Title'] for i in graph.values()])

        ],

        'layout' : go.Layout(

            clickmode = style['layoutClickmode'],
            margin = style['layoutMargin'],
            mapbox = layoutMapbox,
            uirevision= 'foo')

    }


@app.callback(Output('homeDropdownId', 'value'),
              Input('homeGraphId', 'clickData'))
def graphFunction(arg):
    '''  '''

    if (arg):

        return arg['points'][0]['customdata']


@app.callback(Output('homeButtonIdB', 'children'),
              Output('homeDropdownId', 'options'),
              Input('homeButtonIdA', 'n_clicks'),
              State('homeDropdownId', 'value'))
def buttonFunction(*args):
    '''  '''

    try:

        graph = getGraph()

        if (args[0]):

            graph['Recent'] = graph[args[1]]
            setGraph(graph)

        return (getGraph()['Recent']['Title'],
                [{'label' : i['Title'],
                  'value' : i['Title']}

                 for i in list(getGraph().values())[1:]])

    except:

        return None
