import dash
import pandas as pd
from dash import html, dcc
import plotly.graph_objs as go

df = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Value': [10, 12, 15, 18, 17, 20, 22, 25, 28, 30]
})

app = dash.Dash(__name__)
app.title = 'TITLE'
app.layout = html.Div(children=[
    dcc.Graph(
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Value'],
                    mode='lines+markers',
                    name='Value'
                )
            ],
            'layout': go.Layout(
                title='Date vs Value',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Value'}
            )
        }
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)
