#This is my contact page
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
github = "general/github.png"
linkedin = "general/linkedin.png"
#-----------------------------------------------------------
def create_footer():
    return dbc.Container(
        dbc.Row(
            dbc.Col(
                html.Footer([
                    html.H4("Contact Me", style={'color': 'black', 'margin': '0', 'padding': '10px', 'text-decoration': 'underline'}, className="text-center"),
                    # html.Br(),
                    dbc.Col(
                        [
                            html.Div([
                                html.Img(src=dash.get_asset_url(github), height="32px", width="32px", style={"margin-right": "10px"}),
                                dbc.CardLink("Linkedin", href="https://www.linkedin.com/in/alexander-fastner/", style={"margin-right": "50px"}),
                                html.Img(src=dash.get_asset_url(linkedin), height="32px", width="32px", style={"margin-right": "10px"}),
                                dbc.CardLink("Github", href="https://github.com/AlexanderFastner"),
                                html.Br(),
                                html.Plaintext("Email: alexanderfastner+contact@gmail.com", style={'color': 'black', 'margin': '0', 'padding': '0'}),
                            ]),
                            
                        ], className="text-center", style={'height': 'auto', 'minHeight': '40px'}
                    )
                ], className="bg-dark p-0 fixed-bottom")
            )
        ),
        fluid=True,
        className="p-0"
    )
