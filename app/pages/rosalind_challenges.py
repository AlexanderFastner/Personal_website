#This is a page detailing Rosaling problems
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Rosalind_challenges")
#-----------------------------------------------------------
#TODO 
#write description ADD SOME EXAMPLES

Rosalind = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        dbc.Stack(
                            [
                                dbc.Col([html.Img(src=dash.get_asset_url("rosalind/Rosalind_logo.png"), height="60px")], width="auto"),
                            ],
                            direction="horizontal",
                        )
                    ]
                ),
                dbc.CardBody(
                    [
                        dcc.Markdown(
                            """
                            ## What is Rosalind?

                            Rosalind is a platform for learning Bioinformatics by working through a collection of problems.    [Rosalind Website](https://rosalind.info/about/)

                            # Some examples of what I have done so far

                            **SGRA**: Using the Spectrum Graph to Infer Peptides
                            In this challenge one must transform a list of positive real numbers corresponding to the spectrum graph of a protein seequence
                            into the longest protein string that matches the spectum graph.\n

                            **NKEW**: Newick Format with Edge Weights
                            Upon recieving a weighted newick tree return a collection of numbers that represents the distances between the nodes.


                            # There are many others covering topics like: 
                            - Alignment
                            - Combinatorics
                            - Computational Mass SPectrometry
                            - Divide and Conquer
                            - Dynamic Programming
                            - Genomic Assembly
                            - Genome REarrangments
                            - Graph Algorithms
                            - Graphs
                            - Heredity
                            - Phylogeny
                            - Population Dynamics
                            - Porbability
                            - Set Theory
                            - Sorting
                            - String Algorithms

                            Check out my solutions here [Github]("https://github.com/AlexanderFastner/Rosalind).

                            ### Current Ranking
                        """),
                        html.Iframe(src="https://rosalind.info/statistics/countries/de/", width="100%", height="500") # , height="500", style={"border": "none"}
                    ]
                ),
            ],
        )
    ]
),

iframe = html.Div(
    [   
        html.Iframe(src="https://rosalind.info/users/Alex.Fastner/", height="1000", width="100%", style={"border": "none"}),
        html.Br(),
        html.A("My Account", href="https://rosalind.info/users/Alex.Fastner/", target="_blank"), 
    ]
),

#-----------------------------------------------------------
layout = (
    [
        dbc.Row(
            [
                dbc.Col(Rosalind, width=6),
                dbc.Col(iframe, width=6),
            ]
        )
    ]
)
#-----------------------------------------------------------