from flask import Flask
from markupsafe import escape
from flask import url_for
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, World newer version </p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {'<b> Sam </b>'}!"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

