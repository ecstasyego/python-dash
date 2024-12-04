
```python
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "TITLE"

# CONTENTS
main = html.Div([html.H2(html.A("PROJECT", href="/")),
                 html.H6('description'),
                 html.Hr(),
                 dcc.Markdown("Hello, World!"),
                 ])
app.layout = html.Div([dcc.Location(id="url"), main])

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)
```


## API Reference
https://dash.plotly.com/dash-core-components

```python
# 'Checklist', 'Clipboard', 'ConfirmDialog', 'ConfirmDialogProvider', 'DatePickerRange', 'DatePickerSingle', 'Download', 'Dropdown', 'Geolocation', 'Graph', 'Input', 'Interval', 'Link', 'Loading', 'Location', 'LogoutButton', 'Markdown', 'RadioItems', 'RangeSlider', 'Slider', 'Store', 'Tab', 'Tabs', 'Textarea', 'Tooltip', 'Upload'

import dash
help(dash.dcc.Markdown)
```

- Markdown(children=None, id=undefined, className=undefined, mathjax=undefined, dangerously_allow_html=undefined, link_target=undefined, dedent=undefined, highlight_config=undefined, loading_state=undefined, style=undefined, **kwargs)
- Link(children=None, href=required, target=undefined, refresh=undefined, title=undefined, className=undefined, style=undefined, id=undefined, loading_state=undefined, **kwargs)
- Location(id=required, pathname=undefined, search=undefined, hash=undefined, href=undefined, refresh=undefined, **kwargs)
- Tabs(children=None, id=undefined, value=undefined, className=undefined, content_className=undefined, parent_className=undefined, style=undefined, parent_style=undefined, content_style=undefined, vertical=undefined, mobile_breakpoint=undefined, colors=undefined, loading_state=undefined, persistence=undefined, persisted_props=undefined, persistence_type=undefined, **kwargs)
- Tab(children=None, id=undefined, label=undefined, value=undefined, disabled=undefined, disabled_style=undefined, disabled_className=undefined, className=undefined, selected_className=undefined, style=undefined, selected_style=undefined, loading_state=undefined, **kwargs)


