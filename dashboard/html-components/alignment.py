import dash
from dash import html

app = dash.Dash(__name__)
app.title = "TITLE"
app.layout = html.Div(
    children = [
        html.Div("A", style={'display':'inline-block', 'width':'30%'}),
        html.Div("B", style={'display':'inline-block', 'width':'30%'}),
        html.Div("C", style={'display':'inline-block', 'width':'30%'})
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)                                                                                                                                         
