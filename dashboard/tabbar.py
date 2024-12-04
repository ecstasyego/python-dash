import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "TITLE"
main = html.Div([html.H2(html.A("PROJECT", href="/")),
                 html.H6('description')])
contents = {}
contents['root'] = html.Div('Root Page')
contents['tab1'] = html.Div('Page 1')
contents['tab2'] = html.Div('Page 2')
contents['tab3'] = html.Div('Page 3')
tabbar = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['tab1'])), label="Tab 1", disabled=False),
                   dbc.Tab(dbc.Card(dbc.CardBody(contents['tab2'])), label="Tab 2", disabled=False),
                   dbc.Tab(dbc.Card(dbc.CardBody(contents['tab3'])), label="Tab 3", disabled=True)])
app.layout = html.Div([dcc.Location(id="url"), main, tabbar])

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)
