import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'



@app.route('/api', methods=['GET', 'POST'])
def form():
    print(request.args)
    dummy_results = {"data":[{"date": "2014-07-01", "amount": 290},
                             {"date": "2014-08-01", "amount": 210},
                             {"date": "2014-09-01", "amount": 210},
                             {"date": "2014-10-01", "amount": 140},
                             {"date": "2014-11-01", "amount": 80},
                             ],
                     "args":request.args,
                     "json":request.get_json(force=True)}
    return jsonify(**dummy_results)