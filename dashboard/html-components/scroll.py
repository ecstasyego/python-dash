import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

sidebar = html.Div(
    children=[
        html.H2("SIDEBAR"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("MENU 1", href="#"),
                dbc.NavLink("MENU 2", href="#"),
                dbc.NavLink("MENU 3", href="#"),
                dbc.NavLink("MENU 4", href="#"),
                dbc.NavLink("MENU 5", href="#"),
                dbc.NavLink("MENU 6", href="#"),
                dbc.NavLink("MENU 7", href="#"),
                dbc.NavLink("MENU 8", href="#"),
                dbc.NavLink("MENU 9", href="#"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "position": "fixed",
        "width": "250px",
        "height": "100vh",
        "overflowY": "auto", # scroll
    },
)

content = html.Div(children=[html.H1("CONTENT"), html.P("description")], style={"marginLeft": "270px", "padding": "20px"})

app.layout = html.Div([sidebar, content])

if __name__ == '__main__':
    app.run_server(debug=True)
