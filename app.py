import flask
import os

app = flask.Flask(__name__)

#root or basic page
@app.route('/')
def root():
       return flask.render_template('AgCompanies.html')

app.run(
       host = os.getenv('IP','0.0.0.0'),
       port = int(os.getenv('PORT', 8080)),
       debug = True)