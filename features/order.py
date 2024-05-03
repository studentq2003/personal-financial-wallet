from datetime import datetime


def get_date(x, format="%d.%m.%Y"):
    return datetime.strptime(x.get("history_date"), format)


def order_date(data, state):
    ordered_data = sorted(data, key=lambda x: (x["date"], x["time"]), reverse=state)
    return ordered_data


def order_value(data, state):
    ordered_data = sorted(data, key=lambda x: (x["value"]), reverse=state)
    return ordered_data
