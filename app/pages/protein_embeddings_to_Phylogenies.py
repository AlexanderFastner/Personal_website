#This is a page detailing my work on making Phylogenies fromm Protein embeddings
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Protein_embeddings_to_Phylogenies")
#-----------------------------------------------------------
about = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                dcc.Markdown(
                    '''
                        # Protein embeddings to Phylogenies

                        Check out the paper here: [Final_Report.pdf](assets/protein_embeddings/Embeddings_to_Phylogenies.pdf)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
                        We also made a poster for ISMB/ECCB 2023! [Final Poster](assets/protein_embeddings/Poster_Protein_Embeddings_to_Phylogeny.pdf)

                        ### Introduction

                        Phylogenetic trees are a vital tool in evolutionary biology used to
                        visualize the relationships between different organisms based on their
                        genetic sequences. The process of constructing phylogenetic trees involves
                        comparing the genetic sequences of different organisms and identifying
                        the similarities and differences between them. Traditionally, multiple
                        sequence alignments (MSAs) are used to align the protein sequences to
                        find conserved regions. The proteins are then clustered by these regions
                        to build phylogenetic trees. The similarity of sequences in evolutionary
                        relationships is generally derived through methods such as maximum
                        likelihood or Bayesian inference. Although MSAs are currently the most
                        reliable way to create trees, it is a very time consuming method. In order to
                        reduce time, we used protein sequence embeddings to cluster them without
                        doing MSAs first.

                        **TLDR**: We take an vector representation of a protein sequence, calculate how different it is from others, and build a tree with those relationships and evaluate.

                        ### Datasets
                        - 1000 random sequences of Uniclust30 and Uniclust90
                        - KLK dataset & KLK redundancy reduced (see paper) - both esm-2 and prott5 embeddings
                        - kinase and phosphatase datasets (see paper)

                        ### VAE Hyperparameters
                        - Epochs: **1**, 3, 10, 100, 500
                        - Activation Function: ReLU, **Sigmoid**, Tanh, Mish
                        - Loss function: **MSE**, KL, BCE
                        - layers: **1/2/8/16**, 1/4/8/16, 1/4/16/32, 1/8/16/32
                        * most successful

                        ### Descritpion 

                        We first try to establish that there is information contained in the dataset at all. 
                        Then we use dimensionality reduction to try and filter only those dimensions that contain the most inofrmation and hopefully reduce the noise.
                        To this end we use a VAE (Variable Autoencoder). We tested various distance metrics, clustering algorithms and activation functions and hidden layer depths. 
                        In the end we find that the training needed is minimal and that further epochs end up making worse trees.
                        The results of the various parameter mixes can be seen in the resulting figures. 

                        ### Result

                        In the end we find that the protein embeddings alone with minimal training, even without additional dimensionality reduction were substantial support for building trees.
                    '''
                ),
            ),
        ),
    ]
)
#-----------------------------------------------------------
final_trees = "protein_embeddings/final_trees.png"
general_structure = "protein_embeddings/general_structure.png"
distances = "protein_embeddings/distances.png"
parameters = "protein_embeddings/parameters.png"

figures = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader("General Structure"),
                dbc.CardImg(src = dash.get_asset_url(general_structure), className="w-100")
            ]
        ),
        dbc.Card(
            [
                dbc.CardHeader("Parameters"),
                dbc.CardImg(src = dash.get_asset_url(parameters), className="w-100")
            ]
        ), 
        dbc.Card(
            [
                dbc.CardHeader("Distance Matricies by metric (with and without Training)"),
                dbc.CardImg(src = dash.get_asset_url(distances), className="w-100")
            ]
        ), 
        dbc.Card(
            [
                dbc.CardHeader("Final Trees"),
                dbc.CardImg(src = dash.get_asset_url(final_trees), className="w-100")
            ]
        ),       
    ]
)
#-----------------------------------------------------------
layout = (
    [
        dbc.Row(
            [
                dbc.Col(about, width=8),
                dbc.Col(figures, width=4),
            ],
        ),
    ]
)
#-----------------------------------------------------------
