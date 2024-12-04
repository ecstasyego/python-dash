################################## CONFIG ##################################
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from plotly.subplots import make_subplots
import plotly.graph_objs as go
config = {}
config['dash-server'] = '127.0.0.1'
config['dash-port'] = '8050'
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "TITLE"
################################## CONFIG ##################################
################################## CODEBLOCK ##################################





# O[T,0,0] : Figure
fig = make_subplots(rows=1, cols=1, subplot_titles=['TITLE'])
fig.add_trace(go.Scatter(x=[1,2,3], y=[3,2,1], mode='lines+markers'), row=1, col=1)
# O[T,0,1] : Description
description1 = "Description"
# O[T,1,0] : Description
description2 = "Description"
# O[T,1,1] : Description
description3 = "Description"





################################## CODEBLOCK ##################################
################################## DASHBOARD ##################################
O = {}
O['T,_,_'] = None
O['T,0,0'] = dcc.Graph(figure=fig)
O['T,0,1'] = dcc.Markdown(description1)
O['T,1,0'] = dcc.Markdown(description2)
O['T,1,1'] = dcc.Markdown(description3)
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader('T,0,0'), dbc.CardBody(O['T,0,0'])], color='light', inverse=False, outline=True)]
C['T,0,1'] = [dbc.Card([dbc.CardHeader('T,0,1'), dbc.CardBody(O['T,0,1'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader('T,1,0'), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
C['T,1,1'] = [dbc.Card([dbc.CardHeader('T,1,1'), dbc.CardBody(O['T,1,1'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab'] = [dbc.Row([dbc.Col(C['T,0,0'], width=6), dbc.Col(C['T,0,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="PAGE1", disabled=False)])
main = html.Div([html.H2(html.A('PROJECT', href="/")),
                 html.H6('description'),
                 html.Div([dbc.Button("TASK", color="secondary", href='https://github.com/ailever/ailever/wiki')]),
                 html.Br()])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
