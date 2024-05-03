from datetime import datetime


def get_date(x, format="%d.%m.%Y"):
    return datetime.strptime(x.get("history_date"), format)


def order(data):
    # ordered_data = sorted(data,  key = lambda measure: measure['date'], reverse=True)
    # ordered_time = sorted(ordered_data, key = lambda measure: measure['time'])
    ordered_data = sorted(data, key=lambda x: (x["date"], x["time"]), reverse=True)
    return ordered_data
