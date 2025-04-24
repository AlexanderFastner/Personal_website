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
                    It is intended to serve as a resource for Biologists to analyze and interpret their sequencing data for aquatic life.\n

                    I solo developed this webtool and built it with python Dash, containerized as a Docker image, and hosted on Heroku. 
                    It allows a user to compare their aquatic specimens Busco genes (Benchmarking Universal Single-Copy Orthologs) to our dataset. 
                    These genes are selected because they are expected to be found in at least 90% of species in a lineage, and in a single copy in 90% of those species.
                    BUSCO genes serve as a standard set of markers for assessing the completeness and quality of genome assemblies, gene sets, and transcriptomes. The presence, absence, duplication, or fragmentation of these genes in a dataset provides an objective measure of how complete and accurate a genome assembly or annotation is

                    Different visualizations are generated to show differences between transcriptomes as well as the biases introduced by different assembly programs (Trinity, TransPi).
                    TransPi is an assembly made by combining results from several other assemblers with stringent filtering criteria.
                    On your right you can see some examples of various data explorations possible with this site.

                    Check it out here! [Canata](https://github.com/AlexanderFastner/cantata_frontend)\n
                    If you are interested in the code check my [Github site](https://cantatadb-8f2293883fc5.herokuapp.com/)\n
                '''),
            ),
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
