import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'



@app.route('/api')
def form():
    dummy_results = {}
    return dummy_results