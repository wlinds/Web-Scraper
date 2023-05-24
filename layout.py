from dash import Dash, html, dcc

class Layout:

    def __init__(self) -> None:

        print("loading layout")

    def layout(self):

        return html.H1("Hello World")