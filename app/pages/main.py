#This is the main landing page of my Website
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#----------------------------------------------------------
dash.register_page(__name__, path="/")
#-----------------------------------------------------------
layout = (
    [
        #TODO add cols/rows
        #TODO add picture to the right with email/linkedin/github links/resume
        dbc.Card(
            dbc.CardBody(
                dcc.Markdown('''
                             # About  Me:
                             ...\n
                             ...\n
                             '''),
            ),
            style={"width": "40%"},
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H1("Bioinformatics Projects"),
                    dcc.Markdown('''
                                Cantata Frontend\n
                                Rosalind Challenges\n
                                Protein embeddings to Phylogenies\n
                                DysRegNetWeb\n
                                SpongeDB_v2\n 
                                Masters Thesis...\n
                                Bachelors Thesis...\n
                                '''),
                ]
            ),
            style={"width": "40%"},
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H1("Data Analysis Case studies"),
                    dcc.Markdown('''
                                Cyclistic Case Study\n
                                ... more on the way\n 
                                '''),
                ]
            ),
            style={"width": "40%"},
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H1("Games"),
                    dcc.Markdown('''
                                Othello\n
                                Hopefully some more when I find some time\n 
                                '''),
                ]
            ),
            style={"width": "40%"},
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H1("Random"),
                    dcc.Markdown('''
                                Arduino\n
                                Raspi\n 
                                '''),
                ]
            ),
            style={"width": "40%"},
        ),
    ]
)



#-----------------------------------------------------------




#-----------------------------------------------------------