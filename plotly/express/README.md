
```python
import numpy as np
import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px

df = pd.DataFrame({'Date':pd.date_range(end='00:00:00', periods=100, freq='B'), 'Value':np.random.normal(size=100).cumsum()})
fig = px.line(df, x='Date', y='Value')

app = dash.Dash(__name__)
app.title = "TITLE"
app.layout = dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run_server(debug=True)
```
