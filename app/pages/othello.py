#This is a page detailing my work on Othello
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Othello")
#-----------------------------------------------------------
layout = (
    html.Div(
        style={"display": "flex", "justify-content": "center"},
        children=[
            html.H1("Othello"),
            
            dbc.Card(
                dbc.CardBody(
                    dcc.Markdown('''
                                 Game Description ...\n
                                 Integration + download options coming soon...\n
                                 '''),
                ),
                style={"width": "60%"},
            ),
        ]
    )
)
#-----------------------------------------------------------