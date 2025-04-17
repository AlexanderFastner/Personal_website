#This is a page detailing my work on DysRegNetWeb
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/DysRegNetWeb")
#-----------------------------------------------------------
info = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                dcc.Markdown(
                    '''
                    ## DysRegNet

                    Gene regulation is frequently altered in diseases in unique and patient-specific ways. 
                    Hence, personalised strategies have been proposed to infer patient-specific gene-regulatory networks. 
                    However, existing methods do not scale well because they often require recomputing the entire network per sample.
                    Moreover, they do not account for clinically important confounding factors such as age, sex or treatment history.
                    Finally, a user-friendly implementation for the analysis and interpretation of such networks is missing.

                    ## DysRegNetWeb

                    We built a web interface for the pre-existing DysReg Net to allow users to easily check for dysregulation of specific genes and compare to GTEx tissue data. 
                    The constructed biological network information is contained in a neo4j graphical database and displayed in an intuitive way. 

                    ## Use

                    After selecting a cancer and target genes a network is shown with the levels of dysregulation shown as red percentages on the arrows connecting them. 
                    This can then be filtered and compared to the regulation in other cancer types. Additional parameter sliders are available for adjusting what to display.

                    Check out the webpage here [here](https://exbio.wzw.tum.de/dysregnet/)\n
                    DysRegNet is available as a [Python package](https://github.com/biomedbigdata/DysRegNet_package)\n
                    [Publication](https://pubmed.ncbi.nlm.nih.gov/39631757/)\n

                    '''
                ),
            ),
        ),
    ]
)

figures = html.Div(
    [   
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Dysregulation Network")),
                    dbc.CardImg(src = dash.get_asset_url("dysregnet/dysregnet_1.png"), className="w-100"),
                ]),
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Gene mutation frequency among patients")),
                    dbc.CardImg(src=dash.get_asset_url("dysregnet/dysregnet_2.png"), className="w-100"),
                ]),
                dbc.Card([
                    dbc.CardHeader(html.H5("Patient-specific promoter methylation heatmap")),
                    dbc.CardImg(src=dash.get_asset_url("dysregnet/dysregnet_3.png"), className="w-100"),
                ]),
                dbc.Card([
                    dbc.CardHeader(html.H5("Patient-specific dysregulation heatmap")),
                    dbc.CardImg(src=dash.get_asset_url("dysregnet/dysregnet_4.png"), className="w-100"),
                ]),
            ]),
        ])
    ]
),

#-----------------------------------------------------------
layout = (
    dbc.Row(
        [
            dbc.Col(info, width=6),
            dbc.Col(figures, width=6),
        ]
    )
)