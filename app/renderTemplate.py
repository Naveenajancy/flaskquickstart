
from flask import Flask

app = Flask(__name__)
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest