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
       return flask.render_template('home.html')

@app.route('/regulations')
def regs():
       output = Markup(usdaDivs[:])
       return flask.render_template('regulations.html',output=output)
       
@app.route('/AgCompanies')
def coms():
       return flask.render_template('AgCompanies.html')
       
@app.route('/farmerportal')
def farmerportal():
       return flask.render_template('farmerportal.html')

@app.route('/workerportal')
def workerportal():
       return flask.render_template('workerportal.html')
       
@app.route('/workerComp')
def workercomp():
       return flask.render_template('workerComp.html')
       
@app.route('/equipment')
def equipment():
       equipmentList = ["Tractors", "Cultivator", "Harrow", "Subsoiler", "Plough"]
       equipmentNumAvailability = [5, 5, 3, 4, 10]
       equipmentMaxHours = 10
       equipmentCurrentRenters = "N/A"
       return flask.render_template(
              "equipment.html",
              equipmentList = equipmentList[:],
              equipmentNumAvailability = equipmentNumAvailability[:],
              equipmentMaxHours = equipmentMaxHours,
              equipmentCurrentRenters = equipmentCurrentRenters
              )

app.run(
       host = os.getenv('IP','0.0.0.0'),
       port = int(os.getenv('PORT', 8080)))