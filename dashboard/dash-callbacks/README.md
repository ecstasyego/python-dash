- https://dash.plotly.com/basic-callbacks

```python
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "TITLE"

# CONTENTS
main = html.Div([html.H2(html.A("PROJECT", href="/")),
                 html.H6('description'),
                 html.Hr(),
                 dcc.Markdown("Hello, World!"),
                 ])
app.layout = html.Div([dcc.Location(id="url"), main])

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)
```


## API Reference
- [https://github.com/ecstasyego/python-dash/tree/main/dashboard/bootstrap-components](https://github.com/ecstasyego/python-dash/blob/main/dashboard/core-components/README.md)
- [https://github.com/ecstasyego/python-dash/tree/main/dashboard/html-components](https://github.com/ecstasyego/python-dash/blob/main/dashboard/html-components/README.md)
- [https://github.com/ecstasyego/python-dash/blob/main/dashboard/bootstrap-components](https://github.com/ecstasyego/python-dash/blob/main/dashboard/bootstrap-components/README.md)

