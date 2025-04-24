#This is a page detailing my work on my Bachelors_Thesis
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from pages.components.custom_elements import custom_hr
#-----------------------------------------------------------
dash.register_page(__name__, path="/Bachelors_Thesis")
#-----------------------------------------------------------
#Table for ClonalFrame Parameters
table_header = [html.Thead(html.Tr([html.Th("Parameter"), html.Th("Default"), html.Th("Alternate parameters")]))]

row1 = html.Tr([html.Td("R/theta (Relative rate of recombination to mutation)"), html.Td("0.1"), html.Td("0.01, 0.001")])
row2 = html.Tr([html.Td("Kappa (Relative rate of transitions to transversions)"), html.Td("2.0"), html.Td("1.0, 3.0")])
row3 = html.Tr([html.Td("Nu (Mean divergence of imported DNA) "), html.Td("0.1"), html.Td("1.0, 0.01")])

table_body = [html.Tbody([row1, row2, row3])]
table = dbc.Table(table_header + table_body, bordered=True, color="secondary")
#-----------------------------------------------------------
#TODO ADD LDHELMET RESULTS
#TODO ADD FIGURES

about = html.Div([
    html.H4("Search for evidence of recombination in Alternaria solani using genomic tools"),
    custom_hr,
    dcc.Markdown("""[Link to github repo](https://github.com/AlexanderFastner/Alternaria-Solani-Recombination)&nbsp; &nbsp; &nbsp; &nbsp; Check out the full Paper here: [Bachelor.pdf](bachelor/Bachelor.pdf)"""),
    html.P(
        '''
        Alternaria solani is a fungal pathogen responsible for early blight in tomatoes and potatoes, two globally important crops. The disease typically begins as small, dark lesions with characteristic concentric rings on older leaves, but can spread to stems and fruit, causing significant defoliation and yield loss. As a necrotrophic pathogen, A. solani kills host tissue and feeds on the resulting dead material. Notably, it reproduces asexually via conidia and has no known sexual stage, although some genetic evidence suggests recombination may occur.

        Fungicides, particularly succinate dehydrogenase inhibitors (SDHIs), are commonly used to manage early blight. However, resistance to these fungicides is emerging, with highly resistant strains now reported in parts of Europe. This resistance appears to have developed independently in different regions, hinting at possible genetic recombination within the pathogen population.

        To investigate this, I analyzed 48 A. solani samples from various European regions and the United States using recombination detection tools ClonalFrameML and LDHelmet. These tools help assess whether genetic exchange occurs, which is important for designing robust, cost-effective integrated pest management strategies. Understanding the pathogen’s reproductive biology can inform how we approach disease control, especially as resistance to chemical controls grows.
        '''
    ),
    html.H5("ClonalFrameML"),
    html.P(
        """
        ClonalFrameML is a maximum likelihood-based software tool designed for detecting and quantifying recombination events in bacterial genomes. It analyzes aligned whole-genome sequence data to reconstruct phylogenies that account for recombination, estimate key recombination parameters, and map where recombination has occurred across the genome. ClonalFrameML is particularly efficient, capable of processing hundreds of genomes in a matter of hours, and is well-suited for large-scale comparative genomics studies.
        """
    ),
    html.H5("LDHelmet"),
    html.P(
        """
        LDhelmet is a statistical tool used to infer fine-scale crossover recombination rates from population genetic data, particularly from phased and aligned DNA sequences. It uses advanced population genetic models and Markov Chain Monte Carlo (MCMC) methods to generate detailed recombination maps, identifying recombination hotspots with high accuracy. LDhelmet is robust to noise in the data and is designed for use with up to 50 haplotypes, making it suitable for whole-genome population studies.
        """
    ),
    html.H4("Results"),
    custom_hr,
    html.H5("ClonalFrameML"),
    html.P(
        """
        Understanding the output:
        On the left-hand side is a dendrogram with the corresponding sample names in the middle. 
        The rows on the right-hand side reflect clonalFrameML’s prediction for likelihood of recombination for each position across the genome. 
        The output shown here is color coded. Dark blue - detected recombination :light blue, yellow, orange, red - Homoplasies or raw mutations.
        A strong indication of suspected recombination would be that the same positions are marked in blue and would show here as vertical blue lines.
        """
    ),
    dcc.Markdown("> **Homoplasy**: is a mutation that occurs on multiple branches"),
    table,
    html.P(
        """
        Consider:\n
        Fungal recombination detection tools arent common or well documented- thus we tried ClonalFrameML.\n

        1. Genomes are cut together from reads originating from several chromosomes. The high levels of recombination suggested at the bounderies of chromosomes are very likley artifacts in the program. ClonalFrameML was initially developed to be used on bacterial genomes. As we are using a non-circular genome the program might be detecting repeating sequences on both sides of the chromosome and interpreting these as recombination.\n
        Our approach to addressing this and get more resolution is to run each chromosome individually. \n
        2. The horizontal blue lines are likely an artifact of how ClonalFrameML works and appear on the in-between genomes that are generated as a stand in for a common ancestor link.
        """
    ),
    html.H5("LDHelmet"),
    dcc.Markdown(
        """
        These figures shown here were generated utilizing ggplot2 in R. \n
        The X axis represents the position in the sequence and the Y shows the recombination rate/base pair (ρ/bp).

        - **X-axis** represents the position in the sequence\n
        - **Y-axis** shows the recombination rate/base pair (ρ/bp)
        """
    ),
    html.P(
        """
        The visualized results produced by LDHelmet are less prone to noise and more easily parsable.
        With LDHelmet we find 14 regions that show evidence of recombination. Many of which upon visual inspection line up with results from ClonalFrameML.
        """
    ),
])

#TODO split into column  and make into images smaller and figures larger

figures = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("Alternaria Solani on Leaves")),
                dbc.CardImg(src = dash.get_asset_url("bachelor/alternaria_solani.jpg"), className="w-100"), # Credit Jerzy Opioła, CC BY-SA 4.0via Wikimedia Commons
            ]), 
            dbc.Card([
                dbc.CardHeader(html.H5("Map")),
                dbc.CardImg(src = dash.get_asset_url("bachelor/map.png"), className="w-100"),
            ]),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("Chromosome 5 ClonalFrameML")),
                dbc.CardImg(src = dash.get_asset_url("bachelor/chr1_clonalframeml.png"), className="w-100"),
            ]),
            dbc.Card([
                dbc.CardHeader(html.H5("Chromosome 7 LDHelmet")),
                dbc.CardImg(src = dash.get_asset_url("bachelor/chr7_LDhelmet.png"), className="w-100"),
            ]),
            dbc.Card([
                dbc.CardHeader(html.H5("Chromosome 1 Comparison between both")),
                dbc.CardImg(src = dash.get_asset_url("bachelor/chr1_comparison.png"), className="w-100"),
            ]),
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
