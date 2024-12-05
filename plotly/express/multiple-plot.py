import numpy as np
import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px

df = pd.DataFrame(data=np.random.normal(size=(100,5)).cumsum(0), columns=['A', 'B', 'C', 'D', 'E'], index=pd.date_range(end='00:00:00', periods=100, freq='B').rename('Date')).reset_index()
fig = px.line(df, x='Date', y=['A', 'B', 'C', 'D', 'E'])

app = dash.Dash(__name__)
app.title = "TITLE"
app.layout = dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run_server(debug=True)
