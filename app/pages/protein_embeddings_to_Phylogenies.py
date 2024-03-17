#This is a page detailing my work on making Phylogenies fromm Protein embeddings
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Protein_embeddings_to_Phylogenies")
#-----------------------------------------------------------
layout = (
    html.Div(
        style={"display": "flex", "justify-content": "center"},
        children=[
            html.H1("Protein_embeddings_to_Phylogenies"),
            
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