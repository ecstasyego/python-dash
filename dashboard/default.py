import dash
from dash import dcc, html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
app.layout = dcc.Markdown('''
## TITLE
- contents 1
- contents 2
''')

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)
