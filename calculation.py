def calculate_result(request_json):
    savings_targets = request_json['savings_targets']
    if len(savings_targets) == 0:
        return []
    sorted_targets = sorted((target['date'], float(target['amount'])) for target in savings_targets)
    last_date = sorted_targets[-1][0]
    
    running_ammount = 0
    running_ammounts = []
    
    for date, ammount in sorted_targets:
        running_ammount += ammount
        running_ammounts.append((date, running_ammount))
    return [{"date": date, "amount": amount} for date, amount in running_ammounts]