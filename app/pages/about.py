#This is a page About Me
#-----------------------------------------------------------
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
#-----------------------------------------------------------
dash.register_page(__name__, path="/about")
#-----------------------------------------------------------
profile_picture = "general/profile_picture.png"
#-----------------------------------------------------------

about = html.Div([
    #TODO break this up into non markdown components SO I can style inline
    #TODO Add other images of me to click through?
    #TODO add tum and LMU logos

    dbc.Card(
        dbc.CardBody(
            dcc.Markdown(
                '''
                ## About  Me:
                
                In my free time, I immerse myself in a variety of engaging hobbies that keep my mind active and satisfy my sense of adventure.
                One of my greatest passions is diving, where I explore the serene underwater world, discovering vibrant marine ecosystems and 
                experiencing the peaceful weightlessness that only exists beneath the waves. 
                When I'm not underwater, I pour my creative energy into various tech projects that challenge my problem-solving skills and 
                keep me constantly learning something new.

                One aspect of programming that has always interested me, but never came up in my studies, was embedded Programming.
                I've recently enjoyed learning soldering and tinkering with an Arduino board to create a custom physical volume control for my PC.
                
                Another project I've wanted to work on is to make my own app. To this end I took an Android development course
                and began on designing a mobile version of the game machine strike. This is a board stategy game similar to chess, and I 
                continuosly work on it in my free time getting it closer and closer to a playable version.
                
                The versatile Raspberry Pi has become another favorite platform for my experiments. Most recently I want to set it up as a web host for this site.
                Figuring out the ins and outs of the OS as well as setting up networking, security and port forwarding was quite the interesting challenge. 
                From this I learned some valuable skills that I can continue to use for various projects in the future.

                All of these projects along with many others are linked in my portfolio.
                
                ### Education
                I am a Bay Area native who pursued higher education in Germany, by leveraging my dual citizenship and German language proficiency.
                In Munich I began on my Bachelors in Bioinformatics in 2022 in a program shared between the two large universities in Munich.

                [Technical University of Munich](https://www.tum.de/en/)

                [Ludwig-Maximilians-Universitaet](https://www.lmu.de/en/)
                
                #### **Bioinformatics Bachelor (TUM/LMU)**: Search for evidence of recombination in Alternaria solani using genomic tools 
                    
                The fungal pathogen Alternaria solani is known to cause early blight in tomatoes and potatoes and causes millions in economic losses every year. 
                In my thesis I use genomic tools (LDHelmet, clonalframeML) to analyze data from 48 isolates and search for evidence that the genomic variation we 
                see across isolates is caused by an unknown sexual reproduction phase as opposed to asexual reproduction. 
                In addition to the two above mentioned tools the data was cleaned, and pre-processed in bash. Then the resulting output was visualized in R.
                I went on to continue this work as research assistant for Prof. Stam at the Phytopathology chair at TUM and also later at Kiel University.

                
                #### **Bioinformatics Master (TUM/LMU + Helmholtz Institute)**: Bioinformatic Analysis of the role of MAFA in Stem Cell-Derived Human Pancreatic Islets
                
                In this research collaboration with (Theis Lab Helmholtz and Hebrok Lab TUM), I conducted a bioinformatics analysis focusing on Type 1 diabetes
                and stem cell-derived β cell maturation. Using Bulk RNA sequencing data from the Transcription Factor MAFA and its naturally occurring mutant 
                MAFAS64F cell lines, I employed various bioinformatics methods to identify differentially expressed genes, as well as Transcription Factors and
                Pathways of interest. Despite the limitations of the available bulkRNA data, my work established a solid foundation for future investigations
                into MAFA's role in β cell maturation and insulin production, contributing to the broader goal of developing stable, functional stem cell-derived
                β cells for potential Type 1 diabetes treatment. In the future my findings will serve as a comparison point for a single-cell RNAseq analysis.


                I completed my M.Sc. in 2024 and moved back to the United States to start my Career.
                If you are interested in my work, you can find more information on my linkedIn.                        
            '''),
        ),
    ),
])
#-----------------------------------------------------------
Picture_Card = dbc.Card(
    dbc.CardBody(
        [   
            dbc.Col(
                [
                html.Img(src=dash.get_asset_url(profile_picture), className="w-100"),
                html.Br(),
                dbc.CardLink("Linkedin", href="https://www.linkedin.com/in/alexander-fastner/"),
                html.Br(),
                dbc.CardLink("Github", href="https://github.com/AlexanderFastner"),
                html.Br(),
                html.Plaintext("Email: alexanderfastner@gmail.com"),
                ], style={'textAlign': 'right'}
            )
        ]
    ),
)
#-----------------------------------------------------------
cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(about, width=8),
                dbc.Col(Picture_Card, width=4),
            ]
        )
    ]
)
#-----------------------------------------------------------
layout = (
    [
        cards
    ]
)
#-----------------------------------------------------------
