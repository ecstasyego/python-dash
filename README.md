# python-dash
```
- main.py
- assets/favicon.ico
```
```python
# main.py
import dash
from dash import dcc, html

app = dash.Dash(__name__)
app.title = "APP PAGE TITLE"
app.layout = html.Div([
    html.H1("Hello, Dash!"),
    dcc.Graph(
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```
  
