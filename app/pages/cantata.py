#This is a page detailing my work on Cantata 
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Cantata")
#-----------------------------------------------------------
heatmap_example = "Cantata/heatmap_example.png"
stacked_area_example = "Cantata/stacked_area_example.png"
raincloud_example = "Cantata/raincloud_example.png"
alignment_example = "Cantata/alignment_example.png"
#-----------------------------------------------------------
info = html.Div(
    # style={"display": "flex"},
    children=[
        dbc.Card(
            dbc.CardBody(
                dcc.Markdown(
                    '''
                    ### CANTATA\n

                    **CANTATA** is a (**C**ommunity b**A**sed **N**on-bila**T**eri**A**n **T**ranscriptome **A**rchive).\n

                    The aim of this project is to provide an archive of non-bilaterian transcriptomic resources assembled and annotated in a standardized manner.
                    I solo developed the frontend and visualization tools for this resource in python dash and hosted it using docker and heroku.
                    It is intended to serve as a resource for Biologists to analyze and interpret their sequencing data for aquatic life.\n

                    On your right you can see some examples of various visualizations possible with this site.

                    Check it out here! [Canata](https://github.com/AlexanderFastner/cantata_frontend)\n
                    If you are interested in the code check my [Github site](https://cantatadb-8f2293883fc5.herokuapp.com/)\n

                '''),
            ),
            # style={"width": "60%"},
        ),
    ]
)
#-----------------------------------------------------------
examples = html.Div(
    children=[
        dbc.Card([
            dbc.CardHeader(html.H5("Heatmap Example")),
            dbc.CardImg(src=dash.get_asset_url(heatmap_example), className="w-100"),
        ]),
        dbc.Card([
            dbc.CardHeader(html.H5("Stacked Area Example")),
            dbc.CardImg(src=dash.get_asset_url(stacked_area_example), className="w-100"),
        ]),
        dbc.Card([
            dbc.CardHeader(html.H5("Raincloud Example")),
            dbc.CardImg(src=dash.get_asset_url(raincloud_example), className="w-100"),
        ]),
        dbc.Card([
            dbc.CardHeader(html.H5("Alignment Comparison Example")),
            dbc.CardImg(src=dash.get_asset_url(alignment_example), className="w-100"),
        ]),
    ]
)

#-----------------------------------------------------------
layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(info, width=5),
                dbc.Col(examples, width=7),
            ]
        )
    ]
)
#-----------------------------------------------------------
