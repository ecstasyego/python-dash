import dash
from dash import html, dcc                                                                                                                                             from dash import Input, Output                                                                                                                                         import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
app.title = "TITLE"
app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Slider(
        id='input-slider',
        min=0,
        max=10,
        step=1,
        value=5
    ),
])

@app.callback(
    Output('graph', 'figure'),
    [Input('input-slider', 'value')]
)
def update_graph(slider_value):
    return go.Figure(
        data=[go.Bar(x=[1, 2, 3], y=[slider_value, slider_value + 1, slider_value + 2])],
        layout=go.Layout(title=f'Bar Chart - Slider Value: {slider_value}')
    )

if __name__ == '__main__':
    app.run_server(debug=True)
