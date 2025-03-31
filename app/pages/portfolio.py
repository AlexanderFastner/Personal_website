#This is my portfolio page
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/portfolio")
#-----------------------------------------------------------
DNA_graphic = "general/DNA_graphic.png"

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
    style={"width": "100%"},
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
    style={"width": "100%"},
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
    style={"width": "100%"},
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
    style={"width": "100%"},
)

banner = dbc.Col(
    [
        html.Img(src=dash.get_asset_url(DNA_graphic), height="1400px"),
    ]
),

#-----------------------------------------------------------
cards = html.Div(
    [
        dbc.Col(
            [
                #Overview
                #mention that its mine
                Bioinformatics_Projects_Card,
                Data_Analysis_Card,
                Games_Card,
                Random_Card,
            ],
            # style={"width": "100%", "margin-left": "5rem"},
        ),
    ]
)
#-----------------------------------------------------------
layout = (
    [
        dbc.Row(
            [
                dbc.Col(banner, width="auto", className="px-0"),
                dbc.Col(cards, className="mx-3"),
                dbc.Col(banner, width="auto", className="px-0"),
            ],
            className="g-0"
        ),
    ]
)
#-----------------------------------------------------------