#This is my contact page
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/contact")
#-----------------------------------------------------------

#TODO add ways to contact me
#TODO think of a design - layout for this
#TODO add picture
#TODO add logos for linkedin and github

links = dbc.Card(
    [
         dbc.Col(
            [

                html.Br(),
                dbc.CardLink("Linkedin", href="https://www.linkedin.com/in/alexander-fastner/"),
                html.Br(),
                dbc.CardLink("Github", href="https://github.com/AlexanderFastner"),
                html.Br(),
                html.Plaintext("Email: alexanderfastner+contact@gmail.com"),
            ]
         )
    ]
)
#-----------------------------------------------------------
layout = (
    [
        links
    ]
)
#-----------------------------------------------------------
