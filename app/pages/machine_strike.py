#This is a page detailing my work on Machine Strike
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Machine_Strike")
#-----------------------------------------------------------
about = html.Div([

    #TODO update github description of this

    #TODO Fill this out better
    html.H4("Machine Strike"),
    #TODO Link to game wiki ...etc
    dcc.Markdown("""[Link to github repo](https://github.com/AlexanderFastner/Machine_Strike)&nbsp; &nbsp; &nbsp; &nbsp;"""),

    html.P("Basic Premise, Pictures, Description, Kotlin, maps, what I will change/do differently"),
    html.H4("Machine Strike"),
])
#-----------------------------------------------------------
#TODO ADD Picutres of maps and UI and such
#TODO Add pictures to github as well


#-----------------------------------------------------------
layout = ([
    dbc.Row(
        [
            dbc.Col(about, width=12),
            # dbc.Col(figures, width=6),
        ],
    ),
])
#-----------------------------------------------------------
