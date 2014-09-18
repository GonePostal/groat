import os
from flask import Flask, jsonify, request
import pymongo
import db
import calculation

collection_name = 'money_calc'

app = Flask(__name__, static_folder='front_end/static', static_url_path='')


@app.route('/')
def route_index():
    return app.send_static_file('form.html')


@app.route('/design')
def route_design():
    return app.send_static_file('design.html')


@app.route('/experiment')
def route_experiment():
    return app.send_static_file('experiment.html')


@app.route('/monthly_sample.json', methods=['GET', 'POST'])
def form():
    request_json = request.get_json()
    result_json = calculation.calculate_result(request_json)
    result_dict = db.store_results(request.args, request_json, result_json, collection_name)
    return jsonify(**result_dict)

