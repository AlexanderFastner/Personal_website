#This is a page detailing my work on Cyclistic_Case_Study
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/Cyclistic_Case_Study")
#-----------------------------------------------------------
layout = (
    html.Div(
        #style={"display": "flex", "justify-content": "center"},
        [

            dbc.Stack(
                [
                    dbc.Col([html.Img(src=dash.get_asset_url("cyclistic/images/Cyclistic_logo.png"), height="100px", width="100px")], width="100px"),
                    dbc.Col([html.H1("My Capstone Case Study as part of the Google Data Analyst Course.")], width=10),
                ],
                direction="horizontal",
            ),

            dbc.Row(
                dbc.Col(
                    [
                        html.Br(),
                        
                        #TODO move logo and title into the card
                        #TODO styling
                        #TODO footer of card 1 is the links
                            #TODO links into listgroup 
                            #dbc.ListGroup(
                            #     [
                            #         dbc.ListGroupItem("Item 1"),
                            #         dbc.ListGroupItem("Item 2"),
                            #         dbc.ListGroupItem("Item 3"),
                            #     ],
                            #     flush=True,
                            #),
                        #TODO make seperate card for the figures
                        #https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/

                        dbc.Card(
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
                                    #Include links to the prompt 
                                    html.A("Capstone Project Description", href="assets/cyclistic/ProjectDescription.html", target="_blank"),
                                    html.Br(),
                                    #the final report .hmtl
                                    html.A("Final Report", href="assets/cyclistic/2022_viz.html", target="_blank"),
                                    html.Br(),
                                    #Powerpoint Presentation 
                                    dbc.CardLink("PowerPoint Presentation", href="https://github.com/AlexanderFastner/Cyclystic_Case_Study/blob/main/Cyclistic%20presentation.pptx"),
                                    html.Br(),
                                    #Repo Link
                                    dbc.CardLink("Project Github Repo (R code here)", href="https://github.com/AlexanderFastner/Cyclystic_Case_Study"),
                                    html.Br(),
                                    html.Br(),
                                    html.H2("Figures from the analysis"),
                                    html.Br(),
                                    #include some images
                                    html.H3("Ride length Breakdown for Members vs. Casual Users"),
                                    html.Img(src=dash.get_asset_url("cyclistic/images/compared_stacked_bar.png"), height="500px", width="1200px"),
                                    html.Br(),
                                    html.H3("Comparative Daily Usage"),
                                    html.Img(src=dash.get_asset_url("cyclistic/images/comparative_daily_usage.png"), height="500px", width="800px"),
                                    html.Br(),
                                    html.H3("Distribution of ride duration for Members vs. Casual Users"),
                                    html.Img(src=dash.get_asset_url("cyclistic/images/ride_duration_distribution.png"), height="500px", width="1200px"),
                                    html.Br(),
                                    html.H3("Monthly Usage breakdown"),
                                    html.Img(src=dash.get_asset_url("cyclistic/images/monthly_usage.png"), height="500px", width="1200px"),
                                    html.Br(),


                                    
                                ]
                            ),
                            style={"width": "60%"},
                        ),
                        
                    ],
                )
            )
        ]
    )
)
#-----------------------------------------------------------