# flaskquickstart
Learn about python Flask
A minimal Flask application
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

Let's understand the code flow:

    First we imported the Flask class. An instance of this class will be our WSGI application.

    Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

    We then use the path/endpoint/route() decorator to tell Flask what URL should trigger our function.

    The function helloe_world returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.
