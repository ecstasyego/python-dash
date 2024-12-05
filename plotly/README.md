
- https://plotly.com/python-api-reference/
- https://plotly.com/python/reference/index/
- https://plotly.com/python/


```python
import dash
from dash import dcc, html
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[10, 11, 12])],
    layout=go.Layout(title='Plotly Bar Chart Example')
)

app = dash.Dash(__name__)
app.title = "TITLE"
app.layout = dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run_server(debug=True)
```
