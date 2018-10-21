from flask import Flask, url_for, Response
from flask import request
import sys
import json
from flask_heroku import Heroku
import os.path

app = Flask( __name__ )
heroku = Heroku(app)
button = "disarmed"

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)


@app.route("/control")
def bOn():
	button = request.args.get('button')
	db  = open("db", "w")
	db.write(button)
	db.close()
	return "received"

@app.route("/")
def hello():
	content = get_file('index2.html')
	return Response(content, mimetype="text/html")

@app.route("/state")
def state():
	db  = open("db", "r")
	text = db.read()
	db.close()
	return text

if __name__ == '__main__':
	db = open("db", "w")
	db.write("disarmed")
	db.close()
	app.run()


# from flask import Flask
# app = Flask(__name__)
 
# @app.route("/")
# def hello():
#     return "Hello World!"
 
# if __name__ == "__main__":
#     app.run()