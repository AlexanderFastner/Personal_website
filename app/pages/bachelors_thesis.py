#This is a page detailing my work on my Bachelors_Thesis
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Bachelors_Thesis")
#-----------------------------------------------------------
#TODO MAKE THIS NOT USE CARDS!!!

about = html.Div([
    dbc.Card([
        dbc.CardHeader("Search for evidence of recombination in Alternaria solani using genomic tools"),
        dbc.CardBody(
            dcc.Markdown(
                '''
                Alternaria solani is a fungal pathogen responsible for early blight in tomatoes and potatoes, two globally important crops. The disease typically begins as small, dark lesions with characteristic concentric rings on older leaves, but can spread to stems and fruit, causing significant defoliation and yield loss. As a necrotrophic pathogen, A. solani kills host tissue and feeds on the resulting dead material. Notably, it reproduces asexually via conidia and has no known sexual stage, although some genetic evidence suggests recombination may occur.

                Fungicides, particularly succinate dehydrogenase inhibitors (SDHIs), are commonly used to manage early blight. However, resistance to these fungicides is emerging, with highly resistant strains now reported in parts of Europe. This resistance appears to have developed independently in different regions, hinting at possible genetic recombination within the pathogen population.

                To investigate this, I analyzed 48 A. solani samples from various European regions and the United States using recombination detection tools ClonalFrameML and LDHelmet. These tools help assess whether genetic exchange occurs, which is important for designing robust, cost-effective integrated pest management strategies. Understanding the pathogen’s reproductive biology can inform how we approach disease control, especially as resistance to chemical controls grows.
                '''
            ),
        ),
    ]),
    dbc.Card([
        dbc.CardHeader("ClonalFrameML"),
        dbc.CardBody(
            html.P("ClonalFrameML is a maximum likelihood-based software tool designed for detecting and quantifying recombination events in bacterial genomes. It analyzes aligned whole-genome sequence data to reconstruct phylogenies that account for recombination, estimate key recombination parameters, and map where recombination has occurred across the genome. ClonalFrameML is particularly efficient, capable of processing hundreds of genomes in a matter of hours, and is well-suited for large-scale comparative genomics studies.")
        ),
    ]),
    dbc.Card([
        dbc.CardHeader("LDHelmet"),
        dbc.CardBody(
            html.P("LDhelmet is a statistical tool used to infer fine-scale crossover recombination rates from population genetic data, particularly from phased and aligned DNA sequences. It uses advanced population genetic models and Markov Chain Monte Carlo (MCMC) methods to generate detailed recombination maps, identifying recombination hotspots with high accuracy. LDhelmet is robust to noise in the data and is designed for use with up to 50 haplotypes, making it suitable for whole-genome population studies.")
        ),
    ]),
    dbc.Card([
        dbc.CardHeader("Results"),
        dbc.CardBody(
            html.P("TODO")
        ),
        dbc.CardFooter(
            html.P(
                """[
                Link to github repo](https://github.com/AlexanderFastner/Alternaria-Solani-Recombination)
                Paper here: [Bachelor.pdf](bachelor/Bachelor.pdf)
                """
            ),
        )
    ]),
])

#TODO split into column  andd make into images smaller and figures larger

figures = html.Div([
    dbc.Col([
        dbc.Card([
            dbc.CardHeader(html.H5("Alternaria Solani on Leaves")),
            dbc.CardImg(src = dash.get_asset_url("bachelor/alternaria_solani.jpg"), className="w-100"), # Credit Jerzy Opioła, CC BY-SA 4.0via Wikimedia Commons
            # dbc.CardFooter(),
        ]),
        dbc.Card([
            dbc.CardHeader(html.H5("Figure 1")),
            # dbc.CardImg(src = dash.get_asset_url("bachelor/bachelor_1.png"), className="w-100"),
        ]),
        dbc.Card([
            dbc.CardHeader(html.H5("Figure 2")),
            # dbc.CardImg(src = dash.get_asset_url("bachelor/bachelor_2.png"), className="w-100"),
        ]),
    ]),
])
#-----------------------------------------------------------
layout = ([
    dbc.Row(
        [
            dbc.Col(about, width=6),
            dbc.Col(figures, width=6),
        ],
    ),
])
#-----------------------------------------------------------
