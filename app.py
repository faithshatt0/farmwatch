import flask
import os
from flask import Flask, render_template, request, redirect, url_for

app = flask.Flask(__name__)

num = 1
date = []
time = []
field = []
action = []
numWorkers = []

#root or basic page
@app.route('/agcompanies')
def agcompanies():
       return flask.render_template('AgCompanies.html')

@app.route('/schedule')
def schedule():
       return flask.render_template('calendarPage.html', date=date , time=time , field=field , action=action , numWorkers=numWorkers, num=num)

@app.route('/addevent', methods = ['GET', 'POST'])
def addEvent():
       num = len(action)
       if request.method == "POST":
              date.append(request.form['date'])
              time.append(request.form['time'])
              field.append(request.form['field'])
              action.append(request.form['action'])
              numWorkers.append(request.form['numWorkers'])
              
              return redirect(url_for('schedule'))
       return flask.render_template('addevent.html')
       

app.run(
       host = os.getenv('IP','0.0.0.0'),
       port = int(os.getenv('PORT', 8080)),
       debug = True)