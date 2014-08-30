import os
from flask import Flask, jsonify, request
import pymongo

MONGODB_URI = os.environ.get('MONGOHQ_URL', "")
client = pymongo.MongoClient(MONGODB_URI)
db = client.db
money_calc = db.money_calc

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/api.json', methods=['GET', 'POST'])
def form():
    result_dict = {"data":get_dummy_data(),
                     "request_args":request.args,
                     "request_json":request.get_json(force=True),
                     "mongo_debug":{"MONGODB_URI":MONGODB_URI,
                                    "collection_object":str(money_calc),
                                    "previous_collection_count":money_calc.count(),
                                    }
                    }
    money_calc.insert(result_dict)
    result_dict['_id'] = str(result_dict['_id'])
    return jsonify(**result_dict)

def get_dummy_data():
    return [{"date": "2014-07-01", "amount": 290},
            {"date": "2014-08-01", "amount": 210},
            {"date": "2014-09-01", "amount": 210},
            {"date": "2014-10-01", "amount": 140},
            {"date": "2014-11-01", "amount": 80},
            ]