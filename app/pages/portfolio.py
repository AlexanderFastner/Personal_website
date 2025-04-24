#This is my portfolio page
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/portfolio")
#-----------------------------------------------------------
DNA_graphic = "general/DNA_graphic.png"

#TODO FINISH ALL PROJECTS

#TODO maybe replace with non card element - and style better!
Intro_Card = dbc.Card(
    dbc.CardBody(
        [
            html.H2("This is a collection of all the various projects I have worked on throughout the years."),
        ]
    )
)

Bioinformatics_Projects_Card = dbc.Card([
    dbc.CardHeader(html.H4("Bioinformatics Projects")),
    dbc.CardBody(
        [
            dbc.ListGroup(
                [
                    #TODO add a 1 sentence summary and thumbnail? of what each link is
                    dcc.Link(dbc.ListGroupItem("Cantata"), href="/Cantata"),
                    dcc.Link(dbc.ListGroupItem("Rosalind challenges"), href="/Rosalind_challenges"),
                    dcc.Link(dbc.ListGroupItem("Protein embeddings to Phylogenies"), href="/Protein_embeddings_to_Phylogenies"),
                    dcc.Link(dbc.ListGroupItem("DysRegNetWeb"), href="/DysRegNetWeb"),
                    # dcc.Link(dbc.ListGroupItem("SpongeDB_v2"), href="/SpongeDB_v2"),
                    dcc.Link(dbc.ListGroupItem("Bachelors Thesis"), href="/Bachelors_Thesis"),
                    # TODO add NLR work and publication here!
                    dcc.Link(dbc.ListGroupItem("Masters Thesis"), href="/Masters_Thesis"),
                ],
                flush=True,
            ),
        ]
    ),
])

Data_Analysis_Card = dbc.Card(
    [
        dbc.CardHeader(html.H4("Data Analysis Case studies")),
        dbc.CardBody([
            dbc.ListGroup([
                dcc.Link(dbc.ListGroupItem("Cyclistic Case Study"), href="/Cyclistic_Case_Study"),
            ]),
        ]),
    ]
)

Games_Card = dbc.Card([
    dbc.CardHeader(html.H4("Games")),
    dbc.CardBody([
        dbc.ListGroup(
            [
            dcc.Link(dbc.ListGroupItem("Othello"), href="/Othello"),
            html.H6("Machine Strike - Coming soon"),
            html.H6("2 Cars - Coming soon"),
            ]
        ),
    ]),
])

Random_Card = dbc.Card([
    dbc.CardHeader(html.H4("Random")),
    dbc.CardBody([
        dbc.ListGroup(
            [
            dcc.Link(dbc.ListGroupItem("Arduino"), href="/Arduino"),
            html.H6("Raspberry Pi - Coming soon"),
            html.H6("3d Printing - Coming soon"),
            # dcc.Link(dbc.ListGroupItem("Raspberry Pi"), href="/RasPi"),
            # dcc.Link(dbc.ListGroupItem("3d Printing"), href="/RasPi"),
            ]
        ),
    ]),
])

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
                Intro_Card,
                Bioinformatics_Projects_Card,
                Data_Analysis_Card,
                Games_Card,
                Random_Card,
            ],
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