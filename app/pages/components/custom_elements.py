#This is a page to hold custom standardized html/dbc/dcc elements to use across this page
import dash
from dash import dcc, html
#-----------------------------------------------------------
# custom_hr = html.Hr(
#     style={
#         "borderWidth": "0.5vh",
#         "width": "100%",
#         "borderColor": "#F3DE8A",
#         "opacity": "unset",
#     }
# )
custom_hr = html.Hr(
    style={
        "border": "none",
        "height": "0.5vh",
        "width": "100%",
        "background": "linear-gradient(to right in hsl, #00CC00, #0066FF)",
        # "margin": "1em 0",
    }
)
#-----------------------------------------------------------
#TEST
# custom_header = html.H1("My Custom Header", style={"color": "blue"})