- https://dash.plotly.com/dash-html-components

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
```python
import dash
help(dash.html.Div)
```

- Div(children=None, id=undefined, n_clicks=undefined, n_clicks_timestamp=undefined, disable_n_clicks=undefined, key=undefined, accessKey=undefined, className=undefined, contentEditable=undefined, dir=undefined, draggable=undefined, hidden=undefined, lang=undefined, role=undefined, spellCheck=undefined, style=undefined, tabIndex=undefined, title=undefined, loading_state=undefined, **kwargs)
- P(children=None, id=undefined, n_clicks=undefined, n_clicks_timestamp=undefined, disable_n_clicks=undefined, key=undefined, accessKey=undefined, className=undefined, contentEditable=undefined, dir=undefined, draggable=undefined, hidden=undefined, lang=undefined, role=undefined, spellCheck=undefined, style=undefined, tabIndex=undefined, title=undefined, loading_state=undefined, **kwargs)
- H2(children=None, id=undefined, n_clicks=undefined, n_clicks_timestamp=undefined, disable_n_clicks=undefined, key=undefined, accessKey=undefined, className=undefined, contentEditable=undefined, dir=undefined, draggable=undefined, hidden=undefined, lang=undefined, role=undefined, spellCheck=undefined, style=undefined, tabIndex=undefined, title=undefined, loading_state=undefined, **kwargs)
- Hr(children=None, id=undefined, n_clicks=undefined, n_clicks_timestamp=undefined, disable_n_clicks=undefined, key=undefined, accessKey=undefined, className=undefined, contentEditable=undefined, dir=undefined, draggable=undefined, hidden=undefined, lang=undefined, role=undefined, spellCheck=undefined, style=undefined, tabIndex=undefined, title=undefined, loading_state=undefined, **kwargs)


