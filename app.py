import flask
import os
from flask import Flask, render_template, request, redirect, url_for

app = flask.Flask(__name__)

num = 1
date = ""
time = ""
field = ""
action = ""
numWorkers = ""

#root or basic page
@app.route('/agcompanies')
def agcompanies():
       return flask.render_template('AgCompanies.html')

@app.route('/schedule')
def schedule():
       return flask.render_template('calendarPage.html')

@app.route('/addevent', methods = ['GET', 'POST'])
def addEvent():
       if request.method == "POST":
              date = request.form['date']
              time = request.form['time']
              print date
              print time
              field = request.form['field']
              action = request.form['action']
              numWorkers = request.form['numWorkers']
              
              num = num + 1
              return redirect(url_for('calendarPage.html', date=date , time=time , field=field , action=action , numWorkers=numWorkers, num=num))
       return flask.render_template('addevent.html')
       

app.run(
       host = os.getenv('IP','0.0.0.0'),
       port = int(os.getenv('PORT', 8080)),
       debug = True)