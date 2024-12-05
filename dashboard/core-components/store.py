import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Button('Set Data', id='set-button'),
    html.Button('Get Data', id='get-button'),
    html.Div(id='output-data'),    
    dcc.Store(id='data-store', storage_type=['memory', 'session', 'local'][0]) 
])

@app.callback(
    Output('data-store', 'data'),
    Input('set-button', 'n_clicks'),
    prevent_initial_call=True
)
def store_data(n_clicks):
    return {'message': 'Hello, Dash!'}

@app.callback(
    Output('output-data', 'children'),
    Input('data-store', 'data'),
    prevent_initial_call=True
)
def display_data(data):
    if data is not None:
        return f"Stored Data: {data['message']}"
    return "No Data Stored"

if __name__ == '__main__':
    app.run_server(debug=True)
