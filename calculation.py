def calculate_result(request_dict):
    savings_targets = request_dict['savings_targets']
    if len(savings_targets) == 0:
        return []
    sorted_targets = sorted((target['date'], float(target['amount'])) for target in savings_targets)
    last_date = sorted_targets[-1][0]
    
    running_amount = 0
    running_amounts = []
    
    for date, amount in sorted_targets:
        running_amount += amount
        running_amounts.append((date, running_amount))
    return [{"date": date, "amount": amount} for date, amount in running_amounts]