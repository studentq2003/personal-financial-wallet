def order_date(data, state):
    ordered_data = sorted(data, key=lambda x: (x["date"], x["time"]), reverse=state)
    return ordered_data


def order_value(data, state):
    ordered_data = sorted(data, key=lambda x: (x["value"]), reverse=state)
    return ordered_data
