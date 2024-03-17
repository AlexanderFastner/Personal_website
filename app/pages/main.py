#This is the main landing page of my Website
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#----------------------------------------------------------
dash.register_page(__name__, path="/")
#-----------------------------------------------------------
#TODO add picture to the right with email/linkedin/github links/resume
#TODO add picture cards

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
    style={"width": "40%"},
)

Bioinformatics_Projects_Card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Bioinformatics Projects"),
            dbc.ListGroup(
                [
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
    style={"width": "40%"},
)

Data_Analysis_Card = dbc.Card(
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
)

Games_Card = dbc.Card(
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
)

Random_Card = dbc.Card(
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
)

#TODO replace this
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
Picture_Card = dbc.Card(
    dbc.CardBody(
        [
            html.H1("Picture"),
            html.Img(src=PLOTLY_LOGO, height="300px"),
        ]
    )
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
                        #upper right is picture + links
                        dbc.Row(
                            [
                                Picture_Card,
                            ]
                        )
                        #maybe add something bottom right in the future
                    ],
                    style={"width": "100%"},
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