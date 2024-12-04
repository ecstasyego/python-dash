## Installation

```bash
$ pip install dash
$ pip install dash_bootstrap_components
```

```python
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
app.title = "TITLE"
app.layout = dcc.Markdown("Hello, World!")

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)
```
