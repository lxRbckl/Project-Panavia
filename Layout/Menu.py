# Import <
from Home import homeLayout
from Open import openLayout
from Create import createLayout
from Panavia import app, getStyle
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# >


# UI <
style = getStyle('Menu')
app.layout = html.Div([

    html.Div([

        # Header <
        html.H1('Panavia', style = style['h1Style']),

        # >

        # Tabs <
        dcc.Tabs(value = 'Home',
                 id = 'menuTabsId',
                 children = [

                     dcc.Tab(label = i,
                             value = i,
                             style = style['tabStyle'],
                             selected_style = style['tabSelected_style'])

                 for i in ['Home', 'Create', 'Open']

                 ])

        # >

    ], style = style['divStyle']),

    # Responsive UI <
    html.Div(id = 'menuDivId')

    # >

])

# >


@app.callback(Output('menuDivId', 'children'),
              Input('menuTabsId', 'value'))
def tabsFunction(arg):
    '''  '''

    return {'Home' : homeLayout,
            'Open' : openLayout,
            'Create' : createLayout}[arg]


if (__name__ == '__main__'):

    app.run_server(debug = True)
