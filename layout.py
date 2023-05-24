from dash import Dash, dcc, html
from dash.html import Div, H1, H4, Header
import dash_bootstrap_components as dbc


class Layout:
    def __init__(self) -> None:
        print("loading layout")

    def layout(self):
        return dbc.Container(
            [
                Header(H4("Web-Scraper"))
            ], class_name= "main-container"
        )
