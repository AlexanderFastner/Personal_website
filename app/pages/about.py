#This is a page About Me
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/about")
#-----------------------------------------------------------
about = (
    html.Div(
        style={"display": "flex", "justify-content": "center"},
        children=[

            #TODO Add images of me
            #TODO  Write better intro text - similar as linkedin
            dbc.Card(
                dbc.CardBody(
                    dcc.Markdown(
                        '''
                        # About  Me:
                        3-4 sentence intro
                        
                        ### Hobbies
                            diving
                            Random projects: Arduino
                                             Android Apps
                                             Raspberry Pi
                        
                        ### Education
                        I am a Bay Area native who pursued higher education in Germany, by leveraging my dual citizenship and German language proficiency. 
                        In Munich I began on my Bachelors in Bioinformatics in 2022 in a program shared between the two large universities in Munich. 
                            Technical University of Munich - add link
                            Ludwig-Maximilians-Universitaet - add link
                        
                        
                        
                        Talk about various lectures...
                        ...
                        ...

                        TUM/LMU Bioinformatics Bachelor - title/topic

                        other lectures in mmy masters program

                        TUM/LMU Bioinformatics Master- title/topic

                        I completed my M.Sc. in 2024 and moved back to the United States to start my Career.
                        
                        If you are interested in my work, you can find more information on my linkedIn.                        
                    '''),
                ),
            ),
        ]
    )
)
#-----------------------------------------------------------

profile_picture = "general/profile_picture.png"

Picture_Card = dbc.Card(
    dbc.CardBody(
        [   
            dbc.Col(
                [
                html.Img(src=dash.get_asset_url(profile_picture), height="800px"),
                html.Br(),
                dbc.CardLink("Linkedin", href="https://www.linkedin.com/in/alexander-fastner/"),
                html.Br(),
                dbc.CardLink("Github", href="https://github.com/AlexanderFastner"),
                html.Br(),
                html.Plaintext("Email: alexanderfastner@gmail.com"),
                ]
            )
        ]
    ),
)
#-----------------------------------------------------------
cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(about, width=8),
                dbc.Col(Picture_Card, width=4),
            ]
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
