import datetime


def calculate_result(request_dict):
    savings_targets = request_dict.get('savings_targets', [])
    if len(savings_targets) == 0:
        return []
    savings_day_of_month = 1
    # Put savings targets in order so we can create an accumulated target to hit
    sorted_targets = sorted((target['date'], float(target['amount'])) for target in savings_targets)
    last_date = datetime.datetime.strptime(sorted_targets[-1][0], "%Y-%m-%d")
    last_date = datetime.date(last_date.year, last_date.month, last_date.day)
    todays_date = datetime.date.today()

    savings_dates = list(get_first_of_the_month_generator(todays_date, last_date))

    running_amount = 0
    running_amounts = []
    
    for date, amount in sorted_targets:
        running_amount += amount

    monthly_savings = running_amount / len(savings_dates)

    return [{"date": date.strftime("%Y-%m-%d"), "amount": int(monthly_savings)} for date in savings_dates]


def get_next_first_day_of_month(dt):
    for i in range(31):
        date = dt + datetime.timedelta(days=i)
        if date.day == 1:
            return date


def get_first_of_the_month_generator(start_date, end_date):
    while(True):
        next_first = get_next_first_day_of_month(start_date)
        if next_first > end_date:
            return
        yield next_first
        start_date = next_first + datetime.timedelta(days=1)
