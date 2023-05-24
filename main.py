from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from layout import Layout


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    meta_tags=[dict(name="viewport", content="width=device-width, initial-scale=1.0")],
)

app.layout = Layout().layout()

if __name__ == "__main__":
    app.run_server(debug=True)
