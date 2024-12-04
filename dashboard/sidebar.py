import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "TITLE"
sidebar = html.Div([html.H2(html.A("PROJECT", href="/"), className="display-4"),
                    html.Hr(),
                    html.P("description", className="lead"),
                    dbc.Nav([dbc.NavLink("Page 1", href="/page1", id="page1"),
                             dbc.NavLink("Page 2", href="/page2", id="page2"),
                             dbc.NavLink("Page 3", href="/page3", id="page3")], vertical=True, pills=True)])
content = html.Div(id="page-content")
main = dbc.Row([dbc.Col(sidebar, width=2), dbc.Col(content, width=10)])
app.layout = html.Div([dcc.Location(id="url"), main])

contents = {}
contents['root'] = html.Div('Root Page')
contents['page1'] = html.Div('Page 1')
contents['page2'] = html.Div('Page 2')
contents['page3'] = html.Div('Page 3')

@app.callback([Output(f"page{i}", "active") for i in range(1, 4)],
              Input("url", "pathname"))
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False
    return [pathname == f"/page{i}" for i in range(1, 4)]

@app.callback(Output("page-content", "children"),
              Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/" : return contents['root']
    elif pathname == "/page1" : return contents['page1']
    elif pathname == "/page2" : return contents['page2']
    elif pathname == "/page3" : return contents['page3']
    return dbc.Jumbotron([html.H1("404: Not found", className="text-danger"),
                          html.Hr(),
                          html.P(f"The pathname {pathname} was not recognised...")])

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)


