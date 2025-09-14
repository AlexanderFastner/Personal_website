#This is the main landing page of my Website/Blog area
#-----------------------------------------------------------
import os
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback

from assets.blog.blog_cards import blog_posts

print(os.getcwd())
#----------------------------------------------------------
dash.register_page(__name__, path="/")
#-----------------------------------------------------------
#shark = "general/shark.jpg"
profile_picture = "general/profile_picture.png"
DNA_graphic = "general/DNA_graphic.png"
#-----------------------------------------------------------
cards = []
# #Shark banner
# dbc.Col(
#     html.Img(src=dash.get_asset_url(shark), height="400px", width="600px"),
# ),
#-----------------------------------------------------------
#Add to Blog
#1 write actual blog page and text
#2 title, date, blurb, image (optional), link -- for Home Page Card
#-----------------------------------------------------------

#TODO add content
    #TODO add NLR work and publication here!
    #TODO add the AWS Certification
    #TODO add the ardunio Project post here too
#TODO add a way to write and edit these posts through a mobile app -- so I am more likely to do it

#TODO get card content from utils on startup

# @callback(
#     Output(dcc.Store(id='blog-posts'), 'data'), 
#     Input(dcc.Store(id='blog-posts'), 'data')
# )
def preprocess_blog_posts():
    """
    Generates a list of blog post cards.

    Args:
        blog_posts: A list of dictionaries representing blog posts.

    Returns:
        A list of dbc.Card objects.
    """
    for blog_post in blog_posts: #Stored in assests/blog_posts
        if 'image' in blog_post and blog_post['image']:  # Check if 'image' key exists and is not empty
            card_content = [
                html.H3(blog_post['title']),
                html.P(f"{blog_post['date']}"),
                html.Img(src=blog_post['image'], className="img-fluid mb-2"),
                html.P(blog_post['content'][:150] + "...", className="text-muted"),
                dbc.Button("Read More", color="primary", href=f"/post/{blog_posts.index(blog_post)}")
            ]
        else:
            card_content = [
                html.H3(blog_post['title']),
                html.P(f"{blog_post['date']}"),
                html.P(blog_post['content'][:150] + "...", className="text-muted"),
                dbc.Button("Read More", color="primary", href=f"/post/{blog_posts.index(blog_post)}")
            ]
        cards.append(dbc.Card(card_content, className="mb-4"))

        print(cards)        
    return html.Div(cards)
#-----------------------------------------------------------
# Define the layout
layout = html.Div(
    [
        html.H1("My Awesome Blog", className="text-center my-4"),
        # Blog Posts Section
        dbc.Row(
            [
            dbc.Col(
                    [
                        dcc.Store(id='blog-posts', data=blog_posts)
                    ], md=6
                )
        ], className="mb-4") 
    ]
)

#-----------------------------------------------------------


