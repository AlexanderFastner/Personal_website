#This is a page detailing my work on making Phylogenies fromm Protein embeddings
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from pages.components.custom_elements import custom_hr
#-----------------------------------------------------------
dash.register_page(__name__, path="/Protein_embeddings_to_Phylogenies")
#-----------------------------------------------------------
#Hyperparameter Table
table_header = [
    html.Thead(
        html.Tr([
            html.Th("Hyperparameter"),
            html.Th("Values")
        ])
    )
]
row1 = html.Tr([
    html.Td("Epochs"),
    html.Td([
        html.B("1"), ", 3, 10, 100 500"
    ])
])
row2 = html.Tr([
    html.Td("Activation Function"),
    html.Td([
        "ReLU, ", html.B("Sigmoid"), ", Tanh, Mish"
    ])
])
row3 = html.Tr([
    html.Td("Loss Function"),
    html.Td([
        html.B("MSE"),", KL, BCE"
    ])
])
row4 = html.Tr([
    html.Td("Layers"),
    html.Td([
        html.B("1/2/8/16"), ", 1/4/8/16, 1/4/16/32, 1/8/16/32"
    ])
])
table_body = [html.Tbody([row1, row2, row3, row4])]
table = dbc.Table(table_header + table_body, bordered=True, color="secondary")
#-----------------------------------------------------------
about = html.Div(
    [
        html.H3("Protein embeddings to Phylogenies"),
        custom_hr,
        dcc.Markdown(
            '''
                Check out the paper here: [Final_Report.pdf](assets/protein_embeddings/Embeddings_to_Phylogenies.pdf)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
                We also made a poster for ISMB/ECCB 2023! [Final Poster](assets/protein_embeddings/Poster_Protein_Embeddings_to_Phylogeny.pdf)
            '''
        ),
        html.H4("Introduction"),
        html.P(
            '''
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
            '''
        ),
        html.H4("Datasets"),
        html.P(
            '''
            - 1000 random sequences of Uniclust30 and Uniclust90
            - KLK dataset & KLK redundancy reduced (see paper) - both esm-2 and prott5 embeddings
            - kinase and phosphatase datasets (see paper)
            '''
        ),
        table,
        html.B("* most successful"),
        html.H4("Description"),
        html.P(
            '''
            We first try to establish that there is information contained in the dataset at all. 
            Then we use dimensionality reduction to try and filter only those dimensions that contain the most inofrmation and hopefully reduce the noise.
            To this end we use a VAE (Variable Autoencoder). We tested various distance metrics, clustering algorithms and activation functions and hidden layer depths. 
            In the end we find that the training needed is minimal and that further epochs end up making worse trees.
            The results of the various parameter mixes can be seen in the resulting figures. 
            '''
        ),
        html.H4("Result"),
        html.P('In the end we find that the protein embeddings alone with minimal training, even without additional dimensionality reduction were substantial support for building trees.'),
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
