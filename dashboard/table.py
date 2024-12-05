import dash
import dash_table
import pandas as pd
from dash import html

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

app = dash.Dash(__name__)
app.title = 'TITLE'
app.layout = html.Div([
    dash_table.DataTable(
        columns=[
            {"name": col, "id": col} for col in df.columns
        ],
        data=df.to_dict('records'),
        style_table={'height': '400px', 'overflowY': 'auto'},
        style_cell={'textAlign': 'center', 'padding': '10px'},
        style_header={'backgroundColor': 'lightblue', 'fontWeight': 'bold'},
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
