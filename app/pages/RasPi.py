#This is a page detailing my RasPi projects
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/RasPi")
#-----------------------------------------------------------
layout = html.Div([
    html.H1("RasPi"),
    dbc.Card(
        dbc.CardBody(
            dcc.Markdown(
                '''
                Projects list\n
                Hosting this website\n
                More Projects coming soon...\n
                link to github\n
            '''),
        ),
    ),
])
#-----------------------------------------------------------

