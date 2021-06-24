from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST Method successful"
    else:
        return "Get Method Suceesful"