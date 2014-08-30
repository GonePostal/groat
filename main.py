import os
from flask import Flask, jsonify, request
import pymongo
from db import store_results
from calculation import calculate_result

collection_name = 'money_calc'

app = Flask(__name__, static_folder='front_end/static', static_url_path='')


@app.route('/')
def route_index():
    return app.send_static_file('index.html')


@app.route('/form')
def route_form():
    return app.send_static_file('form.html')


dummy_request_json = {
  "savings_targets": [{"name": "NY trip","amount": 120.00,"date": "2014-09-12"},
                      {"name": "New shoes","amount": 1500.00,"date": "2014-11-03"}
                     ],
  "existing_savings": 134.26,
  "session_id": "ae98-08c2-bd39-a167"
}


@app.route('/monthly_sample.json', methods=['GET', 'POST'])
def form():
    request_json = request.get_json()
    result_json = calculate_result(dummy_request_json)
    result_dict = store_results(request.args, request_json, result_json, collection_name)
    return jsonify(**result_dict)

