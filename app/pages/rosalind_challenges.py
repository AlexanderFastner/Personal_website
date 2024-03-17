#This is a page detailing Rosaling problems
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Rosalind_challenges")
#-----------------------------------------------------------
layout = (
    html.Div(
        style={"display": "flex", "justify-content": "center"},
        children=[
            html.H1("Rosalind challenges"),
            
            dbc.Card(
                dbc.CardBody(
                    dcc.Markdown('''
                                 What are they?\n
                                 My progress:\n
                                 link to github\n
                                 ...\n
                                 '''),
                ),
                style={"width": "60%"},
            ),
        ]
    )
)


#-----------------------------------------------------------
