#This is a page detailing my work on making Phylogenies fromm Protein embeddings
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Masters_Thesis")
#-----------------------------------------------------------
layout = (
    html.Div(
        style={"display": "flex", "justify-content": "center"},
        children=[
            html.H1("Masters_Thesis"),
            
            dbc.Card(
                dbc.CardBody(
                    dcc.Markdown('''
                                 Project Description ...\n
                                 Coming soon...\n
                                 link to Paper\n
                                 link to github\n
                                 '''),
                ),
                style={"width": "60%"},
            ),
        ]
    )
)
#-----------------------------------------------------------