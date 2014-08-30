from calculation import calculate_result


dummy_request_json = {
  "savings_targets": [{"name": "NY trip","amount": '120.00',"date": "2014-09-12"},
                      {"name": "New shoes","amount": '1500.00',"date": "2014-07-03"}
                     ],
  "existing_savings": '134.26',
  "session_id": "ae98-08c2-bd39-a167"
}

print(calculate_result(dummy_request_json))