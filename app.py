from flask import Flask, logging, render_template
import logging
import requests

app = Flask(__name__)

# Epic Oauth Connectivity
FHIR_SERVER_URL = "http://157.245.79.105:8080/fhir"

# SMART config
FHIR_AUTH_URL = "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/authorize"
FHIR_TOKEN_URL = "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token"
FHIR_API_URL = "https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4/"
CLIENT_ID = "ffb905d2-f94d-4cb5-a29c-0b048275f662"
REDIRECT_URI = "http://localhost:5000/Home"
SCOPES = "patient/launch,patient/Goal.write,patient/Goal.read,patient/Goal.search,patient/Observation.search,patient/Observation.read,patient/Observation.write,patient/Patient.read"

FHIR_AUTH_URL2 = "https://keycloak.testphysicalactivity.com/realms/physical_activity/protocol/openid-connect/auth"
FHIR_TOKEN_URL2 = "https://keycloak.testphysicalactivity.com/realms/physical_activity/protocol/openid-connect/token"
FHIR_API_URL2 = "https://fhir.testphysicalactivity.com/fhir/"
CLIENT_ID2 = "physical_activity"
REDIRECT_URI2 = "http://localhost:5000/call-back"
SCOPES2 = "patient/Patient.read"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/launch')
def launch():
    return ""

@app.route('/launch2')
def launch2():
    return ""

@app.route('/epic')
def epic():
    return ""

@app.route('/listpatients')
def listpatients():
    return ""

@app.route('/reset')
def reset():
    return ''


if __name__ == '__main__':
    import flaskbeaker

    flaskbeaker.FlaskBeaker.setup_app(app)

    logging.basicConfig(level=logging.DEBUG)
    #    make_ssl_devcert("cert.pem", host="localhost")
    #    app.run(debug=True, port=8000, ssl_context=('cert.pem', 'key.pem'))
    app.run(debug=True, port=5000)
    
    
    