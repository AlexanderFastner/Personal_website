#This is a page detailing my work on my masters thesis
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from pages.components.custom_elements import custom_hr
#-----------------------------------------------------------
dash.register_page(__name__, path="/Masters_Thesis")
#-----------------------------------------------------------
#TODO ADD TABLE

#-----------------------------------------------------------
#TODO Link to Helmholtz and Theislab websites
#TODO PUT THIS ON GITHUB TOO
about = html.Div([
    html.H4("Masters Theis: Bioinformatic Analysis of the role of MAFA in Stem Cell-Derived Human Pancreatic Islets."),
    custom_hr,
    dcc.Markdown("""[Link to github repo](https://github.com/AlexanderFastner/MAFA_functional_analysis)&nbsp; &nbsp; &nbsp; &nbsp; Check out the full Paper here: [Master_Thesis.pdf](master/Final_Print_Master_Thesis.pdf)"""),
    html.P("This project is a collaboration between the Theis Lab at the Helmholtz Institute of Munich and Hebrok Lab at Technical University of Munich (TUM)."),
    html.H4("Abstract"),
    html.P(
        """
        Type 1 diabetes (T1D) is an autoimmune disorder characterized by immune-mediated destruction of insulin-producing pancreatic β-cells, leading to lifelong dependence on exogenous insulin.
        Current stem cell-based therapies aim to restore endogenous insulin production by generating functional β-cells from pluripotent stem cells, though challenges remain in achieving functional maturity comparable to primary β-cells.
        The transcription factor MAFA plays a pivotal role in maintaining β-cell identity and regulating insulin production, with human β-cells showing developmental-stage-specific MAFA expression patterns – low activity in juvenile cells and higher expression in mature adult cells.
        A naturally occurring MAFAS64F mutation initially enhances insulin production through elevated MAFA activity, but this effect proves transient, highlighting MAFA's dual role in promoting β-cell function and its susceptibility to instability.

        Bulk RNA sequencing of MAFAWT and MAFAS64F cell lines revealed heightened differential gene expression in the mutant, particularly in pathways related to β-cell maturation and insulin biosynthesis. Surprisingly, control cell lines showed greater activation scores in key metabolic pathways despite lower MAFA expression, suggesting compensatory mechanisms in unmodified cells. While the study faced limitations from sparse temporal data, it established an analytical framework to investigate MAFA's role in stabilizing stem cell-derived β-cells – a critical step toward developing durable cell replacement therapies for T1D. These findings underscore the need to balance MAFA-driven insulin production with mechanisms ensuring long-term β-cell survival and function.
        """
    ),
    #TODO Center this and split into columns
    
    dbc.Row([
        dbc.Col(
            [
                html.H4("Experiment Design"),
                html.Img(src = dash.get_asset_url("master/hpsc_progression.png")),
                html.P(
                    """
                    The general strategy for generating β cells from human pluripotent stem cells (hPSCs) is to closely recapitulate the path that hPSCs take during embryogenesis.
                    They are directed from the initial starting hPSCs through various intermediary stages to finally become pancreatic islet β cells.
                    """
                ),
                html.Br(),
                html.H4("Data Flow"),
                html.Img(src = dash.get_asset_url("master/dataflow.png"), height="40%", width="40%"),
            ], style={'textAlign': 'center'}
        ),
        dbc.Col([
            html.H4("Insulin Production", style={'textAlign': 'center'}),
            dbc.Row([
                    dbc.Col([
                        html.P(
                            """
                            After stimulation with Dox, MAFA expression is detectable. The stem cell lines were then differentiated towards β cells and treated with Dox starting at -3, -7, and -14 days.
                            The samples were then assayed for glucose-stimulated insulin secretion (GSIS) functionality after 7 and 14 days of Dox treatment.

                            *The data from the 3 day Dox treatment was not included in the data used in this project.
                            """
                        ),
                    ]),
                    dbc.Col([html.Img(src = dash.get_asset_url("master/gsis.png"), height="80%", width="80%")]),
                ]),
        ]),
    ]),
    

    html.P("Problem statement?"),

    html.H4("Results"),
    html.P("Discuss Results"),
])
#-----------------------------------------------------------

#TODO make this formatting better!

# figures = html.Div([
#     dbc.Row([
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardHeader(html.H5("TODO")),
#                 # dbc.CardImg(src = dash.get_asset_url("master/1.png"), className="w-100"),
#             ]), 
#             dbc.Card([
#                 dbc.CardHeader(html.H5("TODO")),
#                 # dbc.CardImg(src = dash.get_asset_url("master/1.png"), className="w-100"),
#             ]),
#         ]),
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardHeader(html.H5("TODO")),
#                 # dbc.CardImg(src = dash.get_asset_url("master/1.png"), className="w-100"),
#             ]),
#             dbc.Card([
#                 dbc.CardHeader(html.H5("TODO")),
#                 # dbc.CardImg(src = dash.get_asset_url("master/1.png"), className="w-100"),
#             ]),
#             dbc.Card([
#                 dbc.CardHeader(html.H5("TODO")),
#                 # dbc.CardImg(src = dash.get_asset_url("master/1.png"), className="w-100"),
#             ]),
#         ]),
#     ]),
# ])

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

