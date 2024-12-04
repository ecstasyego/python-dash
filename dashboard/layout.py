import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "TITLE"


main = html.Div([html.H2(html.A("PROJECT", href="/")),
                 html.H6('description'),
                 html.Hr(),
                 html.Div([dbc.Row([dbc.Col(dcc.Markdown("## T00"), width=6), dbc.Col(dcc.Markdown("## T01"), width=6)]), html.Br(),
                           dbc.Row([dbc.Col(dcc.Markdown("## T10"), width=6), dbc.Col(dcc.Markdown("## T11"), width=6)]), html.Br(),
                           html.Br()]),
                 ])
app.layout = html.Div([dcc.Location(id="url"), main])

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)                                                                                                          
