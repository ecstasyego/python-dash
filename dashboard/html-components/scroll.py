import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "TITLE"
sidebar = html.Div(
    children=[
        html.H2("SIDEBAR"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("MENU 0", href="#"),
                dbc.NavLink("MENU 1", href="#"),
                dbc.NavLink("MENU 2", href="#"),
                dbc.NavLink("MENU 3", href="#"),
                dbc.NavLink("MENU 4", href="#"),
                dbc.NavLink("MENU 5", href="#"),
                dbc.NavLink("MENU 6", href="#"),
                dbc.NavLink("MENU 7", href="#"),
                dbc.NavLink("MENU 8", href="#"),
                dbc.NavLink("MENU 9", href="#"),
                dbc.NavLink("MENU 10", href="#"),
                dbc.NavLink("MENU 11", href="#"),
                dbc.NavLink("MENU 12", href="#"),
                dbc.NavLink("MENU 13", href="#"),
                dbc.NavLink("MENU 14", href="#"),
                dbc.NavLink("MENU 15", href="#"),
                dbc.NavLink("MENU 16", href="#"),
                dbc.NavLink("MENU 17", href="#"),
                dbc.NavLink("MENU 18", href="#"),
                dbc.NavLink("MENU 19", href="#"),
                dbc.NavLink("MENU 20", href="#"),
                dbc.NavLink("MENU 21", href="#"),
                dbc.NavLink("MENU 22", href="#"),
                dbc.NavLink("MENU 23", href="#"),
                dbc.NavLink("MENU 24", href="#"),
                dbc.NavLink("MENU 25", href="#"),
                dbc.NavLink("MENU 26", href="#"),
                dbc.NavLink("MENU 27", href="#"),
                dbc.NavLink("MENU 28", href="#"),
                dbc.NavLink("MENU 29", href="#"),
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
