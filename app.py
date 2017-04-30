import flask
from flask import Markup
import os
from webScraping import *

app = flask.Flask(__name__)
output = []
usdaDivs = [str(item).replace('\n','') for item in usdaDivs]
usdaDivs = [str(item).replace('\t','') for item in usdaDivs]
usdaDivs = [str(item).replace('\xc2','') for item in usdaDivs]
usdaDivs = [str(item).replace('\xa0','') for item in usdaDivs]

#root or basic page
@app.route('/')
def root():
       return flask.render_template('AgCompanies.html')

@app.route('/regulations')
def regs():
       output = Markup(usdaDivs[:])
       return flask.render_template('regulations.html',output = output[:])

app.run(
       host = os.getenv('IP','0.0.0.0'),
       port = int(os.getenv('PORT', 8080)),
       debug = True)