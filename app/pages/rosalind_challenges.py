#This is a page detailing Rosaling problems
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Rosalind_challenges")
#-----------------------------------------------------------
#TODO 
#Make 2 column
#make my progress into iframe
    #remove image
    #move my progress to rigth hand side
#write description


layout = (
    html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        [
                                            dbc.Stack(
                                                [
                                                    dbc.Col([html.Img(src=dash.get_asset_url("rosalind/Rosalind_logo.png"), height="100px", width="250px")], width="100px"),
                                                ],
                                                direction="horizontal",
                                            )
                                        ]
                                    ),
                                    dbc.CardBody(
                                        [
                                            html.H1("What is Rosalind?"),
                                            html.P("""Rosalind is a platform for learning Bioinformatics by working through a collection of problems.\n
                                                   
                                                   """),


                                            html.A("Rosalind Website", href="https://rosalind.info/about/", target="_blank"),
                                            html.Br(),
                                            html.H2("What have I done so far"),
                                            html.P("list/description of some of the problems"),
                                            html.Br(),
                                            html.H2("Current Ranking"),
                                            #embed in Iframe
                                            html.Iframe(src="https://rosalind.info/statistics/countries/de/", height="500", width="100%", style={"border": "none"})
                                        ]
                                    ),
                                    dbc.CardFooter(
                                        [
                                            html.A("Git Repo", href="https://github.com/AlexanderFastner/Rosalind", target="_blank"),
                                        ]
                                    ),
                                ],
                            )
                        ]
                    ),

                    dbc.Col(
                        [   
                            #TODO remove scrollbar (add in Css, scrolling="no" doesnt work)
                            #MY PROGRESS
                            html.Iframe(src="https://rosalind.info/users/Alex.Fastner/", height="1000", width="100%", style={"border": "none"}),
                            html.Br(),
                            html.Br(),
                            #Link to my page
                            html.A("My Account", href="https://rosalind.info/users/Alex.Fastner/", target="_blank"),
                        ]
                    ),
                ]
            )
        ]
    )
)


#-----------------------------------------------------------
