from datetime import datetime


def get_date(x, format="%d.%m.%Y"):
    return datetime.strptime(x.get("date"), format)


def order_date(data, state):
    ordered_data = sorted(
        data,
        key=lambda x: (datetime.strptime(x["date"], "%d-%m-%Y"), datetime.strptime(x["time"], "%H:%M")), reverse=state)
    return ordered_data


def order_value(data, state):
    ordered_data = sorted(data, key=lambda x: (int(x["value"])), reverse=state)
    return ordered_data
