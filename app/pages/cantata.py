#This is a page detailing my work on Cantata 
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Cantata")
#-----------------------------------------------------------
layout = (
    html.Div(
        style={"display": "flex", "justify-content": "center"},
        children=[
            html.H1("Cantata"),
            
            dbc.Card(
                dbc.CardBody(
                    dcc.Markdown('''
                                 What is this\n
                                 link to site\n
                                 link to githubs\n
                                 ...\n
                                 '''),
                ),
                style={"width": "60%"},
            ),
        ]
    )
)
#-----------------------------------------------------------