#This holds the navigation bar
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from dash import html, callback
from dash.dependencies import Input, Output, State
#-----------------------------------------------------------

#TODO make top navivation tab bar with about me, portfolio, contact info, resume/CV, get in touch (email, linkedin)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        #TODO make custom logo of some sort
                        # dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        #TODO adjust font and styles
                        dbc.Col(dbc.NavbarBrand("Alexander Fastner", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("About Me", href="/about")),
                        dbc.NavItem(dbc.NavLink("Portfolio", href="/portfolio")),
                        # dbc.NavItem(dbc.NavLink("Resume/CV", href="/resume")),
                        dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
                    ],
                    className="ms-auto",
                    navbar=True
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)

#-----------------------------------------------------------
#Callbacks
#-----------------------------------------------------------
# add callback for toggling the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

#-----------------------------------------------------------
