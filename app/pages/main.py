#This is the main landing page of my Website
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
import os

print(os.getcwd())
#----------------------------------------------------------
dash.register_page(__name__, path="/")
#-----------------------------------------------------------
shark = "general/shark.jpg"
profile_picture = "general/profile_picture.png"
DNA_graphic = "general/DNA_graphic.png"
#-----------------------------------------------------------

#TODO change to bloglike to coment on things I've done/liked

# #Shark banner
# dbc.Col(
#     html.Img(src=dash.get_asset_url(shark), height="400px", width="600px"),
# ),

#TODO
#Layout last blog posts and permanent things?

#-----------------------------------------------------------
layout = (
    html.H4("Coming soon"),
)