
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


## API Reference: [To Callback](https://github.com/ecstasyego/python-dash/blob/main/dashboard/dash-callbacks/README.md)
https://dash.plotly.com/dash-html-components

```python
# 'A', 'Abbr', 'Acronym', 'Address', 'Area', 'Article', 'Aside', 'Audio', 'B', 'Base', 'Basefont', 'Bdi', 'Bdo', 'Big', 'Blink', 'Blockquote', 'Br', 'Button', 'Canvas', 'Caption', 'Center', 'Cite', 'Code', 'Col', 'Colgroup', 'Content', 'Data', 'Datalist', 'Dd', 'Del', 'Details', 'Dfn', 'Dialog', 'Div', 'Dl', 'Dt', 'Em', 'Embed', 'Fieldset', 'Figcaption', 'Figure', 'Font', 'Footer', 'Form', 'Frame', 'Frameset', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Header', 'Hgroup', 'Hr', 'I', 'Iframe', 'Img', 'Ins', 'Kbd', 'Keygen', 'Label', 'Legend', 'Li', 'Link', 'Main', 'MapEl', 'Mark', 'Marquee', 'Meta', 'Meter', 'Nav', 'Nobr', 'Noscript', 'ObjectEl', 'Ol', 'Optgroup', 'Option', 'Output', 'P', 'Param', 'Picture', 'Plaintext', 'Pre', 'Progress', 'Q', 'Rb', 'Rp', 'Rt', 'Rtc', 'Ruby', 'S', 'Samp', 'Script', 'Section', 'Select', 'Shadow', 'Slot', 'Small', 'Source', 'Spacer', 'Span', 'Strike', 'Strong', 'Sub', 'Summary', 'Sup', 'Table', 'Tbody', 'Td', 'Template', 'Textarea', 'Tfoot', 'Th', 'Thead', 'Time', 'Title', 'Tr', 'Track', 'U', 'Ul', 'Var', 'Video', 'Wbr', 'Xmp'

import dash
help(dash.html.Div)
```

- Div(children=None, id=undefined, n_clicks=undefined, n_clicks_timestamp=undefined, disable_n_clicks=undefined, key=undefined, accessKey=undefined, className=undefined, contentEditable=undefined, dir=undefined, draggable=undefined, hidden=undefined, lang=undefined, role=undefined, spellCheck=undefined, style=undefined, tabIndex=undefined, title=undefined, loading_state=undefined, **kwargs)
- P(children=None, id=undefined, n_clicks=undefined, n_clicks_timestamp=undefined, disable_n_clicks=undefined, key=undefined, accessKey=undefined, className=undefined, contentEditable=undefined, dir=undefined, draggable=undefined, hidden=undefined, lang=undefined, role=undefined, spellCheck=undefined, style=undefined, tabIndex=undefined, title=undefined, loading_state=undefined, **kwargs)
- H2(children=None, id=undefined, n_clicks=undefined, n_clicks_timestamp=undefined, disable_n_clicks=undefined, key=undefined, accessKey=undefined, className=undefined, contentEditable=undefined, dir=undefined, draggable=undefined, hidden=undefined, lang=undefined, role=undefined, spellCheck=undefined, style=undefined, tabIndex=undefined, title=undefined, loading_state=undefined, **kwargs)
- Hr(children=None, id=undefined, n_clicks=undefined, n_clicks_timestamp=undefined, disable_n_clicks=undefined, key=undefined, accessKey=undefined, className=undefined, contentEditable=undefined, dir=undefined, draggable=undefined, hidden=undefined, lang=undefined, role=undefined, spellCheck=undefined, style=undefined, tabIndex=undefined, title=undefined, loading_state=undefined, **kwargs)


