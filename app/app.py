#The main app to run the frontend webpage
#-----------------------------------------------------------
import os
port = os.environ.get("PORT", 8020)
import sys
import dash
import dash_bootstrap_components as dbc
from flask import Flask
from pages.components.navbar import navbar
from pages.components.footer import create_footer

#-----------------------------------------------------------
print("Starting up Personal Website!", flush=True)
print("---------------------------------------------", flush=True)
sys.stdout.flush()
#-----------------------------------------------------------
FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)
#-----------------------------------------------------------
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
#TODO add Navigation
#TODO add footer

app.layout = dbc.Container(
    [
        navbar,
        dash.page_container,
        create_footer(),
    ], 
    style={'padding-bottom': '100px'},
    fluid=True,
)
#----------------------------------------------------------
if __name__ == "__main__":
    debug = os.getenv("DEBUG", "True") == "True"
    app.run_server(host='0.0.0.0', port=port, debug=debug)
#----------------------------------------------------------