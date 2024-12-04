
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
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/

```python
import dash_bootstrap_components as dbc
help(dbc.Nav)
```

- Nav(children=None, id=undefined, style=undefined, class_name=undefined, className=undefined, key=undefined, pills=undefined, card=undefined, fill=undefined, justified=undefined, vertical=undefined, horizontal=undefined, navbar=undefined, navbar_scroll=undefined, loading_state=undefined, **kwargs)
- Button(children=None, id=undefined, class_name=undefined, className=undefined, style=undefined, key=undefined, href=undefined, external_link=undefined, n_clicks=undefined, n_clicks_timestamp=undefined, active=undefined, color=undefined, disabled=undefined, size=undefined, title=undefined, outline=undefined, loading_state=undefined, target=undefined, type=undefined, download=undefined, name=undefined, value=undefined, rel=undefined, **kwargs)
- Alert(children=None, id=undefined, style=undefined, class_name=undefined, className=undefined, key=undefined, color=undefined, is_open=undefined, fade=undefined, dismissable=undefined, duration=undefined, loading_state=undefined, persistence=undefined, persisted_props=undefined, persistence_type=undefined, **kwargs)
