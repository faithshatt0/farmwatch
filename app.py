import flask
from flask import Markup
import os
from webScraping import *
from webScrape import *

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
       
@app.route('/safety')
def safety():
       output = Markup(pennStateDiv[:])
       return flask.render_template('safety.html', output = output)
       
@app.route('/AgCompanies')
def coms():
       return flask.render_template('AgCompanies.html')
       
@app.route('/farmerportal')
def farmerportal():
       num = 1
       date = ["04/30/17", "05/01/17", "05/02/17", "05/03/17", "05/04/17", "05/05/17", "05/06/17"]  
       time = ["3pm", "12pm", "1pm", "4pm", "9am", "7am", "11am"]
       field = ["5","1","7","2","4","6","3"]
       action = ["Spray Pesticide", "Spray Water", "Thin Fields", "Tractor Day", "Manual Labor"]
       numWorkers = ["0","10","20","30","40"]
       return flask.render_template('farmerportal.html', date=date , time=time , field=field , action=action , numWorkers=numWorkers, num=num)
       
@app.route('/addevent', methods = ['GET', 'POST'])
def addEvent():
       return flask.render_template('addevent.html')
       
       
@app.route('/farmersconnect')
def farmersconnect():
       return flask.render_template('farmersconnect.html')

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

@app.route('/workerportal')
def workerportal():
       num = 1
       date = ["04/30/17", "05/01/17", "05/02/17", "05/03/17", "05/04/17", "05/05/17", "05/06/17"]  
       time = ["3pm", "12pm", "1pm", "4pm", "9am", "7am", "11am"]
       field = ["5","1","7","2","4","6","3"]
       action = ["Spray Pesticide", "Spray Water", "Thin Fields", "Tractor Day", "Manual Labor"]
       numWorkers = ["0","10","20","30","40"]
       return flask.render_template('workerportal.html', date=date , time=time , field=field , action=action , numWorkers=numWorkers, num=num)
       
@app.route('/workerComp')
def workercomp():
       return flask.render_template('workerComp.html')

@app.route('/availability')
def availability():
       return flask.render_template("availability.html")

app.run(
       host = os.getenv('IP','0.0.0.0'),
       port = int(os.getenv('PORT', 8080)))