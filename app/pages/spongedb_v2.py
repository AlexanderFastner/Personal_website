#This is a page detailing my work on SpongeDB_v2
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/SpongeDB_v2")
#-----------------------------------------------------------
layout = (
    html.Div(
        style={"display": "flex", "justify-content": "center"},
        children=[
            html.H1("SpongeDB_v2"),
            
            dbc.Card(
                dbc.CardBody(
                    dcc.Markdown('''
                                 Project Description ...\n
                                 link to github\n
                                 '''),
                ),
                style={"width": "60%"},
            ),
        ]
    )
)
#-----------------------------------------------------------