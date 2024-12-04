import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "TITLE"
main = html.Div([html.H2(html.A("PROJECT", href="/")),
                 html.H6('description'),
                 html.Hr()])
topbar = dbc.Nav([dbc.NavItem(dbc.NavLink("Page1", id='page1', active=True, disabled=False, href="/page1")),
                  dbc.NavItem(dbc.NavLink("Page2", id='page2', active=False, disabled=False, href="/page2")),
                  dbc.NavItem(dbc.NavLink("Page3", id='page3', active=False, disabled=False, href="/page3")),
                  dbc.NavItem(dbc.NavLink("Page4", id='page4', active=False, disabled=False, href="/page4")),
                  dbc.NavItem(dbc.NavLink("Page5", id='page5', active=False, disabled=False, href="/page5")),
                  dbc.DropdownMenu([dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")], label="Dropdown", nav=True)], pills=True)
content = html.Div(id="page-content")
app.layout = html.Div([dcc.Location(id="url"), main, topbar, content])

contents = {}
contents['root'] = html.Div('Root Page')
contents['page1'] = html.Div('Page 1')
contents['page2'] = html.Div('Page 2')
contents['page3'] = html.Div('Page 3')
contents['page4'] = html.Div('Page 4')
contents['page5'] = html.Div('Page 5')

@app.callback([Output(f"page{i}", "active") for i in range(1, 6)],
              Input("url", "pathname"))
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False
    return [pathname == f"/page{i}" for i in range(1, 6)]

@app.callback(Output("page-content", "children"),
              Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/" : return contents['root']
    elif pathname == "/page1" : return contents['page1']
    elif pathname == "/page2" : return contents['page2']
    elif pathname == "/page3" : return contents['page3']
    elif pathname == "/page4" : return contents['page4']
    elif pathname == "/page5" : return contents['page5']
    return dbc.Jumbotron([html.H1("404: Not found", className="text-danger"),
                          html.Hr(),
                          html.P(f"The pathname {pathname} was not recognised...")])

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)
