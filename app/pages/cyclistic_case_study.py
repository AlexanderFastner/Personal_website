#This is a page detailing my work on Cyclistic_Case_Study
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Cyclistic_Case_Study")
#-----------------------------------------------------------
about = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        dbc.Stack(
                            [
                                dbc.Col([html.Img(src=dash.get_asset_url("cyclistic/images/Cyclistic_logo.png"), height="100px", width="100px")], width="100px"),
                                dbc.Col([html.H2("My Capstone Case Study as part of the Google Data Analyst Course.")], width=10),
                            ],
                            direction="horizontal",
                        )
                    ]
                ),
                dbc.CardBody(
                    [
                        dcc.Markdown('''
                            ### Cyclistic Case Study: Unlocking User Insights for Strategic Growth
                            The Cyclistic Case Study is a comprehensive exploration into the user data of a fictional rideshare company, Cyclistic.
                            This Google Data Analysis Capstone Project aims to uncover valuable insights about user behavior patterns and devise a strategic approach for converting casual users into subscribing members.
                            Through meticulous data analysis this study unveils key findings that can reshape the company's operational and marketing strategies:
                            
                            #### Uncovering User Behavior Patterns
                            The study delves deep into the user data, identifying distinct patterns and trends in how customers interact with the Cyclistic platform. 
                            This includes understanding the preferences and usage habits of both casual and annual members. 
                            
                            #### Identifying Conversion Opportunities
                            By analyzing the factors that drive user engagement and loyalty, the study pinpoints the most promising opportunities for converting casual riders into subscribing members.
                            This information can inform targeted marketing campaigns and product enhancements to better meet the needs of the target audience. 
                            
                            #### Informing Strategic Decision-Making
                            The insights gathered from this comprehensive analysis provide a solid foundation for Cyclistic to make data-driven decisions.
                            This can lead to the development of more effective operational and marketing strategies, strengthening the company's position in the competitive rideshare market. 
                            
                        '''),
                    ]
                ),
                dbc.CardFooter(
                    [
                        dcc.Markdown(
                            """
                            [Capstone Project Description](assets/cyclistic/ProjectDescription.html)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
                            [Final Report](assets/cyclistic/2022_viz.html)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
                            [PowerPoint Presentation](https://github.com/AlexanderFastner/Cyclystic_Case_Study/blob/main/Cyclistic%20presentation.pptx)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
                            [Project Github Repo (R code here)](https://github.com/AlexanderFastner/Cyclystic_Case_Study)
                            """
                        )
                    ]
                ),
            ],
        ),
    ]
)

figures = html.Div([
    html.H2("Figures from the Analysis"),
    dbc.Card([
        dbc.CardHeader("Ride length Breakdown for Members vs. Casual Users"),
        dbc.CardImg(src=dash.get_asset_url("cyclistic/images/compared_stacked_bar.png"), className="w-100"),
    ]),
    dbc.Card([
        dbc.CardHeader("Comparative Daily Usage"),
        dbc.CardImg(src=dash.get_asset_url("cyclistic/images/comparative_daily_usage.png"), className="w-100"),
    ]),
    dbc.Card([
        dbc.CardHeader("Distribution of ride duration for Members vs. Casual Users"),
        dbc.CardImg(src=dash.get_asset_url("cyclistic/images/ride_duration_distribution.png"), className="w-100"),
    ]),
    dbc.Card([
        dbc.CardHeader("Monthly Usage breakdown"),
        dbc.CardImg(src=dash.get_asset_url("cyclistic/images/monthly_usage.png"), className="w-100"),
    ]),
]),
#-----------------------------------------------------------
layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(about, width=6),
                dbc.Col(figures, width=6),
            ]
        )
    ]
)
#-----------------------------------------------------------