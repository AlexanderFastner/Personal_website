#This is the main landing page of my Website
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#----------------------------------------------------------
dash.register_page(__name__, path="/")
#-----------------------------------------------------------

#-----------------------------------------------------------
#Cards 
About_Me_Card = dbc.Card(
    dbc.CardBody(
        dcc.Markdown('''
                        # About  Me:
                        ...\n
                        ...\n
                        '''),
    ),
    style={"width": "50%"},
)

Bioinformatics_Projects_Card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Bioinformatics Projects"),
            dbc.ListGroup(
                [
                    #TODO add a 1 sentence summary of what each link is
                    dcc.Link(dbc.ListGroupItem("Cantata"), href="/Cantata"),
                    dcc.Link(dbc.ListGroupItem("Rosalind challenges"), href="/Rosalind_challenges"),
                    dcc.Link(dbc.ListGroupItem("Protein embeddings to Phylogenies"), href="/Protein_embeddings_to_Phylogenies"),
                    dcc.Link(dbc.ListGroupItem("DysRegNetWeb"), href="/DysRegNetWeb"),
                    dcc.Link(dbc.ListGroupItem("SpongeDB_v2"), href="/SpongeDB_v2"),
                    dcc.Link(dbc.ListGroupItem("Masters Thesis"), href="/Masters_Thesis"),
                    dcc.Link(dbc.ListGroupItem("Bachelors Thesis"), href="/Bachelors_Thesis"),
                ],
                flush=True,
            ),
            #internal link
            #dbc.CardLink("Card link", href="#"),
            #link to external sites
            #dbc.CardLink("External link", href="https://google.com"),
        ]
    ),
    style={"width": "50%"},
)

Data_Analysis_Card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Data Analysis Case studies"),
            dbc.ListGroup(
                [
                dcc.Link(dbc.ListGroupItem("Cyclistic Case Study"), href="/Cyclistic_Case_Study"),
                ]
            ),
            dcc.Markdown('''more on the way\n '''),
        ]
    ),
    style={"width": "50%"},
)

Games_Card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Games"),
            dbc.ListGroup(
                [
                dcc.Link(dbc.ListGroupItem("Othello"), href="/Othello"),
                ]
            ),
        ]
    ),
    style={"width": "50%"},
)

Random_Card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Random"),
            dbc.ListGroup(
                [
                dcc.Link(dbc.ListGroupItem("Raspberry Pi"), href="/RasPi"),
                dcc.Link(dbc.ListGroupItem("Arduino"), href="/Arduino"),
                ]
            ),
        ]
    ),
    style={"width": "50%"},
)

#TODO add link to and download CV
profile_picture = "profile_picture.png"
print(profile_picture)
import os
print(os.getcwd())
Picture_Card = dbc.Card(
    dbc.CardBody(
        [   
            html.Img(src=dash.get_asset_url(profile_picture), height="600px"),
            dbc.CardLink("Linkedin", href="https://www.linkedin.com/in/alexander-fastner/"),
            html.Br(),
            dbc.CardLink("Github", href="https://github.com/AlexanderFastner"),
            html.Br(),
            html.Plaintext("Email: alexanderfastner@gmail.com"),
        ]
    ),
    style={"width": "40%", "display": "flex"},
)

#-----------------------------------------------------------
cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        About_Me_Card,
                        Bioinformatics_Projects_Card,
                        Data_Analysis_Card,
                        Games_Card,
                        Random_Card,

                    ],
                    style={"width": "100%"},
                ),
                
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                Picture_Card,
                            ],
                            style={"justify-content": "flex-end"},
                        )
                    ],
                    style={"width": "60%"},
                ),
            ],
        )
    ]
)

#-----------------------------------------------------------
layout = (
    [
        cards
    ]
)
#-----------------------------------------------------------