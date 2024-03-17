#The main app to run the frontend webpage
#-----------------------------------------------------------
import os
import dash
import dash_bootstrap_components as dbc
from flask import Flask
#-----------------------------------------------------------
FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)

server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    title="Alexander Roman Fastner",
    external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME],
    requests_pathname_prefix=os.getenv("SUBDOMAIN", "/"),
    #background_callback_manager=background_callback_manager,
    use_pages=True,
)

app.config.suppress_callback_exceptions = True
#-----------------------------------------------------------
#Layout and Navigation
app.layout = dbc.Container()

#----------------------------------------------------------
if __name__ == "__main__":
    debug = os.getenv("DEBUG", "True") == "True"
    app.run_server(port=8020, debug=debug)
#----------------------------------------------------------